# Threat Assessment (TA) - Endpoints Domain
## HAIAMM Assessment Questionnaire v3.0

**Practice:** Threat Assessment (TA)
**Domain:** Endpoints
**Purpose:** Assess organizational maturity in identifying and analyzing threats specific to Human Assisted Intelligence in endpoint security operations
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
**Objective:** Establish baseline threat awareness for HAI endpoint security operations

### Question 1: AI-Specific Threat Scenario Identification

**Q1.1:** Have you documented threat scenarios specific to Human Assisted Intelligence systems performing endpoint security functions (e.g., EDR/XDR, behavioral analytics, ransomware detection, automated response), including adversarial evasion, data poisoning, operational failures, and AI-generated threats?

**Evidence Required:**
- [ ] Inventory of HAI systems performing endpoint security functions
- [ ] Documented threat scenarios covering at least 4 categories:
  - Adversarial manipulation & evasion (adversarial malware for EDR evasion, behavioral mimicry, LOTL attacks, AI-aware ransomware)
  - Data poisoning (behavioral baseline poisoning, false positive injection training, telemetry manipulation)
  - Operational failures (false negatives missing advanced threats/ransomware/insider threats, false positives causing business disruption, model drift, automated overreaction)
  - Supply chain threats (compromised AI EDR/XDR platforms, malicious agent updates, model tampering)
- [ ] Threat scenarios mapped to endpoint types (corporate laptops, BYOD, mobile devices, IoT, servers, privileged workstations)
- [ ] Document updated within last 12 months

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Number of documented endpoint threat scenarios covering ≥4 categories | ___ | ___ | ≥15 scenarios | ☐ | |
| % of AI endpoint security agents mapped to ≥3 specific threat scenarios and failure modes | ___ | ___ | 100% | ☐ | |
| % of endpoint types (corporate, BYOD, mobile, IoT, servers) with threat scenarios documented | ___ | ___ | ≥85% | ☐ | |
| % of AI endpoint actions (quarantines, isolations) causing unplanned business disruption | ___ | ___ | ≤1% | ☐ | |

**Metric Collection Guidance:**
- **Number of scenarios**: Count distinct threat scenarios in endpoint threat inventory; verify coverage across adversarial evasion, data poisoning, operational failures, supply chain, AI-generated threats, endpoint-specific threats; source from threat inventory document
- **% agents mapped**: Divide number of AI endpoint security agents with ≥3 linked threat scenarios by total AI endpoint security agents; source from threat model agent-to-scenario mapping table
- **% endpoint types covered**: Enumerate endpoint types in organizational inventory (Windows laptops, Mac, Linux, iOS/Android BYOD, IoT, servers, privileged workstations); divide types with at least one documented threat scenario by total types; source from endpoint type inventory cross-referenced with threat scenarios
- **% AI actions causing disruption**: Count AI endpoint actions (automated quarantine, isolation, process termination) per month from EDR management console; count those generating helpdesk escalation as unplanned disruption; formula: (disruptive actions / total AI actions) x 100; source from EDR action log and helpdesk ticket system

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

**Q1.2:** Do you have documented threat models for your HAI endpoint security operations, with identified threat owners responsible for tracking and mitigating each threat category?

**Evidence Required:**
- [ ] Formal threat model document for AI endpoint security operations
- [ ] Threat model covers: attack vectors, failure modes, adversarial risks, device diversity, remote/hybrid work considerations
- [ ] Each threat category has assigned owner (individual or team)
- [ ] Threat model includes impact assessment (ransomware outbreaks, undetected breaches, business disruption from false positives)
- [ ] Threat model reviewed and approved by security leadership and IT operations
- [ ] Threat model accessible to relevant teams (SOC, endpoint security, IT operations, helpdesk)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| % of endpoint threat categories with named owner assigned | ___ | ___ | 100% | ☐ | |
| % of threat scenarios with impact differentiated by endpoint criticality tier (critical/high/medium-low) | ___ | ___ | 100% | ☐ | |
| Number of relevant teams (SOC, endpoint security, IT ops, helpdesk) with confirmed threat model access | ___ | ___ | ≥4 teams | ☐ | |
| Days since endpoint threat model reviewed and approved by security leadership | ___ | ___ | ≤90 days | ☐ | |

**Metric Collection Guidance:**
- **% with owner**: Count threat categories in endpoint threat model; divide those with named owner (individual or team) by total categories; source from threat model ownership table
- **% tiered by endpoint criticality**: Audit each threat for presence of impact differentiation across endpoint tiers (critical: executive/admin/production servers vs. high: standard corporate vs. medium-low: BYOD/IoT); divide threats with tier differentiation by total threats
- **Teams with access**: Survey SOC, endpoint security, IT operations, and helpdesk; count teams confirming access and recent use of threat model; source from access log or survey responses
- **Days since review**: Extract from document approval metadata or review calendar; track against quarterly review schedule; alert if >90 days given rapid evolution of ransomware and EDR bypass techniques

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

**Q1.3:** Have you conducted threat awareness training for SOC analysts, endpoint security teams, IT operations, helpdesk, and business users on AI-specific threats to endpoint security operations within the last 90 days of AI EDR/XDR deployment?

**Evidence Required:**
- [ ] Training materials covering AI endpoint security threats
- [ ] Training delivered to at least 4 stakeholder groups:
  - SOC analysts & endpoint security teams (adversarial ML evasion, validation of AI detections, threat hunting beyond AI)
  - IT operations & helpdesk (recognizing AI actions, escalation procedures, balancing security/productivity)
  - Business users (why AI may disrupt work, behaviors triggering anomaly detection, reporting suspicious activity AI misses)
  - Executives & risk management (business impact of failures, cost-benefit analysis, governance requirements)
- [ ] Training includes real-world examples (adversarial ML research, ransomware bypassing AI, false positive business impacts)
- [ ] Training conducted within 90 days of AI endpoint security tool deployment
- [ ] Attendance records and training completion tracking

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| % of SOC analysts, IT operations, and endpoint security teams completing threat awareness training | ___ | ___ | ≥80% | ☐ | |
| % of trainees passing post-training knowledge assessment on endpoint threat scenarios (≥80% score) | ___ | ___ | ≥90% | ☐ | |
| % of AI endpoint monitoring on BYOD and remote worker devices complying with privacy requirements | ___ | ___ | 100% | ☐ | |
| Days from AI EDR/XDR deployment to initial threat awareness training delivery | ___ | ___ | ≤90 days | ☐ | |

**Metric Collection Guidance:**
- **% training completion**: Divide staff completing training by total staff in target roles (SOC, endpoint security, IT ops, helpdesk, representative business users); source from LMS attendance records
- **% passing assessment**: Post-training quiz minimum 10 questions covering EDR evasion, ransomware threats, false positive response, escalation procedures; divide passing scores (≥80%) by total completions; source from LMS gradebook
- **% BYOD/remote privacy compliance**: Audit AI monitoring configuration on BYOD and remote endpoints; verify privacy notice, consent collection, and monitoring scope comply with GDPR/CCPA/employee monitoring laws; divide compliant configurations by total BYOD/remote endpoint configurations; source from MDM/EDR configuration audit
- **Days to training delivery**: Calculate from EDR/XDR go-live to first training session; source from deployment records and training calendar

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
**Objective:** Quantify and prioritize AI endpoint security threats by business impact and likelihood

**Prerequisites:** ALL Level 1 questions must be "Fully Mature" to proceed to Level 2

### Question 4: Abuse Cases and Attack Trees

**Q2.1:** Have you developed detailed abuse cases and attack trees for each HAI agent performing endpoint security, showing how adversaries could exploit or degrade HAI endpoint security operations?

**Evidence Required:**
- [ ] At least 3-5 abuse cases documented per AI endpoint security agent
- [ ] Abuse cases include:
  - Attacker goal, attack path (step-by-step), prerequisites, impact, likelihood
- [ ] Attack trees showing multiple paths to endpoint compromise (e.g., "Ransomware deployment despite AI EDR" with branches)
- [ ] Specific examples documented:
  - Adversarial ransomware for AI EDR evasion (obfuscation techniques bypassing behavioral analytics)
  - Behavioral baseline poisoning for insider threat (gradual data exfiltration training AI to accept malicious patterns)
  - False positive disruption during critical business event
  - Living-off-the-Land attack exploiting AI whitelist (PowerShell, WMI, legitimate tools used maliciously)
  - AI endpoint security tool supply chain compromise
- [ ] Abuse cases validated by security team and shared with SOC/IT operations stakeholders

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Average number of abuse cases documented per AI endpoint security agent | ___ | ___ | ≥3 abuse cases | ☐ | |
| % of critical AI endpoint agents with attack trees covering ≥3 distinct compromise paths | ___ | ___ | 100% | ☐ | |
| % of advanced persistent threat and fileless malware test scenarios detected by AI EDR within 5 minutes | ___ | ___ | ≥90% | ☐ | |
| % of critical endpoint threats with documented and validated mitigation strategies | ___ | ___ | ≥85% | ☐ | |

**Metric Collection Guidance:**
- **Avg abuse cases per agent**: Count total documented endpoint abuse cases; divide by number of AI endpoint security agents (EDR, behavioral analytics, ransomware detection, automated response); source from abuse case registry
- **% with attack trees**: Audit each critical AI endpoint agent for attack tree with ≥3 branches (e.g., evade behavioral detection + poison baselines + exploit AI whitelist + compromise EDR platform); divide qualifying agents by total critical agents
- **APT and fileless malware detection**: Quarterly: run labeled test scenarios in lab environment (APT TTPs, fileless malware, LOTL execution); measure time to AI EDR detection; formula: (scenarios detected within 5 minutes / total test scenarios) x 100; source from lab test report
- **% threats with validated mitigations**: Count critical endpoint threats in risk matrix; divide those with at least one implemented and tested mitigation control by total critical threats; validate through quarterly adversarial test results

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

**Q2.2:** Have you assessed and prioritized AI endpoint security threats using a risk matrix (likelihood × impact), with documented mitigation strategies for high-priority threats and differentiation by endpoint criticality?

**Evidence Required:**
- [ ] Risk assessment framework with likelihood and impact criteria
- [ ] Each threat scenario assessed for:
  - Likelihood (High/Medium/Low based on attack technique documentation, tool availability, skill required)
  - Business impact differentiated by endpoint criticality:
    - Critical endpoints (executives, privileged admins, finance, production servers, PCI/HIPAA systems)
    - High endpoints (standard corporate devices, business-critical applications)
    - Medium/low endpoints (BYOD, guest devices, test systems, IoT)
- [ ] Risk matrix created (e.g., 3×3 or 5×5 grid)
- [ ] High-priority threats identified (High likelihood + Critical/High impact)
- [ ] Mitigation strategies documented for top 5-10 threats (enhanced PowerShell logging, multi-layered detection, backup monitoring, DLP)
- [ ] Risk assessment reviewed quarterly and updated based on ransomware intelligence, threat actor TTPs

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| AI EDR detection rate for LOTL attacks (PowerShell, WMI abuse) in quarterly behavioral bypass testing | ___ | ___ | ≥85% | ☐ | |
| Mean time to detect and contain endpoint threats on critical endpoints (minutes) | ___ | ___ | ≤5 minutes | ☐ | |
| % of offline devices scanned within 1 hour of network reconnection | ___ | ___ | ≥90% | ☐ | |
| % of high-priority endpoint threats with mitigations implemented within 90 days of identification | ___ | ___ | ≥80% | ☐ | |

**Metric Collection Guidance:**
- **LOTL detection rate**: Quarterly: red team executes LOTL attack scenarios (PowerShell-based reconnaissance, WMI lateral movement, certutil download, BITS transfer C2) against production AI behavioral analytics; formula: (LOTL scenarios generating alert / total LOTL scenarios executed) x 100; source from behavioral bypass test report
- **Mean time to detect and contain**: For each incident on critical endpoints (actual and simulated), measure time from attack initiation to AI detection alert AND from alert to automated containment; formula: sum of (detection time + containment time) / number of incidents; source from EDR incident timeline in management console
- **% offline devices scanned on reconnect**: Pull EDR reconnection events from management console; count devices triggering full scan within 60 minutes of reconnection; formula: (devices scanned within 1h / total reconnection events) x 100; source from EDR scan log
- **% mitigations implemented on time**: Track mitigation tickets for high-priority threats; divide those closed within 90 days of threat identification by total high-priority threat mitigations opened; source from issue tracker with threat identification date and closure date

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

**Q2.3:** Have you integrated threat intelligence from adversarial ML research, ransomware analysis, vulnerability databases, and AI EDR vendor advisories to continuously identify emerging threats to AI endpoint security, with annual validation of threat models?

**Evidence Required:**
- [ ] Threat intelligence sources identified and monitored:
  - Academic research (adversarial ML conferences, malware research, endpoint security bypass techniques)
  - Real-world exploits (CVE database for AI/ML libraries in EDR tools, ransomware analysis tracking evasion techniques)
  - Attack technique databases (MITRE ATT&CK endpoint techniques, MITRE ATLAS, LOLBAS project)
  - Vendor intelligence (CrowdStrike, SentinelOne, Microsoft Defender security bulletins and threat reports)
- [ ] Monitoring cadence established:
  - Daily: Ransomware intelligence feeds, critical CVEs affecting endpoint security tools
  - Weekly: Threat actor TTPs, MITRE ATT&CK updates, vendor security advisories
  - Monthly: Academic research papers, security conference proceedings
  - Quarterly: Threat model updates
- [ ] Threat intelligence findings documented in structured format (technique name, affected tools, ATT&CK mapping, references)
- [ ] Annual comprehensive threat model validation completed

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Number of distinct threat intelligence sources monitored (ransomware feeds, adversarial ML research, EDR vendor advisories, MITRE ATT&CK) | ___ | ___ | ≥10 sources | ☐ | |
| Days from new ransomware family or EDR bypass technique disclosure to threat model update | ___ | ___ | ≤14 days | ☐ | |
| % of endpoint security incidents predicted by threat model (attack vector was documented) | ___ | ___ | ≥80% | ☐ | |
| Number of threat model updates completed based on emerging ransomware intelligence in last 12 months | ___ | ___ | ≥4 (quarterly) | ☐ | |

**Metric Collection Guidance:**
- **Number of sources monitored**: Enumerate all active feeds: ransomware trackers (RansomWatch, ID Ransomware), MITRE ATT&CK, LOLBAS project, vendor threat reports (CrowdStrike, SentinelOne, Microsoft), CVE feeds for EDR dependencies, academic preprint servers; count distinct sources in intel register
- **Days to threat model update**: For each new ransomware family or EDR bypass technique in the wild, calculate days from first public disclosure (blog post, vendor advisory, CVE) to threat model update incorporating that technique; average across all actionable disclosures in quarter; source from threat model changelog vs. disclosure timestamps
- **% incidents predicted**: After each endpoint security incident or near-miss, check if attack vector matches a threat model entry; formula: (incidents with matching threat model entry / total incidents) x 100; review at annual validation using 12 months of incident data
- **Number of updates**: Count distinct threat model revision commits or versioned updates driven by ransomware intelligence in 12-month period; source from version control log with commit messages referencing ransomware intelligence

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

**Q3.1:** Do you conduct periodic (at least quarterly) adversarial testing and red team exercises against your HAI endpoint security agents to proactively identify weaknesses before attackers do?

**Evidence Required:**
- [ ] Quarterly adversarial testing program established covering:
  - AI EDR evasion testing (adversarial malware variants, >95% detection rate target)
  - Behavioral analytics bypass testing (LOTL attacks, insider threat scenarios, >85% detection target)
  - Ransomware simulation (detection within 60 seconds, containment before >5% file encryption)
  - Model drift monitoring (monthly testing against golden malware/behavior dataset, >95% accuracy maintained)
- [ ] Annual endpoint red team exercise:
  - Full adversarial simulation against AI EDR/XDR defenses
  - Attack goals: initial access, persistence, lateral movement, data exfiltration, maintain access 72+ hours undetected
  - 2-4 week duration with documented findings
- [ ] Purple team exercises (quarterly collaborative red/blue testing on specific attack categories)
- [ ] Test reports documenting:
  - Successful evasion techniques
  - AI EDR detection gaps by malware family or attack technique
  - Behavioral analytics blind spots (insider threats, LOTL attacks)
  - Time to detection for each attack phase
  - Recommendations for AI tuning, detection rules, SOC procedures

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| AI EDR detection rate for adversarial malware variants (obfuscated, polymorphic, AI-aware) in quarterly evasion testing | ___ | ___ | ≥95% | ☐ | |
| Ransomware detection and containment speed in semi-annual simulation (seconds to detection, % files encrypted before containment) | ___ | ___ | ≤60s detection; <5% files encrypted | ☐ | |
| % of red team endpoint attack scenarios successfully detected or blocked by AI EDR/XDR | ___ | ___ | ≥80% | ☐ | |
| AI EDR true positive rate on monthly golden dataset (model drift monitoring) | ___ | ___ | ≥95% with ≤5% drift | ☐ | |

**Metric Collection Guidance:**
- **EDR adversarial malware detection rate**: Quarterly: red team deploys adversarial malware variants (API-obfuscated ransomware, polymorphic info-stealers, AI-aware execution delays, process-hollowed payloads) in lab with production EDR; formula: (variants detected / total variants deployed) x 100; source from EDR evasion test report
- **Ransomware simulation speed**: Semi-annual: deploy ransomware simulator (RanSim, custom built) in isolated lab; measure (a) seconds from execution to first EDR alert and (b) % of test files encrypted before endpoint isolation; source from ransomware simulation test report with timestamp logs
- **Red team block rate**: Annual: red team executes full endpoint attack chain (phishing, execution, persistence, lateral movement, exfiltration); count attack phase objectives; formula: (objectives detected or blocked / total objectives) x 100; source from annual endpoint red team report
- **Golden dataset accuracy**: Monthly: run AI EDR against fixed dataset of 200-500 labeled samples (known malicious malware + known clean applications); formula: (true positives / (true positives + false negatives)) x 100; track trend month-over-month; alert if <90% or >5% month-over-month decline; source from monthly drift monitoring dashboard

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

**Q3.2:** Do you publish original threat research on AI endpoint security vulnerabilities through blog posts, conference presentations, responsible disclosures to AI EDR/XDR vendors, or contributions to endpoint security community knowledge?

**Evidence Required:**
- [ ] At least 2 public threat intelligence contributions per year
- [ ] Contributions include:
  - Blog posts on AI EDR bypass techniques, adversarial testing findings, ransomware evasion patterns
  - Conference presentations (Black Hat, DEF CON AI Village, security research forums)
  - Responsible vulnerability disclosures to AI endpoint security vendors (CrowdStrike, SentinelOne, Microsoft)
  - Research shared with endpoint security community (MITRE ATT&CK contributions, threat intelligence platforms)
  - Purple team exercise methodologies and findings
- [ ] Public evidence (published articles, conference proceedings, CVE assignments, vendor acknowledgments)
- [ ] Documented impact (vendor patches, detection improvements, industry awareness)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Number of public endpoint/EDR threat intelligence contributions published in last 12 months | ___ | ___ | ≥2 | ☐ | |
| Number of responsible disclosures to AI EDR/XDR vendors (CrowdStrike, SentinelOne, Microsoft) with acknowledged outcome | ___ | ___ | ≥1 | ☐ | |
| Number of novel AI EDR evasion techniques identified per year through testing before weaponization in the wild | ___ | ___ | ≥5 per year | ☐ | |
| Evidence of documented community impact (vendor patches, ATT&CK technique contributions, detection rule publications) | ___ | ___ | ≥1 impact | ☐ | |

**Metric Collection Guidance:**
- **Number of publications**: Count blog posts, technical papers, DEF CON/Black Hat talks, purple team methodology documents published with organization attribution in rolling 12 months; source from publication tracker
- **Responsible disclosures**: Count CVDs submitted to CrowdStrike, SentinelOne, Microsoft Defender, or other AI EDR vendors; count those receiving formal acknowledgment, product update, or CVE assignment; source from disclosure tracking log
- **Novel evasion techniques identified**: Count EDR bypass techniques discovered through quarterly adversarial testing that were not yet documented in MITRE ATT&CK, vendor advisories, or public research at time of discovery; verify by checking discovery date against first public documentation date; source from test reports and ATT&CK/LOLBAS comparison
- **Community impact evidence**: Collect vendor patch notes citing disclosure, CVE database entries, ATT&CK pull request merges, or Sigma/YARA rule publications referencing organization's research; source from public records

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

**Q3.3:** Do you maintain a continuous improvement program for AI endpoint security threat models, incorporating lessons learned from adversarial testing, real-world ransomware incidents, and emerging research, with evidence of threat model evolution over time?

**Evidence Required:**
- [ ] Documented process for updating threat models based on:
  - Adversarial testing results (quarterly EDR evasion tests, behavioral bypass tests, ransomware simulations)
  - Real-world endpoint incidents (ransomware outbreaks, undetected APT activity, false positive business disruptions)
  - Emerging research (adversarial ML techniques, new ransomware families, EDR bypass methods)
  - Vendor intelligence (AI EDR updates, detection improvements, newly identified blind spots)
- [ ] Historical record showing threat model evolution (12+ months)
- [ ] Examples of threat model updates triggering security improvements:
  - Enhanced detection rules after evasion testing
  - Multi-layered defense after ransomware simulation failures
  - LOTL attack monitoring after behavioral bypass findings
  - Purple team playbooks developed from red team exercises
- [ ] Feedback loop: Threat intelligence → Testing → Model update → Mitigation → Re-test
- [ ] Metrics tracked: # of new threats identified, % of threats mitigated, detection accuracy trends (precision/recall/F1), false positive/negative rates

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| % of endpoint threat model content updated annually based on new ransomware families or EDR bypass techniques | ___ | ___ | ≥20% | ☐ | |
| % of quarterly adversarial test findings resulting in documented AI EDR tuning or SOC procedure improvement | ___ | ___ | ≥80% | ☐ | |
| AI EDR false positive rate on monthly golden dataset (known-clean applications incorrectly flagged) | ___ | ___ | ≤5% | ☐ | |
| % of zero-day endpoint exploits detected by AI behavioral analytics in test scenarios despite no signature | ___ | ___ | ≥70% | ☐ | |

**Metric Collection Guidance:**
- **% model content updated**: Compare current endpoint threat model to 12-months-prior version; count threat scenarios, attack techniques, or mitigations added or substantially modified; formula: (changed items / total prior-version items) x 100; source from version control diff or document change log
- **% test findings actioned**: After each quarterly adversarial test (EDR evasion, behavioral bypass, ransomware simulation), count findings generating a tuning ticket (detection rule update, SOC playbook change, configuration adjustment); divide closed tickets within 60 days by total findings; source from issue tracker
- **False positive rate on golden dataset**: Monthly: run AI EDR against fixed dataset of known-clean applications (common software, admin tools, development environments); formula: (false positives / total known-clean samples) x 100; track trend; alert if >5%; source from monthly drift monitoring dashboard
- **Zero-day behavioral detection**: Quarterly: introduce novel zero-day-style exploit scenarios (no existing signatures, behavioral-only detection required) in lab; formula: (scenarios triggering behavioral alert / total novel scenarios) x 100; source from adversarial test report; validates behavioral analytics effectiveness independent of signature coverage

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

**TA-Endpoints Practice Score:** _______ / 3.0

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
- [ ] Adversarial manipulation & evasion (adversarial malware, behavioral mimicry, LOTL attacks, fileless malware, AI detection timing exploitation)
- [ ] Data poisoning and training corruption (behavioral baseline poisoning, false positive injection, telemetry manipulation)
- [ ] Operational security failures (false negatives missing ransomware/APT/insider threats, false positives causing business disruption, model drift, automated overreaction)
- [ ] Supply chain and tool compromise (compromised AI EDR platforms, malicious agent updates, model weight tampering)
- [ ] AI-generated threats (AI-generated polymorphic malware, AI-assisted phishing, automated exploitation, deepfake social engineering)
- [ ] Endpoint-specific threats (BYOD privacy exploitation, mobile MDM bypass, IoT device gaps, remote worker network evasion, ransomware with EDR-disabling capabilities)

**Adversarial Testing Coverage:**
- [ ] EDR evasion testing (adversarial malware variants, API obfuscation, in-memory execution, >95% detection target)
- [ ] Behavioral analytics bypass testing (LOTL attacks, insider threat scenarios, mimicry attacks, >85% detection target)
- [ ] Ransomware simulation (detection speed <60 seconds, containment before >5% encryption, automated response validation)
- [ ] Model drift detection (monthly testing against golden dataset, automated alerting when accuracy degrades >5%)
- [ ] Red team exercises (full attack simulation, initial access to lateral movement to data exfiltration, 72+ hour persistence test)
- [ ] Purple team collaboration (quarterly focused exercises, iterative improvement of AI detection and SOC response)

**Endpoint Criticality Differentiation:**
- [ ] Critical endpoints identified (executives, privileged admins, finance, production servers, PCI/HIPAA systems)
- [ ] High endpoints identified (standard corporate devices, business-critical applications)
- [ ] Medium/low endpoints identified (BYOD, guest devices, test systems, IoT)
- [ ] Risk assessment differentiated by endpoint tier (same threat has different impact based on endpoint criticality)
- [ ] Mitigation strategies prioritized for critical endpoint protection (immediate priority for ransomware detection, privilege account monitoring)

**Device Diversity Considerations:**
- [ ] Corporate laptops (Windows, Mac, Linux) included in threat scenarios
- [ ] BYOD mobile devices (iOS, Android) included with privacy considerations
- [ ] Remote/hybrid work devices addressed (outside network perimeter, home networks, offline gaps)
- [ ] IoT devices and resource-constrained endpoints considered
- [ ] Privileged admin workstations identified for enhanced monitoring
- [ ] Production servers and critical business systems covered

**Ransomware-Specific Coverage:**
- [ ] Adversarial ransomware techniques (AI-aware ransomware, slow encryption, selective targeting)
- [ ] Detection speed requirements (within 60 seconds of execution)
- [ ] Containment effectiveness (isolation before significant data loss)
- [ ] Backup integrity monitoring (preventing encryption of backups)
- [ ] Double extortion scenarios (data exfiltration before encryption)
- [ ] Ransomware with EDR-disabling capabilities (SafeMode boot, process termination, credential theft for console access)

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
**Next Review:** Quarterly or after significant HAI endpoint security changes
