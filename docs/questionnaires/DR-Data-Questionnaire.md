# Design Review (DR) - Data Domain Assessment Questionnaire
## HAIAMM v2.0

---

## Purpose

This questionnaire assesses organizational maturity in conducting design reviews for AI data security systems (classification, DLP, privacy automation). It evaluates review processes, coverage of critical design elements, review quality, and integration with threat modeling and compliance validation.

---

## Instructions

- Answer each question honestly based on current organizational practices
- Select "Yes" only if you have documented evidence of the practice
- Provide specific evidence in the "Evidence Repository" section
- Calculate your maturity level using the scoring guide at the end

---

## Level 1: Foundational (0-3 points)

### Question 1.1: Mandatory Design Review Process with Comprehensive Checklists

**Question:** Is there a mandatory design review process for all AI data security system designs (classification, DLP, privacy automation) with comprehensive review checklists covering classification models, DLP architecture, privacy-preserving AI, and compliance automation?

**Answer:** ☐ Yes ☐ No

**Evidence Required:**
- [ ] **Mandatory design review policy** established:
  - 100% of AI data security system designs must undergo design review before implementation
  - Design review required for: New AI data security systems, major changes to existing systems, new data sources integrated
  - Review completion tracked (dashboard showing pending/completed reviews)
  - No deployment to production without design review approval

- [ ] **Classification design review checklist**:
  - [ ] Multi-modal classification approach reviewed (text, images, structured data strategies)
  - [ ] Classification accuracy targets validated (≥92% structured data, ≥88% unstructured data per SR-Data)
  - [ ] Context-aware classification design reviewed (same data, different sensitivity in different contexts)
  - [ ] Real-time vs batch classification strategy assessed (performance vs accuracy trade-offs)
  - [ ] False negative risks evaluated (what happens if sensitive data is misclassified as non-sensitive?)
  - [ ] False positive mitigation reviewed (target ≤8% per SR-Data to avoid blocking business)
  - [ ] Edge cases identified (unusual data formats, obfuscated PII, emerging data types)

- [ ] **DLP architecture design review checklist**:
  - [ ] Multi-channel coverage validated (email, endpoint, network, cloud DLP)
  - [ ] Inline vs out-of-band design assessed (real-time blocking vs post-analysis trade-offs)
  - [ ] Policy engine design reviewed (centralized policy management, policy consistency across channels)
  - [ ] DLP detection requirements validated (≥93% email DLP, ≥95% endpoint DLP, ≥94% network DLP per SR-Data)
  - [ ] Evasion resistance evaluated (encrypted files, steganography, encoding, protocol abuse detection)
  - [ ] User experience impact assessed (latency ≤200ms email, ≤500ms file upload per SR-Data)
  - [ ] Override processes designed (self-service override, security review for critical data)

- [ ] **Privacy-preserving AI design review checklist**:
  - [ ] Data minimization strategy validated (metadata-only analysis where possible, sampling instead of full scans)
  - [ ] AI service account access controls reviewed (read-only, least privilege, scoped access, time-limited credentials ≤24h)
  - [ ] Training data anonymization validated (no actual PII in AI models, tokens/placeholders used)
  - [ ] Differential privacy integration assessed (privacy budget ε ≤ 10 per SR-Data)
  - [ ] Model privacy risks evaluated (model inversion, membership inference defenses - target ≤0.1% extraction success per SR-Data)
  - [ ] AI vendor data processing reviewed (DPA signed, no training on customer data without consent, data residency controls)

- [ ] **Compliance automation design review checklist**:
  - [ ] GDPR automation design validated:
    - Article 15 (Data Subject Access Request): ≥95% recall, ≤48h search, ≤72h report generation
    - Article 17 (Right to be Forgotten): ≥95% recall, ≥99% deletion verification, ≤30 days
    - Article 20 (Data Portability): Machine-readable export format
  - [ ] CCPA automation design validated:
    - Do Not Sell tracking design
    - Consumer rights automation (access, deletion, opt-out)
    - 45-day fulfillment timeline
  - [ ] Data retention enforcement design reviewed (auto-identify data exceeding retention, soft-delete with quarantine)
  - [ ] Multi-jurisdiction support assessed (GDPR, CCPA, HIPAA, PCI-DSS, conflict resolution when regulations conflict)

**Evidence Location:** ___________________________________________

**Notes:**
___________________________________________________________________
___________________________________________________________________

---

### Question 1.2: Multi-Dimensional Design Review Coverage

**Question:** Does design review cover multiple dimensions of AI data security systems including data lineage, cross-border flows, privacy-enhancing technologies, and integration with existing systems?

**Answer:** ☐ Yes ☐ No

**Evidence Required:**
- [ ] **Data lineage design review**:
  - [ ] Automated lineage discovery approach assessed (query log analysis, application monitoring, network traffic analysis)
  - [ ] Data flow mapping strategy reviewed (how PII flows through systems visualized)
  - [ ] Cross-border flow detection validated (≥90% detection of GDPR/PIPL-violating flows per SR-Data Level 2)
  - [ ] Lineage coverage targets reviewed (≥80% of sensitive data flows mapped per SR-Data Level 2)
  - [ ] Lineage use cases validated (compliance - Article 30 RoPA, DSAR fulfillment, risk analysis - insecure flows)

- [ ] **Privacy-enhancing technologies design review**:
  - [ ] Tokenization design assessed (token vault architecture, key management, de-tokenization access controls)
  - [ ] Format-preserving encryption (FPE) design reviewed (maintain data format while encrypted, key management)
  - [ ] Anonymization design validated (k-anonymity, l-diversity, differential privacy - target ≥99% re-identification protection per SR-Data)
  - [ ] Pseudonymization design reviewed (reversible pseudonyms, mapping key security - separate storage, access controls)
  - [ ] Use cases for each PET validated (tokenization for PCI-DSS scope reduction, anonymization for analytics/research, pseudonymization for longitudinal tracking)

- [ ] **Integration design review**:
  - [ ] Existing system integration assessed (databases, file shares, cloud storage, SaaS apps)
  - [ ] API integration design reviewed (authentication, authorization, rate limiting, error handling)
  - [ ] Performance impact evaluated (classification throughput ≥1 TB/hour, latency ≤500ms real-time per SA-Data)
  - [ ] Backward compatibility validated (existing applications continue to function with AI data security deployed)
  - [ ] Migration strategy reviewed (phased rollout, pilot testing, rollback plan)

- [ ] **Scalability and performance design review**:
  - [ ] Data volume scalability assessed (support ≥10 TB classification per SR-Data)
  - [ ] User scalability reviewed (DLP monitoring ≥5,000 concurrent users per SR-Data)
  - [ ] Distributed scanning architecture validated (parallel workers, incremental scanning)
  - [ ] Resource utilization targets reviewed (≤10% database CPU, ≤20% network bandwidth, ≤5% storage increase per SR-Data)

- [ ] **Security and resilience design review**:
  - [ ] Adversarial robustness assessed (prompt injection prevention, evasion detection, training data poisoning defenses)
  - [ ] High availability design validated (≥99.9% DLP uptime per SR-Data)
  - [ ] Disaster recovery design reviewed (backup/restore procedures, RTO/RPO targets)
  - [ ] Security controls validated (encryption at rest/in transit, access controls, audit logging)

**Evidence Location:** ___________________________________________

**Notes:**
___________________________________________________________________
___________________________________________________________________

---

### Question 1.3: Design Documentation Quality and Review Outcomes

**Question:** Are design review findings documented with clear remediation requirements, and is review effectiveness measured through design approval rates and defect detection?

**Answer:** ☐ Yes ☐ No

**Evidence Required:**
- [ ] **Design documentation requirements** defined:
  - **Architecture Diagrams**: Visual representation of AI data security system architecture
    - Classification pipeline (data sources → scanning → classification → policy enforcement)
    - DLP architecture (multi-channel coverage, policy engine, decision flow)
    - Data lineage (data flow maps showing source → processing → storage → consumption)
  - **Design Specifications**: Detailed written specifications covering:
    - Model architecture (classification algorithms, training approach, accuracy targets)
    - API specifications (endpoints, authentication, data formats)
    - Database schemas (data models, relationships, indexes)
    - Privacy controls (data minimization, anonymization, access controls)
  - **Compliance Mapping**: How design meets regulatory requirements (GDPR, CCPA, HIPAA, PCI-DSS)
  - **Performance Specifications**: Throughput, latency, resource utilization targets

- [ ] **Review findings documentation**:
  - All design review findings documented in structured format:
    - Finding ID, severity (critical, high, medium, low), description, affected component
    - Risk: What could go wrong if not addressed? (e.g., "False negative in classification could expose PII")
    - Recommendation: Specific remediation actions
    - Owner: Who is responsible for remediation
    - Deadline: When remediation must be completed
  - Critical findings: Must be remediated before deployment
  - High findings: Must be remediated within 30 days of deployment or have documented risk acceptance
  - Medium/Low findings: Tracked for future improvement

- [ ] **Review effectiveness metrics** tracked:
  - **Design Approval Rate**: % of designs approved on first review
    - Target: ≥90% approval rate (indicates high design quality, effective pre-review preparation)
    - Low approval rate (<70%) indicates design quality issues or unclear requirements
  - **Defect Detection Rate**: Design review findings per design
    - Track: Average number of critical/high/medium/low findings per review
    - Trend: Decreasing findings over time indicates improving design quality
  - **Defect Prevention Rate**: % of defects prevented by design review (vs found in implementation/production)
    - Target: ≥70% of defects caught in design review (cheaper to fix in design than code)
    - Measure: Compare design review findings to implementation review findings and production incidents

- [ ] **Review outcomes tracked**:
  - **Approved**: Design meets all requirements, cleared for implementation
  - **Approved with Conditions**: Design approved, but must address specific findings before deployment
  - **Rejected**: Design has critical flaws, must be redesigned
  - **Deferred**: Design review postponed (insufficient documentation, SME unavailability)
  - Dashboard showing review status for all AI data security projects

- [ ] **Post-implementation validation**:
  - After deployment, validate design review effectiveness:
    - Did the implemented system meet design specifications?
    - Were design review findings addressed?
    - Did any unforeseen issues arise that design review missed?
  - Lessons learned fed back into design review checklist improvements

**Evidence Location:** ___________________________________________

**Notes:**
___________________________________________________________________
___________________________________________________________________

---

## Level 2: Comprehensive (4-6 points)

### Question 2.1: Integrated Threat Modeling During Design Review

**Question:** Is threat modeling integrated into design review for AI data security systems, using structured methodologies (STRIDE, attack trees) to identify classification poisoning, DLP evasion, model inversion, and privacy violation threats?

**Answer:** ☐ Yes ☐ No

**Evidence Required:**
- [ ] **Threat modeling integrated in design review**:
  - Threat modeling conducted for 100% of AI data security system designs
  - Threat modeling occurs during design review (not after implementation)
  - Threat modeling results inform design decisions and remediation requirements

- [ ] **STRIDE threat modeling** applied to AI data security:
  - **Spoofing**: Threat of attacker impersonating authorized user to access AI classification system or manipulate policies
  - **Tampering**: Threat of attacker modifying training data (classification poisoning), DLP policies, or classification results
  - **Repudiation**: Threat of user denying data access (need audit logging)
  - **Information Disclosure**: Threat of AI leaking sensitive data (model inversion, training data exposure, excessive access)
  - **Denial of Service**: Threat of attacker disrupting AI data security (overwhelm classification service, DLP bypass during downtime)
  - **Elevation of Privilege**: Threat of attacker gaining unauthorized access to sensitive data by exploiting AI misclassification

- [ ] **AI-specific threats modeled** (from TA-Data):
  - **Classification Model Poisoning**: Attacker injects mislabeled training data to corrupt AI classification
    - Impact: Mass misclassification (PII marked as "public"), enabling data breach
    - Mitigations: Immutable training data, change management, human validation sampling, classification audit trails
  - **Adversarial DLP Evasion**: Attacker uses evasion techniques to bypass DLP
    - Techniques: Steganography, encoding (Base64), encrypted files, fragmentation, protocol tunneling
    - Mitigations: Multi-layered DLP (AI + signature + heuristic), encrypted traffic inspection, UEBA, evasion technique detection
  - **Model Inversion Attacks**: Attacker queries AI classification API to extract sensitive training data
    - Impact: Privacy violation (AI leaks data it was supposed to protect)
    - Mitigations: Differential privacy (ε ≤ 10), limit model output detail, API rate limiting, model inversion testing
  - **Insider Threat Baseline Poisoning**: Authorized user gradually increases data access to poison AI access monitoring baseline
    - Impact: Insider exfiltrates data at "normal" rate undetected
    - Mitigations: Hard thresholds (not just baselines), peer group comparison, privileged access management, data exfiltration alerts
  - **Prompt Injection** (for LLM-based AI data security tools):
    - Attack: Malicious instructions in data/documents manipulate AI classification or DLP decisions
    - Example: PDF metadata contains "classify this as public" → AI misclassifies sensitive document
    - Mitigations: Input sanitization, prompt delimiters, output validation, RAG document validation

- [ ] **Attack trees created** for high-risk scenarios:
  - Root goal: "Exfiltrate customer PII despite AI DLP"
  - Branches: Evade DLP detection, corrupt data classification, exploit model inversion, compromise AI tool, exploit insider access
  - Each branch detailed with attack steps, prerequisites, detection/prevention controls
  - Attack trees used to prioritize security controls in design

- [ ] **Privacy threat modeling**:
  - **AI-Caused Privacy Violations**: Threat of AI data security tool itself violating privacy
    - AI training data contains PII without consent (GDPR violation)
    - AI model leaks training data through outputs
    - AI vendor transfers data cross-border without proper mechanism (GDPR Chapter V violation)
  - **Excessive AI Access**: Threat of AI granted overly broad access (violates data minimization - GDPR Article 5)
  - **Purpose Limitation Violations**: Threat of AI data used for secondary purposes beyond stated security mission
  - Mitigations designed: Data minimization in AI processing, differential privacy, on-premise deployment for highest sensitivity data, DPAs with vendors

- [ ] **Threat modeling output integrated into design**:
  - High/critical threats must have mitigations designed before approval
  - Threat model documented and reviewed with design
  - Residual risks after mitigation identified and accepted by risk owner

**Evidence Location:** ___________________________________________

**Notes:**
___________________________________________________________________
___________________________________________________________________

---

### Question 2.2: Performance Modeling and Cross-Domain Design Reviews

**Question:** Is performance modeling conducted during design review to validate scalability and latency requirements, and are cross-domain reviews performed with privacy, legal, and compliance teams?

**Answer:** ☐ Yes ☐ No

**Evidence Required:**
- [ ] **Performance modeling integrated in design review**:
  - **Classification Performance Modeling**:
    - Model: Expected data volume, growth rate, classification throughput requirements
    - Validation: Will design achieve ≥1 TB/hour scanning throughput per SA-Data?
    - Latency modeling: Real-time classification ≤500ms for DLP per SA-Data
    - Resource modeling: Will design stay within ≤10% database CPU, ≤20% network bandwidth per SR-Data?
  - **DLP Performance Modeling**:
    - Latency modeling: Email DLP ≤200ms, file upload DLP ≤500ms per SR-Data
    - Throughput modeling: Support ≥5,000 concurrent users per SR-Data
    - Availability modeling: Achieve ≥99.9% uptime per SR-Data (≤8.7 hours downtime/year)
  - **DSAR Performance Modeling**:
    - Modeling: Can design locate individual's data across all systems within ≤48 hours per SR-Data?
    - Scalability: Performance with 10x data volume, 100x data volume
  - **Load Testing Plans**: Identify load testing approach to validate performance model after implementation

- [ ] **Scalability analysis**:
  - **Data Volume Scalability**: Design assessed for current data volume (e.g., 10 TB) and future growth (e.g., 100 TB in 3 years)
    - Distributed scanning architecture validated (parallel workers, incremental scanning)
    - Sampling strategy for massive datasets
  - **User Scalability**: Design assessed for current users (e.g., 5,000) and growth (e.g., 20,000)
  - **Geographic Scalability**: Design supports multi-region deployment (data residency requirements)
  - **Graceful Degradation**: Design degrades gracefully under load (prioritize high-risk data, queue lower-priority scans)

- [ ] **Cross-domain design reviews** conducted:
  - **Privacy Team Review**:
    - Data Protection Officer (DPO) or privacy team reviews design for GDPR/CCPA compliance
    - Privacy-by-design validated (data minimization, purpose limitation, privacy-by-default)
    - DPIA (Data Protection Impact Assessment) conducted for AI data processing per GDPR Article 35
    - Privacy team sign-off required before deployment
  - **Legal/Compliance Team Review**:
    - Legal counsel reviews design for regulatory compliance (GDPR, CCPA, HIPAA, PCI-DSS, industry-specific)
    - Legal basis for AI data processing validated (GDPR Article 6)
    - Cross-border data transfer mechanisms reviewed (Standard Contractual Clauses, adequacy decisions)
    - Contractual requirements for AI vendors validated (DPA per GDPR Article 28)
  - **Security Team Review**:
    - Security architecture team reviews design for security controls (encryption, access controls, audit logging)
    - Adversarial robustness assessed (prompt injection, evasion, poisoning defenses)
    - Integration with existing security tools (SIEM, SOAR, ticketing)
  - **Data Governance Review**:
    - Data stewards review design for alignment with data governance policies
    - Data classification taxonomy alignment
    - Data ownership and accountability clarity

- [ ] **Cross-functional review meetings**:
  - Design review includes representatives from: Engineering, Privacy, Legal, Security, Data Governance, Business stakeholders
  - Meeting frequency: For major AI data security projects, weekly design review meetings during design phase
  - All stakeholder sign-offs documented before deployment approval

**Evidence Location:** ___________________________________________

**Notes:**
___________________________________________________________________
___________________________________________________________________

---

### Question 2.3: Automated Design Validation and Pattern Libraries

**Question:** Are automated design validation tools used to check designs against security patterns and anti-patterns, with pattern libraries maintained for reusable AI data security architectural components?

**Answer:** ☐ Yes ☐ No

**Evidence Required:**
- [ ] **Automated design validation** implemented:
  - **Infrastructure-as-Code (IaC) Validation**: Automated checks of design specifications
    - Tools: Terraform validation, CloudFormation linter, Azure ARM template validator
    - Checks: Data encryption at rest enabled, network segmentation configured, access controls defined, audit logging enabled
    - Integration: IaC validation runs automatically on design commits (CI/CD pipeline)
  - **Security Policy-as-Code**: Automated validation of design against security policies
    - Tools: Open Policy Agent (OPA), Cloud Custodian, Checkov
    - Policies: "All databases storing PII must have encryption at rest enabled", "AI service accounts must have read-only access"
    - Pass criteria: 100% policy compliance before design approval
  - **Compliance-as-Code**: Automated validation of GDPR/CCPA/HIPAA requirements
    - Checks: DPA required for AI vendors processing EU data, DPIA completed for high-risk processing, data retention policies defined

- [ ] **Design anti-pattern detection**:
  - **AI Data Security Anti-Patterns** detected automatically:
    - **Anti-Pattern: AI Service Account with Write Access**: AI should have read-only access to data (data minimization principle)
    - **Anti-Pattern: Plaintext PII in Training Data**: Training data should use anonymized/tokenized values, not real PII
    - **Anti-Pattern: No Differential Privacy**: AI models trained on PII without differential privacy (privacy risk)
    - **Anti-Pattern: Centralized Data Aggregation**: Bringing all sensitive data to central location for AI analysis (increases breach risk)
    - **Anti-Pattern: No Human Oversight for High-Risk Decisions**: AI autonomously deletes data or declassifies sensitive data without human approval
    - **Anti-Pattern: Single Channel DLP**: DLP only on email, not endpoint/network/cloud (incomplete coverage)
    - **Anti-Pattern: No Evasion Detection**: DLP has no detection for encrypted files, steganography, encoding (easy to bypass)
  - Automated tools flag anti-patterns in design specifications, require remediation before approval

- [ ] **Secure design pattern library** maintained:
  - **AI Data Security Design Patterns** documented and reusable:
    - **Pattern: Metadata-Only Classification**: Classify data based on metadata (file name, schema, access patterns) without reading content (privacy-preserving)
    - **Pattern: Multi-Layered DLP**: Combine AI-based, signature-based, and heuristic DLP for defense in depth
    - **Pattern: Federated Classification**: Train models on distributed data without centralizing (privacy-preserving, regulatory compliant)
    - **Pattern: Tokenization for PCI Scope Reduction**: Replace cardholder data with tokens, reduce PCI-DSS compliance scope
    - **Pattern: Privacy-by-Default Access Controls**: New data repositories default to restrictive access, require justification to expand
    - **Pattern: Soft-Delete with Quarantine**: AI-initiated deletions go to quarantine for 30 days before hard delete (safety net for errors)
    - **Pattern: Just-in-Time Data Access**: Temporary access grants with automatic revocation (minimize standing privileged access)
  - Pattern library includes: Description, architecture diagram, when to use, benefits, trade-offs, implementation guidance, example code
  - Patterns referenced in design reviews: "Design uses 'Multi-Layered DLP' pattern from library"

- [ ] **Reference architectures** available:
  - **Reference Architecture: AI Data Classification Pipeline**: End-to-end architecture for data discovery → scanning → classification → policy enforcement
  - **Reference Architecture: Multi-Channel DLP**: Architecture covering email, endpoint, network, cloud DLP with centralized policy engine
  - **Reference Architecture: GDPR Compliance Automation**: DSAR fulfillment, right to be forgotten, Article 30 RoPA generation
  - Reference architectures include: Architecture diagrams, component descriptions, integration points, scalability considerations, security controls
  - Designers can start from reference architecture, customize for specific use case (faster, more consistent than designing from scratch)

**Evidence Location:** ___________________________________________

**Notes:**
___________________________________________________________________
___________________________________________________________________

---

## Level 3: Industry-Leading (7-9 points)

### Question 3.1: Advanced Automated Design Analysis and AI-Powered Design Review

**Question:** Are advanced automated design analysis tools used including AI-powered design review assistants, formal verification for critical components, and continuous design quality optimization?

**Answer:** ☐ Yes ☐ No

**Evidence Required:**
- [ ] **AI-powered design review assistant** deployed:
  - **AI Design Review Tool**: AI assistant analyzes design specifications and suggests improvements
    - Input: Architecture diagrams, design specifications, threat models
    - AI Analysis: Identify potential security issues, privacy risks, performance bottlenecks, compliance gaps
    - Output: Prioritized list of design review findings with severity, description, remediation recommendations
  - **AI Learning**: AI assistant learns from historical design reviews
    - Past design review findings → training data for AI
    - AI improves over time: Higher accuracy in identifying issues, fewer false positives
  - **Human-AI Collaboration**: AI assistant doesn't replace human reviewers, it augments them
    - AI provides preliminary analysis (finds common issues quickly)
    - Human reviewers focus on complex/nuanced issues requiring judgment
    - Result: ≥30% faster design reviews (per SR-Data Level 3 target)

- [ ] **Formal verification** for critical AI data security components:
  - **Formal Methods**: Mathematical proofs that design meets specifications
    - Use Cases: Prove DLP policy engine correctly enforces policies, prove data deletion algorithm deletes all instances, prove access control logic prevents unauthorized access
  - **Model Checking**: Exhaustively verify all possible states of system
    - Example: Verify classification state machine handles all edge cases correctly
  - **Theorem Proving**: Prove properties of algorithms
    - Example: Prove data anonymization algorithm achieves k-anonymity for all input datasets
  - **Coverage**: Formal verification applied to ≥5 critical security properties per SR-Data Level 3
    - Example properties: "AI service account never has write access to production data", "All PII deletion requests eventually complete within 30 days", "DLP blocks 100% of data transfers matching block policies (no bypass paths)"
  - **Tools**: Use formal verification tools (TLA+, Alloy, Coq, Isabelle, or similar)

- [ ] **Continuous design quality optimization**:
  - **Design Metrics Dashboard**: Real-time dashboard tracking design quality trends
    - Metrics: Design approval rate, defect density (findings per design), review cycle time, defect prevention rate
    - Trends: Improving over time (higher approval rate, lower defect density, faster reviews)
  - **Root Cause Analysis**: For design defects that escape to production
    - Why did design review miss this issue?
    - Checklist update: Add item to design review checklist to catch this class of issue in future
    - AI assistant retraining: Include issue in training data
  - **Continuous Improvement Process**:
    - Quarterly design review retrospectives: What's working? What needs improvement?
    - Checklist evolution: Add new items based on lessons learned, remove outdated items
    - Reviewer training: Share challenging design review scenarios for learning
  - **Benchmark Against Industry**: Compare design review effectiveness to industry benchmarks
    - NIST SSDF, OWASP SAMM, BSIMM design review practices
    - Identify gaps and improvement opportunities

- [ ] **Automated compliance validation**:
  - **Regulatory Requirement Mapping**: Automated mapping of design to regulatory requirements
    - Input: Design specifications
    - Output: Compliance matrix showing which design elements satisfy which GDPR articles, CCPA sections, HIPAA safeguards, PCI-DSS requirements
    - Gap analysis: Identify requirements not yet addressed in design
  - **Automated DPIA**: AI assists with Data Protection Impact Assessment (GDPR Article 35)
    - AI analyzes design and generates preliminary DPIA report
    - DPO reviews and finalizes (AI speeds up process, doesn't replace DPO judgment)

**Evidence Location:** ___________________________________________

**Notes:**
___________________________________________________________________
___________________________________________________________________

---

### Question 3.2: Design Review Metrics with Quantified ROI and Business Impact

**Question:** Are design review effectiveness metrics tracked with quantified ROI, including defect prevention cost savings, reduced time-to-market, and compliance audit performance improvements?

**Answer:** ☐ Yes ☐ No

**Evidence Required:**
- [ ] **Defect prevention cost savings** quantified:
  - **Cost to Fix in Design vs Implementation vs Production**:
    - Industry average: Design fix = 1x cost, Implementation fix = 10x cost, Production fix = 100x cost
    - Calculation: (Design review findings) × (10x - 1x cost) = Savings from preventing implementation fixes
    - Example: 50 design findings prevented × $1,000 each × 9x multiplier = $450,000 savings
  - **Annual Defect Prevention ROI**:
    - Total cost of design review program (reviewer time, tools, training)
    - Total savings from defects prevented (design review findings that would have been expensive implementation/production fixes)
    - ROI: (Savings - Cost) / Cost
    - Target: Design review ROI ≥3:1 per SR-Data Level 3 (similar to software domain)

- [ ] **Design review impact on time-to-market**:
  - **Reduced Rework**: Design review catches issues early, prevents costly implementation rework
    - Metric: % of projects with zero/minimal rework due to design issues
    - Target: ≥80% of projects have no design-caused rework (indicates effective design review)
  - **Faster Reviews Over Time**: Design review becomes faster as team improves
    - Metric: Design review cycle time (days from submission to approval)
    - Trend: Decreasing over time (year 1: 10 days, year 2: 7 days, year 3: 5 days)
    - Driver: Better design quality (fewer findings), AI-powered review assistance, pattern library reuse

- [ ] **Compliance audit performance improvements**:
  - **Regulatory Audit Findings Reduction**:
    - Metric: % reduction in privacy/security audit findings after implementing design review
    - Target: ≥60% reduction in audit findings (similar to SR-Data Level 3 target)
    - Rationale: Design review catches compliance issues before deployment, reducing audit findings
  - **Faster Evidence Production**:
    - Metric: Time to produce design documentation for audits
    - Target: ≤24 hours (per SR-Data Level 3 for regulatory audit evidence)
    - Benefit: Design review process creates audit-ready documentation automatically

- [ ] **Customer trust and business enablement**:
  - **Customer Privacy Satisfaction**: Survey customers on trust in data handling practices
    - Metric: % customers who trust organization with their data
    - Target: ≥90% customer trust (indicates privacy program effectiveness)
  - **Competitive Advantage**: Privacy compliance as competitive differentiator
    - Examples: Win deals due to superior data protection, enter new markets requiring strict privacy (EU, healthcare)
    - Quantified: Revenue enabled by privacy compliance (contracts won, markets entered)

- [ ] **Design review effectiveness scorecard**:
  - **Quarterly Scorecard** tracking:
    - Design approval rate (target ≥90%)
    - Defect detection rate (findings per design - trending down)
    - Defect prevention rate (% defects caught in design vs implementation/production - target ≥70%)
    - Review cycle time (trending down - target ≤5 days)
    - ROI (target ≥3:1)
    - Compliance audit findings (trending down - target ≥60% reduction)
  - Scorecard reviewed by leadership, drives continuous improvement

**Evidence Location:** ___________________________________________

**Notes:**
___________________________________________________________________
___________________________________________________________________

---

### Question 3.3: Industry Contribution and Design Excellence Recognition

**Question:** Do you contribute design review practices to industry standards and open-source communities, and has your organization received recognition for design excellence in AI data security?

**Answer:** ☐ Yes ☐ No

**Evidence Required:**
- [ ] **Industry standards contribution**:
  - **Standards Participation**: Active participation in design review standards
    - Examples: NIST SSDF (Secure Software Development Framework), OWASP SAMM (Software Assurance Maturity Model), ISO 27034 (Application Security)
    - Contribution: ≥2 standards working groups, regular meeting participation
  - **AI-Specific Standards**: Contribute to emerging AI security/privacy standards
    - Examples: ISO/IEC 23894 (AI Risk Management), NIST AI Risk Management Framework, IEEE AI Ethics standards
    - Focus: Design review practices specific to AI data security

- [ ] **Open-source design review tools/frameworks**:
  - **Published Tools**: Open-source design review tools, checklists, or frameworks
    - Examples: AI data security design review checklist (GitHub repo), automated design validation scripts, threat modeling templates
    - Impact: ≥100 GitHub stars or active community adoption
  - **Reference Architectures**: Publish reference architectures for AI data security
    - Examples: Multi-channel DLP reference architecture, GDPR compliance automation architecture, federated learning architecture
    - License: Creative Commons or similar open license

- [ ] **Best practices sharing**:
  - **Conference Presentations**: Present at privacy/security conferences on design review practices
    - Target: ≥2 external presentations per year
    - Topics: AI data security design patterns, privacy-by-design for AI, automated design validation
  - **Publications**: Whitepapers, blog posts, case studies on design review effectiveness
    - Topics: Design review ROI, defect prevention, compliance audit improvements
    - Audience: Privacy professionals, security architects, data engineers

- [ ] **Design excellence recognition**:
  - **Industry Awards**: Recognition for design excellence in AI data security
    - Examples: Privacy award (IAPP Privacy Innovation Award), security award (RSA Innovation Sandbox), AI ethics award
    - Recognition demonstrates thought leadership and best-in-class practices
  - **Customer Recognition**: Customers/partners recognize design excellence
    - Examples: Customer testimonials about superior data protection, partnership opportunities due to privacy program maturity
  - **Regulatory Recognition**: Positive feedback from regulators during audits
    - Example: Regulator commends privacy-by-design approach, cites organization as exemplar

- [ ] **Academic collaboration**:
  - **Research Partnerships**: Collaborate with universities on AI data security design research
    - Topics: Privacy-preserving ML, federated learning, differential privacy, formal verification of AI systems
    - Output: Joint publications, guest lectures, internship programs
  - **Curriculum Development**: Contribute to academic curriculum on secure AI design
    - Example: Guest lecture at university on "Designing AI Data Security Systems for Privacy Compliance"

- [ ] **Community leadership**:
  - **Speaking Engagements**: Regular speaking at industry events
    - Target: ≥4 speaking engagements per year (conferences, webinars, meetups)
  - **Advisory Roles**: Serve on privacy/security advisory boards
    - Examples: IAPP advisory board, startup advisory board for AI security vendors
  - **Mentorship**: Mentor other organizations on design review best practices
    - Example: Privacy community mentorship program, share lessons learned with peers

**Evidence Location:** ___________________________________________

**Notes:**
___________________________________________________________________
___________________________________________________________________

---

## Scoring Guide

### Simplified Scoring Method
- **Level 1 (Foundational)**: All 3 questions in Level 1 answered "Yes" = 3 points
- **Level 2 (Comprehensive)**: All 3 questions in Level 1 AND Level 2 answered "Yes" = 6 points
- **Level 3 (Industry-Leading)**: All 9 questions answered "Yes" = 9 points

### Precise Scoring Method
- Each question worth 1 point
- Partial credit: If ≥70% of evidence checkboxes completed = 0.7 points, ≥50% = 0.5 points
- **Total Score**: Sum of all question scores (0-9 points)
- **Maturity Level**:
  - 0-3 points: Level 1 (Foundational) or below
  - 4-6 points: Level 2 (Comprehensive)
  - 7-9 points: Level 3 (Industry-Leading)

**Your Score:** _______ / 9 points

**Your Maturity Level:** _______________________

---

## Evidence Repository

| Question | Evidence Description | Location/Link | Date |
|----------|---------------------|---------------|------|
| 1.1 | Design review policy and comprehensive checklists | | |
| 1.2 | Multi-dimensional review coverage (lineage, PETs, integration, security) | | |
| 1.3 | Design documentation quality standards and review outcomes tracking | | |
| 2.1 | Threat modeling integration (STRIDE, attack trees, AI-specific threats) | | |
| 2.2 | Performance modeling results and cross-domain review records | | |
| 2.3 | Automated design validation tools and pattern library | | |
| 3.1 | AI-powered design review assistant and formal verification results | | |
| 3.2 | Design review ROI quantification and effectiveness metrics | | |
| 3.3 | Industry contribution evidence and design excellence recognition | | |

---

## Data Domain-Specific Notes

### Critical Design Elements for AI Data Security

**Classification Design Considerations**:
- **Multi-Modal Requirements**: AI must classify text (documents, emails, chat), images (IDs, screenshots via OCR), structured data (databases)
- **Context-Aware Classification**: Same data has different sensitivity in different contexts (customer email in CRM vs medical records)
- **Accuracy Trade-offs**: Structured data (≥92% accuracy target) vs unstructured data (≥88% due to complexity)
- **Edge Cases**: Unusual formats, obfuscated PII, emerging data types require explicit design consideration

**DLP Architecture Considerations**:
- **Multi-Channel Consistency**: Policies must be consistent across email, endpoint, network, cloud channels
- **Inline vs Out-of-Band**: Real-time blocking (inline) vs post-analysis (out-of-band) - different latency/risk trade-offs
- **Evasion Resistance**: Design must address encrypted files, steganography, encoding, protocol abuse
- **User Experience**: Latency (≤200ms email, ≤500ms file upload) critical to avoid user workarounds

**Privacy-Preserving AI Design**:
- **Data Minimization**: AI should classify based on metadata/sampling where possible, not always read full content
- **Anonymization**: Training data must not contain actual PII (use tokens/placeholders)
- **Differential Privacy**: Add noise during training (ε ≤ 10) to prevent AI memorizing individual records
- **Model Privacy**: Defend against model inversion (≤0.1% extraction success target)

### Threat Modeling for AI Data Security

**AI-Specific Threat Categories** (from TA-Data):
1. **Adversarial Manipulation**: Classification poisoning, DLP evasion, model inversion, prompt injection
2. **Operational Failures**: False negatives (missed sensitive data), false positives (business disruption), model drift
3. **Privacy Violations by AI**: AI training data privacy, model data leakage, excessive access, cross-border transfers
4. **Supply Chain Risks**: Compromised AI vendors, malicious model updates, stolen classification models

**STRIDE Application to AI Data Security**:
- **Spoofing**: Attacker impersonates authorized user to access AI
- **Tampering**: Training data poisoning, DLP policy manipulation
- **Repudiation**: Need audit logging of all AI decisions
- **Information Disclosure**: Model inversion, training data exposure, excessive AI access
- **Denial of Service**: Overwhelm AI classification service
- **Elevation of Privilege**: Exploit misclassification to access sensitive data

### Compliance Design Requirements

**GDPR Design Considerations**:
- **Article 15 (Access)**: Design must support finding all of individual's data across all systems (≥95% recall, ≤48h)
- **Article 17 (Deletion)**: Design must support deleting all instances (≥95% recall, ≥99% verification, ≤30 days)
- **Article 25 (Privacy by Design)**: Default to most restrictive classification when uncertain, data minimization in AI processing
- **Article 35 (DPIA)**: Design review should trigger/include DPIA for high-risk AI processing

**CCPA Design Considerations**:
- **Data Inventory**: Design must maintain real-time inventory as AI discovers/classifies data
- **Do Not Sell**: Design must track and enforce do-not-sell flags
- **Consumer Rights**: Access, deletion, opt-out automation (45-day fulfillment)

**Cross-Regulatory Conflicts**:
- Design must handle conflicts (e.g., GDPR deletion vs US legal hold)
- Escalation to legal team when conflicts detected (don't auto-delete)

### Performance Modeling Requirements

**Classification Performance**:
- Throughput: ≥1 TB/hour for batch scanning (SA-Data requirement)
- Latency: ≤500ms for real-time classification (DLP inline blocking)
- Resource: ≤10% database CPU, ≤20% network bandwidth

**DLP Performance**:
- Latency: ≤200ms email, ≤500ms file upload (≤10MB), ≤2s large files (10-100MB)
- Availability: ≥99.9% uptime (≤8.7 hours downtime/year)
- Scalability: Support ≥5,000 concurrent users

**DSAR Performance**:
- Search: ≤48 hours to locate data
- Report: ≤72 hours to generate (within 30-day GDPR/45-day CCPA requirement)

### Integration with Other Practices

- **Threat Assessment (TA-Data)**: TA identifies threats → DR validates design addresses threats
- **Security Requirements (SR-Data)**: SR defines requirements (accuracy, privacy, compliance) → DR validates design meets requirements
- **Secure Architecture (SA-Data)**: SA defines reference architectures → DR validates design follows architectural patterns
- **Implementation Review (IR-Data)**: DR sets design baseline → IR validates code implements design correctly

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

**Document Version:** HAIAMM v2.0
**Practice:** Design Review (DR)
**Domain:** Data
**Questionnaire Version:** 1.0
**Last Updated:** December 2025
