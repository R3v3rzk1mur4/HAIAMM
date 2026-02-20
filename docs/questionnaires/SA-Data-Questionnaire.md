# Secure Architecture (SA) - Data Domain Assessment Questionnaire
## HAIAMM v3.0
**Scoring Model:** Evidence + Outcome Metrics

---

## Purpose

This questionnaire assesses organizational maturity in establishing architectural design for AI-powered data security systems (data classification, DLP, privacy automation). It evaluates AI model architecture, data discovery architecture, multi-channel DLP, privacy-preserving processing, data access policy enforcement, and compliance automation.

---

## Instructions

- Answer each question honestly based on current organizational practices
- Select a maturity tier only if you have documented evidence of the practice and metric data to support it
- Provide specific evidence in the "Evidence Repository" section
- Calculate your maturity level using the scoring guide at the end

---

## Level 1: Foundational (0-3 points)

### Question 1.1: AI Model Architecture and Data Discovery

**Question:** Have you designed AI model architecture for data classification and DLP detection, with scalable data discovery and scanning architecture deployed?

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
    - Throughput: Scan >= 1 TB of data per hour (baseline)
    - Latency: Real-time classification <= 500ms (for DLP inline blocking)

- [ ] **Scan coverage achieved**:
  - >= 95% of data repositories scanned within 30 days of deployment
  - >= 80% of organizational data classified (SR-Data requirement)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Data classification accuracy (structured data) | ___ | ___ | >= 92% | ☐ | |
| Data repository scan coverage | ___ | ___ | >= 95% within 30 days | ☐ | |
| Real-time classification latency (p95) | ___ | ___ | <= 500ms | ☐ | |
| Organizational data classified (% of total) | ___ | ___ | >= 80% | ☐ | |

**Metric Collection Guidance:**
- **Data classification accuracy (structured data)**: Sample audit of 500+ classified records monthly; formula: (correctly classified records / total sampled) x 100; source: classification engine audit logs + human review
- **Data repository scan coverage**: Data discovery dashboard; formula: (repositories scanned in last 30 days / total known repositories) x 100; source: discovery scan job logs
- **Real-time classification latency (p95)**: APM tooling (Datadog, Prometheus); formula: 95th percentile latency from DLP inline classification events; frequency: continuous, report weekly
- **Organizational data classified (% of total)**: Data catalog or DSPM platform; formula: (volume of classified data / total estimated data volume) x 100; frequency: monthly reconciliation

**Answer:**
- ☐ **Fully Mature** (Evidence complete + >= 75% of metrics meet targets = >= 3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________
**Metric Validation Date:** _________________________________
**Notes:** ___________________________________________

---

### Question 1.2: Multi-Channel DLP Architecture and Privacy-Preserving AI

**Question:** Have you implemented multi-channel DLP architecture (email, endpoint, network, cloud) with centralized policy enforcement, and privacy-preserving AI processing architecture?

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
    - **Sampling**: Analyze sample of data (10 rows of database, 10 files in folder), not entire dataset
    - **Anonymization**: When AI must analyze content, anonymize before AI processing
      - Replace actual PII with tokens: "John Smith" -> "[NAME]", "123-45-6789" -> "[SSN]"
  - **Differential Privacy in AI Training**:
    - Add noise to AI training data to prevent AI from memorizing individual records
    - Privacy budget (epsilon) defined: epsilon <= 10 for training (SR-Data requirement)
  - **Access Controls for AI**:
    - AI service account: Read-only access to data
    - Least privilege: Access scoped to repositories being scanned
    - Time-limited: Credentials expire after scan completion (<= 24 hours per SR-Data)
    - Audit: All AI data access logged with timestamp, data accessed, purpose

- [ ] **Privacy protection validated**:
  - Zero GDPR/CCPA violations from AI data processing (SR-Data requirement)
  - AI model privacy tested: <= 0.1% success rate in extracting sensitive values from model (SR-Data requirement)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| DLP detection rate for sensitive data exfiltration attempts | ___ | ___ | >= 93% | ☐ | |
| DLP false positive rate (legitimate work blocked) | ___ | ___ | <= 8% | ☐ | |
| DLP channel coverage (channels actively enforcing policy) | ___ | ___ | 4 of 4 channels (email, endpoint, network, cloud) | ☐ | |
| Privacy compliance violations from AI data processing | ___ | ___ | 0 GDPR/CCPA violations | ☐ | |

**Metric Collection Guidance:**
- **DLP detection rate for sensitive data exfiltration attempts**: DLP platform reporting; formula: (true positive DLP blocks / (true positive blocks + false negatives from red team or audit)) x 100; frequency: monthly; supplement with quarterly red team exercise
- **DLP false positive rate (legitimate work blocked)**: DLP platform + user appeal/override logs; formula: (legitimate transfers blocked or flagged / total DLP events) x 100; frequency: weekly, trend monthly
- **DLP channel coverage**: Architecture inventory audit; formula: count of active DLP channels with policy enforcement enabled / 4 total channels; frequency: quarterly architecture review
- **Privacy compliance violations from AI data processing**: DPO incident log + regulatory reporting system; formula: count of GDPR/CCPA violations attributable to AI data processing activities; frequency: monthly review with DPO

**Answer:**
- ☐ **Fully Mature** (Evidence complete + >= 75% of metrics meet targets = >= 3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________
**Metric Validation Date:** _________________________________
**Notes:** ___________________________________________

---

### Question 1.3: Data Access Policy Enforcement and Compliance Automation Architecture

**Question:** Have you established data access policy enforcement architecture (ABAC, just-in-time access) and compliance automation architecture for GDPR/CCPA (DSAR, deletion, retention)?

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
    - Performance: Locate data within <= 48h, generate report within <= 72h (SR-Data requirement, within GDPR 30-day window)
    - Accuracy: >= 95% recall (find 95% of individual's data per SR-Data)
  - **Article 17 (Right to be Forgotten)**: AI deletes individual's data
    - Discovery: Find all instances of individual's data across all systems
    - Deletion: Automated deletion workflow + verification
    - Timeline: <= 30 days (GDPR requirement)
    - Verification: >= 99% confidence deletion completed (SR-Data requirement)
    - Safety: Soft-delete to quarantine for >= 30 days before hard delete (SR-Data safety guardrail)

- [ ] **CCPA automation architecture** implemented:
  - **Data Inventory**: AI maintains inventory of personal information (categories, sources, purposes, third parties, retention periods)
  - **Do Not Sell Tracking**: AI tracks which data can be sold vs not, prevents sale of flagged data
  - **Consumer Rights Automation**:
    - Right to Know: Generate report within 45 days (>= 95% recall per SR-Data)
    - Right to Delete: Identify and delete within 45 days (>= 95% recall, >= 99% verification per SR-Data)
    - Right to Opt-Out: Flag consumer data as "do not sell", prevent future sales

- [ ] **Data retention architecture** implemented:
  - **Automated Retention Policy Enforcement**:
    - AI identifies data exceeding retention limits based on policies (GDPR, CCPA, HIPAA, PCI-DSS, internal policies)
    - Auto-flag for review or auto-delete (with approval workflow per SR-Data)
  - **Retention Enforcement Metrics**: >= 90% of data within retention limits

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| DSAR fulfillment time (average days to fulfill data subject request) | ___ | ___ | <= 7 days (vs 30-day legal limit) | ☐ | |
| Data deletion verification confidence (Right to be Forgotten completeness) | ___ | ___ | >= 99% verified deletion | ☐ | |
| Data within retention policy limits | ___ | ___ | >= 90% of data stores compliant | ☐ | |
| ABAC policy coverage for sensitive data repositories | ___ | ___ | >= 95% of sensitive repositories under ABAC | ☐ | |

**Metric Collection Guidance:**
- **DSAR fulfillment time**: Privacy request management system (OneTrust, TrustArc, or equivalent); formula: average calendar days from request receipt to report delivery, tracked per request; frequency: monthly aggregate
- **Data deletion verification confidence**: Deletion audit workflow logs; formula: (deletion requests with >= 99% verified completion across all systems / total deletion requests) x 100; verified via sampling re-scan post-deletion; frequency: per-request + monthly summary
- **Data within retention policy limits**: Data catalog / DSPM tool scan; formula: (data assets confirmed within policy-defined retention period / total data assets with defined retention policy) x 100; frequency: monthly automated scan
- **ABAC policy coverage for sensitive data repositories**: Identity governance platform + data catalog; formula: (sensitive repositories with ABAC enforcement enabled / total sensitive repositories identified) x 100; frequency: quarterly

**Answer:**
- ☐ **Fully Mature** (Evidence complete + >= 75% of metrics meet targets = >= 3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________
**Metric Validation Date:** _________________________________
**Notes:** ___________________________________________

---

## Level 2: Comprehensive (4-6 points)

### Question 2.1: Data Lineage Architecture and Cross-System Correlation

**Question:** Have you implemented data lineage and flow tracking architecture with automated lineage discovery, and cross-system data correlation architecture for aggregation detection?

**Evidence Required:**
- [ ] **Automated data lineage discovery** implemented:
  - **Data Flow Tracking**: Track data flow from source -> processing -> storage -> consumption
  - **Discovery Methods**:
    - Query log analysis (database queries showing data movement)
    - Application monitoring (API calls, data transformations)
    - Network traffic analysis (data transfers between systems)
  - **Coverage**: Map >= 80% of sensitive data flows within organization (SR-Data Level 2 requirement)
  - **Lineage Visualization**: Generate data flow diagrams showing how PII/PHI flows through systems
    - Visual representation of data sources, processing systems, destination systems
    - Interactive lineage exploration (click on dataset to see upstream/downstream flows)

- [ ] **Data flow mapping for risk analysis** implemented:
  - **Cross-Border Flow Detection**: Identify data flows crossing regulatory boundaries
    - Detect: EU citizen PII transferred to US servers (GDPR Article 44-50 restrictions)
    - Detect: Chinese citizen data transferred outside China (China PIPL requirements)
    - Accuracy: >= 90% detection of cross-border flows (SR-Data requirement)
    - Action: Verify appropriate transfer mechanism (SCCs, BCRs, adequacy decision) or block transfer
  - **Risky Flow Identification**: Identify data flows to unsecured systems, unauthorized destinations, excessive data sharing
    - Example: PHI transferred via unencrypted email (HIPAA violation)
    - Detection accuracy: >= 90% for common insecure patterns (SR-Data requirement)

- [ ] **Data lineage for compliance** implemented:
  - **GDPR Article 30 Records of Processing**: Auto-generate GDPR documentation
    - Track: Categories of data, purposes of processing, recipients, retention periods, transfers to third countries
    - Accuracy: >= 95% completeness (cover 95% of actual processing activities per SR-Data)
    - Export: Generate Article 30-compliant Records of Processing Activities (RoPA) report on demand
  - **Data Subject Request Fulfillment**: Use lineage to find all instances of individual's data
    - Accuracy: >= 97% recall (SR-Data Level 2 requirement)
    - Time: <= 48 hours for standard request

- [ ] **Cross-system data correlation architecture** implemented:
  - **Data Aggregation Detection**: Detect when non-sensitive data pieces combine to create sensitive aggregation
    - Detection accuracy: >= 85% for common aggregation patterns (SR-Data Level 2 requirement)
    - Action: Reclassify aggregated dataset as sensitive, restrict access
  - **Derived Data Classification**: Classify data derived from sensitive sources
    - Accuracy: >= 90% correct classification of derived data products (SR-Data requirement)

- [ ] **Third-party data sharing monitoring** implemented:
  - **Vendor Data Sharing Tracking**: Maintain inventory (vendor name, data types shared, business purpose, data processing agreement status)
    - Requirement: >= 95% of vendor data sharing has documented business purpose and data processing agreement (SR-Data)
  - **Data Sharing Agreement Compliance**: Monitor that sharing stays within agreement bounds
    - Accuracy: >= 88% detection of out-of-scope data sharing (SR-Data)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Sensitive data flow lineage coverage | ___ | ___ | >= 80% of sensitive data flows mapped | ☐ | |
| Cross-border data flow detection accuracy | ___ | ___ | >= 90% detection rate | ☐ | |
| GDPR Article 30 RoPA completeness | ___ | ___ | >= 95% of processing activities documented | ☐ | |
| Data aggregation / derived data misclassification rate | ___ | ___ | <= 10% (>= 90% correct classification) | ☐ | |

**Metric Collection Guidance:**
- **Sensitive data flow lineage coverage**: Data lineage platform (Collibra, Alation, Apache Atlas, or equivalent); formula: (sensitive data flows with mapped lineage / total sensitive data flows identified via network analysis) x 100; frequency: quarterly reconciliation
- **Cross-border data flow detection accuracy**: Network monitoring + lineage platform; formula: (cross-border flows correctly detected / (correctly detected + missed cross-border flows from audit sample)) x 100; supplement with quarterly manual audit of network egress; frequency: monthly
- **GDPR Article 30 RoPA completeness**: Privacy management platform vs actual processing activities log; formula: (processing activities in RoPA / total known processing activities confirmed by business units) x 100; frequency: semi-annual business unit survey + continuous lineage updates
- **Data aggregation / derived data misclassification rate**: Classification audit of derived datasets; formula: (incorrectly classified derived data assets / total derived data assets audited) x 100; audit sample >= 100 derived datasets per quarter; frequency: quarterly

**Answer:**
- ☐ **Fully Mature** (Evidence complete + >= 75% of metrics meet targets = >= 3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________
**Metric Validation Date:** _________________________________
**Notes:** ___________________________________________

---

### Question 2.2: Privacy-Enhancing Technologies Architecture

**Question:** Have you designed and deployed privacy-enhancing technologies (tokenization, format-preserving encryption, anonymization) with secure architecture for token vaults and key management?

**Evidence Required:**
- [ ] **Tokenization architecture** implemented:
  - **Token Generation**: Replace sensitive data with tokens (reversible mapping)
    - Example: Credit card "4111-1111-1111-1111" -> Token "TKN-8472-9384-7261"
  - **Token Vault**: Secure storage for token mappings
    - Encrypted storage (AES-256 or equivalent)
    - Access controls: Only authorized systems can de-tokenize
    - High availability: >= 99.9% uptime for token vault (business depends on de-tokenization)
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
    - **L-diversity**: Within each k-anonymous group, ensure diversity of sensitive attributes
    - **T-closeness**: Distribution of sensitive attribute in group close to distribution in overall dataset
    - **Differential Privacy**: Add statistical noise to protect individuals while preserving aggregate statistics
  - **Anonymization Quality**: Anonymization meets GDPR standard (>= 99% confidence data cannot be re-identified per SR-Data Level 2)
  - **Coverage**: >= 80% of non-production uses of PII replaced with anonymized alternatives within 12 months (SR-Data Level 2)

- [ ] **Pseudonymization architecture** implemented:
  - **Pseudonymization**: Replace identifiers with pseudonyms where reversibility needed
  - **Security**: Pseudonym mapping key stored separately with strict access controls
  - **Re-identification Protection**: >= 99% probability that pseudonym cannot be linked back without key (SR-Data)

- [ ] **Key management architecture** implemented:
  - **Centralized Key Management**: Keys for encryption, tokenization, pseudonymization managed centrally
  - **Key Storage**: Hardware Security Module (HSM) or cloud KMS (AWS KMS, Azure Key Vault, GCP KMS)
  - **Key Rotation**: Automated key rotation (e.g., monthly/quarterly)
  - **Access Controls**: Separation of duties (different roles for key generation, usage, management)
  - **Audit**: All key access logged

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| PII tokenization / encryption coverage in non-production environments | ___ | ___ | >= 80% of non-production PII uses replaced | ☐ | |
| Token vault availability | ___ | ___ | >= 99.9% uptime | ☐ | |
| Anonymization re-identification risk | ___ | ___ | <= 1% re-identification probability (>= 99% confidence) | ☐ | |
| Key rotation compliance rate | ___ | ___ | 100% of keys rotated on schedule | ☐ | |

**Metric Collection Guidance:**
- **PII tokenization / encryption coverage in non-production environments**: Data catalog scan of non-production environments (dev, test, staging); formula: (non-production data stores using tokenized/anonymized PII / total non-production data stores containing any PII) x 100; frequency: quarterly automated scan
- **Token vault availability**: Infrastructure monitoring (Datadog, CloudWatch, or equivalent); formula: (uptime minutes in period / total minutes in period) x 100; measurement window: rolling 30 days; frequency: continuous monitoring, monthly SLA report
- **Anonymization re-identification risk**: Privacy engineering tool (ARX, Python-based k-anonymity checker, or third-party audit); formula: probability score from re-identification risk assessment on anonymized dataset sample; frequency: per anonymization deployment + semi-annual audit of production anonymized datasets
- **Key rotation compliance rate**: Key Management System audit logs (AWS KMS, Azure Key Vault, or HSM console); formula: (keys rotated within scheduled window / total keys with defined rotation schedule) x 100; frequency: monthly automated compliance check

**Answer:**
- ☐ **Fully Mature** (Evidence complete + >= 75% of metrics meet targets = >= 3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________
**Metric Validation Date:** _________________________________
**Notes:** ___________________________________________

---

### Question 2.3: Proactive Data Risk Reduction Architecture

**Question:** Have you implemented proactive data risk reduction architecture (data minimization automation, purpose limitation enforcement, privacy by design) that identifies and reduces unnecessary sensitive data?

**Evidence Required:**
- [ ] **Data minimization automation architecture** implemented:
  - **Unnecessary PII Detection**: AI identifies PII collected or retained without clear business purpose
    - Flag: PII not accessed in >= 365 days with no documented retention requirement = "Candidate for deletion"
    - Accuracy: >= 90% correct identification of unnecessary PII (SR-Data Level 2)
    - Action: Generate deletion recommendations for data stewards, track progress on deletion
  - **Auto-Deletion Workflow**: Automated deletion of clearly unnecessary data
    - Criteria: Data >7 years old, no regulatory retention requirement, no business access in >2 years
    - Safety: Soft-delete to quarantine, DPO review weekly, hard-delete after 30 days
    - Impact: >= 10% of total PII deleted quarterly based on AI recommendations (SR-Data Level 2 process metric)

- [ ] **Purpose limitation enforcement architecture** implemented:
  - **Purpose Tracking**: AI ensures data is used only for stated purpose
    - Track: Data collection purpose (from privacy notices, consent forms, business documentation)
    - Monitor: Actual data usage (which teams access data, for which applications)
    - Detect: Usage beyond stated purpose (>= 85% accuracy per SR-Data Level 2)
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
    - Result: >= 95% of new data repositories start with restrictive access (SR-Data Level 2)

- [ ] **Sensitive data exposure reduction architecture** implemented:
  - **Least Privilege for Data Access**: AI identifies and reduces overly broad data access
    - Result: Reduce users with access to each sensitive dataset by >= 30% (SR-Data Level 2)
  - **Data Location Consolidation**: AI identifies sensitive data sprawl
    - Result: Reduce number of locations storing each sensitive dataset by >= 40% (SR-Data Level 2)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| PII deleted quarterly via AI minimization recommendations | ___ | ___ | >= 10% of total PII volume per quarter | ☐ | |
| New data sources classified within 24 hours of onboarding | ___ | ___ | >= 95% of new sources | ☐ | |
| Users with unnecessary access to sensitive datasets (access unused >= 90 days) | ___ | ___ | >= 30% reduction from baseline | ☐ | |
| Sensitive data location sprawl (average locations per sensitive dataset) | ___ | ___ | >= 40% reduction from baseline | ☐ | |

**Metric Collection Guidance:**
- **PII deleted quarterly via AI minimization recommendations**: Data minimization workflow tracking system; formula: (volume/count of PII records hard-deleted per quarter via AI recommendations / total PII volume at start of quarter) x 100; frequency: quarterly; track as running total of accepted recommendations
- **New data sources classified within 24 hours of onboarding**: Data discovery event log; formula: (new data sources where first classification scan completed within 24 hours of registration / total new data sources registered) x 100; frequency: monthly; trigger tracked via asset management or CMDB integration
- **Users with unnecessary access to sensitive datasets**: Identity governance platform access certification reports; formula: ((users with access but no access events in >= 90 days at baseline - same count now) / baseline count) x 100; frequency: quarterly access recertification campaign
- **Sensitive data location sprawl**: DSPM or data catalog; formula: average count of distinct storage locations per sensitive dataset class (compare current vs baseline); track top 20 sensitive dataset types; frequency: quarterly

**Answer:**
- ☐ **Fully Mature** (Evidence complete + >= 75% of metrics meet targets = >= 3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________
**Metric Validation Date:** _________________________________
**Notes:** ___________________________________________

---

## Level 3: Industry-Leading (7-9 points)

### Question 3.1: Federated Data Security Architecture

**Question:** Have you implemented federated data security architecture that enables analysis of distributed data without centralizing sensitive information (federated learning, secure multi-party computation)?

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
  - **Use Cases**: Cross-organization analytics, regulatory reporting without centralizing sensitive data, privacy-preserving data sharing
  - **Performance**: SMPC has computational overhead (10-100x slower than plaintext computation), architect for acceptable latency

- [ ] **Differential privacy for external data sharing** implemented:
  - **Privacy Budget for Sharing**: Add noise to shared datasets to protect individual privacy while preserving statistical utility
    - Privacy budget (epsilon) for external sharing: epsilon <= 5 (stricter than epsilon <= 10 for internal training per SR-Data Level 3)
  - **Use Cases**: Share aggregate statistics with partners/public, publish research datasets, contribute to industry benchmarks
  - **Quality Validation**: Verify anonymized data maintains utility for intended analytics (test statistical properties preserved)

- [ ] **Privacy-preserving collaboration enabled**:
  - Documented examples of collaborative data analysis with partners/customers without sharing raw sensitive data
  - Business value quantified (e.g., enabled partnership worth $X, unlocked analytics use case generating $Y value)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Federated model classification accuracy vs centralized baseline | ___ | ___ | >= 90% of centralized model accuracy | ☐ | |
| Privacy-preserving collaboration use cases enabled | ___ | ___ | >= 1 production use case live | ☐ | |
| External data sharing privacy budget compliance (epsilon) | ___ | ___ | epsilon <= 5 for all external sharing | ☐ | |
| Raw PII centralized for cross-entity analytics (target: zero centralization) | ___ | ___ | 0 raw PII centralized from federated sources | ☐ | |

**Metric Collection Guidance:**
- **Federated model classification accuracy vs centralized baseline**: Model evaluation framework; formula: (federated model F1 score on holdout test set / centralized model F1 score on same test set) x 100; run evaluation monthly using a shared labeled test set that does not require raw training data access; frequency: monthly
- **Privacy-preserving collaboration use cases enabled**: Architecture inventory and partnership agreement register; formula: count of distinct production use cases using federated learning or SMPC instead of raw data sharing; frequency: semi-annual inventory update
- **External data sharing privacy budget compliance**: Differential privacy accounting library (Google DP library, OpenDP, or equivalent); formula: maximum epsilon value recorded across all external sharing events in period; alert if any event exceeds epsilon = 5; frequency: per-sharing-event + monthly summary
- **Raw PII centralized for cross-entity analytics**: Data lineage platform + network egress monitoring; formula: count of data flows where raw (untokenized, un-anonymized) PII traverses entity boundaries for analytics purposes; target is zero; frequency: continuous monitoring with monthly zero-violation attestation

**Answer:**
- ☐ **Fully Mature** (Evidence complete + >= 75% of metrics meet targets = >= 3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________
**Metric Validation Date:** _________________________________
**Notes:** ___________________________________________

---

### Question 3.2: Zero-Knowledge and Blockchain-Based Data Governance Architecture

**Question:** Have you designed zero-knowledge architecture for data security policy verification, and blockchain-based data lineage for immutable audit trails?

**Evidence Required:**
- [ ] **Zero-knowledge proof architecture** implemented:
  - **Zero-Knowledge Proofs (ZKP)**: Prove data meets security policy without revealing data itself
    - Example: Prove "this dataset contains no PII" without showing the dataset contents
    - Example: Prove "user X has access permission to data Y" without revealing access control list
  - **Use Cases**: Privacy-preserving access control, compliance verification, audit
  - **ZKP Implementation**: Use ZKP libraries (e.g., ZoKrates, libsnark, Bulletproofs)
  - **Deployment**: ZKP used for at least one production use case (access control, compliance verification, or audit)

- [ ] **Blockchain-based data lineage** implemented:
  - **Immutable Audit Trail**: Record data access, data movement, data transformations on blockchain
    - Benefits: Tamper-proof audit trail, transparency, regulatory compliance
  - **Blockchain Architecture**: Private/permissioned blockchain (not public blockchain - performance and privacy)
    - Technologies: Hyperledger Fabric, Ethereum private network, or similar
  - **Data Lineage on Blockchain**: Record lineage events (data created, accessed, transformed, deleted, shared)
    - Hash of data + metadata recorded on blockchain (not full data - privacy)
    - Data location, timestamp, user, operation, purpose logged immutably
  - **Use Cases**: Regulatory audit, incident investigation, cross-organization data sharing

- [ ] **Homomorphic encryption architecture** explored/implemented:
  - **Homomorphic Encryption (HE)**: Perform computations on encrypted data without decryption
  - **Current Limitation**: HE has significant computational overhead (1000x+ slower than plaintext), limited to specific operations
  - **Implementation Status**: Pilot/proof-of-concept for specific use case, or monitoring HE research for production readiness
  - **Use Cases**: Cloud analytics on sensitive data, regulatory compliance (data never decrypted outside secure environment)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| ZKP production use cases deployed | ___ | ___ | >= 1 production use case | ☐ | |
| Blockchain lineage audit trail coverage (% of sensitive data events recorded immutably) | ___ | ___ | >= 90% of sensitive data events | ☐ | |
| Blockchain lineage tamper detection rate | ___ | ___ | 100% of tamper attempts detected | ☐ | |
| Homomorphic encryption / advanced PET pilot status | ___ | ___ | >= 1 pilot completed or production deployed | ☐ | |

**Metric Collection Guidance:**
- **ZKP production use cases deployed**: Architecture registry and deployment log; formula: count of distinct production workflows using ZKP verification instead of direct data inspection; frequency: semi-annual inventory
- **Blockchain lineage audit trail coverage**: Blockchain node event log vs total sensitive data events in lineage platform; formula: (sensitive data events (access, transform, transfer, delete) recorded on blockchain / total sensitive data events in source systems) x 100; frequency: monthly reconciliation between blockchain ledger and lineage platform
- **Blockchain lineage tamper detection rate**: Blockchain integrity verification job (hash validation run nightly); formula: (tamper attempts detected by hash mismatch / total tamper attempts detected by any means) x 100; supplement with quarterly red team integrity test; frequency: continuous verification with monthly summary
- **Homomorphic encryption / advanced PET pilot status**: Project tracking system; formula: binary indicator (0 = no pilot; 1 = pilot completed or production deployed) for each advanced PET category; note computational overhead benchmarks from pilot; frequency: semi-annual review

**Answer:**
- ☐ **Fully Mature** (Evidence complete + >= 75% of metrics meet targets = >= 3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________
**Metric Validation Date:** _________________________________
**Notes:** ___________________________________________

---

### Question 3.3: Autonomous Data Governance and Industry Contribution

**Question:** Have you achieved autonomous data governance with self-optimizing classification and policy enforcement, while contributing to privacy-preserving ML research and industry standards?

**Evidence Required:**
- [ ] **Autonomous data governance** achieved:
  - **Self-Optimizing Classification**: AI automatically improves classification accuracy over time
    - Automated model retraining: When drift detected (>10% distribution shift or >5% accuracy degradation), trigger retraining within 14 days
    - A/B testing: New models tested against production model, automatically promoted if superior
    - Result: Classification accuracy improves year-over-year without manual tuning
  - **Autonomous Policy Enforcement**: Policies automatically adapt to business changes
    - Example: New business unit created -> AI automatically extends data access policies to new unit
    - Example: Employee role change -> AI automatically adjusts data access within 24 hours
  - **Autonomous Compliance**: AI automatically detects regulatory changes and updates compliance controls
    - Adapt: Update policies within 30 days of new regulation effective date (SR-Data Level 3)
  - **Human Oversight**: Autonomous operations monitored by data stewards, DPO, security team

- [ ] **Self-healing architecture** implemented:
  - **Automated Error Detection**: AI detects when it makes classification errors
  - **Automated Remediation**: AI attempts to fix errors automatically
    - Reclassify misclassified data, update policies to prevent recurrence
    - If auto-remediation not possible, escalate to human with context
  - **Continuous Validation**: Daily/weekly automated testing validates AI continues to meet accuracy requirements (>= 97% per SR-Data Level 3)

- [ ] **Privacy-preserving ML research contribution** demonstrated:
  - **Research Publications**: Published research on privacy-preserving ML techniques
    - Target: >= 2 publications per year
  - **Open-Source Contributions**: Released privacy-preserving ML tools, frameworks, or datasets to open-source community
    - Impact: >= 100 GitHub stars or active community adoption
  - **Standards Participation**: Active participation in privacy/ML standards development (ISO 27701, NIST Privacy Framework, IEEE privacy standards)

- [ ] **Industry thought leadership** demonstrated:
  - **Conference Presentations**: Target: >= 2 external presentations per year
  - **Best Practices Sharing**: Publish architectural patterns, lessons learned, case studies
  - **Community Engagement**: Contribute to industry forums, privacy communities, architecture working groups

- [ ] **Measurable business impact** quantified:
  - **Privacy ROI**: Privacy program ROI >= 5:1 (SR-Data Level 3)
  - **Data minimization impact**: >= 40% reduction in sensitive data volume year-over-year (SR-Data Level 3)
  - **User satisfaction**: >= 85% users agree "AI data security enables my work rather than blocks it" (SR-Data Level 3)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Classification accuracy under autonomous operation (year-over-year improvement) | ___ | ___ | >= 97% accuracy + year-over-year improvement | ☐ | |
| Sensitive data volume reduction (year-over-year via minimization + anonymization) | ___ | ___ | >= 40% YoY reduction | ☐ | |
| Privacy program ROI | ___ | ___ | >= 5:1 (benefits vs costs) | ☐ | |
| Industry contributions per year (publications + open-source + conference talks) | ___ | ___ | >= 4 total contributions per year | ☐ | |

**Metric Collection Guidance:**
- **Classification accuracy under autonomous operation**: Automated model evaluation pipeline; formula: F1 score / accuracy on monthly holdout audit set (minimum 1,000 labeled samples); track trend line over 12+ months to demonstrate year-over-year improvement; frequency: monthly automated evaluation
- **Sensitive data volume reduction (year-over-year)**: Data catalog + DSPM platform volume tracking; formula: ((sensitive data volume at start of year - sensitive data volume at end of year) / sensitive data volume at start of year) x 100; include deletions, anonymization replacements, and consolidations; frequency: quarterly checkpoint, annual comparison
- **Privacy program ROI**: Finance + privacy team joint calculation; formula: (cost avoidance from fines prevented + breach cost reduction + efficiency savings + revenue from trust premium) / (total privacy program operating costs); document assumptions; frequency: annual; reviewed by CFO or finance business partner
- **Industry contributions per year**: Public record tracking (publication database, GitHub repository stats, conference agenda records); formula: count of distinct contributions (papers, open-source releases, conference presentations, standards body participation sessions) in trailing 12 months; frequency: quarterly inventory update

**Answer:**
- ☐ **Fully Mature** (Evidence complete + >= 75% of metrics meet targets = >= 3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________
**Metric Validation Date:** _________________________________
**Notes:** ___________________________________________

---

## Scoring Methodology

### Question Scoring (4-Tier)

| Answer | Score |
|--------|-------|
| Fully Mature | 1.0 |
| Implemented | 0.67 |
| Partial | 0.33 |
| Not Implemented | 0.0 |

### Level Scoring with Progression Rule

**Level 1 Score** = Average of Q1.1 + Q1.2 + Q1.3 scores (max 1.0)

**Level 2 Score** = Average of Q2.1 + Q2.2 + Q2.3 scores x Level 1 Score (max 1.0)
- Progression gate: If Level 1 Score < 1.0, Level 2 score is capped at 0.67 x (L2 raw average)

**Level 3 Score** = Average of Q3.1 + Q3.2 + Q3.3 scores x Level 2 Score (max 1.0)
- Progression gate: If Level 2 Score < 1.0, Level 3 score is capped at 0.67 x (L3 raw average)

### Practice Score

**SA-Data Practice Score = Level 1 Score + Level 2 Score + Level 3 Score (max 3.0)**

| Score Range | Maturity Level |
|-------------|---------------|
| 0.0 - 0.9 | Level 0: Ad-Hoc |
| 1.0 - 1.9 | Level 1: Foundational |
| 2.0 - 2.9 | Level 2: Comprehensive |
| 3.0 | Level 3: Industry-Leading |

**Your SA-Data Practice Score:** _______ / 3.0

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
- Performance: >= 1 TB/hour batch scanning, <= 500ms real-time classification for DLP

### Privacy-Enhancing Technologies (PETs)

**Tokenization vs Encryption**:
- **Tokenization**: Replace sensitive data with tokens (reversible via token vault), reduces PCI-DSS scope, enables analytics on tokenized data
- **Format-Preserving Encryption (FPE)**: Encrypt while maintaining format, enables use in legacy systems without schema changes
- **Standard Encryption**: AES-256 for data at rest, TLS 1.2+ for data in transit

**Anonymization Techniques**:
- **K-anonymity**: Each record indistinguishable from >= k-1 others
- **L-diversity**: Ensure diversity of sensitive attributes within k-anonymous groups
- **Differential Privacy**: Add statistical noise to protect individuals while preserving aggregate utility
- **GDPR Standard**: >= 99% confidence data cannot be re-identified

**Advanced PETs (Level 3)**:
- **Federated Learning**: Train models on distributed data without centralizing (privacy-preserving, regulatory compliant)
- **Secure Multi-Party Computation (SMPC)**: Collaborative analysis without sharing raw data
- **Zero-Knowledge Proofs**: Prove policy compliance without revealing data
- **Homomorphic Encryption**: Compute on encrypted data without decryption (emerging technology, high overhead)

### Compliance Automation Architecture

**GDPR Automation**:
- **Article 15 (Access)**: AI finds all data for individual, generates report within 30 days (target: <= 7 days)
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

- **Threat Assessment (TA-Data)**: TA identifies threats (classification poisoning, DLP evasion, model inversion) -> SA designs defenses
- **Security Requirements (SR-Data)**: SR defines accuracy requirements (>= 92% structured, >= 88% unstructured) -> SA implements models to achieve
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

### Next Assessment Date: _____________________

---

**Document Version:** HAIAMM v3.0
**Scoring Model:** Evidence + Outcome Metrics
**Practice:** Secure Architecture (SA)
**Domain:** Data
**Questionnaire Version:** 3.0
**Last Updated:** February 2026
