# Security Architecture Practice – Data Domain
## HAIAMM v2.1 One-Pager

### Practice Overview

The Security Architecture (SA) practice for the Data domain defines the architectural design for AI-powered data security systems (data classification, DLP, privacy automation). This practice establishes how AI data security capabilities should be architected to achieve security requirements while maintaining privacy, regulatory compliance, and business data access needs.

**Scope**: Architecture for:
- **AI Model Architecture**: Models for data classification, DLP detection, privacy risk analysis
- **Data Discovery Architecture**: Automated discovery of sensitive data across environments
- **Classification Architecture**: Real-time and batch data classification pipelines
- **DLP Architecture**: Multi-channel DLP (email, endpoint, network, cloud)
- **Privacy Automation Architecture**: GDPR/CCPA compliance automation
- **Data Lineage Architecture**: Track data flow across systems
- **Encryption & Tokenization Architecture**: Protect sensitive data at rest and in transit

**Why This Matters**: Data security AI must balance comprehensive scanning (find all sensitive data) with privacy protection (AI itself doesn't become data exposure risk), accurate classification (minimize false positives) with business enablement (don't over-classify and block work), and automated enforcement (DLP blocking) with user productivity. Architecture determines whether AI protects data without creating new vulnerabilities.

---

### Practice Maturity Levels

## Level 1: Foundational Architecture

### Core Objectives
1. Design AI models for data classification and DLP detection
2. Implement data discovery and scanning architecture
3. Establish multi-channel DLP architecture
4. Deploy privacy-preserving AI processing architecture
5. Implement data access policy enforcement architecture
6. Design compliance automation architecture

### Key Activities

#### 1. AI Model Architecture for Data Security

**Classification Models**:
- **Pattern Matching**: Regex patterns for structured data (SSN, credit cards, phone numbers)
  - Fast, accurate for well-formatted data
  - Limitation: Misses unformatted or obfuscated data

- **Machine Learning Classifiers**:
  - Named Entity Recognition (NER) for PII detection in text
  - Document classification (confidential vs public)
  - Context-aware classification (same data, different sensitivity in different contexts)

- **Deep Learning Models**:
  - Transformers (BERT) for semantic understanding of data sensitivity
  - Example: Distinguish between "John Smith" (name in document) vs "John Smith Corporation" (company name—not PII)

**Multi-Modal Classification**:
- **Text**: NLP models for documents, emails, chat
- **Images**: OCR + image classification for sensitive images (IDs, screenshots)
- **Structured Data**: Schema analysis + content sampling for databases

**DLP Detection Models**:
- **Content-Based**: Detect sensitive data in content (email body, file contents)
- **Context-Based**: Detect policy violations based on context (recipient, destination, time)
- **Behavior-Based**: Detect unusual data access patterns (user downloads 10x normal data volume)

#### 2. Data Discovery & Scanning Architecture

**Discovery Methods**:
- **Active Scanning**: Periodic scans of data repositories (daily/weekly/monthly based on risk)
  - Databases: Query for PII patterns
  - File Shares: Scan files for sensitive content
  - Cloud Storage: S3/Blob/GCS scanning
  - SaaS Apps: API-based scanning (Salesforce, Google Workspace, O365)

- **Passive Discovery**: Discover data during normal operations
  - DLP scanning of data in motion (emails, file uploads)
  - User access logging (what data accessed?)

**Scalability Architecture**:
- **Distributed Scanning**: Parallel scanning across multiple workers
- **Incremental Scanning**: Only scan changed data (not full rescans)
- **Sampling**: For massive datasets, statistical sampling (scan 10%, extrapolate)

**Discovery Performance**:
- **Throughput**: Scan 1 TB of data per hour (baseline)
- **Latency**: Real-time classification ≤500ms (for DLP inline blocking)

#### 3. Multi-Channel DLP Architecture

**DLP Channels**:
- **Email DLP**: Scan outbound emails + attachments
  - Integration: SMTP proxy, email gateway API (Proofpoint, Mimecast)
  - Action: Block, encrypt, quarantine, alert

- **Endpoint DLP**: Monitor data on endpoints
  - Agents on endpoints monitor file operations, clipboard, USB, screen capture
  - Integration: Endpoint agent architecture (similar to EDR)

- **Network DLP**: Scan network traffic
  - Deep packet inspection (DPI) for HTTP/S, FTP, etc.
  - Integration: Network TAPs, SPAN ports, cloud proxies

- **Cloud DLP**: Scan cloud storage and SaaS
  - API integration with cloud providers (AWS S3, Azure Blob, GCP Storage, Box, Dropbox)
  - CASB integration for SaaS app DLP

**DLP Decision Architecture**:
- **Policy Engine**: Centralized policy engine (what data can go where?)
- **Context Evaluation**: AI evaluates context (who, what, where, when, why)
- **Risk Scoring**: Combine data sensitivity + destination risk + user risk = Overall risk score
- **Action Selection**: Based on risk score: Allow, Alert, Block, Encrypt

#### 4. Privacy-Preserving AI Architecture

**Data Minimization in AI Processing**:
- **Metadata-Only Analysis**: AI classifies based on metadata (file name, schema, access patterns) without reading content
  - Example: File named "SSN_List.xlsx" in "/HR/Payroll" accessed only by HR → High confidence it's PII without opening file

- **Sampling**: Analyze sample of data (10 rows of database, 10 files in folder), not entire dataset

- **Anonymization**: When AI must analyze content, anonymize before AI processing
  - Replace actual PII with tokens: "John Smith" → "[NAME]", "123-45-6789" → "[SSN]"

**Differential Privacy in AI**:
- Add noise to AI training data (prevent AI from memorizing individual records)
- Privacy budget (ε): How much privacy loss acceptable

**Access Controls for AI**:
- AI service account: Read-only access to data
- Least privilege: Access only repositories being scanned
- Time-limited: Credentials expire after scan completion
- Audit: All AI data access logged

#### 5. Data Access Policy Enforcement Architecture

**Dynamic Access Control**:
- **Attribute-Based Access Control (ABAC)**: Access decisions based on attributes
  - Attributes: User role, data sensitivity, purpose, location, time
  - Example: "Allow HR manager to access PII in HR database during business hours from corporate network for legitimate HR purposes"

- **AI-Driven Policy Enforcement**: AI enforces policies automatically
  - Monitor data access in real-time
  - Block unauthorized access
  - Alert on policy violations

**Just-in-Time Access**:
- Temporary access grants (2-hour access to sensitive database for specific task)
- Automatic revocation after time limit

#### 6. Compliance Automation Architecture

**GDPR Automation Architecture**:
- **Article 15 (Data Subject Access Request)**: AI finds all data for individual across all systems
  - Search: Full-text search + PII matching across databases, file shares, SaaS apps
  - Report Generation: Automated report in machine-readable format

- **Article 17 (Right to be Forgotten)**: AI deletes individual's data
  - Discovery: Find all instances of individual's data
  - Deletion: Automated deletion + verification
  - Timeline: ≤30 days (GDPR requirement)

**CCPA Automation Architecture**:
- Similar to GDPR but California-specific requirements
- Do Not Sell tracking: AI tracks which data can be sold vs not

**Data Retention Architecture**:
- Automated retention policy enforcement
- AI identifies data exceeding retention limits → Auto-delete or flag for review

---

### Key Success Indicators

**Outcome Metrics**:
1. **Classification Accuracy**: ≥92% accurate data classification (structured data)
2. **DLP Detection**: ≥93% detection of sensitive data exfiltration attempts
3. **False Positive Rate**: ≤8% (avoid blocking legitimate work)
4. **Privacy Compliance**: Zero GDPR/CCPA violations from AI data processing
5. **Data Discovery Coverage**: ≥80% of organizational data classified

**Process Metrics**:
1. **Scan Coverage**: ≥95% of data repositories scanned within 30 days
2. **DSAR Fulfillment**: Data subject requests fulfilled within ≤7 days (vs 30-day legal limit)
3. **Retention Enforcement**: ≥90% of data within retention limits

---

## Level 2: Comprehensive Architecture

### Core Objectives
1. Implement data lineage and flow tracking architecture
2. Design privacy-enhancing technologies (tokenization, encryption, anonymization)
3. Establish cross-system data correlation architecture
4. Implement proactive data risk reduction architecture
5. Design advanced compliance automation (multi-jurisdiction)

### Key Activities

#### 1. Data Lineage Architecture

**Automated Lineage Discovery**:
- Track data flow: Source → Processing → Storage → Consumption
- Methods: Query log analysis, application monitoring, network traffic analysis

**Data Flow Mapping**:
- Visualize how PII flows through systems
- Identify risky flows (PII to unsecured systems, cross-border flows)

#### 2. Privacy-Enhancing Technologies

**Tokenization Architecture**:
- Replace sensitive data with tokens (reversible)
- Token vault: Secure storage for token mappings

**Format-Preserving Encryption (FPE)**:
- Encrypt while maintaining format (encrypted SSN still looks like SSN)

**Anonymization Architecture**:
- K-anonymity, L-diversity for statistical anonymization

---

## Level 3: Industry-Leading Architecture

### Core Objectives
1. Implement federated data security (analyze distributed data without centralizing)
2. Design zero-knowledge data security architecture
3. Establish blockchain-based data lineage (immutable audit trail)
4. Contribute to privacy-preserving ML research
5. Achieve autonomous data governance

### Key Activities

#### 1. Federated Data Security

**Federated Learning for Classification**:
- Train classification models across distributed data sources without moving data

#### 2. Zero-Knowledge Architecture

**Zero-Knowledge Proofs**:
- Prove data meets security policy without revealing data itself

---

## Practice Integration

**Threat Assessment (TA)**: TA identifies data security threats → SA designs defenses (classification, DLP, privacy)
**Security Requirements (SR)**: SR defines accuracy requirements → SA implements models to achieve
**Governance (GV)**: GV defines data policies → SA implements automated enforcement

---

## Conclusion

Data SA practice provides architectural guidance for AI-powered data security systems. Level 1 establishes foundational classification, DLP, and privacy-preserving processing. Level 2 adds data lineage and privacy-enhancing technologies. Level 3 achieves federated security and zero-knowledge architectures.

---

**Document Information**:
- **Practice**: Security Architecture (SA)
- **Domain**: Data
- **HAIAMM Version**: 2.1
- **Maturity Levels**: 3 (Foundational, Comprehensive, Industry-Leading)
- **Last Updated**: 2025-12-25
