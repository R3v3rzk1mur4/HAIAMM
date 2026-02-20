# Threat Assessment (TA) - Data Domain Assessment Questionnaire
## HAIAMM v3.0

**Version:** v3.0
**Scoring Model:** Evidence + Outcome Metrics (see Scoring Methodology below)

---

## Purpose

This questionnaire assesses organizational maturity in identifying and analyzing threats specific to HAI data security operations. It evaluates threat modeling, risk prioritization, threat intelligence monitoring, and adversarial testing practices for AI agents performing data discovery, classification, DLP, access monitoring, privacy compliance, and DSAR automation in the Data domain.

---

## Instructions

- Answer each question honestly based on current organizational practices
- Select "Yes" only if you have documented evidence of the practice
- Each question has two components: **Evidence** (what you did) and **Outcome Metrics** (how well it worked)
- **Scoring uses 4 tiers:** Fully Mature (1.0), Implemented (0.67), Partial (0.33), Not Implemented (0.0)
- **Baseline first** - Record current metric values before setting targets
- Provide specific evidence in the "Evidence Repository" section
- Calculate your maturity level using the scoring methodology at the end

---

## Level 1: Foundational (0-3 points)

### Question 1.1: AI-Specific Data Security Threat Scenarios

**Question:** Have you documented threat scenarios specific to AI agents performing data security operations (classification, DLP, access monitoring, privacy compliance)?

**Evidence Required:**
- [ ] Inventory of AI data security agents documented:
  - AI data discovery and classification tools (e.g., BigID, Varonis, Microsoft Purview, OneTrust)
  - AI-powered Data Loss Prevention (DLP) systems
  - AI access anomaly detection and monitoring
  - AI privacy compliance scanning (GDPR, CCPA, HIPAA)
  - AI-assisted Data Subject Access Request (DSAR) automation
  - AI encryption key management or data masking systems
  - AI database activity monitoring (DAM) tools

- [ ] **Adversarial manipulation & evasion threat scenarios** documented (minimum 3):
  - Adversarial data patterns for DLP evasion (steganography, encoding, fragmentation, protocol tunneling)
  - Data obfuscation for classification evasion (PII in images, encoded formats, non-standard schemas)
  - Prompt injection in AI privacy tools (manipulating AI compliance scanners, DSAR automation)
  - Model inversion attacks (extracting sensitive training data from classification models)
  - Access pattern mimicry to evade AI access anomaly detection
  - Slow data exfiltration below AI DLP thresholds

- [ ] **Data poisoning & training corruption threat scenarios** documented (minimum 2):
  - Classification model poisoning (injecting mislabeled data to corrupt AI classification)
  - DLP bypass training (feeding AI DLP with exfiltration patterns labeled as "legitimate")
  - Access baseline corruption (poisoning AI access monitoring baselines)

- [ ] **Operational security failure scenarios** documented (minimum 3):
  - False negative - catastrophic misclassification (AI marks PII database as "public")
  - False negative - missed data exfiltration (AI DLP fails to detect sophisticated theft)
  - False negative - undetected insider threat (authorized user stealing within permissions)
  - False positive - business disruption (AI DLP blocks legitimate data transfers)
  - Model drift - evolving data patterns degrading classification accuracy

- [ ] **Privacy violations by AI itself scenarios** documented (minimum 2):
  - AI training data privacy violations (AI trained on sensitive data without consent)
  - AI model data leakage (AI inadvertently exposes sensitive training data)
  - Excessive AI data access (overly broad permissions violating data minimization)
  - Cross-border data transfer violations (AI telemetry to vendors violating GDPR Chapter V)
  - Purpose limitation violations (AI data used for secondary purposes beyond security)

- [ ] **Regulatory & compliance threat scenarios** documented (minimum 2):
  - GDPR non-compliance (processing without legal basis, inadequate data subject rights)
  - CCPA/CPRA violations (failing to support consumer rights, selling data without consent)
  - HIPAA violations (accessing PHI without authorization, inadequate audit trails)
  - PCI-DSS violations (AI accessing cardholder data without proper segmentation)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| % of known AI data security attack vectors documented | ___ | ___ | ≥85% | ☐ | |
| # of documented threat scenarios across all categories | ___ | ___ | ≥15 scenarios | ☐ | |
| # of regulatory obligations mapped to AI data processing threats | ___ | ___ | 100% of applicable regulations | ☐ | |
| % of threat scenarios validated through PoC testing or PIA | ___ | ___ | ≥70% | ☐ | |

**Metric Collection Guidance:**
- **% of attack vectors documented**: Enumerate known attack vectors from MITRE ATLAS and OWASP ML Top 10; divide count of documented scenarios by total known vectors; assess quarterly
- **# of threat scenarios**: Count distinct documented scenarios; review threat document and count entries across all categories; assess at each document update
- **# of regulatory obligations mapped**: List all applicable regulations (GDPR, CCPA, HIPAA, PCI-DSS); count those with documented AI data processing threat scenarios; review annually or when regulations change
- **% PoC validated**: For each threat scenario, flag as validated if a proof-of-concept test or privacy impact assessment confirms exploitability; divide validated count by total scenario count; review quarterly

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### Question 1.2: Threat Awareness Training for Data Security Teams

**Question:** Have DPOs, data security teams, legal counsel, and leadership received training on threats unique to HAI data security and AI-related privacy risks?

**Evidence Required:**
- [ ] **Data Protection Officers & Privacy Teams** training delivered:
  - Adversarial ML techniques targeting AI data security (model inversion, membership inference, classification poisoning)
  - Privacy risks of AI data security tools themselves (AI training data, model data leakage, excessive access, cross-border transfers)
  - How to validate AI data classification accuracy (sampling methodology, privacy impact assessment for AI tools)
  - Regulatory implications of AI data processing (GDPR Article 22 automated decision-making, Article 35 DPIA requirements)
  - When to distrust AI privacy determinations (human review required for edge cases)
  - Data subject rights when AI processes personal data (right to explanation, right to object, right to human review)

- [ ] **Data Security Teams** training delivered:
  - How AI DLP can be evaded (adversarial data patterns, encoding, steganography, covert channels)
  - Validating AI data classification (sampling sensitive data, testing classification accuracy, identifying edge cases)
  - Supply chain risks in AI data security platforms (vendor access to classified data, model integrity, update validation)
  - Incident response for AI data security failures (mass misclassification, missed exfiltration, privacy breach by AI tool)
  - Balancing AI access to data vs. principle of least privilege

- [ ] **Database Administrators & IT Operations** training delivered:
  - What happens when AI data security tools make mistakes (over-classification blocking applications, misclassification exposing data)
  - How to recognize AI data security actions vs. application issues
  - Escalation procedures when AI disrupts business operations
  - Credential management for AI data security tools (privileged database access)

- [ ] **Legal Counsel & Compliance** training delivered:
  - Regulatory obligations for AI data processing (GDPR, CCPA, sector-specific regulations)
  - Liability for AI data security failures (who is responsible when AI misclassifies data)
  - Contractual requirements for AI data security vendors (data processing agreements, liability caps, breach notification)
  - Data subject rights implications (can individuals object to AI data processing, request human review)
  - Regulatory reporting for AI privacy incidents (GDPR Article 33/34 breach notification)

- [ ] Training completion tracked:
  - Target: ≥80% completion within 90 days of AI data security tool deployment
  - Training includes real-world examples (adversarial ML research, case studies, regulatory enforcement actions)
  - Training effectiveness validated (pre/post assessments, knowledge retention)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| % of DPOs, data security teams, DBAs, and legal counsel completing training | ___ | ___ | ≥80% within 90 days | ☐ | |
| % of DPOs passing post-training assessment (≥75% score) | ___ | ___ | ≥75% of DPOs | ☐ | |
| # of stakeholder groups receiving domain-specific training | ___ | ___ | ≥4 groups | ☐ | |
| Days from AI tool deployment to initial training completion | ___ | ___ | ≤90 days | ☐ | |

**Metric Collection Guidance:**
- **% training completion**: Divide number of staff who completed training by total required staff across all four groups; pull from LMS completion records; measure at 90-day mark
- **% DPOs passing assessment**: Administer standardized pre/post assessment; count DPOs scoring ≥75%; divide by total DPOs; measure after each training cohort
- **# of stakeholder groups**: Count distinct role groups that received tailored training content (DPOs, data security, DBAs, legal); confirm via training attendance records
- **Days to initial completion**: Record date of AI tool go-live and date first full training cohort completed; calculate difference; track per tool deployment

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### Question 1.3: AI Data Security Agent Inventory and Governance

**Question:** Is there an inventory mapping each AI data security agent to potential threat scenarios, failure modes, regulatory obligations, and data types processed?

**Evidence Required:**
- [ ] Comprehensive AI data security agent inventory:
  - Each AI data security tool documented (product name, vendor, deployment date, version)
  - Data security functions performed (data discovery, classification, DLP, access monitoring, privacy compliance, DSAR automation, encryption management, data masking)
  - Data types processed by each AI tool (PII, PHI, PCI, confidential, internal, public)
  - Data sources accessed (databases, file shares, cloud storage, SaaS applications, backups)
  - Regulatory scope (GDPR, CCPA, HIPAA, PCI-DSS, FERPA, SOX applicable)

- [ ] Each AI agent mapped to threat scenarios:
  - Minimum 3 threat scenarios per AI data security agent
  - Specific failure modes documented (false negatives, false positives, model drift, misclassification)
  - Adversarial exploitation scenarios (DLP evasion, classification bypass, access monitoring circumvention)
  - Privacy violation scenarios (data leakage by AI tool, cross-border transfers, excessive access)

- [ ] Privacy governance for AI data security tools documented:
  - Data Protection Impact Assessment (DPIA) completed for each AI data security tool (GDPR Article 35)
  - Legal basis for AI data processing documented (GDPR Article 6: legitimate interest, legal obligation, consent)
  - Data Processing Agreements (DPAs) with AI data security vendors
  - Cross-border data transfer mechanisms documented (Standard Contractual Clauses, adequacy decisions)
  - Purpose limitation documented (AI processes data only for stated security purposes)

- [ ] Executive awareness briefing delivered:
  - CISO/CPO/General Counsel briefed on AI-specific data protection threats
  - Regulatory compliance risks communicated (GDPR fines up to 4% revenue, CCPA violations, HIPAA penalties)
  - Business impact of AI data security failures discussed (breach costs, reputation damage, customer trust)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| % of AI data security agents with completed inventory entry (all fields) | ___ | ___ | 100% | ☐ | |
| % of AI data security agents with completed DPIA | ___ | ___ | 100% within 90 days of deployment | ☐ | |
| % of AI data security agents mapped to ≥3 threat scenarios | ___ | ___ | 100% | ☐ | |
| # of days from new AI tool deployment to inventory inclusion | ___ | ___ | ≤30 days | ☐ | |

**Metric Collection Guidance:**
- **% agents with complete inventory**: Audit inventory spreadsheet or CMDB; count agents with all required fields populated; divide by total AI security agents; review quarterly
- **% with completed DPIA**: Count DPIAs marked complete and approved by DPO; divide by total AI data security agents; pull from DPIA register; review quarterly
- **% mapped to ≥3 scenarios**: For each inventory entry, count linked threat scenarios; flag entries with fewer than 3; divide compliant count by total; review at each inventory update
- **Days to inventory inclusion**: Record go-live date and date of inventory entry creation for each new tool; calculate difference; track as part of AI tool onboarding checklist

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

## Level 2: Comprehensive (4-6 points)

### Question 2.1: Detailed Abuse Cases for AI Data Security Exploitation

**Question:** Have you developed detailed abuse cases showing how adversaries could exploit or bypass AI data security defenses (misclassification, DLP evasion, insider baseline poisoning, model inversion)?

**Evidence Required:**
- [ ] Minimum 3-5 abuse cases per critical AI data security agent documented:
  - Each abuse case includes: Attacker Goal, Attack Path (step-by-step), Prerequisites, Impact, Likelihood
  - Abuse cases cover diverse threat scenarios (not just external attackers - include insider threats, supply chain, AI tool failures)

- [ ] **Classification Model Poisoning abuse case** documented:
  - Attack path: Compromised account → inject mislabeled training data → AI learns incorrect patterns → systematic misclassification → mass data exposure
  - Prerequisites: Access to AI classification administration, knowledge of training process
  - Impact: Critical (mass data breach, regulatory fines, customer lawsuits)
  - Likelihood assessment: Medium (requires privileged access but high-value target)

- [ ] **Adversarial DLP Evasion abuse case** documented:
  - Attack path: Compromised account/insider → research AI DLP detection patterns → develop evasion techniques (steganography, encoding, fragmentation) → slowly exfiltrate sensitive data undetected
  - Prerequisites: Access to sensitive data, technical skill for evasion, patience
  - Impact: Critical (IP theft, customer data breach, regulatory penalties)
  - Likelihood assessment: Medium-High (evasion techniques are public, AI DLP has known limitations)

- [ ] **Insider Threat Baseline Poisoning abuse case** documented:
  - Attack path: Legitimate access → gradually increase data access to poison AI baseline → AI learns elevated access is "normal" → exfiltrate at "normal" rate undetected
  - Prerequisites: Legitimate data access, patience (weeks/months), knowledge of AI baselines
  - Impact: Critical (insider data theft, customer breach, competitive damage)
  - Likelihood assessment: Medium-High (insider threats common, baseline poisoning intuitive)

- [ ] **Model Inversion / Privacy Attack abuse case** documented:
  - Attack path: API access → thousands of classification queries → analyze responses to infer training data properties → reconstruct sensitive PII from training set
  - Prerequisites: API access, ML expertise, computational resources
  - Impact: High (privacy violation, GDPR breach, AI tool leaked data it was supposed to protect)
  - Likelihood assessment: Medium (model inversion is academic research, requires expertise)

- [ ] **Privacy Violation by AI Tool abuse case** documented:
  - Attack path: Deploy AI classification platform → AI scans sensitive data → AI transmits telemetry/training data to vendor across borders → violates GDPR Chapter V → regulatory penalty
  - Prerequisites: AI vendor with cross-border processing, inadequate contractual safeguards
  - Impact: Critical (GDPR violation up to 4% revenue, breach notification required)
  - Likelihood assessment: Medium (many AI vendors have cross-border processing)

- [ ] Attack trees developed showing multiple paths to data breach:
  - Root goal: "Exfiltrate customer PII despite AI DLP"
  - Branches: Evade DLP detection, corrupt data classification, exploit model inversion, compromise AI tool, exploit insider access within baseline

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| % of critical AI data security agents with ≥3 documented abuse cases | ___ | ___ | 100% | ☐ | |
| AI data classification misclassification rate (false negative rate) | ___ | ___ | ≤5% | ☐ | |
| % of abuse cases differentiated by data sensitivity tier (PII vs. confidential vs. internal) | ___ | ___ | 100% | ☐ | |
| # of days to implement mitigations for Critical/High abuse case findings | ___ | ___ | ≤90 days | ☐ | |

**Metric Collection Guidance:**
- **% agents with ≥3 abuse cases**: Count abuse cases per agent in threat model documentation; flag any with fewer than 3; divide compliant count by total critical agents; review quarterly
- **Misclassification rate**: Run quarterly classification accuracy test against 500-1,000 sample dataset with known ground truth; calculate false negative rate (sensitive data missed / total sensitive data); formula: FNR = FN / (FN + TP)
- **% abuse cases differentiated by sensitivity**: Review each abuse case for explicit data sensitivity tier annotation; count fully annotated cases; divide by total abuse cases; review at each threat model update
- **Days to mitigation**: Record date of abuse case documented and date mitigation deployed; calculate mean across all Critical/High findings; track via vulnerability/risk management tool

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### Question 2.2: Risk-Prioritized Threat Assessment with Mitigation Strategies

**Question:** Are AI data security threats prioritized by risk (likelihood × business impact × regulatory consequence) with documented mitigation strategies for high-priority threats?

**Evidence Required:**
- [ ] Likelihood assessment framework defined:
  - **High Likelihood**: Attack technique publicly documented, tools available, low-moderate skill required (e.g., insider threat baseline poisoning)
  - **Medium Likelihood**: Moderate-advanced skill required, technique known but requires customization (e.g., adversarial DLP evasion)
  - **Low Likelihood**: Advanced attack requiring significant skill/resources, theoretical or nation-state level (e.g., sophisticated model inversion)

- [ ] Impact assessment framework by data sensitivity tier:
  - **Restricted/Regulated Data (PII, PHI, PCI, Trade Secrets)**:
    - Critical: Mass data breach, regulatory fines >$1M (GDPR 4% revenue, HIPAA $1.5M/year), class action lawsuits
    - High: Limited exposure (<1,000 records), regulatory investigation, customer notification
    - Medium: Near-miss detected before exposure, internal remediation
  - **Confidential/Internal Data**:
    - Critical: IP theft, competitive damage, employee data breach, business disruption
    - High: Internal data exposure, limited business impact
  - **Public Data**: Low impact for exposure (already public), but misclassification can disrupt business

- [ ] Regulatory impact multiplier documented:
  - GDPR violations: 2-4% global annual revenue (€20M or 4% whichever higher)
  - CCPA violations: $2,500-$7,500 per violation
  - HIPAA violations: $100-$50,000 per violation, up to $1.5M annual maximum
  - PCI-DSS violations: Fines, increased transaction fees, loss of payment processing

- [ ] Risk prioritization matrix created:
  - Each threat scenario scored: Likelihood (1-3) × Impact (1-3) × Regulatory Risk (0-3) = Risk Score (1-9+)
  - Priority levels assigned: Immediate (score 8-9+), High (score 5-7), Medium (score 2-4), Low (score 0-1)
  - Example high-priority threats identified:
    - Classification model poisoning (Medium likelihood × Critical impact × GDPR/CCPA = Immediate)
    - False negative - missed data exfiltration (High likelihood × Critical impact × Regulatory risk = Immediate)
    - Insider threat baseline poisoning (Medium-High likelihood × Critical impact × GDPR/CCPA = Immediate)

- [ ] Mitigation strategies documented for "Immediate" and "High" priority threats:
  - **For "Classification model poisoning"**: Immutable training data controls, change management for classification rules, human validation sampling, classification audit trails, separation of duties
  - **For "Adversarial DLP evasion"**: Multi-layered DLP (AI + signature + heuristic + network forensics), encrypted traffic inspection, UEBA, data watermarking
  - **For "Insider threat baseline poisoning"**: Hard thresholds on data access (not just baselines), peer group comparison analytics, privileged access management (PAM), data exfiltration alerts independent of baselines
  - **For "AI tool privacy violations"**: Vendor privacy due diligence, Data Processing Agreements (DPAs), on-premise AI deployment for highest sensitivity data, model training data residency controls

- [ ] Evidence of mitigation implementation:
  - AI classification validation procedures implemented
  - DLP tuning and multi-layered detection deployed
  - Compensating controls for high-risk scenarios
  - Privacy safeguards documented (DPIAs, DPAs, data residency controls)

- [ ] Quarterly threat model reviews:
  - Threat model updated based on observed incidents, near-misses, regulatory enforcement actions, vendor advisories
  - Risk scores re-evaluated as threat landscape evolves
  - New threats added, obsolete threats removed

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| % of "Immediate" and "High" priority threats with implemented mitigations | ___ | ___ | ≥80% within 90 days | ☐ | |
| AI DLP detection rate for adversarial evasion techniques (quarterly test) | ___ | ___ | ≥85% | ☐ | |
| $ amount of regulatory fines related to AI data security failures | ___ | ___ | $0 | ☐ | |
| # of threat model updates per quarter incorporating new intelligence | ___ | ___ | ≥5 updates per quarter | ☐ | |

**Metric Collection Guidance:**
- **% mitigations implemented**: Count Immediate/High threats with at least one implemented mitigation control in production; divide by total Immediate/High threats; track via risk register; review quarterly
- **DLP evasion detection rate**: Conduct quarterly red team DLP evasion test using standard evasion techniques (steganography, encoding, fragmentation); count detected attempts / total attempts; formula: detection rate = detected / total × 100
- **$ regulatory fines**: Query legal/compliance records for any regulatory fines or settlements related to AI data security; $0 target means zero fines; track annually and upon any regulatory action
- **# threat model updates**: Count discrete threat model change records (new threat added, risk score changed, mitigation added) per quarter; maintain changelog in threat model document

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### Question 2.3: Data Sensitivity Differentiation and Regulatory Compliance

**Question:** Do you differentiate threat risk assessment based on data sensitivity (restricted/PII/PHI vs. confidential vs. internal vs. public) and regulatory applicability (GDPR, CCPA, HIPAA, PCI-DSS)?

**Evidence Required:**
- [ ] Data sensitivity classification scheme defined:
  - **Restricted/Regulated**: PII (GDPR/CCPA), PHI (HIPAA), PCI (cardholder data), Trade Secrets, Financial Data (SOX)
  - **Confidential**: Business confidential, employee data (non-PII), internal financial data, contracts, M&A data
  - **Internal**: Internal-only business data, non-sensitive employee info, operational data
  - **Public**: Publicly available data, marketing materials, published reports

- [ ] Threat risk assessment differentiated by data sensitivity:
  - Restricted/Regulated data threats prioritized highest (highest impact, regulatory fines)
  - Confidential data threats assessed for business impact (IP theft, competitive damage)
  - Internal/Public data threats assessed for business disruption (over-classification blocking operations)
  - Risk scoring adjusted by data sensitivity: Same threat scenario has different risk scores for PII vs. internal data

- [ ] Regulatory applicability mapped to AI data security operations:
  - **GDPR (if processing EU personal data)**:
    - Article 6: Legal basis for AI data processing documented
    - Article 22: Automated decision-making and right to human review
    - Article 25: Privacy-by-design and privacy-by-default requirements
    - Article 35: DPIA (Data Protection Impact Assessment) completed for AI data security tools
    - Chapter V: Cross-border data transfer mechanisms (SCCs, adequacy decisions)
  - **CCPA/CPRA (if processing California consumer data)**:
    - Consumer rights support (access, deletion, opt-out)
    - Automated decision-making opt-outs
    - Do-not-sell obligations
  - **HIPAA (if processing protected health information)**:
    - Administrative, physical, technical safeguards for AI processing PHI
    - Business Associate Agreements (BAAs) with AI vendors
    - Minimum necessary access for AI agents
  - **PCI-DSS (if processing cardholder data)**:
    - Cardholder data environment (CDE) segmentation from AI tools
    - Encryption and access controls for AI accessing payment data
    - Audit logging and monitoring requirements

- [ ] Regulatory compliance documentation:
  - DPIA completed for AI data processing (GDPR Article 35)
  - Legal basis documented for each AI data security tool (legitimate interest, legal obligation, consent)
  - Data subject rights procedures (access, deletion, portability, objection, human review)
  - Data Processing Agreements (DPAs) with AI data security vendors
  - Cross-border transfer compliance (SCCs, adequacy decisions, data localization)

- [ ] Cascading regulatory impact analysis:
  - Recognition that single data breach can trigger multiple regulatory violations simultaneously (e.g., GDPR + CCPA + HIPAA for healthcare data of California EU residents)
  - Combined regulatory fines quantified in risk assessment
  - Multi-jurisdictional litigation risk assessed

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| % of data sensitivity tiers with distinct threat risk scores for the same scenario | ___ | ___ | 100% (all 4 tiers differentiated) | ☐ | |
| % of applicable regulations (GDPR, CCPA, HIPAA, PCI-DSS) with documented AI processing obligations | ___ | ___ | 100% of applicable regulations | ☐ | |
| % of data subject rights request types (access, deletion, portability, objection) tested and validated | ___ | ___ | 100% | ☐ | |
| # of AI data security agents with completed DPAs with their vendors | ___ | ___ | 100% of agents with data processor vendors | ☐ | |

**Metric Collection Guidance:**
- **% sensitivity tiers differentiated**: For each threat scenario, check if risk score matrix has distinct rows per sensitivity tier; count scenarios with all 4 tiers differentiated; divide by total scenarios; review at each threat model update
- **% regulations with documented obligations**: List applicable regulations; for each, check if AI processing obligations are mapped to specific threat scenarios; count mapped regulations / total applicable; review annually
- **% DSR types tested**: Maintain test log of data subject rights tests (DSAR fulfillment, deletion verification, portability export, objection processing); count types tested / 4 total types; run tests semi-annually
- **% agents with DPAs**: Audit vendor contract register for each AI data security agent's vendor; confirm executed DPA exists; count compliant agents / total agents with external vendors; review quarterly

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

## Level 3: Industry-Leading (7-9 points)

### Question 3.1: Active Threat Intelligence Monitoring for AI Data Security

**Question:** Do you actively monitor adversarial ML research, privacy/compliance guidance, regulatory enforcement actions, and vulnerability databases for emerging threats to AI data security tools?

**Evidence Required:**
- [ ] **Academic research monitoring** (theoretical attacks):
  - Adversarial ML conferences: NeurIPS, ICML, ICLR papers on model inversion, membership inference, classification poisoning
  - Security & privacy research: IEEE Security & Privacy, USENIX Security, Privacy Enhancing Technologies Symposium (PETS)
  - Data privacy research: IAPP research on AI privacy implications, regulatory guidance
  - ML privacy techniques: Differential privacy, federated learning, secure multi-party computation research
  - Frequency: Monthly review of academic publications

- [ ] **Real-world exploits & breach intelligence monitoring**:
  - CVE Database: Monitor CVEs for AI/ML libraries in data security tools, data classification platforms, DLP systems
  - Data breach disclosures: Analyze breaches caused by or enabled by AI security tool failures
  - Regulatory enforcement actions: GDPR fines, CCPA actions, HIPAA settlements related to inadequate AI data protection
  - AI privacy incidents database: Track incidents where AI systems caused data exposure or privacy violations
  - Frequency: Daily for critical CVEs and major breaches, weekly for breach analysis

- [ ] **Regulatory & compliance intelligence monitoring**:
  - GDPR guidance: European Data Protection Board (EDPB) guidelines on AI processing, automated decision-making
  - CCPA/CPRA updates: California Privacy Protection Agency (CPPA) regulations
  - HIPAA AI guidance: HHS Office for Civil Rights guidance on AI in healthcare
  - PCI DSS updates: PCI Security Standards Council guidance on AI for cardholder data protection
  - EU AI Act: Provisions affecting AI data security systems
  - Supervisory authority decisions: National DPA decisions on AI data processing legality
  - Frequency: Weekly for regulatory updates, monthly for guidance documents

- [ ] **Attack technique database monitoring**:
  - MITRE ATLAS: Adversarial attacks against AI systems (evasion, poisoning, model theft, privacy violations)
  - OWASP ML Top 10: Vulnerabilities in machine learning applications
  - Privacy attack research: Model inversion, membership inference, data reconstruction attacks
  - DLP evasion techniques: Security research on bypassing data loss prevention
  - Frequency: Monthly review and quarterly threat model updates

- [ ] **Industry & vendor intelligence monitoring**:
  - AI data security vendor research: Vendor blog posts on emerging threats, detection improvements
  - Vendor security advisories: Vulnerability disclosures, updates, best practices
  - Privacy technology vendor research: AI privacy tool vulnerabilities and updates
  - Data protection communities: IAPP, CSA Privacy working groups, industry-specific forums
  - Peer networks: Information sharing with peer organizations on AI data security failures
  - Frequency: Weekly vendor advisories, monthly community engagement

- [ ] Monitoring cadence established:
  - **Daily**: Critical CVEs affecting AI data security tools, major data breach disclosures, regulatory enforcement actions
  - **Weekly**: Privacy regulatory updates, vendor security advisories, data breach analysis
  - **Monthly**: Academic research papers, AI privacy conference proceedings, regulatory guidance updates
  - **Quarterly**: Update threat models with new techniques, reassess risk priorities, DPO/security team training on emerging threats
  - **Annually**: Comprehensive threat landscape review, regulatory landscape assessment, vendor privacy due diligence refresh

- [ ] Threat intelligence backlog maintained:
  - Emerging threats documented in structured format (attack technique, affected tools, regulatory implications, prerequisites, observed in wild, mitigation recommendations)
  - Intelligence findings integrated into threat model quarterly updates
  - Findings shared with data security roadmap and regulatory compliance planning

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| # of threat intelligence sources actively monitored | ___ | ___ | ≥25 sources | ☐ | |
| # of days from regulatory guidance publication to incorporation in threat model | ___ | ___ | ≤14 days | ☐ | |
| % of data security threats documented before public exploit or regulatory enforcement action | ___ | ___ | ≥25% proactively identified | ☐ | |
| % of quarterly threat model updates completed on schedule | ___ | ___ | 100% (4 of 4 per year) | ☐ | |

**Metric Collection Guidance:**
- **# of sources monitored**: Maintain a threat intelligence source registry listing each monitored source, type (academic/regulatory/vendor/community), and monitoring frequency; count entries; review quarterly
- **Days to incorporation**: For each regulatory guidance publication (EDPB, CPPA, HHS), record publication date and date incorporated into threat model; calculate mean; track via changelog
- **% proactively identified**: After any public exploit or enforcement action, check if threat was pre-existing in threat model; count proactively documented threats / total threats at year end; calculate annually
- **% quarterly updates on schedule**: Track quarterly threat model review dates against planned schedule; count completed on-time reviews / 4 planned reviews per year; track in project management system

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### Question 3.2: Periodic Adversarial Testing Against AI Data Security Agents

**Question:** Do you conduct periodic adversarial testing (classification accuracy validation, DLP evasion tests, privacy attack testing, data security red team exercises) against AI data security agents?

**Evidence Required:**
- [ ] **Quarterly AI Data Classification Accuracy Testing** implemented:
  - Test dataset: 500-1,000 data samples with known ground truth classification (PII, PHI, PCI, confidential, public)
  - Edge cases included: PII in unusual formats, sensitive data in images/audio, encrypted data, obfuscated data, novel schemas
  - Diverse data sources tested: Log files, screenshots, archived data, cloud storage, SaaS applications, databases, file shares
  - Accuracy metrics measured: Precision ≥95%, Recall ≥95%, F1 score
  - Misclassification patterns documented (false negatives, false positives)
  - Success criteria: ≥95% precision and ≥95% recall; if <95%, retrain model or add compensating controls
  - Output: Classification accuracy report with edge cases AI struggles with, retraining recommendations

- [ ] **Quarterly AI DLP Evasion Testing** implemented:
  - Red team attempts data exfiltration using evasion techniques:
    - Steganography (data hidden in images, audio, video)
    - Encoding (Base64, ROT13, encryption)
    - Fragmentation (small chunks below AI thresholds)
    - Protocol tunneling (DNS, ICMP, custom protocols)
    - Encrypted channels (personal VPN, cloud storage)
    - API exfiltration (GraphQL, custom APIs AI doesn't monitor)
  - Test sensitive data exfiltrated (not real customer data, controlled environment)
  - Detection rate measured across all evasion methods
  - Success criteria: AI DLP detects ≥90% of exfiltration attempts; if <90%, enhance with network forensics, encrypted traffic inspection, UEBA
  - Output: DLP evasion test report with undetected methods, detection gaps, mitigation recommendations

- [ ] **Semi-Annual Model Inversion & Privacy Attack Testing** implemented:
  - Model inversion testing: Query AI classification API to attempt reconstruction of training data
  - Membership inference testing: Determine if specific sensitive records were in training dataset
  - Information leakage measurement: What sensitive data can be extracted without direct database access
  - Comparison: Deliberately vulnerable model (no privacy protections) vs. production model (differential privacy, k-anonymity)
  - Success criteria: Production AI model leaks <1% of training data information; if >1%, implement differential privacy, federated learning, or restrictive API access controls
  - Output: Privacy attack testing report with information leakage quantification, model privacy improvements, regulatory compliance implications (GDPR Article 25)

- [ ] **Annual Data Security Red Team Exercise** implemented:
  - Full adversarial simulation: Red team attempts to exfiltrate sensitive data despite AI data security defenses
  - Real-world attacker TTPs used (insider threat, credential theft, DLP evasion, classification exploitation)
  - Attack goals:
    - Identify and exfiltrate customer PII (>1,000 records) despite AI DLP
    - Exploit AI data misclassification to access restricted data
    - Poison AI classification to create persistent backdoor
    - Maintain unauthorized data access for 30+ days undetected by AI access monitoring
  - Duration: 2-4 weeks with rules of engagement (no actual exfiltration of real customer data, use synthetic/test data, no production disruption)
  - Output: Red team report documenting successful techniques, AI detection gaps, classification vulnerabilities, prioritized remediation roadmap

- [ ] Adversarial testing results drive improvements:
  - Findings shared with AI data security vendors (responsible disclosure)
  - Work with vendors to patch vulnerabilities, improve classification models, implement privacy-enhancing technologies
  - Threat models updated based on testing insights
  - DLP policies refined, classification accuracy enhanced, regulatory compliance strengthened

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| AI data classification precision and recall on quarterly test dataset | ___ | ___ | ≥95% precision AND ≥95% recall | ☐ | |
| AI DLP detection rate for adversarial exfiltration attempts (quarterly test) | ___ | ___ | ≥90% | ☐ | |
| % of training data information leaked in semi-annual model inversion test | ___ | ___ | <1% | ☐ | |
| % of annual red team data exfiltration attempts blocked by AI defenses | ___ | ___ | ≥85% | ☐ | |

**Metric Collection Guidance:**
- **Classification precision and recall**: Run quarterly test against labeled 500-1,000 sample dataset; compute precision = TP / (TP + FP); compute recall = TP / (TP + FN); both must meet ≥95% threshold; track trends over time
- **DLP detection rate**: During quarterly evasion test, count total exfiltration attempt methods tested and number detected by AI DLP; formula: detection rate = detected / total attempted methods × 100
- **% training data leaked**: During semi-annual privacy attack test, measure information leakage using reconstruction accuracy or membership inference AUC; compare against randomized baseline; report % above baseline leakage
- **% red team attempts blocked**: During annual red team exercise, count total attack scenarios executed and number detected and blocked before data exposure; formula: block rate = blocked / total × 100

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### Question 3.3: Model Drift Monitoring and Regulatory Compliance Validation

**Question:** Is there a process to detect and respond to model drift (degraded AI classification accuracy over time) and validate ongoing regulatory compliance (DPIA updates, data subject rights testing)?

**Evidence Required:**
- [ ] **Model Drift Monitoring** implemented:
  - "Golden dataset" maintained: 500-1,000 data samples with validated ground truth classification
  - Golden dataset updated quarterly with new data types, business data patterns
  - Monthly classification accuracy testing: AI classifies golden dataset, precision/recall measured
  - Trend analysis: Monitor classification accuracy over time for degradation
  - Environmental change monitoring: New business applications, regulatory changes (new data types considered PII), schema migrations
  - Alert threshold: Classification accuracy degrades >5% from baseline triggers investigation
  - Success criteria: Maintain ≥95% classification accuracy on golden dataset; if degrades, investigate drift causes and initiate model retraining
  - Output: Monthly classification accuracy dashboard, drift alerts with root cause analysis, retraining recommendations

- [ ] **Model drift response process** established:
  - Drift investigation: Identify root causes (new data types, schema changes, business process evolution, regulatory changes)
  - Model retraining: Update training data, retrain classification models, validate accuracy improvements
  - Compensating controls: If retraining delayed, implement temporary controls (manual review, rule-based classification for edge cases)
  - Change management: Document drift causes, retraining activities, accuracy improvements
  - Stakeholder communication: Notify DPO, data security team, business units of classification accuracy changes

- [ ] **Regulatory Compliance Validation Program** implemented:
  - **GDPR Article 35 DPIA (Data Protection Impact Assessment)**:
    - DPIA completed for each AI data security tool processing personal data
    - DPIA refreshed annually or when AI processing changes significantly
    - DPIA documents: Nature/scope/context of processing, necessity/proportionality, risks to data subjects, mitigation measures
  - **Data Subject Rights Testing** (GDPR Articles 15-22, CCPA consumer rights):
    - Validate AI can support DSAR (Data Subject Access Request) - locate all personal data within 30 days (GDPR) or 45 days (CCPA)
    - Test right to deletion: AI can identify and delete all personal data across systems
    - Test right to portability: AI can export personal data in structured, machine-readable format
    - Test right to object: AI respects objections to automated processing
    - Test right to human review: Process for human review of AI data classification/access decisions
    - Success criteria: ≥95% of data subject rights requests fulfilled within regulatory timeframes
  - **Cross-Border Transfer Compliance**:
    - Verify AI data processing respects data localization requirements (GDPR Chapter V, CCPA, sector-specific)
    - Transfer mechanisms validated (Standard Contractual Clauses, adequacy decisions, Binding Corporate Rules)
    - AI model training data residency controls documented
    - AI vendor telemetry and cross-border data flows mapped and compliant
  - **Purpose Limitation Testing**:
    - Validate AI data security processes data only for stated security purposes
    - Test that AI data is not repurposed (employee monitoring without consent, business analytics, marketing)
    - Purpose limitation controls audited annually
  - **Legal Basis Validation** (GDPR Article 6):
    - Legal basis documented for each AI data processing activity (legitimate interest, legal obligation, consent)
    - Legitimate Interest Assessments (LIA) completed where applicable
    - Consent mechanisms validated (if consent is legal basis)
    - Legal basis reviewed annually or when AI processing changes

- [ ] **Privacy-Preserving AI Techniques** implemented for highest sensitivity data:
  - Differential privacy: Adding noise to datasets to protect individual privacy while preserving statistical utility
  - Federated learning: Training AI models on distributed data without centralizing sensitive data
  - Secure multi-party computation (SMPC): Collaborative data analysis without revealing individual inputs
  - Homomorphic encryption: Performing computations on encrypted data without decryption (if feasible)
  - K-anonymity or pseudonymization for training data

- [ ] Continuous compliance improvement:
  - Quarterly privacy training program reviews with DPO
  - Privacy training strategy informed by regulatory trends and incident learning
  - Regulatory compliance findings integrated into data security roadmap
  - Regulatory audit preparation: Evidence collection systems, compliance dashboards, automated reporting

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Hours to detect AI classification accuracy degradation >5% from baseline | ___ | ___ | ≤72 hours | ☐ | |
| % of data subject rights requests fulfilled within regulatory timeframes (GDPR 30 days / CCPA 45 days) | ___ | ___ | ≥95% | ☐ | |
| # of privacy-preserving AI techniques implemented for highest-sensitivity data | ___ | ___ | ≥3 techniques | ☐ | |
| YoY change in AI classification accuracy on golden dataset (trend) | ___ | ___ | 0% or positive (no degradation year-over-year) | ☐ | |

**Metric Collection Guidance:**
- **Hours to detect drift**: When drift alert fires (>5% accuracy drop), record timestamp of first alert vs. timestamp of accuracy drop onset (estimated from golden dataset test history); calculate mean detection lag in hours; track per drift event
- **% DSR requests fulfilled on time**: Log all data subject rights requests with received date and fulfillment date; count fulfilled within regulatory deadline / total requests; calculate monthly; formula: fulfillment rate = on-time / total × 100
- **# privacy-preserving techniques**: Inventory implemented techniques (differential privacy, federated learning, SMPC, homomorphic encryption, k-anonymity, pseudonymization); count distinct techniques in production; audit quarterly
- **YoY accuracy trend**: Compare annual average precision/recall from monthly golden dataset tests against prior year average; positive or zero = no degradation; negative = drift trend requiring investigation

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

## Evidence Repository

| Question | Evidence Description | Location/Link | Date |
|----------|---------------------|---------------|------|
| 1.1 | AI data security threat scenario documentation | | |
| 1.1 | Inventory of AI data security agents | | |
| 1.2 | Threat awareness training materials and completion records | | |
| 1.3 | AI data security agent inventory with threat mapping | | |
| 1.3 | DPIAs for AI data security tools | | |
| 2.1 | Abuse cases and attack trees documentation | | |
| 2.2 | Risk prioritization matrix | | |
| 2.2 | Mitigation strategies for high-priority threats | | |
| 2.3 | Data sensitivity classification scheme | | |
| 2.3 | Regulatory compliance documentation (DPIAs, DPAs, legal basis) | | |
| 3.1 | Threat intelligence monitoring subscriptions and reports | | |
| 3.2 | Adversarial testing reports (classification accuracy, DLP evasion, privacy attacks, red team) | | |
| 3.3 | Model drift monitoring dashboard | | |
| 3.3 | Regulatory compliance validation reports (DPIA updates, data subject rights testing) | | |

---

## Assessment Summary

**Assessment Date:** _____________________

**Assessor Name:** _____________________

**Organization/Team:** _____________________

**Current Maturity Level:** _____________________

### Strengths
___________________________________________________________________
___________________________________________________________________
___________________________________________________________________

### Gaps
___________________________________________________________________
___________________________________________________________________
___________________________________________________________________

### Recommended Improvements
___________________________________________________________________
___________________________________________________________________
___________________________________________________________________

### Next Assessment Date:** _____________________

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

L1_score = (Q1.1_score + Q1.2_score + Q1.3_score) / 3
L2_score = (Q2.1_score + Q2.2_score + Q2.3_score) / 3 × (L1_score if L1_score ≥ 1.0, else 0)
L3_score = (Q3.1_score + Q3.2_score + Q3.3_score) / 3 × (L2_score if L2_score ≥ 1.0, else 0)

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

## Data Domain-Specific Notes

### AI-Specific Threat Surface for Data Security

AI agents performing data security introduce novel threats beyond traditional data protection:
- **Adversarial ML Attacks**: Model inversion, membership inference, classification poisoning, DLP evasion
- **Operational Failures**: False negatives (missed exfiltration), false positives (business disruption), model drift
- **Privacy Violations by AI Tools**: AI training data privacy, model data leakage, excessive access, cross-border transfers
- **Regulatory Complexity**: GDPR, CCPA, HIPAA, PCI-DSS each with different AI implications

### Prompt Injection Attacks on AI Data Security

AI data security systems using LLMs (DLP, data classification, privacy compliance scanners, DSAR automation) are vulnerable to prompt injection attacks derived from Arcanum PI Taxonomy by Jason Haddix (CC BY 4.0):

**Attack Intents (Data Domain)**:
- System Prompt Leak: Extract data classification rules, DLP policies, privacy compliance logic
- Data Exfiltration via Prompt: Extract classified data, PII, or sensitive records through prompt manipulation
- Jailbreak Data Access Controls: Bypass data access policies enforced by AI
- Classification Manipulation: Force AI to misclassify sensitive data as public
- Privacy Policy Bypass: Circumvent GDPR/CCPA enforcement via AI manipulation

**Attack Techniques**:
- Document Injection: Malicious prompts embedded in documents AI scans for classification
- RAG Poisoning: Injecting malicious documents into knowledge bases for privacy compliance AI
- Metadata Manipulation: Prompt injection in file metadata, database comments, schema annotations
- Query Injection: Malicious prompts in user-submitted data access requests
- Role-Playing: Impersonating DPO or compliance officer in prompts

**Mitigations**: Input validation, prompt delimiters, output validation, data sanitization, access scoping, human review for sensitive requests, RAG document validation, anomaly detection, audit logging

### Regulatory Considerations

- **GDPR**: Article 6 (legal basis), Article 22 (automated decision-making), Article 25 (privacy-by-design), Article 35 (DPIA), Chapter V (cross-border transfers)
- **CCPA/CPRA**: Consumer rights (access, deletion, opt-out), automated decision-making opt-outs, do-not-sell obligations
- **HIPAA**: Administrative/physical/technical safeguards for AI processing PHI, Business Associate Agreements (BAAs), minimum necessary access
- **PCI-DSS**: Cardholder data environment segmentation, encryption, access controls, audit logging

### Privacy Paradox

AI data security tools need access to sensitive data to protect it, creating circular risk:
- AI agents become attractive targets (compromise AI = access all classified data)
- AI vendors may process customer sensitive data (cross-border transfers, training data, telemetry)
- Balancing AI effectiveness (broad data access) vs. data minimization (GDPR Article 5(1)(c))

---

**Document Version:** HAIAMM v3.0
**Practice:** Threat Assessment (TA)
**Domain:** Data
**Questionnaire Version:** 3.0
**Last Updated:** February 2026
