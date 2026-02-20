# Threat Assessment (TA) - Vendors Domain
## HAIAMM Assessment Questionnaire v3.0

**Practice:** Threat Assessment (TA)
**Domain:** Vendors
**Purpose:** Assess organizational maturity in identifying and analyzing threats specific to Human Assisted Intelligence in vendor security and third-party risk management operations
**Scoring Model:** Evidence + Outcome Metrics

---

## Instructions

- Answer each question honestly based on **current, implemented practices** (not plans or aspirations)
- **Evidence + Metrics required** - Document proof AND collect metrics for each affirmative answer
- **Answer progressively** - Complete all Level 1 questions before Level 2
- **Level progression** - Achieve ALL questions at lower level before advancing
- **Partial implementation = "Partial" or lower** - Practice must be complete and systematic for full credit

---

## Level 1: Foundational
**Objective:** Establish baseline threat awareness for HAI vendor security and third-party risk management

### Question 1: AI-Specific Threat Scenario Identification

**Q1.1:** Have you documented threat scenarios specific to Human Assisted Intelligence systems performing vendor security and third-party risk management functions (e.g., vendor risk assessment, SCA/SBOM analysis, continuous vendor monitoring), including supply chain attacks, adversarial manipulation, data poisoning, operational failures, and regulatory risks?

**Evidence Required:**
- [ ] Inventory of HAI systems performing vendor security functions (vendor risk assessment, questionnaire analysis, continuous monitoring, SCA/SBOM analysis, supply chain threat detection)
- [ ] Documented threat scenarios covering at least 5 categories:
  - Supply chain attacks (malicious vendor approval, malicious dependency injection, compromised SBOM, vendor compromise for lateral attack, fourth-party supply chain attack)
  - Adversarial manipulation (prompt injection in questionnaires, vendor assessment gaming, fake security certifications, vendor security theater)
  - Data poisoning (vendor risk model poisoning, questionnaire answer poisoning, supply chain baseline poisoning, vendor breach data manipulation)
  - Operational failures (false negatives missing vendor breaches/supply chain attacks/catastrophic vendor approvals, false positives blocking legitimate vendors, model drift)
  - Regulatory & compliance risks (GDPR Article 28 violations, HIPAA BAA failures, PCI-DSS vendor management gaps, SOC 2 vendor control failures)
- [ ] Threat scenarios specific to vendor portfolio (SaaS vendors, cloud service providers, MSPs, software developers, payment processors, data processors)
- [ ] Document updated within last 12 months

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Number of documented vendor threat scenarios covering ≥5 categories | ___ | ___ | ≥15 scenarios | ☐ | |
| % of AI vendor security agents mapped to ≥3 specific threat scenarios | ___ | ___ | 100% | ☐ | |
| % of new critical/high vendor contracts including required security provisions (breach notification ≤24h, audit rights) | ___ | ___ | 100% | ☐ | |
| Days since vendor threat document last reviewed and updated | ___ | ___ | ≤365 days | ☐ | |

**Metric Collection Guidance:**
- **Number of scenarios**: Count distinct threat scenarios in vendor threat inventory; verify coverage spans all 5 required categories (supply chain, adversarial manipulation, data poisoning, operational failures, regulatory); source from threat inventory document
- **% agents mapped**: Divide number of AI vendor security agents with ≥3 linked threat scenarios by total AI vendor security agents; extract from threat model agent-to-scenario mapping table
- **% contracts with provisions**: Audit new vendor contracts executed in last 12 months; divide contracts containing breach notification SLA ≤24h and audit rights clauses by total new contracts; source from contract management system
- **Days since review**: Calculate from document last-modified or version control timestamp; alert if >180 days without update following a major vendor breach disclosure

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

**Q1.2:** Do you have documented threat models for your HAI vendor security and third-party risk management operations, with identified threat owners responsible for tracking and mitigating each threat category?

**Evidence Required:**
- [ ] Formal threat model document for AI vendor security operations
- [ ] Threat model covers: supply chain attack vectors, vendor compromise scenarios, fourth-party risks, adversarial assessment manipulation, regulatory compliance threats
- [ ] Each threat category has assigned owner (individual or team)
- [ ] Threat model includes impact assessment by vendor criticality tier (critical/cloud/payment vendors vs. high/business-critical vs. medium-low/support vendors)
- [ ] Threat model reviewed and approved by vendor risk management and security leadership
- [ ] Threat model accessible to relevant teams (vendor risk, procurement, supply chain security, legal counsel, security operations)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| % of vendor threat categories with named owner assigned | ___ | ___ | 100% | ☐ | |
| % of threats differentiated by vendor criticality tier (critical/high/medium-low) | ___ | ___ | 100% | ☐ | |
| Number of relevant teams (vendor risk, procurement, legal, SecOps) with confirmed threat model access | ___ | ___ | ≥4 teams | ☐ | |
| Days since vendor threat model reviewed and approved by vendor risk leadership | ___ | ___ | ≤90 days | ☐ | |

**Metric Collection Guidance:**
- **% with owner**: Count threat categories in vendor threat model; divide those with named owner (individual or team) by total categories; source from threat model ownership table
- **% tiered by vendor criticality**: Audit each threat in model for presence of impact differentiation across vendor tiers (critical cloud/payment vs. high business-critical vs. medium-low support); divide threats with tier differentiation by total threats
- **Teams with access**: Survey vendor risk, procurement, supply chain security, legal counsel, and SecOps teams; count teams confirming access to threat model in last 30 days; source from access log or survey
- **Days since review**: Extract from document approval metadata or review calendar; target ≤90 days given dynamic vendor threat landscape

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

**Q1.3:** Have you conducted threat awareness training for vendor risk analysts, procurement teams, supply chain security specialists, and executive leadership on AI-specific threats to vendor security operations within the last 90 days of AI tool deployment?

**Evidence Required:**
- [ ] Training materials covering AI vendor security threats
- [ ] Training delivered to at least 4 stakeholder groups:
  - Vendor Risk Analysts & Third-Party Risk Managers (how AI vendor assessment can be manipulated, supply chain attack awareness, regulatory vendor requirements, when to override AI approvals)
  - Procurement & Vendor Management Teams (security implications of vendor selection, AI vendor assessment limitations, contract security requirements)
  - Supply Chain & Software Development Teams (software supply chain attack vectors, how AI SCA can be evaded, SBOM security implications, secure dependency management)
  - Legal Counsel & Compliance (third-party risk regulatory requirements, vendor contract security provisions, vendor breach liability, subprocessor management)
- [ ] Training includes real-world examples (SolarWinds/Kaseya supply chain attacks, vendor breach case studies, dependency confusion attacks, vendor questionnaire gaming)
- [ ] Training conducted within 90 days of AI vendor security tool deployment
- [ ] Attendance records and training completion tracking

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| % of vendor risk, procurement, supply chain, and legal teams completing threat awareness training | ___ | ___ | ≥80% | ☐ | |
| % of trainees passing post-training assessment on vendor supply chain threat scenarios (≥80% score) | ___ | ___ | ≥85% | ☐ | |
| Number of high-risk vendor proposals rejected per quarter based on threat assessment findings | ___ | ___ | ≥5 per quarter | ☐ | |
| Days from AI vendor tool deployment to initial threat awareness training delivery | ___ | ___ | ≤90 days | ☐ | |

**Metric Collection Guidance:**
- **% training completion**: Divide staff completing training by total staff in target roles (vendor risk analysts, procurement, supply chain security, legal counsel); source from LMS attendance records
- **% passing assessment**: Post-training quiz minimum 10 questions covering supply chain attacks, questionnaire gaming, regulatory requirements; divide passing scores (≥80%) by total completions; source from LMS gradebook
- **High-risk vendors rejected**: Count vendor proposals where threat assessment findings (AI or human) were documented rationale for rejection; source from vendor risk management system decision log; note some organizations may legitimately have fewer proposals
- **Days to training delivery**: Calculate from AI vendor tool go-live to first training session; source from deployment log and training calendar

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________
**Metric Validation Date:** _________________________________
**Notes:** ___________________________________________

---

**Level 1 Score:** _____ / 3.0 (sum of question scores using 1.0/0.67/0.33/0.0)

**Level 1 Achieved (all Fully Mature):** ☐ Yes ☐ No

---

## Level 2: Comprehensive
**Objective:** Quantify and prioritize AI vendor security threats by business impact, supply chain attack sophistication, and likelihood

**Prerequisites:** ALL Level 1 questions must be "Fully Mature" to proceed to Level 2

### Question 4: Abuse Cases and Attack Trees

**Q2.1:** Have you developed detailed abuse cases and attack trees for each HAI agent performing vendor security, showing how adversaries could exploit or degrade HAI vendor security operations to enable supply chain attacks or organizational compromise?

**Evidence Required:**
- [ ] At least 3-5 abuse cases documented per AI vendor security agent
- [ ] Abuse cases include:
  - Attacker goal, attack path (step-by-step), prerequisites, impact (by vendor criticality tier), likelihood, regulatory consequences
- [ ] Attack trees showing multiple paths to organizational compromise via vendor (malicious vendor approval, vendor compromise, supply chain dependency attack, fourth-party attack)
- [ ] Specific examples documented:
  - Malicious vendor approval through questionnaire gaming (prompt injection, fake certifications, assessment pattern exploitation)
  - Dependency confusion attack evading AI SCA (public package repository with higher version, obfuscated malware)
  - Vendor breach undetected by AI continuous monitoring (lagging indicators, credential theft, data exfiltration)
  - Fourth-party supply chain attack outside AI visibility (subprocessor compromise, vendor's vendor breach)
  - Vendor acquisition risk missed by AI (ownership change, security degradation post-acquisition)
- [ ] Abuse cases validated by vendor risk team and shared with stakeholders (procurement, legal, executive leadership)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Average number of abuse cases documented per critical AI vendor security agent | ___ | ___ | ≥3 abuse cases | ☐ | |
| % of critical vendors with documented attack trees showing ≥2 organizational compromise paths | ___ | ___ | 100% | ☐ | |
| AI vendor risk assessment accuracy when validated against independent assessments or known breach outcomes | ___ | ___ | ≥90% | ☐ | |
| % of high/critical vendor threats with documented and validated mitigation strategies | ___ | ___ | ≥85% | ☐ | |

**Metric Collection Guidance:**
- **Avg abuse cases per agent**: Count total documented abuse cases in registry; divide by number of AI vendor security agents (vendor risk platform, SCA tool, continuous monitoring); source from abuse case registry
- **% with attack trees**: Audit each critical AI vendor security agent for presence of attack tree with ≥2 distinct paths (e.g., malicious vendor approval AND vendor compromise paths); divide qualifying agents by total critical agents
- **AI vendor assessment accuracy**: Quarterly: run AI vendor risk assessment against historical vendor dataset where actual risk outcomes are known (vendor breaches, security failures); formula: (correct risk classifications / total vendors assessed) x 100; supplement with red team validation using test vendor scenarios
- **% threats with validated mitigations**: Count high/critical threats in vendor risk matrix; divide those with implemented and tested mitigation by total; validate through adversarial testing evidence

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

**Q2.2:** Have you assessed and prioritized AI vendor security threats using a risk matrix (likelihood × impact × supply chain attack sophistication), with documented mitigation strategies for high-priority threats differentiated by vendor criticality tier?

**Evidence Required:**
- [ ] Risk assessment framework with likelihood, impact, and supply chain attack sophistication criteria
- [ ] Each threat scenario assessed for:
  - Likelihood (High/Medium/Low based on technical feasibility, public examples, attacker motivation)
  - Business impact differentiated by vendor criticality tier (Critical vendors: cloud/payment/security vs. High vendors: business-critical SaaS vs. Medium-Low vendors: support/marketing)
  - Supply chain attack sophistication (nation-state vs. criminal organization vs. opportunistic)
- [ ] Risk matrix created (e.g., 3×3 or 5×5 grid)
- [ ] High-priority threats identified (High likelihood + Critical impact)
- [ ] Mitigation strategies documented for top 5-10 threats with specific controls:
  - Vendor breach undetected → Multi-source vendor monitoring (AI + manual threat hunting + breach intelligence feeds), vendor access behavioral analytics, 24-hour breach notification SLAs
  - Malicious dependency supply chain attacks → Multi-layered dependency security (AI SCA + curated private repositories + dependency pinning + SBOM validation + code review)
  - Malicious vendor approval → Human validation of critical/high vendor approvals, independent verification of certifications, reference checks, deep-dive assessments
  - Fourth-party subprocessor risks → Subprocessor discovery/mapping, GDPR Article 28(2) approval workflows, contractual flow-down requirements, extended monitoring
- [ ] Risk assessment reviewed quarterly and updated based on vendor breaches, supply chain attacks, regulatory enforcement

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Mean time to detect vendor security degradation or breach (days) | ___ | ___ | ≤7 days | ☐ | |
| AI SCA detection rate for adversarial dependency attacks in quarterly evasion testing | ___ | ___ | ≥95% | ☐ | |
| % of critical vendor subprocessors with documented risk assessments (fourth-party visibility) | ___ | ___ | ≥80% | ☐ | |
| Number of successful supply chain attacks via vendor compromise in measurement period | ___ | ___ | 0 | ☐ | |

**Metric Collection Guidance:**
- **Mean time to detect vendor degradation**: For each vendor security incident or simulated breach, measure elapsed time from breach occurrence to AI/human detection; formula: sum of detection times / number of incidents; source from vendor monitoring alert log and incident records; for simulation, use vendor breach simulation exercise timestamps
- **SCA detection rate**: Quarterly: create test malicious packages (dependency confusion, typosquatting, obfuscated malware) in isolated test environment; run production AI SCA; formula: (malicious packages detected / total injected malicious packages) x 100; source from SCA evasion test report
- **% fourth-party coverage**: Select all critical vendors (tier 1); conduct subprocessor discovery interviews or questionnaire; count subprocessors with documented risk assessments; formula: (subprocessors with risk assessment / total discovered subprocessors for critical vendors) x 100
- **Successful supply chain attacks**: Count confirmed supply chain attacks through vendor relationships in measurement period; source from incident management system; zero is target; validate through red team exercise results

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

**Q2.3:** Have you integrated threat intelligence from supply chain security research, vendor breach disclosures, vulnerability databases, and industry sources to continuously identify emerging threats to AI vendor security, with annual validation of threat models?

**Evidence Required:**
- [ ] Threat intelligence sources identified and monitored:
  - Supply Chain Security Research (NIST SSDF/SP 800-161, OpenSSF, SLSA framework, SBOM standards)
  - Real-World Vendor Breach Intelligence (MOVEit, Kaseya, Okta incidents; SolarWinds, Codecov, event-stream supply chain attacks)
  - Vendor Risk Platform Intelligence (OneTrust, ServiceNow, BitSight, SecurityScorecard advisories)
  - Regulatory & Compliance Intelligence (GDPR Article 28 enforcement, HIPAA BAA violations, PCI-DSS 12.8, SOC 2 vendor findings)
  - Attack Technique Databases (MITRE ATT&CK supply chain compromise, dependency attack databases, software supply chain frameworks)
- [ ] Monitoring cadence established:
  - Daily: Critical vendor breaches, major supply chain attack disclosures, malicious package alerts
  - Weekly: Vendor breach intelligence, supply chain security advisories, regulatory enforcement actions
  - Monthly: Academic research papers, vendor risk best practices, AI assessment tool updates
  - Quarterly: Threat model updates, vendor risk priority reassessment, threat landscape briefing
- [ ] Threat intelligence findings documented in structured format (threat name, description, affected vendor types, prerequisites, mitigation recommendations)
- [ ] Annual comprehensive threat model validation completed

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Number of distinct threat intelligence sources actively monitored (supply chain, breach intel, regulatory) | ___ | ___ | ≥10 sources | ☐ | |
| Days from major vendor breach disclosure to vendor threat model update | ___ | ___ | ≤7 days | ☐ | |
| % of detected vendor security incidents predicted in threat model | ___ | ___ | ≥80% | ☐ | |
| % of AI vendor assessment overrides (human overriding AI) that are validated as correct decisions | ___ | ___ | ≥85% | ☐ | |

**Metric Collection Guidance:**
- **Number of sources monitored**: Enumerate all active intelligence subscriptions, breach monitoring feeds, regulatory alert services; count distinct sources in threat intel register; include daily malicious package alerts, weekly breach intelligence, monthly research monitoring
- **Days to model update after breach**: For each major public vendor breach (MOVEit-class events), calculate days from public disclosure to threat model update incorporating the breach pattern; source from threat model changelog and breach disclosure timestamps
- **% incidents predicted**: After each vendor security incident affecting the organization or portfolio, check if attack vector was in threat model; formula: (incidents matching threat model entry / total vendor incidents) x 100; review at annual validation
- **% override accuracy**: Track all human overrides of AI vendor risk decisions; after 12 months, validate if override was correct (using vendor breach data, independent assessment, or retrospective review); formula: (correct overrides / total overrides) x 100; source from vendor risk decision log

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________
**Metric Validation Date:** _________________________________
**Notes:** ___________________________________________

---

**Level 2 Score:** _____ / 3.0 (sum of question scores using 1.0/0.67/0.33/0.0)

**Level 2 Achieved (all Fully Mature):** ☐ Yes ☐ No

---

## Level 3: Industry-Leading
**Objective:** Proactively test and share threat intelligence through adversarial testing, vendor security validation, and industry contribution

**Prerequisites:** ALL Level 2 questions must be "Fully Mature" to proceed to Level 3

### Question 7: Adversarial Testing and Red Team Exercises

**Q3.1:** Do you conduct periodic (at least quarterly) adversarial testing and red team exercises against your HAI vendor security agents to proactively identify weaknesses before attackers exploit them?

**Evidence Required:**
- [ ] Quarterly adversarial testing program established:
  - AI vendor risk assessment validation (test vendor dataset with known risk profiles, adversarial vendors with fake certifications/questionnaire gaming/prompt injection)
  - Supply chain / SCA evasion testing (test malicious packages: dependency confusion, typosquatting, backdoored libraries, obfuscated malware)
  - Vendor breach simulation (simulated vendor compromise scenarios, unusual access patterns, credential theft, data exfiltration)
- [ ] Testing methodology includes:
  - Create test vendor dataset of 50-100 simulated vendors (high-risk/insecure, medium-risk, low-risk/secure)
  - Measure AI vendor assessment accuracy: % of high-risk vendors correctly identified (target: >90%)
  - Measure AI SCA detection rate across attack types (target: >95% detection)
  - Measure AI vendor monitoring detection time for simulated breaches (target: 24-48 hours)
- [ ] Annual vendor security red team exercise (2-4 weeks, attempt to compromise organization through vendor relationships)
- [ ] Test reports documenting:
  - Vendor assessment misclassification patterns (false negatives/positives)
  - SCA blind spots (undetected attack techniques)
  - Vendor monitoring gaps (missed compromise indicators)
  - Recommendations for improvement
- [ ] Evidence of vendor tool engagement or model updates when accuracy falls below threshold

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| AI vendor risk assessment accuracy on test dataset (high-risk vendors correctly identified) | ___ | ___ | ≥90% | ☐ | |
| AI vendor monitoring detection time for simulated vendor compromise scenarios | ___ | ___ | ≤48 hours | ☐ | |
| % of red team vendor attack scenarios successfully blocked by AI vendor security defenses | ___ | ___ | ≥80% | ☐ | |
| AI vendor risk model accuracy on golden dataset (quarterly measurement - drift detection) | ___ | ___ | ≥90% with ≤10% drift | ☐ | |

**Metric Collection Guidance:**
- **Vendor assessment accuracy**: Quarterly: run 50-100 simulated vendor scenarios (known-high-risk with fake certs, questionnaire gaming, prompt injection; known-low-risk); formula: (correctly classified vendors / total test vendors) x 100; source from quarterly vendor assessment validation report
- **Detection time for simulated breach**: Semi-annual: simulate vendor compromise (unusual access patterns, credential theft indicators, data exfiltration signals from test vendor account); measure elapsed time from simulation start to AI/human detection; source from vendor breach simulation report
- **Red team block rate**: Annual: red team attempts malicious vendor onboarding, dependency injection, vendor compromise pivot; count attack objectives attempted; formula: (blocked/detected objectives / total objectives) x 100; source from annual vendor red team report
- **Golden dataset drift**: Quarterly: run AI vendor assessment against 100-200 historical vendor assessments with validated outcomes; formula: (correct assessments / total) x 100 compared to prior quarter; alert if >10% drift; source from quarterly accuracy dashboard

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

**Q3.2:** Do you publish original threat research on AI vendor security vulnerabilities, supply chain attacks, or third-party risk management through blog posts, conference presentations, responsible disclosures, or contributions to supply chain security frameworks?

**Evidence Required:**
- [ ] At least 2 public threat intelligence contributions per year
- [ ] Contributions include:
  - Blog posts on vendor assessment evasion techniques, supply chain attack case studies, dependency attack methods
  - Conference presentations (RSA, Black Hat, DEF CON, SANS, supply chain security conferences)
  - Responsible vulnerability disclosures to AI vendor risk platform vendors (OneTrust, ServiceNow, BitSight, SecurityScorecard)
  - Contributions to OpenSSF, SLSA framework, SBOM standards, MITRE ATT&CK supply chain compromise, vendor risk best practices
- [ ] Public evidence (published articles, conference proceedings, CVE assignments, framework contributions)
- [ ] Documented impact (vendor patches, industry awareness, supply chain security community engagement)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Number of public vendor/supply chain threat intelligence contributions published in last 12 months | ___ | ___ | ≥2 | ☐ | |
| Number of responsible disclosures to AI vendor risk platform vendors with acknowledged outcome | ___ | ___ | ≥1 | ☐ | |
| Number of contributions to supply chain security frameworks (OpenSSF, SLSA, SBOM, MITRE ATT&CK supply chain) | ___ | ___ | ≥1 | ☐ | |
| Number of novel vendor threat scenarios identified before public supply chain attack or advisory | ___ | ___ | ≥3 per year | ☐ | |

**Metric Collection Guidance:**
- **Number of publications**: Count blog posts, technical papers, conference presentations on vendor/supply chain security published with organization attribution in rolling 12 months; source from publication tracker
- **Responsible disclosures**: Count CVDs submitted to OneTrust, ServiceNow, BitSight, SecurityScorecard, or similar platforms; count those receiving formal acknowledgment, patch, or CVE assignment; source from disclosure tracking log
- **Framework contributions**: Count accepted contributions to OpenSSF, SLSA, SBOM working groups, or MITRE ATT&CK supply chain techniques; source from GitHub commit history or working group acknowledgment records
- **Proactive threat identification**: Count vendor threats added to threat model with documented date; cross-reference against public supply chain attack databases and advisory publication dates to confirm they predate public disclosure; source from threat model changelog

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

**Q3.3:** Do you maintain a continuous improvement program for AI vendor security threat models, incorporating lessons learned from adversarial testing, real-world vendor breaches/supply chain attacks, and emerging research, with evidence of threat model evolution over time?

**Evidence Required:**
- [ ] Documented process for updating threat models based on:
  - Adversarial testing results (quarterly vendor assessment validation, SCA evasion testing, vendor breach simulation)
  - Real-world AI vendor security incidents (vendor breaches affecting organization, supply chain attacks, dependency vulnerabilities, fourth-party compromises)
  - Emerging research (supply chain security research, vendor breach case studies, dependency attack techniques, regulatory enforcement)
  - Red team exercise findings (annual vendor security red team results)
- [ ] Historical record showing threat model evolution (12+ months of updates)
- [ ] Examples of threat model updates triggering new mitigations (enhanced vendor assessment procedures, supply chain security controls, monitoring improvements, fourth-party mapping)
- [ ] Feedback loop: Threat intelligence → Testing → Model update → Mitigation → Re-test
- [ ] Metrics tracked: # of new threats identified, % of threats mitigated, vendor assessment accuracy trend, SCA detection rate, vendor breach detection time
- [ ] Model drift monitoring program with quarterly testing against golden vendor dataset:
  - 100-200 historical vendor assessments with validated risk scores
  - Accuracy trend monitoring, automated alerting when accuracy degrades >10%
- [ ] Fourth-party risk mapping program with validated subprocessor visibility and GDPR Article 28 compliance

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| % of vendor threat model content updated annually based on new supply chain attacks or research | ___ | ___ | ≥20% | ☐ | |
| % of quarterly adversarial test findings resulting in documented vendor security improvement | ___ | ___ | ≥80% | ☐ | |
| % of critical vendor subprocessors monitored with GDPR Article 28 compliant approval workflows | ___ | ___ | ≥80% | ☐ | |
| Number of proactive vendor threat scenarios discovered per quarter through threat intelligence before exploitation | ___ | ___ | ≥5 per year | ☐ | |

**Metric Collection Guidance:**
- **% model content updated**: Compare current vendor threat model to 12-months-prior version; count distinct threat scenarios, mitigations, or attack patterns added or substantially modified; formula: (changed items / total prior-version items) x 100; source from version control diff
- **% findings actioned**: After each quarterly adversarial test, count findings generating a mitigation ticket; track closure within 90 days; formula: (findings with closed improvement action / total findings) x 100; source from issue tracker linked to test reports
- **% subprocessors with GDPR-compliant workflows**: For all critical vendors, count discovered subprocessors; divide those with completed Article 28 subprocessor assessment and approved DPA flow-down by total discovered subprocessors; source from fourth-party risk registry
- **Proactive threat discovery**: Count new vendor threats in model documented before public supply chain attack, CVE, or vendor advisory references that technique; verify dates from threat model changelog vs. NVD/vendor advisory publication dates; annual count

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________
**Metric Validation Date:** _________________________________
**Notes:** ___________________________________________

---

**Level 3 Score:** _____ / 3.0 (sum of question scores using 1.0/0.67/0.33/0.0)

**Level 3 Achieved (all Fully Mature):** ☐ Yes ☐ No

---

## Practice Score Calculation

### Updated Scoring Formula

```
L1_score = (Q1.1 + Q1.2 + Q1.3) / 3
L2_score = (Q2.1 + Q2.2 + Q2.3) / 3 × (L1 if L1 ≥ 1.0, else 0)
L3_score = (Q3.1 + Q3.2 + Q3.3) / 3 × (L2 if L2 ≥ 1.0, else 0)
Practice Score = L1_score + L2_score + L3_score (Max = 3.0)
```

**TA-Vendors Practice Score:** _______ / 3.0

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
- [ ] Supply chain attacks (malicious vendor approval, malicious dependency injection, compromised SBOM, vendor compromise for lateral attack, fourth-party supply chain attack, software update supply chain attack)
- [ ] Adversarial manipulation of vendor assessments (prompt injection in questionnaires, vendor assessment gaming, social engineering of AI analysts, fake security certifications, vendor security theater)
- [ ] Data poisoning & model corruption (vendor risk model poisoning, questionnaire answer poisoning, supply chain baseline poisoning, vendor breach data manipulation)
- [ ] Operational vendor security failures (false negatives missing vendor breaches/supply chain attacks/catastrophic vendor approvals, false positives blocking legitimate vendors, model drift)
- [ ] Fourth-party & extended supply chain risks (subprocessor risk blindness, vendor acquisition risk, concentrated vendor dependencies, vendor exit risk)
- [ ] Regulatory & compliance risks (GDPR Article 28 violations, HIPAA BAA failures, PCI-DSS vendor management gaps, SOC 2 vendor control failures)

**Supply Chain Attack Coverage:**
- [ ] Dependency confusion attacks (public package repositories, internal package naming, version manipulation)
- [ ] Typosquatting and malicious packages (npm, PyPI, RubyGems, Maven attacks)
- [ ] Compromised package repositories and maintainer takeovers
- [ ] SBOM manipulation and falsification
- [ ] Transitive dependency risks and abandoned packages
- [ ] Software update supply chain attacks (SolarWinds-style attacks)

**Adversarial Testing Coverage:**
- [ ] Vendor risk assessment validation (test vendor datasets, adversarial vendors, fake certifications, questionnaire gaming)
- [ ] Supply chain / SCA evasion testing (malicious packages, dependency confusion, typosquatting, obfuscated malware)
- [ ] Vendor breach simulation (credential theft, unusual access patterns, data exfiltration detection)
- [ ] Vendor security red team exercises (full adversarial simulation through vendor relationships)
- [ ] Model drift detection (quarterly testing against golden vendor dataset, accuracy trend monitoring)
- [ ] Fourth-party risk mapping (subprocessor discovery, GDPR Article 28 compliance validation)

**Vendor Tier Differentiation:**
- [ ] Critical vendors (cloud infrastructure, payment processors, primary SaaS, security services, data processors)
- [ ] High vendors (business-critical SaaS, development tools, analytics platforms)
- [ ] Medium-Low vendors (support, marketing, non-critical services)

**Regulatory Compliance Coverage:**
- [ ] GDPR Article 28 (processor obligations, subprocessor approval, Data Processing Agreements)
- [ ] HIPAA BAA (Business Associate Agreements, PHI protection, vendor safeguards)
- [ ] PCI-DSS 12.8 (service provider management, vendor compliance monitoring)
- [ ] SOC 2 vendor controls (vendor due diligence, ongoing monitoring, vendor audit findings)

---

## Updated Scoring Methodology

### Question-Level Scoring
| Answer Category | Score | Criteria |
|----------------|-------|----------|
| **Fully Mature** | 1.0 | Evidence complete + ≥75% of metrics meet targets (≥3 of 4 metrics) |
| **Implemented** | 0.67 | Evidence complete + 50-74% of metrics meet targets (2 of 4 metrics) |
| **Partial** | 0.33 | Evidence complete + <50% metrics meet targets OR incomplete evidence |
| **Not Implemented** | 0.0 | No evidence |

### Level Scoring
```
L1_score = (Q1.1 + Q1.2 + Q1.3) / 3
L2_score = (Q2.1 + Q2.2 + Q2.3) / 3 × (L1 if L1 ≥ 1.0, else 0)
L3_score = (Q3.1 + Q3.2 + Q3.3) / 3 × (L2 if L2 ≥ 1.0, else 0)
Practice Score = L1_score + L2_score + L3_score (Max = 3.0)
```

| Score Range | Level |
|-------------|-------|
| 2.5-3.0 | Level 3: Industry-Leading |
| 1.5-2.49 | Level 2: Comprehensive |
| 0.5-1.49 | Level 1: Foundational |
| <0.5 | Level 0: Ad-hoc |

---

**Document Version:** 3.0
**Last Updated:** 2026-02-19
**Next Review:** Quarterly or after significant HAI system changes
