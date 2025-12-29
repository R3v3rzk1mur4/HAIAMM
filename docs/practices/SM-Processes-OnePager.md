# Strategy & Metrics (SM)
## Processes Domain - HAIAMM v2.1

---

### Practice Overview

**Objective:** Establish unified strategic roadmap for AI-operated security processes within the organization

**Description:** Build and maintain a Human-Assisted Intelligence Assurance program to better understand and manage risks when AI agents operate critical security workflow functions such as incident response automation, compliance reporting, security metrics tracking, vulnerability management, change management, and GRC (Governance, Risk, Compliance) processes.

**Context:** Organizations increasingly deploy AI agents to automate security processes - from AI-generated compliance reports to automated incident triage, AI-driven vulnerability prioritization, and intelligent security awareness training delivery. This practice ensures strategic oversight of these AI process operations, measuring their effectiveness and aligning AI agent workflow automation with business operations and regulatory requirements.

---

## Maturity Level 1
### Objective: Establish unified roadmap for security processes operated by AI

At this level, organizations recognize that AI agents are performing security workflow and process automation work, and establish basic strategic oversight.

#### Activities

**A) Estimate overall risk in the context of AI-operated security processes**

Create an inventory of AI agents operating security workflows and processes. Identify critical security operations where AI agents make process decisions or automate workflows. Document potential failure scenarios: What happens if an AI agent incorrectly triages a critical security incident as low priority? Generates an inaccurate compliance report? Fails to escalate a vulnerability requiring urgent remediation?

Conduct initial risk assessment considering:
- Business impact of AI process errors (missed critical incidents, failed audits, delayed vulnerability remediation)
- Operational dependencies on AI-automated security processes (can humans take over if AI fails?)
- Human oversight gaps in current AI process operations (who reviews AI-generated reports, AI triage decisions?)
- Compliance requirements for process documentation and auditability (SOC 2, ISO 27001, regulatory audits)
- Potential for AI workflow automation to introduce blind spots (processes AI handles that humans no longer review)

**B) Build and maintain Human-Assisted Intelligence Assurance programs**

Develop a strategic roadmap for governing AI agents that operate security processes and workflows. Define executive sponsorship (typically CISO or Head of Security Operations), establish governance structure, and create a plan for implementing human oversight of AI process automation.

Key elements:
- Identify executive sponsor for AI security process automation program
- Document current state: Which AI tools/agents automate security workflows? (incident response, compliance, vulnerability management, metrics)
- Define target state: What level of AI process autonomy is acceptable for different security operations?
- Create 12-18 month roadmap for implementing AI process governance
- Establish basic metrics: How many AI agents? What processes do they automate? What is the human backup plan?
- Address auditability: How will AI-automated processes be documented for compliance audits?

**C) Establish foundational threat intelligence for AI process security**

Identify threat intelligence requirements and integrate basic threat intelligence consumption to inform AI-operated security process decisions.

**Processes Domain Threat Intelligence Requirements**:

**Threat Intelligence Types for Process Security**:
- **Incident Response Intelligence**: What incident patterns are emerging? (DFIR research, incident reports)
- **SOAR Intelligence**: What automation bypass techniques exist? (security automation research, process attack patterns)
- **Detection Evasion Intelligence**: What techniques evade security monitoring? (alert fatigue, correlation evasion)
- **Operational Failure Intelligence**: What AI security process failures have occurred? (vendor advisories, lessons learned)

**Foundational Threat Intelligence Sources**:

**Free/Open-Source Sources**:
- **SANS Incident Handler Diary**: Daily incident response intelligence (free)
- **DFIR Blogs**: Digital forensics and incident response research (free)
- **SOAR Vendor Blogs**: Security automation best practices (free)
- **Security Operations Research**: SOC research, automation trends (free)

**Commercial Sources** (optional):
- **SOAR Vendor Intelligence**: Palo Alto Cortex XSOAR, Splunk SOAR threat intelligence (paid)
- **Incident Response Intelligence**: Mandiant, CrowdStrike IR intelligence (paid)

**Integration Patterns**:
- **Pattern 1: Incident Enrichment**: AI triages incident → Threat intelligence: Similar incident pattern seen in 47 recent attacks → Escalate priority
- **Pattern 2: Process Validation**: AI automates response → Threat intelligence: This playbook bypassed in recent attacks → Add human validation

**Foundational Metrics**:
- **Coverage**: ≥70% of security processes informed by threat intelligence
- **Freshness**: ≤24 hours for critical process intelligence
- **Process Improvement**: ≥20% increase in detecting process attacks

---

## Maturity Level 2
### Objective: Classify security processes and measure AI agent effectiveness by criticality

At this level, organizations differentiate security processes by operational criticality and regulatory importance, tailoring AI agent oversight based on process classification.

#### Activities

**A) Classify security processes based on AI operational risk and business criticality**

Segment security processes into risk tiers based on business impact, regulatory requirements, and AI agent autonomy. High-criticality processes (incident response, regulatory compliance reporting, critical vulnerability remediation) require stricter AI oversight than low-criticality processes (routine metrics collection, basic security awareness delivery).

Process classification considers:
- **Business criticality**: Impact of process failure (critical incident missed, compliance violation, SLA breach)
- **Regulatory scope**: Processes required for SOC 2, ISO 27001, HIPAA, PCI-DSS, industry audits
- **Operational dependencies**: Can business operations continue if this AI-automated process fails?
- **AI agent autonomy**: Degree of human review/approval required for AI process decisions
- **Error consequence**: Cost of AI mistakes in this process (financial, reputational, regulatory)

Example classification with AI oversight:
- **Critical (Incident Response, Compliance Reporting)**: AI agents support/recommend, humans approve all critical decisions and final reports
- **High (Issue Management, Change Control)**: AI agents prioritize and automate routine tasks, humans review high-impact decisions within 24 hours
- **Medium (Security Metrics, Training Delivery)**: AI agents operate autonomously with weekly human review of outputs and quality
- **Low (Routine Scanning, Basic Reporting)**: AI agents operate fully autonomously with monthly audit

**B) Establish and measure per-classification AI process automation goals**

Define specific effectiveness metrics for AI agents operating at each process criticality level. Track whether AI process automation is actually improving security operations efficiency and effectiveness, not just generating activity.

Metrics by process classification:
- **Triage accuracy**: % of incidents AI correctly prioritizes (validated against human expert review)
- **Process completion rate**: % of automated workflows AI successfully completes without human intervention
- **False escalation rate**: % of AI escalations that were unnecessary (alert fatigue for human reviewers)
- **Time savings**: Reduction in manual effort for process execution (hours saved per week/month)
- **Quality metrics**: Accuracy of AI-generated reports, completeness of AI-automated workflows
- **Human override rate**: How often humans must correct or reject AI process decisions

Example goals:
- Critical processes (Incident Response): AI triage accuracy >90%, 100% human approval for high-severity incidents, <5% false escalations
- High processes (Issue Management): AI prioritization matches expert judgment >85% of time, reduces manual triage effort by 60%
- Medium processes (Security Metrics): AI-generated reports >95% accurate (validated by sampling), reduce reporting time by 70%

**C) Classify process threats by organizational relevance and measure threat intelligence ROI**

**Process Threat Classification**:

**Critical Process Threats**:
- **Active attacks on AI security processes**: Threat actors targeting SOAR platforms, incident response automation
- **Automation bypass techniques affecting your tools**: Techniques that evade your SOAR/SIEM/EDR automation
- **Operational dependencies at risk**: Critical security processes that could fail (alert fatigue, correlation overload)
- **AI Response**: Immediate process hardening, human validation ≤1 hour, emergency failover testing
- **Update Frequency**: Real-time

**High-Relevance Threats**:
- **Emerging detection evasion techniques**: New methods to bypass security monitoring
- **Incident response challenges in your environment**: IR challenges specific to your infrastructure type
- **AI Response**: Enhanced monitoring, process review ≤24 hours
- **Update Frequency**: Daily

**Cross-Domain Correlation**:
- **Processes ↔ Endpoints**: Incident response automation + Endpoint evasion = Detection gap
- **Processes ↔ Infrastructure**: SOAR automation + Infrastructure attack = Bypass opportunity

**Threat Intelligence ROI for Process Security**:
- **Investment**: SOAR intelligence, IR research subscriptions, automation advisories
- **Value**: Faster incident response, reduced automation bypass, operational resilience
- **Target ROI**: ≥3:1

---

## Maturity Level 3
### Objective: Align AI process automation investment with demonstrable operational efficiency and security effectiveness

At this level, organizations prove ROI of AI-operated security processes through data-driven metrics, operational efficiency gains, and security outcome improvements.

#### Activities

**A) Conduct periodic industry-wide cost comparisons for AI process automation**

Benchmark AI security process automation costs and effectiveness against industry peers and operational standards. Compare security operations outcomes (incident response time, vulnerability remediation speed, compliance efficiency) relative to investment in AI process automation.

Comparison metrics:
- **Cost per automated process**: AI agent licensing + integration costs / number of processes automated
- **FTE efficiency**: Human analyst hours saved through AI automation × loaded FTE cost
- **Operational speed**: Time reduction for key processes (incident MTTR, vulnerability remediation, compliance reporting)
- **Quality improvement**: Reduction in process errors, compliance findings, missed incidents
- **Scalability**: Ability to handle increased volume without proportional human staffing increases

Data sources:
- Industry reports (Gartner, Forrester on SOAR, AI security automation)
- Peer benchmarking (security operations maturity assessments, SANS surveys)
- Operational baselines (pre-AI vs. post-AI process performance)
- Vendor-provided case studies (validated through independent measurement or pilot programs)

**B) Collect metrics for historic AI security process automation spend and operational outcomes**

Track AI process automation investment over time and correlate with measurable operational improvements in security effectiveness, efficiency, and quality. Demonstrate whether increased AI automation is actually improving security operations outcomes.

Historical tracking (minimum 12 months, ideally 24+ for trend analysis):
- **Investment**: AI agent licensing, SOAR platform costs, integration/customization, analyst training, ongoing maintenance
- **Activity**: Processes automated, incidents triaged, vulnerabilities prioritized, reports generated, workflows completed
- **Operational outcomes**: Mean time to detect (MTTD), mean time to respond (MTTR), vulnerability remediation SLA compliance, process completion rate
- **Efficiency gains**: Analyst hours saved, overtime reduction, ability to handle increased volume with same staffing
- **Quality improvements**: Reduction in compliance audit findings, decrease in missed incidents, improvement in process consistency

Calculate demonstrable ROI with operational efficiency metrics:
- **Cost avoidance**: Prevented FTE hires due to AI automation (analysts not hired × annual loaded cost)
- **Productivity gains**: Analyst hours saved × loaded hourly cost (reallocated to higher-value work)
- **Speed improvements**: Faster incident response reduces breach impact (MTTR reduction × average incident cost)
- **Quality value**: Fewer compliance findings, consistent process execution, reduced human error
- **Scalability benefit**: Handling X% more security events with same team size

Present to executives and board as: "AI security process automation cost $X, saved $Y in analyst time, reduced MTTR by Z%, enabled handling of A% more incidents with existing team - ROI of N:1. Additionally, improved compliance audit results (B fewer findings) and analyst job satisfaction (C% reduction in repetitive work)."

**C) Produce and share original security process threat intelligence**

**Process Threat Intelligence Production**:

**Production Mechanisms**:
- **Incident Pattern Documentation**: Document novel incident response challenges, automation bypass techniques
- **SOAR Playbook Sharing**: Share effective security automation playbooks (anonymized)
- **Detection Evasion Research**: Analyze and document detection evasion techniques discovered through security operations
- **Volume Targets**: ≥4 process threat patterns/year, ≥2 automation best practice reports/year

**Industry Contribution**:
- **Security Operations ISACs**: Share SOC intelligence, incident response lessons learned
- **SOAR Vendor Partnerships**: Share automation gaps, playbook effectiveness, detection bypasses
- **MITRE ATT&CK**: Contribute defense evasion techniques and detection methods
- **Conference Presentations**: ≥2 presentations/year on security operations automation and AI-SOAR
- **Open-Source Tools**: SOAR playbooks, incident response automation, detection rules

**Success Criteria**:
- Process threat intelligence production (≥4 patterns/year, ≥2 best practice reports/year)
- Active participation in ≥3 security operations communities
- Industry leadership through SOAR playbook sharing and presentations

---

## Key Success Indicators

**Level 1:**
- AI security process automation strategy document exists and is current (<12 months old)
- Executive sponsor identified and engaged (CISO or Head of Security Operations)
- Basic inventory of AI agents automating security workflows and processes
- Documented backup plan if AI-automated processes fail (human takeover procedures)

**Level 2:**
- Security processes classified by criticality tier with documented AI oversight requirements per tier
- AI agent effectiveness metrics tracked for each process classification level
- Evidence that AI process automation goals differ based on process criticality
- Regular validation of AI process outputs through human sampling and quality review

**Level 3:**
- Annual benchmarking against industry peers for AI security process automation costs and outcomes
- Multi-year historical data showing AI automation investment trends and demonstrable operational ROI
- Quantified efficiency gains (analyst hours saved, MTTR reduction) tied to AI process automation spend
- Executive/board-level reporting on AI process automation effectiveness with operational value demonstrated
- Documented process quality improvements and scalability benefits from AI automation

---

## Common Pitfalls

**Level 1:**
- ❌ Inventory is incomplete (missing AI-powered SOAR workflows, forgotten automation scripts, shadow automation)
- ❌ Strategy document focuses on technology not outcomes (lists AI tools bought, not processes improved)
- ❌ No backup plan if AI automation fails (creates operational dependency without contingency)
- ❌ Auditability not considered (can't explain to auditors how AI-automated processes work)

**Level 2:**
- ❌ Process classification is too broad ("all incident response is critical" - insufficient granularity)
- ❌ AI oversight same for all process types (routine metrics get same scrutiny as incident triage)
- ❌ Metrics track AI activity (workflows run, reports generated) not outcomes (quality, accuracy, efficiency)
- ❌ No quality validation of AI-generated outputs (reports never reviewed, automation trusted blindly)
- ❌ False escalation rate not monitored (AI creates noise, analysts suffer alert fatigue)

**Level 3:**
- ❌ ROI calculation includes only cost savings, ignores quality/speed improvements
- ❌ Benchmarking uses wrong peer group (comparing enterprise SOC to small team capabilities)
- ❌ Historical data exists but doesn't correlate AI investment to measurable operational improvements
- ❌ Efficiency gains are theoretical ("AI could save 40 hours/week") not measured (actual time saved not tracked)
- ❌ Analyst satisfaction not measured (AI automation may save time but create frustration if poorly designed)

---

## Practice Maturity Questions

**Level 1:**
1. Do you have a documented strategy for AI agents operating security processes and workflows?
2. Is there an inventory of AI agents that automate security operations (incident response, compliance, vulnerability management, metrics)?
3. Has executive leadership acknowledged and sponsored the AI security process automation program with backup plans if AI fails?

**Level 2:**
1. Are security processes classified by criticality tier with different AI oversight requirements per classification?
2. Are AI agent effectiveness metrics (triage accuracy, process completion rate, quality) tracked by process classification?
3. Do security process automation goals for AI agents vary based on process criticality and operational risk?

**Level 3:**
1. Do you benchmark AI security process automation costs and operational outcomes against industry peers annually?
2. Is there multi-year historical data on AI process automation investment correlated with measurable efficiency gains (analyst hours saved, MTTR reduction)?
3. Can you demonstrate ROI of AI process automation with quantified operational value and security effectiveness improvements?

---

## Operational Considerations

AI-operated security processes must maintain operational resilience and auditability:

- **Business Continuity**: AI process automation should include failover to human operations if AI systems are unavailable
- **Audit Trail**: AI-automated processes must maintain sufficient logging and documentation for compliance audits (SOC 2, ISO 27001)
- **Change Management**: Updates to AI process automation must follow change control procedures to avoid operational disruption
- **Human Skills**: Staff must maintain skills to perform processes manually if AI automation fails or is disabled
- **Quality Assurance**: Regular sampling and review of AI-automated process outputs to ensure quality and catch drift
- **Escalation Procedures**: Clear criteria for when AI agents should escalate to human decision-makers in process execution

Organizations must balance automation efficiency with operational resilience and the ability to explain/audit AI-operated processes.

---

**Document Version:** HAIAMM v2.1
**Practice:** Strategy & Metrics (SM)
**Domain:** Processes
**Last Updated:** December 2025
**Author:** Verifhai
