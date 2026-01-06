# Issue Management (IM) - Software Domain
## HAIAMM Assessment Questionnaire v2.0

**Practice:** Issue Management (IM)
**Domain:** Software
**Purpose:** Assess organizational maturity in vulnerability management for Human Assisted Intelligence code security systems

---

## Instructions

- Answer each question honestly based on **current, implemented practices** (not plans or aspirations)
- **"Yes" requires evidence** - Document proof for each affirmative answer
- **Answer progressively** - Complete all Level 1 questions before Level 2
- **Level progression** - Achieve ALL questions at lower level before advancing
- **Partial implementation = "No"** - Practice must be complete and systematic

---

## Level 1: Foundational
**Objective:** Establish continuous vulnerability discovery, risk-based prioritization, SLA-driven remediation, and developer workflow integration

### Question 1: Continuous Vulnerability Discovery and Comprehensive Scanning

**Q1.1:** Have you established continuous vulnerability discovery across all AI system components (dependencies, code, containers, infrastructure, AI models) achieving 100% scanning coverage with daily dependency scans, real-time SAST on commits, weekly DAST, and ≥5 complementary scanning tools?

**Evidence Required:**
- [ ] Dependency Scanning:
  - Automated dependency scanning (Snyk, Dependabot, OWASP Dependency-Check, Safety, npm audit)
  - Frequency: Daily scans, real-time scanning on dependency changes
  - Transitive Dependency Scanning (≥5 levels deep)
  - Coverage: Application dependencies, ML framework dependencies (TensorFlow, PyTorch, scikit-learn)
  - License compliance scanning (FOSSA, Black Duck)
- [ ] Code Vulnerability Scanning:
  - Static Application Security Testing (SAST): SonarQube, Semgrep, CodeQL, Bandit, ESLint
  - Coverage: SQL injection, XSS, command injection, insecure crypto, hardcoded secrets
  - Integration: Run on every commit, block PRs with critical vulnerabilities
  - Secret Scanning: git-secrets, TruffleHog, GitGuardian (source code, config files, container images, commit history)
  - Infrastructure-as-Code (IaC) Scanning: Checkov, tfsec, kube-score (Terraform, CloudFormation, Kubernetes manifests)
- [ ] Dynamic Vulnerability Scanning:
  - Dynamic Application Security Testing (DAST): OWASP ZAP, Burp Suite, Nuclei
  - Frequency: Weekly scans, on-demand for major releases
  - API Security Scanning: Postman Security, 42Crunch (authentication, authorization, injection, rate limiting)
- [ ] Container and Image Scanning:
  - Container image scanning: Trivy, Grype, Clair, Anchore (base images, layers, dependencies)
  - Policy: Block deployment of images with critical CVEs
  - Runtime container scanning: Falco, Sysdig, Aqua Security (detect runtime exploitation)
- [ ] AI Model Vulnerability Assessment:
  - Adversarial robustness assessment (FGSM, PGD, poisoning, model inversion, extraction)
  - Frequency: After each model update, quarterly reassessment
  - Model dependency scanning (ML framework CVEs from NVD, GitHub Security Advisories)
  - Pre-trained model scanning (assess backdoors, trojans, data poisoning in Hugging Face, TensorFlow Hub, PyTorch Hub)
- [ ] Cloud Infrastructure Scanning:
  - Cloud Security Posture Management (CSPM): Prisma Cloud, Wiz, Orca Security
  - Coverage: IAM misconfigurations, exposed storage, network security (AWS, Azure, GCP)
- [ ] Scanning Coverage Metrics:
  - 100% of code repositories, dependencies, and infrastructure scanned
  - Scan Frequency: Daily dependency scans, weekly DAST, real-time SAST on commits
  - Tool Coverage: ≥5 complementary scanning tools
- [ ] Evidence of comprehensive scanning (scan logs, vulnerability reports, coverage metrics)

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

### Question 2: Risk-Based Prioritization and SLA-Driven Remediation

**Q1.2:** Have you implemented risk-based vulnerability prioritization (CVSS scoring, exploitability assessment, business impact, ML-based prioritization) with defined remediation SLAs (Critical ≤24h, High ≤7d, Medium ≤30d, Low ≤90d) achieving ≥95% SLA compliance and ≤10 critical/≤50 high vulnerabilities open at any time?

**Evidence Required:**
- [ ] Risk-Based Prioritization:
  - CVSS Scoring: Common Vulnerability Scoring System (0.0-10.0: None, Low, Medium, High, Critical)
  - Exploitability Assessment: Evaluate exploit complexity, attack vector, public exploits available (Exploit-DB, Metasploit)
  - Business Impact Assessment: Component criticality, data sensitivity, user exposure
  - ML-Based Risk Prioritization (optional): Train model on CVSS, exploitability, asset criticality, threat intel to predict exploitation likelihood
  - Context-Aware Prioritization: Factor deployment context (internet-facing vs internal, data sensitivity)
- [ ] Vulnerability Classification:
  - Critical: CVSS ≥9.0, active exploitation, RCE, auth bypass in production
  - High: CVSS 7.0-8.9, high impact, no compensating controls
  - Medium: CVSS 4.0-6.9, moderate impact, compensating controls exist
  - Low: CVSS 0.1-3.9, minimal impact, difficult to exploit
- [ ] Remediation SLAs Defined:
  - Critical: ≤24 hours (1 business day)
  - High: ≤7 days (1 week)
  - Medium: ≤30 days (1 month)
  - Low: ≤90 days (1 quarter) or accepted risk
- [ ] Remediation Workflows:
  - Automated Dependency Updates: Dependabot, Renovate Bot (auto-merge patches, review minor/major, run tests before merge)
  - Automated Configuration Fixes: Auto-remediate common misconfigurations (low-risk auto-applied, high-risk require approval)
  - Manual Remediation: Patch management (test → staging → production), code fixes (developer assigned → fix → review → test → deploy)
  - Compensating Controls: Temporary mitigations (WAF rules, segmentation, validation) when patches unavailable, documented until permanent fix
  - Risk Acceptance: Formal risk acceptance with senior management approval for critical/high, re-evaluate quarterly
  - Zero-Day Response: Playbook defined (threat assessment ≤2h, mitigation ≤4h), emergency patching fast-tracked
- [ ] Remediation Metrics:
  - SLA Compliance: ≥95% vulnerabilities remediated within SLA
  - Mean Time to Remediate (MTTR): Critical ≤24h, High ≤7d, Medium ≤30d, Low ≤90d
  - Vulnerability Backlog: ≤10 critical, ≤50 high vulnerabilities open at any time
  - Automated Remediation Rate: ≥60% of vulnerabilities auto-remediated
- [ ] Evidence of prioritization and SLA-driven remediation (vulnerability database, remediation tracking, SLA compliance reports)

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

### Question 3: Vulnerability Tracking, Developer Integration, and Prompt Injection Management

**Q1.3:** Do you maintain centralized vulnerability tracking with comprehensive metrics (MTTR, SLA compliance, backlog trends), integrate vulnerability management into development workflows (shift-left scanning with PR blocking, ≤5% false positive rate, fast feedback ≤5min SAST), and have dedicated prompt injection vulnerability management (if LLM-based) covering ≥8 vulnerability categories with specific remediation workflows?

**Evidence Required:**
- [ ] Vulnerability Tracking and Metrics:
  - Centralized Vulnerability Tracking: Track all vulnerabilities in single system (Jira, ServiceNow, dedicated VM platform)
  - Data tracked: CVE ID, severity, affected components, remediation status, SLA deadline
  - Vulnerability deduplication (CVE-based, component fingerprinting)
  - Historical data retained (≥2 years)
  - SLA Tracking: Monitor remediation against SLAs, alerts on approaching deadlines
  - Remediation Velocity: Track mean/median time-to-remediate by severity
  - Comprehensive Metrics:
    - Vulnerability Backlog (total open, breakdown by severity)
    - Mean Time to Remediate (MTTR) by severity
    - SLA Compliance (% vulnerabilities remediated within SLA, target ≥95%)
    - Vulnerability Discovery Rate (new vulnerabilities per month)
    - Vulnerability Density (vulnerabilities per KLOC)
  - Executive Reporting: Monthly vulnerability report for CISO/leadership, real-time risk dashboard
- [ ] Integration with Development Workflows:
  - Shift-Left Issue Management:
    - Pre-Commit Scanning: git hooks, IDE plugins (secrets, basic vulnerabilities)
    - Pull Request Scanning: GitHub Advanced Security, GitLab Security Scanning (block PRs with critical vulnerabilities)
    - CI/CD Integration: Build → SAST → Dependency scan → Container scan → Deploy (fail build on critical vulnerabilities)
  - Developer Experience:
    - Actionable Findings: Clear remediation guidance (description, affected code, fix recommendation, references)
    - Low False Positive Rate: ≤5% target (tune scanning tools, suppression for false positives)
    - Fast Feedback: SAST results ≤5 minutes, dependency scan ≤2 minutes
- [ ] Prompt Injection Vulnerability Management (if LLM-based tools):
  - Vulnerability Categories Defined (≥8 categories):
    - PI-001: System Prompt Leakage (High if sensitive data)
    - PI-002: Jailbreak / Safety Bypass (Critical)
    - PI-003: Injection-Based Data Exfiltration (Critical if PII/credentials)
    - PI-004: Tool/Function Enumeration (Medium)
    - PI-005: Prompt-Based DoS (High if production impact)
    - PI-006: Multi-Chain Prompt Attack (High)
    - PI-007: RAG Knowledge Base Poisoning (Critical if affects security decisions)
    - PI-008: Evasion via Encoding/Obfuscation (High if detection bypassed)
  - Remediation Workflows Specific to PI:
    - Critical PI (PI-002, PI-003, PI-007): ≤24 hours, disable LLM integration, investigate scope, implement fix, test, gradual rollout, notify CISO if customer data exposed
    - High PI (PI-001, PI-005, PI-006, PI-008): ≤7 days, strengthen validation, monitor, test
    - Medium PI (PI-004): ≤30 days, enhance error handling, limit information disclosure
  - Detection: Prompt injection testing (ST-Software), code review (IR-Software), runtime monitoring
  - Tracking: Dedicated tracking for PI vulnerabilities separate from standard CVEs
- [ ] Vulnerability Disclosure and Response:
  - Security Advisory Process (internal/external if applicable)
  - Responsible Disclosure Policy (security@company.com, SLA: acknowledge ≤24h, updates every 7 days)
  - Bug Bounty Program (optional): HackerOne, Bugcrowd
  - Vendor Advisory Monitoring: Cloud providers, ML frameworks, third-party services
- [ ] Continuous Improvement:
  - Vulnerability retrospectives (post-incident reviews, trend analysis)
  - Tool optimization (scanner tuning, coverage assessment, quarterly validation)
  - Security training (secure coding, VM processes)
- [ ] Evidence of tracking, integration, and comprehensive management (metrics dashboard, scan logs, developer feedback, PI vulnerability tracking if applicable)

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

**Level 1 Score:** _____ / 3 questions answered "Yes"

**Level 1 Achieved:** ☐ Yes (3/3) ☐ No (< 3/3)

---

## Level 2: Comprehensive
**Objective:** Implement continuous always-on assessment, advanced threat intelligence integration, automated correlation, risk-based patching, and vulnerability prediction

**Prerequisites:** ALL Level 1 questions must be "Yes" to proceed to Level 2

### Question 4: Continuous Always-On Vulnerability Assessment and Threat Intelligence Integration

**Q2.1:** Have you implemented continuous always-on vulnerability assessment (not periodic scanning, but real-time continuous monitoring) and advanced threat intelligence integration correlating vulnerabilities with active exploitation data (CISA KEV, threat intel feeds, exploit databases)?

**Evidence Required:**
- [ ] Continuous Always-On Vulnerability Assessment:
  - Always-On Scanning: Continuous monitoring (not just periodic scans)
  - Real-Time Detection: Vulnerabilities detected and reported immediately upon discovery
  - Continuous Dependency Monitoring: Real-time alerts on new CVEs affecting dependencies
  - Continuous Infrastructure Monitoring: Always-on CSPM, runtime container scanning
  - Continuous Code Monitoring: Real-time SAST on code changes (not just periodic scans)
  - Benefits: Minimize exposure window, immediate vulnerability awareness
- [ ] Advanced Threat Intelligence Integration:
  - Threat Intelligence Sources:
    - CISA Known Exploited Vulnerabilities (KEV) Catalog
    - Commercial threat intel feeds (Recorded Future, CrowdStrike, Mandiant)
    - Open-source threat intel (AlienVault OTX, MISP)
    - Exploit databases (Exploit-DB, Metasploit Framework)
    - Dark web monitoring (exploit availability, vulnerability discussions)
  - Vulnerability-Threat Correlation:
    - Correlate discovered vulnerabilities with active exploitation intelligence
    - Prioritize vulnerabilities with known active exploitation higher
    - Alert on new exploits for existing vulnerabilities
  - Exploitability Trending:
    - Track changes in exploitability over time (newly published exploit → elevated priority)
    - Monitor weaponization status (PoC published → exploit in wild → mass exploitation)
  - Automated Priority Adjustment:
    - Auto-elevate priority when exploitation confirmed
    - Example: Medium vulnerability → High when CISA KEV added
- [ ] Metrics:
  - Real-Time Detection: ≥95% of new vulnerabilities detected within 24 hours
  - Threat Intel Coverage: 100% of critical/high vulnerabilities correlated with threat intel
  - Exploitability Accuracy: ≥90% of "actively exploited" classifications accurate
- [ ] Evidence of continuous assessment and threat intelligence improving prioritization (always-on monitoring logs, threat intel correlation reports, elevated prioritization examples)

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

### Question 5: Automated Vulnerability Correlation and Risk-Based Patching

**Q2.2:** Have you implemented automated vulnerability correlation (link related vulnerabilities across systems, identify attack chains) and risk-based patching (prioritize patches based on real-world exploitation likelihood, asset criticality, compensating controls)?

**Evidence Required:**
- [ ] Automated Vulnerability Correlation:
  - Cross-System Correlation:
    - Link related vulnerabilities across different components (same vulnerability in library used in multiple services)
    - Identify attack chains (vulnerability A enables vulnerability B exploitation)
    - Track vulnerability families (related CVEs, vulnerability variants)
  - Duplicate Detection:
    - Automatically deduplicate same vulnerability reported by different scanners
    - Merge vulnerability reports across tools into single tracking item
  - Blast Radius Analysis:
    - Identify all systems affected by single vulnerability
    - Quantify exposure (# of systems, # of users, data sensitivity)
  - Remediation Impact Analysis:
    - Predict remediation effort (# of systems to patch, testing required)
    - Identify shared dependencies (patching one library fixes multiple vulnerabilities)
- [ ] Risk-Based Patching:
  - Patching Priority Factors:
    - Real-World Exploitation Likelihood (CISA KEV, exploit availability, attack targeting)
    - Asset Criticality (production vs dev, customer-facing vs internal, data sensitivity)
    - Compensating Controls (WAF, segmentation, access controls reducing risk)
    - Patch Availability (patch available vs workaround only)
    - Patch Risk (stability risk, breaking changes, testing requirements)
  - Risk-Based Prioritization Algorithm:
    - ML model or scoring algorithm combining factors
    - Output: Prioritized patch schedule
    - Validation: Compare predicted vs actual exploitation attempts
  - Differential Patching:
    - Critical assets patched faster (production ≤24h, dev ≤7d for same vulnerability)
    - Internet-facing systems prioritized over internal
    - Systems with high data sensitivity prioritized
- [ ] Advanced Metrics:
  - Vulnerability Reintroduction Rate: Track if same vulnerability re-introduced (indicates process gap)
  - Patch Effectiveness: Validate patch actually eliminates vulnerability (post-patch scanning)
  - Risk Reduction: Quantify risk reduction from patching (CVSS reduction, exploitability reduction)
- [ ] Evidence of correlation and risk-based patching improving efficiency (correlation examples, risk-based patch schedules, metrics showing improved outcomes)

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

### Question 6: Vulnerability Prediction and Proactive Discovery

**Q2.3:** Have you implemented vulnerability prediction using ML models to identify vulnerable code patterns before exploitation, and conduct proactive vulnerability discovery through code pattern analysis and security research?

**Evidence Required:**
- [ ] Vulnerability Prediction:
  - ML-Based Vulnerability Prediction:
    - Train models to predict vulnerabilities in code patterns
    - Features: Code complexity, input handling patterns, framework usage, historical vulnerability patterns
    - Training Data: Historical vulnerability data, fixed vulnerabilities, code characteristics
    - Output: Predicted vulnerable code areas (before vulnerability discovered/exploited)
  - Code Pattern Analysis:
    - Identify anti-patterns correlated with vulnerabilities
    - Detect risky code patterns (dynamic SQL construction, eval(), unsafe deserialization)
    - Flag code for security review based on risk score
  - Predictive Alerts:
    - Alert developers on potentially vulnerable code before submission
    - Provide guidance on secure alternatives
  - Validation:
    - Measure prediction accuracy (% of predictions that are true vulnerabilities)
    - Track false positive rate (<20% target for predictions)
    - Evidence of predictions preventing vulnerabilities
- [ ] Proactive Vulnerability Discovery:
  - Internal Security Research:
    - Dedicated time for security research on AI systems
    - Fuzzing, symbolic execution, manual code audit
    - Focus on novel vulnerability classes
  - Security Champions:
    - Developers trained in vulnerability discovery
    - Regular security code review sessions
    - Share findings across organization
  - Vulnerability Trends Analysis:
    - Identify vulnerability hotspots (components with frequent vulnerabilities)
    - Analyze root causes (why vulnerabilities introduced?)
    - Implement preventive measures
- [ ] Metrics:
  - Prediction Accuracy: ≥60% of predicted vulnerabilities confirmed
  - Proactive Discovery: ≥20% of vulnerabilities found proactively (before external report)
  - Prevention: Vulnerable code patterns decreasing over time
- [ ] Evidence of prediction and proactive discovery improving security (prediction models, proactive findings, vulnerability trend improvements)

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

**Level 2 Score:** _____ / 3 questions answered "Yes"

**Level 2 Achieved:** ☐ Yes (3/3) ☐ No (< 3/3)

---

## Level 3: Industry-Leading
**Objective:** Achieve proactive vulnerability research, zero-day discovery program, continuous penetration testing, and public vulnerability disclosure leadership

**Prerequisites:** ALL Level 2 questions must be "Yes" to proceed to Level 3

### Question 7: Proactive Vulnerability Research and Zero-Day Discovery Program

**Q3.1:** Have you established an internal vulnerability research team conducting proactive security research and a zero-day discovery program (internal bug bounty, continuous red team exercises) finding vulnerabilities before attackers, with ≥30% of critical vulnerabilities discovered proactively?

**Evidence Required:**
- [ ] Proactive Vulnerability Research Team:
  - Dedicated Security Research Team:
    - Team size: ≥2 FTE dedicated security researchers
    - Focus: Proactive vulnerability discovery in AI systems
    - Research Areas: Novel attack techniques, zero-day discovery, exploitation research
  - Research Activities:
    - Advanced fuzzing programs (coverage-guided fuzzing, grammar-based fuzzing)
    - Symbolic execution and formal methods
    - Manual code audit and architecture review
    - Adversarial ML research (novel attacks on AI models)
    - Supply chain security research
  - Research Tools:
    - Custom tooling developed for vulnerability discovery
    - Automated vulnerability hunting infrastructure
    - Exploit development and validation frameworks
  - Research Output:
    - Internal vulnerability reports (findings, exploitation, remediation)
    - Security advisories for discovered vulnerabilities
    - Threat intelligence from research (attack patterns, indicators)
- [ ] Zero-Day Discovery Program:
  - Internal Bug Bounty:
    - Employee bug bounty program (incentivize internal vulnerability discovery)
    - Rewards tiered by severity ($500-$5,000+ for internal findings)
    - Gamification and recognition
  - Continuous Red Team Exercises:
    - Red team operates continuously (not periodic exercises)
    - Purple team collaboration (red team + blue team learning)
    - Adversarial testing of AI systems
    - Attack simulations (multi-stage attacks, persistence, lateral movement)
  - Zero-Day Response:
    - Rapid internal patching (internal 0-days fixed before disclosure ≤7 days)
    - Post-discovery review (how was 0-day possible? preventive measures?)
- [ ] Metrics:
  - Proactive Discovery Rate: ≥30% of critical vulnerabilities discovered proactively (before external report)
  - Zero-Day Discovery: ≥5 zero-days discovered internally per year
  - Time to Remediate Internal Findings: ≤7 days for critical internal findings
  - External vs Internal Discovery: More vulnerabilities found internally than externally
- [ ] Evidence of proactive research preventing exploitation (research findings, zero-day discoveries, remediation before external disclosure)

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

### Question 8: Continuous Penetration Testing and AI-Powered Vulnerability Analysis

**Q3.2:** Do you conduct continuous penetration testing (always-on testing for exploitable vulnerabilities, automated and manual testing) and employ AI-powered vulnerability analysis to predict, prioritize, and correlate vulnerabilities with measurably improved outcomes (≥40% faster MTTR, ≥50% more accurate prioritization)?

**Evidence Required:**
- [ ] Continuous Penetration Testing:
  - Always-On Penetration Testing:
    - Continuous testing (not periodic/quarterly penetration tests)
    - Automated penetration testing tools running continuously (Nuclei, automated exploit frameworks)
    - Manual penetration testing conducted regularly (weekly/monthly)
  - Scope:
    - All internet-facing systems tested continuously
    - Internal systems tested regularly
    - AI-specific attack vectors (model evasion, prompt injection, data poisoning)
  - Exploitation Validation:
    - Validate vulnerabilities are exploitable (not just theoretical)
    - Develop proof-of-concept exploits
    - Measure exploitability (time to exploit, skill required, prerequisites)
  - Remediation Validation:
    - Re-test after remediation to confirm vulnerability eliminated
    - Track patch effectiveness (did patch work?)
  - Integration:
    - Pen test findings fed into vulnerability management system
    - Prioritize vulnerabilities confirmed exploitable
- [ ] AI-Powered Vulnerability Analysis:
  - AI Prediction Models:
    - Predict which vulnerabilities will be exploited (features: CVSS, exploitability, threat intel, asset criticality)
    - Predict remediation effort and patch risk
    - Recommend optimal remediation sequence
  - AI Correlation:
    - Automatically correlate related vulnerabilities
    - Identify attack chains and dependencies
    - Group vulnerabilities by root cause
  - AI Prioritization:
    - Dynamic prioritization based on changing threat landscape
    - Real-time reprioritization as new intelligence emerges
    - Personalized prioritization per organization context
  - Measurable Improvements:
    - ≥40% faster MTTR (AI-assisted prioritization vs manual)
    - ≥50% more accurate prioritization (% of AI-prioritized vulnerabilities exploited vs baseline)
    - ≥30% reduction in vulnerability backlog (better remediation efficiency)
    - Developer satisfaction: ≥85% agree AI recommendations are helpful
- [ ] Evidence of continuous testing and AI improving vulnerability management (continuous pen test findings, AI model performance metrics, MTTR improvements, prioritization accuracy)

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

### Question 9: Public Vulnerability Disclosure and Industry Leadership

**Q3.3:** Does your organization actively participate in public vulnerability disclosure (responsible disclosure to community, CVE assignments for discovered vulnerabilities, contributions to vulnerability databases) and demonstrate industry leadership (at least 2 contributions per year: vulnerability research publications, open-source VM tools, security standards participation)?

**Evidence Required:**
- [ ] Public Vulnerability Disclosure:
  - Responsible Disclosure Program:
    - Publicly disclosed vulnerabilities to affected vendors/communities
    - Coordinated disclosure timeline (90-day disclosure policy)
    - CVE assignments obtained for public vulnerabilities
  - CVE Contributions:
    - ≥2 CVEs assigned per year for vulnerabilities discovered in open-source components
    - Documented in NVD, vendor advisories, security bulletins
  - Vulnerability Database Contributions:
    - Contributions to NVD, OWASP, MITRE ATT&CK, Exploit-DB
    - Vulnerability details, exploitation techniques, remediation guidance
    - Exploit PoCs shared (after remediation available)
  - Public Security Advisories:
    - Publish security advisories for vulnerabilities in organization's products (if applicable)
    - Transparency in vulnerability handling and remediation
- [ ] Industry Leadership Contributions (at least 2 per year):
  - Vulnerability Research Publications:
    - Conference presentations (Black Hat, DEF CON, OWASP, security conferences)
    - Research papers (academic or practitioner publications)
    - Blog posts on vulnerability discovery, exploitation, remediation
  - Open-Source VM Tools:
    - Published open-source vulnerability scanning tools
    - Contributed to existing VM tools (OpenSCAP, OWASP Dependency-Check, etc.)
    - Shared automation frameworks, remediation scripts
  - Security Standards Participation:
    - Contributions to CVE/NVD processes, CVSS scoring, CWE definitions
    - Participation in OWASP, SANS, NIST vulnerability management standards
    - Influence on industry VM best practices
  - Vulnerability Management Best Practices:
    - Published case studies on VM programs
    - Shared remediation workflows, SLA frameworks
    - Training materials for vulnerability management
- [ ] Public Evidence:
  - CVE assignments linked to organization
  - Conference presentations and published papers
  - Open-source tool repositories
  - Security advisory publications
- [ ] Industry Impact:
  - CVEs referenced by other researchers/organizations
  - VM tools adopted by ≥10 other organizations
  - Standards or best practices incorporating your contributions
  - Recognition as thought leader in vulnerability management
- [ ] Internal Excellence Program:
  - Recognition for vulnerability discovery
  - Vulnerability research celebrated internally
  - Knowledge sharing culture

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

**Level 3 Score:** _____ / 3 questions answered "Yes"

**Level 3 Achieved:** ☐ Yes (3/3) ☐ No (< 3/3)

---

## Practice Score Calculation

### Simplified Scoring (Recommended)

```
Level 1 Achieved (all 3 "Yes"): 1.0 point
Level 2 Achieved (all 3 "Yes"): +1.0 point (total 2.0)
Level 3 Achieved (all 3 "Yes"): +1.0 point (total 3.0)
```

**IM-Software Practice Score:** _______ / 3.0

### Precise Scoring (For Formal Audits)

```
L1_score = (L1 "Yes" answers) / 3
L2_score = (L2 "Yes" answers) / 3 × L1_score
L3_score = (L3 "Yes" answers) / 3 × L2_score

Practice Score = L1_score + L2_score + L3_score
```

**IM-Software Practice Score (Precise):** _______ / 3.0

---

## Assessment Summary

**Assessment Date:** _________________________________

**Assessor(s):** _____________________________________

**HAI System(s) Assessed:** __________________________

**Overall Maturity Level:**
- ☐ Level 0 (Score < 1.0): Ad-hoc, no formal vulnerability management for AI systems
- ☐ Level 1 (Score 1.0 - 1.9): Foundational VM with continuous scanning, SLA-driven remediation, developer integration
- ☐ Level 2 (Score 2.0 - 2.9): Comprehensive VM with always-on assessment, threat intel, correlation, prediction
- ☐ Level 3 (Score 3.0): Industry-leading with proactive research, zero-day discovery, public disclosure

**Strengths:**

_________________________________________________________________

**Gaps:**

_________________________________________________________________

**Priority Improvements:**

_________________________________________________________________

**Re-Assessment Date:** _________________________________

---

## Evidence Repository

Link all evidence documents here for audit trail:

| Question | Evidence Document | Location | Date | Owner |
|----------|------------------|----------|------|-------|
| Q1.1 | | | | |
| Q1.2 | | | | |
| Q1.3 | | | | |
| Q2.1 | | | | |
| Q2.2 | | | | |
| Q2.3 | | | | |
| Q3.1 | | | | |
| Q3.2 | | | | |
| Q3.3 | | | | |

---

## Issue Management Specific Notes

**Continuous Vulnerability Discovery (Level 1):**
- [ ] Dependency Scanning (daily, real-time, transitive ≥5 levels, license compliance)
- [ ] Code Vulnerability Scanning (SAST on every commit, secret scanning, IaC scanning)
- [ ] Dynamic Scanning (DAST weekly, API security scanning)
- [ ] Container Scanning (image scanning with CVE blocking, runtime scanning)
- [ ] AI Model Assessment (adversarial robustness, model dependency scanning, pre-trained model scanning)
- [ ] Cloud Infrastructure Scanning (CSPM for AWS/Azure/GCP)
- [ ] 100% scanning coverage, ≥5 complementary tools

**Risk-Based Prioritization:**
- [ ] CVSS Scoring, Exploitability Assessment, Business Impact
- [ ] ML-Based Prioritization (optional but recommended)
- [ ] Context-Aware Prioritization

**Remediation SLAs:**
- [ ] Critical: ≤24 hours
- [ ] High: ≤7 days
- [ ] Medium: ≤30 days
- [ ] Low: ≤90 days or risk acceptance

**Remediation Workflows:**
- [ ] Automated Dependency Updates (≥60% auto-remediated)
- [ ] Automated Configuration Fixes
- [ ] Manual Patching and Code Fixes
- [ ] Compensating Controls
- [ ] Risk Acceptance with senior approval
- [ ] Zero-Day Response (assessment ≤2h, mitigation ≤4h)

**Tracking and Metrics (Level 1):**
- [ ] Centralized tracking (Jira, ServiceNow, VM platform)
- [ ] SLA Compliance ≥95%
- [ ] MTTR: Critical ≤24h, High ≤7d, Medium ≤30d, Low ≤90d
- [ ] Vulnerability Backlog: ≤10 critical, ≤50 high
- [ ] Automated Remediation Rate ≥60%
- [ ] False Positive Rate ≤5%
- [ ] Vulnerability Density ≤5 per KLOC

**Developer Integration:**
- [ ] Shift-Left (pre-commit, PR scanning, CI/CD integration)
- [ ] Actionable findings, low false positives (≤5%), fast feedback (SAST ≤5min)

**Prompt Injection VM (if LLM-based):**
- [ ] ≥8 PI vulnerability categories (PI-001 through PI-008)
- [ ] Specific remediation workflows (Critical PI ≤24h, High ≤7d, Medium ≤30d)
- [ ] Dedicated tracking separate from standard CVEs

**Level 2 Advanced Practices:**
- [ ] Continuous Always-On Assessment (real-time, not periodic)
- [ ] Advanced Threat Intelligence (CISA KEV, threat feeds, exploit DBs, dark web)
- [ ] Automated Vulnerability Correlation (cross-system, attack chains, blast radius)
- [ ] Risk-Based Patching (exploitation likelihood, asset criticality, compensating controls)
- [ ] Vulnerability Prediction (ML models, code pattern analysis, ≥60% accuracy)
- [ ] Proactive Discovery (≥20% found proactively)

**Level 3 Industry-Leading:**
- [ ] Proactive Vulnerability Research Team (≥2 FTE, advanced fuzzing, symbolic execution)
- [ ] Zero-Day Discovery Program (internal bug bounty, continuous red team, ≥5 0-days/year)
- [ ] Proactive Discovery Rate ≥30% of critical vulnerabilities
- [ ] Continuous Penetration Testing (always-on, automated + manual, exploitation validation)
- [ ] AI-Powered Vulnerability Analysis (≥40% faster MTTR, ≥50% more accurate prioritization)
- [ ] Public Vulnerability Disclosure (≥2 CVEs/year, responsible disclosure, NVD/OWASP contributions)
- [ ] Industry Leadership (≥2 contributions/year: research publications, open-source tools, standards participation)

---

**Document Version:** 2.0
**Last Updated:** 2025-12-29
**Next Review:** Quarterly or after significant HAI system changes
