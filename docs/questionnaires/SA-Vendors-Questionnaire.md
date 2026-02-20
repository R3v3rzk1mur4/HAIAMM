# Secure Architecture (SA) - Vendors Domain
## HAIAMM Assessment Questionnaire v3.0

**Practice:** Secure Architecture (SA)
**Domain:** Vendors
**Purpose:** Assess organizational maturity in architectural design for AI-powered third-party risk management, vendor assessment, supply chain security, and continuous vendor monitoring systems
**Scoring Model:** Evidence + Outcome Metrics (see Scoring Methodology below)

---

## Instructions

- Answer each question honestly based on **current, implemented practices** (not plans or aspirations)
- **"Yes" requires evidence** - Document proof for each affirmative answer
- **Answer progressively** - Complete all Level 1 questions before Level 2
- **Level progression** - Achieve ALL questions at lower level before advancing
- **Partial implementation = "No"** - Practice must be complete and systematic
- Each question has two components: **Evidence** (what you did) and **Outcome Metrics** (how well it worked)
- **Scoring uses 4 tiers:** Fully Mature (1.0), Implemented (0.67), Partial (0.33), Not Implemented (0.0)
- **Baseline first** - Record current metric values before setting targets

---

## Level 1: Foundational
**Objective:** Establish foundational architecture for AI-powered vendor risk management with multi-factor risk scoring models, multi-source data integration, continuous monitoring, and SBOM analysis capabilities

### Question 1: AI Model Architecture for Vendor Risk Assessment

**Q1.1:** Have you designed and deployed AI model architecture for vendor risk assessment (multi-factor risk scoring combining security posture, data handling, compliance, incident history, and financial stability), SBOM analysis models (vulnerability detection, dependency risk scoring, supply chain attack detection), and vendor behavior anomaly detection with model versioning and explainability?

**Evidence Required:**
- [ ] AI Model Architecture designed and implemented:
  - Multi-Factor Risk Scoring: Weighted combination of risk signals (security posture ×0.30, data handling ×0.25, compliance ×0.20, incident history ×0.15, financial stability ×0.10)
  - ML Risk Classification: Supervised learning models classify vendor risk tier (Critical, High, Medium, Low) with confidence scores
  - Training Data: Labeled dataset of vendor assessments validated by security experts
  - Dynamic Weight Adjustment: Weights adjusted based on vendor type (e.g., data processor → data handling weight 0.40)
- [ ] SBOM Analysis Models:
  - Vulnerability Detection: Scan SBOMs for known CVEs with ≥99% detection rate
  - Dependency Risk Scoring: Score risk of each dependency (age, maintenance status, vulnerability count)
  - Supply Chain Attack Detection: Detect typosquatting, suspicious packages, anomalous updates
  - Transitive Dependency Analysis: Analyze dependencies ≥5 levels deep
- [ ] Vendor Behavior Anomaly Detection:
  - Unsupervised learning for unusual vendor behavior (unexpected data access, sudden security rating drops)
  - Baseline establishment per vendor with deviation alerting
- [ ] Model Versioning & Management:
  - Model registry with versions, metadata, performance metrics
  - A/B testing architecture for new models before full deployment
  - Rollback capability if model performance degrades ≥10%
- [ ] Explainability Architecture:
  - Risk score explanations (which factors contributed most to vendor risk tier)
  - SBOM findings with remediation guidance per vulnerability
  - Anomaly explanations with evidence (what changed, when, severity)
- [ ] Architecture documentation (diagrams, design decisions, technology choices)
- [ ] Architecture reviewed and approved by security leadership and vendor management

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Vendor assessment accuracy (AI vs human expert agreement %) | ___ | ___ | ≥85% | ☐ | |
| SBOM CVE detection rate (% of known CVEs detected) | ___ | ___ | ≥99% | ☐ | |
| Vendor risk tier classification confidence score (avg) | ___ | ___ | ≥0.80 | ☐ | |
| Vendor risk model rollback time when degradation detected (minutes) | ___ | ___ | ≤60 min | ☐ | |

**Metric Collection Guidance:**
- **Vendor assessment accuracy**: Monthly sample of 20+ vendor assessments; compare AI-assigned risk tier to independent human expert review; formula: (agreements / total reviewed) × 100
- **SBOM CVE detection rate**: Quarterly benchmark using synthetic SBOMs with known CVEs injected; formula: (CVEs detected / CVEs present) × 100; source: SBOM analysis pipeline logs
- **Vendor risk tier classification confidence score**: Extract confidence scores from ML model outputs weekly; compute fleet average; source: model inference logs
- **Vendor risk model rollback time**: Track from degradation alert trigger to rollback completion; source: model registry audit log with timestamps

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### Question 2: Multi-Source Data Integration and Vendor Monitoring Architecture

**Q1.2:** Have you implemented multi-source data integration architecture (vendor questionnaires, security ratings APIs, breach databases, SBOM sources, threat intelligence feeds) with entity resolution, schema standardization, and continuous vendor monitoring architecture (event-driven and polling-based) with tiered monitoring frequency by vendor criticality?

**Evidence Required:**
- [ ] Multi-Source Data Integration Architecture:
  - Vendor Questionnaire Integration: Automated distribution and response ingestion (CSV, JSON, API)
  - Questionnaire Standardization: Map diverse questionnaire formats to common schema
  - Security Ratings APIs: BitSight, SecurityScorecard, RiskRecon with daily sync
  - Breach Database Integration: HaveIBeenPwned, breach notification sites, threat intelligence feeds
  - SBOM Source Integration: SPDX and CycloneDX format support, vendor portal uploads, automated collection
  - Threat Intelligence Feeds: Industry ISACs, security vendor feeds, open-source intelligence
- [ ] Data Normalization:
  - Vendor Entity Resolution: ML models + manual curation to match vendor entities across data sources
  - Schema Standardization: Common schema (vendor ID, name, domains, risk score, certifications, data processing details)
  - Data Quality Validation: Completeness, freshness, accuracy checks on ingested data
- [ ] Continuous Vendor Monitoring Architecture:
  - Event-Driven: Webhook integration for vendor-pushed security events (incidents, certification updates, breach disclosures)
  - Polling Architecture: Periodic checks by data type (security ratings daily, certifications monthly, breach databases daily)
  - Change Detection & Alerting: Rating degradation (≥1 letter grade), breach detection (≤24 hours), certification expiration (30-day warning), behavioral anomalies
- [ ] Tiered Monitoring by Vendor Criticality:
  - Critical vendors: Daily monitoring
  - High vendors: Weekly monitoring
  - Medium vendors: Monthly monitoring
  - Low vendors: Quarterly monitoring
- [ ] Infrastructure: Scalable data pipeline supporting ≥1,000 vendor relationships
- [ ] Monitoring dashboard for vendor risk posture overview

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Vendor breach detection time from public disclosure (hours) | ___ | ___ | ≤24 hours | ☐ | |
| Data pipeline freshness: % of Critical/High vendor records updated within SLA | ___ | ___ | ≥90% | ☐ | |
| Vendor entity resolution accuracy (% correctly matched across sources) | ___ | ___ | ≥95% | ☐ | |
| Monitoring coverage: % of Critical/High vendors with active continuous monitoring | ___ | ___ | ≥90% | ☐ | |

**Metric Collection Guidance:**
- **Vendor breach detection time**: Compare breach alert timestamp in system to public disclosure timestamp; track monthly; source: monitoring event log and external breach notification timestamps
- **Data pipeline freshness**: Weekly query of vendor record last-updated timestamps vs monitoring tier SLA; formula: (vendors updated within SLA / total vendors in tier) × 100; source: data pipeline metadata
- **Vendor entity resolution accuracy**: Quarterly manual audit of 50 random entity resolution matches; formula: (correct matches / total audited) × 100; source: entity resolution audit log
- **Monitoring coverage**: Weekly query of monitoring configuration vs vendor inventory; formula: (Critical+High vendors monitored / total Critical+High vendors) × 100; source: monitoring platform configuration

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### Question 3: Risk Scoring Engine, Compliance Automation, and Security Architecture

**Q1.3:** Have you implemented vendor risk scoring and prioritization architecture (combined vendor risk × business criticality with risk-based action workflows), compliance automation architecture (regulatory requirement mapping, contract analysis via NLP, automated evidence collection), and security architecture protecting vendor risk management systems from adversarial manipulation?

**Evidence Required:**
- [ ] Vendor Risk Scoring & Prioritization Engine:
  - Combined Scoring: Vendor Risk × Business Criticality = Priority Score
  - Risk-Based Action Workflows: Priority >80 requires CISO approval; 60-80 requires security team approval; <60 automated approval
  - Dynamic Recalculation: Risk scores updated automatically when new data arrives
- [ ] Compliance Automation Architecture:
  - Jurisdiction Detection: Determine which regulations apply per vendor (GDPR, HIPAA, PCI-DSS, CCPA) based on location, data types, processing activities
  - Requirement Database: Regulatory vendor requirements mapped (GDPR Article 28 DPA terms, HIPAA BAA, PCI compliance validation)
  - Contract Analysis: NLP models analyze vendor contracts for required clauses (e.g., GDPR Article 28 compliance in DPA)
  - Automated Evidence Collection: SOC 2 reports, certifications, attestations, BAAs, DPAs gathered and tracked
  - Compliance Reporting: Auto-generated audit reports (e.g., GDPR Article 30 processor list)
- [ ] Security Architecture for Vendor Risk Management Systems:
  - Data Security: Vendor assessment data encrypted at rest (AES-256) and in transit (TLS 1.3)
  - Access Controls: RBAC with least privilege for vendor data access
  - API Security: Authentication (OAuth 2.0), authorization, input validation, rate limiting
  - Audit Logging: All vendor assessments, risk score changes, compliance checks logged with ≥1 year retention
  - Adversarial Defense: Input validation on vendor-submitted data (questionnaires, SBOMs) to prevent manipulation
  - Network Security: Vendor risk management systems in dedicated network segment
- [ ] Architecture documentation and approval by security and compliance leadership

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Vendor onboarding risk assessment completion time (days) | ___ | ___ | ≤7 days | ☐ | |
| Compliance evidence collection automation rate (% auto-collected vs manual) | ___ | ___ | ≥70% | ☐ | |
| Vendor risk false positive alert rate (% of alerts requiring no action) | ___ | ___ | ≤15% | ☐ | |
| Risk score recalculation latency after new data event (minutes) | ___ | ___ | ≤30 min | ☐ | |

**Metric Collection Guidance:**
- **Vendor onboarding risk assessment completion time**: Track from vendor onboarding request creation to risk tier assignment; monthly average; source: vendor management workflow timestamps
- **Compliance evidence collection automation rate**: Monthly audit of evidence collection events; formula: (auto-collected items / total evidence items collected) × 100; source: compliance evidence management system
- **Vendor risk false positive alert rate**: Weekly review of vendor alerts; human analysts mark false positives; formula: (false positive alerts / total alerts) × 100; source: alert management system
- **Risk score recalculation latency**: Average time from data ingestion event to updated risk score availability; source: data pipeline event timestamps and risk score update log

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

**Level 1 Score:** _____ / 3 questions answered "Yes"

**Level 1 Achieved:** ☐ Yes (3/3) ☐ No (< 3/3)

---

## Level 2: Comprehensive
**Objective:** Implement predictive vendor risk modeling, vendor ecosystem intelligence with dependency mapping, advanced supply chain analysis, and vendor deception detection

**Prerequisites:** ALL Level 1 questions must be "Yes" to proceed to Level 2

### Question 4: Predictive Vendor Risk and Leading Indicator Architecture

**Q2.1:** Have you implemented predictive vendor risk architecture including time-series models that forecast vendor risk trajectories (improving, stable, degrading), breach probability modeling, and leading indicator detection (executive turnover, financial distress, security rating decline) that provides early warning of vendor risk increases?

**Evidence Required:**
- [ ] Predictive Vendor Risk Models:
  - Time-Series Forecasting: Models predict vendor risk trajectory over 3-6-12 month horizons
  - Breach Probability Modeling: Predict which vendors are likely to suffer security breaches
  - Confidence Intervals: Predictions include uncertainty bounds
  - Validation: Back-testing against historical vendor incidents (≥70% prediction accuracy for high-risk vendors)
- [ ] Leading Indicator Detection:
  - Executive Turnover Monitoring: Detect CISO/CTO departures from vendors (news feeds, LinkedIn integration)
  - Financial Distress Signals: Credit ratings, SEC filings, revenue decline indicators
  - Security Rating Decline: Trend analysis detecting gradual degradation before threshold breach
  - Technical Indicators: Domain/SSL certificate changes, infrastructure changes, exposed services
- [ ] Early Warning System:
  - Alert thresholds for leading indicators (e.g., vendor security rating declining 3 consecutive months)
  - Proactive risk mitigation recommendations before vendor risk materializes
  - Integration with vendor management workflows (trigger enhanced due diligence)
- [ ] Model performance tracking: Prediction accuracy reviewed quarterly
- [ ] False positive rate for early warnings ≤20%

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Predictive model accuracy for high-risk vendor identification (%) | ___ | ___ | ≥70% | ☐ | |
| Average early warning lead time before risk materialization (days) | ___ | ___ | ≥14 days | ☐ | |
| Leading indicator false positive rate (% of warnings requiring no action) | ___ | ___ | ≤20% | ☐ | |
| Proactive risk mitigation actions triggered per quarter (count) | ___ | ___ | ≥5 actions | ☐ | |

**Metric Collection Guidance:**
- **Predictive model accuracy**: Quarterly back-test against actual vendor incidents in prior period; formula: (correctly predicted high-risk vendors / total high-risk vendors that materialized) × 100; source: model prediction log vs incident record
- **Early warning lead time**: For each materialized vendor risk event, calculate days between first early warning alert and confirmed incident; source: alert log timestamps vs vendor incident report dates
- **Leading indicator false positive rate**: Monthly review of leading indicator alerts by vendor risk team; formula: (alerts with no subsequent risk materialization within 90 days / total alerts) × 100; source: alert management system
- **Proactive risk mitigation actions**: Count of enhanced due diligence, access restrictions, or contract renegotiations triggered by predictive alerts; source: vendor management workflow action log

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### Question 5: Vendor Ecosystem Intelligence and Systemic Risk Architecture

**Q2.2:** Have you implemented vendor ecosystem intelligence architecture including complete dependency network mapping (vendor → subprocessors → sub-subprocessors), graph database for relationship storage, concentration risk identification, and cascading failure modeling to quantify systemic risk across the vendor ecosystem?

**Evidence Required:**
- [ ] Dependency Network Mapping:
  - Complete vendor ecosystem mapped (vendor → subprocessors → sub-subprocessors, ≥3 levels deep)
  - Graph database (Neo4j or equivalent) storing dependency relationships
  - Automated discovery: NLP analysis of vendor contracts, DPAs, and public disclosures to identify subprocessors
  - Continuous updates: Subprocessor changes detected within ≤30 days
- [ ] Concentration Risk Identification:
  - Single Points of Failure: Identify subprocessors used by ≥3 critical vendors
  - Geographic Concentration: Identify vendor clusters in high-risk jurisdictions
  - Technology Concentration: Identify shared technology dependencies (e.g., all vendors use same cloud provider)
  - Risk Quantification: Business impact analysis if concentrated dependency fails
- [ ] Cascading Failure Modeling:
  - Simulation: Model cascading failures ("if subprocessor X fails, which vendors affected, what business impact?")
  - Propagation Analysis: Understand how a vendor breach propagates through supply chain
  - Scenario Planning: Pre-computed response plans for top 10 concentration risk scenarios
- [ ] Vendor Relationship Visualization:
  - Interactive dependency graphs for security and executive stakeholders
  - Risk heat maps overlaid on vendor ecosystem topology
- [ ] Ecosystem intelligence updated at least quarterly

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Vendor ecosystem mapping depth achieved (levels of subprocessor hierarchy mapped) | ___ | ___ | ≥3 levels | ☐ | |
| Subprocessor change detection time (days from change to system update) | ___ | ___ | ≤30 days | ☐ | |
| Concentration risks identified and documented (count of single points of failure) | ___ | ___ | 100% of known SPOFs | ☐ | |
| Cascading failure scenarios with pre-computed response plans (count) | ___ | ___ | ≥10 scenarios | ☐ | |

**Metric Collection Guidance:**
- **Vendor ecosystem mapping depth**: Annual audit of graph database to measure maximum depth of subprocessor relationships mapped; source: graph database query (MAX depth from root vendor nodes)
- **Subprocessor change detection time**: Track subprocessor change announcements vs date of graph database update; sample 10+ changes per quarter; source: contract/DPA amendment timestamps vs graph update log
- **Concentration risks identified**: Quarterly query of graph database for shared subprocessors used by ≥3 critical vendors; document all identified; formula: (documented SPOFs / all identified SPOFs via audit) × 100; source: graph database + manual audit
- **Cascading failure scenarios with plans**: Count of documented scenario plans in risk registry; review quarterly for completeness; source: risk scenario planning document repository

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### Question 6: Advanced Supply Chain Analysis and Vendor Deception Detection

**Q2.3:** Have you implemented advanced supply chain security architecture including deep dependency analysis (≥5 levels, transitive vulnerability tracking, license compliance), vendor deception detection models (questionnaire inconsistency detection, certification fabrication detection, behavioral indicators of deception), and federated vendor intelligence sharing with peer organizations?

**Evidence Required:**
- [ ] Advanced Supply Chain Analysis:
  - Deep Dependency Analysis: Transitive dependencies analyzed ≥5 levels with risk scoring per level
  - License Compliance: Automated license compatibility checking across dependency trees
  - Dependency Health Scoring: Maintenance status, community activity, vulnerability response time per dependency
  - SBOM Drift Detection: Alert when vendor SBOM changes significantly between assessments
  - Zero-Day Dependency Alerts: Immediate notification when newly disclosed vulnerabilities affect vendor dependencies
- [ ] Vendor Deception Detection:
  - Questionnaire Inconsistency Detection: NLP models identify contradictions across questionnaire responses
  - Certification Fabrication Detection: Automated verification of claimed certifications (SOC 2, ISO 27001) against registries
  - Cross-Reference Validation: Compare vendor self-reported data against external sources (security ratings, breach databases)
  - Behavioral Deception Indicators: Patterns suggesting vendor is misrepresenting security posture (delayed responses, vague answers, inconsistent details)
  - Deception confidence scoring with evidence trail for investigator review
- [ ] Federated Vendor Intelligence:
  - Anonymized vendor risk data sharing with peer organizations or industry ISACs
  - Privacy-preserving techniques (differential privacy, secure multi-party computation)
  - Shared threat intelligence about vendor-related incidents
- [ ] Supply chain and deception detection models validated against known cases

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Supply chain analysis depth (max dependency levels analyzed) | ___ | ___ | ≥5 levels | ☐ | |
| Zero-day dependency alert time from CVE publication to notification (hours) | ___ | ___ | ≤4 hours | ☐ | |
| Vendor deception detection rate (% of known deceptive submissions flagged) | ___ | ___ | ≥80% | ☐ | |
| Certification verification automation rate (% auto-verified vs manual) | ___ | ___ | ≥90% | ☐ | |

**Metric Collection Guidance:**
- **Supply chain analysis depth**: Quarterly audit of SBOM analysis pipeline depth configuration and sample analysis outputs; source: SBOM analysis engine configuration and analysis reports
- **Zero-day dependency alert time**: Track from NVD/CVE publication timestamp to first alert delivery for affected vendors; measure monthly; source: CVE feed ingestion log vs alert delivery log
- **Vendor deception detection rate**: Quarterly validation using synthetic deceptive submissions and known historical cases; formula: (detected deceptive submissions / total deceptive submissions in test set) × 100; source: deception detection model validation results
- **Certification verification automation rate**: Monthly audit of certification verification events; formula: (auto-verified certifications / total certification claims processed) × 100; source: compliance automation system event log

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

**Level 2 Score:** _____ / 3 questions answered "Yes"

**Level 2 Achieved:** ☐ Yes (3/3) ☐ No (< 3/3)

---

## Level 3: Industry-Leading
**Objective:** Implement autonomous vendor risk operations, zero-trust vendor access architecture, blockchain-based audit trails, and contribute to open-source vendor risk management tools

**Prerequisites:** ALL Level 2 questions must be "Yes" to proceed to Level 3

### Question 7: Autonomous Vendor Risk Operations

**Q3.1:** Have you implemented autonomous vendor risk operations where AI conducts vendor risk assessments autonomously for ≥80% of low-risk vendors (with human review only for high-risk or edge cases), automated vendor onboarding/offboarding with security validation, and self-tuning risk models that automatically adjust weights and thresholds based on operational outcomes?

**Evidence Required:**
- [ ] Autonomous Vendor Assessment:
  - AI autonomously assesses ≥80% of low-risk vendor renewals
  - Human review triggered only for high-risk vendors, new critical vendors, or edge cases
  - Assessment accuracy: ≥90% agreement between autonomous and human expert assessments
  - Autonomous assessment completion time: ≤24 hours (vs ≤7 days for manual)
- [ ] Automated Vendor Lifecycle Management:
  - Automated Onboarding: Security questionnaire distribution, response analysis, risk scoring, approval routing
  - Automated Offboarding: Access revocation, data deletion verification, certificate invalidation
  - Continuous Re-assessment: Automated periodic reviews based on vendor tier (Critical: quarterly, High: semi-annual, Medium: annual)
- [ ] Self-Tuning Risk Models:
  - Automatic weight adjustment based on which risk factors best predict actual vendor incidents
  - Threshold optimization based on false positive/negative analysis
  - Model retraining triggered automatically when performance degrades ≥5%
  - Drift detection with automated alerting
- [ ] Governance: Audit trail of all autonomous decisions with explainability
- [ ] Override capability: Security team can override any autonomous decision
- [ ] Performance metrics: Autonomous assessment accuracy tracked monthly

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Autonomous assessment rate for low-risk vendors (%) | ___ | ___ | ≥80% | ☐ | |
| Autonomous assessment completion time vs manual baseline (hours) | ___ | ___ | ≤24 hours | ☐ | |
| Autonomous vs human expert agreement rate on risk tier (%) | ___ | ___ | ≥90% | ☐ | |
| Self-tuning model retraining frequency when degradation detected (days to retrain) | ___ | ___ | ≤7 days | ☐ | |

**Metric Collection Guidance:**
- **Autonomous assessment rate**: Monthly report from assessment workflow; formula: (low-risk vendor assessments completed autonomously / total low-risk vendor assessments) × 100; source: assessment workflow system
- **Autonomous assessment completion time**: Average hours from assessment initiation to completed risk tier assignment for autonomous track; source: workflow timestamp log
- **Autonomous vs human expert agreement rate**: Monthly sample of 20+ autonomous assessments; human expert reviews same vendor and assigns tier; formula: (agreements / total reviewed) × 100; source: QA review log
- **Self-tuning model retraining frequency**: Track from model degradation detection alert to successful retrained model deployment; source: model registry and drift detection alert log with timestamps

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### Question 8: Zero-Trust Vendor Access and Blockchain Audit Architecture

**Q3.2:** Have you implemented zero-trust vendor access architecture (continuous verification, just-in-time access with automatic revocation, micro-segmented vendor environments, real-time posture assessment) and blockchain or immutable ledger-based vendor audit trails providing tamper-proof records of assessments, certifications, incidents, and compliance status?

**Evidence Required:**
- [ ] Zero-Trust Vendor Access Architecture:
  - Continuous Verification: Vendor access continuously validated (not just at onboarding)
  - Just-in-Time Access: Temporary access grants with automatic expiration and revocation
  - Micro-Segmented Environments: Each vendor operates in isolated environment with least-privilege network access
  - Real-Time Posture Assessment: Vendor security posture checked before each access grant
  - Conditional Access Policies: Access restricted based on vendor risk score, time of day, data sensitivity
  - Vendor Identity Verification: Multi-factor authentication for vendor personnel accessing systems
- [ ] Immutable Vendor Audit Trails:
  - Blockchain or immutable ledger recording: Assessment results, certification validations, incident reports, compliance status changes
  - Tamper-Proof: Cryptographic verification that records haven't been altered
  - Multi-Party Verification: Vendor, assessor, and system signatures on key records
  - Audit Trail Completeness: Every vendor risk decision traceable from data ingestion to final assessment
  - Retention: Immutable records maintained for ≥5 years (regulatory compliance)
- [ ] Architecture supports regulatory audit requirements (SOC 2, ISO 27001, GDPR accountability)
- [ ] Performance: Zero-trust access decisions made in ≤500ms (no significant vendor workflow impact)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Zero-trust access decision latency (ms, 95th percentile) | ___ | ___ | ≤500 ms | ☐ | |
| Just-in-time access sessions auto-revoked on expiry (% of sessions) | ___ | ___ | ≥99% | ☐ | |
| Audit trail tamper detection rate (% of tamper attempts detected in testing) | ___ | ___ | 100% | ☐ | |
| Immutable audit record retention compliance (% of records within ≥5 year retention) | ___ | ___ | 100% | ☐ | |

**Metric Collection Guidance:**
- **Zero-trust access decision latency**: Continuous monitoring of access decision API response times; measure 95th percentile weekly; source: API gateway metrics and access control system telemetry
- **JIT access auto-revocation rate**: Weekly query of access session records; formula: (sessions auto-revoked at expiry / total JIT sessions that reached expiry) × 100; source: privileged access management (PAM) system logs
- **Audit trail tamper detection rate**: Quarterly red team exercise attempting to modify audit records; formula: (tamper attempts detected / total tamper attempts) × 100; source: cryptographic integrity verification results
- **Immutable record retention compliance**: Annual audit of ledger records; formula: (records meeting ≥5 year retention requirement / total required records) × 100; source: ledger/blockchain record metadata

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### Question 9: Open-Source Contribution and Continuous Architecture Evolution

**Q3.3:** Do you contribute to open-source vendor risk management tools or industry standards, participate in collaborative vendor intelligence platforms, and maintain a continuous architecture improvement program incorporating lessons learned from vendor incidents, autonomous operation outcomes, and emerging supply chain threats?

**Evidence Required:**
- [ ] Open-Source and Industry Contributions:
  - At least 2 contributions per year: open-source vendor risk tools, SBOM analysis libraries, vendor scoring frameworks
  - Industry standards participation: NIST, ISO, OWASP supply chain security working groups
  - Published research: Blog posts, conference talks, or papers on AI-powered vendor risk management
  - Vendor intelligence sharing: Active participation in industry ISACs or vendor risk sharing platforms
- [ ] Continuous Architecture Evolution:
  - Documented process for updating vendor risk architecture based on:
    - Vendor incidents (breaches, compliance failures, service disruptions)
    - Autonomous operation outcomes (accuracy trends, edge cases discovered)
    - Emerging supply chain threats (new attack vectors, regulatory changes)
    - Technology advancements (new ML techniques, new data sources)
  - Historical record showing architecture evolution (12+ months)
  - Examples of architecture improvements triggered by operational experience:
    - Enhanced deception detection after vendor misrepresentation incident
    - Improved ecosystem mapping after cascading vendor failure
    - New data source integration after intelligence gap identified
- [ ] Feedback Loop: Threat intelligence → Architecture update → Testing → Deployment → Monitoring → Re-assess
- [ ] Metrics tracked: vendor coverage, assessment accuracy, prediction accuracy, false positive/negative rates, autonomous operation percentage, time-to-assessment

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Open-source / industry contributions per year (count) | ___ | ___ | ≥2 per year | ☐ | |
| Architecture improvement cycle time: threat identified to deployed improvement (days) | ___ | ___ | ≤90 days | ☐ | |
| Architecture improvements triggered by operational experience (12-month trailing count) | ___ | ___ | ≥3 per year | ☐ | |
| Year-over-year improvement in vendor assessment accuracy (percentage points) | ___ | ___ | ≥5 pp YoY | ☐ | |

**Metric Collection Guidance:**
- **Open-source / industry contributions**: Annual inventory of GitHub PRs, published blog posts, conference presentations, standards group participation; source: internal contribution tracking log
- **Architecture improvement cycle time**: Track from formal identification of threat/gap to deployment of architecture change; source: architecture change management system with timestamps
- **Architecture improvements from operational experience**: Annual review counting improvements directly traceable to incident, red team, or operational feedback triggers; source: architecture decision record (ADR) repository
- **Year-over-year accuracy improvement**: Compare annual average vendor assessment accuracy metric (from Q1.1) to prior year baseline; formula: current_year_avg_accuracy - prior_year_avg_accuracy; source: model performance tracking dashboard

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

**Level 3 Score:** _____ / 3 questions answered "Yes"

**Level 3 Achieved:** ☐ Yes (3/3) ☐ No (< 3/3)

---

## Practice Score Calculation

### Simplified Scoring (Recommended)

```
Level 1 Achieved (all 3 "Fully Mature" or "Implemented"): 1.0 point
Level 2 Achieved (all 3 "Fully Mature" or "Implemented"): +1.0 point (total 2.0)
Level 3 Achieved (all 3 "Fully Mature" or "Implemented"): +1.0 point (total 3.0)
```

**SA-Vendors Practice Score:** _______ / 3.0

### Precise Scoring (For Formal Audits)

```
L1_score = (Q1.1_score + Q1.2_score + Q1.3_score) / 3
L2_score = (Q2.1_score + Q2.2_score + Q2.3_score) / 3 × (L1_score if L1_score ≥ 1.0, else 0)
L3_score = (Q3.1_score + Q3.2_score + Q3.3_score) / 3 × (L2_score if L2_score ≥ 1.0, else 0)

Practice Score = L1_score + L2_score + L3_score
```

**SA-Vendors Practice Score (Precise):** _______ / 3.0

---

## Assessment Summary

**Assessment Date:** _________________________________

**Assessor(s):** _____________________________________

**HAI System(s) Assessed:** __________________________

**Overall Maturity Level:**
- ☐ Level 0 (Score < 0.5): Ad-hoc, no formal vendor security architecture
- ☐ Level 1 (Score 0.5 - 1.49): Foundational risk assessment and monitoring architecture
- ☐ Level 2 (Score 1.5 - 2.49): Comprehensive predictive modeling and ecosystem intelligence
- ☐ Level 3 (Score 2.5 - 3.0): Industry-leading autonomous operations and zero-trust vendor access

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

## Secure Architecture Vendor-Specific Notes

**Architecture Components Covered:**
- [ ] AI model architecture for vendor risk assessment (multi-factor scoring, ML classification, confidence scoring)
- [ ] SBOM analysis architecture (vulnerability detection, dependency risk scoring, supply chain attack detection)
- [ ] Multi-source data integration (vendor questionnaires, security ratings, breach databases, threat intelligence)
- [ ] Vendor entity resolution and schema standardization
- [ ] Continuous monitoring architecture (event-driven + polling, tiered by vendor criticality)
- [ ] Risk scoring and prioritization engine (vendor risk × business criticality)
- [ ] Compliance automation (jurisdiction detection, contract NLP analysis, evidence collection, audit reporting)
- [ ] Predictive risk modeling (time-series forecasting, breach probability, leading indicators)
- [ ] Vendor ecosystem intelligence (dependency mapping, concentration risk, cascading failure modeling)
- [ ] Supply chain deep analysis (transitive dependencies, license compliance, SBOM drift)
- [ ] Vendor deception detection (questionnaire inconsistency, certification fabrication, behavioral indicators)
- [ ] Zero-trust vendor access (continuous verification, just-in-time access, micro-segmentation)
- [ ] Immutable audit trails (blockchain/ledger, tamper-proof records, multi-party verification)

**Vendor Architecture Scalability Requirements:**
- [ ] Support ≥1,000 vendor relationships with continuous monitoring
- [ ] Vendor risk assessment completion ≤7 days (manual), ≤24 hours (autonomous)
- [ ] Zero-trust access decisions ≤500ms
- [ ] SBOM analysis ≥99% CVE detection rate
- [ ] Breach detection ≤24 hours of vendor breach disclosure

**Supply Chain Security Architecture:**
- [ ] SBOM format support: SPDX (JSON, XML), CycloneDX (JSON, XML)
- [ ] Graph database for dependency relationships (Neo4j or equivalent)
- [ ] Transitive dependency analysis ≥5 levels deep
- [ ] Typosquatting and suspicious package detection
- [ ] Zero-day dependency alerting

**Compliance Architecture Coverage:**
- [ ] GDPR (DPA Article 28, subprocessor lists, breach notification, Article 30 processor records)
- [ ] HIPAA (BAA requirements, compliance attestation)
- [ ] PCI-DSS (compliance validation for payment-related vendors)
- [ ] CCPA (service provider requirements, data sale restrictions)
- [ ] Multi-jurisdiction conflict resolution

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

**Document Version:** 3.0
**Last Updated:** 2026-02-18
**Next Review:** Quarterly or after significant HAI vendor risk management changes
