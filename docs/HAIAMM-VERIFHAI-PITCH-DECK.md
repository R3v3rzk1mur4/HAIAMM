![HAIAMM Logo](images/HAIAMM_logo.png)

# HAIAMM + Verifhai: Secure Your AI-Operated Security

## Complete Pitch Deck

**Version:** 2.0
**Format:** Slide-by-slide content for PowerPoint/Google Slides/Keynote
**Duration:** 20-25 minute presentation

---

## SLIDE 1: Title Slide

**Visual:** HAIAMM logo, clean professional background, Verifhai icon

# HAIAMM + Verifhai
## Human-Assisted Intelligence Assurance Maturity Model

**The Framework + The Tool to Secure AI-Operated Security**

| HAIAMM | Verifhai |
|--------|----------|
| The Framework | The Interactive Mentor |
| What to measure | How to build it |

100% Open Source | OWASP Top 10 Aligned | Community-Driven

[Your Name]
[Date]

**Speaker Notes:**
Welcome. Today I'm presenting HAIAMM version 2.2 - not just as a framework, but as a complete solution. HAIAMM tells you WHAT to secure. Verifhai shows you HOW to build it. Together, they're the first end-to-end system for securing AI-operated security programs.

---

## SLIDE 2: The $4M Question

**Visual:** CISO at board meeting, executives asking questions, AI icons in background

# Your Board Will Ask This Question

> "We've invested $2M in AI security tools. Our AI agents are running pentests, blocking threats, generating compliance evidence, and making critical decisions.
>
> **Can you prove they're working correctly?**
>
> Show me the data."

**Without HAIAMM + Verifhai:** "We... trust the vendors?"

**With HAIAMM + Verifhai:** "Yes. We're at Level 2 maturity with 94% goal hijack detection rate."

**Speaker Notes:**
This is the question every CISO will face in 2025-2026. AI agents are no longer assistants - they ARE the security program. And there's been no way to prove they're effective. Until now.

---

## SLIDE 3: The Paradigm Shift

**Visual:** Timeline showing evolution from manual to AI-operated security

# Security Has Fundamentally Changed

```
1990-2020: Humans DO security
2020-2024: Humans + AI assistance
2025+:     AI agents DO security, humans OVERSEE
```

**The New Reality:**
- Darktrace AI → Autonomously blocks threats
- GitHub Copilot Autofix → Auto-merges security fixes
- AI GRC Tools → Generates compliance evidence
- Wiz AI → Runs continuous pentesting

**The Gap:**
- ISO 27001 assesses human controls
- NIST CSF assesses human processes
- OWASP SAMM assesses human development
- **Nothing assesses AI-operated security**

Until HAIAMM.

**Speaker Notes:**
We've crossed a threshold. AI agents aren't helping with security anymore - they ARE the security team. A Darktrace agent makes thousands of decisions per hour without human approval. This is a fundamentally different operating model, and it needs a fundamentally different assurance framework.

---

## SLIDE 4: Why This Matters (The Risk Amplification Problem)

**Visual:** Scale showing human mistake (small) vs AI mistake (massive amplification)

# AI Security Failures Scale Catastrophically

| Human Analyst | AI Agent |
|---------------|----------|
| Misses 1 vulnerability | Misses vulnerability CLASS |
| 1 system at risk | 1,200 systems at risk |
| Hours to impact | Milliseconds to impact |
| Can be retrained | Requires architecture change |

## Real 2024-2025 Incidents:

**GraphQL Blind Spot:** AI testing agent trained only on REST missed ALL GraphQL injection vulnerabilities. 200+ critical vulns ignored for 9 months. Breach cost: $4M+

**Compliance Hallucination:** AI compliance agent fabricated encryption evidence for 6 months. HIPAA audit failure. Fine: $2M

**Agent Gap Attack:** 5 AI security agents with zero coordination. Attacker exploited unmonitored API gateway between their domains. Payment data stolen.

**Speaker Notes:**
These are real incidents from organizations that trusted their AI security tools without verification. The common thread: no framework existed to assess if AI agents were actually effective. That's the gap HAIAMM fills.

---

## SLIDE 5: Introducing HAIAMM v2.0

**Visual:** Framework structure diagram with OWASP alignment highlighted

# HAIAMM: The Framework

**Human-Assisted Intelligence Assurance Maturity Model**

```
┌─────────────────────────────────────────────────────────────┐
│                    HAIAMM v2.0 FRAMEWORK                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │  6 DOMAINS   │  │ 12 PRACTICES │  │  3 LEVELS    │      │
│  ├──────────────┤  ├──────────────┤  ├──────────────┤      │
│  │ Software     │  │ SM PC EG     │  │ L1 Foundation│      │
│  │ Infrastructure│ │ TA SR SA     │  │ L2 Structured│      │
│  │ Endpoints    │  │ DR IR ST     │  │ L3 Optimized │      │
│  │ Data         │  │ IM EH ML     │  │              │      │
│  │ Processes    │  └──────────────┘  └──────────────┘      │
│  │ Vendors      │                                          │
│  └──────────────┘  ┌──────────────────────────────────┐    │
│                    │     OWASP TOP 10 ALIGNMENT       │    │
│                    ├──────────────────────────────────┤    │
│                    │ LLM Risks (LLM01-LLM10) mapped   │    │
│                    │ Agentic Risks (ASI01-ASI10) mapped│   │
│                    └──────────────────────────────────┘    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**What's New in v2.2:**
- Full OWASP Top 10 for LLM Applications 2025 mapping
- Full OWASP Top 10 for Agentic Applications 2026 mapping
- Measurable outcomes with formulas and data sources
- Modular handbook with Quick Start Guide

**Speaker Notes:**
Version 2.0 represents a major evolution. We've mapped every OWASP risk to specific practices with measurable outcomes. You don't just know what to do - you know exactly how to measure success.

---

## SLIDE 6: Introducing Verifhai

**Visual:** Interactive CLI/chat interface, mentor icon

# Verifhai: The Interactive Mentor

**From Assessment to Action**

```
┌─────────────────────────────────────────────────────────────┐
│                    VERIFHAI INTERFACE                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  > /verifhai start                                          │
│                                                             │
│  Welcome to Verifhai! I'll help you build security INTO     │
│  your AI system, not bolt it on after.                      │
│                                                             │
│  What are you building?                                     │
│  [1] LLM Application (chatbot, copilot, RAG)               │
│  [2] AI Agent (autonomous, tool-using)                      │
│  [3] ML Pipeline (training, inference)                      │
│                                                             │
│  > 2                                                        │
│                                                             │
│  AI Agents carry higher risk. Let's start with Security     │
│  Requirements (SR) - defining what your agent CAN, CANNOT,  │
│  and MUST do...                                             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Verifhai Commands:**
| Command | What It Does |
|---------|--------------|
| `/verifhai start` | Begin security journey for new AI project |
| `/verifhai assess` | Quick maturity assessment (10 min) |
| `/verifhai practice sr` | Build Security Requirements interactively |
| `/verifhai review` | Review code for AI-specific vulnerabilities |
| `/verifhai status` | Check progress across all practices |
| `/verifhai measure` | Full maturity measurement with scores |

**Speaker Notes:**
Verifhai is where the framework comes alive. It's an interactive mentor that guides you through building security into your AI systems. Not a questionnaire - a hands-on partner that helps you create actual security artifacts.

---

## SLIDE 7: HAIAMM + Verifhai = Complete Solution

**Visual:** Two puzzle pieces fitting together

# The Framework + The Tool

| HAIAMM | Verifhai |
|--------|----------|
| **What** to secure | **How** to build it |
| Assessment framework | Interactive mentor |
| 432 questions | Guided activities |
| Maturity scores | Security artifacts |
| Periodic measurement | Day-to-day guidance |

## Together They Solve:

1. **"What should we measure?"** → HAIAMM's 12 practices with OWASP mapping
2. **"How do we actually do it?"** → Verifhai's guided workflows
3. **"How do we prove it?"** → Measurable outcomes with formulas
4. **"How do we improve?"** → Maturity progression L1→L2→L3

**Speaker Notes:**
Think of HAIAMM as the curriculum and Verifhai as the tutor. HAIAMM defines what good looks like. Verifhai helps you build it. Most frameworks stop at assessment. We continue through implementation.

---

## SLIDE 8: OWASP Agentic Top 10 Alignment

**Visual:** Risk matrix with practice mappings

# Mapping Real Risks to Real Practices

**OWASP Top 10 for Agentic Applications 2026 - Now with Measurable Outcomes**

| Risk | Description | Primary Practices | Measurement |
|------|-------------|-------------------|-------------|
| **ASI01** | Agent Goal Hijack | TA, SR, ST, ML | >90% hijack detection rate |
| **ASI02** | Tool Misuse | SA, PC, ML | <5% unauthorized tool use |
| **ASI03** | Identity Abuse | SR, EH, ML | 100% least-privilege |
| **ASI04** | Supply Chain | TA, SA, IM | 100% provenance verified |
| **ASI05** | Code Execution | SR, ST, EH | 100% sandboxed |
| **ASI06** | Memory Poisoning | DR, ST, EH | >95% tamper detection |
| **ASI07** | Inter-Agent Comm | SA, SR, ML | 100% authenticated |
| **ASI08** | Cascading Failures | SA, IM, ML | <15 min containment |
| **ASI09** | Trust Exploitation | EG, PC, ML | >80% user awareness |
| **ASI10** | Rogue Agents | TA, ML, IM | MTTD <4 hours |

**Every risk mapped. Every practice defined. Every outcome measurable.**

**Speaker Notes:**
This is the strategic value. Your security team no longer needs to guess which controls address which risks. We've done the mapping. And more importantly, we've defined what success looks like with specific, measurable targets.

---

## SLIDE 9: Sample Measurable Outcome

**Visual:** Measurement dashboard mockup

# From Abstract to Concrete

## Example: ASI01 - Agent Goal Hijack

**Risk:** Attackers manipulate AI agent goals through prompt injection or context manipulation.

**Measurable Outcome:**

```
┌─────────────────────────────────────────────────────────────┐
│  GOAL HIJACK DETECTION RATE                                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Target: >90% of goal hijack attempts detected before       │
│          action execution                                   │
│                                                             │
│  Formula:                                                   │
│  Detection Rate = (Detected Attempts / Total Attempts) × 100│
│                                                             │
│  Data Sources:                                              │
│  - Security testing results (red team exercises)            │
│  - Production monitoring alerts                             │
│  - Incident reports                                         │
│                                                             │
│  Validation:                                                │
│  - Monthly red team exercises with injection attempts       │
│  - Quarterly third-party validation                         │
│                                                             │
│  Current: 73%  │████████████████░░░░│  Target: 90%         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Speaker Notes:**
This is what makes HAIAMM v2.0 different. We don't just say "implement goal integrity checking." We define the measurement formula, the data sources, and the validation method. This is what auditors and boards actually need.

---

## SLIDE 10: The 12 Practices

**Visual:** 4x3 grid with function groupings

# 12 Practices Across 4 Business Functions

![Governance](images/governance_small_logo.png) **GOVERNANCE** - How you govern AI security agents
| Practice | Focus |
|----------|-------|
| **SM** Strategy & Metrics | Security strategy, KPIs, ROI |
| **PC** Policy & Compliance | Policies, standards, regulations |
| **EG** Education & Guidance | Training, awareness, culture |

![Building](images/building_small_logo.png) **BUILDING** - How you build AI agents securely
| Practice | Focus |
|----------|-------|
| **TA** Threat Assessment | Threat modeling, AI-specific risks |
| **SR** Security Requirements | CAN/CANNOT/MUST definitions |
| **SA** Secure Architecture | Defense-in-depth, isolation |

![Verification](images/verification_small_logo.png) **VERIFICATION** - How you verify AI agents work correctly
| Practice | Focus |
|----------|-------|
| **DR** Design Review | Architecture security reviews |
| **IR** Implementation Review | Code and config security |
| **ST** Security Testing | AI-specific testing, red team |

![Operations](images/operations_small_logo.png) **OPERATIONS** - How you run AI agents safely
| Practice | Focus |
|----------|-------|
| **IM** Issue Management | Vulnerability tracking, incidents |
| **EH** Environment Hardening | Sandboxing, isolation |
| **ML** Monitoring & Logging | Detection, alerting, forensics |

**Speaker Notes:**
Twelve practices organized into four business functions. Each practice has specific Level 1, 2, and 3 objectives. Each maps to specific OWASP risks. Each has measurable outcomes.

---

## SLIDE 11: Verifhai in Action - Building Security Requirements

**Visual:** Interactive session screenshot

# Verifhai Workflow: Security Requirements (SR)

```
> /verifhai practice sr

Starting Security Requirements builder for your AI Agent.

Step 1: Define Agent Purpose
What is this agent designed to do? (1-2 sentences)
> Process customer support tickets and escalate urgent issues

Step 2: Define CANNOT List (Hard Limits)
What should this agent NEVER do? I'll suggest based on purpose:
- [ ] Access production databases directly
- [ ] Send external communications without approval
- [ ] Modify its own configuration
- [ ] Access credentials or secrets
> Add: Delete or modify customer data

Step 3: Define CAN List (Permitted Actions)
What IS this agent allowed to do?
> Read tickets, classify priority, route to teams, send internal notifications

Step 4: Define MUST List (Required Behaviors)
What MUST this agent always do?
> Log all actions, verify before escalation, stay within ticket scope

Generating security-requirements.md...

Created: security-requirements.md
Your agent now has a formal permission model.
L1 Security Requirements: ACHIEVED
```

**Speaker Notes:**
This is Verifhai turning assessment into action. Instead of asking "Do you have security requirements?" it helps you CREATE them. The output is a real document your team can use. This is learn-by-doing security.

---

## SLIDE 12: Verifhai in Action - Code Review

**Visual:** Code analysis output

# Verifhai Workflow: AI Security Code Review

```
> /verifhai review

Analyzing code in context for AI-specific vulnerabilities...

┌─────────────────────────────────────────────────────────────┐
│  VERIFHAI SECURITY REVIEW                                   │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  [HIGH] ASI02 - Tool Misuse Risk                           │
│  Line 45: execute_tool(user_input)                          │
│  Issue: Unsanitized user input passed to tool executor      │
│  Fix: Validate against approved tool list before execution  │
│                                                             │
│  [MEDIUM] ASI01 - Goal Hijack Risk                         │
│  Line 23: agent.set_goal(request.context)                   │
│  Issue: No goal integrity validation                        │
│  Fix: Add goal hash verification before execution           │
│                                                             │
│  [LOW] LLM07 - Prompt Leakage Risk                         │
│  Line 12: response.include(system_prompt)                   │
│  Issue: System prompt exposed in error responses            │
│  Fix: Sanitize error outputs before returning               │
│                                                             │
│  Summary: 1 High, 1 Medium, 1 Low                          │
│  Would you like help fixing the HIGH issue first?           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Speaker Notes:**
Verifhai isn't just a questionnaire - it's an active security partner. It reviews actual code for AI-specific vulnerabilities mapped to OWASP risks. It doesn't just identify issues - it explains why they matter and how to fix them.

---

## SLIDE 13: Quick Start Guide

**Visual:** Decision tree flowchart

# Get Started in 10 Minutes

```
                    ┌─────────────────────────────────────┐
                    │     What are you working on?        │
                    └─────────────────┬───────────────────┘
                                      │
            ┌─────────────────────────┼─────────────────────────┐
            │                         │                         │
            ▼                         ▼                         ▼
    ┌───────────────┐       ┌─────────────────┐       ┌─────────────────┐
    │ LLM App       │       │ AI Agents       │       │ AI Security     │
    │ (chatbot,     │       │ (autonomous,    │       │ Program         │
    │ copilot, RAG) │       │ tool-using)     │       │ (enterprise)    │
    └───────┬───────┘       └────────┬────────┘       └────────┬────────┘
            │                        │                         │
            ▼                        ▼                         ▼
    ┌───────────────┐       ┌─────────────────┐       ┌─────────────────┐
    │ Top 10 LLM    │       │ Top 10 Agentic  │       │ First 30 Days   │
    │ Risks         │       │ Risks           │       │ Roadmap         │
    └───────────────┘       └─────────────────┘       └─────────────────┘
```

**5 Quick Wins You Can Do Today:**
1. Inventory all AI systems (30 min)
2. Add input validation to LLM endpoints (30 min)
3. Enable output logging with PII redaction (20 min)
4. Restrict agent permissions (30 min)
5. Define your "kill switch" procedure (15 min)

**Speaker Notes:**
The handbook includes a Quick Start Guide inspired by OWASP's approach. You can start improving security in 10 minutes with no budget. The 5 Quick Wins are actionable steps any team can implement today.

---

## SLIDE 14: First 30 Days Roadmap

**Visual:** Weekly timeline with milestones

# From Zero to Level 1 in 30 Days

| Week | Focus | Key Deliverables |
|------|-------|------------------|
| **Week 1** | Discovery | AI system inventory, ownership assigned, risk ranking |
| **Week 2** | Foundation | Threat assessment (TA L1), Security requirements (SR L1) |
| **Week 3** | Controls | Environment hardening (EH L1), Monitoring setup (ML L1) |
| **Week 4** | Governance | Policies documented (PC L1), Metrics baseline (SM L1) |

**Day-by-Day Guidance:**
- Day 1: Create AI system inventory template
- Day 2: Document all LLM/agent systems
- Day 3: Categorize by capability (tool access, data access, autonomy)
- Day 4: Assign ownership for each system
- Day 5: Initial risk ranking workshop
- ... (29 more days fully documented)

**Speaker Notes:**
The First 30 Days guide is the onramp for new teams. Every day has specific actions, deliverables, and time estimates. By Day 30, you've achieved Level 1 maturity across core practices and have a measurable baseline.

---

## SLIDE 15: Tiered Assessment Model

**Visual:** 3 tiers as building blocks

# Scale Assessment to Your Needs

| Tier | Time | Questions | Coverage | Use Case |
|------|------|-----------|----------|----------|
| **Tier 1** | 20-30 min | 24 | 2 domains | Quick baseline, exec briefing |
| **Tier 2** | 3-4 hours | 192 | 4 domains | Operational assessment |
| **Tier 3** | 12-16 hours | 432 | 6 domains | Full maturity certification |

**Assessment Flow:**

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Tier 1    │ ──► │   Tier 2    │ ──► │   Tier 3    │
│  Quick Check│     │ Operational │     │    Full     │
│  (20 min)   │     │  (3-4 hrs)  │     │ (12-16 hrs) │
└─────────────┘     └─────────────┘     └─────────────┘
      │                   │                   │
      ▼                   ▼                   ▼
   Baseline            Roadmap          Certification
   Score              Development       Documentation
```

**Speaker Notes:**
Start with Tier 1 today - it takes 20 minutes. You'll immediately see where your gaps are. Then progress to Tier 2 for detailed operational assessment. Tier 3 is for official certification and regulatory compliance.

---

## SLIDE 16: The ROI Case

**Visual:** ROI calculation with before/after

# Investment vs. Return

**Investment:**
| Activity | Cost | Time |
|----------|------|------|
| Self-assessment (Tier 1-2) | $0 | 4 hours |
| First 30 Days implementation | Internal effort | 30 days |
| Official certification | $50K-$150K | 4-8 weeks |

**Returns:**

| Outcome | Value |
|---------|-------|
| Prevent 1 AI-related breach | $4M+ avoided |
| Avoid regulatory fine | $2M+ avoided |
| Insurance discount | $50K-$100K/year |
| Board confidence | Priceless |
| Competitive advantage | Market differentiation |

**ROI Calculation:**
- Certification cost: $100K
- Breach prevention: $4M
- **ROI: 40x**

**Speaker Notes:**
The math is simple. One AI security incident costs millions. Certification costs tens of thousands. Even if you only prevent one incident over three years, the ROI is 40x. And you get insurance discounts, regulatory compliance, and board confidence as bonuses.

---

## SLIDE 17: Regulatory Timeline

**Visual:** Timeline with regulatory milestones

# Compliance is Coming - Be Ready

```
2025                2026                2027                2028
──┼───────────────────┼───────────────────┼───────────────────┼──►
  │                   │                   │                   │
  │                   │                   │                   │
  ▼                   ▼                   ▼                   ▼
HAIAMM 2.2        EU AI Act          Insurance           Global
Launch            Enforcement         Mandates            Standard

Early             Compliance          Premium             Table
Adopters          Required            Discounts           Stakes
```

**Key Deadlines:**
- **June 2026:** EU AI Act enforcement for high-risk AI
- **2027:** Cyber insurance will require AI security evidence
- **2028:** SOC 2 / ISO 27001 auditors will expect AI governance

**First Mover Advantage:**
- 18-month window before mandatory compliance
- Early adopters set the standard
- Build competitive moat now

**Speaker Notes:**
The EU AI Act is not optional. High-risk AI systems making security decisions will require documented oversight. Insurance companies are already asking about AI governance. By 2028, this will be table stakes. Organizations that get certified now have an 18-month head start.

---

## SLIDE 18: Accountability Framework

**Visual:** Courtroom/boardroom scene

# When AI Fails, Who's Responsible?

**Scenario:** AI testing agent misses critical RCE. Breach. $10M loss.

**Questions from Board/Regulators:**
- Who approved the AI agent?
- How was it validated?
- What oversight existed?
- Why didn't humans catch it?
- **Was due diligence performed?**

**Without HAIAMM:**
| Question | Answer |
|----------|--------|
| Framework used? | None |
| Evidence of oversight? | Informal |
| Proof of reasonable care? | Can't demonstrate |
| Liability? | Personal exposure |

**With HAIAMM + Verifhai:**
| Question | Answer |
|----------|--------|
| Framework used? | HAIAMM Level 2 certified |
| Evidence of oversight? | Assessment documentation |
| Proof of reasonable care? | Industry standard compliance |
| Liability? | Due diligence demonstrated |

**Speaker Notes:**
This is about protecting yourself and your organization. When an AI security agent fails - and they will - you need to show due diligence. HAIAMM provides the reasonable person standard. Verifhai provides the implementation evidence. Together, they're your defense.

---

## SLIDE 19: What You Get (Free)

**Visual:** GitHub repo, documentation site, Verifhai interface

# Completely Free - Start Today

**HAIAMM Framework (Open Source):**
- Complete v2.2 framework
- 12 practices × 6 domains × 3 levels
- 432 assessment questions
- OWASP Top 10 mappings (LLM + Agentic)
- Measurable outcomes with formulas

**HAIAMM Handbook:**
- Quick Start Guide (10 min)
- First 30 Days Roadmap
- Risk-Practice Matrix
- Assessment Checklist
- Tools & Resources Guide

**Verifhai Interactive Tool:**
- `/verifhai start` - Begin journey
- `/verifhai assess` - Quick assessment
- `/verifhai practice` - Build security artifacts
- `/verifhai review` - Code security review
- `/verifhai measure` - Full maturity measurement

**No barriers. No vendor lock-in. Start now.**

**Speaker Notes:**
Let me be explicit - everything you need to assess and improve your AI security is free. Download it today. Run an assessment. Build security requirements. Review your code. You only pay when you want official third-party certification.

---

## SLIDE 20: What You Pay For

**Visual:** Certification badge, professional services

# Professional Services (When You Need Validation)

**Official HAIAMM Certification ($50K-$150K)**
- Third-party expert assessment
- "HAIAMM Level X Certified" credential
- Industry benchmarking data
- Regulatory compliance evidence
- Insurance documentation
- Public certification badge

**Training & Workshops ($1K-$5K/person)**
- Certified HAIAMM Assessor training
- Executive AI security briefings
- Team workshops

**Consulting ($15K-$50K/month)**
- Gap remediation acceleration
- AI agent security architecture
- Custom implementation support

**Enterprise Platform ($10K-$50K/year)**
- Multi-user collaboration
- Continuous monitoring
- Benchmarking database access

**Speaker Notes:**
Professional services provide two things: expertise and validation. When auditors need evidence, when insurance needs documentation, when the board needs third-party confirmation - that's when certification has ROI. Everything else you can do yourself.

---

## SLIDE 21: Three Ways to Start

**Visual:** Three paths with icons

# Choose Your Entry Point

**Option 1: Free Self-Assessment (Today)**
```
1. Download HAIAMM from GitHub
2. Run /verifhai assess (10 minutes)
3. Review gaps and scores
4. Build improvement roadmap
Cost: $0 | Timeline: 1 day
```

**Option 2: First 30 Days Program (This Month)**
```
1. Follow day-by-day guide
2. Achieve Level 1 maturity
3. Create security artifacts
4. Establish baseline metrics
Cost: Internal effort | Timeline: 30 days
```

**Option 3: Official Certification (This Quarter)**
```
1. Contact for assessment
2. Expert-led evaluation
3. Receive certification
4. Use for compliance
Cost: $50K-$150K | Timeline: 4-8 weeks
```

**Speaker Notes:**
I recommend starting with Option 1 today. Takes 10 minutes. You'll immediately see where you stand. Then follow the First 30 Days to build your foundation. When you need official validation for auditors or insurance, engage for certification.

---

## SLIDE 22: Call to Action

**Visual:** Bold CTA, QR codes, contact info

# Your AI Agents Are Making Security Decisions Right Now

## Are They Making the Right Ones?

**Start Free:**
- GitHub: [repository URL]
- Documentation: [docs URL]
- Command: `/verifhai start`

**Get Certified:**
- Contact: [email]
- Website: [URL]

**Join the Community:**
- Discord: [link]
- Contributing: [guidelines URL]

---

**HAIAMM + Verifhai**
*The Framework + The Tool for AI-Operated Security*

**Speaker Notes:**
Thank you. Your AI security agents are running right now - making decisions, blocking threats, generating evidence. The question is: do you know if they're doing it correctly? HAIAMM + Verifhai gives you the answer. Download it today, start your assessment, and join us in defining the standard for AI-operated security assurance.

---

## SLIDE 23: Q&A

**Visual:** Question marks, HAIAMM + Verifhai logos

# Questions?

**Resources:**
- Framework: [GitHub URL]
- Documentation: [Handbook URL]
- Verifhai: [Tool URL]
- Contact: [Email]
- Community: [Discord/Slack]

**Common Questions:**
- "How long does certification take?" → 4-8 weeks
- "Can we customize the framework?" → Yes, extend with custom domains
- "How does it integrate with existing tools?" → API and export options
- "What if we're already using NIST/ISO?" → Complementary, not competing

---

## APPENDIX A: Framework Comparison

**Visual:** Detailed comparison matrix

# HAIAMM vs. Other Frameworks

| Aspect | HAIAMM | NIST AI RMF | ISO 27001 | OWASP LLM Top 10 |
|--------|--------|-------------|-----------|------------------|
| **Focus** | AI-operated security | AI system security | General security | LLM vulnerabilities |
| **Assesses AI agents doing security?** | ✅ Yes | ❌ No | ❌ No | ❌ No |
| **Measurable outcomes?** | ✅ With formulas | ⚠️ General guidance | ⚠️ Controls only | ❌ Risks only |
| **Interactive tool?** | ✅ Verifhai | ❌ No | ❌ No | ❌ No |
| **Implementation guidance?** | ✅ First 30 Days | ⚠️ Playbook | ❌ No | ⚠️ Mitigations |
| **Open Source?** | ✅ 100% | ✅ Yes | ❌ Paid | ✅ Yes |

**HAIAMM complements these frameworks - it doesn't replace them.**

---

## APPENDIX B: The 12 Practices Detail

**Visual:** Practice cards with OWASP mappings

# Practices × OWASP Risk Coverage

| Practice | Agentic Risks Addressed | LLM Risks Addressed |
|----------|------------------------|---------------------|
| **SM** Strategy & Metrics | Secondary for all | Secondary for all |
| **PC** Policy & Compliance | ASI02, ASI09 | LLM02, LLM06 |
| **EG** Education & Guidance | ASI09 | None primary |
| **TA** Threat Assessment | ASI01, ASI04, ASI10 | LLM04 |
| **SR** Security Requirements | ASI01, ASI03, ASI05, ASI07 | LLM01, LLM05, LLM10 |
| **SA** Secure Architecture | ASI02, ASI04, ASI07, ASI08 | LLM03, LLM06, LLM08 |
| **DR** Design Review | ASI06 | LLM02, LLM04, LLM09 |
| **IR** Implementation Review | ASI05 | LLM05 |
| **ST** Security Testing | ASI01, ASI05, ASI06 | LLM01, LLM04, LLM05, LLM07, LLM08, LLM09 |
| **IM** Issue Management | ASI04, ASI08, ASI10 | LLM03 |
| **EH** Environment Hardening | ASI03, ASI05, ASI06, ASI07 | LLM01, LLM03, LLM07, LLM08, LLM10 |
| **ML** Monitoring & Logging | ASI01-ASI10 (all) | LLM02, LLM06, LLM07, LLM09, LLM10 |

---

## APPENDIX C: Sample Assessment Questions

**Visual:** Question examples by level

# Assessment Questions by Maturity Level

**Security Requirements (SR) - Sample:**

| Level | Question |
|-------|----------|
| L1 | Does the AI agent have documented CAN/CANNOT/MUST boundaries? |
| L1 | Are critical actions (write, execute, send) explicitly listed? |
| L2 | Are security requirements derived from formal threat assessment? |
| L2 | Are requirements testable with specific acceptance criteria? |
| L3 | Are requirements automatically verified in CI/CD pipeline? |
| L3 | Do requirements cover emerging AI-specific risks (ASI01-10)? |

**Scoring:** Each question: Yes (1) | Partial (0.5) | No (0)

**Maturity Calculation:**
- Level 1: Average L1 score ≥ 2.0
- Level 2: L1 achieved + average L2 score ≥ 2.0
- Level 3: L2 achieved + average L3 score ≥ 2.0

---

## APPENDIX D: Verifhai Technical Architecture

**Visual:** System architecture diagram

# Verifhai Integration

```
┌──────────────────────────────────────────────────────────────┐
│                    HAI SECURITY ECOSYSTEM                     │
├──────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌─────────────────────┐      ┌─────────────────────────────┐│
│  │  Verifhai Skill     │      │  HAIAMM Framework           ││
│  │  (Claude Code)      │      │  (JSON Data Model)          ││
│  ├─────────────────────┤      ├─────────────────────────────┤│
│  │ - Interactive guide │      │ - 6 domains                 ││
│  │ - Code review       │◄────►│ - 12 practices              ││
│  │ - Practice builders │      │ - 432 questions             ││
│  │ - Real-time mentor  │      │ - OWASP mappings            ││
│  └─────────────────────┘      └─────────────────────────────┘│
│              │                            │                   │
│              └────────────┬───────────────┘                   │
│                           │                                   │
│                           ▼                                   │
│              ┌─────────────────────────┐                     │
│              │    Security Artifacts   │                     │
│              ├─────────────────────────┤                     │
│              │ - security-requirements │                     │
│              │ - threat-assessment.md  │                     │
│              │ - architecture-review   │                     │
│              │ - test-results.json     │                     │
│              └─────────────────────────┘                     │
│                                                               │
└──────────────────────────────────────────────────────────────┘
```

---

## APPENDIX E: Roadmap Priorities by Risk Profile

**Visual:** Priority matrix

# Where to Start Based on Your Risk

**If you're deploying AI Agents (highest risk):**
1. Start: SR (Security Requirements) - Define boundaries
2. Then: ST (Security Testing) - Test for ASI01-10
3. Then: ML (Monitoring & Logging) - Detect anomalies

**If you're running LLM Applications:**
1. Start: EH (Environment Hardening) - Prevent injection
2. Then: ST (Security Testing) - Test for LLM01-10
3. Then: DR (Design Review) - Architecture validation

**If you're establishing an AI Security Program:**
1. Start: SM (Strategy & Metrics) - Define goals
2. Then: PC (Policy & Compliance) - Set policies
3. Then: TA (Threat Assessment) - Understand risks

**All paths lead to Level 1 maturity within 30 days.**

---

**END OF DECK**

---

## Presentation Notes

**Total Slides:** 23 core + 5 appendix
**Presentation Time:** 20-25 minutes (core slides only)
**Target Audience:** CISOs, security leaders, AI/ML engineering leads, board members

**Delivery Tips:**
1. Open strong with the $4M question (Slide 2)
2. Use real incident stories (Slide 4) to create urgency
3. Demo Verifhai live if possible (Slides 11-12)
4. Emphasize "free to try" throughout
5. End with clear three-path call to action (Slide 21)

**Adaptation Options:**
- **10-minute version:** Slides 1, 2, 5-7, 13, 19, 22
- **Executive version:** Focus on ROI and accountability (Slides 16-18)
- **Technical version:** Include all appendix slides
- **Verifhai demo:** Expand Slides 11-12 with live demonstration

**Key Messages:**
1. AI agents ARE the security team now - they need assessment
2. HAIAMM is the framework, Verifhai is the tool
3. Everything is free to start - certification when you need validation
4. OWASP alignment provides strategic risk coverage
5. Measurable outcomes, not just checkboxes
