#!/usr/bin/env python3
"""Generate EMEA sales report with chart and Slack-formatted text."""

import csv
import os
from datetime import datetime, timedelta
from collections import defaultdict
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# Configuration
CSV_FILE = '/home/user/Demo/emea-sales-report/emea_deals.csv'
OUTPUT_DIR = '/home/user/Demo/emea-sales-report/output'
QUARTERLY_TARGET = 5_600_000  # $5.6M target

# Current quarter boundaries (Q4 2025: Oct 1 - Dec 31)
Q_START = datetime(2025, 10, 1)
Q_END = datetime(2025, 12, 31)


def parse_currency(value):
    """Parse currency string to float."""
    if not value:
        return 0.0
    # Remove $, commas, and whitespace
    cleaned = value.replace('$', '').replace(',', '').strip()
    try:
        return float(cleaned)
    except ValueError:
        return 0.0


def parse_date(date_str):
    """Parse date string to datetime."""
    if not date_str:
        return None
    try:
        # Handle format like "10/1/2025"
        return datetime.strptime(date_str.strip(), '%m/%d/%Y')
    except ValueError:
        try:
            # Try alternate format
            return datetime.strptime(date_str.strip(), '%Y-%m-%d')
        except ValueError:
            return None


def get_week_number(date, q_start):
    """Get week number within the quarter (1-based)."""
    if date < q_start:
        return 0
    delta = date - q_start
    return (delta.days // 7) + 1


def load_deals(csv_file):
    """Load deals from CSV file."""
    deals = []
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            deals.append(row)
    return deals


def analyze_deals(deals):
    """Analyze deals and return weekly aggregations."""
    closed_won_by_week = defaultdict(float)
    closed_won_deals = []
    pipeline_deals = []

    for deal in deals:
        stage = deal.get('Stage', '').strip()
        close_date = parse_date(deal.get('Close Date', ''))
        new_arr = parse_currency(deal.get('New ARR', ''))

        if not close_date:
            continue

        # Check if within current quarter
        if close_date < Q_START or close_date > Q_END:
            continue

        if stage == 'Closed Won':
            week = get_week_number(close_date, Q_START)
            closed_won_by_week[week] += new_arr
            closed_won_deals.append({
                'account': deal.get('Account Name', ''),
                'opportunity': deal.get('Opportunity Name', ''),
                'owner': deal.get('Opportunity Owner', ''),
                'arr': new_arr,
                'close_date': close_date,
                'type': deal.get('Type', '')
            })
        elif stage in ['Commit', 'Best Case', 'Pipeline']:
            pipeline_deals.append({
                'account': deal.get('Account Name', ''),
                'opportunity': deal.get('Opportunity Name', ''),
                'owner': deal.get('Opportunity Owner', ''),
                'arr': new_arr,
                'close_date': close_date,
                'stage': stage,
                'forecast': deal.get('Forecast Category', ''),
                'type': deal.get('Type', '')
            })

    return closed_won_by_week, closed_won_deals, pipeline_deals


def generate_chart(closed_won_by_week, output_path):
    """Generate weekly cumulative progress chart."""
    # Get all weeks up to current week
    today = datetime.now()
    current_week = min(get_week_number(today, Q_START), 13)  # Max 13 weeks in quarter

    weeks = list(range(1, current_week + 1))

    # Calculate cumulative totals
    cumulative = []
    running_total = 0
    for week in weeks:
        running_total += closed_won_by_week.get(week, 0)
        cumulative.append(running_total)

    # Create chart
    fig, ax = plt.subplots(figsize=(10, 6))

    # Week labels
    week_labels = [f'W{w}' for w in weeks]

    # Plot bars
    bars = ax.bar(week_labels, cumulative, color='#4A90D9', edgecolor='white', linewidth=0.5)

    # Add target line
    ax.axhline(y=QUARTERLY_TARGET, color='#E74C3C', linestyle='--', linewidth=2, label=f'Target: ${QUARTERLY_TARGET/1_000_000:.1f}M')

    # Format y-axis as currency
    def currency_formatter(x, pos):
        if x >= 1_000_000:
            return f'${x/1_000_000:.1f}M'
        elif x >= 1_000:
            return f'${x/1_000:.0f}K'
        else:
            return f'${x:.0f}'

    ax.yaxis.set_major_formatter(mticker.FuncFormatter(currency_formatter))

    # Add value labels on bars
    for bar, val in zip(bars, cumulative):
        height = bar.get_height()
        ax.annotate(f'${val/1_000_000:.2f}M',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=8)

    # Styling
    ax.set_xlabel('Week', fontsize=12)
    ax.set_ylabel('Cumulative Closed Won ARR', fontsize=12)
    ax.set_title('EMEA Q4 2025 - Weekly Cumulative Progress', fontsize=14, fontweight='bold')
    ax.legend(loc='upper left')
    ax.set_ylim(0, max(QUARTERLY_TARGET * 1.1, max(cumulative) * 1.1 if cumulative else QUARTERLY_TARGET))

    # Grid
    ax.yaxis.grid(True, linestyle='--', alpha=0.7)
    ax.set_axisbelow(True)

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()

    return cumulative[-1] if cumulative else 0


def generate_slack_message(closed_won_deals, pipeline_deals, total_closed):
    """Generate Slack-formatted message."""
    lines = []

    # Header
    lines.append("*:chart_with_upwards_trend: EMEA CQ Update*")
    lines.append("")

    # Progress summary
    pct_to_target = (total_closed / QUARTERLY_TARGET) * 100
    lines.append(f"*Progress to Target:* ${total_closed:,.0f} / ${QUARTERLY_TARGET:,.0f} ({pct_to_target:.1f}%)")
    lines.append("")

    # Closed Won section
    lines.append("*:white_check_mark: Closed Won This Quarter:*")
    if closed_won_deals:
        # Sort by ARR descending
        sorted_deals = sorted(closed_won_deals, key=lambda x: x['arr'], reverse=True)
        for deal in sorted_deals[:10]:  # Top 10
            deal_type = f" ({deal['type']})" if deal['type'] else ""
            lines.append(f"• {deal['account']} - ${deal['arr']:,.0f}{deal_type}")
    else:
        lines.append("• No closed won deals yet")
    lines.append("")

    # Pipeline section - Commit deals
    commit_deals = [d for d in pipeline_deals if d['forecast'] == 'Commit']
    if commit_deals:
        lines.append("*:dart: Commit Deals:*")
        sorted_commits = sorted(commit_deals, key=lambda x: x['arr'], reverse=True)
        for deal in sorted_commits[:5]:
            lines.append(f"• {deal['account']} - ${deal['arr']:,.0f} (Close: {deal['close_date'].strftime('%m/%d')})")
        lines.append("")

    # Top Renewals
    renewals = [d for d in pipeline_deals if 'Renewal' in d.get('type', '')]
    if renewals:
        lines.append("*:arrows_counterclockwise: Top Renewals:*")
        sorted_renewals = sorted(renewals, key=lambda x: x['arr'], reverse=True)
        for deal in sorted_renewals[:5]:
            lines.append(f"• {deal['account']} - ${deal['arr']:,.0f}")
        lines.append("")

    return '\n'.join(lines)


def main():
    """Main entry point."""
    # Create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Check if CSV exists
    if not os.path.exists(CSV_FILE):
        print(f"Error: CSV file not found at {CSV_FILE}")
        print("Please save your exported CSV data to this location.")
        return

    print("Loading deals from CSV...")
    deals = load_deals(CSV_FILE)
    print(f"Loaded {len(deals)} deals")

    print("Analyzing deals...")
    closed_won_by_week, closed_won_deals, pipeline_deals = analyze_deals(deals)

    print(f"Found {len(closed_won_deals)} Closed Won deals in Q4 2025")
    print(f"Found {len(pipeline_deals)} pipeline deals")

    # Generate chart
    chart_path = os.path.join(OUTPUT_DIR, 'emea_progress_chart.png')
    print(f"Generating chart: {chart_path}")
    total_closed = generate_chart(closed_won_by_week, chart_path)

    # Generate Slack message
    slack_msg = generate_slack_message(closed_won_deals, pipeline_deals, total_closed)

    # Save Slack message
    slack_path = os.path.join(OUTPUT_DIR, 'slack_message.txt')
    with open(slack_path, 'w') as f:
        f.write(slack_msg)

    print(f"\nSlack message saved to: {slack_path}")
    print("\n" + "="*60)
    print("SLACK MESSAGE (copy/paste this):")
    print("="*60)
    print(slack_msg)
    print("="*60)
    print(f"\nChart saved to: {chart_path}")


if __name__ == '__main__':
    main()
