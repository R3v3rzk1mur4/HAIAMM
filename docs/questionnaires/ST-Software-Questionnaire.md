# Security Testing (ST) - Software Domain
## HAIAMM Assessment Questionnaire v2.0

**Practice:** Security Testing (ST)
**Domain:** Software
**Purpose:** Assess organizational maturity in security testing for Human Assisted Intelligence software security systems

---

## Instructions

- Answer each question honestly based on **current, implemented practices** (not plans or aspirations)
- **"Yes" requires evidence** - Document proof for each affirmative answer
- **Answer progressively** - Complete all Level 1 questions before Level 2
- **Level progression** - Achieve ALL questions at lower level before advancing
- **Partial implementation = "No"** - Practice must be complete and systematic

---

## Level 1: Foundational
**Objective:** Establish comprehensive security testing program for AI systems

### Question 1: AI Model Security Testing

**Q1.1:** Do you conduct comprehensive security testing of HAI models including adversarial robustness testing (evasion attacks, data poisoning), model performance testing (accuracy, edge cases), and explainability testing?

**Evidence Required:**
- [ ] Adversarial robustness testing performed:
  - Evasion attacks (model detects ≥70% of adversarial examples)
  - Data poisoning testing (accuracy drop ≤10% with 5% poisoned data)
  - Model inversion testing (reconstruction accuracy ≤10%)
- [ ] Model performance testing documented:
  - Test set with ≥10,000 samples
  - Accuracy metrics (Precision ≥90%, Recall ≥85%)
  - Edge case testing (obfuscated code, encoding variations)
- [ ] Explainability testing completed (≥80% of explanations rated "helpful")
- [ ] Test results documented and reviewed by security team

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

### Question 2: Code Analysis Accuracy and Integration Security Testing

**Q1.2:** Do you test SAST/DAST accuracy (true positive rate ≥90%, false positive rate ≤5%) and conduct integration security testing for APIs, IDE plugins, and CI/CD pipelines?

**Evidence Required:**
- [ ] SAST accuracy testing with benchmarks:
  - True positive rate ≥90% (detects known vulnerabilities)
  - False positive rate ≤5% (doesn't over-alert)
  - False negative rate ≤10% (doesn't miss vulnerabilities)
- [ ] DAST testing against vulnerable applications (OWASP Juice Shop, WebGoat)
  - Detects ≥85% of OWASP Top 10 vulnerabilities
- [ ] API security testing (authentication, authorization, input validation, rate limiting)
- [ ] IDE plugin security (no sensitive data leakage)
- [ ] CI/CD integration security (fail-safe behavior, no credential leakage)

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

### Question 3: Prompt Injection Testing and Automated Regression Testing

**Q1.3:** If using LLM-based HAI tools, do you conduct comprehensive prompt injection testing (covering attack intents, techniques, and evasions), and maintain an automated regression test suite that runs on every code change?

**Evidence Required:**
- [ ] Prompt injection testing (if LLM-based tools):
  - Attack intent testing (system prompt leak, jailbreak, data exfiltration) - ≥95% blocked
  - Attack technique testing (role-playing, cognitive overload, nested injection)
  - Attack evasion testing (encoding, obfuscation, character manipulation)
  - Documented test results showing defense effectiveness
- [ ] Automated regression test suite:
  - Coverage ≥90% of critical functionality
  - Runs on 100% of PRs before merge
  - Execution time ≤30 minutes
- [ ] Model regression testing (accuracy drop ≤2% after updates)
- [ ] If no LLM-based tools: Alternative comprehensive testing documented

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

**Level 1 Score:** _____ / 3 questions answered "Yes"

**Level 1 Achieved:** ☐ Yes (3/3) ☐ No (< 3/3)

---

## Level 2: Comprehensive
**Objective:** Implement continuous adversarial testing and third-party security validation

**Prerequisites:** ALL Level 1 questions must be "Yes" to proceed to Level 2

### Question 4: Continuous Adversarial Testing and Fuzzing

**Q2.1:** Do you conduct ongoing adversarial testing through continuous red team exercises, fuzz testing for AI models, and property-based testing to validate security invariants?

**Evidence Required:**
- [ ] Continuous red team exercises (at least quarterly)
  - Red team attempts to bypass AI security gates
  - Documented adversarial attack attempts and success/failure rates
  - Findings fed back into model retraining or defense improvements
- [ ] Fuzz testing program for AI models
  - Mutate inputs to find crashes, errors, or unexpected behavior
  - Tools and methodology documented (AFL, libFuzzer, or custom)
  - Fuzzing coverage metrics tracked
- [ ] Property-based testing implemented
  - Security invariants defined and tested (e.g., "No SQL injection should pass SAST")
  - Automated property testing integrated into CI/CD
- [ ] Test results tracked over time (trending analysis)

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

### Question 5: Third-Party Penetration Testing and Performance Benchmarking

**Q2.2:** Do you conduct annual third-party penetration testing of your HAI systems and benchmark performance against industry standards?

**Evidence Required:**
- [ ] Annual third-party penetration testing completed
  - Independent security firm engaged
  - Scope covers AI models, APIs, infrastructure, integrations
  - Penetration test report with findings and remediation
  - Critical/High findings remediated within defined SLA
- [ ] Performance benchmarking against industry standards
  - Latency benchmarks (IDE response ≤3s, API P95 ≤500ms)
  - Scalability benchmarks (concurrent users, requests/second)
  - Accuracy benchmarks (comparison to OWASP Benchmark, industry tools)
- [ ] Benchmarking results shared with leadership
- [ ] Performance metrics tracked over time

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

### Question 6: Threat Model Validation Testing and Attack Surface Analysis

**Q2.3:** Do you conduct testing specifically designed to validate your threat models, including attack surface analysis and quantified tracking of security posture improvements over time?

**Evidence Required:**
- [ ] Threat model validation testing program
  - Test cases derived from documented threats (from TA practice)
  - Each threat scenario tested (e.g., prompt injection, model evasion, data poisoning)
  - Validation results documented (threat mitigated / residual risk)
- [ ] Attack surface analysis conducted
  - Attack surface quantified (exposed APIs, authentication points, input vectors)
  - Reduction in attack surface measured over time
  - Findings drive architectural improvements
- [ ] Security posture trending
  - Vulnerability detection rate tracked over time
  - Mean time to detect (MTTD) and remediate (MTTR) tracked
  - Security metrics reviewed quarterly with stakeholders

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

**Level 2 Score:** _____ / 3 questions answered "Yes"

**Level 2 Achieved:** ☐ Yes (3/3) ☐ No (< 3/3)

---

## Level 3: Industry-Leading
**Objective:** Achieve formal verification, AI-assisted testing, and public security validation

**Prerequisites:** ALL Level 2 questions must be "Yes" to proceed to Level 3

### Question 7: Formal Verification and AI-Assisted Security Testing

**Q3.1:** Do you employ formal verification for critical security properties and use AI-assisted security testing to generate test cases and discover edge cases?

**Evidence Required:**
- [ ] Formal verification implemented for critical security properties
  - Properties formally specified (e.g., "No user input can bypass authentication")
  - Verification tools used (TLA+, Coq, Isabelle/HOL, or similar)
  - Verification proofs completed and validated
  - At least 3 critical security properties formally verified
- [ ] AI-assisted security testing program
  - AI generates test cases automatically (adversarial examples, edge cases)
  - AI discovers previously unknown vulnerability patterns
  - Evidence of AI-generated test cases finding real issues
  - AI testing integrated into continuous testing pipeline

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

### Question 8: Bug Bounty Program and Continuous Production Security Validation

**Q3.2:** Do you operate a bug bounty program for external security researchers and conduct continuous security validation in production through runtime testing and canary deployments?

**Evidence Required:**
- [ ] Active bug bounty program
  - Public bug bounty platform (HackerOne, Bugcrowd) or private program
  - Bounty program covers AI security systems (models, APIs, integrations)
  - At least 1 submission received and processed per quarter
  - Documented bounty payouts and vulnerability fixes
- [ ] Continuous security validation in production
  - Runtime security testing (canary analysis, shadow deployments)
  - Production monitoring of model behavior and security metrics
  - Automated rollback on security degradation detection
  - Evidence of production security validation preventing issues

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

### Question 9: Public Security Testing Reports and Industry Contribution

**Q3.3:** Do you publish public security testing reports demonstrating transparency, and contribute security testing methodologies, datasets, or tools to the industry?

**Evidence Required:**
- [ ] Public security testing reports published (at least annually)
  - Security testing methodology disclosed
  - Aggregate security metrics shared (without sensitive details)
  - Public evidence (blog post, security page, transparency report)
  - Demonstrates commitment to security transparency
- [ ] Industry contributions (at least 1 per year):
  - Published security testing methodologies or best practices
  - Open-source security testing tools or frameworks
  - Contributed datasets for AI security benchmarking
  - Participation in AI security testing standards development
- [ ] Public evidence (GitHub repositories, conference presentations, academic papers)

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

**ST-Software Practice Score:** _______ / 3.0

### Precise Scoring (For Formal Audits)

```
L1_score = (L1 "Yes" answers) / 3
L2_score = (L2 "Yes" answers) / 3 × L1_score
L3_score = (L3 "Yes" answers) / 3 × L2_score

Practice Score = L1_score + L2_score + L3_score
```

**ST-Software Practice Score (Precise):** _______ / 3.0

---

## Assessment Summary

**Assessment Date:** _________________________________

**Assessor(s):** _____________________________________

**HAI System(s) Assessed:** __________________________

**Overall Maturity Level:**
- ☐ Level 0 (Score < 1.0): Ad-hoc, no formal security testing
- ☐ Level 1 (Score 1.0 - 1.9): Comprehensive testing program established
- ☐ Level 2 (Score 2.0 - 2.9): Continuous adversarial testing and third-party validation
- ☐ Level 3 (Score 3.0): Formal verification and public security validation

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

## Security Testing Specific Notes

**Testing Categories Covered:**
- [ ] AI model security (adversarial robustness, performance, explainability)
- [ ] Code analysis accuracy (SAST/DAST true/false positive rates)
- [ ] Integration security (API, IDE plugins, CI/CD)
- [ ] Infrastructure security (deployment, database, secrets)
- [ ] Performance and scalability (latency, throughput, scalability)
- [ ] Resilience and fail-safe behavior
- [ ] Compliance and privacy (GDPR, data retention)

**Prompt Injection Testing (if LLM-based):**
- [ ] Attack intent coverage (13 attack goals tested)
- [ ] Attack technique coverage (18 attack methods tested)
- [ ] Attack evasion coverage (20 evasion methods tested)
- [ ] Defense effectiveness ≥95% for all attack categories

**Test Automation:**
- [ ] Regression tests run on every PR (100% coverage)
- [ ] CI/CD integration (fail-safe deployment blocking)
- [ ] Performance tests automated (latency, scalability)
- [ ] Security tests integrated into development workflow

---

**Document Version:** 2.0
**Last Updated:** 2025-12-29
**Next Review:** Quarterly or after significant HAI system changes
