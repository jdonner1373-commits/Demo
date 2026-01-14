# How to Build the EMEA Sales Command Center Glean Agent
## Step-by-Step Implementation Guide

---

## Overview

Building a Glean agent involves:
1. Setting up data source connections
2. Configuring the agent in Glean's interface
3. Writing prompts and instructions
4. Testing with real queries
5. Iterating based on results
6. Deploying for users

**Time estimate**: 6-12 hours for MVP (spread over 2-3 days)

---

## Prerequisites

### Access Required
- [ ] Glean workspace admin access (or work with your Glean admin)
- [ ] Salesforce API access (or work with Salesforce admin)
- [ ] Google Workspace admin access for Sheets/Drive
- [ ] Slack workspace permissions

### Information to Gather
- [ ] Salesforce instance URL (e.g., amplitude.my.salesforce.com)
- [ ] Google Sheet IDs for your trackers
- [ ] List of Slack channels to index
- [ ] Sample questions you want the agent to answer (20-30 examples)

---

## Phase 1: Connect Data Sources (2-3 hours)

### Step 1.1: Connect Salesforce to Glean

**Option A: If Salesforce is already connected to Glean workspace**
1. Log into Glean admin console
2. Go to **Settings** → **Datasources**
3. Check if Salesforce is listed and showing "Connected"
4. If yes, verify it's indexing the objects you need:
   - Opportunities
   - Accounts
   - Contacts
   - Forecasts
   - Activities

**Option B: If you need to connect Salesforce**
1. In Glean admin console: **Settings** → **Datasources** → **Add Datasource**
2. Select **Salesforce**
3. Follow the OAuth flow to authenticate
4. Configure which objects to index:
   ```
   ✓ Opportunities (required)
   ✓ Accounts (required)
   ✓ Contacts (recommended)
   ✓ Forecasts (recommended)
   ✓ Tasks & Events (optional)
   ✓ Custom Objects (if you have territory objects)
   ```
5. Set indexing schedule (recommend: every 15 minutes for real-time)
6. Wait for initial index to complete (can take 2-4 hours)

**Testing:**
- Search for a known opportunity name in Glean
- You should see the Salesforce record in search results
- Click through to verify data looks correct

### Step 1.2: Connect Google Sheets

**For each tracker sheet:**

1. Go to **Settings** → **Datasources** → **Google Drive**
2. Ensure Google Drive connector is active
3. By default, Glean indexes all accessible Google Sheets
4. Verify your key sheets are indexed:
   - Search for "EMEA Linearity Tracker" in Glean
   - Search for "Pipegen Performance"
   - Search for "Churn Tracker"

**If sheets aren't appearing:**
1. Check sharing permissions (sheets must be shared with glean-service-account or your org domain)
2. Wait 1-2 hours for indexing
3. Force re-index from admin console if needed

**Pro tip:** For structured data queries, you may want to use Google Sheets API directly instead of relying on Glean's indexing. We'll cover this in advanced configuration.

### Step 1.3: Connect Slack

1. Go to **Settings** → **Datasources** → **Slack**
2. Verify Slack is connected (usually already connected for enterprise)
3. Configure which channels to index:
   ```
   ✓ #emea-sales
   ✓ #sales-ops
   ✓ #forecast-updates
   ✓ #churn-saves
   ✓ Direct messages (optional, privacy considerations)
   ```
4. Set indexing scope:
   - Recommendation: "Messages from last 90 days" (performance vs completeness tradeoff)

### Step 1.4: Connect Google Calendar

1. Go to **Settings** → **Datasources** → **Google Calendar**
2. Verify connection
3. Calendar events are usually indexed automatically for all users
4. Verify by searching for a recent meeting name

---

## Phase 2: Create the Glean Agent (2-4 hours)

### Step 2.1: Access Glean Agents Interface

1. Log into Glean (glean.com or your company's Glean instance)
2. Click on your profile icon → **Admin** → **Agents** (or look for "Build Agent" option)
   - **Note**: This feature might be called "AI Assistants" or "Custom Agents" depending on your Glean version
3. Click **Create New Agent**

### Step 2.2: Basic Agent Configuration

**Agent Name:**
```
EMEA Sales Command Center
```

**Agent Description** (what users see):
```
Your AI-powered sales operations analyst for EMEA. Ask me about pipeline,
deals, forecasts, territories, and account performance. I can query Salesforce,
Google Sheets, and Slack to give you instant answers.

Try asking:
• "What are our top 10 EMEA deals by ARR?"
• "Which Commit deals are at risk of slipping?"
• "How is UK performing vs Germany this quarter?"
• "Show me at-risk renewals over $100K in Q1"
```

**Agent Icon/Avatar:**
Choose something professional (chart icon, dashboard icon, or Amplitude logo)

### Step 2.3: Configure Agent Instructions (System Prompt)

This is the most important part - it tells the agent how to behave.

**Click "Edit Instructions" or "System Prompt" and paste:**

```
You are the EMEA Sales Command Center, an expert sales operations analyst
for Amplitude's EMEA region. Your role is to help sales leaders, managers,
and operations teams get instant insights about deals, pipeline, forecasts,
and performance.

## Your Capabilities

You have access to:
1. Salesforce data (opportunities, accounts, contacts, forecasts)
2. Google Sheets trackers (linearity, pipegen, churn tracking)
3. Slack conversations (sales channels, deal discussions)
4. Google Calendar (meeting context)

## Core Knowledge

### Geography
EMEA includes: UK, Germany, France, Netherlands, Nordics (Sweden, Norway,
Denmark, Finland), DACH (Germany, Austria, Switzerland), Southern Europe
(Spain, Italy), Eastern Europe, and other European, Middle Eastern, and
African markets.

### Segments
- Velocity: SMB accounts, ARR $0-50K
- Emerging Enterprise: Mid-market, ARR $50K-250K
- Major Enterprise: Large enterprises, ARR $250K+

### Fiscal Calendar
- Q1: Feb 1 - Apr 30
- Q2: May 1 - Jul 31
- Q3: Aug 1 - Oct 31
- Q4: Nov 1 - Jan 31

Current quarter: Q4 FY26 (ends Jan 31, 2026)
Quarterly EMEA target: $5.6M

### Forecast Categories
- Pipeline: Early stage, low confidence
- Best Case: Moderate confidence
- Commit: High confidence, expected to close
- Closed Won: Deal completed
- Closed Lost: Did not close

### Key People
- Lee: EMEA Sales VP
- Dan: Company CRO

## How to Answer Questions

### Deal Intelligence Queries
When asked about deals, opportunities, or pipeline:
1. Default to EMEA region unless asked otherwise
2. Query Salesforce for current data
3. Sort by ARR (descending) unless specified otherwise
4. Include: Account Name, Opportunity Name, ARR, Stage, Forecast Category,
   Close Date, Owner
5. Always provide Salesforce links to records
6. Limit to top 10 results unless asked for more

Example query: "What are our top EMEA deals?"
→ Search Salesforce for Opportunities WHERE Region = "EMEA" ORDER BY ARR DESC LIMIT 10

### Risk Analysis Queries
When asked about at-risk deals or slipping opportunities:
1. Look for signals: long time in stage, no recent activity, forecast category
   downgrades, close date in past or near future with low stage
2. Highlight specific risks (e.g., "No activity in 14 days", "In negotiation
   for 45+ days")
3. Suggest actions (e.g., "Urgent: contact owner", "Consider forecast downgrade")

### Performance Queries
When asked about AE performance, regional comparisons, or quotas:
1. Check Google Sheets first (pipegen tracker, linearity tracker)
2. Supplement with Salesforce Closed Won data
3. Show comparative metrics (vs target, vs peers, vs prior period)
4. Highlight top and bottom performers
5. Calculate percentages and gaps

### Forecast & Pipeline Queries
When asked about pipeline coverage, forecast amounts, or quota tracking:
1. Sum opportunities by forecast category
2. Calculate coverage ratio (open pipeline ÷ remaining quota)
3. Show breakdown by segment or region if relevant
4. Compare to targets and historical norms

### Account Intelligence Queries
When asked about specific accounts:
1. Search Salesforce for account and related opportunities
2. Search Slack for recent mentions or discussions
3. Search calendar for recent meetings
4. Provide timeline of key events
5. Summarize current status and context

## Response Formatting

### Default Format (Executive Summary)
- Lead with key insight or answer
- Use bullet points for lists
- Keep responses concise (5-10 items max)
- Include relevant metrics and percentages
- Always cite sources (Salesforce links, Sheet names, Slack threads)
- End with suggested follow-up questions

### For Numbers
- Currency: Use $ symbol with K/M notation (e.g., "$1.2M", "$450K")
- Percentages: One decimal place (e.g., "65.3%")
- Dates: MM/DD/YYYY format (e.g., "01/28/2026")

### For Slack Outputs
When user asks to "draft a Slack message" or "format for Slack":
- Use Slack markdown (* for bold, • for bullets, > for quotes)
- Include relevant emojis (⚠️ for risks, ✅ for wins, 📊 for data)
- Keep concise (under 500 words)
- Include links to source records

### Source Citations
Always include sources at the end:
- Salesforce: [Account Name - Opportunity](https://amplitude.my.salesforce.com/...)
- Google Sheets: [Sheet Name](https://docs.google.com/spreadsheets/d/...)
- Slack: [#channel-name - Date](slack://...)

## Rules & Guardrails

1. **Always filter to EMEA** unless explicitly asked for global data
2. **Verify data freshness**: Note if data is older than 24 hours
3. **Flag missing data**: If critical fields are empty, mention it
4. **Be honest about limitations**: If you can't find data, say so
5. **Protect privacy**: Don't share contact details (emails, phones) unless
   explicitly asked
6. **No speculation**: Only report data you can verify from sources
7. **Round appropriately**: ARR to nearest $1K for clarity

## Common Query Patterns

### "Show me..." or "What are..."
→ Return a formatted list with relevant fields

### "How is X performing..."
→ Return metrics vs targets/benchmarks with percentages

### "Which deals..." or "Find opportunities..."
→ Query Salesforce with specified filters

### "Compare X vs Y"
→ Side-by-side metrics with delta/percentage change

### "At risk..." or "Likely to churn..."
→ Apply risk scoring logic and rank by risk level

### "Draft a message..." or "Write an update..."
→ Generate formatted text suitable for the specified channel

## Error Handling

- **No results found**: "I couldn't find any [X] matching your criteria.
  Try broadening the search or check if filters are correct."
- **Ambiguous query**: Ask clarifying questions (e.g., "Did you mean Q4 FY25
  or Q4 FY26?")
- **Missing access**: "I don't have access to that data. Check with your admin."
- **Stale data**: "Note: This data was last updated [timestamp]. Results may
  not reflect recent changes."

## Tone & Style

- Professional but approachable
- Confident and helpful
- Data-driven and specific
- Proactive (suggest follow-ups, highlight risks)
- Concise (executives value brevity)

## Example Interactions

User: "What are our top 5 deals in EMEA?"
You:
"Here are the top 5 EMEA opportunities by ARR:

1. Deutsche Bank - Enterprise Analytics - $850K
   Stage: Negotiation | Forecast: Commit | Close: 01/28/2026
   Owner: Sarah Mitchell

2. Unilever UK - Product Analytics Expansion - $720K
   Stage: Business Case | Forecast: Best Case | Close: 01/15/2026
   Owner: James Rodriguez

[... 3 more ...]

Total ARR: $3.28M
Last updated: Jan 9, 2026 10:30 AM GMT

Related questions you might ask:
• Which of these deals are at risk?
• Show me the pipeline for next quarter
• How does this compare to last quarter?

Sources: [Salesforce - EMEA Opportunities Report]"

---

Remember: Your goal is to save users time by providing instant, accurate,
actionable insights. Be the trusted data partner that helps EMEA sales
leaders make better decisions faster.
```

### Step 2.4: Configure Data Source Permissions

In the agent settings:

1. **Select which datasources the agent can access:**
   ```
   ✓ Salesforce
   ✓ Google Drive (for Sheets)
   ✓ Slack
   ✓ Google Calendar
   ```

2. **Set permission model:**
   - Choose "User-level permissions" (agent inherits user's access)
   - This ensures users only see data they have permission to see

3. **Configure query limits:**
   - Max results per query: 100
   - Query timeout: 30 seconds
   - Cache TTL: 15 minutes (balance between freshness and speed)

### Step 2.5: Add Example Queries (Training)

Glean learns from examples. Add 15-20 sample queries with expected behaviors:

**Deal Intelligence:**
```
Query: "What are our top 10 EMEA deals by ARR?"
Expected: List of 10 opportunities sorted by ARR, with key fields

Query: "Show me all Commit deals closing next week"
Expected: Filtered list where Forecast = "Commit" and Close Date = next 7 days

Query: "Find renewals over $100K in Q1"
Expected: Opportunities where Type = "Renewal" and ARR > $100K and Close Date in Q1
```

**Performance:**
```
Query: "How is UK performing vs Germany this quarter?"
Expected: Comparative metrics for both regions

Query: "Show me AE pipegen performance"
Expected: Pull from Google Sheets pipegen tracker
```

**Risk Analysis:**
```
Query: "Which Commit deals are at risk?"
Expected: Commit deals with risk signals (stale, long cycle, etc.)

Query: "What renewals are likely to churn?"
Expected: Renewals with churn indicators
```

These examples help Glean understand query intent and improve accuracy.

---

## Phase 3: Testing & Iteration (2-3 hours)

### Step 3.1: Basic Functionality Testing

**Test each query type:**

1. Open the agent in Glean
2. Start with simple queries:
   - "What are the top 5 EMEA deals?"
   - "Show me deals closing this month"
   - "Find opportunities in the UK"

3. Check the responses:
   - ✓ Does it return correct data?
   - ✓ Is formatting clean and readable?
   - ✓ Are sources cited?
   - ✓ Are Salesforce links working?

4. Test edge cases:
   - Empty results: "Show me deals in Antarctica"
   - Ambiguous queries: "How are we doing?" (should ask for clarification)
   - Complex queries: "Show me Major Enterprise renewals over $100K in Germany closing in Q1 that are in Commit forecast"

### Step 3.2: Accuracy Testing

**Create a test spreadsheet:**

| Query | Expected Answer | Agent Answer | Match? | Notes |
|-------|----------------|--------------|--------|-------|
| "Top 5 EMEA deals" | [Manual Salesforce query result] | [Agent response] | ✓/✗ | |
| "UK vs Germany performance" | [Manual calculation] | [Agent response] | ✓/✗ | |

Test 10-15 queries against manual results. Target: 90%+ accuracy.

**Common accuracy issues and fixes:**

| Issue | Fix |
|-------|-----|
| Wrong region data | Improve region filtering in system prompt |
| Missing recent deals | Check Salesforce indexing frequency |
| Incorrect calculations | Add explicit calculation instructions |
| Stale data | Reduce cache TTL or force refresh |

### Step 3.3: Performance Testing

**Measure response times:**
- Simple queries (top deals): Should be < 3 seconds
- Complex queries (multi-filter): Should be < 10 seconds
- If slower, optimize by:
  - Reducing Salesforce query scope
  - Increasing cache TTL
  - Simplifying agent instructions

### Step 3.4: Iterate Based on Results

**Common improvements needed:**

1. **Agent returns too much data**
   - Solution: Add "Limit to top 10 unless asked for more" to instructions

2. **Agent doesn't understand EMEA-specific terms**
   - Solution: Add more examples and definitions to system prompt

3. **Formatting is inconsistent**
   - Solution: Provide explicit formatting templates in instructions

4. **Agent can't find Google Sheets data**
   - Solution: Either wait for indexing OR use Google Sheets API integration (advanced)

5. **Sources not cited**
   - Solution: Add "Always include source links" to rules section

**Iteration process:**
1. Identify issue
2. Update system prompt or configuration
3. Test again with same query
4. Repeat until satisfied

---

## Phase 4: Advanced Configuration (Optional, 2-4 hours)

### Step 4.1: Direct Google Sheets API Integration

If Glean's indexing of Sheets isn't giving structured data you need:

**Option: Use Glean's Actions/Functions**

Some Glean plans support custom functions/actions:

1. Go to Agent settings → **Actions**
2. Create new action: "Query Pipegen Tracker"
3. Configure:
   ```yaml
   Action Name: get_pipegen_data
   Description: Get AE pipegen performance from Google Sheets

   Function Type: Google Sheets Query
   Sheet ID: [your-sheet-id]
   Range: 'Weekly Pipegen!A:M'

   Parameters:
     - ae_name (optional): Filter to specific AE
     - month (optional): Filter to specific month

   Returns: Structured data with columns [AE Name, Target, Actual, Gap, etc.]
   ```

4. Update system prompt to use this action:
   ```
   When asked about pipegen performance, use the get_pipegen_data action
   to retrieve current data from the Google Sheets tracker.
   ```

**Note:** This feature availability depends on your Glean plan. Check with Glean support or Vikram's team.

### Step 4.2: Add Alerting (If Supported)

Some Glean agents support proactive alerts:

**Example alert configuration:**
```yaml
Alert Name: Large Deal At Risk
Trigger: Daily at 9am
Condition: |
  Find opportunities WHERE:
  - ARR > $100K
  - Forecast Category = "Commit"
  - Last Modified Date > 7 days ago

Action: Send Slack message to #sales-ops with list of at-risk deals
```

### Step 4.3: Add Scheduled Reports

If your Glean plan supports it:

```yaml
Scheduled Report: Weekly Pipeline Summary
Frequency: Every Friday at 4pm
Recipients: [Your email, Lee's email]
Content: |
  Run these queries and compile into email:
  1. Total pipeline for current quarter
  2. Commit forecast by segment
  3. Top 10 deals closing next week
  4. At-risk renewals

Format: Executive summary email
```

---

## Phase 5: Deployment & Training (1-2 hours)

### Step 5.1: Beta Testing

Before full rollout:

1. **Invite 3-5 beta testers:**
   - Lee (primary user)
   - 1-2 sales managers
   - 1-2 sales ops colleagues

2. **Give them test scenarios:**
   - "Find the status of your largest deal"
   - "Check your team's performance this quarter"
   - "Look for at-risk renewals you own"

3. **Collect feedback:**
   - What worked well?
   - What didn't work?
   - What queries did you try that failed?
   - What would make this more useful?

4. **Iterate based on feedback** (1-2 iterations)

### Step 5.2: Create User Documentation

**Quick Start Guide** (1 page):
```markdown
# EMEA Sales Command Center - Quick Start

## What is it?
Your AI-powered sales analyst. Ask questions, get instant answers from
Salesforce, Google Sheets, and Slack.

## How to access
1. Go to Glean (glean.amplitude.com)
2. Click "Agents" in left sidebar
3. Select "EMEA Sales Command Center"

## Try these questions:
• "What are my top 5 deals?"
• "Show me Commit deals closing this month"
• "How is my team performing vs target?"
• "Which of my renewals are at risk?"

## Tips:
✓ Be specific (mention dates, regions, segments)
✓ Ask follow-up questions to dig deeper
✓ Request Slack formatting when you want to share
✓ Check the source links if you need more detail

Questions? Contact [Your Name] in #sales-ops
```

### Step 5.3: Announce & Train

**Slack announcement in #emea-sales:**
```
📣 NEW TOOL: EMEA Sales Command Center is live!

Tired of waiting for pipeline reports? Want instant answers about your deals?

The EMEA Sales Command Center is an AI agent that answers questions about
pipeline, deals, forecasts, and performance in seconds.

Try it: [Link to Glean agent]

Sample questions:
• "What are our top EMEA deals right now?"
• "Show me at-risk renewals in my territory"
• "How is UK performing this quarter?"

Quick start guide: [Link to doc]
Demo video: [Link - record a 2 min video]

Office hours: Tuesday 2-3pm GMT for live help
Questions: #sales-ops or DM me

Let's make sales ops faster! 🚀
```

**Optional: Host a 30-minute training session**
- Live demo of common queries
- Q&A
- Tips and tricks
- Record for those who can't attend

### Step 5.4: Monitor Usage

**Track these metrics:**

1. **Adoption:**
   - How many unique users per week?
   - How many queries per user?
   - Target: 80% of EMEA sales leaders using weekly within 2 months

2. **Engagement:**
   - What are the most common queries?
   - Which queries fail most often?
   - Are users asking follow-up questions (sign of value)?

3. **Satisfaction:**
   - Send monthly survey (1-2 questions)
   - "How useful was the Sales Command Center this month?" (1-5 scale)
   - "What would make it better?" (open text)

**Glean admin console should show:**
- Agent usage stats
- Popular queries
- Failed queries (use these to improve!)

---

## Phase 6: Ongoing Optimization (Continuous)

### Week 1-2: Fix obvious issues
- Queries that fail frequently → improve system prompt
- Data quality problems → work with Salesforce admin
- Performance issues → optimize queries

### Month 1-2: Add capabilities
- New query types based on user requests
- Better formatting for specific outputs
- Integration with additional data sources

### Month 3+: Advanced features
- Predictive analytics (if Glean supports)
- Automated alerts
- Scheduled reports
- Expansion to other regions

---

## Troubleshooting Common Issues

### Issue: Agent returns no results for valid queries

**Diagnostic steps:**
1. Check if Salesforce data is indexed (search manually in Glean)
2. Verify EMEA opportunities exist in Salesforce
3. Check agent permissions (can it access Salesforce?)
4. Review query logs (if available) to see what the agent searched for

**Solutions:**
- If indexing issue: Contact Glean support, force re-index
- If permission issue: Update agent datasource permissions
- If query logic issue: Improve system prompt with clearer instructions

### Issue: Agent returns wrong data

**Example:** Asked for "UK deals" but got Germany deals too

**Solutions:**
- Add explicit filtering examples to system prompt
- Provide list of UK countries/territories in context
- Add validation rule: "Always verify region matches query"

### Issue: Responses are too slow (>30 seconds)

**Solutions:**
- Increase cache TTL (trade freshness for speed)
- Limit result count (top 10 vs top 100)
- Simplify Salesforce queries (fewer fields, narrower date ranges)
- Work with Glean team to optimize indexing

### Issue: Agent can't access Google Sheets data

**Solutions:**
- Verify sheets are shared with appropriate permissions
- Wait for indexing (can take 1-2 hours)
- Check if Google Drive connector is active
- Consider using direct Google Sheets API (advanced)

### Issue: Users don't understand how to ask questions

**Solutions:**
- Add more example queries to agent description
- Create a "cheat sheet" of common queries
- Host training session
- Add "Did you mean...?" suggestions to agent responses

---

## Getting Help

### Internal Resources (Amplitude)
- **Vikram's team** (mentioned in AI Day email):
  - Ankit Mishra
  - Gary Vang
  - Jason Kowalczyk
  - Mike Jones
  - Ravindra Bura

  → Schedule time with them for technical help

- **Glean workspace admin** at Amplitude
  → For permissions, datasource config, agent access

- **Salesforce admin** at Amplitude
  → For API access, custom fields, data quality

### External Resources
- **Glean Support**: support@glean.com or through your admin console
- **Glean Documentation**: docs.glean.com (agents section)
- **Glean Community**: community.glean.com (other users' tips)

### For AI Day
- Set up office hours with Vikram's team **before** AI Day
- Test your build with them
- Get their feedback on configuration
- They can help troubleshoot live during the hackathon

---

## Realistic Timeline

### If you're starting from scratch:

**Day 1 (3-4 hours):**
- Connect Salesforce to Glean (if not already connected)
- Verify Google Sheets indexing
- Create basic agent with simple system prompt
- Test 5 basic queries

**Day 2 (3-4 hours):**
- Refine system prompt based on Day 1 results
- Add example queries
- Test 15-20 different query types
- Iterate on formatting and accuracy

**Day 3 (2 hours):**
- Beta test with Lee and 1-2 colleagues
- Collect feedback
- Make final refinements
- Prepare demo and documentation

**AI Day (4-6 hours):**
- Work with Vikram's team on advanced features
- Optimize performance
- Add any requested capabilities
- Practice demo
- Final testing

**Post AI Day (ongoing):**
- Roll out to all users
- Monitor usage
- Iterate based on feedback
- Expand capabilities

---

## Success Criteria for AI Day

By the end of AI Day, you should have:

✓ **Working agent** that answers 15-20 query types accurately
✓ **Live demo ready** (tested queries that work reliably)
✓ **Clear value prop** (before/after time comparison)
✓ **User testimonial** (get Lee to try it and provide quote)
✓ **Roadmap** (what you'll build with funding)

**Good enough is better than perfect** for the hackathon. Focus on:
- Core queries working well (top deals, performance, at-risk)
- Impressive demo (live Q&A)
- Clear business value (time saved, decisions enabled)

You can always improve after you win! 🏆

---

## Quick Start Checklist

**Before AI Day:**
- [ ] Verify Salesforce is connected to Glean
- [ ] Verify Google Sheets are indexed
- [ ] List 20 questions you want the agent to answer
- [ ] Schedule time with Vikram's team for help

**During AI Day:**
- [ ] Create agent in Glean
- [ ] Write system prompt (use template above)
- [ ] Add example queries
- [ ] Test with real questions
- [ ] Iterate on accuracy
- [ ] Practice demo
- [ ] Get Lee to test it
- [ ] Prepare pitch

**For the Win:**
- [ ] Demo works flawlessly (practice 5+ times)
- [ ] Business value is clear (time saved, ROI)
- [ ] Roadmap is exciting (where this goes next)
- [ ] You're confident and enthusiastic
- [ ] You've got backup slides if needed

---

Let's build this thing! 🚀
