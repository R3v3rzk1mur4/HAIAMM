# Threat Assessment (TA) - Infrastructure Domain
## HAIAMM Assessment Questionnaire v3.0

**Practice:** Threat Assessment (TA)
**Domain:** Infrastructure
**Purpose:** Assess organizational maturity in identifying and analyzing threats specific to Human Assisted Intelligence in infrastructure security operations
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
**Objective:** Establish baseline threat awareness for HAI infrastructure security

### Question 1: AI-Specific Threat Scenario Identification

**Q1.1:** Have you documented threat scenarios specific to Human Assisted Intelligence systems performing infrastructure security functions (e.g., CSPM, network anomaly detection, vulnerability scanning, automated remediation), including adversarial manipulation, data poisoning, operational failures, and supply chain threats?

**Evidence Required:**
- [ ] Inventory of HAI systems performing infrastructure security functions (cloud security, network detection, infrastructure hardening)
- [ ] Documented threat scenarios covering at least 4 categories:
  - Adversarial manipulation (prompt injection in CSPM, adversarial network traffic, firewall bypass, IDS evasion)
  - Data poisoning (network traffic poisoning, configuration baseline corruption, vulnerability database manipulation)
  - Operational failures (false negatives missing cloud misconfigurations/intrusions, false positives causing infrastructure lockdown, automated misconfiguration, cascading remediation failures)
  - Supply chain threats (compromised AI CSPM/CNAPP tools, malicious AI security agents, model weight tampering)
- [ ] Threat scenarios specific to cloud environments (multi-cloud AWS/Azure/GCP, containers, Kubernetes, serverless)
- [ ] Document updated within last 12 months

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| % of known AI infra attack vectors documented (CSPM evasion, IDS bypass, auto-remediation risks) | ___ | ___ | ≥85% | ☐ | |
| Number of documented threat scenarios covering ≥4 categories | ___ | ___ | ≥12 scenarios | ☐ | |
| % of AI infra agents mapped to ≥3 threat scenarios each | ___ | ___ | 100% | ☐ | |
| Days since threat document last updated | ___ | ___ | ≤365 days | ☐ | |

**Metric Collection Guidance:**
- **% attack vectors documented**: Enumerate known attack vector categories from MITRE ATLAS + MITRE ATT&CK for Cloud; divide documented categories by total enumerated; collect at document creation and quarterly
- **Number of threat scenarios**: Count distinct scenarios in threat inventory document; minimum 12 required covering adversarial manipulation, data poisoning, operational failures, supply chain, AI-generated IaC risks, cloud-specific threats
- **% agents mapped**: Divide number of AI infra agents with ≥3 mapped threat scenarios by total AI infra agents; extract from threat model index
- **Days since update**: Calculate from document metadata last-modified date; alert if >90 days without review following a cloud provider advisory

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

**Q1.2:** Do you have documented threat models for your HAI infrastructure security operations, with identified threat owners responsible for tracking and mitigating each threat category?

**Evidence Required:**
- [ ] Formal threat model document for AI infrastructure security operations
- [ ] Threat model covers: attack vectors (prompt injection, adversarial evasion), failure modes (false negatives/positives), operational risks (cascading failures)
- [ ] Each threat category has assigned owner (individual or team)
- [ ] Threat model includes impact assessment by infrastructure tier (production/critical vs. staging vs. development)
- [ ] Threat model reviewed and approved by infrastructure security leadership
- [ ] Threat model accessible to relevant teams (infrastructure, security operations, cloud architects, AI/ML)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| % of threat categories with named owner assigned | ___ | ___ | 100% | ☐ | |
| % of threats differentiated by infrastructure tier (prod/staging/dev) | ___ | ___ | 100% | ☐ | |
| Days since threat model reviewed and approved by leadership | ___ | ___ | ≤90 days | ☐ | |
| % of relevant teams with documented access to threat model | ___ | ___ | 100% | ☐ | |

**Metric Collection Guidance:**
- **% with owner**: Count threat categories in model with named individual/team owner; divide by total threat categories; extract from threat model ownership table
- **% tiered by infra tier**: Audit threat model for production/staging/development impact differentiation; count threats with tier-differentiated impact statements divided by total threats
- **Days since leadership review**: Extract from document approval metadata or review log; target ≤90 days (aligns with quarterly threat model review cadence)
- **% teams with access**: Survey relevant teams (infra, SecOps, cloud architects, AI/ML); divide teams with confirmed access by total relevant teams

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

**Q1.3:** Have you conducted threat awareness training for infrastructure engineers, cloud architects, security operations, and IT leadership on AI-specific threats to infrastructure security operations within the last 90 days of AI tool deployment?

**Evidence Required:**
- [ ] Training materials covering AI infrastructure security threats
- [ ] Training delivered to at least 3 stakeholder groups:
  - Infrastructure Engineers (how AI CSPM can be manipulated, why AI-generated IaC requires security review, validating AI security findings)
  - Security Operations Teams (adversarial ML attacks on network detection, when to distrust AI findings, supply chain risks in AI tools)
  - Cloud Architects & Engineering Leadership (business risk of AI failures, when AI autonomy is appropriate, governance requirements)
- [ ] Training includes real-world examples (adversarial network evasion research, AI CSPM bypass techniques, cloud misconfiguration incidents, insecure AI-generated IaC)
- [ ] Training conducted within 90 days of AI infrastructure security tool deployment
- [ ] Attendance records and training completion tracking

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| % of infra engineers, cloud architects, and SecOps completing training | ___ | ___ | ≥80% | ☐ | |
| % of trainees passing post-training knowledge assessment (≥80% score) | ___ | ___ | ≥90% | ☐ | |
| Days from AI tool deployment to initial training delivery | ___ | ___ | ≤90 days | ☐ | |
| % of engineers correctly identifying AI infra manipulation attempts in simulated scenarios | ___ | ___ | ≥70% | ☐ | |

**Metric Collection Guidance:**
- **% training completion**: Divide staff completing training by total staff in target roles (infra engineers, cloud architects, SecOps); source from LMS attendance records
- **% passing assessment**: Run post-training quiz (≥10 questions on AI infra threats); divide passing scores by total completions; extract from LMS gradebook
- **Days to training delivery**: Calculate from AI tool go-live date to first training session date; source from deployment log and training calendar
- **% simulation success**: Conduct tabletop or phishing-style simulation testing ability to identify prompt injection in CSPM context; score and divide correct identifications by total participants

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
**Objective:** Quantify and prioritize AI infrastructure security threats by business impact and likelihood

**Prerequisites:** ALL Level 1 questions must be "Fully Mature" to proceed to Level 2

### Question 4: Abuse Cases and Attack Trees

**Q2.1:** Have you developed detailed abuse cases and attack trees for each HAI agent performing infrastructure security, showing how adversaries could exploit or degrade HAI infrastructure security operations?

**Evidence Required:**
- [ ] At least 3-5 abuse cases documented per AI infrastructure security agent
- [ ] Abuse cases include:
  - Attacker goal, attack path (step-by-step), prerequisites, impact (by infrastructure tier), likelihood
- [ ] Attack trees showing multiple paths to infrastructure compromise
- [ ] Specific examples documented:
  - Prompt injection in CSPM via cloud resource metadata (tags, descriptions)
  - Adversarial network traffic for IDS evasion (slow exfiltration, protocol tunneling)
  - Cloud configuration baseline poisoning (corrupting secure reference configurations)
  - Automated remediation cascade failure (triggering service disruptions)
  - Model drift exploitation (attacks disguised as new legitimate traffic patterns)
- [ ] Abuse cases validated by infrastructure security team and shared with stakeholders

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Average number of abuse cases documented per AI infra security agent | ___ | ___ | ≥3 abuse cases | ☐ | |
| % of critical AI infra agents with attack trees showing ≥2 compromise paths | ___ | ___ | 100% | ☐ | |
| % of production cloud misconfigurations detected by AI CSPM in quarterly validation testing | ___ | ___ | ≥90% | ☐ | |
| % of high-priority threats with documented mitigation strategies | ___ | ___ | ≥75% | ☐ | |

**Metric Collection Guidance:**
- **Avg abuse cases per agent**: Count total documented abuse cases; divide by number of AI infra security agents in inventory; source from abuse case registry
- **% with attack trees**: Audit each critical AI infra agent for presence of attack tree with ≥2 paths to compromise; divide qualifying agents by total critical agents
- **% CSPM detection**: Quarterly: create 100-200 intentional cloud misconfigurations (public S3, overly permissive IAM, disabled logging); run AI CSPM; divide detected by total injected; formula: (detected misconfigs / total injected misconfigs) x 100
- **% threats with mitigations**: Count distinct high-priority threats in risk matrix; divide those with at least one documented mitigation control by total high-priority threats

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

**Q2.2:** Have you assessed and prioritized AI infrastructure security threats using a risk matrix (likelihood × impact), with documented mitigation strategies for high-priority threats differentiated by infrastructure criticality tier?

**Evidence Required:**
- [ ] Risk assessment framework with likelihood and impact criteria
- [ ] Each threat scenario assessed for:
  - Likelihood (High/Medium/Low based on technical feasibility, public research, attacker skill)
  - Business impact differentiated by infrastructure tier (Critical/Production vs. High/Staging vs. Medium-Low/Development)
- [ ] Risk matrix created (e.g., 3×3 or 5×5 grid)
- [ ] High-priority threats identified (High likelihood + Critical impact)
- [ ] Mitigation strategies documented for top 5-10 threats with specific technical controls:
  - AI network IDS evasion → Multi-layered detection, encrypted traffic inspection, deception technology
  - AI-generated insecure IaC → Mandatory security review, automated IaC scanning (Checkov, tfsec), policy-as-code enforcement
  - Model drift → Monthly performance testing, automated drift detection, scheduled retraining
- [ ] Risk assessment reviewed quarterly and updated based on threat intelligence

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| % of high/critical infrastructure threats with mitigations implemented and validated | ___ | ___ | ≥75% | ☐ | |
| AI network IDS detection rate for adversarial traffic in quarterly evasion testing | ___ | ___ | ≥85% | ☐ | |
| Number of production outages caused by AI auto-remediation errors in measurement period | ___ | ___ | 0 | ☐ | |
| Days to implement mitigation for high-priority threats after identification | ___ | ___ | ≤90 days | ☐ | |

**Metric Collection Guidance:**
- **% mitigations implemented**: Count high/critical threats in risk matrix; divide those with at least one implemented and tested mitigation control by total high/critical threats; validate through quarterly adversarial test results
- **IDS detection rate**: Quarterly red team test: launch labeled adversarial traffic (slow exfiltration, protocol tunneling, traffic mimicry) in test environment; formula: (alerts triggered / total adversarial traffic sessions) x 100; source from red team evasion test report
- **Production outages from auto-remediation**: Count change management tickets flagged as AI auto-remediation errors causing outage; source from incident management system (PagerDuty, ServiceNow)
- **Days to mitigation**: Track from risk matrix entry date to confirmed mitigation deployment date; source from risk register and change management system

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

**Q2.3:** Have you integrated threat intelligence from academic research, cloud security advisories, vulnerability databases, and industry sources to continuously identify emerging threats to AI infrastructure security, with annual validation of threat models?

**Evidence Required:**
- [ ] Threat intelligence sources identified and monitored:
  - Academic research (NeurIPS, ICML, IEEE Security on adversarial ML, network security)
  - Cloud vendor security advisories (AWS Security Bulletins, Azure Security Center, GCP Security Command Center)
  - AI CSPM/CNAPP vendor advisories (Wiz, Prisma Cloud, Orca Security, Lacework)
  - Attack technique databases (MITRE ATT&CK for Cloud, MITRE ATLAS, CSA Threat Horizon, OWASP Cloud-Native Top 10)
- [ ] Monitoring cadence established:
  - Weekly: CVE scanning for AI/ML dependencies, cloud platform security updates
  - Monthly: Academic research review, cloud security conference proceedings, vendor advisories
  - Quarterly: Threat model updates, risk priority reassessment
- [ ] Threat intelligence findings documented in structured format
- [ ] Annual comprehensive threat model validation completed

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Number of distinct threat intelligence sources actively monitored | ___ | ___ | ≥15 sources | ☐ | |
| Days from cloud security advisory publication to threat model update | ___ | ___ | ≤30 days | ☐ | |
| % of detected infrastructure attacks predicted in threat model | ___ | ___ | ≥80% | ☐ | |
| Number of threat model updates completed in last 12 months | ___ | ___ | ≥4 (quarterly) | ☐ | |

**Metric Collection Guidance:**
- **Number of sources monitored**: Enumerate all intelligence feeds, advisory subscriptions, research monitoring channels; document in threat intel register; count distinct sources
- **Days to threat model update**: For each new advisory actioned, calculate days from advisory publication date to threat model update commit; average across all actioned advisories in quarter; source from threat model git history and advisory timestamps
- **% attacks predicted**: After each detected infrastructure security incident or near-miss, check if attack vector was in threat model; formula: (incidents with matching threat model entry / total incidents) x 100; review quarterly
- **Number of updates**: Count distinct threat model revision commits or versioned updates in 12-month period; source from threat model version control log

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
**Objective:** Proactively test and share threat intelligence through adversarial testing and industry contribution

**Prerequisites:** ALL Level 2 questions must be "Fully Mature" to proceed to Level 3

### Question 7: Adversarial Testing and Red Team Exercises

**Q3.1:** Do you conduct periodic (at least quarterly) adversarial testing and red team exercises against your HAI infrastructure security agents to proactively identify weaknesses before attackers do?

**Evidence Required:**
- [ ] Quarterly adversarial testing program established:
  - Cloud misconfiguration evasion testing (CSPM tools, prompt injection via resource tags, configuration obfuscation)
  - Network intrusion detection evasion testing (adversarial traffic patterns, slow/low techniques, protocol tunneling)
- [ ] Testing methodology includes:
  - Create intentional insecure cloud configurations (public S3 buckets, overly permissive IAM, disabled logging, unencrypted storage)
  - Apply adversarial techniques (prompt injection, evasion patterns, timing-based evasion)
  - Measure evasion success rate (target: AI detects >95% of misconfigurations and >90% of network intrusions)
- [ ] Semi-annual prompt injection testing (for LLM-based CSPM tools)
- [ ] Annual infrastructure red team exercise (2-4 weeks, attempt to compromise cloud infrastructure despite AI security defenses)
- [ ] Test reports documenting:
  - Evasion techniques that succeeded
  - Specific misconfiguration/attack types bypassed
  - Recommendations for improvement
- [ ] Evidence of AI vendor engagement or model retraining when detection rate falls below threshold

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| AI CSPM detection rate for intentional misconfigurations in quarterly evasion testing | ___ | ___ | ≥95% | ☐ | |
| AI network IDS detection rate across all attack categories in quarterly testing | ___ | ___ | ≥90% | ☐ | |
| % of red team infrastructure compromise attempts detected and blocked | ___ | ___ | ≥85% | ☐ | |
| Hours to detect AI infrastructure security tool degradation and initiate correction | ___ | ___ | ≤72 hours | ☐ | |

**Metric Collection Guidance:**
- **CSPM detection rate**: Quarterly: inject 100-200 known misconfigurations across cloud accounts; formula: (misconfigs flagged by AI CSPM / total injected misconfigs) x 100; include prompt injection variants in 50% of test resources; source from CSPM test report
- **IDS detection rate**: Quarterly: red team executes labeled attack sessions (recon, lateral movement, exfiltration, C2) using adversarial evasion; formula: (sessions triggering IDS alert / total attack sessions) x 100; source from red team report
- **Red team block rate**: Annual red team: count total compromise attempt objectives; divide blocked/detected objectives by total objectives; source from annual red team final report
- **Hours to detect degradation**: When golden dataset monthly test shows accuracy drop >5%, measure elapsed time from test completion to vendor engagement or retraining initiation; source from model drift monitoring log

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

**Q3.2:** Do you publish original threat research on AI infrastructure security vulnerabilities through blog posts, conference presentations, responsible disclosures, or contributions to MITRE ATT&CK/ATLAS, CSA, or OWASP Cloud-Native Security?

**Evidence Required:**
- [ ] At least 2 public threat intelligence contributions per year
- [ ] Contributions include:
  - Blog posts on AI CSPM/network detection bypass techniques
  - Conference presentations (re:Inforce, Cloud Security Summit, Black Hat, DEF CON, SANS)
  - Responsible vulnerability disclosures to AI infrastructure security vendors (Wiz, Prisma Cloud, Orca, Darktrace, Vectra)
  - Contributions to MITRE ATT&CK for Cloud, MITRE ATLAS, CSA Threat Horizon, OWASP Cloud-Native Application Security Top 10
- [ ] Public evidence (published articles, conference proceedings, CVE assignments, framework contributions)
- [ ] Documented impact (vendor patches, industry awareness, community engagement)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Number of public threat intelligence contributions published in last 12 months | ___ | ___ | ≥2 | ☐ | |
| Number of responsible disclosures to AI infra security vendors resulting in acknowledgment or patch | ___ | ___ | ≥1 | ☐ | |
| Number of contributions to recognized frameworks (MITRE ATT&CK for Cloud, ATLAS, CSA, OWASP) | ___ | ___ | ≥1 | ☐ | |
| Evidence of documented community impact (vendor patches, CVE assignments, framework updates) | ___ | ___ | ≥1 impact | ☐ | |

**Metric Collection Guidance:**
- **Number of publications**: Count blog posts, conference papers, technical reports published with organization attribution in 12-month rolling window; source from publication tracker or marketing/comms log
- **Responsible disclosures acknowledged**: Count CVDs submitted to vendors with formal acknowledgment, CVE assignment, or confirmed patch; source from disclosure tracking log
- **Framework contributions**: Count accepted pull requests, submitted ATT&CK techniques, or acknowledged CSA/OWASP contributions; source from GitHub contribution history or framework acknowledgment records
- **Community impact evidence**: Collect vendor patch notes citing disclosure, CVE database entries, framework changelog entries, or conference proceeding citations; source from public records

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

**Q3.3:** Do you maintain a continuous improvement program for AI infrastructure security threat models, incorporating lessons learned from adversarial testing, real-world incidents, and emerging research, with evidence of threat model evolution over time?

**Evidence Required:**
- [ ] Documented process for updating threat models based on:
  - Adversarial testing results (quarterly CSPM evasion tests, network IDS evasion tests)
  - Real-world AI infrastructure security incidents (internal or industry cloud breaches, network compromises)
  - Emerging research (academic papers on adversarial ML, cloud security research, vendor advisories)
  - Red team exercise findings (annual infrastructure red team results)
- [ ] Historical record showing threat model evolution (12+ months of updates)
- [ ] Examples of threat model updates triggering new mitigations (new detection rules, enhanced monitoring, compensating controls)
- [ ] Feedback loop: Threat intelligence → Testing → Model update → Mitigation → Re-test
- [ ] Metrics tracked: # of new threats identified, % of threats mitigated, evasion rate trend (CSPM, network IDS), model drift indicators
- [ ] Model drift monitoring program with monthly testing against golden datasets:
  - CSPM: 100-200 cloud configurations with known misconfigurations
  - Network Detection: labeled network traffic (malicious vs. benign)
  - Automated alerting when accuracy degrades >5%

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| % of threat model content updated annually based on new research or incidents | ___ | ___ | ≥20% | ☐ | |
| AI infra security tool detection accuracy on golden dataset (monthly test - CSPM true positive rate) | ___ | ___ | ≥95% | ☐ | |
| % of quarterly adversarial test findings resulting in documented mitigation action | ___ | ___ | ≥80% | ☐ | |
| Number of new infrastructure threats identified per quarter before public exploit or vendor advisory | ___ | ___ | ≥2 | ☐ | |

**Metric Collection Guidance:**
- **% content updated annually**: Compare current threat model version to version from 12 months prior; count sections, scenarios, or controls modified or added; formula: (changed items / total items in prior version) x 100; source from threat model version diff
- **Golden dataset accuracy**: Monthly: run AI CSPM and network detection against fixed golden dataset (100-200 CSPM configs, labeled network traffic); formula: (true positives / (true positives + false negatives)) x 100; track in monthly performance dashboard with automated alert at <90%
- **% findings actioned**: After each quarterly adversarial test, count findings with documented mitigation ticket created and closed within 90 days; formula: (findings with closed mitigation / total findings) x 100; source from issue tracker
- **New threats proactively identified**: Count threats added to threat model before a public CVE, vendor advisory, or public exploit references that technique; source from threat model changelog cross-referenced with advisory publication dates

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

**TA-Infrastructure Practice Score:** _______ / 3.0

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
- [ ] Adversarial manipulation (prompt injection in CSPM, adversarial network traffic, firewall/security group bypass, IDS/NIDS evasion)
- [ ] Data poisoning (network traffic poisoning, cloud configuration baseline corruption, vulnerability database manipulation, telemetry data poisoning)
- [ ] Operational infrastructure failures (false negatives missing cloud misconfigurations/network intrusions, false positives causing infrastructure lockdown, automated misconfiguration, cascading remediation failures, model drift)
- [ ] Supply chain and infrastructure threats (compromised AI CSPM/CNAPP tools, malicious AI security agents, model weight tampering, stolen cloud security models)
- [ ] AI-generated infrastructure risks (insecure IaC generation from ChatGPT/Copilot, vulnerable container configurations, dangerous auto-remediation)

**Cloud-Specific Threat Coverage:**
- [ ] Multi-tenant isolation failures (container escape, VM breakout, cloud resource isolation weaknesses)
- [ ] IAM and access management gaps (privilege escalation paths, cross-account access, role assumption chains)
- [ ] Cloud API abuse (metadata service abuse, SSRF, IAM enumeration)
- [ ] Serverless security gaps (Lambda function vulnerabilities, API Gateway misconfigurations, event-driven architecture risks)
- [ ] Infrastructure persistence (rogue IAM roles, backdoor Lambda functions, modified security groups)

**Adversarial Testing Coverage:**
- [ ] CSPM evasion testing (prompt injection, configuration obfuscation, timing-based evasion)
- [ ] Network IDS evasion testing (adversarial traffic patterns, slow/low techniques, protocol tunneling, traffic mimicry)
- [ ] IaC security testing (AI-generated Terraform/CloudFormation/Kubernetes manifests scanned for vulnerabilities)
- [ ] Model drift detection (monthly testing against golden datasets, accuracy trend monitoring)
- [ ] Infrastructure red team exercises (full adversarial simulation attempting cloud infrastructure compromise)

**Infrastructure Tier Differentiation:**
- [ ] Critical/Production infrastructure (data breach, multi-hour outage, compliance violation >$1M, widespread compromise)
- [ ] High/Staging infrastructure (credential exposure, business operations disruption, compliance risk)
- [ ] Medium-Low/Development infrastructure (security findings in non-production, rapid remediation possible)

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
