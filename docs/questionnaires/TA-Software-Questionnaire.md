# Threat Assessment (TA) - Software Domain
## HAIAMM Assessment Questionnaire v2.0

**Practice:** Threat Assessment (TA)
**Domain:** Software
**Purpose:** Assess organizational maturity in identifying and analyzing threats specific to Human Assisted Intelligence in software security operations

---

## Instructions

- Answer each question honestly based on **current, implemented practices** (not plans or aspirations)
- **"Yes" requires evidence** - Document proof for each affirmative answer
- **Answer progressively** - Complete all Level 1 questions before Level 2
- **Level progression** - Achieve ALL questions at lower level before advancing
- **Partial implementation = "No"** - Practice must be complete and systematic

---

## Level 1: Foundational
**Objective:** Establish baseline threat awareness for HAI software security

### Question 1: AI-Specific Threat Scenario Identification

**Q1.1:** Have you documented threat scenarios specific to Human Assisted Intelligence systems performing software security functions (e.g., SAST/DAST, code review, security testing), including adversarial manipulation, data poisoning, operational failures, and prompt injection attacks?

**Evidence Required:**
- [ ] Inventory of HAI systems performing software security functions
- [ ] Documented threat scenarios covering at least 4 categories:
  - Adversarial manipulation (prompt injection, security gate bypass, model evasion)
  - Data poisoning (training corruption, false positive injection)
  - Operational failures (false negatives/positives, model drift, cascading failures)
  - Supply chain threats (compromised AI tools, model tampering)
- [ ] Threat scenarios based on Arcanum PI Taxonomy for prompt injection (if LLM-based tools)
- [ ] Document updated within last 12 months

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

### Question 2: Threat Model Documentation and Ownership

**Q1.2:** Do you have documented threat models for your HAI software security operations, with identified threat owners responsible for tracking and mitigating each threat category?

**Evidence Required:**
- [ ] Formal threat model document for AI software security operations
- [ ] Threat model covers: attack vectors, failure modes, adversarial risks
- [ ] Each threat category has assigned owner (individual or team)
- [ ] Threat model includes impact assessment (what happens if threat materializes)
- [ ] Threat model reviewed and approved by security leadership
- [ ] Threat model accessible to relevant teams (security, engineering, AI/ML)

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

### Question 3: Threat Awareness Training

**Q1.3:** Have you conducted threat awareness training for developers, security engineers, and engineering leadership on AI-specific threats to software security operations within the last 90 days of AI tool deployment?

**Evidence Required:**
- [ ] Training materials covering AI software security threats
- [ ] Training delivered to at least 3 stakeholder groups:
  - Developers (AI code generation risks, when to distrust AI findings)
  - Security engineers (adversarial ML attacks, AI tool limitations)
  - Engineering leadership (business risks, governance requirements)
- [ ] Training includes real-world examples (research papers, bypass techniques, case studies)
- [ ] Training conducted within 90 days of AI security tool deployment
- [ ] Attendance records and training completion tracking

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

**Level 1 Score:** _____ / 3 questions answered "Yes"

**Level 1 Achieved:** ☐ Yes (3/3) ☐ No (< 3/3)

---

## Level 2: Comprehensive
**Objective:** Quantify and prioritize AI software security threats by business impact and likelihood

**Prerequisites:** ALL Level 1 questions must be "Yes" to proceed to Level 2

### Question 4: Abuse Cases and Attack Trees

**Q2.1:** Have you developed detailed abuse cases and attack trees for each HAI agent performing software security, showing how adversaries could exploit or degrade HAI security operations?

**Evidence Required:**
- [ ] At least 3-5 abuse cases documented per AI security agent
- [ ] Abuse cases include:
  - Attacker goal, attack path (step-by-step), prerequisites, impact, likelihood
- [ ] Attack trees showing multiple paths to compromise (e.g., "Deploy vulnerable code" with branches)
- [ ] Specific examples documented:
  - Adversarial code evasion (obfuscation to bypass AI SAST)
  - Prompt injection via code comments (manipulate AI code reviewer)
  - False positive flooding to create alert fatigue
- [ ] Abuse cases validated by security team and shared with stakeholders

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

### Question 5: Risk Prioritization Matrix

**Q2.2:** Have you assessed and prioritized AI software security threats using a risk matrix (likelihood × impact), with documented mitigation strategies for high-priority threats?

**Evidence Required:**
- [ ] Risk assessment framework with likelihood and impact criteria
- [ ] Each threat scenario assessed for:
  - Likelihood (High/Medium/Low based on technical feasibility, skill required)
  - Business impact (Critical/High/Medium/Low based on breach cost, compliance, reputation)
- [ ] Risk matrix created (e.g., 3×3 or 5×5 grid)
- [ ] High-priority threats identified (High likelihood + High impact)
- [ ] Mitigation strategies documented for top 5-10 threats
- [ ] Risk assessment reviewed quarterly and updated based on threat intelligence

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

### Question 6: Threat Intelligence Integration and Validation

**Q2.3:** Have you integrated threat intelligence from academic research, vulnerability databases, and industry sources to continuously identify emerging threats to AI software security, with annual validation of threat models?

**Evidence Required:**
- [ ] Threat intelligence sources identified and monitored:
  - Academic research (NeurIPS, ICML, arXiv for adversarial ML)
  - CVE database (for AI/ML libraries in security tools)
  - AI security vendor advisories (Snyk, GitHub, Veracode)
  - MITRE ATLAS or OWASP ML Top 10
- [ ] Monitoring cadence established:
  - Weekly: CVE scanning
  - Monthly: Academic research review
  - Quarterly: Threat model updates
- [ ] Threat intelligence findings documented in structured format
- [ ] Annual comprehensive threat model validation completed

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

**Level 2 Score:** _____ / 3 questions answered "Yes"

**Level 2 Achieved:** ☐ Yes (3/3) ☐ No (< 3/3)

---

## Level 3: Industry-Leading
**Objective:** Proactively test and share threat intelligence through adversarial testing and industry contribution

**Prerequisites:** ALL Level 2 questions must be "Yes" to proceed to Level 3

### Question 7: Adversarial Testing and Red Team Exercises

**Q3.1:** Do you conduct periodic (at least quarterly) adversarial testing and red team exercises against your HAI software security agents to proactively identify weaknesses before attackers do?

**Evidence Required:**
- [ ] Quarterly evasion testing program established
- [ ] Testing methodology includes:
  - Create vulnerable code samples
  - Apply adversarial obfuscation techniques (encoding, API misuse, control flow obfuscation)
  - Measure evasion success rate (target: AI detects >95% of adversarial samples)
- [ ] Semi-annual prompt injection testing (for LLM-based tools)
- [ ] Test reports documenting:
  - Evasion techniques that succeeded
  - Specific vulnerability types bypassed
  - Recommendations for improvement
- [ ] Evidence of AI vendor engagement or model retraining when evasion rate >5%

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

### Question 8: Public Threat Intelligence Contribution

**Q3.2:** Do you publish original threat research on AI software security vulnerabilities through blog posts, conference presentations, responsible disclosures, or contributions to MITRE ATLAS/OWASP ML Top 10?

**Evidence Required:**
- [ ] At least 2 public threat intelligence contributions per year
- [ ] Contributions include:
  - Blog posts on AI security tool bypass techniques
  - Conference presentations (DEF CON AI Village, Black Hat, etc.)
  - Responsible vulnerability disclosures to AI security vendors
  - Contributions to MITRE ATLAS, OWASP ML Top 10, or AI Incident Database
- [ ] Public evidence (published articles, conference proceedings, CVE assignments)
- [ ] Documented impact (vendor patches, industry awareness, community engagement)

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

### Question 9: Continuous Improvement and Threat Model Evolution

**Q3.3:** Do you maintain a continuous improvement program for AI software security threat models, incorporating lessons learned from adversarial testing, real-world incidents, and emerging research, with evidence of threat model evolution over time?

**Evidence Required:**
- [ ] Documented process for updating threat models based on:
  - Adversarial testing results (quarterly)
  - Real-world AI security incidents (internal or industry)
  - Emerging research (academic papers, vendor advisories)
  - Red team exercise findings
- [ ] Historical record showing threat model evolution (12+ months)
- [ ] Examples of threat model updates triggering new mitigations
- [ ] Feedback loop: Threat intelligence → Testing → Model update → Mitigation → Re-test
- [ ] Metrics tracked: # of new threats identified, % of threats mitigated, evasion rate trend

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

**TA-Software Practice Score:** _______ / 3.0

### Precise Scoring (For Formal Audits)

```
L1_score = (L1 "Yes" answers) / 3
L2_score = (L2 "Yes" answers) / 3 × L1_score
L3_score = (L3 "Yes" answers) / 3 × L2_score

Practice Score = L1_score + L2_score + L3_score
```

**TA-Software Practice Score (Precise):** _______ / 3.0

---

## Assessment Summary

**Assessment Date:** _________________________________

**Assessor(s):** _____________________________________

**HAI System(s) Assessed:** __________________________

**Overall Maturity Level:**
- ☐ Level 0 (Score < 1.0): Ad-hoc, no formal threat assessment
- ☐ Level 1 (Score 1.0 - 1.9): Foundational threat awareness and documentation
- ☐ Level 2 (Score 2.0 - 2.9): Comprehensive risk prioritization and validation
- ☐ Level 3 (Score 3.0): Industry-leading adversarial testing and contribution

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

## Threat Assessment Specific Notes

**AI-Specific Threat Categories Covered:**
- [ ] Adversarial manipulation (prompt injection, security gate bypass, model evasion)
- [ ] Data poisoning and training corruption
- [ ] Operational security failures (false negatives/positives, model drift)
- [ ] Supply chain and infrastructure threats
- [ ] AI-generated code risks (Copilot, ChatGPT vulnerabilities)

**Prompt Injection Attack Coverage** (if LLM-based tools):
- [ ] Attack intents documented (jailbreak, data exfiltration, system prompt leak)
- [ ] Attack techniques documented (role-playing, cognitive overload, nested injection)
- [ ] Attack evasions documented (encoding, obfuscation, character manipulation)

**Adversarial Testing Coverage:**
- [ ] Evasion testing (obfuscation techniques against AI SAST/DAST)
- [ ] Prompt injection testing (manipulation of AI code reviewers)
- [ ] False positive resilience testing (alert fatigue scenarios)
- [ ] Model drift detection (accuracy degradation over time)

---

**Document Version:** 2.0
**Last Updated:** 2025-12-29
**Next Review:** Quarterly or after significant HAI system changes
