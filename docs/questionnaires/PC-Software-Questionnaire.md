# Policy & Compliance (PC) - Software Domain
## HAIAMM Assessment Questionnaire v2.0

**Practice:** Policy & Compliance (PC)
**Domain:** Software
**Purpose:** Assess organizational maturity in policies and compliance for Human Assisted Intelligence software security operations

---

## Instructions

- Answer each question honestly based on **current, implemented practices** (not plans or aspirations)
- **"Yes" requires evidence** - Document proof for each affirmative answer
- **Answer progressively** - Complete all Level 1 questions before Level 2
- **Level progression** - Achieve ALL questions at lower level before advancing
- **Partial implementation = "No"** - Practice must be complete and systematic

---

## Level 1: Foundational
**Objective:** Establish foundational policies for AI-operated software security and identify compliance requirements

### Question 1: AI Agent Operations Policies and Finding Quality Standards

**Q1.1:** Do you have documented policies governing how AI agents operate software security functions (code scanning, security testing, deployment gates), including acceptable AI autonomy, finding quality standards (false positive rates <20%), and developer experience requirements?

**Evidence Required:**
- [ ] Written policy document governing AI agent operations in software security
- [ ] AI Agent Scope defined (which software security functions AI may perform: SAST/DAST, SCA, security testing, code review, CI/CD gates)
- [ ] Deployment Gate Authority specified (what security decisions AI can make autonomously vs. requiring override)
- [ ] Finding Quality Standards defined:
  - AI SAST/DAST false positive rate <20%
  - AI security findings must be actionable (include remediation guidance)
  - Accuracy requirements documented
- [ ] Developer Experience Policies included:
  - AI tools integrate into development workflow (IDE, PR comments, CI/CD)
  - AI security checks complete in <10 minutes
  - Security vs. velocity balance defined
- [ ] Policies approved by leadership (CISO, VP Engineering, or equivalent)
- [ ] Policies communicated to developers and security teams

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

### Question 2: Compliance Framework Identification and Mapping

**Q1.2:** Have you identified and documented applicable compliance requirements (PCI-DSS Requirement 6, HIPAA, OWASP ASVS, NIST SSDF, SOX) that apply to AI-operated software security, with mapping showing how AI capabilities meet each requirement?

**Evidence Required:**
- [ ] Compliance frameworks identified and documented (applicable to your organization):
  - Secure Development Standards: OWASP ASVS, NIST SSDF, ISO 27034
  - Regulatory Requirements: PCI-DSS Req 6 (if payment data), HIPAA §164.308(a)(8) (if health data), SOX (if financial apps)
  - Industry Frameworks: BSIMM, SAMM, or equivalent
  - Customer Requirements: Vendor security questionnaires requiring secure development evidence
- [ ] Compliance-to-AI mapping documented:
  - Does AI code scanning meet mandatory scanning requirements (PCI-DSS 6.3.2, HIPAA risk analysis)?
  - Does AI security testing meet testing requirements (OWASP ASVS verification)?
  - Does AI code review satisfy secure development requirements?
  - Can you demonstrate AI software security effectiveness to auditors?
- [ ] Gaps identified (requirements AI doesn't meet, requiring manual processes)
- [ ] Compliance documentation reviewed within last 12 months

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

### Question 3: Audit Trail and Developer Workflow Requirements

**Q1.3:** Do you maintain comprehensive audit trails for all AI software security decisions (vulnerabilities detected, security gate decisions, developer overrides with justification), and have documented policies for developer override procedures?

**Evidence Required:**
- [ ] Audit Trail Requirements implemented:
  - All AI security findings logged (vulnerability type, severity, location, timestamp)
  - Security gate decisions logged (build passed/failed, reason)
  - Developer overrides logged (who, when, justification, AppSec approval if required)
  - Audit logs retained per compliance requirements (≥1 year)
- [ ] Developer Override Procedures documented:
  - Critical vulnerabilities (SQL injection, RCE, auth bypass) require AppSec approval to override
  - High/Medium findings allow developer override with documented justification
  - Override process is auditable and reviewable
- [ ] Audit trail accessible for compliance audits and security reviews
- [ ] Evidence of audit trail supporting successful compliance audits

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

**Level 1 Score:** _____ / 3 questions answered "Yes"

**Level 1 Achieved:** ☐ Yes (3/3) ☐ No (< 3/3)

---

## Level 2: Comprehensive
**Objective:** Implement comprehensive risk-based policies with regular validation and developer feedback

**Prerequisites:** ALL Level 1 questions must be "Yes" to proceed to Level 2

### Question 4: Application Risk-Based Policies and Developer Experience Governance

**Q2.1:** Do you implement comprehensive application risk-based policies that specify different AI requirements for each application tier (critical/high/medium/low), with developer experience governance including tool integration requirements, finding presentation standards, and documented feedback mechanisms?

**Evidence Required:**
- [ ] Application Risk Classification Policies documented:
  - Risk tiers defined (Critical/High/Medium/Low based on business criticality, data sensitivity)
  - Different AI scanning depth for each tier (e.g., Critical = comprehensive SAST/DAST/SCA, Low = basic SAST)
  - Different security gate strictness per tier (e.g., Critical = block on High findings, Low = block on Critical only)
  - All applications classified according to framework
- [ ] Technology Stack Policies defined (different AI tool selection for different languages/frameworks)
- [ ] Security Finding Severity Policies with corresponding actions:
  - Critical = block deployment + immediate fix
  - High = fix within sprint (7 days)
  - Medium/Low = backlog with defined SLA
- [ ] Developer Experience Governance implemented:
  - Tool Integration Requirements (AI tools integrate into IDE, PR checks, CI/CD)
  - Finding Presentation Standards (clear descriptions, remediation examples, secure coding links)
  - Developer Training Requirements (training on AI security tools and secure coding)
- [ ] Documented feedback mechanisms (developers can report tool friction, false positives, missing features)
- [ ] Policies reviewed and updated at least annually

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

### Question 5: Regular Software Security Validation and Testing

**Q2.2:** Do you conduct regular validation of AI software security effectiveness through quarterly AI tool testing, monthly false positive audits, annual penetration testing that validates AI findings, and annual benchmark testing against standard test suites?

**Evidence Required:**
- [ ] Quarterly Vulnerability Detection Validation:
  - Inject known vulnerabilities to measure AI detection rates
  - Validate true positive rates (≥85% detection of known vulnerabilities)
  - Document results and trends
- [ ] Monthly False Positive Audits:
  - Review developer-reported false positives
  - Measure false positive rate (trending toward <10%)
  - Tune AI tools to reduce noise
- [ ] Annual Penetration Testing including AI validation:
  - Penetration tests review AI security findings
  - Compare pentest findings to AI findings (did AI miss vulnerabilities? Did AI generate false positives?)
  - Document gaps and improvements
- [ ] Annual Benchmark Testing:
  - Test AI security tools against standard test suites (OWASP Benchmark, NIST SAMATE, or equivalent)
  - Compare results to industry baselines
  - Validate AI tool effectiveness objectively
- [ ] Developer Satisfaction Surveys conducted (at least annually)
- [ ] Validation results drive tool improvements and policy updates

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

### Question 6: False Positive Management and Developer Feedback

**Q2.3:** Do you have documented procedures for false positive handling with defined SLAs for AppSec team review, track false positive rate trends showing improvement, and demonstrate evidence of tool improvements based on developer feedback?

**Evidence Required:**
- [ ] False Positive Handling Procedures documented:
  - False positive report form or process
  - AppSec team SLA for review (e.g., ≤5 business days)
  - AI tool tuning based on validated false positives
  - Suppression rules documented and reviewed
- [ ] False Positive Rate Trending:
  - False positive rate tracked over time (monthly/quarterly)
  - Historical data (≥6 months) showing improvement trend
  - Target false positive rate defined (e.g., <10%) and tracking toward goal
- [ ] Developer Feedback Implementation:
  - Feedback collected regularly (surveys, tickets, retrospectives)
  - Evidence of acting on feedback (tool configuration changes, vendor engagement, process improvements)
  - Developer satisfaction metrics tracked (trending positive)
  - Communication loop closed (developers informed of changes made based on feedback)
- [ ] AI software security successfully passes compliance audits
- [ ] Evidence of continuous improvement (tool effectiveness improving, developer satisfaction increasing)

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

**Level 2 Score:** _____ / 3 questions answered "Yes"

**Level 2 Achieved:** ☐ Yes (3/3) ☐ No (< 3/3)

---

## Level 3: Industry-Leading
**Objective:** Achieve continuous security validation, AI-assisted remediation, and industry leadership in secure development standards

**Prerequisites:** ALL Level 2 questions must be "Yes" to proceed to Level 3

### Question 7: Continuous Security Validation and Real-Time Monitoring

**Q3.1:** Do you deploy continuous security validation with real-time dashboards showing vulnerability density trends, AI finding accuracy, remediation velocity, and automated effectiveness testing that continuously validates AI security tool detection?

**Evidence Required:**
- [ ] Real-Time Security Dashboards deployed:
  - Live visibility into software security posture
  - Vulnerability density trends tracked over time
  - AI finding accuracy metrics (true positive rate, false positive rate)
  - Remediation velocity tracked (time from detection to fix)
  - Security gate pass rates monitored
  - Dashboards accessible to security leadership and development teams
- [ ] Automated Effectiveness Testing implemented:
  - Continuous validation of AI security tool detection (daily or more frequent)
  - Automated injection of test vulnerabilities
  - Automated measurement of AI detection rates
  - Automated alerting on detection degradation
- [ ] Trend Analysis capabilities:
  - Historical tracking (≥12 months) of security metrics
  - Predictive analytics (forecast vulnerability trends, capacity needs)
  - Evidence of trends driving investment decisions
- [ ] Automated Security Evidence generation for compliance (vulnerability scan results, remediation records, security testing reports)
- [ ] Security Regression Detection (AI detects when code changes re-introduce previously fixed vulnerabilities)

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

### Question 8: AI-Assisted Remediation and Automated Testing

**Q3.2:** Do you implement AI-assisted vulnerability remediation capabilities (AI suggests or auto-applies security fixes with developer review), automated security test case generation, and intelligent finding prioritization based on exploitability and business impact?

**Evidence Required:**
- [ ] AI-Assisted Remediation implemented:
  - AI suggests security fixes for vulnerabilities (code patches, configuration changes)
  - AI auto-applies fixes to developer branches with review workflow (optional)
  - Developer review and approval required before merging AI fixes
  - Evidence of AI-assisted remediation accelerating fix times (≥30% faster remediation)
  - Tools: GitHub Copilot Autofix, AI-generated patches, or equivalent
- [ ] Automated Security Testing:
  - AI generates security test cases based on code changes
  - AI executes security tests automatically in CI/CD
  - Coverage tracking for AI-generated tests
- [ ] Intelligent Finding Prioritization:
  - AI prioritizes remediation based on exploitability (CVSS, EPSS, threat intelligence)
  - Business impact considered (application criticality, data sensitivity)
  - Attack surface analysis (internet-facing vs. internal)
  - Evidence of prioritization improving remediation efficiency
- [ ] Proactive Security Guidance (AI provides security recommendations during coding in IDE)
- [ ] Security Debt Tracking (AI helps manage unresolved findings, predicts security debt accumulation)

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

### Question 9: Industry Standards Contribution and Explainable AI Findings

**Q3.3:** Do you actively contribute to secure development AI standards (OWASP, NIST SSDF, IEEE), participate in AI security tool benchmarking, and implement explainable AI security findings where developers can understand why AI flagged code?

**Evidence Required:**
- [ ] Industry Standards Contributions (at least 2 per year):
  - Participation in secure development standards development (OWASP AI security tools guidance, NIST SSDF AI integration, IEEE standards)
  - Contributions to AI tool benchmarking initiatives (vendor-neutral tool comparisons)
  - Published research or best practices on AI secure development
  - Open-source security tool contributions (OWASP projects, community scanners, shared vulnerability datasets)
- [ ] Explainable AI Findings implemented:
  - AI security findings include explanations (WHY code was flagged, not just THAT it was flagged)
  - Developers can understand reasoning (feature importance, matched patterns, security rule triggered)
  - Explanation quality validated (≥80% of developers find explanations helpful)
  - Evidence of explainability improving developer trust and adoption
- [ ] Public Evidence:
  - Conference presentations on AI secure development
  - Blog posts or white papers published
  - GitHub repositories with open-source contributions
  - Standards body participation documented
- [ ] Documented industry impact (vendor product improvements, peer organization adoption, standards influenced)
- [ ] Zero critical application security findings in production that AI tools should have detected (12+ month track record)

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

**PC-Software Practice Score:** _______ / 3.0

### Precise Scoring (For Formal Audits)

```
L1_score = (L1 "Yes" answers) / 3
L2_score = (L2 "Yes" answers) / 3 × L1_score
L3_score = (L3 "Yes" answers) / 3 × L2_score

Practice Score = L1_score + L2_score + L3_score
```

**PC-Software Practice Score (Precise):** _______ / 3.0

---

## Assessment Summary

**Assessment Date:** _________________________________

**Assessor(s):** _____________________________________

**HAI System(s) Assessed:** __________________________

**Overall Maturity Level:**
- ☐ Level 0 (Score < 1.0): Ad-hoc, no formal policies for AI software security
- ☐ Level 1 (Score 1.0 - 1.9): Foundational policies and compliance mapping established
- ☐ Level 2 (Score 2.0 - 2.9): Comprehensive risk-based policies with regular validation
- ☐ Level 3 (Score 3.0): Continuous validation and industry leadership

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

## Policy & Compliance Specific Notes

**Policy Coverage:**
- [ ] AI Agent Operations Policies (scope, autonomy, finding quality)
- [ ] Application Risk Classification Policies (critical/high/medium/low tiers)
- [ ] Developer Experience Policies (tool integration, workflows, training)
- [ ] Security Finding Severity Policies (critical/high/medium/low actions)
- [ ] Override Procedures (when developers can override AI findings)
- [ ] Audit Trail Requirements (logging all AI security decisions)

**Compliance Frameworks Addressed:**
- [ ] PCI-DSS Requirement 6 (Secure Development, Code Review)
- [ ] OWASP ASVS (Application Security Verification Standard)
- [ ] NIST SSDF (Secure Software Development Framework)
- [ ] HIPAA §164.308(a)(8) (Evaluation - if applicable)
- [ ] SOX (Change Management for Financial Applications - if applicable)
- [ ] ISO 27034 (Application Security)

**Validation Activities:**
- [ ] Quarterly vulnerability detection validation
- [ ] Monthly false positive audits
- [ ] Annual penetration testing including AI validation
- [ ] Annual benchmark testing (OWASP Benchmark, NIST SAMATE)
- [ ] Developer satisfaction surveys

**AI-Assisted Capabilities (Level 3):**
- [ ] Real-time security dashboards
- [ ] Automated effectiveness testing
- [ ] AI-assisted remediation (fix suggestions/auto-apply)
- [ ] Automated security test generation
- [ ] Intelligent finding prioritization
- [ ] Explainable AI findings

---

**Document Version:** 2.0
**Last Updated:** 2025-12-29
**Next Review:** Quarterly or after significant HAI system changes
