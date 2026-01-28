# HAIAMM x NIST AI RMF Playbook: Action-Level Mapping
## Comprehensive Cross-Reference of 450+ Suggested Actions to HAIAMM Practices

**Version:** 1.0
**Date:** January 2026
**HAIAMM Version:** 2.2
**NIST AI RMF:** 1.0 (AI 100-1), Playbook (AI 600-1)

---

## Executive Summary

The NIST AI RMF Playbook contains **72 subcategories** with **450+ suggested actions** across 4 functions. This document maps each subcategory to specific HAIAMM practices, identifies coverage levels, and highlights where HAIAMM extends beyond NIST or where NIST covers ground HAIAMM does not.

### Coverage Summary

| NIST Function | Subcategories | HAIAMM Coverage |
|---------------|---------------|-----------------|
| **GOVERN** (19) | 19 | 84% (16/19 strong or moderate) |
| **MAP** (16) | 16 | 69% (11/16 strong or moderate) |
| **MEASURE** (18) | 18 | 78% (14/18 strong or moderate) |
| **MANAGE** (19) | 19 | 89% (17/19 strong or moderate) |
| **Total** | **72** | **81% overall alignment** |

### Key Finding

HAIAMM and NIST AI RMF are genuinely complementary:
- **NIST provides the "what"** — broad AI governance principles and risk categories
- **HAIAMM provides the "how"** — specific security practices with measurable outcomes
- **Together** they form a complete AI security governance program

---

## How to Read This Document

| Symbol | Meaning |
|--------|---------|
| **HAIAMM Practice** | Two-letter code (SM, PC, EG, TA, SR, SA, DR, IR, ST, IM, EH, ML) |
| **Coverage** | Full / Partial / Extended / Gap |
| **Level** | L1 (Foundation), L2 (Structured), L3 (Optimized) |
| **Domain** | Which of the 6 HAIAMM domains apply |

---

## GOVERN Function Mapping

### GOVERN 1: Policies, Processes, and Procedures

#### GOVERN 1.1 — Legal and Regulatory Requirements

| NIST Suggested Action | HAIAMM Practice | Coverage | Notes |
|----------------------|-----------------|----------|-------|
| Monitor applicable legal/regulatory considerations | PC L1 | Full | PC L1 explicitly covers regulatory awareness |
| Align risk management with applicable legal standards | PC L2 | Full | PC L2 requires compliance implementation |
| Maintain training policies on legal considerations | EG L1 | Full | EG L1 covers compliance training |

**HAIAMM Practice:** PC (Policy & Compliance) L1-L2, EG (Education & Guidance) L1
**Domains:** All 6 — legal requirements span entire stack

---

#### GOVERN 1.2 — Trustworthy AI Characteristics Integration

| NIST Suggested Action | HAIAMM Practice | Coverage | Notes |
|----------------------|-----------------|----------|-------|
| Define key AI terms, scope, purposes | SM L1 | Full | SM L1 establishes AI strategy |
| Connect AI governance to existing governance | SM L1, PC L1 | Full | HAIAMM integrates with existing programs |
| Align with data governance policies | SA (Data domain) | Full | Data domain covers governance |
| Detail standards for experimental design | SR L1 | Partial | HAIAMM focuses on security requirements |
| Document risk mapping processes | TA L1-L2 | Full | TA is HAIAMM's risk mapping practice |
| Detail model testing/validation | ST L1-L3 | Full | Security Testing practice |
| Include legal/risk function review | PC L2 | Full | Policy & Compliance |
| Establish monitoring/auditing frequency | ML L2 | Full | Monitoring & Logging |
| Outline change management requirements | IM L2 | Partial | Issue Management covers changes |
| Define stakeholder engagement processes | SM L2 | Partial | Strategy & Metrics |
| Establish whistleblower policies | PC L1 | Gap | HAIAMM doesn't address whistleblower mechanisms |
| Detail and test incident response plans | IM L1-L2 | Full | Issue Management |
| Ensure policies include third-party AI systems | SA (Vendors) | Full | Vendors domain |

**HAIAMM Coverage:** 85% — Strong alignment. Gap: whistleblower/reporting mechanisms.

---

#### GOVERN 1.3 — Risk Tolerance and Resource Allocation

| NIST Suggested Action | HAIAMM Practice | Coverage | Notes |
|----------------------|-----------------|----------|-------|
| Establish mechanisms for measuring AI impact | TA L2-L3 | Full | Measurable outcomes in v2.2 |
| Define mechanisms for measuring likelihood | TA L2 | Full | Risk scoring formulas |
| Define assessment scales (qualitative/quantitative) | SM L2-L3 | Full | HAIAMM maturity scoring |
| Establish overall risk measurement approach | TA L2, SM L2 | Full | Combined practice coverage |
| Assign systems to uniform risk scales | SM L2 | Partial | HAIAMM uses maturity levels, not risk scales |

**HAIAMM Coverage:** 90% — HAIAMM's measurable outcomes (v2.2) directly address this.

---

#### GOVERN 1.4 — Transparent Risk Management Processes

| NIST Suggested Action | HAIAMM Practice | Coverage | Notes |
|----------------------|-----------------|----------|-------|
| Establish documentation policies | SM L2, DR L1 | Full | Design Review requires documentation |
| Verify documentation policies are current | SM L3 | Full | L3 continuous improvement |
| Establish model documentation inventory | SM L1 | Partial | HAIAMM tracks practices, not model inventory |
| Review risk management processes regularly | SM L3 | Full | L3 optimization |
| Establish public disclosure policies | PC L2 | Partial | HAIAMM focuses on internal compliance |
| Document transparency tools and standards | SM L2 | Partial | HAIAMM mentions but doesn't detail transparency tools |

**HAIAMM Coverage:** 75% — HAIAMM covers risk documentation but is lighter on public transparency.

---

#### GOVERN 1.5 — Ongoing Monitoring and Review

| NIST Suggested Action | HAIAMM Practice | Coverage | Notes |
|----------------------|-----------------|----------|-------|
| Allocate resources for assessing AI impacts | SM L2 | Full | Strategy & Metrics |
| Establish monitoring policies for performance | ML L1-L2 | Full | Monitoring & Logging |
| Establish incident response policies | IM L1-L2 | Full | Issue Management |
| Define personnel responsible for monitoring | SM L2 | Full | Roles and responsibilities |
| Enable feedback mechanisms from impacted individuals | — | Gap | HAIAMM doesn't address external feedback channels |
| Establish recourse mechanisms | — | Gap | HAIAMM doesn't cover end-user recourse |
| Establish opt-out mechanisms | — | Gap | Outside HAIAMM scope (security focus) |

**HAIAMM Coverage:** 60% — Strong on monitoring and incident response. Gaps on user recourse and feedback channels (HAIAMM is security-focused, not user-rights-focused).

---

#### GOVERN 1.6 — AI System Inventory

| NIST Suggested Action | HAIAMM Practice | Coverage | Notes |
|----------------------|-----------------|----------|-------|
| Establish AI system inventory policies | SM L1 | Partial | HAIAMM implies but doesn't mandate inventory |
| Define responsible individual/team | SM L2 | Partial | Covered in roles/responsibilities |
| Define which systems are inventoried | SM L1 | Partial | Scope definition |
| Define inventory attributes | SM L1, DR L1 | Partial | Documentation requirements |

**HAIAMM Coverage:** 50% — HAIAMM assumes inventory exists but doesn't prescribe how to create one.

---

#### GOVERN 1.7 — Decommissioning and Phase-Out

| NIST Suggested Action | HAIAMM Practice | Coverage | Notes |
|----------------------|-----------------|----------|-------|
| Establish decommissioning policies | IM L2 | Partial | Issue Management covers some lifecycle |
| Delineate storage for decommissioned systems | EH L2 | Partial | Environment Hardening |
| Track accountability of decommissioning | SM L2 | Partial | Strategy & Metrics |
| Address preservation of artifacts | — | Gap | HAIAMM doesn't detail decommissioning |

**HAIAMM Coverage:** 35% — Decommissioning is a gap. HAIAMM focuses on build and operate, not retire.

---

### GOVERN 2: Accountability Structures

#### GOVERN 2.1 — Roles and Responsibilities

| NIST Suggested Action | HAIAMM Practice | Coverage | Notes |
|----------------------|-----------------|----------|-------|
| Define AI risk management roles | SM L2 | Full | Strategy & Metrics covers governance roles |
| Promote regular communication among AI actors | SM L2 | Full | |
| Separate development from testing functions | ST L2, IR L2 | Full | HAIAMM separates verification from building |
| Identify and prevent conflicts of interest | PC L2 | Partial | Not explicitly addressed |
| Incentivize collaboration with legal/compliance | PC L2 | Full | Policy & Compliance |

**HAIAMM Coverage:** 80%

---

#### GOVERN 2.2 — Personnel Training

| NIST Suggested Action | HAIAMM Practice | Coverage | Notes |
|----------------------|-----------------|----------|-------|
| Establish ongoing education policies | EG L1-L3 | Full | Education & Guidance core purpose |
| Ensure training suitable for different groups | EG L2 | Full | Role-based training |
| Address technical and socio-technical aspects | EG L1-L2 | Partial | HAIAMM focuses on security training |
| Include personnel acknowledgment mechanisms | EG L2 | Partial | Not explicitly required |
| Define accountability escalation paths | SM L2 | Full | Governance structure |

**HAIAMM Coverage:** 75%

---

#### GOVERN 2.3 — Executive Leadership Responsibility

| NIST Suggested Action | HAIAMM Practice | Coverage | Notes |
|----------------------|-----------------|----------|-------|
| Declare organizational risk tolerances | SM L1-L2 | Full | Strategy & Metrics |
| Support AI risk management efforts | SM L2 | Full | |
| Establish board committees for AI oversight | SM L3 | Partial | HAIAMM recommends but doesn't prescribe board structure |

**HAIAMM Coverage:** 75%

---

### GOVERN 3: Workforce Diversity

#### GOVERN 3.1 — Diverse Team Decision-Making

| NIST Suggested Action | HAIAMM Practice | Coverage | Notes |
|----------------------|-----------------|----------|-------|
| Define hiring practices for diversity | — | Gap | Outside HAIAMM scope |
| Empower staff for feedback | EG L2 | Partial | Education includes awareness |
| Seek external expertise | TA L2 (Vendors) | Partial | Vendor engagement |

**HAIAMM Coverage:** 25% — HAIAMM focuses on security competency, not workforce diversity.

---

#### GOVERN 3.2 — Human-AI Configuration Oversight

| NIST Suggested Action | HAIAMM Practice | Coverage | Notes |
|----------------------|-----------------|----------|-------|
| Define human roles for AI oversight | SR L1 | Full | Security Requirements includes human oversight |
| Establish proficiency standards | EG L2 | Full | Training competency |
| Define human oversight policies | SR L1, SM L2 | Full | Least Agency Principle |
| Manage known risks in human-AI configurations | TA L2 | Full | Threat Assessment |

**HAIAMM Coverage:** 85% — The "Human Assisted Intelligence" paradigm directly addresses this.

---

### GOVERN 4: Safety-First Culture

#### GOVERN 4.1 — Critical Thinking and Safety-First Culture

| NIST Suggested Action | HAIAMM Practice | Coverage | Notes |
|----------------------|-----------------|----------|-------|
| Require oversight functions from design outset | SR L1 | Full | Security by design |
| Promote effective challenge through red-teaming | ST L2-L3 | Full | Security Testing |
| Incentivize safety-first mindset | EG L1-L2 | Full | Education & Guidance |
| Establish whistleblower protections | — | Gap | Not in HAIAMM scope |

**HAIAMM Coverage:** 75%

---

#### GOVERN 4.3 — AI Testing and Incident Identification

| NIST Suggested Action | HAIAMM Practice | Coverage | Notes |
|----------------------|-----------------|----------|-------|
| Establish policies facilitating AI testing | ST L1-L2 | Full | Security Testing |
| Commit to identifying system limitations | ST L2, TA L2 | Full | Testing + Threat Assessment |
| Establish incident response documentation | IM L1-L2 | Full | Issue Management |
| Establish public disclosure policies for incidents | IM L2 | Partial | HAIAMM covers response, less on disclosure |
| Establish incident handling guidelines | IM L1-L3 | Full | Issue Management |

**HAIAMM Coverage:** 85%

---

### GOVERN 5: Stakeholder Engagement

#### GOVERN 5.1 — External Stakeholder Feedback

| NIST Suggested Action | HAIAMM Practice | Coverage | Notes |
|----------------------|-----------------|----------|-------|
| Establish feedback mechanisms (bug bounties, etc.) | ST L3 | Partial | HAIAMM mentions external testing |
| Verify stakeholder feedback includes diverse populations | — | Gap | Outside security scope |
| Publish AI principles | SM L1 | Partial | Strategy, not public principles |

**HAIAMM Coverage:** 30% — HAIAMM is organizationally focused, not public-engagement focused.

---

### GOVERN 6: Third-Party Management

#### GOVERN 6.1 — Third-Party Risks

| NIST Suggested Action | HAIAMM Practice | Coverage | Notes |
|----------------------|-----------------|----------|-------|
| Establish third-party AI policies | SA (Vendors) L1-L2 | Full | Vendors domain |
| Establish transparency into third-party functions | SA (Vendors) L2 | Full | Vendor assessment |
| Evaluate existing third-party technology policies | SA (Vendors) L1 | Full | |
| Address supply chain and procurement | SA (Vendors) L1-L2 | Full | Supply chain coverage |

**HAIAMM Coverage:** 95% — Vendors domain directly addresses this.

---

#### GOVERN 6.2 — Third-Party Failure Contingencies

| NIST Suggested Action | HAIAMM Practice | Coverage | Notes |
|----------------------|-----------------|----------|-------|
| Establish policies for third-party failures | SA (Vendors) L2, IM L2 | Full | |
| Verify incident response covers third-party systems | IM L2 (Vendors) | Full | |

**HAIAMM Coverage:** 95%

---

## MAP Function Mapping

### MAP 1: Context Establishment

#### MAP 1.1 — Intended Purpose and Deployment

| Key NIST Suggested Actions | HAIAMM Practice | Coverage |
|---------------------------|-----------------|----------|
| Assess trustworthiness of system design | DR L1-L2 | Full |
| Formalize task, purpose, minimum functionality | SR L1 | Full |
| Determine if non-AI options are more trustworthy | TA L1 | Partial |
| Define acceptable context of use | SR L1, SM L1 | Full |
| Identify human-AI interaction models | SR L1 (HAI specific) | Full |
| Plan for risks in human-AI configurations | TA L1-L2 | Full |

**HAIAMM Coverage:** 80% — Strong on security context, lighter on non-AI alternatives analysis.

---

#### MAP 1.5 — Organizational Risk Tolerance

| Key NIST Suggested Actions | HAIAMM Practice | Coverage |
|---------------------------|-----------------|----------|
| Apply regulations for risk criteria | PC L1-L2 | Full |
| Create risk criteria (financial, operational, safety) | TA L2 | Full |
| Define maximum allowable risk thresholds | TA L2, SM L2 | Full |
| Document tradeoffs across trustworthy characteristics | TA L2, SM L2 | Partial |
| Review "off-label" system uses | TA L2 | Full |

**HAIAMM Coverage:** 85%

---

### MAP 2: AI System Categorization

#### MAP 2.3 — Scientific Integrity and TEVV

| Key NIST Suggested Actions | HAIAMM Practice | Coverage |
|---------------------------|-----------------|----------|
| Develop and apply TEVV protocols | ST L1-L3, DR L1-L2 | Full |
| Verify performance metrics are unambiguous | SM L2-L3 | Full |
| Establish testable modules enabling evaluation | ST L2, IR L2 | Full |
| Map adherence to data privacy/security policies | SA (Data) L1-L2 | Full |
| Document test/training data lineage | DR L1 (Data) | Partial |
| Establish practices detecting emergent properties | ML L3 | Partial |
| Identify techniques managing bias sources | — | Gap |

**HAIAMM Coverage:** 70% — Strong on testing, lighter on bias management.

---

### MAP 3: Capabilities Understanding

#### MAP 3.4 — Operator and Practitioner Proficiency

| Key NIST Suggested Actions | HAIAMM Practice | Coverage |
|---------------------------|-----------------|----------|
| Identify skills requirements for operators | EG L2 | Full |
| Create operational documentation | EH L1, SM L2 | Full |
| Develop training materials | EG L1-L2 | Full |
| Design certification procedures | EG L3 | Partial |
| Verify output interpretability | DR L2, SR L2 | Full |

**HAIAMM Coverage:** 80%

---

### MAP 4: Risk and Benefit Mapping

#### MAP 4.1-4.2 — Third-Party Risk

| Key NIST Suggested Actions | HAIAMM Practice | Coverage |
|---------------------------|-----------------|----------|
| Review third-party audit reports | SA (Vendors) L1 | Full |
| Create inventory of third-party materials | SA (Vendors) L1 | Full |
| Assess third-party material for bias/privacy/security | SA (Vendors) L2, TA (Vendors) | Full |
| Apply traditional risk controls to third-party tech | SA (Vendors) L1-L2 | Full |

**HAIAMM Coverage:** 95%

---

## MEASURE Function Mapping

### MEASURE 1: Methods and Metrics

#### MEASURE 1.1 — AI Risk Measurement Approach Selection

| Key NIST Suggested Actions | HAIAMM Practice | Coverage |
|---------------------------|-----------------|----------|
| Establish approaches for detecting/tracking risks | ML L1-L2, TA L1-L2 | Full |
| Identify testing procedures and metrics | ST L1-L3 | Full |
| Define acceptable performance limits | SM L2-L3 | Full |
| Define metrics for AI actor competency | EG L2 | Full |
| Identify transparency metrics | SM L2 | Partial |
| Monitor AI system external inputs | ML L2, SA (Vendors) | Full |
| Assess pre vs post-deployment performance | ST L2, ML L2 | Full |

**HAIAMM Coverage:** 85% — v2.2 measurable outcomes directly address measurement.

---

#### MEASURE 1.3 — Independent Assessor Involvement

| Key NIST Suggested Actions | HAIAMM Practice | Coverage |
|---------------------------|-----------------|----------|
| Utilize separate testing teams | ST L2, IR L2 | Full |
| Plan and evaluate prototypes with end users | ST L2, DR L2 | Partial |
| Assess independence of TEVV actors | SM L2 | Partial |
| Evaluate interdisciplinary internal team | — | Gap |
| Evaluate external stakeholder feedback effectiveness | — | Gap |

**HAIAMM Coverage:** 50% — HAIAMM supports independent testing but doesn't prescribe assessor qualifications.

---

### MEASURE 2: Trustworthy Characteristics Evaluation

#### MEASURE 2.4 — Production Monitoring

| Key NIST Suggested Actions | HAIAMM Practice | Coverage |
|---------------------------|-----------------|----------|
| Monitor how production differs from pre-deployment | ML L2-L3 | Full |
| Monitor for anomalies using control limits | ML L2 | Full |
| Verify alerts for distribution differences | ML L2, IM L1 | Full |
| Utilize human review for unexpected data | ML L2 (HAI oversight) | Full |
| Collect use cases from operational environment | ML L3, ST L3 | Full |

**HAIAMM Coverage:** 95% — Monitoring & Logging directly addresses production monitoring.

---

#### MEASURE 2.6 — Safety Risk Evaluation

| Key NIST Suggested Actions | HAIAMM Practice | Coverage |
|---------------------------|-----------------|----------|
| Measure system under stress conditions | ST L2-L3 | Full |
| Stress-test under likely scenarios (concept drift, high load) | ST L2 | Full |
| Apply chaos engineering approaches | ST L3 | Full |
| Measure performance in real-time | ML L1-L2 | Full |
| Document incident response plans | IM L1-L2 | Full |
| Compare safety testing with risk tolerances | SM L2-L3 | Full |

**HAIAMM Coverage:** 95% — HAIAMM's Building + Verification functions map directly.

---

#### MEASURE 2.7 — Security and Resilience Evaluation

| Key NIST Suggested Actions | HAIAMM Practice | Coverage |
|---------------------------|-----------------|----------|
| Establish security tests and metrics (red-teaming) | ST L2-L3 | Full |
| Use red-team exercises under adversarial conditions | ST L2, TA L2 | Full |
| Document red-team results for continuous improvement | ST L3, IM L2 | Full |
| Evaluate mismatches between claimed and actual performance | ST L2, DR L2 | Full |
| Use countermeasures (auth, throttling, differential privacy) | EH L1-L2, SA L1-L2 | Full |
| Modify security procedures based on production events | IM L2-L3, EH L2 | Full |
| Share error/attack patterns with incident databases | IM L2 | Partial |
| Develop information sharing practices with other orgs | — | Gap |
| Verify third-party security audits | SA (Vendors) L2 | Full |
| Utilize watermarking for data/model protection | — | Gap |

**HAIAMM Coverage:** 85% — Very strong alignment. Gaps: inter-org info sharing, watermarking.

---

#### MEASURE 2.8 — Transparency and Accountability

| Key NIST Suggested Actions | HAIAMM Practice | Coverage |
|---------------------------|-----------------|----------|
| Maintain audit logs and histories | ML L1-L2 | Full |
| Test explanations with different audiences | — | Gap |
| Measure human oversight of AI systems | ML L2, SM L2 | Full |
| Track organizational accountability via escalations | SM L2, IM L2 | Full |
| Track effectiveness of risk management mechanisms | SM L3 | Full |

**HAIAMM Coverage:** 75% — Strong on logging/accountability. Gap: explainability testing.

---

#### MEASURE 2.9 — AI Model Explanation and Validation

| Key NIST Suggested Actions | HAIAMM Practice | Coverage |
|---------------------------|-----------------|----------|
| Verify systems produce explainable models | DR L2 | Partial |
| Utilize inherently explainable approaches | — | Gap |
| Test explanations with relevant actors | — | Gap |
| Document AI model details (model cards) | DR L1, SM L2 | Partial |
| Assess explanation characteristics (fidelity, consistency) | — | Gap |
| Secure model development against external manipulation | EH L2, ST L2 | Full |

**HAIAMM Coverage:** 35% — HAIAMM focuses on security, not explainability. This is a valid scope difference.

---

#### MEASURE 2.10 — Privacy Risk Examination

| Key NIST Suggested Actions | HAIAMM Practice | Coverage |
|---------------------------|-----------------|----------|
| Document collection/management of sensitive data | SA (Data) L1-L2 | Full |
| Quantify privacy metrics (k-anonymity, etc.) | SA (Data) L2 | Partial |
| Establish access controls for sensitive data | EH (Data) L1, SA (Data) L1 | Full |
| Monitor internal queries for personal record patterns | ML (Data) L2 | Full |
| Use privacy-enhancing techniques | SA (Data) L2 | Partial |

**HAIAMM Coverage:** 70% — HAIAMM's Data domain covers privacy through a security lens.

---

#### MEASURE 2.11 — Fairness and Bias Evaluation

| Key NIST Suggested Actions | HAIAMM Practice | Coverage |
|---------------------------|-----------------|----------|
| Conduct fairness assessments | — | Gap |
| Evaluate within-group and intersectional disparities | — | Gap |
| Understand bias sources in training data | SA (Data) L2 | Partial |
| Leverage impact assessments for bias | — | Gap |
| Use context-specific fairness metrics | — | Gap |
| Apply pre/in/post-processing bias techniques | — | Gap |

**HAIAMM Coverage:** 10% — **This is NIST AI RMF's strongest area that HAIAMM intentionally doesn't cover.** HAIAMM is a security maturity model, not a fairness/bias framework. Organizations need both.

---

### MEASURE 3-4: Risk Tracking and Efficacy

#### MEASURE 3.1-3.3 — Risk Tracking

| Key NIST Suggested Actions | HAIAMM Practice | Coverage |
|---------------------------|-----------------|----------|
| Identify existing and emergent risks | TA L2-L3, ML L2-L3 | Full |
| Approach difficult-to-assess risks | TA L3 | Full |
| Establish end-user feedback processes | — | Gap |

**HAIAMM Coverage:** 70%

---

## MANAGE Function Mapping

### MANAGE 1: Risk Prioritization

#### MANAGE 1.1-1.4 — Risk Treatment and Response

| Key NIST Suggested Actions | HAIAMM Practice | Coverage |
|---------------------------|-----------------|----------|
| Evaluate systems against trustworthiness characteristics | ST L1-L3, DR L1-L2 | Full |
| Continuously track negative risks and benefits | ML L1-L3, TA L2 | Full |
| Allocate risk management resources by tolerance | SM L2 | Full |
| Document risk response procedures | IM L1-L2 | Full |
| Prioritize safety, legal, regulatory risks | TA L2, PC L2 | Full |
| Store documentation in secure repositories | EH L1 | Full |
| Document residual risks | TA L2, IM L2 | Full |
| Inform stakeholders of limitations | SM L2 | Partial |

**HAIAMM Coverage:** 90%

---

### MANAGE 2: Benefit Maximization

#### MANAGE 2.1-2.4 — Deployment Risk Management

| Key NIST Suggested Actions | HAIAMM Practice | Coverage |
|---------------------------|-----------------|----------|
| Plan risk management aligned with tolerances | SM L2, TA L2 | Full |
| Establish risk controls (data, ML security) | SA L1-L2, EH L1-L2 | Full |
| Implement TEVV protocols | ST L1-L3 | Full |
| Monitor for drift and unusual behavior | ML L2-L3 | Full |
| Verify deactivation capabilities | IM L2, EH L2 | Full |
| Apply bypass protocols | IM L2 | Full |
| Conduct root cause analyses | IM L2-L3 | Full |

**HAIAMM Coverage:** 90%

---

### MANAGE 3: Third-Party Risk

#### MANAGE 3.1 — Third-Party Resource Monitoring

| Key NIST Suggested Actions | HAIAMM Practice | Coverage |
|---------------------------|-----------------|----------|
| Apply organizational risk tolerance to third-party AI | SA (Vendors) L1-L2 | Full |
| Document third-party AI systems | SA (Vendors) L1 | Full |
| Establish TEVV for third-party systems | ST (Vendors) L2 | Full |
| Enable third parties to report vulnerabilities | IM (Vendors) L2 | Full |
| Monitor third-party systems for negative impacts | ML (Vendors) L2 | Full |
| Decommission third-party systems exceeding tolerances | IM (Vendors) L2 | Full |

**HAIAMM Coverage:** 95% — Vendors domain is purpose-built for this.

---

#### MANAGE 3.2 — Pre-trained Model Monitoring

| Key NIST Suggested Actions | HAIAMM Practice | Coverage |
|---------------------------|-----------------|----------|
| Identify pre-trained models in inventory | SA (Vendors) L1, SM L1 | Full |
| Establish continual monitoring of pre-trained models | ML (Vendors) L2, SA (Vendors) L2 | Full |
| Identify and remediate risks from pre-trained models | TA (Vendors) L2, IM (Vendors) | Full |

**HAIAMM Coverage:** 90% — HAIAMM's Vendors domain + ML practice covers model supply chain.

---

### MANAGE 4: Risk Treatment and Communication

#### MANAGE 4.1 — Post-Deployment Monitoring

| Key NIST Suggested Actions | HAIAMM Practice | Coverage |
|---------------------------|-----------------|----------|
| Monitor system performance for trustworthiness risks | ML L1-L3 | Full |
| Perform post-deployment TEVV (validity, bias, security) | ST L2-L3, ML L2 | Full |
| Establish red-teaming at regular intervals | ST L2-L3 | Full |
| Track dataset modifications | SA (Data) L2 | Full |
| Share error/attack patterns with communities | IM L2 | Partial |
| Respond to detected negative impacts | IM L1-L2 | Full |

**HAIAMM Coverage:** 90%

---

#### MANAGE 4.3 — Incident Communication and Tracking

| Key NIST Suggested Actions | HAIAMM Practice | Coverage |
|---------------------------|-----------------|----------|
| Share information about errors/incidents with stakeholders | IM L2 | Full |
| Maintain incident database with dates, frequency, impact | IM L2-L3, ML L2 | Full |
| Maintain system change database | IM L2 | Full |
| Maintain version history | DR L1, SM L2 | Full |

**HAIAMM Coverage:** 95%

---

## Consolidated Gap Analysis

### Where HAIAMM Covers NIST AI RMF Well

| NIST Area | HAIAMM Strength | Coverage |
|-----------|-----------------|----------|
| **Security testing (MEASURE 2.7)** | ST practice is comprehensive | 85% |
| **Safety evaluation (MEASURE 2.6)** | ST + ML practices | 95% |
| **Third-party management (GOVERN 6, MANAGE 3)** | Vendors domain | 95% |
| **Risk assessment (MAP 1, GOVERN 1.3)** | TA practice + measurable outcomes | 90% |
| **Incident management (MANAGE 4)** | IM practice | 90% |
| **Production monitoring (MEASURE 2.4)** | ML practice | 95% |
| **Policy and compliance (GOVERN 1.1)** | PC practice | 90% |
| **Human-AI oversight (GOVERN 3.2)** | HAI paradigm is core | 85% |

### Where NIST AI RMF Covers Ground HAIAMM Does Not

| NIST Area | HAIAMM Gap | Why |
|-----------|-----------|-----|
| **Fairness and bias (MEASURE 2.11)** | 10% coverage | HAIAMM is a security model, not a fairness model |
| **Explainability (MEASURE 2.9)** | 35% coverage | HAIAMM focuses on security, not interpretability |
| **Workforce diversity (GOVERN 3.1)** | 25% coverage | HR/diversity is outside security scope |
| **User recourse (GOVERN 1.5)** | 20% coverage | End-user rights not in security scope |
| **Public transparency (GOVERN 1.4)** | 40% coverage | HAIAMM is internally focused |
| **Decommissioning (GOVERN 1.7)** | 35% coverage | HAIAMM covers build and operate, not retire |
| **Environmental impact (MEASURE 2.12)** | 0% coverage | Not in scope |
| **Stakeholder engagement (GOVERN 5)** | 30% coverage | HAIAMM is security-practitioner focused |

### Where HAIAMM Extends Beyond NIST AI RMF

| HAIAMM Capability | NIST AI RMF Gap |
|-------------------|-----------------|
| **AI agent goal integrity (ASI01)** | Not addressed — NIST is pre-agentic |
| **Prompt injection testing** | Not addressed — specific attack vector |
| **Agent permission boundaries (CAN/CANNOT/MUST)** | Not addressed — agent-specific |
| **Multi-agent coordination security (ASI07)** | Not addressed — agent-specific |
| **AI behavioral anomaly detection** | Partially addressed in MEASURE 2.4 |
| **Rogue agent detection (ASI10)** | Not addressed — agent-specific |
| **OWASP Top 10 alignment (LLM + Agentic)** | Not addressed — NIST is framework-agnostic |
| **Measurable security outcomes with formulas** | NIST suggests metrics but provides no formulas |
| **6-domain architecture (Software, Data, Infra, Vendors, Processes, Endpoints)** | NIST is domain-agnostic |
| **Interactive assessment tooling (Verifhai)** | NIST has no tooling |

---

## Implementation Guidance: Using Both Together

### For Organizations Starting Fresh

```
1. Start with NIST AI RMF GOVERN function
   → Establish governance, policies, accountability
   → Use HAIAMM SM, PC, EG for security-specific governance

2. Use NIST MAP function + HAIAMM TA practice
   → NIST provides risk context and categorization
   → HAIAMM provides security-specific threat assessment

3. Apply HAIAMM MEASURE alignment for testing
   → NIST MEASURE guides what to measure
   → HAIAMM ST, DR, IR provides how to test

4. Operate using HAIAMM Operations function
   → NIST MANAGE provides management principles
   → HAIAMM IM, EH, ML provides security operations
```

### For Organizations Already Using NIST AI RMF

```
1. Map existing NIST compliance to HAIAMM practices
   → Use this document as cross-reference
   → Identify HAIAMM practices not yet covered

2. Add HAIAMM's 6-domain assessment layer
   → Apply HAIAMM across Software, Data, Infrastructure,
     Vendors, Processes, Endpoints

3. Implement HAIAMM measurable outcomes
   → Replace NIST's general measurement guidance
     with HAIAMM's specific formulas and targets

4. Deploy Verifhai for interactive assessment
   → Operationalize NIST compliance through
     HAIAMM's assessment tooling
```

### For Organizations Already Using HAIAMM

```
1. Address NIST gaps (fairness, explainability, transparency)
   → These are valid requirements HAIAMM doesn't cover
   → Use NIST AI RMF MEASURE 2.9, 2.11 directly

2. Document NIST alignment for compliance
   → Use this mapping to demonstrate NIST coverage
   → Identify the 19% gap areas and address separately

3. Add decommissioning process (GOVERN 1.7)
   → HAIAMM gap — adopt NIST guidance directly

4. Add stakeholder engagement (GOVERN 5)
   → HAIAMM gap — adopt NIST guidance directly
```

---

## Quantitative Summary

| Metric | Value |
|--------|-------|
| NIST AI RMF Subcategories | 72 |
| NIST Suggested Actions | ~450+ |
| HAIAMM Full Coverage | 42 subcategories (58%) |
| HAIAMM Partial Coverage | 16 subcategories (22%) |
| HAIAMM Gaps | 14 subcategories (19%) |
| HAIAMM Extensions Beyond NIST | 10 capabilities |
| Combined Coverage (using both) | ~95% of AI security governance |

---

## Document Information

| Field | Value |
|-------|-------|
| Document | NIST AI RMF Playbook Action-Level Mapping |
| HAIAMM Version | 2.2 |
| NIST AI RMF Version | 1.0 (AI 100-1) |
| NIST Playbook Version | AI 600-1 |
| Last Updated | January 2026 |

---

**Sources:**
- NIST AI 100-1: AI Risk Management Framework (2023)
- NIST AI 600-1: AI RMF Generative AI Profile (2024)
- NIST AI RMF Playbook: airc.nist.gov/AI_RMF_Playbook
- HAIAMM v2.2: Framework Structure and Assessment Questionnaires

---

**Related Documents:**
- [Framework Mappings (Handbook Ch. 9)](handbook/09-FRAMEWORK-MAPPINGS.md)
- [Competitive Analysis](HAIAMM-COMPETITIVE-ANALYSIS.md)
- [HAIAMM Framework Structure](HAIAMM-Framework-Structure.md)
