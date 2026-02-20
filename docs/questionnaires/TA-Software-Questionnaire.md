# Threat Assessment (TA) - Software Domain
## HAIAMM Assessment Questionnaire v3.0

**Practice:** Threat Assessment (TA)
**Domain:** Software
**Purpose:** Assess organizational maturity in identifying and analyzing threats specific to Human Assisted Intelligence in software security operations

**Scoring Model:** Evidence + Outcome Metrics (see Scoring Methodology below)

---

## Instructions

- Answer each question honestly based on **current, implemented practices** (not plans or aspirations)
- Each question has two components: **Evidence** (what you did) and **Outcome Metrics** (how well it worked)
- **Scoring uses 4 tiers:** Fully Mature (1.0), Implemented (0.67), Partial (0.33), Not Implemented (0.0)
- **Answer progressively** - Complete all Level 1 questions before Level 2
- **Level progression** - Achieve ALL questions at lower level before advancing
- **Baseline first** - Record current metric values before setting targets

---

## Level 1: Foundational
**Objective:** Establish baseline threat awareness for HAI software security

### **Question 1: AI-Specific Threat Scenario Identification**

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

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| # of documented AI-specific threat scenarios | ___ | ___ | ≥12 (3 per category) | ☐ | |
| % of AI security incidents traceable to documented threats | ___ | ___ | ≥80% | ☐ | |
| Mean time from threat discovery to documentation | ___ | ___ | ≤14 days | ☐ | |
| % of engineering teams aware of top 5 AI threats | ___ | ___ | ≥90% | ☐ | |

**Metric Collection Guidance:**
- **# of documented threats**: Count unique threat scenarios in threat model document (must have description, attack vector, impact)
- **% incidents traceable**: Review last 12 months of AI security incidents; calculate (incidents matching documented threats / total incidents) × 100
- **Mean time to documentation**: Average days from when threat is first identified (meeting notes, Slack, ticket) to formal documentation
- **% teams aware**: Survey or quiz results from engineering teams on top 5 threat scenarios

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

##### **Question 2: Threat Model Documentation and Ownership**

**Q1.2:** Do you have documented threat models for your HAI software security operations, with identified threat owners responsible for tracking and mitigating each threat category?

**Evidence Required:**
- [ ] Formal threat model document for AI software security operations
- [ ] Threat model covers: attack vectors, failure modes, adversarial risks
- [ ] Each threat category has assigned owner (individual or team)
- [ ] Threat model includes impact assessment (what happens if threat materializes)
- [ ] Threat model reviewed and approved by security leadership
- [ ] Threat model accessible to relevant teams (security, engineering, AI/ML)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| % of documented threats with assigned owners | ___ | ___ | 100% | ☐ | |
| % of threat owners who can articulate mitigation strategy | ___ | ___ | ≥85% | ☐ | |
| Threat model review frequency | ___ per year | ___ per year | ≥4 per year (quarterly) | ☐ | |
| % of high-priority threats with active mitigation in progress | ___ | ___ | 100% | ☐ | |

**Metric Collection Guidance:**
- **% threats with owners**: (Threats with named owners / Total documented threats) × 100 from threat model document
- **% owners articulate strategy**: Interview or survey threat owners; score based on ability to describe 1) threat vector, 2) impact, 3) current mitigation status
- **Review frequency**: Count threat model update commits/versions in last 12 months from version control or document history
- **% high-priority with active mitigation**: From threat model, count (High/Critical threats with "In Progress" or "Implemented" mitigation status / Total High/Critical threats) × 100

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

##### **Question 3: Threat Awareness Training**

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

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| % of target audience completing training | ___ | ___ | ≥95% | ☐ | |
| Mean training assessment score | ___ | ___ | ≥80% | ☐ | |
| % of AI security incidents caused by trained behaviors | ___ | ___ | ≤20% | ☐ | |
| Training refresh completion rate (annual) | ___ | ___ | ≥90% | ☐ | |

**Metric Collection Guidance:**
- **% completing training**: (Employees who completed training / Total target audience) × 100 from LMS or attendance tracking
- **Mean assessment score**: Average score from post-training quiz/assessment across all participants
- **% incidents caused by trained behaviors**: Review last 6 months of incidents; calculate (Incidents caused by behaviors covered in training / Total incidents) × 100 (lower is better)
- **Refresh completion**: For employees trained >12 months ago, (Completed refresh training / Total requiring refresh) × 100

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

## **Level 2: Comprehensive**

##### **Question 4: Abuse Cases and Attack Trees**

**Q2.1:** Have you developed detailed abuse cases and attack trees for each HAI agent performing software security, showing how adversaries could exploit or degrade HAI security operations?

**Evidence Required:**
- [ ] At least 3-5 abuse cases documented per AI security agent
- [ ] Abuse cases include: attacker goal, attack path (step-by-step), prerequisites, impact, likelihood
- [ ] Attack trees showing multiple paths to compromise (e.g., "Deploy vulnerable code" with branches)
- [ ] Specific examples documented:
  - Adversarial code evasion (obfuscation to bypass AI SAST)
  - Prompt injection via code comments (manipulate AI code reviewer)
  - False positive flooding to create alert fatigue
- [ ] Abuse cases validated by security team and shared with stakeholders

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| # of documented abuse cases per AI agent | ___ | ___ | ≥5 per agent | ☐ | |
| % of abuse cases with tested mitigations | ___ | ___ | ≥80% | ☐ | |
| % of real-world attack attempts matching documented abuse cases | ___ | ___ | ≥70% | ☐ | |
| Mean time to create mitigation for new abuse case | ___ | ___ | ≤30 days | ☐ | |

**Metric Collection Guidance:**
- **# abuse cases per agent**: Count documented abuse cases in threat model per AI system (must have all required elements: goal, path, prerequisites, impact, likelihood)
- **% with tested mitigations**: (Abuse cases with executed tests validating mitigation / Total abuse cases) × 100 from test results or security review records
- **% real attacks matching cases**: Review security logs/incidents for last 6 months; calculate (Attack attempts matching documented abuse cases / Total attack attempts) × 100
- **Mean time to mitigation**: Average days from abuse case documentation date to mitigation deployment for last 5 new abuse cases

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

##### **Question 5: Risk Prioritization Matrix**

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

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| % of documented threats with risk scores | ___ | ___ | 100% | ☐ | |
| % of high/critical threats with active mitigations | ___ | ___ | 100% | ☐ | |
| Mean time to mitigate high-priority threats | ___ | ___ | ≤60 days | ☐ | |
| # of unaddressed critical threats | ___ | ___ | 0 | ☐ | |

**Metric Collection Guidance:**
- **% with risk scores**: (Threats with both likelihood and impact scores / Total documented threats) × 100 from threat model
- **% high/critical with mitigations**: (High/Critical threats with "Implemented" or "In Progress" mitigation / Total High/Critical threats) × 100
- **Mean time to mitigate**: Average days from high-priority threat identification to mitigation deployment for last 5 threats
- **# unaddressed critical**: Count of threats scored "Critical" (highest likelihood × highest impact) with no mitigation plan or owner assigned

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

##### **Question 6: Threat Intelligence Integration and Validation**

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

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| # of threat intelligence sources monitored | ___ | ___ | ≥4 sources | ☐ | |
| # of new threats identified from intelligence (per year) | ___ | ___ | ≥8 per year | ☐ | |
| Mean time from threat intelligence discovery to threat model update | ___ | ___ | ≤30 days | ☐ | |
| % of intelligence findings actioned (investigated/mitigated) | ___ | ___ | ≥75% | ☐ | |

**Metric Collection Guidance:**
- **# sources monitored**: Count unique threat intelligence sources with documented monitoring process (must have owner and cadence)
- **# new threats identified**: Count threats added to threat model in last 12 months attributed to external intelligence sources (not internal discovery)
- **Mean time to update**: Average days from threat intelligence publication date to threat model document update for last 10 intelligence-driven updates
- **% findings actioned**: (Intelligence findings resulting in investigation, testing, or mitigation / Total intelligence findings) × 100 from intelligence tracking system

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

## **Level 3: Industry-Leading**

##### **Question 7: Adversarial Testing and Red Team Exercises**

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

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| AI evasion success rate (adversarial samples) | ___% | ___% | ≤5% | ☐ | |
| Prompt injection defense effectiveness (% blocked) | ___% | ___% | ≥95% | ☐ | |
| # of adversarial test cycles completed (per year) | ___ | ___ | ≥4 per year | ☐ | |
| Mean time to remediate discovered evasion technique | ___ | ___ | ≤45 days | ☐ | |

**Metric Collection Guidance:**
- **Evasion success rate**: (Adversarial samples that bypassed AI detection / Total adversarial samples tested) × 100 from quarterly test reports (lower is better)
- **Prompt injection effectiveness**: (Prompt injection attacks blocked / Total prompt injection attacks tested) × 100 from semi-annual test reports
- **# test cycles**: Count completed adversarial testing cycles in last 12 months (must have test report and results)
- **Mean time to remediate**: Average days from evasion discovery in test to deployed mitigation (model update, rule enhancement, or code change) for last 5 findings

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

##### **Question 8: Public Threat Intelligence Contribution**

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

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| # of public threat intelligence contributions (per year) | ___ | ___ | ≥2 per year | ☐ | |
| # of disclosed vulnerabilities resulting in vendor patches | ___ | ___ | ≥1 per year | ☐ | |
| Community reach (blog views, conference attendees, citations) | ___ | ___ | ≥1,000 per contribution | ☐ | |
| % of contributions acknowledged by industry (vendor response, citations) | ___% | ___% | ≥50% | ☐ | |

**Metric Collection Guidance:**
- **# contributions**: Count published blog posts, conference talks, disclosed CVEs, and framework contributions in last 12 months (must be publicly verifiable)
- **# resulting in patches**: Count disclosed vulnerabilities that resulted in official vendor security updates or CVE assignments
- **Community reach**: Sum of blog post views + conference attendees + academic citations + social media reach for contributions in last 12 months
- **% acknowledged**: (Contributions receiving vendor response, official citation, or community recognition / Total contributions) × 100

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

##### **Question 9: Continuous Improvement and Threat Model Evolution**

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

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Threat model update frequency | ___ per year | ___ per year | ≥4 per year (quarterly) | ☐ | |
| # of threat model updates triggered by testing/incidents | ___ | ___ | ≥8 per year | ☐ | |
| % of identified threats with deployed mitigations | ___% | ___% | ≥90% | ☐ | |
| Evasion rate trend (year-over-year improvement) | ___% YoY change | ___% YoY change | ≥20% reduction YoY | ☐ | |

**Metric Collection Guidance:**
- **Update frequency**: Count threat model document updates in last 12 months from version control history (must have meaningful content changes, not just formatting)
- **# updates from testing/incidents**: Count threat model updates explicitly attributed to testing results or incident findings in update notes
- **% with mitigations**: (Documented threats with "Implemented" or "In Progress" mitigation status / Total documented threats) × 100
- **Evasion rate trend**: Compare current adversarial evasion rate to rate 12 months ago; calculate percentage reduction (e.g., 15% → 10% = 33% reduction)

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

## **Updated Scoring Methodology**

##### **Question-Level Scoring**

Each question receives a score based on evidence + outcome metrics:

| Answer Category | Score | Criteria |
|----------------|-------|----------|
| **Fully Mature** | 1.0 | Evidence complete + ≥75% of metrics meet targets (≥3 of 4 metrics) |
| **Implemented** | 0.67 | Evidence complete + 50-74% of metrics meet targets (2 of 4 metrics) |
| **Partial** | 0.33 | Evidence complete + <50% metrics meet targets OR incomplete evidence |
| **Not Implemented** | 0.0 | No evidence |

### **Level Scoring**

```
Level Score = Sum of question scores in that level / Number of questions

L1_score = (Q1.1_score + Q1.2_score + Q1.3_score) / 3
L2_score = (Q2.1_score + Q2.2_score + Q2.3_score) / 3 × (L1_score if L1_score ≥ 1.0, else 0)
L3_score = (Q3.1_score + Q3.2_score + Q3.3_score) / 3 × (L2_score if L2_score ≥ 1.0, else 0)
```

**Level progression rule:** Must achieve 100% "Yes" (score ≥1.0) at lower level before scoring next level.

### **Practice Score**

```
Practice Score = L1_score + L2_score + L3_score
Maximum = 3.0
```

### **Maturity Interpretation**

| Score Range | Maturity Level | Interpretation |
|-------------|---------------|----------------|
| 2.5 - 3.0 | **Level 3: Industry-Leading** | Comprehensive evidence + strong outcome metrics across all levels |
| 1.5 - 2.49 | **Level 2: Comprehensive** | Strong evidence + metrics at L1-L2, partial at L3 |
| 0.5 - 1.49 | **Level 1: Foundational** | Basic evidence + some outcome metrics at L1, weak L2-L3 |
| < 0.5 | **Level 0: Ad-hoc** | Minimal evidence or metrics |

### **Why This Methodology Works**

1. **Separates "doing" from "measuring"**: Evidence proves you did the activity; metrics prove it was effective
2. **Partial credit for effort**: Organizations get credit for implementing practices even if outcomes aren't perfect yet
3. **Incentivizes measurement**: The 0.67 score for "Implemented" encourages organizations to track metrics
4. **Progressive difficulty**: Level progression still requires strong foundational evidence
5. **Actionable feedback**: Scoring reveals whether gaps are in implementation or effectiveness
