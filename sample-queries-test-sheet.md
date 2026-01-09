# Sample Queries Test Sheet
## For EMEA Sales Command Center Agent Testing

Use this sheet to test your agent systematically. Check off queries as they work correctly.

---

## Category 1: Basic Deal Intelligence (MUST WORK)

### Simple List Queries
- [ ] "What are our top 10 EMEA deals by ARR?"
  - Expected: List of 10 opps, sorted by ARR descending, with account, ARR, stage, close date, owner

- [ ] "Show me our top 5 new business deals in EMEA"
  - Expected: Filtered to Type = "New Business", top 5 by ARR

- [ ] "What deals are closing this month?"
  - Expected: Opportunities with Close Date in January 2026

- [ ] "Show me all opportunities in the UK"
  - Expected: Filtered to UK accounts/territories

- [ ] "Find deals over $100K"
  - Expected: Filtered to ARR > $100,000

### Filtered Queries
- [ ] "Show me Commit deals closing next week"
  - Expected: Forecast = "Commit" AND Close Date = Jan 10-16, 2026

- [ ] "What Major Enterprise deals are in Stage 3 or later?"
  - Expected: Segment = "Major Enterprise" AND Stage >= 3

- [ ] "Show me all renewals closing in Q1"
  - Expected: Type = "Renewal" AND Close Date = Feb 1 - Apr 30, 2026

- [ ] "Find all opportunities owned by Sarah Mitchell"
  - Expected: Opportunity Owner = "Sarah Mitchell"

- [ ] "What deals in Germany are in Best Case?"
  - Expected: Country = "Germany" AND Forecast = "Best Case"

---

## Category 2: Performance Analysis (HIGH VALUE)

### Regional Comparisons
- [ ] "How is UK performing vs Germany this quarter?"
  - Expected: Side-by-side metrics (Closed Won, Pipeline, Attainment %) for both

- [ ] "Compare performance across all EMEA regions"
  - Expected: Table with UK, Germany, France, Nordics, etc. with key metrics

- [ ] "What's our total Closed Won ARR for EMEA this quarter?"
  - Expected: Sum of all Closed Won opportunities in Q4 FY26

### AE Performance
- [ ] "Show me the top 3 performing AEs by Closed Won ARR"
  - Expected: Ranked list of AEs with their Closed Won totals

- [ ] "Who are the bottom 3 AEs in pipegen this month?"
  - Expected: Check Google Sheets pipegen tracker, show bottom 3 with metrics

- [ ] "How is Sarah Mitchell performing vs her quota?"
  - Expected: Sarah's Closed Won vs target, with percentage

- [ ] "Show me pipegen performance for all AEs in December"
  - Expected: Pull from Google Sheets pipegen tracker for December 2025

### Segment Performance
- [ ] "How is the Velocity segment performing?"
  - Expected: Metrics for Velocity segment (total ARR, deal count, etc.)

- [ ] "Compare Emerging Enterprise vs Major Enterprise performance"
  - Expected: Side-by-side comparison of both segments

---

## Category 3: Risk & Health Analysis (WOW FACTOR)

### At-Risk Deals
- [ ] "Which Commit deals are at risk of slipping?"
  - Expected: Commit forecast deals with risk signals (stale, long stage duration, etc.)

- [ ] "Show me opportunities that haven't been updated in 2 weeks"
  - Expected: Last Modified Date > 14 days ago

- [ ] "What deals are stuck in Stage 2 for over 30 days?"
  - Expected: Stage = 2 AND stage duration > 30 days

- [ ] "Find deals that moved from Commit to Best Case this week"
  - Expected: Forecast category downgrade in last 7 days

### Churn & Renewals
- [ ] "Which renewals over $100K are at risk of churning in Q1?"
  - Expected: Type = "Renewal" AND ARR > $100K AND Q1 close AND churn signals

- [ ] "Show me all renewals closing in February"
  - Expected: Type = "Renewal" AND Close Date in Feb 2026

- [ ] "What's our total renewal ARR for next quarter?"
  - Expected: Sum of renewal opportunities closing Q1 2026

- [ ] "Find accounts with payment issues"
  - Expected: Check Slack/Salesforce for payment delinquency flags

---

## Category 4: Forecast & Pipeline (CRITICAL FOR LEE)

### Pipeline Coverage
- [ ] "What's our total pipeline for Q1 2026?"
  - Expected: Sum of all opportunities closing Q1 2026 by forecast category

- [ ] "What's our pipeline coverage ratio?"
  - Expected: (Total Pipeline ÷ Remaining Quota) calculation

- [ ] "How much is in Commit for this quarter?"
  - Expected: Sum of ARR where Forecast = "Commit" and Close Date in Q4 FY26

- [ ] "Show me forecast breakdown by segment"
  - Expected: Pipeline/Best Case/Commit totals for each segment

### Quota Tracking
- [ ] "Are we on track to hit our $5.6M quarterly target?"
  - Expected: Closed Won + Commit vs $5.6M target with percentage

- [ ] "How much quota do we have left to cover this quarter?"
  - Expected: $5.6M - Closed Won = remaining gap

- [ ] "What's our week-over-week pipeline change?"
  - Expected: Compare current week pipeline to last week

---

## Category 5: Account Intelligence (CONTEXTUAL)

### Account Lookup
- [ ] "Tell me about Deutsche Bank"
  - Expected: Account summary, opportunities, recent activity, Slack mentions

- [ ] "What's the status of the Unilever UK opportunity?"
  - Expected: Specific opportunity details with full context

- [ ] "Show me all opportunities for Siemens"
  - Expected: All opps associated with Siemens account (all subsidiaries)

- [ ] "Which accounts has Lee met with recently?"
  - Expected: Check calendar for Lee's recent meetings, show associated accounts

### Multi-Source Context
- [ ] "What have we discussed about Booking.com in Slack?"
  - Expected: Recent Slack messages mentioning Booking.com

- [ ] "Find accounts mentioned in #emea-sales this week"
  - Expected: Parse Slack messages for account names

- [ ] "What's the history of our largest deal?"
  - Expected: Timeline of changes, meetings, Slack discussions for top deal

---

## Category 6: Action Generation (PRACTICAL VALUE)

### Message Drafting
- [ ] "Draft a Slack message about our top 3 at-risk deals"
  - Expected: Formatted Slack message with emojis, bullets, links

- [ ] "Write an update on UK performance for Lee"
  - Expected: Executive summary suitable for Lee's review

- [ ] "Create a check-in message for the Unilever deal owner"
  - Expected: Personalized message with deal context

### Summaries & Reports
- [ ] "Summarize our Q4 performance"
  - Expected: Executive brief with key metrics and highlights

- [ ] "Give me talking points for the forecast call"
  - Expected: Bullet points on pipeline, commits, risks

- [ ] "What should I focus on in this week's churn save call?"
  - Expected: Top at-risk renewals with suggested strategies

---

## Category 7: Complex Multi-Filter Queries (ADVANCED)

- [ ] "Show me Major Enterprise renewals over $100K in Germany closing in Q1 that are in Commit forecast"
  - Expected: Multiple filters applied correctly

- [ ] "Find new business deals in Nordics owned by Anna Bergström in Stage 3+ closing before end of January"
  - Expected: All filters combined

- [ ] "What Velocity segment opportunities in UK were created this month and are in Best Case?"
  - Expected: Multiple filters on segment, region, create date, forecast

---

## Category 8: Edge Cases & Error Handling (ROBUSTNESS)

### Empty Results
- [ ] "Show me deals in Antarctica"
  - Expected: "No results found. EMEA includes [list of regions]. Did you mean...?"

- [ ] "Find opportunities closing in 1995"
  - Expected: "No results found. Did you mean a different date range?"

### Ambiguous Queries
- [ ] "How are we doing?"
  - Expected: Ask clarifying question ("Do you mean overall performance, a specific region, or...?")

- [ ] "Show me the big deals"
  - Expected: Ask clarification ("By 'big', do you mean over $100K, $500K, or top 10 by ARR?")

### Permission Issues (if testable)
- [ ] Ask user without Salesforce access to query deals
  - Expected: "You don't have access to Salesforce data. Contact your admin."

---

## Testing Process

For each query:
1. **Run the query** in the Glean agent
2. **Check accuracy**: Verify against manual Salesforce query or Google Sheet
3. **Check formatting**: Is the response clean, readable, properly formatted?
4. **Check sources**: Are Salesforce/Sheet links included and working?
5. **Check speed**: Did it respond in < 10 seconds?
6. **Check follow-ups**: Does it suggest relevant next questions?

---

## Scoring Your Agent

**MVP Ready (for AI Day demo):**
- ✅ 15+ queries working accurately
- ✅ Categories 1, 2, 3, 4 mostly working
- ✅ Fast responses (< 10 sec)
- ✅ Clean formatting
- ✅ Sources cited

**Production Ready:**
- ✅ 30+ queries working accurately
- ✅ All categories working
- ✅ Edge cases handled gracefully
- ✅ 95%+ accuracy vs manual queries
- ✅ User feedback positive

**Award-Winning Demo:**
- ✅ 40+ queries working
- ✅ Complex multi-filter queries work
- ✅ Action generation impressive
- ✅ Multi-source context synthesis
- ✅ Proactive suggestions
- ✅ Live demo flawless

---

## Demo-Day Priority Queries (MUST WORK PERFECTLY)

These are the queries you'll use in your live demo. Test them 10+ times each:

1. ⭐ "What are our top 5 new business deals in EMEA right now?"
2. ⭐ "Which of these deals has the highest risk of slipping?"
3. ⭐ "Draft a Slack message to check in with that AE"
4. ⭐ "How is UK performing vs Germany this quarter?"
5. ⭐ "Show me the bottom 3 AEs in pipegen this month"
6. ⭐ "Which renewals over $100K are at risk of churning in Q1?"
7. ⭐ "Summarize the [Account Name] situation for Lee"

**Practice these until they work perfectly every time.**

---

## Troubleshooting Log

As you test, track issues here:

| Query | Issue | Fix Applied | Resolved? |
|-------|-------|-------------|-----------|
| "Top 10 deals" | Returned global, not EMEA | Added "Always filter to EMEA" to prompt | ✓ |
| "UK vs Germany" | Couldn't find data | Clarified region definitions | ✓ |
| | | | |

---

## Success Metrics

Track these as you test:

- **Accuracy rate**: ____ / ____ queries correct (target: 90%+)
- **Avg response time**: _____ seconds (target: < 10 sec)
- **Source citation rate**: ____% (target: 100%)
- **Formatting quality**: _____ / 5 (target: 4+)

---

Good luck with testing! 🚀
