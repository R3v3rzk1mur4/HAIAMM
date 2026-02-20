# Threat Assessment (TA) - Processes Domain
## HAIAMM Assessment Questionnaire v3.0

**Practice:** Threat Assessment (TA)
**Domain:** Processes
**Purpose:** Assess organizational maturity in identifying and analyzing threats specific to Human Assisted Intelligence in security process automation
**Version:** v3.0
**Scoring Model:** Evidence + Outcome Metrics (see Scoring Methodology below)

---

## Instructions

- Answer each question honestly based on **current, implemented practices** (not plans or aspirations)
- **"Yes" requires evidence** - Document proof for each affirmative answer
- **Answer progressively** - Complete all Level 1 questions before Level 2
- **Level progression** - Achieve ALL questions at lower level before advancing
- Each question has two components: **Evidence** (what you did) and **Outcome Metrics** (how well it worked)
- **Scoring uses 4 tiers:** Fully Mature (1.0), Implemented (0.67), Partial (0.33), Not Implemented (0.0)
- **Baseline first** - Record current metric values before setting targets

---

## Level 1: Foundational
**Objective:** Establish baseline threat awareness for HAI security process automation

### Question 1: AI-Specific Threat Scenario Identification

**Q1.1:** Have you documented threat scenarios specific to Human Assisted Intelligence systems performing security process automation (e.g., SOAR, incident triage, vulnerability management, compliance reporting), including adversarial manipulation, data poisoning, operational failures, and prompt injection attacks?

**Evidence Required:**
- [ ] Inventory of HAI systems performing security process automation functions
- [ ] Documented threat scenarios covering at least 4 categories:
  - Adversarial manipulation (prompt injection in incident tickets, alert correlation evasion, triage manipulation)
  - Data poisoning (incident triage model poisoning, vulnerability prioritization corruption, compliance baseline poisoning)
  - Operational failures (false negatives missing critical incidents, false positives causing alert fatigue, model drift, catastrophic automation errors)
  - Supply chain threats (compromised SOAR platforms, malicious workflow updates, model tampering)
- [ ] Threat scenarios based on Arcanum PI Taxonomy for prompt injection (if LLM-based process automation)
- [ ] Document updated within last 12 months

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| % of AI security process agents with documented threat scenarios | ___ | ___ | ≥90% | ☐ | |
| Number of distinct threat scenario categories documented | ___ | ___ | ≥4 categories | ☐ | |
| % of SOAR/process automation workflows mapped to at least 1 threat scenario | ___ | ___ | 100% | ☐ | |
| Days since threat scenario document was last reviewed/updated | ___ | ___ | ≤365 days | ☐ | |

**Metric Collection Guidance:**
- **% of AI security process agents with documented threat scenarios**: Divide number of AI process agents with documented scenarios by total AI process agents in inventory; collect from threat model register and AI inventory spreadsheet
- **Number of distinct threat scenario categories documented**: Count unique threat categories in the documented threat scenario library; review threat model document and count top-level category headings
- **% of SOAR workflows mapped to at least 1 threat scenario**: Divide number of SOAR playbooks/workflows with at least one linked threat scenario by total active playbooks; pull from SOAR platform workflow list and cross-reference threat model
- **Days since last review**: Calculate days from most recent approved revision date on threat scenario document to today; check document version history or change log

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### Question 2: Threat Model Documentation and Ownership

**Q1.2:** Do you have documented threat models for your HAI security process automation operations, with identified threat owners responsible for tracking and mitigating each threat category?

**Evidence Required:**
- [ ] Formal threat model document for AI security process automation
- [ ] Threat model covers: attack vectors, failure modes, adversarial risks, operational dependencies
- [ ] Each threat category has assigned owner (individual or team)
- [ ] Threat model includes impact assessment (consequences of triage failures, missed incidents, compliance errors)
- [ ] Threat model reviewed and approved by security leadership and compliance teams
- [ ] Threat model accessible to relevant teams (SOC, incident response, vulnerability management, compliance)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| % of threat categories with a named, active owner | ___ | ___ | 100% | ☐ | |
| Number of distinct threat model sections reviewed and signed off by security leadership | ___ | ___ | ≥3 sections (attack vectors, failure modes, adversarial risks) | ☐ | |
| % of relevant stakeholder teams (SOC, IR, vuln mgmt, compliance) with confirmed access to threat model | ___ | ___ | 100% | ☐ | |
| Days since last formal threat model review or approval | ___ | ___ | ≤180 days | ☐ | |

**Metric Collection Guidance:**
- **% of threat categories with a named owner**: Extract threat category list from threat model; verify each has an owner entry that maps to a current employee or team; divide owned categories by total categories
- **Number of signed-off sections**: Check threat model document for approval signatures, dated sign-off entries, or formal review records in document management system
- **% of stakeholder teams with confirmed access**: Survey team leads or check access control list for the threat model document/wiki page; divide teams with confirmed access by total required stakeholder teams
- **Days since last formal review**: Subtract approval date from today; source from document metadata, version control log, or governance meeting minutes

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### Question 3: Threat Awareness Training

**Q1.3:** Have you conducted threat awareness training for SOC analysts, incident responders, vulnerability management teams, compliance analysts, and security leadership on AI-specific threats to security process automation within the last 90 days of AI tool deployment?

**Evidence Required:**
- [ ] Training materials covering AI security process automation threats
- [ ] Training delivered to at least 3 stakeholder groups:
  - SOC analysts & incident responders (AI triage manipulation, escalation procedures, manual failover skills)
  - Vulnerability management teams (AI prioritization corruption, manual assessment skills)
  - Compliance & GRC teams (AI compliance report limitations, auditability requirements)
- [ ] Training includes real-world examples (prompt injection in tickets, triage failures, compliance automation errors)
- [ ] Training conducted within 90 days of AI process automation deployment
- [ ] Attendance records and training completion tracking

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| % of required stakeholder groups that completed threat awareness training | ___ | ___ | ≥100% of 3 required groups | ☐ | |
| % of individual trainees within required groups who completed training | ___ | ___ | ≥80% | ☐ | |
| Days between AI process automation deployment and first training delivery | ___ | ___ | ≤90 days | ☐ | |
| % of trainees who passed post-training knowledge check (score ≥70%) | ___ | ___ | ≥75% | ☐ | |

**Metric Collection Guidance:**
- **% of stakeholder groups trained**: Divide number of stakeholder groups with completed training sessions by total required groups (SOC/IR, vuln mgmt, compliance/GRC); verify using training attendance records
- **% of individuals trained**: Divide number of individuals who completed training with attendance confirmation by total headcount in required stakeholder groups; source from LMS or attendance sign-in sheets
- **Days to first delivery**: Calculate difference between AI tool go-live date (from project records) and date of first training session (from training records)
- **% passing knowledge check**: Divide number of participants scoring ≥70% on post-training quiz by total participants; extract from LMS quiz results or paper-based assessment records

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

**Level 1 Score:** _____ / 3 questions answered "Implemented" or better

**Level 1 Achieved:** ☐ Yes (3/3 at Implemented or Fully Mature) ☐ No

---

## Level 2: Comprehensive
**Objective:** Quantify and prioritize AI security process threats by business impact and likelihood

**Prerequisites:** ALL Level 1 questions must be "Implemented" or "Fully Mature" to proceed to Level 2

### Question 4: Abuse Cases and Attack Trees

**Q2.1:** Have you developed detailed abuse cases and attack trees for each HAI agent performing security process automation, showing how adversaries could exploit or degrade HAI process operations?

**Evidence Required:**
- [ ] At least 3-5 abuse cases documented per AI security process agent
- [ ] Abuse cases include:
  - Attacker goal, attack path (step-by-step), prerequisites, impact, likelihood
- [ ] Attack trees showing multiple paths to process failure (e.g., "Delay incident response" with branches)
- [ ] Specific examples documented:
  - Prompt injection to downgrade critical incidents (triage manipulation)
  - Alert correlation evasion through attack fragmentation
  - Vulnerability prioritization model poisoning
  - AI compliance report errors submitted to auditors
  - Operational dependency failure during security crisis
- [ ] Abuse cases validated by security team and shared with SOC/compliance stakeholders

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Average number of documented abuse cases per AI security process agent | ___ | ___ | ≥3 abuse cases per agent | ☐ | |
| % of abuse cases that include a quantified business impact (e.g., hours of response delay, dollar cost, audit penalty) | ___ | ___ | ≥80% | ☐ | |
| % of abuse cases that have been reviewed and acknowledged by the relevant process owner (SOC lead, compliance lead, etc.) | ___ | ___ | 100% | ☐ | |
| % of high-likelihood abuse cases (rated Medium or High likelihood) that have at least one documented mitigation | ___ | ___ | ≥85% | ☐ | |

**Metric Collection Guidance:**
- **Average abuse cases per agent**: Count total documented abuse cases across all AI process agents; divide by number of agents; source from abuse case register or threat model appendix
- **% with quantified business impact**: Review each abuse case for a specific impact statement with a measurable value (hours, dollars, regulatory penalty); divide qualifying cases by total cases
- **% reviewed by process owners**: Check abuse case documents for sign-off, email acknowledgment, or meeting minutes confirming process owner review; divide confirmed reviews by total abuse cases
- **% of high-likelihood cases with mitigations**: Filter abuse cases rated Medium or High likelihood; check each for at least one linked mitigation control or SOC procedure; divide cases with mitigations by total high-likelihood cases

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### Question 5: Risk Prioritization Matrix

**Q2.2:** Have you assessed and prioritized AI security process automation threats using a risk matrix (likelihood × impact), with documented mitigation strategies for high-priority threats and differentiation by process criticality?

**Evidence Required:**
- [ ] Risk assessment framework with likelihood and impact criteria
- [ ] Each threat scenario assessed for:
  - Likelihood (High/Medium/Low based on technical feasibility, public research availability)
  - Business impact differentiated by process criticality:
    - Critical processes (incident response, vulnerability management, compliance reporting)
    - High processes (security metrics, change management, risk assessment)
    - Medium/low processes (training delivery, routine reporting)
- [ ] Risk matrix created (e.g., 3×3 or 5×5 grid)
- [ ] High-priority threats identified (High likelihood + Critical/High impact)
- [ ] Mitigation strategies documented for top 5-10 threats (input sanitization, human validation, failover procedures)
- [ ] Risk assessment reviewed quarterly and updated based on operational failures, threat intelligence

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| % of documented threat scenarios with a completed likelihood × impact risk score | ___ | ___ | 100% | ☐ | |
| % of High-priority threats (High/Critical risk score) with at least one implemented mitigation control | ___ | ___ | ≥85% | ☐ | |
| Number of distinct process criticality tiers represented in the risk matrix (Critical/High/Medium-Low) | ___ | ___ | ≥3 tiers | ☐ | |
| Number of quarters since last risk matrix review and update | ___ | ___ | ≤1 quarter (≤90 days) | ☐ | |

**Metric Collection Guidance:**
- **% of threats with completed risk scores**: Count threat scenarios in risk register with both likelihood and impact fields populated; divide by total threat scenarios; source from risk matrix spreadsheet or GRC tool
- **% of high-priority threats with implemented mitigations**: Filter risk matrix for High/Critical scored threats; verify each has a mitigation in "Implemented" status (not just "Planned"); divide by total high-priority threats
- **Number of process criticality tiers**: Review risk matrix for distinct impact tiers differentiated by process type; count distinct tiers present (Critical process, High process, Medium/Low process)
- **Quarters since last review**: Calculate days since last dated review entry in risk matrix; divide by 90; source from document revision history or quarterly governance meeting minutes

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### Question 6: Threat Intelligence Integration and Validation

**Q2.3:** Have you integrated threat intelligence from security operations research, SOAR vendor advisories, incident response lessons learned, and automation failure reports to continuously identify emerging threats to AI security process automation, with annual validation of threat models?

**Evidence Required:**
- [ ] Threat intelligence sources identified and monitored:
  - Security operations research (SANS Institute, operational resilience studies)
  - SOAR vendor advisories (Splunk, Palo Alto, IBM, Microsoft security bulletins)
  - Real-world operational intelligence (post-mortems of AI triage failures, compliance automation errors)
  - Attack technique intelligence (MITRE ATT&CK, prompt injection research)
- [ ] Monitoring cadence established:
  - Weekly: SOAR vendor advisories, critical operational failures
  - Monthly: Security operations research, automation lessons learned
  - Quarterly: Threat model updates
- [ ] Threat intelligence findings documented in structured format
- [ ] Annual comprehensive threat model validation completed

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Number of active threat intelligence sources monitored on at least a weekly cadence | ___ | ___ | ≥4 sources | ☐ | |
| Number of threat intelligence findings formally logged in the past 12 months | ___ | ___ | ≥12 findings (1 per month minimum) | ☐ | |
| % of logged threat intelligence findings that triggered a threat model update or control review | ___ | ___ | ≥40% | ☐ | |
| Months since last annual comprehensive threat model validation | ___ | ___ | ≤12 months | ☐ | |

**Metric Collection Guidance:**
- **Number of active intel sources monitored weekly**: Count distinct sources in the threat intelligence monitoring register with a confirmed weekly review cadence; verify with calendar entries, feed subscription records, or analyst workflow documentation
- **Number of findings logged in past 12 months**: Count entries in threat intelligence log or backlog dated within the last 12 months; source from threat intelligence tracking spreadsheet, JIRA backlog, or wiki
- **% of findings triggering updates**: Filter logged findings; count those with a linked threat model change ticket or control review action; divide by total findings; source from change log cross-referenced with threat intel log
- **Months since annual validation**: Subtract date of last completed annual threat model validation report from today; source from validation report document or governance calendar

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

**Level 2 Score:** _____ / 3 questions answered "Implemented" or better

**Level 2 Achieved:** ☐ Yes (3/3 at Implemented or Fully Mature) ☐ No

---

## Level 3: Industry-Leading
**Objective:** Proactively test and share threat intelligence through adversarial testing and industry contribution

**Prerequisites:** ALL Level 2 questions must be "Implemented" or "Fully Mature" to proceed to Level 3

### Question 7: Adversarial Testing and Operational Resilience Exercises

**Q3.1:** Do you conduct periodic (at least quarterly) adversarial testing and operational resilience exercises against your HAI security process automation to proactively identify weaknesses before attackers or crises expose them?

**Evidence Required:**
- [ ] Quarterly testing program established covering:
  - AI incident triage accuracy testing (100-200 test incidents, >90% accuracy target)
  - Prompt injection & manipulation testing (resistance to triage downgrade, incident closure attempts)
  - Model drift monitoring (monthly testing against golden incident dataset)
- [ ] Semi-annual operational failover exercises:
  - Simulated AI SOAR platform outage
  - SOC performs manual incident triage, vulnerability prioritization
  - Performance measured: >70% operational capacity maintained manually
- [ ] Annual security process red team exercise:
  - Red team attempts to exploit AI automation (triage manipulation, alert evasion, prioritization corruption)
  - 2-4 week duration with documented findings
- [ ] Test reports documenting:
  - Successful manipulation techniques
  - AI process automation vulnerabilities
  - Manual failover capabilities and gaps
  - Skills retention assessment
  - Recommendations for improvement

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| AI incident triage accuracy rate on quarterly test dataset (100-200 test incidents) | ___ | ___ | ≥90% accuracy | ☐ | |
| % of prompt injection attempts successfully resisted by AI process automation (quarterly manipulation testing) | ___ | ___ | ≥95% resistance rate | ☐ | |
| SOC manual operational capacity maintained during simulated SOAR outage (semi-annual failover exercise) | ___ | ___ | ≥70% of normal capacity | ☐ | |
| % of red team process manipulation scenarios that successfully bypassed AI automation defenses (annual exercise) | ___ | ___ | ≤20% success rate for red team | ☐ | |

**Metric Collection Guidance:**
- **AI triage accuracy rate**: Divide number of test incidents correctly triaged by AI (matching expert ground-truth severity) by total test incidents; formula: (correct triage / total incidents) × 100; source from quarterly triage accuracy test report
- **Prompt injection resistance rate**: Divide number of injection attempts where AI maintained correct behavior by total injection attempts; formula: (resisted attempts / total attempts) × 100; source from quarterly manipulation testing report
- **SOC manual capacity during failover**: Measure number of incidents triaged per hour manually during exercise divided by normal AI-assisted rate; express as percentage; source from operational failover exercise report
- **Red team success rate**: Divide number of red team attack scenarios that successfully manipulated AI process automation by total scenarios attempted; formula: (successful manipulations / total scenarios) × 100; source from annual red team report; lower is better

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### Question 8: Public Threat Intelligence Contribution

**Q3.2:** Do you publish original threat research on AI security process automation vulnerabilities through blog posts, conference presentations, responsible disclosures to SOAR vendors, or contributions to security operations community knowledge?

**Evidence Required:**
- [ ] At least 2 public threat intelligence contributions per year
- [ ] Contributions include:
  - Blog posts on AI process automation challenges, triage failures, lessons learned
  - Conference presentations (SANS Summits, RSA, security operations forums)
  - Responsible vulnerability disclosures to SOAR/AI automation vendors
  - Case studies shared with peer organizations on operational failures, manual failover experiences
  - Contributions to security operations best practices, SOC manager communities
- [ ] Public evidence (published articles, conference proceedings, vendor acknowledgments)
- [ ] Documented impact (vendor improvements, industry awareness, community engagement)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Number of public threat intelligence contributions published in the past 12 months | ___ | ___ | ≥2 per year | ☐ | |
| Number of responsible vulnerability disclosures submitted to SOAR/AI automation vendors in the past 12 months | ___ | ___ | ≥1 per year | ☐ | |
| Number of documented vendor improvements or community actions attributable to your contributions | ___ | ___ | ≥1 documented impact | ☐ | |
| Year-over-year change in public contributions (trend) | ___ | ___ | Stable or increasing (≥0% YoY change) | ☐ | |

**Metric Collection Guidance:**
- **Number of public contributions**: Count published blog posts, conference talks, white papers, and community forum contributions with public URLs or proceedings citations; maintain a contributions log with publication date and link
- **Number of responsible disclosures**: Count formal disclosure submissions to vendor security teams or bug bounty programs; source from disclosure tracking log with submission dates and vendor acknowledgments
- **Documented vendor/community impacts**: Count vendor patch notes, CVE assignments, community forum responses, or industry citations that reference your research; source from vendor acknowledgment emails, CVE records, or publication analytics
- **Year-over-year trend**: Compare total contributions in current 12-month period to prior 12-month period; formula: ((current year count - prior year count) / prior year count) × 100; source from contributions log

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### Question 9: Continuous Improvement and Threat Model Evolution

**Q3.3:** Do you maintain a continuous improvement program for AI security process automation threat models, incorporating lessons learned from adversarial testing, real-world operational failures, and emerging research, with evidence of threat model evolution over time?

**Evidence Required:**
- [ ] Documented process for updating threat models based on:
  - Adversarial testing results (quarterly triage accuracy, manipulation testing, failover exercises)
  - Real-world operational failures (AI triage errors causing delayed response, compliance report mistakes, automation outages)
  - Emerging research (security operations studies, prompt injection techniques, SOAR vulnerabilities)
  - Industry intelligence (peer organization lessons learned, vendor advisories)
- [ ] Historical record showing threat model evolution (12+ months)
- [ ] Examples of threat model updates triggering process changes:
  - Enhanced input sanitization after manipulation testing
  - Human validation requirements for critical decisions
  - Improved failover procedures after resilience exercises
  - Skills maintenance programs addressing capability gaps
- [ ] Feedback loop: Threat intelligence → Testing → Model update → Mitigation → Re-test
- [ ] Metrics tracked: # of new threats identified, % of threats mitigated, triage accuracy trends, manual capability retention

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| % of threat model content (sections, threat entries) updated in the past 12 months based on testing or operational data | ___ | ___ | ≥20% updated annually | ☐ | |
| Number of process or control changes directly triggered by threat model updates in the past 12 months | ___ | ___ | ≥3 process changes per year | ☐ | |
| Quarter-over-quarter trend in AI triage accuracy on golden dataset (trailing 4 quarters) | ___ | ___ | Stable or improving (≤5% degradation per quarter) | ☐ | |
| % of identified threats in the model that have moved from "Open" to "Mitigated" status over the past 12 months | ___ | ___ | ≥50% of open threats mitigated within 12 months | ☐ | |

**Metric Collection Guidance:**
- **% of threat model content updated**: Compare current threat model to version from 12 months prior using document diff or version control history; count sections or threat entries with substantive changes; divide by total sections/entries; source from document version control (Git, SharePoint, Confluence history)
- **Number of process changes triggered by threat model updates**: Count action items in threat model update meeting minutes or change log that resulted in a deployed control, procedure update, or training change; source from change management records cross-referenced with threat model update dates
- **Quarter-over-quarter triage accuracy trend**: Plot AI triage accuracy rate from quarterly test reports over trailing 4 quarters; calculate average quarter-over-quarter change; source from quarterly triage accuracy test reports
- **% of threats mitigated**: Filter threat model for entries marked "Open" 12 months ago; count those now marked "Mitigated" or "Closed"; divide by original open count; source from threat model status tracking log or GRC tool

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

**Level 3 Score:** _____ / 3 questions answered "Implemented" or better

**Level 3 Achieved:** ☐ Yes (3/3 at Implemented or Fully Mature) ☐ No

---

## Assessment Summary

**Assessment Date:** _________________________________

**Assessor(s):** _____________________________________

**HAI System(s) Assessed:** __________________________

**Overall Maturity Level:**
- ☐ Level 0 (Score < 0.5): Ad-hoc, no formal threat assessment
- ☐ Level 1 (Score 0.5 - 1.49): Foundational threat awareness and documentation
- ☐ Level 2 (Score 1.5 - 2.49): Comprehensive risk prioritization and validation
- ☐ Level 3 (Score 2.5 - 3.0): Industry-leading adversarial testing and contribution

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
- [ ] Adversarial manipulation (prompt injection in tickets, alert evasion, workflow bypass)
- [ ] Data poisoning (triage model corruption, prioritization manipulation, compliance baseline poisoning)
- [ ] Operational process failures (false negatives missing critical incidents, false positives causing alert fatigue, model drift, catastrophic automation errors)
- [ ] Supply chain and SOAR platform threats (compromised automation platforms, malicious workflow updates)
- [ ] Auditability and compliance risks (unexplainable AI decisions, insufficient audit trails, AI-generated report errors)
- [ ] Human skill atrophy and operational dependency (loss of manual capabilities, over-reliance on AI, single point of failure)

**Prompt Injection Attack Coverage** (if LLM-based SOAR/process automation):
- [ ] Attack intents documented (system prompt leak, jailbreak workflow automation, incident manipulation, compliance falsification)
- [ ] Attack techniques documented (ticket field injection, alert metadata manipulation, playbook parameter injection, role-playing)
- [ ] Attack evasions documented (encoding in tickets, format-based injection, language evasion, character manipulation)

**Adversarial Testing Coverage:**
- [ ] Triage accuracy testing (quarterly validation against test incident dataset, >90% accuracy target)
- [ ] Prompt injection testing (manipulation resistance for incident downgrade, workflow bypass attempts)
- [ ] Operational failover exercises (manual process capability validation, skills retention assessment)
- [ ] Model drift detection (monthly testing, automated alerting on accuracy degradation >10%)
- [ ] Red team exercises (full adversarial simulation against AI process automation, 2-4 week duration)

**Process Criticality Differentiation:**
- [ ] Critical processes identified (incident response, vulnerability remediation, compliance reporting)
- [ ] High processes identified (security metrics, change management, risk assessment)
- [ ] Medium/low processes identified (training delivery, routine reporting)
- [ ] Risk assessment differentiated by process tier (same threat has different impact based on process criticality)
- [ ] Mitigation strategies prioritized for critical process failures (immediate priority for incident triage/compliance automation)

**Operational Resilience Considerations:**
- [ ] Manual failover procedures documented (backup processes when AI automation fails)
- [ ] Skills maintenance program (regular manual investigation exercises, competency testing)
- [ ] Automation dependency limits defined (maximum % automation per process, critical processes retain human oversight)
- [ ] Human validation requirements (which AI decisions require human approval before execution)
- [ ] Escalation procedures (when AI actions disrupt business, override process, accountability framework)

---

## Updated Scoring Methodology

### Question-Level Scoring

Each question receives a score based on evidence + outcome metrics:

| Answer Category | Score | Criteria |
|----------------|-------|----------|
| **Fully Mature** | 1.0 | Evidence complete + ≥75% of metrics meet targets (≥3 of 4 metrics) |
| **Implemented** | 0.67 | Evidence complete + 50-74% of metrics meet targets (2 of 4 metrics) |
| **Partial** | 0.33 | Evidence complete + <50% metrics meet targets OR incomplete evidence |
| **Not Implemented** | 0.0 | No evidence |

### Level Scoring

Level Score = Sum of question scores in that level / Number of questions

```
L1_score = (Q1.1_score + Q1.2_score + Q1.3_score) / 3
L2_score = (Q2.1_score + Q2.2_score + Q2.3_score) / 3 × (L1_score if L1_score ≥ 1.0, else 0)
L3_score = (Q3.1_score + Q3.2_score + Q3.3_score) / 3 × (L2_score if L2_score ≥ 1.0, else 0)
```

### Practice Score

Practice Score = L1_score + L2_score + L3_score (Maximum = 3.0)

### Maturity Interpretation

| Score Range | Maturity Level | Interpretation |
|-------------|---------------|----------------|
| 2.5 - 3.0 | Level 3: Industry-Leading | Comprehensive evidence + strong outcome metrics |
| 1.5 - 2.49 | Level 2: Comprehensive | Strong evidence + metrics at L1-L2 |
| 0.5 - 1.49 | Level 1: Foundational | Basic evidence + some outcome metrics at L1 |
| < 0.5 | Level 0: Ad-hoc | Minimal evidence or metrics |

---

**Document Version:** 3.0
**Last Updated:** 2026-02-18
**Next Review:** Quarterly or after significant HAI process automation changes
