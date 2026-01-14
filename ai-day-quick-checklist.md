# AI Day Quick Checklist
## EMEA Sales Command Center - Pre-Event Prep

---

## 🎯 THE GOAL

Build a working Glean agent that answers sales questions instantly, demo it live, and win $50K funding.

**Time available**: ~6-12 hours before AI Day + 4-6 hours during event

---

## BEFORE AI DAY

### Week Before (2-3 hours)

**Access & Permissions:**
- [ ] Confirm you have Glean workspace access (glean.amplitude.com or similar)
- [ ] Verify you can access Glean agent builder (Admin → Agents)
- [ ] Check Salesforce API access (can you see Salesforce data in Glean search?)
- [ ] Verify Google Sheets are indexed (search for "EMEA Linearity Tracker" in Glean)
- [ ] List your key data sources:
  - [ ] Salesforce instance URL: ___________________________
  - [ ] Key Google Sheets IDs: ___________________________
  - [ ] Slack channels to index: _________________________

**Get Technical Support:**
- [ ] Email Vikram's team to schedule 30-60 min help session
  - Ankit Mishra, Gary Vang, Jason Kowalczyk, Mike Jones, Ravindra Bura
  - Ask about: Salesforce connector setup, agent configuration, optimization
- [ ] Schedule time **before** AI Day (not during)

**Prepare Your Materials:**
- [ ] Review `/home/user/Demo/glean-agent-proposals.md` (your strategy)
- [ ] Review `/home/user/Demo/build-guide.md` (how to build)
- [ ] Review `/home/user/Demo/demo-script.md` (what to demo)
- [ ] List 20 questions you need the agent to answer (use sample-queries-test-sheet.md)

### 2-3 Days Before AI Day (3-4 hours)

**Create Basic Agent:**
- [ ] Log into Glean
- [ ] Create new agent: "EMEA Sales Command Center"
- [ ] Copy system prompt from `build-guide.md` (Phase 2.3)
- [ ] Configure data sources (Salesforce, Google Sheets, Slack)
- [ ] Add 5-10 example queries

**Basic Testing:**
- [ ] Test query: "What are our top 10 EMEA deals by ARR?"
  - Does it return results? _____ (Yes/No)
  - Is data accurate? _____ (Yes/No)
  - Response time: _____ seconds
- [ ] Test query: "Show me Commit deals closing next week"
  - Works? _____ (Yes/No)
- [ ] Test query: "How is UK performing this quarter?"
  - Works? _____ (Yes/No)

**If queries don't work:**
- Check if Salesforce is indexed (search manually in Glean)
- Verify agent has permission to access Salesforce
- Simplify system prompt and try again
- Reach out to Vikram's team for help

### 1 Day Before AI Day (2-3 hours)

**Refine & Test:**
- [ ] Test all 7 demo-day priority queries (from sample-queries-test-sheet.md)
  - [ ] "What are our top 5 new business deals in EMEA right now?"
  - [ ] "Which of these deals has the highest risk of slipping?"
  - [ ] "Draft a Slack message to check in with that AE"
  - [ ] "How is UK performing vs Germany this quarter?"
  - [ ] "Show me the bottom 3 AEs in pipegen this month"
  - [ ] "Which renewals over $100K are at risk of churning in Q1?"
  - [ ] "Summarize the [specific account] situation for Lee"

- [ ] Run each query 3 times to ensure consistency
- [ ] Fix any issues (update system prompt, adjust filters)
- [ ] Time each query (should be < 10 seconds)

**Get User Feedback:**
- [ ] Ask Lee to test the agent (10 minutes)
  - Get him to ask 2-3 real questions
  - Note what works and what doesn't
  - Ask for a quote/testimonial if he likes it
- [ ] Ask 1-2 sales managers to try it
- [ ] Collect feedback and iterate

**Prepare Demo Materials:**
- [ ] Create pitch deck slides (use `pitch-deck-outline.md` as template)
  - Minimum 10 slides: Problem, Solution, How it Works, Demo, Impact, Roadmap, Budget, Call to Action
- [ ] Practice pitch out loud (time yourself - should be 8-10 min including demo)
- [ ] Record demo video as backup (in case live demo fails)
- [ ] Print one-pager for judges (from pitch-deck-outline.md)

**Prepare Your Computer:**
- [ ] Charge laptop fully
- [ ] Clear desktop (close unnecessary apps)
- [ ] Open required tabs:
  - Glean agent interface
  - Salesforce (to show source data)
  - Your pitch deck
  - Backup demo video
- [ ] Test screen sharing (Zoom/Google Meet)
- [ ] Zoom in browser for visibility (125%)
- [ ] Test audio/video

### Night Before AI Day

**Final Checks:**
- [ ] Agent works for all 7 demo queries ✓
- [ ] Pitch deck complete ✓
- [ ] Demo practiced 3+ times ✓
- [ ] Backup plan ready (slides, video) ✓
- [ ] One-pagers printed ✓
- [ ] Laptop charged ✓
- [ ] You know your pitch cold ✓

**Get Sleep:**
- [ ] Go to bed early
- [ ] Set alarm with buffer time
- [ ] You've got this! 🚀

---

## DURING AI DAY

### Morning Setup (30 min before)

**Technical:**
- [ ] Test agent one final time with all 7 demo queries
- [ ] Check Salesforce connection (is it up to date?)
- [ ] Open all needed tabs (Glean, Salesforce, deck, backup)
- [ ] Test screen share
- [ ] Close Slack/email (no distractions)
- [ ] Set phone to Do Not Disturb
- [ ] Have water nearby

**Mental Prep:**
- [ ] Review demo script (just read through, don't practice)
- [ ] Review your pitch opening (first 30 seconds)
- [ ] Take 3 deep breaths
- [ ] Remember: you're solving a REAL problem you live with daily
- [ ] You know this domain better than anyone in the room

### Build/Refinement Time (3-4 hours)

**Priority 1: Make demo queries bulletproof**
- [ ] Test each demo query 5 times
- [ ] Fix any inconsistencies
- [ ] Make sure responses are formatted well
- [ ] Ensure source links work

**Priority 2: Add impressive features (if time)**
- [ ] Add more example queries to agent
- [ ] Improve response formatting (tables, bullets, emojis)
- [ ] Add "suggested follow-up questions" to responses
- [ ] Connect additional data sources (if easy)

**Priority 3: Get help from Vikram's team**
- [ ] Show them your agent
- [ ] Ask for optimization suggestions
- [ ] Get help with any technical issues
- [ ] Ask them to test it and provide feedback

**Don't do (time sinks):**
- ❌ Don't try to add complex features you haven't tested
- ❌ Don't rebuild from scratch if it's mostly working
- ❌ Don't spend hours on perfect formatting
- ❌ Don't get distracted by other teams' projects
- **Focus on making your 7 demo queries work perfectly**

### 1 Hour Before Pitch

**Final Testing:**
- [ ] Run all 7 demo queries one last time
- [ ] Confirm they all work
- [ ] If one fails, have a backup query ready

**Rehearsal:**
- [ ] Practice opening (30 sec - the problem statement)
- [ ] Practice live demo transitions
- [ ] Practice closing (30 sec - the ask)
- [ ] Time the full thing (should be 9-10 min)

**Logistics:**
- [ ] Bathroom break
- [ ] Water bottle filled
- [ ] Laptop plugged in (don't rely on battery)
- [ ] Phone silenced
- [ ] Backup slides ready
- [ ] One-pagers ready to hand out

**Mental Game:**
- [ ] You've done the work
- [ ] You know the material
- [ ] You're solving a real problem
- [ ] Your demo works
- [ ] You've got this 💪

---

## DURING YOUR PITCH (10 minutes)

### Timing Breakdown
- **0:00-0:45** - Problem statement (paint the pain)
- **0:45-1:30** - Solution overview (what the agent does)
- **1:30-5:30** - LIVE DEMO (the wow moment) ⭐
- **5:30-7:00** - Impact & ROI (why this matters)
- **7:00-8:30** - Roadmap & budget (where this goes)
- **8:30-10:00** - Q&A or extended demo

### Demo Execution

**Stay calm:**
- If a query fails: Have a backup ready
- If Salesforce is slow: Use the cache response time
- If you freeze: Look at your notes, take a breath, continue
- If judges ask questions mid-demo: Answer briefly, keep moving

**Showmanship:**
- Type queries slowly so judges can read them
- Pause after each response to let it sink in
- Highlight impressive parts ("Notice it analyzed all 400 deals in 2 seconds")
- Show enthusiasm (you're excited about this!)

### After Your Pitch

- [ ] Answer judge questions confidently
- [ ] Provide one-pagers to judges
- [ ] Thank them for their time
- [ ] Exhale! You did it!

---

## POST-PITCH

### Immediate (5 min)
- [ ] Write down any questions you couldn't answer (for follow-up)
- [ ] Note any technical issues that occurred
- [ ] Gather feedback from teammates who watched

### If You Win Your VP Group
- [ ] Prepare for finals (refine based on feedback)
- [ ] Practice demo again (it needs to be even better)
- [ ] Add any requested features if time allows

### If You Don't Win Your VP Group
- [ ] Still build it! You've done most of the work
- [ ] Roll it out to EMEA team anyway
- [ ] Document the impact over next 3 months
- [ ] Pitch for funding in Q1 planning
- **The agent has value regardless of the competition result**

---

## BACKUP PLANS

### If Live Demo Fails Completely
- [ ] Switch to pre-recorded demo video
- [ ] Walk through it with narration
- [ ] Still impressive, just not live

### If Glean is Down
- [ ] Show screenshots of working queries
- [ ] Show your Salesforce manual process (emphasize pain)
- [ ] Explain what the agent would do
- [ ] Offer to demo later

### If You Run Out of Time
- [ ] Skip to the demo (most important part)
- [ ] Do 2-3 queries instead of 7
- [ ] Jump to ROI slide
- [ ] Summarize verbally

---

## CONFIDENCE BUILDERS

**You have advantages:**
1. ✅ You live this problem every day (authenticity)
2. ✅ You know exactly what questions to ask (domain expertise)
3. ✅ You have executive sponsor (Lee will vouch for this)
4. ✅ You can quantify ROI precisely (10-12 hrs/week saved)
5. ✅ You already have some automation (Python scripts show you're serious)
6. ✅ This is a perfect Glean use case (NL search, multi-source)

**Your competition may:**
- ❌ Have theoretical problems (not real pain)
- ❌ Have unclear ROI (hard to measure)
- ❌ Have complex solutions (hard to demo)
- ❌ Lack domain expertise (generic solutions)

**You're in a strong position. Trust the work you've done.**

---

## FINAL REMINDERS

### What Judges Care About
1. **Real problem** - Is this actually painful? (YES - you spend 10+ hrs/week on this)
2. **Clear solution** - Does the agent solve it? (YES - demo proves it)
3. **Measurable impact** - What's the ROI? (YES - $50K+/year time savings)
4. **Impressive demo** - Does it wow them? (YES - live AI Q&A is cool)
5. **Scalability** - Can others use it? (YES - all regions, all GTM teams)
6. **Your credibility** - Do they trust you can execute? (YES - you're already automating)

### What Makes You Win
- ✅ Authenticity (you FEEL the pain when you talk about it)
- ✅ Clarity (simple problem, simple solution, clear value)
- ✅ Execution (you built it, not just ideas)
- ✅ Vision (roadmap shows this is just the beginning)
- ✅ Passion (you're excited about making sales ops better)

### What Doesn't Matter
- ❌ Perfect slides (content > design)
- ❌ Fancy features (working > impressive)
- ❌ Technical jargon (judges want business value)
- ❌ Comparison to others (focus on your story)

---

## THE WINNING FORMULA

**Problem (emotional) + Solution (clear) + Demo (impressive) + Impact (measurable) = Win**

You have all four pieces. Now go execute.

---

## EMERGENCY CONTACTS

- **Vikram's team**: ______________ (Slack handle)
- **Glean admin**: ______________ (Slack handle)
- **Your manager**: ______________ (for support/encouragement)
- **Lee (EMEA VP)**: ______________ (for testimonial/testing)

---

## YOU'VE GOT THIS! 🚀

Remember why you're doing this:
- To save yourself 500+ hours per year
- To help Lee make better, faster decisions
- To make EMEA sales ops world-class
- To prove AI can transform revenue operations

**This is your competition to win. Go get it.** 🏆

---

## Post-Event (Win or Lose)

- [ ] Thank Vikram's team for support
- [ ] Thank Lee and testers for feedback
- [ ] Share results with your team
- [ ] Roll out the agent (even if you didn't win)
- [ ] Document impact over 90 days
- [ ] Present results to leadership
- [ ] Apply learnings to next project

**The agent has value regardless of competition outcome. You've built something valuable.**

---

Good luck! 🍀
