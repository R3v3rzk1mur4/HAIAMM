# Issue Management Practice – Vendors Domain
## HAIAMM v2.1 One-Pager

### Practice Overview

Issue Management for Vendors ensures AI vendor risk management systems systematically identify, assess, prioritize, and remediate vulnerabilities in vendor systems, vendor-provided software (SBOMs), and vendor risk management platforms themselves.

---

### Level 1: Key Issue Management Activities

**Vendor Platform Vulnerabilities**:
- [ ] **Vendor Risk Platform Scanning**: Scan vendor risk management platforms
  - Platforms: BitSight API, SecurityScorecard API, RiskRecon, Prevalent, UpGuard integrations
  - Coverage: Platform CVEs (NVD, vendor advisories), API vulnerabilities (injection, authentication bypass), misconfigurations (weak TLS, exposed endpoints, default credentials)
  - Frequency: Daily CVE monitoring (automated alerts on new CVEs), weekly configuration scans (CIS benchmarks, security best practices)
  - Tools: Vulnerability scanners (Nessus, Qualys, OpenVAS), dependency checkers (Snyk, Dependabot), SAST/DAST for custom code
  - SLA: Critical platform CVEs patched within ≤24 hours, High ≤7 days, Medium ≤30 days
  - Prioritization: Public exploits available (Critical), affects Critical vendor data (High), low risk or isolated systems (Medium/Low)
- [ ] **Platform Integration Security**: Secure integrations with vendor data sources
  - Sources: Questionnaire systems, breach databases (HIBP, Risk Based Security), SBOM repositories, threat intel feeds, third-party APIs (BitSight, SecurityScorecard)
  - Coverage: API authentication (weak API keys, credential stuffing), authorization (IDOR, privilege escalation), injection vulnerabilities (SQL, command, LDAP), credential security (plaintext secrets, hardcoded keys)
  - Testing: API security scanning (OWASP ZAP, Burp Suite), penetration testing (quarterly for Critical integrations), credential audits (rotate every 90 days)
  - Findings: Log all vulnerabilities (CVSS score, affected integration, remediation status), track in issue management system
- [ ] **Vendor Platform Dependency Management**: Track platform dependencies
  - Dependencies: Programming language libraries (npm, PyPI, Maven), OS packages (apt, yum), container images (Docker base images)
  - Scanning: Automated dependency scanning (Dependabot, Snyk, GitHub Security Advisories), daily scans for new CVEs
  - Remediation: Update vulnerable dependencies within SLA (Critical ≤24 hours, High ≤7 days), test before production deployment
  - Supply Chain: Verify dependency integrity (checksums, signatures), detect malicious packages (typosquatting, suspicious behavior)

**Vendor Software Vulnerabilities (SBOM)**:
- [ ] **SBOM Vulnerability Scanning**: Scan vendor-provided SBOMs for CVEs
  - Scope: All vendor-provided software (on-prem, SaaS, cloud services), open-source dependencies, commercial components
  - Tools: SBOM scanners (Grype, Trivy, Dependency-Track), CVE databases (NVD, GitHub Security Advisories, OSV), vendor-specific databases
  - Frequency: Daily SBOM scans (detect new CVEs in existing SBOMs), immediate scan on new SBOM ingestion (when vendor provides updated SBOM)
  - Coverage: Direct dependencies + transitive dependencies (≥5 levels deep), detect vulnerability propagation (CVE in library used by 10 vendors)
  - Output: Vulnerability report per vendor (CVE ID, CVSS score, affected component/version, remediation available, exploitability)
- [ ] **Vulnerability Prioritization**: Prioritize vendor software vulnerabilities
  - Factors: Vendor criticality (Critical vendors prioritized), exploitability (CISA KEV, public exploit code), affected components (core vs. optional features), compensating controls (WAF, network isolation reduces risk)
  - CVSS: Base score (inherent severity), Temporal score (exploit availability, patch availability), Environmental score (criticality to your org)
  - SLA: Critical vendor vulnerabilities (CVSS ≥9.0, exploit available) ≤7 days vendor response, High (CVSS 7.0-8.9) ≤30 days, Medium (CVSS 4.0-6.9) ≤60 days
  - Queue: Prioritized vulnerability remediation queue (sorted by risk score = CVSS × vendor criticality × exploitability)
- [ ] **Vendor Notification**: Notify vendors of vulnerabilities in their software
  - Process: Identify vulnerability in SBOM → verify it's not false positive → notify vendor (email, portal, API) → set remediation deadline (per SLA) → track remediation progress → verify fix (request updated SBOM, test patch)
  - Escalation: If vendor doesn't respond within ≤48 hours (Critical), ≤7 days (High), escalate to vendor account manager, vendor management, consider contract enforcement
  - Communication: Use vendor portal for notifications (audit trail), follow up via email if no response, include CVE details + remediation guidance
  - Metrics: Track vendor response time, MTTR, SLA compliance rate (% vulnerabilities remediated within SLA)
- [ ] **False Positive Management**: Handle SBOM vulnerability false positives
  - Causes: Component not actually used (included but not executed), vulnerability doesn't apply (affects Windows but vendor runs Linux), vendor already patched (SBOM out of date)
  - Process: Vendor contests vulnerability → provide evidence (code analysis showing component unused, patch notes) → security team reviews → mark false positive or request vendor update SBOM
  - Tracking: Track false positive rate by vendor (high rate indicates inaccurate SBOMs), request SBOM quality improvements

**Vendor Security Incident Tracking**:
- [ ] **Breach Monitoring**: Monitor vendor security breaches
  - Sources: Breach databases (HIBP, Risk Based Security), vendor disclosures (emails, portals, press releases), threat intel feeds, news monitoring (automated alerts)
  - Frequency: Real-time monitoring (24/7), automated alerts within ≤1 hour of disclosure, review within ≤24 hours
  - Response: Assess impact (does breach include our data? Which data types? Customer impact?) → notify stakeholders (legal, compliance, affected business units) → require vendor remediation plan (≤48 hours for Critical)
  - Tracking: Log all vendor breaches (date, type, data exposed, impact, vendor response, resolution), track to closure
- [ ] **Vendor Incident Response**: Track vendor incident remediation
  - Tracking: Vendor incident response timeline (detection → notification → containment → remediation → verification), remediation steps (patch deployed, accounts reset, logs reviewed), verification evidence (pen test, SOC 2 report, attestation)
  - SLA: Critical vendor incidents require remediation plan ≤48 hours, remediation complete ≤30 days; High incidents ≤7 days response, ≤60 days remediation
  - Validation: Verify vendor remediation (request evidence, independent audit for Critical incidents, penetration testing to confirm fix)
  - Escalation: If vendor misses SLA, escalate to vendor executive team, consider contract suspension, evaluate vendor termination

**Vendor Risk Score Impact**:
- [ ] **Vulnerability-Driven Risk Adjustment**: Update vendor risk scores based on vulnerabilities
  - Impact: Critical vulnerabilities increase vendor risk score (+10-20 points), major breach (+20-30 points), unpatched CVE >30 days (+5-10 points per month)
  - Triggers: Major breach affecting customer data, unpatched critical CVE >30 days (especially with public exploit), repeated security incidents (≥3 in 12 months), compliance violations
  - Outcome: Risk score increase → tier escalation (High → Critical) → enhanced monitoring (daily vs. weekly) → remediation requirements (mandatory pen test, security audit) → vendor review (contract renegotiation, replacement evaluation)
  - De-escalation: Risk score decreases when vendor remediates (verified patch deployed, incident closed, compliance restored), gradual recovery over time (demonstrate sustained security posture improvement)
- [ ] **Remediation Tracking**: Track vendor vulnerability remediation
  - Metrics: Vendor MTTR (mean time to remediate, by severity), % vulnerabilities remediated within SLA, repeat vulnerabilities (same CVE reappears), open vulnerability count
  - Reporting: Vendor security scorecards (risk score, vulnerability count, MTTR, SLA compliance), executive dashboards (top 10 high-risk vendors, trends), board reports (quarterly risk summary)
  - Benchmarking: Compare vendor MTTR against industry peers (via BitSight, SecurityScorecard benchmarks), identify laggard vendors

**Supply Chain Issue Management**:
- [ ] **Subprocessor Vulnerabilities**: Track vulnerabilities in vendor subprocessors
  - Scope: Vendor dependencies ≥3 levels deep (vendor → subprocessor → sub-subprocessor), critical subprocessors (handle PHI/PII, core infrastructure like AWS)
  - Process: Request subprocessor SBOMs (contractual requirement), scan subprocessor SBOMs for CVEs, track subprocessor remediation (via vendor or directly for critical subprocessors)
  - Risk: Subprocessor vulnerability impacts vendor (vendor's service disrupted) → impacts your organization (service unavailable, data exposed), cascading failures across supply chain
  - Monitoring: Alert on subprocessor breaches, vulnerabilities in widely-used subprocessors (AWS, Azure, GCP, Stripe, Auth0)
- [ ] **Dependency Concentration Risk**: Identify shared vulnerable components
  - Detection: Same vulnerable library used by multiple vendors (e.g., log4j used by 50 vendors), same subprocessor compromised (AWS breach affects 30 vendors)
  - Risk: Single vulnerability affects multiple vendors simultaneously (blast radius), coordinated patching required (all vendors must patch in parallel)
  - Mitigation: Diversify vendors (avoid single points of failure), implement compensating controls (WAF, network segmentation), stagger vendor patching (not all vendors patch simultaneously to avoid service disruption)
  - Metrics: Concentration index (max % vendors depending on single component/subprocessor), target ≤30%

**Remediation Workflows**:
- [ ] **Vendor Remediation Requests**: Request vendors remediate vulnerabilities
  - Process: Identify vulnerability in SBOM/platform → notify vendor via portal/email → set remediation deadline per SLA (Critical ≤7 days, High ≤30 days, Medium ≤60 days) → track progress (weekly status updates for Critical, biweekly for High) → verify fix (updated SBOM, patch notes, testing)
  - SLA: Critical vendor vulnerabilities ≤7 days response + ≤30 days remediation, High ≤7 days response + ≤60 days remediation
  - Escalation: If vendor doesn't respond or misses SLA, escalate to vendor account manager → vendor CISO → contract review → potential termination for repeated violations
  - Automation: Automated vendor notification (API, email), SLA tracking (alerts when approaching deadline), remediation verification (parse updated SBOM, verify CVE resolved)
- [ ] **Compensating Controls**: Implement controls when vendor remediation delayed
  - Examples: Enhanced monitoring (SIEM alerts on vendor API usage), network segmentation (isolate vendor integration), input validation (sanitize vendor data before processing), rate limiting (prevent exploitation via API abuse), WAF rules (block known exploit patterns)
  - Documentation: Track compensating controls in risk register (vulnerability ID, control, effectiveness, owner, removal date), remove controls when vendor patches (verify remediation, disable compensating controls, document closure)
  - Validation: Verify compensating controls effective (penetration testing, red team exercises), measure residual risk
- [ ] **Vendor Contract Review**: Review contracts for persistent security issues
  - Triggers: Repeated vulnerabilities in same component (≥3 occurrences), missed remediation SLAs (≥3 violations in 12 months), major breaches (especially PHI/PII exposure), consistent poor security posture (risk score >70 for ≥6 months)
  - Options: Renegotiate security terms (stricter SLAs, mandatory pen testing, enhanced audit rights), add security requirements (SBOM provision, vulnerability disclosure program, cyber insurance), consider vendor replacement (if security posture unacceptable)
  - Process: Vendor review meeting (security + procurement + legal) → present security issues + remediation failures → negotiate improved terms or initiate replacement vendor search

**Vulnerability Metrics**:
- [ ] **Vendor Vulnerability Count**: Track vulnerabilities per vendor
  - Breakdown: By severity (Critical, High, Medium, Low), by vendor, by component type (OS, libraries, application code)
  - Trend: Decreasing vulnerabilities indicates improving vendor security (target: ≥20% reduction year-over-year), increasing vulnerabilities indicates degrading security posture (trigger vendor review)
  - Benchmarking: Compare vulnerability density (vulnerabilities per 1,000 lines of code, vulnerabilities per SBOM component) against industry benchmarks
- [ ] **Vendor MTTR**: Mean time for vendors to remediate vulnerabilities
  - Target: Critical ≤30 days (from discovery to verified remediation), High ≤60 days, Medium ≤90 days
  - Benchmark: Compare vendor MTTR against industry averages (BitSight median MTTR: 45 days for High severity), identify slow vendors (MTTR >90th percentile)
  - Segmentation: Track MTTR by vendor tier (Critical vendors should have faster MTTR), by vulnerability type (RCE vs. XSS)
- [ ] **SBOM Coverage**: % vendors providing SBOMs
  - Target: ≥80% of software vendors provide SBOMs, ≥95% of Critical vendors
  - Trend: Increasing SBOM adoption improves supply chain visibility (track quarterly progress), mandates SBOM in new vendor contracts
  - Quality: Track SBOM quality metrics (completeness, accuracy, freshness), flag vendors with low-quality SBOMs
- [ ] **Breach Impact**: Vendors affected by security breaches
  - Metric: % vendors with security incidents in past 12 months, segmented by severity (Critical breaches with PHI/PII exposure vs. minor incidents)
  - Target: ≤10% of vendors with incidents, ≤2% with Critical incidents
  - Analysis: Identify breach patterns (ransomware trend, phishing uptick), inform vendor security requirements
- [ ] **SLA Compliance Rate**: % vulnerabilities remediated within SLA
  - Target: ≥90% of Critical vulnerabilities remediated within SLA, ≥85% of High
  - Tracking: Track SLA compliance by vendor (identify consistently non-compliant vendors), by vulnerability type
  - Consequences: Vendors with <70% SLA compliance subject to contract review, potential penalties

**Success Indicators**:
- **SBOM Coverage**: ≥80% of software vendors provide SBOMs, ≥95% of Critical vendors, quarterly updates
- **Vulnerability Detection**: Vendor vulnerabilities detected within ≤24 hours of CVE disclosure, ≥95% SBOM scan coverage
- **Vendor MTTR**: Critical ≤30 days, High ≤60 days, Medium ≤90 days (from discovery to verified remediation)
- **SLA Compliance**: ≥90% of Critical vulnerabilities remediated within SLA, ≥85% of High
- **Breach Response**: All vendor breaches assessed within ≤24 hours, impact determined within ≤48 hours
- **Platform Patching**: ≥95% of platform CVEs patched within SLA (Critical ≤24h, High ≤7d)
- **Dependency Management**: Zero high/critical vulnerabilities in vendor platform dependencies >30 days old
- **False Positive Rate**: ≤15% false positive rate on SBOM vulnerability scans

---

### Level 2: Advanced Issue Management

**AI-Powered Vulnerability Prioritization**:
- [ ] **ML-Based Risk Scoring**: AI prioritizes vendor vulnerabilities
  - Features: CVSS score, exploit availability (Exploit-DB, Metasploit), vendor criticality, affected component (core vs. optional), compensating controls
  - Algorithm: Gradient boosting or neural network predicts exploitation likelihood, business impact
  - Output: Risk score (0-100) for each vulnerability, prioritized remediation queue
  - Success Criteria: ≥85% agreement with expert prioritization, ≥90% of exploited vulnerabilities ranked in top 10%
  - Continuous Learning: Retrain model monthly using latest vulnerability data, exploitation events
- [ ] **Exploit Prediction**: Predict which vulnerabilities will be exploited
  - Prediction: Likelihood of exploitation within 30 days (based on historical data, dark web chatter, attacker TTPs)
  - Success Criteria: ≥70% precision (predicted exploits actually exploited), ≥60% recall (exploited vulnerabilities predicted)
  - Proactive Patching: Auto-escalate predicted-to-be-exploited vulnerabilities, require vendor response within ≤48 hours

**Automated Vulnerability Remediation**:
- [ ] **Auto-Patching for Low-Risk Vulnerabilities**: Automatically patch vendor platform
  - Scope: Low-risk vulnerabilities (CVSS <4.0), non-production environments, reversible changes
  - Process: Detect vulnerability → test patch in staging → deploy to production (with rollback plan) → verify remediation
  - Human-in-Loop: Require approval for production patches, Critical system patches
  - Success Criteria: ≥50% of Low/Medium vulnerabilities auto-patched, zero regressions from auto-patching
- [ ] **Automated Vendor Outreach**: AI drafts vendor vulnerability notifications
  - LLM Drafting: AI generates vendor notification (CVE details, affected components, remediation deadline, escalation path)
  - Customization: Tailored to vendor relationship (friendly tone for partners, formal for new vendors)
  - Review: Security analyst reviews + approves before sending (prevent hallucinations, ensure accuracy)
  - Success Criteria: ≥80% of AI-drafted notifications require zero edits, ≥30% reduction in analyst time

**Continuous Vulnerability Monitoring**:
- [ ] **Real-Time SBOM Scanning**: Scan SBOMs continuously as new CVEs published
  - Architecture: Stream processing (Kafka) ingests CVE feeds (NVD, OSV), matches against vendor SBOMs in real-time
  - Latency: Vendor vulnerability alerts within ≤1 hour of CVE publication
  - Scale: Process ≥10,000 CVEs/day, scan ≥1,000 vendor SBOMs
  - Success Criteria: ≥99% of vendor vulnerabilities detected within ≤24 hours of CVE disclosure
- [ ] **Predictive Vulnerability Scanning**: Identify vulnerable code before CVE assigned
  - Method: Static analysis, binary analysis, ML-based code vulnerability detection (DeepCode, Snyk Code)
  - Benefit: Discover zero-day vulnerabilities in vendor code before public CVE (responsible disclosure to vendor)
  - Success Criteria: Discover ≥5 zero-days in vendor software per year, vendor patches before public exploit

**Vendor Vulnerability SLA Enforcement**:
- [ ] **Automated SLA Tracking**: Track vendor remediation SLAs automatically
  - Tracking: Vulnerability discovered date, vendor notified date, SLA deadline, current status, days remaining
  - Alerts: Alert when approaching SLA deadline (≤20% time remaining), alert on SLA miss
  - Dashboard: Real-time SLA compliance dashboard (per vendor, per severity, overall)
- [ ] **Contract Penalties for SLA Violations**: Enforce contractual penalties
  - Penalties: Service credits for SLA misses (e.g., 10% monthly fee per missed Critical SLA), escalating penalties for repeat violations
  - Automation: Calculate penalties automatically, invoice vendor (if contract allows)
  - Fairness: Allow vendor to contest penalties (provide evidence of extenuating circumstances)

**Supply Chain Vulnerability Mapping**:
- [ ] **Vulnerability Propagation Analysis**: Map vulnerability cascades through supply chain
  - Graph: Build dependency graph (vendor → subprocessor → components), identify vulnerability paths
  - Analysis: If component X vulnerable, which vendors affected? Which subprocessors? What's blast radius?
  - Prioritization: Vulnerabilities affecting ≥10 vendors = high priority (coordinate patching across vendors)
  - Success Criteria: Complete supply chain vulnerability map, blast radius calculated for each CVE

**Success Indicators - Level 2**:
- **AI Prioritization**: ≥85% agreement with expert prioritization, ≥90% of exploited vulnerabilities in top 10%
- **Exploit Prediction**: ≥70% precision, ≥60% recall for exploitation prediction
- **Auto-Remediation**: ≥50% of Low/Medium vulnerabilities auto-patched, zero regressions
- **Real-Time Monitoring**: ≥99% vulnerabilities detected within ≤24 hours of CVE disclosure, alert latency ≤1 hour
- **SLA Enforcement**: Automated tracking for 100% of vendor vulnerabilities, ≥90% SLA compliance

---

### Level 3: Research-Grade Issue Management

**Autonomous Vulnerability Management**:
- [ ] **Full-Cycle Autonomous Remediation**: AI manages vendor vulnerabilities end-to-end
  - Workflow: Detect vulnerability → assess risk → notify vendor (AI-drafted message) → track remediation → verify fix → close ticket (all automated)
  - AI Capabilities: LLM prioritizes vulnerabilities, drafts vendor communications, evaluates remediation evidence, makes escalation decisions
  - Human Oversight: Human approval required for Critical vendors, contract penalties, vendor termination
  - Success Criteria: ≥70% of Low/Medium vulnerabilities fully autonomous, ≥95% accuracy vs. human decisions
- [ ] **Self-Learning Vulnerability System**: System improves based on outcomes
  - Learning: Track which vulnerabilities exploited, which vendors missed SLAs, which controls effective
  - Adaptation: Update risk model (upweight features predicting exploitation), adjust SLAs (faster for slow vendors), improve notifications (templates with highest response rates)
  - Success Criteria: ≥15% improvement in exploitation prediction annually, ≥10% improvement in vendor MTTR

**Formal Verification of Vulnerability Management**:
- [ ] **Provably Complete Vulnerability Detection**: Mathematically prove all vulnerabilities detected
  - Method: Formal specification of vulnerability scanning requirements (all CVEs scanned, all SBOMs analyzed)
  - Verification: Prove implementation scans all required sources, no CVEs missed
  - Properties: Completeness (all vulnerabilities detected), timeliness (detection within ≤24 hours), accuracy (≤15% false positives)
  - Success Criteria: Formal proof of vulnerability detection completeness, zero audit findings for missed vulnerabilities
- [ ] **Verified Remediation Workflows**: Formally verify remediation processes
  - Specification: Remediation workflow as state machine (discovered → notified → in_progress → verified → closed)
  - Verification: Prove all vulnerabilities eventually reach closed state, SLAs enforced correctly
  - Success Criteria: Formal proof of remediation process correctness, zero SLA tracking errors

**Quantum-Resistant Vulnerability Analysis**:
- [ ] **Post-Quantum Cryptography Vulnerability Assessment**: Assess vendor quantum readiness
  - Assessment: Identify vendors using quantum-vulnerable crypto (RSA, ECDH, ECDSA), assess migration plans to PQC
  - Timeline: Track vendor PQC adoption, require Critical vendors migrate by 2030
  - Vulnerability: Treat quantum-vulnerable crypto as vulnerability (medium severity now, high severity post-2030)
  - Success Criteria: 100% of Critical vendors have PQC migration plans, ≥50% completed migration by 2030

**Research Publications**:
- [ ] **Vendor Vulnerability Management Framework**: Publish open-source framework
  - Framework: Complete vendor vulnerability management system (SBOM scanning, ML prioritization, automated vendor outreach, SLA tracking)
  - License: Apache 2.0, permissive open source
  - Community: ≥10,000 GitHub stars, ≥50 contributors, used by ≥100 organizations
- [ ] **Academic Publications**: Publish vulnerability management research
  - Venues: IEEE S&P, USENIX Security, ACM CCS, NDSS
  - Topics: ML-based vulnerability prioritization, exploit prediction, autonomous vulnerability remediation, supply chain vulnerability propagation
  - Success Criteria: ≥3 publications in top-tier security conferences, ≥100 citations

**Success Indicators - Level 3**:
- **Autonomous Management**: ≥70% of vulnerabilities fully autonomous, ≥95% accuracy vs. human decisions
- **Self-Learning**: ≥15% annual improvement in exploitation prediction, ≥10% improvement in vendor MTTR
- **Formal Verification**: Formal proof of vulnerability detection completeness, zero audit findings
- **Quantum Readiness**: 100% Critical vendors have PQC plans, ≥50% migrated by 2030
- **Research Impact**: ≥10,000 GitHub stars on open source framework, ≥3 academic publications

---

**Document Information**: Practice: Issue Management (IM) | Domain: Vendors | HAIAMM v2.1 | Last Updated: 2025-12-30
