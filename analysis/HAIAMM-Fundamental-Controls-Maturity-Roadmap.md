# HAIAMM Fundamental Controls Maturity Roadmap
## Essential NIST/CMMC Controls for AI-Operated Security Programs

**Date:** December 18, 2025
**Version:** 1.0
**Focus:** Most fundamental controls for building HAI security programs (Maturity Levels 1 → 2 → 3)

---

## PHILOSOPHY: BASICS FIRST

HAIAMM assesses how well **AI agents perform security work**, not how to secure AI systems. This roadmap identifies the **most fundamental controls** organizations need when building HAI security programs.

**Progression:**
- **Level 1 (Basic):** Can AI agents do security work at all?
- **Level 2 (Defined):** Can AI agents do security work consistently and correctly?
- **Level 3 (Optimized):** Can AI agents do security work better than humans at scale?

---

## MATURITY LEVEL 1: BASIC AI SECURITY OPERATIONS

**Goal:** Establish that AI agents can perform basic security tasks with human oversight.

**Timeframe:** 0-6 months
**CMMC Equivalent:** Level 1 (Foundational)
**Questions:** 24 (Tier 1)

### Core Question: "Do you have AI agents doing security work, and can humans verify they're working?"

---

### LEVEL 1 FUNDAMENTAL CONTROLS (10 Essential Controls)

#### 1. ACCESS CONTROL (AC) - "Can AI agents access what they need, but only what they need?"

**NIST Control:** AC.3.001 - Limit system access to authorized users
**Why Fundamental:** If AI agents have unlimited access, they're a security risk, not a security solution.

**HAIAMM Assessment:**
- **L1.AC.Q1:** "Are AI security agents granted access using least-privilege principles?"
  - ✅ Yes = AI agents only access systems they're supposed to monitor/protect
  - ❌ No = AI agents have admin access everywhere (dangerous)

**What This Looks Like:**
- AI vulnerability scanner can read code repos but can't modify code
- AI monitoring agent can view logs but can't delete them
- AI compliance agent can assess policies but can't change them

**Human Verification:** "Can a human see exactly what systems each AI agent can access?"

---

#### 2. IDENTIFICATION & AUTHENTICATION (IA) - "Do we know which AI agent did what?"

**NIST Control:** IA.3.083 - Identify information system users
**Why Fundamental:** If you can't identify which AI agent took an action, you can't trust HAI security operations.

**HAIAMM Assessment:**
- **L1.IA.Q1:** "Does each AI security agent have a unique identity for tracking actions?"
  - ✅ Yes = "VulnScanner-AI-01" has its own login, separate from "ComplianceAI-02"
  - ❌ No = All AI agents share "admin" account (accountability nightmare)

**What This Looks Like:**
- AI agent "ThreatDetector-AI" has its own service account
- Logs show "ThreatDetector-AI flagged vulnerability CVE-2024-1234"
- Not "system flagged vulnerability" (which system? which AI?)

**Human Verification:** "Can a human trace every AI action back to a specific AI agent?"

---

#### 3. AUDIT & ACCOUNTABILITY (AU) - "Can we see what AI agents are doing?"

**NIST Control:** AU.3.046 - Create and retain audit logs
**Why Fundamental:** You can't trust AI security decisions you can't audit.

**HAIAMM Assessment:**
- **L1.AU.Q1:** "Do AI security agents create audit logs for all security actions?"
  - ✅ Yes = Every AI decision is logged with timestamp, agent ID, and reasoning
  - ❌ No = AI agents operate as black boxes

**What This Looks Like:**
- AI flags vulnerability → Log shows: "2025-12-18 14:32 | VulnScanner-AI-01 | Detected SQL injection in login.php | Severity: High"
- AI blocks traffic → Log shows: "2025-12-18 14:35 | FirewallAI-02 | Blocked IP 192.168.1.100 | Reason: Malicious pattern detected"

**Human Verification:** "Can a human review AI agent logs to understand what happened and why?"

---

#### 4. INCIDENT RESPONSE (IR) - "When AI agents find problems, do humans know about it?"

**NIST Control:** IR.3.098 - Report incidents to designated officials
**DFARS Requirement:** 72-hour incident reporting
**Why Fundamental:** AI agents finding threats is worthless if humans never hear about them.

**HAIAMM Assessment:**
- **L1.IR.Q1:** "When AI agents detect security incidents, are humans notified promptly?"
  - ✅ Yes = AI flags issue → Human gets alert within minutes/hours
  - ❌ No = AI detects breach but nobody knows for days

**What This Looks Like:**
- AI detects ransomware → Sends Slack alert to security team immediately
- AI finds data exfiltration → Creates ticket in incident management system
- AI identifies insider threat → Escalates to security manager

**Human Verification:** "Can humans demonstrate they received and reviewed AI-generated alerts?"

---

#### 5. SYSTEM & COMMUNICATIONS PROTECTION (SC) - "Is sensitive data encrypted when AI agents handle it?"

**NIST Control:** SC.3.177 - Employ FIPS-validated cryptography
**Why Fundamental:** If AI agents handle unencrypted sensitive data, you're creating new vulnerabilities.

**HAIAMM Assessment:**
- **L1.SC.Q1:** "Do AI agents encrypt sensitive data (CUI/PII) at rest and in transit?"
  - ✅ Yes = AI stores findings encrypted, transmits over TLS
  - ❌ No = AI vulnerability reports sit in plain text on shared drives

**What This Looks Like:**
- AI security testing results stored in encrypted database
- AI compliance reports transmitted over HTTPS only
- AI agent API keys stored in encrypted vault (not config files)

**Human Verification:** "Can a human confirm AI agents use encryption for sensitive data?"

---

#### 6. CONFIGURATION MANAGEMENT (CM) - "Do we know what AI security tools are deployed?"

**NIST Control:** CM.3.068 - Establish baseline configurations
**Why Fundamental:** If you don't know what AI agents you have, you can't manage them.

**HAIAMM Assessment:**
- **L1.CM.Q1:** "Do you maintain an inventory of all AI security agents deployed?"
  - ✅ Yes = Spreadsheet/system listing all AI agents, purposes, versions
  - ❌ No = Developers deployed AI tools; nobody knows what's running

**What This Looks Like:**
- **AI Security Agent Inventory:**
  - VulnScanner-AI-01 | Snyk AI | Scans code repos | Version 2.3 | Owner: DevSecOps
  - ThreatDetector-AI | Darktrace | Network monitoring | Version 5.1 | Owner: SOC
  - ComplianceAI | Custom | Policy checks | Version 1.0 | Owner: GRC team

**Human Verification:** "Can a human produce a list of all AI security agents in 5 minutes?"

---

#### 7. SYSTEM & INFORMATION INTEGRITY (SI) - "Can AI agents actually find security problems?"

**NIST Control:** SI.3.214 - Monitor system security alerts
**Why Fundamental:** If AI agents don't detect real threats, they're expensive noise generators.

**HAIAMM Assessment:**
- **L1.SI.Q1:** "Do AI security agents successfully identify real vulnerabilities and threats?"
  - ✅ Yes = AI finds vulnerabilities confirmed by humans as real
  - ❌ No = AI generates 1000 alerts, 990 are false positives

**What This Looks Like:**
- AI vulnerability scanner finds SQL injection → Confirmed exploitable
- AI threat detector flags malware → Confirmed by human analyst
- AI compliance agent finds policy violation → Confirmed non-compliant

**Human Verification:** "Can humans show examples of real threats AI agents detected?"

---

#### 8. RISK ASSESSMENT (RA) - "Do humans understand the risks of using AI for security?"

**NIST Control:** RA.3.161 - Conduct risk assessments
**Why Fundamental:** HAI security operations create new risks you must identify.

**HAIAMM Assessment:**
- **L1.RA.Q1:** "Have you assessed the risks of AI agents performing security work?"
  - ✅ Yes = Documented risks: AI false negatives, AI bias, adversarial attacks
  - ❌ No = Deployed AI security without risk analysis

**What This Looks Like:**
- **Risk Assessment Document:**
  - Risk 1: AI misses zero-day → Mitigation: Human review of critical systems
  - Risk 2: AI fooled by adversarial input → Mitigation: Multi-AI validation
  - Risk 3: AI over-privileges itself → Mitigation: Least-privilege enforcement

**Human Verification:** "Can humans explain 3 risks of HAI security operations and mitigations?"

---

#### 9. AWARENESS & TRAINING (AT) - "Do humans know how to work with AI security agents?"

**NIST Control:** AT.3.027 - Provide security awareness training
**Why Fundamental:** Humans must know when to trust AI and when to override it.

**HAIAMM Assessment:**
- **L1.AT.Q1:** "Are staff trained on overseeing AI security agents and interpreting their outputs?"
  - ✅ Yes = Security team trained: "When AI flags X, investigate Y first"
  - ❌ No = AI alerts go to untrained staff who ignore them

**What This Looks Like:**
- Training module: "How to Validate AI Vulnerability Reports"
- Documented procedures: "When AI Threat Detector Alerts You"
- Quarterly drills: "Responding to AI-Detected Incidents"

**Human Verification:** "Can humans demonstrate they've been trained on HAI security operations?"

---

#### 10. MEDIA PROTECTION (MP) - "Are AI agent outputs protected from unauthorized access?"

**NIST Control:** MP.3.115 - Protect and control media containing CUI
**Why Fundamental:** If AI security reports leak, you've created the breach you tried to prevent.

**HAIAMM Assessment:**
- **L1.MP.Q1:** "Are AI security agent outputs (reports, findings) restricted to authorized personnel?"
  - ✅ Yes = Vulnerability reports only accessible to security team
  - ❌ No = AI compliance reports visible to entire company

**What This Looks Like:**
- AI penetration test results stored in access-controlled system
- AI threat intelligence reports marked "Confidential - SOC Only"
- AI security assessment outputs require MFA to view

**Human Verification:** "Can humans show access controls on AI security outputs?"

---

## MATURITY LEVEL 1 CHECKLIST

**Before claiming Level 1 maturity, you should be able to answer YES to:**

| # | Control | Question | Pass/Fail |
|---|---------|----------|-----------|
| 1 | Access Control | Can you list what systems each AI agent can access? | ☐ Yes ☐ No |
| 2 | Identity | Does each AI agent have a unique identity? | ☐ Yes ☐ No |
| 3 | Audit Logs | Can you show logs of AI agent actions? | ☐ Yes ☐ No |
| 4 | Incident Response | Do humans receive AI security alerts? | ☐ Yes ☐ No |
| 5 | Encryption | Is sensitive AI data encrypted? | ☐ Yes ☐ No |
| 6 | Inventory | Can you list all AI security agents deployed? | ☐ Yes ☐ No |
| 7 | Effectiveness | Can AI agents find real security problems? | ☐ Yes ☐ No |
| 8 | Risk Assessment | Have you assessed AI security risks? | ☐ Yes ☐ No |
| 9 | Training | Are staff trained on HAI security operations? | ☐ Yes ☐ No |
| 10 | Output Protection | Are AI security reports access-controlled? | ☐ Yes ☐ No |

**If you can't answer YES to all 10, you're not ready for Level 2.**

---

## MATURITY LEVEL 2: DEFINED AI SECURITY OPERATIONS

**Goal:** AI agents perform security work consistently using documented processes with continuous human oversight.

**Timeframe:** 6-18 months
**CMMC Equivalent:** Level 2 (Advanced)
**Questions:** 192 (Tier 2)

### Core Question: "Do AI agents follow documented procedures, and can humans validate they're working correctly?"

---

### LEVEL 2 FUNDAMENTAL CONTROLS (15 Essential Controls)

**Level 2 = Level 1 + Documented Processes + Validation + Continuous Monitoring**

#### 11. POLICY & COMPLIANCE (PC) - "Are HAI security operations governed by documented policies?"

**NIST Control:** PL.3.001 - Develop security plans
**Why Fundamental:** Ad-hoc AI security creates gaps; documented policies ensure consistency.

**HAIAMM Assessment:**
- **L2.PC.Q1:** "Do you have documented policies governing how AI agents perform security work?"
  - ✅ Yes = "AI Security Operations Policy v2.0" defines roles, responsibilities, limits
  - ❌ No = AI agents operate without written rules

**What This Looks Like:**
- **AI Security Policy Document:**
  - Section 1: Which security tasks AI agents may perform
  - Section 2: Required human review checkpoints
  - Section 3: AI agent access limitations
  - Section 4: Incident escalation procedures
  - Section 5: AI decision override authority

**Maturity Indicator:** Policy is written, approved by leadership, reviewed annually.

---

#### 12. SECURITY REQUIREMENTS (SR) - "Do AI agents meet defined security standards?"

**NIST Control:** SA.3.001 - Obtain system components from trusted sources
**Why Fundamental:** Commercial AI security tools have vulnerabilities; you must vet them.

**HAIAMM Assessment:**
- **L2.SR.Q1:** "Do you have security requirements that AI security agents must meet before deployment?"
  - ✅ Yes = Checklist: "AI tool must support MFA, audit logging, least privilege"
  - ❌ No = Developers deploy any AI security tool they find

**What This Looks Like:**
- **AI Security Agent Requirements:**
  - Must support role-based access control (RBAC)
  - Must provide audit trails for all actions
  - Must encrypt data at rest and in transit
  - Must support API key rotation
  - Must pass security assessment before production

**Maturity Indicator:** No AI security agent deployed without requirements checklist.

---

#### 13. SECURE ARCHITECTURE (SA) - "Are AI agents isolated from production systems?"

**NIST Control:** SC.3.178 - Deny network communications by default
**Why Fundamental:** AI security agents shouldn't be able to damage what they're protecting.

**HAIAMM Assessment:**
- **L2.SA.Q1:** "Are AI security agents deployed in isolated environments with controlled production access?"
  - ✅ Yes = AI agents run in dedicated network segment, limited production access
  - ❌ No = AI agents run on same network as critical systems with full access

**What This Looks Like:**
- AI vulnerability scanners run in "Security Tools VLAN"
- AI agents access production via read-only API gateway
- AI testing agents NEVER touch production databases directly
- Network segmentation enforced by firewall rules

**Maturity Indicator:** Network diagram shows AI agent isolation and controlled access paths.

---

#### 14. DESIGN REVIEW (DR) - "Do humans review AI security workflows before deployment?"

**NIST Control:** CAM.3.001 - Conduct security assessments
**Why Fundamental:** AI agents making security decisions need pre-deployment validation.

**HAIAMM Assessment:**
- **L2.DR.Q1:** "Are AI agent security workflows reviewed by humans before production deployment?"
  - ✅ Yes = Security architect reviews: "This AI will monitor X and alert on Y"
  - ❌ No = AI agents deployed without design review

**What This Looks Like:**
- **Design Review Checklist:**
  - What security function does this AI perform?
  - What data does it access?
  - What actions can it take automatically?
  - What actions require human approval?
  - What's the false positive rate?
  - How are errors handled?

**Maturity Indicator:** Every AI security agent has approved design review document.

---

#### 15. CODE REVIEW (CR) - "Are AI agent prompts/configurations reviewed for security issues?"

**NIST Control:** CM.3.069 - Review and approve system changes
**Why Fundamental:** Prompts are code; bad prompts create vulnerabilities.

**HAIAMM Assessment:**
- **L2.CR.Q1:** "Are AI agent system prompts and configurations reviewed before deployment?"
  - ✅ Yes = Security team reviews prompts: "Don't expose credentials in output"
  - ❌ No = Developers write prompts without security review

**What This Looks Like:**
- **Prompt Review Checklist:**
  - ✅ Prompt doesn't instruct AI to execute commands
  - ✅ Prompt limits AI output to security findings only
  - ✅ Prompt prevents AI from exposing sensitive data
  - ✅ Prompt includes error handling instructions
  - ✅ Configuration files don't contain hardcoded credentials

**Maturity Indicator:** Version control for AI prompts with approval workflow.

---

#### 16. SECURITY TESTING (ST) - "Are AI security agents tested for adversarial attacks?"

**NIST Control:** CAM.3.002 - Assess security controls
**Why Fundamental:** If AI agents can be fooled, they're a liability.

**HAIAMM Assessment:**
- **L2.ST.Q1:** "Do you test AI security agents for adversarial manipulation before production?"
  - ✅ Yes = Red team tests: "Can we trick AI into missing vulnerabilities?"
  - ❌ No = AI agents deployed without adversarial testing

**What This Looks Like:**
- **Adversarial Test Scenarios:**
  - Prompt injection: Can attacker make AI ignore threats?
  - Data poisoning: Can attacker train AI to miss specific attacks?
  - False positive flooding: Can attacker overwhelm AI with noise?
  - Evasion: Can attacker craft exploits AI won't detect?

**Maturity Indicator:** Test reports showing AI agent resilience to adversarial attacks.

---

#### 17. ENVIRONMENT HARDENING (EH) - "Are AI agent runtime environments secured?"

**NIST Control:** CM.3.072 - Implement least functionality
**Why Fundamental:** Compromised AI agent environments = compromised security program.

**HAIAMM Assessment:**
- **L2.EH.Q1:** "Are AI agent runtime environments hardened per security baselines?"
  - ✅ Yes = Containers run minimal OS, no unnecessary services
  - ❌ No = AI agents run on default Ubuntu with all services enabled

**What This Looks Like:**
- AI agents run in hardened containers (minimal base image)
- Unnecessary network services disabled
- Security updates applied automatically
- File system read-only except for logs
- Resource limits enforced (CPU, memory, network)

**Maturity Indicator:** Hardening checklist for every AI agent runtime environment.

---

#### 18. MONITORING & LOGGING (ML) - "Are AI agent activities continuously monitored?"

**NIST Control:** AU.3.052 - Monitor organizational systems
**Why Fundamental:** AI agents need monitoring just like humans do.

**HAIAMM Assessment:**
- **L2.ML.Q1:** "Do you continuously monitor AI agent activities for anomalous behavior?"
  - ✅ Yes = SIEM alerts when AI agent behaves unexpectedly
  - ❌ No = AI agents run unsupervised

**What This Looks Like:**
- Dashboard showing: AI agent uptime, actions/hour, error rates
- Alerts: "AI agent made 10x normal API calls" (possible compromise)
- Retention: 90+ days of AI agent logs for forensics
- Monitoring: API usage, resource consumption, decision patterns

**Maturity Indicator:** Automated monitoring with alerts for AI agent anomalies.

---

#### 19. ISSUE MANAGEMENT (IM) - "How do you handle false positives/negatives from AI agents?"

**NIST Control:** SI.3.216 - Respond to information spills
**Why Fundamental:** AI agents make mistakes; you must track and fix them.

**HAIAMM Assessment:**
- **L2.IM.Q1:** "Do you track false positives and false negatives from AI security agents?"
  - ✅ Yes = Ticketing system: "AI flagged false positive, fixed prompt"
  - ❌ No = AI mistakes not documented or analyzed

**What This Looks Like:**
- **Issue Tracking:**
  - Ticket #1234: AI missed SQL injection (false negative) → Root cause: Obfuscated payload
  - Ticket #1235: AI flagged legitimate code (false positive) → Root cause: Overly broad rule
  - Monthly report: AI accuracy trending up from 85% → 92%

**Maturity Indicator:** Dashboard showing AI agent accuracy metrics over time.

---

#### 20. MULTIFACTOR AUTHENTICATION (MFA) - "Is MFA enforced for AI agent system access?"

**NIST Control:** IA.3.085 - Employ multifactor authentication
**DFARS Requirement:** MFA for all CUI access
**Why Fundamental:** If attackers compromise AI agent credentials, game over.

**HAIAMM Assessment:**
- **L2.MFA.Q1:** "Do you enforce MFA for all human access to AI agent management systems?"
  - ✅ Yes = Admins need MFA to access AI agent dashboards/configs
  - ❌ No = Password-only access to AI security infrastructure

**What This Looks Like:**
- AI agent management portal requires hardware token or authenticator app
- API keys for AI agents stored in MFA-protected vault
- Admin actions on AI agents logged with MFA verification timestamp

**Maturity Indicator:** Zero human access to AI agent systems without MFA.

---

#### 21. CONFIGURATION BASELINES (CM) - "Are AI agent configurations managed under change control?"

**NIST Control:** CM.3.070 - Restrict/disable network protocols
**Why Fundamental:** Uncontrolled AI configuration changes create security gaps.

**HAIAMM Assessment:**
- **L2.CM.Q1:** "Are AI agent configurations managed with version control and change approval?"
  - ✅ Yes = Git repo for AI configs, pull requests reviewed before merge
  - ❌ No = Admins edit AI configurations directly in production

**What This Looks Like:**
- AI agent prompts stored in Git with change history
- Configuration changes require approval workflow
- Rollback capability for bad AI configuration changes
- Automated testing of configuration changes before production

**Maturity Indicator:** All AI configuration changes traceable in version control.

---

#### 22. RISK MITIGATION (RA) - "Do you have documented mitigations for AI security risks?"

**NIST Control:** RA.3.162 - Update risk assessments when changes occur
**Why Fundamental:** Identifying risks without mitigation is security theater.

**HAIAMM Assessment:**
- **L2.RA.Q1:** "Do you have documented risk mitigation strategies for HAI security operations?"
  - ✅ Yes = Risk register with mitigations: "AI false negative → Human review of critical assets"
  - ❌ No = Risks identified but no mitigation plan

**What This Looks Like:**
- **Risk Mitigation Plan:**
  - Risk: AI misses advanced attacks → Mitigation: Hybrid AI+human analyst review
  - Risk: AI poisoned by training data → Mitigation: Vendor attestation + validation testing
  - Risk: AI over-alerts and fatigues team → Mitigation: Tune thresholds based on feedback

**Maturity Indicator:** Each identified risk has documented mitigation and owner.

---

#### 23. PHYSICAL PROTECTION (PE) - "Are AI agent hardware and infrastructure physically secured?"

**NIST Control:** PE.3.131 - Limit physical access to organizational systems
**Why Fundamental:** Physical access to AI agent infrastructure bypasses all software controls.

**HAIAMM Assessment:**
- **L2.PE.Q1:** "Are AI agent systems deployed in physically secured locations with access controls?"
  - ✅ Yes = AI servers in locked data center with badge access
  - ❌ No = AI agent servers in unsecured office space

**What This Looks Like:**
- Cloud AI agents: AWS/Azure/GCP with physical security attestations
- On-prem AI agents: Data center with 24/7 monitoring, badge access logs
- Workstation AI agents: Full-disk encryption, physical locks

**Maturity Indicator:** Physical security verification for all AI agent infrastructure.

---

#### 24. PERSONNEL SECURITY (PS) - "Are personnel with AI agent access properly vetted?"

**NIST Control:** PS.3.139 - Screen individuals before authorizing access
**Why Fundamental:** Insider threats can weaponize AI agents.

**HAIAMM Assessment:**
- **L2.PS.Q1:** "Are personnel with administrative access to AI security agents background-checked?"
  - ✅ Yes = Admins with AI agent access undergo background screening
  - ❌ No = Anyone can be granted AI agent admin access

**What This Looks Like:**
- HAI security operations team undergoes background checks
- Privileged access to AI agents requires manager approval
- Contractors with AI agent access sign NDAs
- Access reviews quarterly: "Who still needs AI admin access?"

**Maturity Indicator:** Personnel security procedures for AI agent access documented and followed.

---

#### 25. SUPPLY CHAIN RISK MANAGEMENT (SR) - "Do you assess risks from AI security vendors?"

**NIST Control:** SR.3.227 - Identify, prioritize, and assess suppliers
**NEW in NIST Rev. 3**
**Why Fundamental:** AI security tools from compromised vendors = backdoor into your security program.

**HAIAMM Assessment:**
- **L2.SR.Q1:** "Do you conduct Third-Party Risk Management (TPRM) assessments for AI security vendors?"
  - ✅ Yes = Vendor questionnaire: "How do you secure your AI training data?"
  - ❌ No = AI tools purchased without vendor security assessment

**What This Looks Like:**
- **Vendor Risk Assessment:**
  - Does vendor have SOC 2 Type II certification?
  - Where is AI training data stored?
  - Can vendor access our data?
  - What's vendor's incident response process?
  - Is vendor's AI supply chain secured?

**Maturity Indicator:** No AI security vendor contracts without TPRM assessment.

---

## MATURITY LEVEL 2 CHECKLIST

**Before claiming Level 2 maturity, you should be able to answer YES to Level 1 (all 10) PLUS:**

| # | Control | Question | Pass/Fail |
|---|---------|----------|-----------|
| 11 | Policy | Do you have documented HAI security operations policies? | ☐ Yes ☐ No |
| 12 | Requirements | Do AI agents meet security requirements before deployment? | ☐ Yes ☐ No |
| 13 | Architecture | Are AI agents isolated from production systems? | ☐ Yes ☐ No |
| 14 | Design Review | Are AI workflows reviewed before deployment? | ☐ Yes ☐ No |
| 15 | Code Review | Are AI prompts/configs reviewed for security? | ☐ Yes ☐ No |
| 16 | Testing | Are AI agents tested for adversarial attacks? | ☐ Yes ☐ No |
| 17 | Hardening | Are AI runtime environments hardened? | ☐ Yes ☐ No |
| 18 | Monitoring | Do you continuously monitor AI agent activities? | ☐ Yes ☐ No |
| 19 | Issue Tracking | Do you track AI false positives/negatives? | ☐ Yes ☐ No |
| 20 | MFA | Is MFA enforced for AI system access? | ☐ Yes ☐ No |
| 21 | Change Control | Are AI configs under version control? | ☐ Yes ☐ No |
| 22 | Risk Mitigation | Do you have documented risk mitigations? | ☐ Yes ☐ No |
| 23 | Physical Security | Are AI systems physically secured? | ☐ Yes ☐ No |
| 24 | Personnel Security | Are AI admins background-checked? | ☐ Yes ☐ No |
| 25 | Vendor Risk | Do you assess AI vendor security? | ☐ Yes ☐ No |

**If you can't answer YES to all 25 (10 from L1 + 15 from L2), you're not ready for Level 3.**

---

## MATURITY LEVEL 3: OPTIMIZED AI SECURITY OPERATIONS

**Goal:** AI agents perform security work better than humans at scale with continuous optimization and advanced threat defense.

**Timeframe:** 18+ months
**CMMC Equivalent:** Level 3 (Expert)
**Questions:** 432 (Tier 3)

### Core Question: "Do AI agents proactively improve security posture and defend against advanced threats?"

---

### LEVEL 3 FUNDAMENTAL CONTROLS (10 Essential Controls)

**Level 3 = Level 2 + Continuous Improvement + Advanced Threat Defense + Automation**

#### 26. CONTINUOUS MONITORING (CAM) - "Are AI agents continuously assessed for effectiveness?"

**NIST Control:** CAM.3.002 - Assess security controls at regular intervals
**Why Fundamental:** Level 3 requires proof that HAI security operations are getting better.

**HAIAMM Assessment:**
- **L3.CAM.Q1:** "Do you conduct quarterly assessments of AI agent security effectiveness with metrics-based improvement?"
  - ✅ Yes = "Q4 2025: AI detection rate 92% → Q1 2026: 96%" with root cause analysis
  - ❌ No = AI agents never assessed for improvement

**What This Looks Like:**
- **Quarterly AI Security Scorecard:**
  - Detection rate: 96% (↑4% from last quarter)
  - False positive rate: 2% (↓1% from last quarter)
  - Mean time to detect: 3.2 minutes (↓0.5 min from last quarter)
  - Coverage: 98% of infrastructure monitored
  - Improvement actions implemented: 12

**Maturity Indicator:** Trend data showing measurable HAI security operations improvement over time.

---

#### 27. THREAT-INFORMED DEFENSE (RA) - "Do AI agents use threat intelligence to prioritize security work?"

**NIST Control:** RA.3.161 - Use threat intelligence in risk assessments
**Why Fundamental:** Level 3 AI agents don't just find vulnerabilities; they prioritize based on active threats.

**HAIAMM Assessment:**
- **L3.RA.Q1:** "Do AI security agents integrate threat intelligence to prioritize vulnerabilities based on active exploitation?"
  - ✅ Yes = AI flags CVE-2024-1234 as critical because ransomware gangs exploiting it NOW
  - ❌ No = AI treats all vulnerabilities equally regardless of threat landscape

**What This Looks Like:**
- AI vulnerability scanner: "CVE-2024-1234: CRITICAL - Actively exploited by APT28 (CISA Alert)"
- AI threat detector: "This pattern matches ransomware group observed this week"
- AI prioritization: High-threat vulnerabilities flagged within 1 hour, low-threat within 24 hours

**Maturity Indicator:** AI security decisions informed by real-time threat intelligence feeds.

---

#### 28. AUTOMATED RESPONSE (IR) - "Can AI agents automatically contain threats?"

**NIST Control:** IR.3.100 - Implement incident handling capability
**Why Fundamental:** Level 3 = AI agents contain threats at machine speed, not waiting for humans.

**HAIAMM Assessment:**
- **L3.IR.Q1:** "Do AI security agents automatically contain threats with human notification and override capability?"
  - ✅ Yes = AI detects malware → Quarantines host → Alerts SOC → Human approves/overrides
  - ❌ No = AI detects threats but always waits for human action

**What This Looks Like:**
- **Automated Containment Scenarios:**
  - AI detects lateral movement → Blocks network traffic → Notifies SOC
  - AI identifies compromised credentials → Disables account → Triggers password reset
  - AI finds data exfiltration → Isolates system → Preserves forensics
  - ALL actions logged, humans can override within 5 minutes

**Maturity Indicator:** AI agents contain >80% of threats automatically with <1% false containment rate.

---

#### 29. AI-TO-AI COORDINATION (SA) - "Do multiple AI agents coordinate security operations?"

**NIST Control:** SC.3.185 - Coordinate information security with external service providers
**Why Fundamental:** Level 3 = AI agents work together, not in silos.

**HAIAMM Assessment:**
- **L3.SA.Q1:** "Do AI security agents coordinate with each other to provide comprehensive protection?"
  - ✅ Yes = Threat detector AI → Shares indicators → Vulnerability scanner AI → Prioritizes related vulns
  - ❌ No = Each AI agent operates independently, duplicating work

**What This Looks Like:**
- **AI Security Agent Orchestration:**
  - ThreatDetector-AI finds suspicious IP → Alerts FirewallAI → Blocks IP across all systems
  - VulnScanner-AI finds SQLi → Alerts WebAppFirewallAI → Updates WAF rules
  - ComplianceAI finds misconfiguration → Alerts RemediationAI → Auto-generates fix script
  - Coordination via secure API mesh with audit logging

**Maturity Indicator:** Documented AI agent workflows showing coordinated security operations.

---

#### 30. ADVANCED ADVERSARY DEFENSE (SI) - "Can AI agents detect advanced persistent threats (APTs)?"

**NIST Control:** SI.3.215 - Identify unauthorized system changes
**NIST SP 800-172 Enhanced**
**Why Fundamental:** Level 3 = Defense against nation-state actors, not just script kiddies.

**HAIAMM Assessment:**
- **L3.SI.Q1:** "Do AI agents detect advanced attack techniques (living-off-the-land, fileless malware, etc.)?"
  - ✅ Yes = AI detects PowerShell abuse, memory-only exploits, supply chain attacks
  - ❌ No = AI only detects signature-based malware

**What This Looks Like:**
- AI detects: Legitimate admin tools used maliciously (PSExec, WMI, PowerShell)
- AI identifies: Anomalous behavior patterns indicating APT (slow, stealthy lateral movement)
- AI correlates: Multiple low-severity events → High-severity campaign
- AI baselines: Normal vs. abnormal admin behavior

**Maturity Indicator:** AI agents successfully detect advanced attack simulations (red team exercises).

---

#### 31. SECURITY OPERATIONS CENTER (SOC) INTEGRATION (ML) - "Do AI agents integrate with 24/7 SOC operations?"

**NIST Control:** AU.3.053 - Provide audit record reduction
**NIST SP 800-172 Enhanced**
**Why Fundamental:** Level 3 = AI agents as force multipliers for human analysts, not replacements.

**HAIAMM Assessment:**
- **L3.ML.Q1:** "Do AI agents integrate with SOC workflows to triage and prioritize alerts for human analysts?"
  - ✅ Yes = AI pre-investigates 1000 alerts → Escalates 10 high-priority to humans
  - ❌ No = AI dumps all alerts to humans without triage

**What This Looks Like:**
- **AI-Augmented SOC:**
  - AI processes 10,000 security events/hour
  - AI automatically dismisses 9,500 false positives
  - AI enriches 500 alerts with context (threat intel, asset criticality)
  - AI escalates 50 high-priority alerts to L2 analysts
  - AI drafts incident response playbooks for critical alerts

**Maturity Indicator:** SOC metrics showing AI reduces analyst workload by >70% while increasing detection rate.

---

#### 32. PLAN OF ACTION & MILESTONES (PC) - "Do you continuously improve HAI security operations with documented plans?"

**NIST Control:** PL.3.001 - System security plans
**CMMC POA&M Requirement**
**Why Fundamental:** Level 3 = Never done improving; always planning next optimization.

**HAIAMM Assessment:**
- **L3.PC.Q1:** "Do you maintain Plans of Action & Milestones (POA&Ms) for HAI security operations improvements?"
  - ✅ Yes = "Q2 2026 Goal: Reduce AI false positive rate from 2% to 1%" with 180-day plan
  - ❌ No = No formal improvement planning

**What This Looks Like:**
- **POA&M Example:**
  - Gap: AI misses obfuscated malware
  - Action: Train AI on evasion techniques dataset
  - Owner: Security Engineering Team
  - Timeline: 90 days
  - Success Metric: Detect 95% of obfuscated samples
  - Status: In Progress (Day 45/90)

**Maturity Indicator:** Quarterly POA&Ms with >80% completion rate and measurable improvements.

---

#### 33. VENDOR CONTINUOUS MONITORING (SR) - "Do you continuously monitor AI vendor security posture?"

**NIST Control:** SR.3.228 - Monitor supply chain risks
**Why Fundamental:** Level 3 = Vendor assessment isn't one-time; it's continuous.

**HAIAMM Assessment:**
- **L3.SR.Q1:** "Do you continuously monitor AI security vendors for security incidents and supply chain compromises?"
  - ✅ Yes = Automated alerts when AI vendor reports breach or loses certification
  - ❌ No = Vendor assessed once at contract signing, never reviewed

**What This Looks Like:**
- **Vendor Monitoring Dashboard:**
  - Snyk AI Security Tool: SOC 2 expires in 60 days (alert)
  - Darktrace: No security incidents this quarter (green)
  - CustomAI Vendor: Acquired by Company X (review security posture)
  - Automated checks: Vendor certifications, breach notifications, M&A activity

**Maturity Indicator:** Automated vendor monitoring with quarterly security posture reviews.

---

#### 34. ADVERSARIAL RESILIENCE TESTING (ST) - "Do you continuously test AI agents against evolving adversarial techniques?"

**NIST Control:** CAM.3.002 - Assess security controls
**Why Fundamental:** Level 3 = Attackers evolve; your testing must too.

**HAIAMM Assessment:**
- **L3.ST.Q1:** "Do you conduct quarterly red team exercises specifically targeting AI security agents?"
  - ✅ Yes = Red team attempts to fool AI agents every quarter with new techniques
  - ❌ No = AI agents tested once at deployment, never again

**What This Looks Like:**
- **Quarterly Adversarial Testing:**
  - Q1: Prompt injection attacks against AI security chatbots
  - Q2: Data poisoning attempts against AI training data
  - Q3: Evasion techniques against AI malware detectors
  - Q4: Model inversion attacks to extract training data
  - Results documented, AI agents hardened based on findings

**Maturity Indicator:** Red team reports showing AI agent resilience improving quarter-over-quarter.

---

#### 35. METRICS & OPTIMIZATION (SM) - "Do you measure and optimize AI security ROI?"

**NIST Control:** CAM.3.001 - Develop and implement security assessment plans
**Why Fundamental:** Level 3 = Prove HAI security operations deliver measurable value.

**HAIAMM Assessment:**
- **L3.SM.Q1:** "Do you measure HAI security operations ROI with metrics like cost-per-detection, time-to-remediation, and coverage?"
  - ✅ Yes = "AI detected 1,200 vulns at $5/vuln vs. human pentest $500/vuln"
  - ❌ No = HAI security operations deployed without measuring effectiveness

**What This Looks Like:**
- **AI Security Operations Dashboard:**
  - Cost per vulnerability detected: $5 (vs. $500 manual)
  - Mean time to detect: 3.2 minutes (vs. 8 hours manual)
  - Coverage: 98% of infrastructure (vs. 60% manual sampling)
  - False positive rate: 2% (vs. 5% traditional SIEM)
  - Analyst time saved: 720 hours/quarter

**Maturity Indicator:** Executive dashboard showing HAI security operations business value and continuous optimization.

---

## MATURITY LEVEL 3 CHECKLIST

**Before claiming Level 3 maturity, you should be able to answer YES to Level 1 (10) + Level 2 (15) PLUS:**

| # | Control | Question | Pass/Fail |
|---|---------|----------|-----------|
| 26 | Continuous Assessment | Do you quarterly assess AI effectiveness with metrics? | ☐ Yes ☐ No |
| 27 | Threat Intelligence | Do AI agents use threat intel to prioritize work? | ☐ Yes ☐ No |
| 28 | Automated Response | Can AI agents automatically contain threats? | ☐ Yes ☐ No |
| 29 | AI Coordination | Do AI agents coordinate with each other? | ☐ Yes ☐ No |
| 30 | APT Defense | Can AI agents detect advanced persistent threats? | ☐ Yes ☐ No |
| 31 | SOC Integration | Do AI agents integrate with 24/7 SOC operations? | ☐ Yes ☐ No |
| 32 | POA&M | Do you maintain improvement plans for AI security? | ☐ Yes ☐ No |
| 33 | Vendor Monitoring | Do you continuously monitor AI vendor security? | ☐ Yes ☐ No |
| 34 | Red Team Testing | Do you quarterly test AI agents with red teams? | ☐ Yes ☐ No |
| 35 | ROI Metrics | Do you measure and optimize AI security ROI? | ☐ Yes ☐ No |

**Level 3 requires YES to all 35 controls (10+15+10).**

---

## SIMPLIFIED ROADMAP VIEW

### What You Need at Each Level

```
LEVEL 1: BASIC (0-6 months)
├─ Can AI agents do security work?
├─ 10 fundamental controls
├─ Focus: Visibility, Identity, Audit
└─ Example: "We have AI vulnerability scanners and can see what they find"

LEVEL 2: DEFINED (6-18 months)
├─ Do AI agents follow documented procedures?
├─ 25 controls (10 from L1 + 15 new)
├─ Focus: Policies, Testing, Monitoring
└─ Example: "AI agents operate per documented policies with continuous validation"

LEVEL 3: OPTIMIZED (18+ months)
├─ Do AI agents improve security better than humans?
├─ 35 controls (25 from L2 + 10 new)
├─ Focus: Automation, Optimization, Advanced Defense
└─ Example: "AI agents autonomously contain threats and continuously improve"
```

---

## QUICK START: YOUR FIRST 30 DAYS

**If you're starting from zero, focus on these 5 controls first:**

### Week 1: Inventory
**Control #6 (CM):** List all AI security tools you're using
- Output: Spreadsheet with AI agent names, purposes, owners

### Week 2: Access Control
**Control #1 (AC):** Document what each AI agent can access
- Output: Matrix showing AI agents × Systems they can access

### Week 3: Audit Logging
**Control #3 (AU):** Enable logging for all AI agent actions
- Output: Logs showing what AI agents are doing

### Week 4: Human Oversight
**Control #4 (IR):** Ensure humans receive AI security alerts
- Output: Notification workflow tested and documented

**By Day 30, you should be able to answer: "What AI security agents do we have, what can they access, and can we see what they're doing?"**

---

## IMPLEMENTATION PRIORITIES

### High Priority (Implement First)
These controls are foundational; you can't skip them:

1. **Access Control (AC)** - Without least privilege, AI agents are dangerous
2. **Audit & Accountability (AU)** - Without logs, you have no visibility
3. **Incident Response (IR)** - Without human notification, AI findings are lost
4. **Identity (IA)** - Without unique IDs, you can't trace AI actions
5. **Inventory (CM)** - Without knowing what you have, you can't manage it

### Medium Priority (Implement Second)
These controls make AI operations reliable:

6. **Security Testing (ST)** - Prevents deploying vulnerable AI agents
7. **Monitoring & Logging (ML)** - Detects AI agent anomalies
8. **Policy & Compliance (PC)** - Ensures consistency
9. **Risk Assessment (RA)** - Identifies AI-specific risks
10. **Vendor Risk (SR)** - Prevents compromised AI tools

### Lower Priority (Implement Third)
These controls optimize and scale AI operations:

11. **Automated Response (IR)** - Requires proven AI agent reliability first
12. **AI Coordination (SA)** - Complex; requires multiple mature AI agents
13. **ROI Metrics (SM)** - Important but not urgent for basic operations

---

## COMMON MISTAKES TO AVOID

### ❌ Mistake 1: "We deployed AI security tools, so we're Level 2"
**Reality:** Deploying tools without documented policies, testing, and monitoring = Level 1 at best

### ❌ Mistake 2: "Our AI vendor is SOC 2 certified, so we don't need to assess them"
**Reality:** Vendor certification doesn't eliminate supply chain risk; you still need TPRM (Control #25)

### ❌ Mistake 3: "AI agents are autonomous, so we don't need human oversight"
**Reality:** Level 3 requires MORE human oversight, not less; automation amplifies both success and failure

### ❌ Mistake 4: "We'll skip Level 1 and go straight to Level 2"
**Reality:** Level 2 requires Level 1 foundations; skipping creates security gaps

### ❌ Mistake 5: "We passed CMMC Level 2, so we don't need HAIAMM"
**Reality:** CMMC assesses traditional security; HAIAMM assesses HAI security (different focus)

---

## SUMMARY: THE 35 FUNDAMENTAL CONTROLS

| Level | Controls | Focus | Timeline |
|-------|----------|-------|----------|
| **Level 1** | 10 controls | Can AI agents do security work? | 0-6 months |
| **Level 2** | +15 controls (25 total) | Do AI agents follow documented procedures? | 6-18 months |
| **Level 3** | +10 controls (35 total) | Do AI agents improve security at scale? | 18+ months |

**The entire roadmap in one sentence:**
*Start by making AI agents visible and accountable (L1), then make them reliable and consistent (L2), then make them continuously improving and autonomous (L3).*

---

**Document Version:** 1.0
**Last Updated:** December 18, 2025
**Next Steps:** Use this roadmap to prioritize HAIAMM question development for v2.0

**Related Documents:**
- Full Analysis: `NIST-DFARS-CMMC-HAIAMM-Alignment-Analysis.md`
- Executive Summary: `EXECUTIVE-SUMMARY-NIST-CMMC-Integration.md`
