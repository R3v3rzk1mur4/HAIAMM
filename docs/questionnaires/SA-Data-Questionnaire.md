# Secure Architecture (SA) - Data Domain Assessment Questionnaire
## HAIAMM v2.0

---

## Purpose

This questionnaire assesses organizational maturity in establishing architectural design for AI-powered data security systems (data classification, DLP, privacy automation). It evaluates AI model architecture, data discovery architecture, multi-channel DLP, privacy-preserving processing, data access policy enforcement, and compliance automation.

---

## Instructions

- Answer each question honestly based on current organizational practices
- Select "Yes" only if you have documented evidence of the practice
- Provide specific evidence in the "Evidence Repository" section
- Calculate your maturity level using the scoring guide at the end

---

## Level 1: Foundational (0-3 points)

### Question 1.1: AI Model Architecture and Data Discovery

**Question:** Have you designed AI model architecture for data classification and DLP detection, with scalable data discovery and scanning architecture deployed?

**Answer:** ☐ Yes ☐ No

**Evidence Required:**
- [ ] **Classification model architecture** implemented:
  - **Pattern Matching**: Regex patterns for structured data (SSN, credit cards, phone numbers, emails, national IDs)
    - Fast, accurate for well-formatted data
  - **Machine Learning Classifiers**: Named Entity Recognition (NER) for PII detection in text, document classification (confidential vs public), context-aware classification
  - **Deep Learning Models**: Transformers (BERT, similar) for semantic understanding
    - Example: Distinguish "John Smith" (name) vs "John Smith Corporation" (company name - not PII)
  - **Multi-Modal Classification**:
    - Text: NLP models for documents, emails, chat
    - Images: OCR + image classification for sensitive images (IDs, screenshots)
    - Structured Data: Schema analysis + content sampling for databases

- [ ] **DLP detection model architecture** implemented:
  - **Content-Based Detection**: Detect sensitive data in content (email body, file contents)
  - **Context-Based Detection**: Detect policy violations based on context (recipient, destination, time)
  - **Behavior-Based Detection**: Detect unusual data access patterns (user downloads 10x normal data volume)

- [ ] **Data discovery architecture** deployed:
  - **Active Scanning**: Periodic scans of data repositories (daily/weekly/monthly based on risk)
    - Databases: Query for PII patterns
    - File Shares: Scan files for sensitive content
    - Cloud Storage: S3/Blob/GCS scanning
    - SaaS Apps: API-based scanning (Salesforce, Google Workspace, M365, Box, Dropbox, Slack)
  - **Passive Discovery**: Discover data during normal operations
    - DLP scanning of data in motion (emails, file uploads)
    - User access logging (what data accessed?)

- [ ] **Scalability architecture** implemented:
  - **Distributed Scanning**: Parallel scanning across multiple workers
  - **Incremental Scanning**: Only scan changed data (not full rescans)
  - **Sampling**: For massive datasets, statistical sampling (scan representative sample, extrapolate)
  - **Discovery Performance**:
    - Throughput: Scan ≥1 TB of data per hour (baseline)
    - Latency: Real-time classification ≤500ms (for DLP inline blocking)

- [ ] **Scan coverage achieved**:
  - ≥95% of data repositories scanned within 30 days of deployment
  - ≥80% of organizational data classified (SR-Data requirement)

**Evidence Location:** ___________________________________________

**Notes:**
___________________________________________________________________
___________________________________________________________________

---

### Question 1.2: Multi-Channel DLP Architecture and Privacy-Preserving AI

**Question:** Have you implemented multi-channel DLP architecture (email, endpoint, network, cloud) with centralized policy enforcement, and privacy-preserving AI processing architecture?

**Answer:** ☐ Yes ☐ No

**Evidence Required:**
- [ ] **Multi-channel DLP architecture** deployed:
  - **Email DLP**: Scan outbound emails + attachments
    - Integration: SMTP proxy, email gateway API (Proofpoint, Mimecast, native email security)
    - Actions: Block, encrypt, quarantine, alert
  - **Endpoint DLP**: Monitor data on endpoints
    - Agents on endpoints monitor file operations, clipboard, USB, screen capture, print
    - Integration: Endpoint agent architecture (similar to EDR deployment)
  - **Network DLP**: Scan network traffic
    - Deep packet inspection (DPI) for HTTP/S, FTP, cloud protocols
    - Integration: Network TAPs, SPAN ports, cloud proxies (Zscaler, Netskope)
  - **Cloud DLP**: Scan cloud storage and SaaS
    - API integration with cloud providers (AWS S3, Azure Blob, GCP Storage, Box, Dropbox, OneDrive)
    - CASB integration for SaaS app DLP

- [ ] **DLP decision architecture** implemented:
  - **Centralized Policy Engine**: Single policy engine defining what data can go where
  - **Context Evaluation**: AI evaluates context (who, what, where, when, why)
  - **Risk Scoring**: Combine data sensitivity + destination risk + user risk = Overall risk score
  - **Action Selection**: Based on risk score: Allow, Alert, Block, Encrypt
  - Architecture supports policy consistency across all DLP channels (email, endpoint, network, cloud enforce same policies)

- [ ] **Privacy-preserving AI architecture** implemented:
  - **Data Minimization in AI Processing**:
    - **Metadata-Only Analysis**: AI classifies based on metadata (file name, schema, access patterns) without reading content where possible
      - Example: File named "SSN_List.xlsx" in "/HR/Payroll" accessed only by HR → High confidence it's PII without opening file
    - **Sampling**: Analyze sample of data (10 rows of database, 10 files in folder), not entire dataset
    - **Anonymization**: When AI must analyze content, anonymize before AI processing
      - Replace actual PII with tokens: "John Smith" → "[NAME]", "123-45-6789" → "[SSN]"
  - **Differential Privacy in AI Training**:
    - Add noise to AI training data to prevent AI from memorizing individual records
    - Privacy budget (ε) defined: ε ≤ 10 for training (SR-Data requirement)
  - **Access Controls for AI**:
    - AI service account: Read-only access to data
    - Least privilege: Access scoped to repositories being scanned
    - Time-limited: Credentials expire after scan completion (≤24 hours per SR-Data)
    - Audit: All AI data access logged with timestamp, data accessed, purpose

- [ ] **Privacy protection validated**:
  - Zero GDPR/CCPA violations from AI data processing (SR-Data requirement)
  - AI model privacy tested: ≤0.1% success rate in extracting sensitive values from model (SR-Data requirement)

**Evidence Location:** ___________________________________________

**Notes:**
___________________________________________________________________
___________________________________________________________________

---

### Question 1.3: Data Access Policy Enforcement and Compliance Automation Architecture

**Question:** Have you established data access policy enforcement architecture (ABAC, just-in-time access) and compliance automation architecture for GDPR/CCPA (DSAR, deletion, retention)?

**Answer:** ☐ Yes ☐ No

**Evidence Required:**
- [ ] **Dynamic access control architecture** implemented:
  - **Attribute-Based Access Control (ABAC)**: Access decisions based on attributes
    - Attributes: User role, data sensitivity, purpose, location, time
    - Example: "Allow HR manager to access PII in HR database during business hours from corporate network for legitimate HR purposes"
  - **AI-Driven Policy Enforcement**: AI enforces policies automatically
    - Monitor data access in real-time
    - Block unauthorized access
    - Alert on policy violations
  - **Just-in-Time Access**:
    - Temporary access grants (e.g., 2-hour access to sensitive database for specific task)
    - Automatic revocation after time limit
    - Audit trail of temporary access grants

- [ ] **GDPR automation architecture** implemented:
  - **Article 15 (Data Subject Access Request)**: AI finds all data for individual across all systems
    - Search: Full-text search + PII matching across databases, file shares, SaaS apps
    - Report Generation: Automated report in machine-readable format (JSON, XML, CSV)
    - Performance: Locate data within ≤48h, generate report within ≤72h (SR-Data requirement, within GDPR 30-day window)
    - Accuracy: ≥95% recall (find 95% of individual's data per SR-Data)
  - **Article 17 (Right to be Forgotten)**: AI deletes individual's data
    - Discovery: Find all instances of individual's data across all systems
    - Deletion: Automated deletion workflow + verification
    - Timeline: ≤30 days (GDPR requirement)
    - Verification: ≥99% confidence deletion completed (SR-Data requirement)
    - Safety: Soft-delete to quarantine for ≥30 days before hard delete (SR-Data safety guardrail)

- [ ] **CCPA automation architecture** implemented:
  - **Data Inventory**: AI maintains inventory of personal information (categories, sources, purposes, third parties, retention periods)
  - **Do Not Sell Tracking**: AI tracks which data can be sold vs not, prevents sale of flagged data
  - **Consumer Rights Automation**:
    - Right to Know: Generate report within 45 days (≥95% recall per SR-Data)
    - Right to Delete: Identify and delete within 45 days (≥95% recall, ≥99% verification per SR-Data)
    - Right to Opt-Out: Flag consumer data as "do not sell", prevent future sales

- [ ] **Data retention architecture** implemented:
  - **Automated Retention Policy Enforcement**:
    - AI identifies data exceeding retention limits based on policies (GDPR, CCPA, HIPAA, PCI-DSS, internal policies)
    - Auto-flag for review or auto-delete (with approval workflow per SR-Data)
  - **Retention Enforcement Metrics**: ≥90% of data within retention limits

**Evidence Location:** ___________________________________________

**Notes:**
___________________________________________________________________
___________________________________________________________________

---

## Level 2: Comprehensive (4-6 points)

### Question 2.1: Data Lineage Architecture and Cross-System Correlation

**Question:** Have you implemented data lineage and flow tracking architecture with automated lineage discovery, and cross-system data correlation architecture for aggregation detection?

**Answer:** ☐ Yes ☐ No

**Evidence Required:**
- [ ] **Automated data lineage discovery** implemented:
  - **Data Flow Tracking**: Track data flow from source → processing → storage → consumption
  - **Discovery Methods**:
    - Query log analysis (database queries showing data movement)
    - Application monitoring (API calls, data transformations)
    - Network traffic analysis (data transfers between systems)
  - **Coverage**: Map ≥80% of sensitive data flows within organization (SR-Data Level 2 requirement)
  - **Lineage Visualization**: Generate data flow diagrams showing how PII/PHI flows through systems
    - Visual representation of data sources, processing systems, destination systems
    - Interactive lineage exploration (click on dataset to see upstream/downstream flows)

- [ ] **Data flow mapping for risk analysis** implemented:
  - **Cross-Border Flow Detection**: Identify data flows crossing regulatory boundaries
    - Detect: EU citizen PII transferred to US servers (GDPR Article 44-50 restrictions)
    - Detect: Chinese citizen data transferred outside China (China PIPL requirements)
    - Accuracy: ≥90% detection of cross-border flows (SR-Data requirement)
    - Action: Verify appropriate transfer mechanism (SCCs, BCRs, adequacy decision) or block transfer
  - **Risky Flow Identification**: Identify data flows to unsecured systems, unauthorized destinations, excessive data sharing
    - Example: PHI transferred via unencrypted email (HIPAA violation)
    - Example: PII to cloud storage without encryption at rest
    - Detection accuracy: ≥90% for common insecure patterns (SR-Data requirement)

- [ ] **Data lineage for compliance** implemented:
  - **GDPR Article 30 Records of Processing**: Auto-generate GDPR documentation
    - Track: Categories of data, purposes of processing, recipients, retention periods, transfers to third countries
    - Update: Automatically as new data sources/flows detected
    - Accuracy: ≥95% completeness (cover 95% of actual processing activities per SR-Data)
    - Export: Generate Article 30-compliant Records of Processing Activities (RoPA) report on demand
  - **Data Subject Request Fulfillment**: Use lineage to find all instances of individual's data
    - Query: "Find all data for individual X across all systems"
    - Use lineage map to identify all systems that may contain their data
    - Accuracy: ≥97% recall (SR-Data Level 2 requirement)
    - Time: ≤48 hours for standard request

- [ ] **Cross-system data correlation architecture** implemented:
  - **Data Aggregation Detection**: Detect when non-sensitive data pieces combine to create sensitive aggregation
    - Example: Public data (name from LinkedIn) + internal data (badge number) + public data (home address from property records) = Full PII profile
    - Detection accuracy: ≥85% for common aggregation patterns (SR-Data Level 2 requirement)
    - Action: Reclassify aggregated dataset as sensitive, restrict access
  - **Derived Data Classification**: Classify data derived from sensitive sources
    - Anonymized reports derived from PII inherit some sensitivity from source data
    - ML models trained on sensitive data classified based on potential for data leakage
    - Accuracy: ≥90% correct classification of derived data products (SR-Data requirement)

- [ ] **Third-party data sharing monitoring** implemented:
  - **Vendor Data Sharing Tracking**: Maintain inventory (vendor name, data types shared, business purpose, data processing agreement status)
    - Detect: New data flows to vendors not in approved vendor list → Alert for vendor risk assessment
    - Requirement: ≥95% of vendor data sharing has documented business purpose and data processing agreement (SR-Data)
  - **Data Sharing Agreement Compliance**: Monitor that sharing stays within agreement bounds
    - Example: Agreement allows sharing customer names/emails but not SSNs
    - AI detects: SSN being sent to vendor → Block + alert (agreement violation)
    - Accuracy: ≥88% detection of out-of-scope data sharing (SR-Data)

**Evidence Location:** ___________________________________________

**Notes:**
___________________________________________________________________
___________________________________________________________________

---

### Question 2.2: Privacy-Enhancing Technologies Architecture

**Question:** Have you designed and deployed privacy-enhancing technologies (tokenization, format-preserving encryption, anonymization) with secure architecture for token vaults and key management?

**Answer:** ☐ Yes ☐ No

**Evidence Required:**
- [ ] **Tokenization architecture** implemented:
  - **Token Generation**: Replace sensitive data with tokens (reversible mapping)
    - Example: Credit card "4111-1111-1111-1111" → Token "TKN-8472-9384-7261"
  - **Token Vault**: Secure storage for token mappings
    - Encrypted storage (AES-256 or equivalent)
    - Access controls: Only authorized systems can de-tokenize
    - High availability: ≥99.9% uptime for token vault (business depends on de-tokenization)
    - Audit: All de-tokenization requests logged
  - **Use Cases**: Payment processing (PCI-DSS scope reduction), analytics (analyze tokenized data without exposing PII), testing (developers use tokens, not real data)

- [ ] **Format-Preserving Encryption (FPE)** implemented:
  - **FPE Architecture**: Encrypt while maintaining format
    - Example: Encrypted SSN still looks like SSN format (###-##-####), fits in same database fields
  - **Benefits**: Encrypted data can be used in legacy systems without schema changes, maintains data format for applications
  - **Key Management**: Secure key storage (Hardware Security Module or cloud KMS)
  - **Use Cases**: Encrypt sensitive fields in databases, file shares while maintaining application compatibility

- [ ] **Anonymization architecture** implemented:
  - **Anonymization Techniques**:
    - **K-anonymity**: Generalize data so each record is indistinguishable from at least k-1 others
      - Example: Age 27 → Age range 25-30
    - **L-diversity**: Within each k-anonymous group, ensure diversity of sensitive attributes
    - **T-closeness**: Distribution of sensitive attribute in group close to distribution in overall dataset
    - **Differential Privacy**: Add statistical noise to protect individuals while preserving aggregate statistics
  - **Anonymization Quality**: Anonymization meets GDPR standard (≥99% confidence data cannot be re-identified per SR-Data Level 2)
  - **Use Cases**: Analytics, research, data sharing with partners, test data generation
  - **Coverage**: ≥80% of non-production uses of PII replaced with anonymized alternatives within 12 months (SR-Data Level 2)

- [ ] **Pseudonymization architecture** implemented:
  - **Pseudonymization**: Replace identifiers with pseudonyms where reversibility needed
    - Use cases: Research, analytics requiring longitudinal tracking without full identification
  - **Security**: Pseudonym mapping key stored separately with strict access controls
  - **Re-identification Protection**: ≥99% probability that pseudonym cannot be linked back without key (SR-Data)

- [ ] **Key management architecture** implemented:
  - **Centralized Key Management**: Keys for encryption, tokenization, pseudonymization managed centrally
  - **Key Storage**: Hardware Security Module (HSM) or cloud KMS (AWS KMS, Azure Key Vault, GCP KMS)
  - **Key Rotation**: Automated key rotation (e.g., monthly/quarterly)
  - **Access Controls**: Separation of duties (different roles for key generation, usage, management)
  - **Audit**: All key access logged

**Evidence Location:** ___________________________________________

**Notes:**
___________________________________________________________________
___________________________________________________________________

---

### Question 2.3: Proactive Data Risk Reduction Architecture

**Question:** Have you implemented proactive data risk reduction architecture (data minimization automation, purpose limitation enforcement, privacy by design) that identifies and reduces unnecessary sensitive data?

**Answer:** ☐ Yes ☐ No

**Evidence Required:**
- [ ] **Data minimization automation architecture** implemented:
  - **Unnecessary PII Detection**: AI identifies PII collected or retained without clear business purpose
    - Scan: Databases, file shares, SaaS applications for PII
    - Analyze: Last accessed date, business purpose (from metadata/usage patterns), retention policy
    - Flag: PII not accessed in ≥365 days with no documented retention requirement = "Candidate for deletion"
    - Accuracy: ≥90% correct identification of unnecessary PII (SR-Data Level 2)
    - Action: Generate deletion recommendations for data stewards, track progress on deletion
  - **Auto-Deletion Workflow**: Automated deletion of clearly unnecessary data
    - Criteria: Data >7 years old, no regulatory retention requirement, no business access in >2 years
    - Safety: Soft-delete to quarantine, DPO review weekly, hard-delete after 30 days
    - Impact: ≥10% of total PII deleted quarterly based on AI recommendations (SR-Data Level 2 process metric)

- [ ] **Purpose limitation enforcement architecture** implemented:
  - **Purpose Tracking**: AI ensures data is used only for stated purpose
    - Track: Data collection purpose (from privacy notices, consent forms, business documentation)
    - Monitor: Actual data usage (which teams access data, for which applications)
    - Detect: Usage beyond stated purpose (≥85% accuracy per SR-Data Level 2)
    - Example: Customer emails collected for "order fulfillment" being used for marketing without consent → Alert to privacy team
  - **Purpose-Based Access Control**: Access policies enforce purpose limitation
    - Data tagged with collection purpose, access granted only for compatible purposes
  - **Action**: Block out-of-purpose usage, require consent update or deletion

- [ ] **Privacy by design enforcement architecture** implemented:
  - **New Data Source Scanning**: AI automatically scans and classifies new data sources
    - Trigger: New database created, new SaaS app connected, new file share mounted
    - Action: Within 24 hours, AI classifies data, assesses privacy risk, notifies data steward (SR-Data Level 2)
    - Privacy review: If sensitive data detected, require privacy impact assessment before production use
  - **Default to Private**: AI enforces "privacy by default" in configurations
    - Detect: New data repositories with default public/broad access permissions
    - Action: Auto-restrict to private/minimal access + alert data owner
    - Override: Owner can expand access after documenting business justification
    - Result: ≥95% of new data repositories start with restrictive access (SR-Data Level 2)

- [ ] **Sensitive data exposure reduction architecture** implemented:
  - **Least Privilege for Data Access**: AI identifies and reduces overly broad data access
    - Analyze: Who has access to sensitive data repositories (groups, roles, individuals)
    - Identify: Users with access who never use it (≥90 days no access) or out-of-role access
    - Recommend: Access removals to data owners
    - Result: Reduce users with access to each sensitive dataset by ≥30% (SR-Data Level 2)
  - **Data Location Consolidation**: AI identifies sensitive data sprawl
    - Detect: Same sensitive dataset duplicated in ≥5 locations (CRM, multiple databases, file shares, SaaS apps)
    - Analyze: Which copies are necessary (production), which are redundant (backups, stale copies)
    - Recommend: Delete redundant copies, consolidate to authoritative source
    - Result: Reduce number of locations storing each sensitive dataset by ≥40% (SR-Data Level 2)

**Evidence Location:** ___________________________________________

**Notes:**
___________________________________________________________________
___________________________________________________________________

---

## Level 3: Industry-Leading (7-9 points)

### Question 3.1: Federated Data Security Architecture

**Question:** Have you implemented federated data security architecture that enables analysis of distributed data without centralizing sensitive information (federated learning, secure multi-party computation)?

**Answer:** ☐ Yes ☐ No

**Evidence Required:**
- [ ] **Federated learning architecture** implemented:
  - **Distributed Model Training**: Train AI classification models across distributed data sources without moving data
    - Architecture: Model trained locally at each data source, only model updates (gradients) transmitted to central server
    - Benefits: Privacy-preserving (raw data never leaves source), regulatory compliance (data stays in jurisdiction), reduced data movement
    - Use Cases: Train data classification models across subsidiaries in different countries (GDPR, PIPL compliance), train models across customer sites without accessing customer data
  - **Federated Aggregation**: Central server aggregates model updates from distributed sources
    - Secure aggregation: Individual model updates encrypted, only aggregate visible to server
    - Differential privacy: Add noise to model updates before transmission (protect individual data points)
  - **Deployment**: Federated models deployed for production classification

- [ ] **Secure Multi-Party Computation (SMPC) architecture** implemented:
  - **Collaborative Analysis**: Enable collaborative data analysis with partners without sharing raw data
    - Example: Two companies jointly analyze customer overlap without revealing their customer lists to each other
  - **SMPC Protocols**: Cryptographic protocols enable computation on encrypted data
    - Each party's data remains encrypted, computation produces result without any party seeing others' data
  - **Use Cases**: Cross-organization analytics, regulatory reporting without centralizing sensitive data, privacy-preserving data sharing
  - **Performance**: SMPC has computational overhead (10-100x slower than plaintext computation), architect for acceptable latency

- [ ] **Differential privacy for external data sharing** implemented:
  - **Privacy Budget for Sharing**: Add noise to shared datasets to protect individual privacy while preserving statistical utility
    - Privacy budget (ε) for external sharing: ε ≤ 5 (stricter than ε ≤ 10 for internal training per SR-Data Level 3)
  - **Use Cases**: Share aggregate statistics with partners/public, publish research datasets, contribute to industry benchmarks
  - **Quality Validation**: Verify anonymized data maintains utility for intended analytics (test statistical properties preserved)

- [ ] **Privacy-preserving collaboration enabled**:
  - Documented examples of collaborative data analysis with partners/customers without sharing raw sensitive data
  - Business value quantified (e.g., enabled partnership worth $X, unlocked analytics use case generating $Y value)

**Evidence Location:** ___________________________________________

**Notes:**
___________________________________________________________________
___________________________________________________________________

---

### Question 3.2: Zero-Knowledge and Blockchain-Based Data Governance Architecture

**Question:** Have you designed zero-knowledge architecture for data security policy verification, and blockchain-based data lineage for immutable audit trails?

**Answer:** ☐ Yes ☐ No

**Evidence Required:**
- [ ] **Zero-knowledge proof architecture** implemented:
  - **Zero-Knowledge Proofs (ZKP)**: Prove data meets security policy without revealing data itself
    - Example: Prove "this dataset contains no PII" without showing the dataset contents
    - Example: Prove "user X has access permission to data Y" without revealing access control list
  - **Use Cases**: Privacy-preserving access control (prove authorization without revealing policies), compliance verification (prove GDPR compliance without exposing data), audit (prove data handling correctness without revealing data)
  - **ZKP Implementation**: Use ZKP libraries (e.g., ZoKrates, libsnark, Bulletproofs)
  - **Deployment**: ZKP used for at least one production use case (access control, compliance verification, or audit)

- [ ] **Blockchain-based data lineage** implemented:
  - **Immutable Audit Trail**: Record data access, data movement, data transformations on blockchain
    - Benefits: Tamper-proof audit trail (cannot retroactively alter access logs), transparency (auditors can verify data handling), regulatory compliance (prove data governance)
  - **Blockchain Architecture**: Private/permissioned blockchain (not public blockchain - performance and privacy)
    - Technologies: Hyperledger Fabric, Ethereum private network, or similar
  - **Data Lineage on Blockchain**: Record lineage events (data created, accessed, transformed, deleted, shared)
    - Hash of data + metadata recorded on blockchain (not full data - privacy)
    - Data location, timestamp, user, operation, purpose logged immutably
  - **Use Cases**: Regulatory audit (prove data handling for GDPR/CCPA), incident investigation (tamper-proof forensics), cross-organization data sharing (shared audit trail)

- [ ] **Homomorphic encryption architecture** explored/implemented:
  - **Homomorphic Encryption (HE)**: Perform computations on encrypted data without decryption
    - Example: Search encrypted database without decrypting, perform analytics on encrypted datasets
  - **Current Limitation**: HE has significant computational overhead (1000x+ slower than plaintext), limited to specific operations
  - **Implementation Status**: Pilot/proof-of-concept for specific use case, or monitoring HE research for production readiness
  - **Use Cases**: Cloud analytics on sensitive data (encrypt before cloud, compute in cloud without decryption), regulatory compliance (data never decrypted outside secure environment)

**Evidence Location:** ___________________________________________

**Notes:**
___________________________________________________________________
___________________________________________________________________

---

### Question 3.3: Autonomous Data Governance and Industry Contribution

**Question:** Have you achieved autonomous data governance with self-optimizing classification and policy enforcement, while contributing to privacy-preserving ML research and industry standards?

**Answer:** ☐ Yes ☐ No

**Evidence Required:**
- [ ] **Autonomous data governance** achieved:
  - **Self-Optimizing Classification**: AI automatically improves classification accuracy over time
    - Continuous learning: AI learns from human corrections, new data types, evolving business context
    - Automated model retraining: When drift detected (>10% distribution shift or >5% accuracy degradation), trigger retraining within 14 days
    - A/B testing: New models tested against production model, automatically promoted if superior
    - Result: Classification accuracy improves year-over-year without manual tuning
  - **Autonomous Policy Enforcement**: Policies automatically adapt to business changes
    - Example: New business unit created → AI automatically extends data access policies to new unit
    - Example: Employee role change → AI automatically adjusts data access within 24 hours
  - **Autonomous Compliance**: AI automatically detects regulatory changes and updates compliance controls
    - Monitor: Regulatory updates (GDPR guidance, new state privacy laws, enforcement actions)
    - Assess: Impact on current data operations
    - Adapt: Update policies within 30 days of new regulation effective date (SR-Data Level 3)
  - **Human Oversight**: Autonomous operations monitored by data stewards, DPO, security team (not fully unsupervised)

- [ ] **Self-healing architecture** implemented:
  - **Automated Error Detection**: AI detects when it makes classification errors
    - Methods: User feedback, sampling audit, anomaly detection
  - **Automated Remediation**: AI attempts to fix errors automatically
    - Reclassify misclassified data, update policies to prevent recurrence
    - If auto-remediation not possible, escalate to human with context
  - **Continuous Validation**: Daily/weekly automated testing validates AI continues to meet accuracy requirements (≥97% per SR-Data Level 3)

- [ ] **Privacy-preserving ML research contribution** demonstrated:
  - **Research Publications**: Published research on privacy-preserving ML techniques
    - Topics: Federated learning, differential privacy, secure multi-party computation, homomorphic encryption, zero-knowledge proofs
    - Venues: Academic conferences (NeurIPS, ICML), privacy conferences (PETS, IAPP), industry whitepapers
    - Target: ≥2 publications per year
  - **Open-Source Contributions**: Released privacy-preserving ML tools, frameworks, or datasets to open-source community
    - Examples: Federated learning framework, differential privacy library, privacy test datasets
    - Impact: ≥100 GitHub stars or active community adoption
  - **Standards Participation**: Active participation in privacy/ML standards development
    - Examples: ISO 27701, NIST Privacy Framework, IEEE privacy standards, W3C Privacy Interest Group

- [ ] **Industry thought leadership** demonstrated:
  - **Conference Presentations**: Present at privacy/security conferences on data security architecture
    - Target: ≥2 external presentations per year (RSA, Black Hat, IAPP Global Privacy Summit, Strata Data Conference)
  - **Best Practices Sharing**: Publish architectural patterns, lessons learned, case studies
    - Topics: Federated data security architecture, privacy-by-design patterns, autonomous governance
    - Format: Blog posts, whitepapers, architecture diagrams shared under Creative Commons
  - **Community Engagement**: Contribute to industry forums, privacy communities, architecture working groups

- [ ] **Measurable business impact** quantified:
  - **Privacy ROI**: Privacy program ROI ≥5:1 (benefits exceed costs by 5x per SR-Data Level 3)
    - Cost avoidance: Regulatory fines avoided, breach costs prevented
    - Efficiency gains: Time/cost savings from automation
    - Revenue enablement: Business enabled by privacy compliance (customer trust, competitive advantage, new markets)
  - **Data minimization impact**: ≥40% reduction in sensitive data volume year-over-year (through proactive deletion, anonymization, consolidation per SR-Data Level 3)
  - **User satisfaction**: ≥85% users agree "AI data security enables my work rather than blocks it" (SR-Data Level 3)

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
| 1.1 | AI model architecture documentation (classification, DLP detection) | | |
| 1.1 | Data discovery architecture and scan coverage metrics | | |
| 1.2 | Multi-channel DLP architecture documentation | | |
| 1.2 | Privacy-preserving AI architecture documentation | | |
| 1.3 | Data access policy enforcement (ABAC, just-in-time access) | | |
| 1.3 | Compliance automation architecture (GDPR, CCPA) | | |
| 2.1 | Data lineage architecture and flow diagrams | | |
| 2.1 | Cross-system correlation implementation | | |
| 2.2 | Privacy-enhancing technologies (tokenization, FPE, anonymization) | | |
| 2.2 | Key management architecture documentation | | |
| 2.3 | Proactive data risk reduction architecture and metrics | | |
| 3.1 | Federated data security implementation (federated learning, SMPC) | | |
| 3.2 | Zero-knowledge proof and blockchain lineage implementation | | |
| 3.3 | Autonomous data governance metrics and industry contributions | | |

---

## Data Domain-Specific Notes

### Architecture Principles for AI Data Security

**Privacy-First Architecture**:
- AI data security systems must be architected to minimize privacy risk while maximizing security effectiveness
- Data minimization: AI should classify based on metadata/sampling, not always read full content
- Privacy-preserving ML: Differential privacy, federated learning, secure aggregation protect training data
- Access controls: AI service accounts have least privilege, time-limited access, full audit trails

**Multi-Channel Consistency**:
- DLP policies must be consistent across all channels (email, endpoint, network, cloud)
- Centralized policy engine ensures uniform enforcement
- Risk-based approach: High-risk data gets stricter controls across all channels

**Scalability Requirements**:
- Data security AI must scale to organizational data footprint (petabytes, millions of files)
- Distributed scanning, incremental scanning, statistical sampling enable scalability
- Performance: ≥1 TB/hour batch scanning, ≤500ms real-time classification for DLP

### Privacy-Enhancing Technologies (PETs)

**Tokenization vs Encryption**:
- **Tokenization**: Replace sensitive data with tokens (reversible via token vault), reduces PCI-DSS scope, enables analytics on tokenized data
- **Format-Preserving Encryption (FPE)**: Encrypt while maintaining format, enables use in legacy systems without schema changes
- **Standard Encryption**: AES-256 for data at rest, TLS 1.2+ for data in transit

**Anonymization Techniques**:
- **K-anonymity**: Each record indistinguishable from ≥k-1 others
- **L-diversity**: Ensure diversity of sensitive attributes within k-anonymous groups
- **Differential Privacy**: Add statistical noise to protect individuals while preserving aggregate utility
- **GDPR Standard**: ≥99% confidence data cannot be re-identified

**Advanced PETs (Level 3)**:
- **Federated Learning**: Train models on distributed data without centralizing (privacy-preserving, regulatory compliant)
- **Secure Multi-Party Computation (SMPC)**: Collaborative analysis without sharing raw data
- **Zero-Knowledge Proofs**: Prove policy compliance without revealing data
- **Homomorphic Encryption**: Compute on encrypted data without decryption (emerging technology, high overhead)

### Compliance Automation Architecture

**GDPR Automation**:
- **Article 15 (Access)**: AI finds all data for individual, generates report within 30 days (target: ≤7 days)
- **Article 17 (Deletion)**: AI deletes all instances, verifies completion within 30 days
- **Article 30 (Records of Processing)**: AI auto-generates RoPA from data lineage
- **Article 35 (DPIA)**: AI assists with Data Protection Impact Assessments for new systems

**CCPA Automation**:
- Data inventory maintained in real-time as AI discovers/classifies data
- Consumer rights (access, deletion, opt-out) automated via AI discovery + workflow
- Do-not-sell enforcement via AI policy engine

**Cross-Regulatory Complexity**:
- Organizations often subject to GDPR, CCPA, HIPAA, PCI-DSS, industry-specific regulations simultaneously
- Architecture must support multiple overlapping compliance frameworks
- When regulations conflict, architecture escalates to legal team (don't auto-delete when legal hold exists)

### Data Lineage and Flow Analysis

**Lineage Discovery Methods**:
- **Query Log Analysis**: Analyze database queries to identify data movement
- **Application Monitoring**: Monitor API calls, data transformations in applications
- **Network Traffic Analysis**: Identify data transfers between systems

**Lineage Use Cases**:
- **Compliance**: GDPR Article 30 Records of Processing, demonstrate data handling for audits
- **Data Subject Requests**: Use lineage to find all instances of individual's data
- **Risk Analysis**: Identify risky data flows (cross-border, insecure channels, unnecessary flows)
- **Impact Analysis**: Understand downstream impact before deleting/modifying data

### Integration with Other Practices

- **Threat Assessment (TA-Data)**: TA identifies threats (classification poisoning, DLP evasion, model inversion) → SA designs defenses
- **Security Requirements (SR-Data)**: SR defines accuracy requirements (≥92% structured, ≥88% unstructured) → SA implements models to achieve
- **Design Review (DR-Data)**: DR reviews architecture before deployment, validates privacy-preserving design
- **Implementation Review (IR-Data)**: IR validates implementation matches architectural design

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
**Practice:** Secure Architecture (SA)
**Domain:** Data
**Questionnaire Version:** 1.0
**Last Updated:** December 2025
