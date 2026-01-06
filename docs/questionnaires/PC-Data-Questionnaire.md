# Policy & Compliance (PC) - Data Domain
## HAIAMM Assessment Questionnaire v2.0

**Practice:** Policy & Compliance (PC)
**Domain:** Data
**Purpose:** Assess organizational maturity in policies and compliance for Human Assisted Intelligence data security and privacy operations

---

## Instructions

- Answer each question honestly based on **current, implemented practices** (not plans or aspirations)
- **"Yes" requires evidence** - Document proof for each affirmative answer
- **Answer progressively** - Complete all Level 1 questions before Level 2
- **Level progression** - Achieve ALL questions at lower level before advancing
- **Partial implementation = "No"** - Practice must be complete and systematic

---

## Level 1: Foundational
**Objective:** Establish foundational policies for AI-operated data security and identify privacy compliance requirements

### Question 1: AI Agent Data Security Policies and Privacy Principles

**Q1.1:** Have you established documented policies governing AI agent operations in data security and privacy (defining AI agent scope, data access boundaries, privacy-by-design requirements, human oversight for sensitive data, data subject rights support, audit trail requirements) with alignment to privacy principles (data minimization, purpose limitation, transparency)?

**Evidence Required:**
- [ ] AI Agent Data Security Policies documented:
  - AI Agent Scope: Defined which data security functions AI may perform (data discovery/classification, access anomaly detection, DLP enforcement, privacy compliance scanning)
  - Data Access Boundaries: Specified what data AI can access and for what purposes (AI can read data for classification but cannot transmit outside organization)
  - Privacy-by-Design Requirements:
    - Data minimization (AI doesn't collect more data than needed for security)
    - Purpose limitation (AI uses data only for security, not other purposes)
  - Human Oversight for Sensitive Data:
    - PII, PHI, financial data classifications require human validation
    - AI can auto-classify public data, must escalate sensitive data for review
  - Data Subject Rights Support:
    - AI systems support subject access requests (GDPR Article 15)
    - AI systems support right to erasure (GDPR Article 17)
    - AI systems support right to explanation of AI decisions affecting individuals (GDPR Article 22)
  - Audit Trail Requirements:
    - All AI data security decisions logged (classifications, access detections, privacy violations)
    - Logs include: what AI decision, which data, timestamp, user context
- [ ] Example Policy Statements:
  - "AI agents may autonomously classify data assets but require human review for Restricted/Highly Confidential designations"
  - "AI data security agents must not transmit data outside organizational boundaries except to approved security vendors under DPA"
  - "All AI data classification decisions must be explainable to data subjects upon request"
  - "AI access anomaly detection must preserve user privacy (aggregate analysis, not individual surveillance)"
- [ ] Privacy Principles Alignment:
  - Transparency: Data subjects informed that AI monitors their data access (privacy notice updates)
  - Lawful Basis: Lawful basis for AI processing personal data documented (Legitimate interest under GDPR Article 6(1)(f)?)
  - Accountability: Policies approved by Data Protection Officer or privacy team
- [ ] Policies communicated to all stakeholders (security team, data owners, privacy team, legal)
- [ ] Evidence of policy implementation (policies published, training conducted, policy acknowledgments)

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

### Question 2: Privacy Regulation Identification and Compliance Mapping

**Q1.2:** Have you identified and documented applicable privacy regulations and data protection frameworks (GDPR, CCPA/CPRA, HIPAA, PCI-DSS, PIPEDA, industry standards) with specific requirements mapped to AI-operated data security functions, including lawful basis, transparency requirements, automated decision-making considerations, DPIA requirements, and cross-border transfer safeguards?

**Evidence Required:**
- [ ] Privacy Regulation Identification:
  - Geographic Regulations: GDPR (EU), CCPA/CPRA (California), PIPEDA (Canada), LGPD (Brazil), Privacy Act (Australia)
  - Sector-Specific: HIPAA (healthcare), GLBA (financial), FERPA (education), COPPA (children's data)
  - Industry Standards: PCI-DSS (payment card data), ISO 27701 (privacy management), NIST Privacy Framework
  - Contractual: Data Processing Agreements (DPAs), customer privacy commitments, vendor privacy requirements
  - All applicable regulations documented with justification
- [ ] Compliance Mapping to AI Data Security:
  - Lawful Basis: What is lawful basis for AI processing personal data for security?
    - GDPR Article 6(1)(f) legitimate interest? Balancing test documented?
    - Other lawful basis (consent, contract, legal obligation)?
  - Transparency Requirements:
    - How are data subjects informed about AI data monitoring?
    - Privacy notice updated to describe AI data security operations?
  - Automated Decision-Making (GDPR Article 22):
    - Do AI data security decisions constitute "automated decision-making" requiring human review?
    - Right to human review documented and available?
  - Data Protection Impact Assessment (DPIA):
    - Is DPIA required for AI data security? (GDPR Article 35 - likely yes for large-scale monitoring)
    - DPIA initiated or completed?
  - Cross-Border Transfers:
    - If AI tools are SaaS, do they transfer data across borders?
    - Standard Contractual Clauses or other transfer mechanisms in place?
- [ ] Compliance Requirements Documented:
  - Specific requirements from each applicable regulation
  - Requirements mapped to AI data security capabilities
  - Gaps identified (requirements AI doesn't meet, requiring manual processes or policy exceptions)
- [ ] Documentation reviewed within last 12 months
- [ ] Evidence of compliance mapping (compliance matrix, gap analysis, DPIA initiation)

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

### Question 3: Basic Audit Trail and Privacy Compliance Documentation

**Q1.3:** Do you maintain basic audit trail capability for all AI data security decisions (comprehensive logging of classifications, access decisions, privacy detections with retention aligned to regulatory requirements) and have initiated Data Protection Impact Assessment (DPIA) for AI data security operations with documented privacy risks and initial mitigation measures?

**Evidence Required:**
- [ ] Basic Audit Trail Capability:
  - Comprehensive Logging of AI Data Security Decisions:
    - Data classification decisions (what data classified, what classification assigned, AI confidence score, timestamp)
    - Access anomaly detections (who accessed what data, what anomaly detected, AI risk score)
    - Privacy violation detections (what privacy violation, which data, which regulation, AI assessment)
    - DLP enforcement actions (what data blocked, what policy violated, AI decision)
  - Log Contents:
    - What AI decision was made
    - Which data was involved (data asset identifier, not full data contents)
    - Timestamp and user context
    - AI system that made decision
    - Human override if applicable
  - Log Retention:
    - Aligned to regulatory requirements (GDPR: typically 1-3 years, HIPAA: 6 years, PCI-DSS: 1 year)
    - Longer retention for compliance-critical logs
  - Log Access Controls:
    - Restricted access to audit logs (privacy team, security team, auditors only)
    - Audit log access itself is logged
  - Log Integrity Protection:
    - Write-once storage or log signing
    - Protection against tampering
- [ ] DPIA for AI Data Security Initiated/Completed:
  - DPIA Document exists (GDPR Article 35 requirement for large-scale monitoring)
  - DPIA Components:
    - Necessity Assessment: Is AI data security processing necessary and proportionate?
    - Risk Assessment: Privacy risks identified (excessive surveillance, algorithmic bias, data breaches from AI)
    - Mitigation Measures: Safeguards documented (access controls, encryption, data minimization, human oversight)
    - Consultation: Data Protection Officer (DPO) or privacy team consulted
    - Public Interest Balance: Legitimate interest in security balanced against individual privacy rights
  - Privacy Risks Documented:
    - Risk of excessive data collection/surveillance
    - Risk of algorithmic bias in AI data classification
    - Risk of data breach from AI system compromise
    - Risk of privacy rights violations (inability to explain AI decisions, inability to delete data)
  - Initial Mitigation Measures:
    - Data minimization enforced
    - Human oversight for sensitive data
    - Encryption and access controls
    - Audit trails for accountability
- [ ] Privacy Compliance Documentation:
  - Records of Processing Activities (ROPA) started for AI data security (GDPR Article 30)
  - Privacy notices updated to describe AI data monitoring
  - Data subject rights procedures drafted (how to handle rights requests involving AI)
- [ ] Evidence of audit trails and DPIA (log samples, DPIA document, privacy documentation)

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

**Level 1 Score:** _____ / 3 questions answered "Yes"

**Level 1 Achieved:** ☐ Yes (3/3) ☐ No (< 3/3)

---

## Level 2: Comprehensive
**Objective:** Implement comprehensive data protection policies with privacy-by-design governance and regular privacy compliance validation

**Prerequisites:** ALL Level 1 questions must be "Yes" to proceed to Level 2

### Question 4: Comprehensive Data Protection Policies and Privacy-by-Design Governance

**Q2.1:** Have you implemented comprehensive data protection policies with data sensitivity-based AI governance (different AI autonomy for public vs. PII vs. PHI data), purpose limitation enforcement, data minimization requirements, defined retention policies, third-party AI vendor governance, and privacy-enhancing technical controls (pseudonymization, encryption, access controls, automated retention enforcement)?

**Evidence Required:**
- [ ] Comprehensive Data Protection Policies:
  - Data Sensitivity-Based AI Governance:
    - Public Data: AI can auto-classify autonomously
    - PII (Personally Identifiable Information): AI flags, human validates classification
    - PHI (Protected Health Information): AI flags, human validates + privacy team approval
    - Financial/Payment Data: AI flags, human validates + compliance team approval
    - Different autonomy levels documented for each data tier
  - Purpose Limitation Enforcement:
    - AI agents can only use data for stated security purposes
    - AI cannot repurpose security data for marketing, analytics beyond security, or other purposes
    - Technical controls enforce purpose limitation
  - Data Minimization Requirements:
    - AI data security tools collect minimum data necessary
    - Access logs: yes (necessary for security)
    - Full packet capture: only when justified and approved
    - User personal details: only when needed for investigation
  - Retention Policies Defined:
    - How long AI systems retain data used for security analysis
    - Aligned to GDPR storage limitation principle
    - Automated deletion after retention period
    - Different retention for different data types (access logs: 90 days, incident data: 1 year, compliance logs: per regulation)
  - Third-Party AI Vendor Governance:
    - Vendor Data Processing Agreements (DPAs) required for all SaaS AI data security tools
    - DPAs include data transfer safeguards (Standard Contractual Clauses if cross-border)
    - Vendor security assessments conducted
    - Vendor compliance certifications validated (SOC 2, ISO 27001, ISO 27701)
  - Data Subject Rights Procedures:
    - How to provide Article 15 access to AI classification decisions
    - How to delete data from AI systems per Article 17
    - How to explain AI decisions per Article 22
    - How to object to AI processing per Article 21
    - Procedures documented, tested, and operational
- [ ] Privacy-Enhancing Technical Controls:
  - Pseudonymization/Anonymization: Data pseudonymized in AI security analysis where possible
  - Encryption: Data at rest and in transit encrypted in AI systems (AES-256, TLS 1.3)
  - Access Controls: AI agent access limited to minimum necessary data (RBAC, least privilege)
  - Automated Retention Enforcement: AI security logs automatically deleted per retention schedule
  - Audit logging of privacy-sensitive operations
- [ ] Policies reviewed and approved by privacy team, legal, and Data Protection Officer (if applicable)
- [ ] Evidence of comprehensive policies and technical controls (policy documents, DPAs, retention configurations, encryption evidence)

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

### Question 5: Completed DPIA and Regular Privacy Compliance Validation

**Q2.2:** Have you completed Data Protection Impact Assessment (DPIA) for AI data security with documented necessity assessment, risk assessment, mitigation measures, DPO consultation, and public interest balancing, and do you conduct regular privacy compliance validation (quarterly internal audits, annual privacy assessments, vendor privacy assessments, data subject rights tracking, privacy incident response integration)?

**Evidence Required:**
- [ ] Completed DPIA for AI Data Security:
  - DPIA Document completed (GDPR Article 35)
  - Necessity Assessment:
    - Is AI data security processing necessary and proportionate?
    - Can security be achieved without AI monitoring?
    - Documented justification for AI use
  - Risk Assessment:
    - Privacy risks identified and assessed:
      - Excessive surveillance risk
      - Algorithmic bias in access decisions risk
      - Data breach from AI system compromise risk
      - Privacy rights violation risk
    - Risk likelihood and impact quantified
  - Mitigation Measures:
    - Safeguards documented and implemented:
      - Access controls limiting AI data access
      - Encryption protecting data in AI systems
      - Data minimization enforced
      - Human oversight for sensitive decisions
      - Audit trails for accountability
    - Residual risks accepted by stakeholders
  - DPO Consultation:
    - Data Protection Officer consulted (GDPR requirement)
    - DPO sign-off on DPIA
  - Public Interest Balance:
    - Legitimate interest in security weighed against individual privacy rights (GDPR Article 6(1)(f))
    - Balancing test documented
    - Conclusion: Legitimate interest justified or alternative lawful basis used
  - DPIA reviewed and updated at least annually or when AI capabilities change
- [ ] Regular Privacy Compliance Validation:
  - Quarterly Internal Privacy Audits:
    - Sample AI classification decisions (verify accuracy, human oversight compliance)
    - Review data access logs (verify AI only accesses authorized data)
    - Validate data minimization (verify AI not collecting excessive data)
    - Check retention policy enforcement (verify automated deletion working)
  - Annual Privacy Assessments:
    - Comprehensive review of AI data security privacy compliance
    - Third-party privacy assessment (optional but recommended)
    - Privacy certification audit (ISO 27701, Privacy Shield, TrustArc)
  - Vendor Privacy Assessments:
    - Annual review of AI data security vendor privacy practices
    - DPA compliance validated
    - Vendor security certifications reviewed
    - Data transfer mechanisms validated (SCCs, adequacy decisions)
  - Data Subject Rights Fulfillment Tracking:
    - Track and respond to rights requests involving AI systems
    - Article 15 access requests: Provide AI classification decisions (SLA: ≤30 days)
    - Article 17 erasure requests: Delete data from AI systems (SLA: ≤30 days)
    - Article 22 automated decision-making objections: Provide human review
    - Rights request metrics: Volume, response time, fulfillment rate
  - Privacy Incident Response Integration:
    - AI data security systems included in privacy breach response plans
    - If AI system breached, notification procedures per GDPR Article 33/34 (authority notification ≤72 hours)
    - Privacy breach drills include AI system scenarios
- [ ] Records of Processing Activities (ROPA) maintained for AI data security (GDPR Article 30)
- [ ] Evidence of DPIA and validation activities (DPIA document, audit reports, rights request logs, incident response plans)

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

### Question 6: Privacy Metrics and Compliance Reporting

**Q2.3:** Do you maintain comprehensive privacy metrics for AI data security operations (data minimization compliance, retention policy enforcement, data subject rights response SLAs, privacy incident rates) and provide regular privacy compliance reporting to stakeholders (quarterly reports to privacy team, annual reports to leadership/board, regulatory reporting as required)?

**Evidence Required:**
- [ ] Comprehensive Privacy Metrics:
  - Data Minimization Compliance:
    - % of AI data collection justified by necessity
    - Data reduction achieved (e.g., "AI collects 70% less data than full packet capture")
    - Unnecessary data collection incidents (target: zero)
  - Retention Policy Enforcement:
    - % of data deleted on schedule (target: 100%)
    - Overretention incidents (target: zero)
    - Automated deletion success rate
  - Data Subject Rights Response:
    - Rights request volume (access, erasure, objection, explanation)
    - Response time (SLA: ≤30 days per GDPR Article 12)
    - Fulfillment rate (target: 100% for valid requests)
    - Rights request types breakdown
  - Privacy Incident Rates:
    - Privacy breaches involving AI systems (target: zero critical)
    - Regulatory notifications made (GDPR Article 33/34)
    - Privacy near-misses (caught before breach)
  - AI Decision Transparency:
    - % of AI decisions that can be explained (target: 100%)
    - Explainability accuracy (human reviewers agree with AI explanation)
  - Vendor Compliance:
    - % of AI vendors with current DPAs (target: 100%)
    - % of vendors with privacy certifications (target: ≥80%)
- [ ] Privacy Compliance Reporting:
  - Quarterly Reports to Privacy Team/DPO:
    - Privacy metrics summary
    - Compliance validation results
    - Data subject rights fulfillment
    - Privacy incidents and near-misses
    - DPIA updates
  - Annual Reports to Leadership/Board:
    - Privacy compliance status (GDPR, CCPA, HIPAA, etc.)
    - Privacy program maturity
    - Privacy risks and mitigations
    - Privacy incidents and regulatory actions
    - Privacy investment and ROI
  - Regulatory Reporting:
    - Privacy breach notifications (GDPR Article 33/34, CCPA, HIPAA Breach Notification Rule)
    - Supervisory authority inquiries responded to
    - DPIA provided to authority if requested (GDPR Article 36)
- [ ] Privacy dashboard accessible to stakeholders (real-time compliance metrics)
- [ ] Evidence of metrics tracking and reporting (metrics dashboard, quarterly reports, annual reports)

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

**Level 2 Score:** _____ / 3 questions answered "Yes"

**Level 2 Achieved:** ☐ Yes (3/3) ☐ No (< 3/3)

---

## Level 3: Industry-Leading
**Objective:** Achieve continuous privacy compliance with privacy-enhancing technologies and lead industry privacy standards for AI

**Prerequisites:** ALL Level 2 questions must be "Yes" to proceed to Level 3

### Question 7: Privacy-by-Default Automation and Continuous Compliance Monitoring

**Q3.1:** Have you implemented privacy-by-default automation with continuous compliance monitoring (real-time privacy dashboards, automated privacy control testing, privacy-as-code, automated rights request handling, privacy drift detection, automated DPIA updates) achieving ≥99% privacy compliance with real-time visibility?

**Evidence Required:**
- [ ] Privacy-by-Default Automation:
  - Real-Time Privacy Dashboards:
    - Live visibility into AI data security privacy compliance status
    - GDPR compliance controls: passing/failing status
    - Data subject rights response SLAs: on-time performance
    - DPIA mitigation status: implemented/not implemented
    - Privacy metrics updated in real-time
  - Automated Privacy Control Testing:
    - Continuous validation of privacy safeguards
    - AI agents accessing only authorized data (automated testing)
    - Retention policies enforced (automated verification)
    - Pseudonymization applied where required (automated checking)
    - Test results: pass/fail with alerting on failures
  - Privacy-as-Code:
    - Data protection policies codified and automatically enforced
    - AI agents cannot violate privacy policies due to technical controls (not just policy documentation)
    - Policy changes deployed as code updates
    - Policy compliance verified through automated tests
  - Automated Rights Request Handling:
    - AI-assisted response to data subject rights (not fully automated, but AI-assisted)
    - Automated Article 15 data access reports (AI generates report of data held, human reviews)
    - Automated Article 17 erasure from AI systems (AI executes deletion, human verifies)
    - Faster rights request response (target: ≤7 days vs. ≤30 day legal requirement)
  - Privacy Drift Detection:
    - Immediate alerting when AI data security operations drift from privacy requirements
    - Real-time monitoring of AI behavior against privacy policies
    - Automated remediation or human escalation on drift
  - Automated DPIA Updates:
    - Continuous DPIA refresh as AI data security capabilities evolve
    - Automated risk reassessment when AI changes
    - DPIA always current (not annual review, but continuous)
- [ ] Privacy Compliance Metrics:
  - ≥99% privacy compliance with regulatory requirements
  - Real-time visibility into compliance status
  - Zero critical privacy violations
  - Privacy drift detected and resolved within ≤24 hours
- [ ] Evidence of automation and continuous monitoring (real-time dashboards, automated test results, privacy-as-code repositories, DPIA automation)

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

### Question 8: Privacy-Enhancing Technologies (PETs) Implementation

**Q3.2:** Have you implemented privacy-enhancing technologies (PETs) in AI data security including ≥2 advanced PETs (differential privacy, federated learning, homomorphic encryption, secure multi-party computation, zero-knowledge proofs) with documented privacy benefits and use cases?

**Evidence Required:**
- [ ] Privacy-Enhancing Technologies Implemented (≥2 of the following):
  - Differential Privacy:
    - Add statistical noise to AI data security analytics
    - Protect individual privacy while preserving security insights
    - Use Case: Aggregate access pattern analysis without revealing individual behavior
    - Privacy Benefit: Individual data cannot be re-identified from aggregated reports
    - Implementation: Differential privacy libraries (Google DP, OpenDP, IBM diffprivlib)
    - Epsilon parameter tuned for privacy-utility tradeoff
  - Federated Learning:
    - Train AI security models on decentralized data without centralizing sensitive data
    - Use Case: Train AI access anomaly detection across multiple data silos without centralizing logs
    - Privacy Benefit: Raw data never leaves data silo, only model updates shared
    - Implementation: TensorFlow Federated, PySyft, Flower
  - Homomorphic Encryption:
    - Analyze encrypted data for security purposes without decrypting
    - Use Case: AI classifies encrypted data without seeing plaintext (emerging capability)
    - Privacy Benefit: AI never accesses plaintext, even during analysis
    - Implementation: Microsoft SEAL, PALISADE, HElib
  - Secure Multi-Party Computation (SMPC):
    - Collaborate on security threat intelligence without sharing raw data
    - Use Case: Multi-organization threat intelligence sharing without revealing individual data
    - Privacy Benefit: Aggregate intelligence derived without any party seeing others' data
    - Implementation: MP-SPDZ, FRESCO, Sharemind
  - Zero-Knowledge Proofs:
    - Prove AI data security properties without revealing underlying data
    - Use Case: Prove compliance (e.g., "all PII is encrypted") without revealing PII
    - Privacy Benefit: Verifiable compliance without data disclosure
    - Implementation: zk-SNARKs, zk-STARKs libraries
- [ ] PET Implementation Documentation:
  - Use cases documented for each PET
  - Privacy benefits quantified (e.g., "differential privacy reduces re-identification risk by 95%")
  - Trade-offs documented (utility loss, performance impact)
  - Validation: Privacy guarantees tested and verified
- [ ] Privacy Team Approval:
  - Privacy team validated PET implementations provide meaningful privacy protection
  - Not just "privacy theater" but real privacy enhancement
- [ ] Evidence of PETs improving privacy (implementation documentation, privacy benefit quantification, validation results)

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

### Question 9: Privacy Standards Leadership and Industry Contribution

**Q3.3:** Does your organization lead industry development of privacy-preserving AI data security standards through regulatory engagement, standards development participation, published transparency reports (at least annually), open-source privacy tools contributions, and achieved third-party privacy certification (ISO 27701 or equivalent) with documented industry impact?

**Evidence Required:**
- [ ] Regulatory Engagement:
  - Participate in privacy regulator consultations on AI
  - Respond to ICO, CNIL, EDPB, FTC guidance requests on AI privacy
  - Participate in regulatory sandbox programs (ICO Sandbox, Singapore PDPC Sandbox)
  - Engage with regulators proactively (not just reactively when investigated)
  - Documented regulator interactions (consultation responses, sandbox participation)
- [ ] Standards Development Participation:
  - Contribute to privacy standards for AI:
    - ISO/IEC 27701 (Privacy Information Management)
    - IEEE AI Ethics Standards
    - NIST Privacy Framework AI extensions
    - OWASP AI Security and Privacy Guide
  - Active participation (not just passive membership)
  - Contributions documented (standards proposals, working group participation)
- [ ] Published Transparency Reports (at least annually):
  - Annual transparency report on AI data security operations
  - Contents:
    - How many data subjects monitored by AI
    - Data subject rights requests received and fulfilled (volume, type, response time)
    - AI privacy incidents (if any)
    - Privacy compliance metrics
    - DPIA summaries
  - Public evidence (transparency report URL, accessible to customers and regulators)
- [ ] Open-Source Privacy Tools Contributions:
  - Contribute privacy-preserving AI data security tools to open source
  - Examples:
    - Differential privacy libraries for security analytics
    - Federated learning frameworks for data security
    - Privacy-as-code policy enforcement tools
    - Automated DPIA tools
  - Open-source repositories published (GitHub, etc.)
  - Community adoption (downloads, forks, stars, contributions from others)
- [ ] Third-Party Privacy Certification Achieved:
  - ISO 27701 certification for AI data security operations
  - Or equivalent: Privacy by Design Certification, TrustArc/IAPP certifications
  - Certification scope includes AI data security
  - Certification current (not expired)
  - Certificate evidence and public validation
- [ ] Adoption of Emerging Privacy Standards:
  - Privacy-by-Design Frameworks (Ann Cavoukian's 7 Foundational Principles)
  - Algorithmic Fairness Standards (NIST AI RMF, IEEE Ethically Aligned Design)
  - Explainability Standards (XAI for data classification decisions)
  - Privacy Governance Frameworks (OECD AI Principles, EU Ethics Guidelines for Trustworthy AI)
- [ ] Documented Industry Impact:
  - Other organizations adopting your privacy practices or tools
  - Industry standards incorporating your contributions
  - Regulatory guidance influenced by your engagement
  - Recognition as privacy thought leader (conference invitations, awards)
- [ ] Internal Privacy Excellence Program:
  - Privacy champions within organization
  - Privacy innovation encouraged and rewarded
  - Continuous privacy improvement culture

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

**PC-Data Practice Score:** _______ / 3.0

### Precise Scoring (For Formal Audits)

```
L1_score = (L1 "Yes" answers) / 3
L2_score = (L2 "Yes" answers) / 3 × L1_score
L3_score = (L3 "Yes" answers) / 3 × L2_score

Practice Score = L1_score + L2_score + L3_score
```

**PC-Data Practice Score (Precise):** _______ / 3.0

---

## Assessment Summary

**Assessment Date:** _________________________________

**Assessor(s):** _____________________________________

**HAI System(s) Assessed:** __________________________

**Data Assets in Scope:** ____________________________

**Overall Maturity Level:**
- ☐ Level 0 (Score < 1.0): Ad-hoc, no formal privacy policies for AI data security
- ☐ Level 1 (Score 1.0 - 1.9): Foundational policies, privacy regulations identified, basic audit trails
- ☐ Level 2 (Score 2.0 - 2.9): Comprehensive data protection policies, completed DPIA, regular privacy validation
- ☐ Level 3 (Score 3.0): Continuous privacy compliance, PETs implemented, industry leadership

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

## Policy & Compliance Specific Notes (Data Domain)

**AI Agent Data Security Policies:**
- [ ] AI agent scope defined (classification, access detection, DLP, privacy scanning)
- [ ] Data access boundaries (what data AI can access, for what purposes)
- [ ] Privacy-by-design (data minimization, purpose limitation, transparency)
- [ ] Human oversight for sensitive data (PII, PHI, financial require human review)
- [ ] Data subject rights support (access, erasure, explanation, objection)
- [ ] Audit trail requirements (all AI decisions logged)

**Privacy Regulations Identified:**
- [ ] GDPR (EU) - if applicable
- [ ] CCPA/CPRA (California) - if applicable
- [ ] HIPAA (healthcare) - if applicable
- [ ] PCI-DSS (payment data) - if applicable
- [ ] Other geographic/sector regulations as applicable
- [ ] Industry standards (ISO 27701, NIST Privacy Framework)

**Compliance Mapping:**
- [ ] Lawful basis documented (GDPR Article 6)
- [ ] Transparency requirements (privacy notices updated)
- [ ] Automated decision-making considerations (GDPR Article 22)
- [ ] DPIA requirements (GDPR Article 35)
- [ ] Cross-border transfer safeguards (SCCs, adequacy decisions)

**Audit Trails (Level 1):**
- [ ] All AI data security decisions logged
- [ ] Retention aligned to regulations (1-6 years depending on regulation)
- [ ] Log access controls and integrity protection

**DPIA Components:**
- [ ] Necessity assessment (is AI processing necessary?)
- [ ] Risk assessment (surveillance, bias, breach, rights violations)
- [ ] Mitigation measures (access controls, encryption, minimization, oversight)
- [ ] DPO consultation
- [ ] Public interest balancing (legitimate interest test)

**Level 2 Comprehensive Policies:**
- [ ] Data sensitivity-based governance (Public/PII/PHI/Financial different rules)
- [ ] Purpose limitation enforced (security only, no repurposing)
- [ ] Data minimization required (minimum necessary data)
- [ ] Retention policies defined (automated deletion)
- [ ] Third-party vendor governance (DPAs, assessments, certifications)
- [ ] Privacy-enhancing controls (pseudonymization, encryption, access limits, automated retention)

**Privacy Compliance Validation:**
- [ ] Quarterly internal privacy audits
- [ ] Annual privacy assessments
- [ ] Vendor privacy assessments
- [ ] Data subject rights tracking (≤30 day SLA)
- [ ] Privacy incident response integration (GDPR Article 33/34 notification ≤72 hours)
- [ ] Records of Processing Activities (ROPA) maintained

**Privacy Metrics (Level 2):**
- [ ] Data minimization compliance
- [ ] Retention policy enforcement (100% deleted on schedule)
- [ ] Rights request response (≤30 days, 100% fulfillment)
- [ ] Privacy incident rates (target: zero critical)
- [ ] AI decision explainability (100%)
- [ ] Vendor compliance (100% DPAs, ≥80% certifications)

**Level 3 Privacy-by-Default:**
- [ ] Real-time privacy dashboards (≥99% compliance)
- [ ] Automated privacy control testing
- [ ] Privacy-as-code (policies enforced technically)
- [ ] Automated rights request handling (≤7 days vs. ≤30 day requirement)
- [ ] Privacy drift detection (resolved ≤24 hours)
- [ ] Automated DPIA updates (continuous refresh)

**Privacy-Enhancing Technologies (Level 3):**
- [ ] Differential Privacy (aggregate analytics without individual re-identification)
- [ ] Federated Learning (distributed training without centralizing data)
- [ ] Homomorphic Encryption (analyze encrypted data)
- [ ] Secure Multi-Party Computation (collaborative intelligence without data sharing)
- [ ] Zero-Knowledge Proofs (prove compliance without data disclosure)
- [ ] ≥2 PETs implemented with documented benefits

**Industry Leadership (Level 3):**
- [ ] Regulatory engagement (ICO, CNIL, EDPB, FTC consultations, sandbox programs)
- [ ] Standards development (ISO 27701, IEEE, NIST Privacy Framework, OWASP)
- [ ] Annual transparency reports (published publicly)
- [ ] Open-source privacy tools (differential privacy libraries, federated learning, privacy-as-code)
- [ ] Third-party privacy certification (ISO 27701 or equivalent)
- [ ] Industry impact (adoption, standards incorporation, thought leadership)

---

**Document Version:** 2.0
**Last Updated:** 2025-12-29
**Next Review:** Quarterly or after significant HAI system changes
