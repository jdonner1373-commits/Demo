# EMEA Sales Command Center Agent - Demo Script
## AI Day 2026 - 10 Minute Presentation

---

## Pre-Demo Checklist

- [ ] Glean agent configured and tested
- [ ] Live Salesforce connection working
- [ ] Sample queries tested and responses look good
- [ ] Backup slides ready in case of technical issues
- [ ] Timer set for 10 minutes
- [ ] Screen sharing ready
- [ ] Slack window open for message formatting demo
- [ ] Salesforce tab open to show source linking

---

## Demo Flow (10 minutes)

### Opening (45 seconds) - SET THE STAGE

**[Screen: Title slide with your name and agent name]**

> "Hi everyone! I'm [Your Name], Sales Ops & Strategy Manager for EMEA.
>
> I spend about 8-12 hours every week doing the same thing: answering questions from our EMEA VP Lee about deals, pipeline, and account performance.
>
> Questions like 'What are our biggest deals?' or 'Which renewals are at risk?' sound simple, but each one requires me to:
> - Log into Salesforce
> - Build custom reports with filters
> - Export to spreadsheets
> - Cross-reference with my Google Sheets trackers
> - Format for executive consumption
> - Send via Slack or present in meetings
>
> This takes 15-45 minutes per question, creates context switching, and delays leadership decisions.
>
> Today I'm showing you the **EMEA Sales Command Center** - an AI agent that turns these 30-minute analyses into 30-second conversations."

**[Screen: Switch to Glean agent interface]**

---

### Demo Part 1: Deal Intelligence (3 minutes) - THE WOW MOMENT

**Query 1: Basic Deal Query**

> "Let's start simple. Lee asks me this question almost weekly."

**[Type in Glean]:** `What are our top 5 new business deals in EMEA right now?`

**Expected Agent Response:**
```
Here are the top 5 new business opportunities in EMEA by ARR:

1. Deutsche Bank - Enterprise Analytics Platform - $850K
   Stage: Negotiation | Forecast: Commit | Close: 01/28/2026
   Owner: Sarah Mitchell | Link: [SF Link]

2. Unilever UK - Product Analytics Expansion - $720K
   Stage: Business Case | Forecast: Best Case | Close: 01/15/2026
   Owner: James Rodriguez | Link: [SF Link]

3. Siemens DACH - Multi-Product Bundle - $680K
   Stage: Solution Design | Forecast: Best Case | Close: 02/12/2026
   Owner: Emma Schmidt | Link: [SF Link]

4. Booking.com - User Analytics Suite - $540K
   Stage: Negotiation | Forecast: Commit | Close: 01/22/2026
   Owner: Lars van den Berg | Link: [SF Link]

5. Spotify Sweden - Cross-Platform Analytics - $490K
   Stage: Discovery | Forecast: Pipeline | Close: 03/15/2026
   Owner: Anna Bergström | Link: [SF Link]

Total ARR: $3.28M
Data as of: Jan 9, 2026 10:30 AM GMT
```

> "30 seconds. Live data from Salesforce. Formatted and ready to send to Lee."

**[Pause for effect]**

**Query 2: Risk Analysis (show intelligence)**

> "But Lee doesn't just want lists - he wants insights. Let's dig deeper."

**[Type in Glean]:** `Which of these deals has the highest risk of slipping?`

**Expected Agent Response:**
```
⚠️ Risk Analysis - 2 deals flagged:

HIGH RISK: Unilever UK - $720K
- Close date: 01/15/2026 (6 days away)
- Last activity: 14 days ago
- Still in Stage 3 (Business Case) but forecasted close is imminent
- Missing: Executive sponsor confirmation, legal review
- Action: Urgent - connect with James Rodriguez

MODERATE RISK: Deutsche Bank - $850K
- Close date: 01/28/2026
- Stage duration: 45 days in Negotiation (avg is 30 days)
- Pricing concerns mentioned in last Slack update
- Action: Confirm procurement timeline

Would you like me to draft check-in messages for the owners?
```

> "Notice it's not just pulling data - it's analyzing deal health, comparing to benchmarks, and flagging specific risks. This is the kind of insight that takes me 30 minutes of manual digging."

**Query 3: Action Generation (show automation)**

**[Type in Glean]:** `Yes, draft a Slack message for James about the Unilever deal`

**Expected Agent Response:**
```
Here's a suggested message for James Rodriguez:

---

Hey James 👋

Quick check on the Unilever UK deal ($720K, closing 01/15):

I noticed:
• Last update was 2 weeks ago
• We're 6 days from close but still in Business Case stage
• Missing exec sponsor confirmation and legal review

Can you share a quick status update? Anything blocking that we can help with?

Given the close date, want to make sure we're on track or if we need to adjust forecast category.

Thanks!

[Salesforce Link: opp/12345]

---

Copy this to Slack?
```

> "Now I've gone from question to insight to action in under 2 minutes. That's the power of this agent."

**[Briefly show copying to Slack - don't actually send]**

---

### Demo Part 2: Performance Analysis (3 minutes) - SHOW BREADTH

**Query 4: Regional Comparison**

> "Lee also asks me to compare regional performance constantly. This normally requires custom Salesforce reports."

**[Type in Glean]:** `How is UK performing vs Germany this quarter?`

**Expected Agent Response:**
```
Q4 FY26 Performance Comparison (as of 01/09/2026):

UK:
📈 Closed Won: $1.8M (64% of regional target)
📊 Open Pipeline: $4.2M (3.2x coverage)
🎯 Commit Forecast: $950K
👥 AEs: 6 | Avg ARR per AE: $300K

Germany:
📈 Closed Won: $1.4M (52% of regional target)
📊 Open Pipeline: $3.8M (2.8x coverage)
🎯 Commit Forecast: $720K
👥 AEs: 5 | Avg ARR per AE: $280K

Key Insights:
✅ UK ahead on attainment (12 points higher)
✅ UK has stronger pipeline coverage
⚠️ Germany's pipeline coverage below 3x target
💡 Germany has 2 large renewals at risk ($400K+ total)

UK top performer: Sarah Mitchell ($580K closed)
Germany top performer: Emma Schmidt ($510K closed)
```

> "This gives Lee everything he needs for his weekly leadership call. Normally takes me an hour to pull this together."

**Query 5: Deep Dive on Underperformance**

**[Type in Glean]:** `Show me the bottom 3 AEs in pipegen this month`

**Expected Agent Response:**
```
December 2025 Pipegen - Bottom 3 Performers:

1. Alex Thompson (Emerging Enterprise, UK)
   Generated: $180K | Target: $400K | Gap: -55%
   Deals created: 3 | Avg deal size: $60K
   ⚠️ Trend: Down 30% vs last month

2. Marc Dubois (Major Enterprise, France)
   Generated: $220K | Target: $500K | Gap: -56%
   Deals created: 2 | Avg deal size: $110K
   ⚠️ Trend: Down 25% vs last month

3. Johan Svensson (Velocity, Nordics)
   Generated: $95K | Target: $200K | Gap: -53%
   Deals created: 8 | Avg deal size: $12K
   ⚠️ Trend: Flat vs last month

Common pattern: All three have low activity in prospecting (SDR-sourced deals down 40%)

Would you like to see their current Commit pipeline to assess recovery potential?
```

**[Type in Glean]:** `Yes, what Commit deals do they have?`

**Expected Agent Response:**
```
Current Commit Forecast for Underperforming AEs:

Alex Thompson:
• Barclays PLC - $240K (Close: 01/22)
• Tesco Digital - $180K (Close: 02/05)
Total Commit: $420K (could recover if both close)

Marc Dubois:
• Airbus France - $680K (Close: 01/30)
Total Commit: $680K (strong recovery if closes)

Johan Svensson:
• Klarna AB - $85K (Close: 01/18)
• Spotify Free Tier - $45K (Close: 01/25)
Total Commit: $130K (partial recovery)

💡 Marc has potential to significantly outperform if Airbus closes
⚠️ Alex and Johan need pipeline building focus for Q1
```

> "Now we've identified the problem AND the potential solution. This is strategic insight, not just reporting."

---

### Demo Part 3: Churn Intelligence (2 minutes) - SHOW BUSINESS IMPACT

**Query 6: At-Risk Renewals**

> "One more scenario - every week I prep for our churn save calls. Let me show you how the agent helps."

**[Type in Glean]:** `Which renewals over $100K are at risk of churning in Q1?`

**Expected Agent Response:**
```
⚠️ Q1 2026 At-Risk Renewals (ARR > $100K):

1. Sainsbury's UK - $320K Renewal
   Close: 02/15/2026 | Owner: Sarah Mitchell
   Risk Score: HIGH
   Signals:
   - MAU down 40% last 2 months
   - 3 support tickets escalated in Dec
   - Budget concerns mentioned in last call
   - No exec engagement in 60 days

2. Zalando Germany - $280K Renewal
   Close: 03/01/2026 | Owner: Emma Schmidt
   Risk Score: MEDIUM
   Signals:
   - Product adoption stagnant (only using 2 of 5 modules)
   - Champion left company in November
   - Competitive evaluation mentioned (Mixpanel)

3. ING Bank Netherlands - $195K Renewal
   Close: 02/28/2026 | Owner: Lars van den Berg
   Risk Score: MEDIUM
   Signals:
   - Payment 30 days overdue (Finance flagged)
   - QBR postponed twice
   - Requesting discount in renewal discussions

Total at-risk ARR: $795K

Recommended actions:
• Sainsbury's: Urgent exec alignment + product adoption plan
• Zalando: Find new champion + demo advanced features
• ING: Resolve payment issue + prove ROI for renewal discount

Previous similar saves: [Links to 3 comparable accounts with strategies]
```

**[Type in Glean]:** `Summarize the Sainsbury's situation for my churn save call`

**Expected Agent Response:**
```
Executive Brief: Sainsbury's UK - $320K At-Risk Renewal

Account Context:
- Customer since: May 2023 (2.5 years)
- Original ARR: $280K → Upsold to $320K in 2024
- Segment: Major Enterprise (Retail)
- Owner: Sarah Mitchell
- Champion: David Roberts (Analytics Director)

Current Situation:
⚠️ Usage declining sharply (MAU -40% since Oct 2025)
⚠️ Multiple support escalations (dashboard performance, data sync issues)
⚠️ Budget pressure mentioned in Q4 call (Nov 18, 2025)
⚠️ No exec engagement since Oct 2025

Recent Activity:
- Last call: Dec 10 (David expressed frustration with support response times)
- Slack messages: 3 in December (all related to technical issues)
- Support tickets: 5 open (3 marked urgent)

Risk Assessment: HIGH
- Renewal date: 02/15/2026 (37 days)
- Probability of churn: 60%
- Impact: $320K ARR loss

Save Strategy (based on similar accounts):
1. Immediate: Exec sponsor (Lee) outreach to David's VP
2. This week: Dedicated support sprint to close all tickets
3. Next week: Product adoption workshop (get them using dormant features)
4. Ongoing: Weekly check-ins until renewal signed

Comparable saves:
- Tesco (similar usage drop) - saved with exec intervention + CSM change
- Marks & Spencer (support issues) - saved with dedicated tech resources

Prep for call:
✓ Support team briefed on ticket priority
✓ Product specialists on standby for workshop
✓ CSM prepared with adoption plan
⚠️ Need: Lee's calendar availability for exec call

[Salesforce Link] | [Support Tickets] | [Usage Dashboard]
```

> "Everything I need for the call in one response. Account history, risk factors, suggested strategies, even comparable accounts we've saved before."

---

### Closing (60 seconds) - DRIVE HOME THE VALUE

**[Screen: Return to closing slide with ROI metrics]**

> "Let me bring this home with the impact:
>
> **Time Savings:**
> - 8-12 hours saved per week for me personally
> - That's 400-600 hours per year
> - At my hourly rate, that's $50K+ in time savings
> - And that doesn't count the value of faster leadership decisions
>
> **Decision Speed:**
> - Lee gets answers in minutes instead of next-day
> - Better informed for customer calls, forecasts, and strategy sessions
> - Enables self-service - he can query directly without waiting for me
>
> **Quality Improvements:**
> - No manual data entry errors
> - Real-time data, not stale reports
> - Consistent analysis methodology
> - Sources always cited and linked
>
> **Scalability:**
> - Built for EMEA but works for any region
> - Every sales leader and manager can use it
> - Extends to SDR leaders, Marketing, Partners, CS
> - 50+ potential users at Amplitude
>
> **The Bottom Line:**
> This agent transforms Sales Operations from a reporting function to a strategic function. Instead of spending 60% of my time pulling data, I can focus on insights, planning, and execution.
>
> And for Lee and our sales team, it means faster, better-informed decisions that directly impact revenue.
>
> Thank you! Happy to take questions."

---

## Q&A Preparation (potential questions)

**Q: What if the data in Salesforce is bad?**

A: "Great question. The agent actually helps with data quality by flagging missing fields or stale dates in its responses. It won't fix bad data, but it surfaces it so we can address it. In some ways, it's a data quality forcing function."

**Q: Can it do forecasting predictions, not just reporting?**

A: "Not in this MVP, but that's absolutely on the roadmap. With enough historical data, we could train it to predict deal close probability, churn likelihood, and forecast accuracy. That's where the real magic happens."

**Q: How do you handle data privacy and access control?**

A: "The agent inherits Salesforce permissions from the logged-in user. So if you don't have access to a deal or account in Salesforce, the agent won't show it to you either. It's permission-aware by design."

**Q: What happens when Salesforce is slow or down?**

A: "We cache frequently-requested queries for 15 minutes to improve performance. If Salesforce is completely down, the agent will return the last cached results with a timestamp warning. For critical real-time needs, we'd obviously wait for Salesforce to recover."

**Q: How long did this take to build?**

A: "The core agent configuration took about 4 hours with Glean's agent builder - mostly mapping data sources and writing sample queries. The refinement (prompt engineering, response formatting) took another 6-8 hours of testing. So roughly 2 days of focused work for an MVP."

**Q: Could this replace you?**

A: "Ha! No. It handles the repetitive reporting and analysis, but all the strategic work - territory planning, process design, stakeholder management, complex problem solving - that still requires human judgment. This just frees me up to do more of that high-value work."

**Q: What was the hardest part technically?**

A: "Getting the Salesforce queries optimized for speed. Some of our data models are complex with lots of relationships. We had to work with Glean's team to structure queries efficiently and use caching smartly. The natural language part actually worked better than expected out of the box."

**Q: How do you measure success?**

A: "Three metrics: 1) Time saved per query (target: 80% reduction), 2) Query accuracy (target: 95% correct answers), 3) Adoption rate (target: 50% of sales leaders using it weekly within 3 months). We're tracking all three."

---

## Backup Plan (if live demo fails)

**Option 1: Screen Recording**
- Have a pre-recorded video of the full demo
- Walk through it with live narration
- Less impressive but shows functionality

**Option 2: Slides with Screenshots**
- Prepared slides showing each query and response
- Still tells the story, just not interactive
- Include actual Salesforce data to prove it's real

**Option 3: Manual Demo**
- Show the Salesforce reports you currently build manually
- Walk through your current process (15 min for one analysis)
- Then show the Glean agent config and explain how it would work
- Less wow-factor but highlights the pain point clearly

---

## Post-Demo Assets to Prepare

1. **One-pager** summarizing the agent for judges
2. **ROI calculation spreadsheet** with detailed assumptions
3. **Rollout plan** if you win funding (30/60/90 day plan)
4. **User testimonials** (get Lee to provide quote after demo)
5. **Comparison table** vs manual process and other tools
6. **Roadmap** for future enhancements

---

## Tips for Delivery

- **Practice 5+ times** - know the flow cold
- **Speak to business value**, not tech features
- **Make it personal** - use real examples from your work
- **Show enthusiasm** - you're excited about this!
- **Pace yourself** - don't rush through queries
- **Pause for impact** - let results sink in
- **Watch the clock** - have a timer visible
- **Prepare for tech fails** - have backup ready
- **Get a buddy** to play "Lee" and ask questions during practice
- **Record yourself** and watch for nervous habits

---

## Day-Of Checklist

**1 hour before:**
- [ ] Test agent with all demo queries
- [ ] Check Salesforce connection
- [ ] Clear browser cache
- [ ] Close unnecessary apps
- [ ] Zoom in on screen for visibility
- [ ] Test screen sharing audio/video
- [ ] Have water nearby
- [ ] Bathroom break
- [ ] Review notes one final time

**10 minutes before:**
- [ ] Open all needed tabs
- [ ] Glean agent interface ready
- [ ] Salesforce logged in (separate tab)
- [ ] Slack open
- [ ] Backup slides ready
- [ ] Timer set
- [ ] Take 3 deep breaths
- [ ] You've got this! 🚀

---

Good luck! This is a winning idea - just execute with confidence.
