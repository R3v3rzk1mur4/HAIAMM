# Implementation Review Practice – Data Domain
## HAIAMM v2.0 One-Pager

### Practice Overview

Implementation Review for Data ensures AI data security system implementations correctly classify sensitive data, prevent leakage, preserve privacy, and comply with regulations while maintaining system performance.

**Scope**: Code reviews for:
- Data classification model implementations (ML models, pattern matching, context analysis)
- DLP system implementations (real-time scanning, channel monitoring, blocking mechanisms)
- Privacy-preserving AI implementations (federated learning, differential privacy, homomorphic encryption)
- Compliance automation implementations (GDPR/CCPA rights, data retention, consent management)
- Data storage security implementations (encryption, access controls, backup systems)

**Why This Matters**: Data security systems handle the organization's most sensitive information. Implementation flaws can lead to data breaches, privacy violations, regulatory fines, and loss of customer trust. Rigorous implementation review ensures data protection systems work correctly and securely.

---

### Level 1: Foundational Implementation Review

### Core Objectives
1. Establish mandatory code review for all data security system code
2. Validate data classification accuracy and performance
3. Review DLP detection and enforcement mechanisms
4. Verify privacy-preserving implementations maintain guarantees
5. Ensure compliance automation meets regulatory requirements
6. Review data storage security and encryption implementations

### Key Activities

#### 1. Data Classification Implementation Review

**Model Code Quality**:
- [ ] Classification model architecture matches approved design
- [ ] Model accuracy meets requirements (≥90% on sensitive data types)
- [ ] Feature engineering correct (extracts relevant classification signals)
- [ ] Model versioning implemented (track classification model versions)
- [ ] Model serialization secure (encrypted model files)

**Pattern Matching Code Review**:
- [ ] Regex patterns comprehensive (covers all sensitive data types: SSN, credit cards, API keys)
- [ ] Pattern matching performance optimized (efficient regex, no catastrophic backtracking)
- [ ] Context analysis code correct (reduces false positives via context)
- [ ] Multi-language support tested (handles all target languages correctly)
- [ ] Pattern updates versioned (track pattern changes over time)

**Classification Logic Review**:
- [ ] Classification thresholds appropriate (confidence score thresholds validated)
- [ ] Tie-breaking logic correct (when multiple classifications possible)
- [ ] Unknown data handling (fallback behavior for unclassifiable data)
- [ ] Performance optimization (classification completes within ≤100ms per document)
- [ ] Batch classification support (efficient bulk classification for large datasets)

**Training and Retraining Code**:
- [ ] Training data collection secure (no sensitive data leakage)
- [ ] Training pipeline correct (data splitting, validation, testing)
- [ ] Retraining triggers validated (accuracy drops, new data types)
- [ ] Model evaluation metrics tracked (precision, recall, F1, by data type)
- [ ] A/B testing implementation (compare new model vs current before full rollout)

#### 2. DLP Implementation Review

**Real-Time Scanning Code**:
- [ ] Scanning performance meets latency budget (≤100ms per document)
- [ ] Asynchronous processing correct (doesn't block user operations)
- [ ] Resource limits enforced (memory limits, CPU limits per scan)
- [ ] Error handling robust (scanner crashes don't affect applications)
- [ ] Scan result caching (avoid re-scanning identical content)

**Channel Monitoring Implementation**:
- [ ] Email scanning integrated correctly (SMTP, API hooks)
- [ ] Chat scanning implemented (Slack, Teams, enterprise chat platforms)
- [ ] File upload scanning (web uploads, cloud sync, file shares)
- [ ] Clipboard monitoring (copy/paste operations)
- [ ] API monitoring (REST API requests/responses containing data)
- [ ] Cloud sync monitoring (Dropbox, Google Drive, OneDrive)
- [ ] Removable media monitoring (USB drives, external disks)

**Detection Logic Review**:
- [ ] Vector embedding similarity detection correct (semantic matching for data variants)
- [ ] Threshold tuning validated (balance detection vs false positives)
- [ ] Alert generation logic tested (proper severity assignment)
- [ ] Deduplication logic (avoid duplicate alerts for same data transfer)
- [ ] Context-aware detection (user role, destination, data sensitivity)

**Enforcement Mechanisms**:
- [ ] Blocking mechanism safe (doesn't corrupt files, graceful failure)
- [ ] Redaction code preserves document structure (redact sensitive parts, keep rest intact)
- [ ] User notification clear (explains what was blocked, why, override process)
- [ ] Quarantine mechanism secure (encrypted quarantine storage, access controls)
- [ ] Override workflow implemented (analysts can approve false positives)
- [ ] Audit logging comprehensive (all DLP actions logged for compliance)

#### 3. Privacy-Preserving AI Implementation Review

**Federated Learning Code**:
- [ ] Client-side training correct (local model training on endpoint data)
- [ ] Gradient aggregation secure (secure aggregation protocol prevents gradient inspection)
- [ ] Model distribution safe (encrypted model distribution to clients)
- [ ] Convergence validation (federated model achieves target accuracy)
- [ ] Byzantine-robust aggregation (handles malicious clients)

**Differential Privacy Implementation**:
- [ ] Noise addition correct (proper Laplace/Gaussian noise for epsilon/delta)
- [ ] Privacy budget tracking (epsilon consumption tracked, enforced)
- [ ] Query limits enforced (prevent privacy budget exhaustion)
- [ ] Composition theorem applied correctly (for multiple queries)
- [ ] Privacy guarantees validated (mathematical proof or empirical validation)

**Homomorphic Encryption Code**:
- [ ] Encryption library correct (uses vetted libraries: Microsoft SEAL, HElib)
- [ ] Encrypted computation correct (results match unencrypted computation)
- [ ] Key management secure (encryption keys protected, rotated)
- [ ] Performance acceptable (latency within acceptable bounds for use case)
- [ ] Decryption safeguards (only authorized services can decrypt)

**Secure Multi-Party Computation**:
- [ ] Protocol implementation correct (follows established SMPC protocols)
- [ ] Party communication secure (encrypted, authenticated)
- [ ] Input validation (reject malformed inputs)
- [ ] Output validation (verify computation correctness)

#### 4. Compliance Automation Implementation Review

**GDPR Implementation**:
- [ ] Data subject access request (SAR) code correct (retrieves all user data)
- [ ] Data deletion code complete (deletes from all systems: databases, backups, logs, caches)
- [ ] Data portability code correct (exports data in machine-readable format)
- [ ] Consent management code validates consent before processing
- [ ] Right to rectification implemented (users can correct their data)
- [ ] Automated deletion after retention period (no manual intervention needed)

**CCPA Implementation**:
- [ ] Opt-out mechanism implemented (users can opt out of data sale)
- [ ] "Do Not Sell" enforcement (no data sharing when user opted out)
- [ ] Data disclosure code (provide categories of data collected)
- [ ] CCPA-specific deletion (deletion within 45 days of request)

**Data Retention Implementation**:
- [ ] Retention policies enforced in code (hard-coded retention periods)
- [ ] Automated deletion triggers (scheduled jobs, event-driven deletion)
- [ ] Deletion verification (confirm data actually deleted, not just marked)
- [ ] Legal hold support (prevent deletion when legal hold active)
- [ ] Retention policy exceptions (handle exceptions with approval workflow)

**Cross-Border Transfer Controls**:
- [ ] Data residency enforcement (data never leaves permitted regions)
- [ ] Transfer logging (log all cross-border data movements)
- [ ] Standard contractual clauses (SCC) validation (verify SCC in place before transfer)
- [ ] Transfer impact assessment (automated assessment of transfer risk)

#### 5. Data Storage Security Implementation Review

**Database Security Code**:
- [ ] Connection security (TLS for all database connections)
- [ ] Credential management (no hardcoded credentials, use secrets manager)
- [ ] SQL injection prevention (parameterized queries, ORM, input validation)
- [ ] Access control enforcement (RBAC enforced at application layer)
- [ ] Encryption at rest enabled (TDE, column-level encryption for sensitive fields)
- [ ] Query logging (log queries accessing sensitive data)

**Object Storage Security**:
- [ ] Bucket ACL enforcement (no public buckets, enforce private access)
- [ ] Encryption enforcement (reject unencrypted uploads)
- [ ] Versioning enabled (protect against accidental deletion)
- [ ] Lifecycle policies (auto-delete old data per retention policy)
- [ ] Access logging (S3 access logs, Azure Storage Analytics)
- [ ] Pre-signed URL security (short expiration, least privilege)

**Encryption Implementation**:
- [ ] Encryption algorithm approved (AES-256, ChaCha20-Poly1305)
- [ ] Key management secure (keys in KMS, not in code)
- [ ] Key rotation implemented (automated annual rotation)
- [ ] Initialization vectors (IVs) unique and random
- [ ] Authenticated encryption (GCM mode, not ECB)
- [ ] Crypto library usage correct (uses vetted libraries, not custom crypto)

**Backup Security Code**:
- [ ] Backup encryption (backups encrypted before storage)
- [ ] Backup access control (separate permissions for backup vs production)
- [ ] Backup testing code (automated restore tests)
- [ ] Immutable backups (object lock prevents deletion/modification)
- [ ] Backup retention enforcement (auto-delete old backups)

#### 6. Test Coverage Review

**Unit Test Coverage**:
- [ ] Classification model tests (test accuracy on diverse datasets)
- [ ] DLP detection tests (test on known sensitive data, known benign data)
- [ ] Privacy mechanism tests (validate differential privacy, encryption correctness)
- [ ] Compliance automation tests (test GDPR/CCPA workflows)
- [ ] Coverage metrics: ≥80% code coverage for critical paths

**Integration Test Coverage**:
- [ ] End-to-end DLP tests (data scanned, classified, blocked/allowed)
- [ ] Channel integration tests (test all DLP channels: email, chat, upload)
- [ ] Database integration tests (CRUD operations with encryption)
- [ ] Compliance workflow tests (SAR, deletion, portability end-to-end)

**Performance Test Coverage**:
- [ ] Classification latency tests (≤100ms per document)
- [ ] DLP scanning throughput tests (≥10,000 documents/hour)
- [ ] Database query performance tests (≤100ms for typical queries)
- [ ] Scalability tests (performance with millions of documents)

**Security Test Coverage**:
- [ ] Adversarial evasion tests (attempt to evade classification)
- [ ] Privacy attack tests (membership inference, model inversion)
- [ ] Injection vulnerability tests (SQL injection, XSS in data fields)
- [ ] Access control tests (verify unauthorized access blocked)

#### 7. Automated Code Analysis

**Static Analysis**:
- [ ] SAST for data handling code (Bandit, Semgrep, CodeQL)
- [ ] Hardcoded secret detection (TruffleHog, git-secrets)
- [ ] Dependency vulnerability scanning (Snyk, Safety)
- [ ] Code quality metrics (complexity ≤15, duplication ≤5%)

**Security Scanning**:
- [ ] Sensitive data in logs (scan for accidental PII logging)
- [ ] Insecure encryption usage (weak algorithms, ECB mode)
- [ ] Missing input validation (unsanitized user input)
- [ ] Excessive permissions (overly broad database/storage access)

---

### Key Success Indicators

**Outcome Metrics**:
1. **Classification Accuracy**: ≥90% accuracy maintained in production
2. **DLP Effectiveness**: ≥85% exfiltration attempts blocked, ≤5% false positive rate
3. **Privacy Compliance**: Zero privacy violations, differential privacy guarantees verified
4. **Regulatory Compliance**: 100% GDPR/CCPA requirements implemented correctly

**Process Metrics**:
1. **Review Coverage**: 100% of data security code reviewed before merge
2. **Review Quality**: ≥5 substantive comments per 100 lines of code
3. **Defect Detection**: ≥80% of bugs caught in code review (before production)
4. **Review Turnaround**: ≥95% of reviews completed within 2 business days

**Technical Metrics**:
1. **Test Coverage**: ≥80% unit test coverage for classification, DLP, privacy code
2. **Performance**: Classification ≤100ms, DLP scanning ≥10,000 docs/hour
3. **Security**: Zero hardcoded secrets, 100% SQL injection prevention
4. **Encryption**: 100% sensitive data encrypted at rest and in transit

---

## Level 2: Comprehensive Implementation Review

### Core Objectives
1. Implement AI-specific code review for Human Assisted Intelligence systems (prompt injection prevention, model security)
2. Establish privacy impact assessment (PIA) during code review
3. Conduct dedicated compliance code review (GDPR/CCPA/HIPAA expert validation)
4. Implement performance profiling before production deployment
5. Conduct adversarial review and privacy attack simulations
6. Establish automated security scanning with AI-specific rules (SEMGREP for prompt injection)

### Key Activities

#### 1. AI-Specific Code Review for Human Assisted Intelligence

**Prompt Injection Prevention Code Review** (for LLM-based AI data security tools):

**SEMGREP Rules for Prompt Injection Detection**:

```yaml
# semgrep-rules/prompt-injection-data-security.yaml

rules:
  - id: direct-user-input-in-llm-prompt
    pattern: |
      prompt = f"Classify this data: {$USER_INPUT}"
    message: "Direct user input in LLM prompt creates prompt injection risk. Use structured prompts with clear system/user separation."
    severity: ERROR
    languages: [python]

  - id: unsanitized-data-in-classification-prompt
    pattern: |
      llm.classify($DATA)
    message: "Data passed to LLM classification without sanitization. Validate/sanitize data before LLM processing to prevent prompt injection."
    severity: WARNING
    languages: [python]

  - id: no-prompt-delimiter
    pattern: |
      prompt = f"{system_instructions}{user_data}"
    message: "No delimiter between system instructions and user data. Use structured format: {'system': '...', 'user': '...'} or XML tags."
    severity: ERROR
    languages: [python]

  - id: credentials-in-system-prompt
    pattern-either:
      - pattern: |
          system_prompt = "... $API_KEY ..."
      - pattern: |
          system_prompt = "... $PASSWORD ..."
      - pattern: |
          system_prompt = "... classification_rules = ... PII ..."
    message: "Credentials or sensitive classification rules in system prompt risk leakage via prompt injection. Externalize secrets."
    severity: CRITICAL
    languages: [python]
```

**Manual Code Review Checklist for Prompt Injection**:
- [ ] **Prompt Construction Review**:
  - [ ] User input sanitized before inclusion in prompts (remove instruction-like text: "ignore previous", "classify as", etc.)
  - [ ] System prompts and user prompts separated via structural delimiters (JSON: `{"system": "...", "user": "..."}` or XML: `<system>...</system><user>...</user>`)
  - [ ] No credentials, API keys, or PII in system prompts (exfiltration risk via prompt injection)
  - [ ] No sensitive classification rules in system prompts (rule leakage enables evasion)
- [ ] **Input Validation for LLM Processing**:
  - [ ] Data content validated before LLM processing (detect malicious instructions, encoded attacks)
  - [ ] Document metadata sanitized (PDF metadata, EXIF data can contain prompt injection payloads)
  - [ ] File type validation (reject unexpected file types that may contain malicious prompts)
- [ ] **Output Validation**:
  - [ ] LLM classification outputs validated before applying data access decisions (never auto-grant access based solely on LLM output)
  - [ ] Anomaly detection for LLM outputs (detect manipulation: all data classified as "public" suddenly)
  - [ ] Classification confidence thresholds enforced (low confidence → human review, not auto-apply)
- [ ] **RAG Document Security** (if using Retrieval-Augmented Generation for compliance guidance):
  - [ ] RAG documents validated before ingestion into knowledge base (prevent poisoned compliance documents: fake GDPR guidance)
  - [ ] RAG document access controls (only authorized sources can add compliance guidance)
  - [ ] RAG document versioning (track changes to compliance guidance)
- [ ] **DSAR Automation Security** (if using LLMs for Data Subject Access Request automation):
  - [ ] Human review required for DSAR responses containing PII, financial data, or >100 records (prevent prompt injection from exfiltrating data via DSAR abuse)
  - [ ] DSAR request validation (detect malicious requests attempting to extract all data)

**Model Security Code Review**:
- [ ] Model serving security:
  - [ ] API rate limiting (prevent abuse, model extraction attacks)
  - [ ] Authentication/authorization (only authorized systems can query classification model)
  - [ ] Model versioning (track which model version made each decision)
  - [ ] Model rollback capability (quickly revert to previous version if issues detected)
- [ ] Model privacy protection:
  - [ ] Differential privacy implementation validated (ε budget enforced, noise addition correct)
  - [ ] Model outputs limited (prevent excessive information leakage enabling model inversion)
  - [ ] Query logging (log all model queries for abuse detection)

#### 2. Privacy Impact Assessment (PIA) During Code Review

**Privacy-by-Design Code Review**:
- [ ] Data minimization validated in code:
  - [ ] Code only collects data necessary for stated purpose (no excessive data collection)
  - [ ] Code only accesses data required for operation (AI service accounts have least privilege: read-only, scoped, time-limited)
  - [ ] Code deletes data when no longer needed (retention enforcement, automated deletion)
- [ ] Purpose limitation validated:
  - [ ] Code only uses data for stated security purpose (no repurposing for analytics, marketing)
  - [ ] Code enforces purpose-based access control (data tagged with purpose, access granted only for compatible purposes)

**Privacy Controls Code Review**:
- [ ] Consent management code validated:
  - [ ] Code checks consent before processing personal data
  - [ ] Code respects consent withdrawals (stop processing, delete data within required timeframe)
  - [ ] Code links data to consent records (audit trail)
- [ ] Data subject rights code validated:
  - [ ] GDPR Article 15 (Access): Code retrieves all instances of individual's data (≥95% recall per SR-Data)
  - [ ] GDPR Article 17 (Deletion): Code deletes all instances across all systems (≥95% recall, ≥99% verification per SR-Data)
  - [ ] Code implements soft-delete with quarantine (≥30 days before hard delete per SR-Data safety guardrail)
  - [ ] Code checks legal holds before deletion (prevent deletion when legal hold active)

**Data Processing Agreement (DPA) Compliance**:
- [ ] If using third-party AI/ML services (cloud APIs):
  - [ ] Code verifies DPA in place before sending data to vendor API
  - [ ] Code enforces data residency (sensitive data doesn't leave approved jurisdictions)
  - [ ] Code validates vendor sub-processors (no data to unapproved sub-processors)
  - [ ] Code implements data portability (can export data from vendor if switching providers)

#### 3. Compliance Code Review (Dedicated Expert Validation)

**GDPR Compliance Expert Review**:
- [ ] Legal basis validation:
  - [ ] Code documents legal basis for each processing activity (GDPR Article 6: legitimate interest, legal obligation, consent)
  - [ ] If using "legitimate interest": Code demonstrates balancing of interests (organization's security need vs data subject's privacy rights)
  - [ ] If using "consent": Code implements valid consent (freely given, specific, informed, unambiguous, withdrawable)
- [ ] Special category data handling (GDPR Article 9):
  - [ ] Code identifies special category data (racial origin, political opinions, religious beliefs, health data, biometric data, sex life)
  - [ ] Code applies additional safeguards for special category data (higher accuracy ≥98% per SR-Data, explicit consent or legal basis)
- [ ] Automated decision-making (GDPR Article 22):
  - [ ] Code identifies automated decisions with significant effect (AI auto-deletes data, AI blocks access)
  - [ ] Code implements right to human review (users can request human decision-maker review AI decision)
  - [ ] Code provides meaningful information about decision logic (explainability)

**CCPA Compliance Expert Review**:
- [ ] Consumer rights implementation:
  - [ ] Code implements right to know (disclose categories of personal information collected)
  - [ ] Code implements right to delete (delete consumer's personal information within 45 days)
  - [ ] Code implements right to opt-out (stop selling personal information)
  - [ ] Code implements right to non-discrimination (equal service despite exercising rights)
- [ ] "Sale" definition compliance:
  - [ ] Code identifies data sharing that constitutes "sale" under CCPA (valuable consideration exchanged)
  - [ ] Code implements do-not-sell enforcement (respect opt-outs)

**HIPAA Compliance Expert Review** (if applicable):
- [ ] PHI handling validation:
  - [ ] Code identifies Protected Health Information (18 HIPAA identifiers)
  - [ ] Code applies HIPAA safeguards: Access controls, encryption, audit logging
  - [ ] Code implements minimum necessary access (users only access PHI required for job function)
  - [ ] Code generates audit logs for all PHI access (user, timestamp, data accessed, purpose)
- [ ] Business Associate Agreement (BAA) compliance:
  - [ ] If AI vendor processes PHI: Code verifies BAA in place before sending PHI to vendor
  - [ ] Code implements breach notification (detect unauthorized PHI access, notify within HIPAA timeline)

**PCI-DSS Compliance Expert Review** (if applicable):
- [ ] Cardholder data handling:
  - [ ] Code detects cardholder data with ≥99% accuracy (per SR-Data)
  - [ ] Code enforces Cardholder Data Environment (CDE) boundaries (prevent cardholder data outside CDE)
  - [ ] Code implements PCI retention limits (detect cardholder data >90 days post-transaction, flag for deletion/justification)
  - [ ] Code prevents storage of sensitive authentication data (CVV, PIN, full magnetic stripe)

#### 4. Performance Profiling Before Production

**Classification Performance Profiling**:
- [ ] Profile classification on production-like dataset:
  - [ ] Measure latency: p50, p95, p99 (validate ≤500ms for real-time DLP per SR-Data)
  - [ ] Measure throughput: documents classified per hour (validate ≥1 TB/hour per SA-Data)
  - [ ] Identify bottlenecks: Model inference, database lookups, network calls
  - [ ] Optimize hot paths: Cache frequently classified patterns, batch processing
- [ ] Profile classification accuracy on diverse dataset:
  - [ ] Test on data types: Structured (databases), unstructured (documents), multi-modal (images)
  - [ ] Validate accuracy: ≥92% structured, ≥88% unstructured per SR-Data Level 1
  - [ ] Identify accuracy gaps: Which data types underperform? Which false negatives critical?

**DLP Performance Profiling**:
- [ ] Profile DLP scanning:
  - [ ] Measure latency: Email DLP ≤200ms, file upload ≤500ms per SR-Data
  - [ ] Measure throughput: Support ≥5,000 concurrent users per SR-Data
  - [ ] Test under load: Performance degrades gracefully (queue, prioritize, don't crash)
- [ ] Profile DLP detection accuracy:
  - [ ] Test detection rate on known exfiltration attempts (target ≥85% detection per SR-Data Level 1)
  - [ ] Test false positive rate (target ≤8% Level 1, ≤5% Level 2 per SR-Data)

**DSAR Performance Profiling**:
- [ ] Profile Data Subject Access Request fulfillment:
  - [ ] Measure search time: Can code locate individual's data across all systems within ≤48 hours per SR-Data?
  - [ ] Measure accuracy: ≥95% recall (find 95% of individual's data)
  - [ ] Optimize search: Parallel searches across data sources, indexed queries

#### 5. Adversarial Review and Privacy Attack Simulations

**Adversarial Code Review**:
- [ ] Red team reviews privacy-preserving implementations:
  - [ ] Attempt to bypass differential privacy (query manipulation, composition attacks)
  - [ ] Attempt model inversion (reconstruct training data from model outputs)
  - [ ] Attempt membership inference (determine if specific data was in training set)
  - [ ] Attempt prompt injection (manipulate LLM-based classification/DLP)
  - [ ] Attempt classification poisoning (corrupt training data via feedback loop)

**Privacy Attack Testing**:
- [ ] Membership inference attack test:
  - [ ] Given known data sample, attempt to determine if it was in training data
  - [ ] Success criteria: ≤55% accuracy (barely better than random = 50% per SR-Data Level 2)
  - [ ] If >55%: Strengthen differential privacy (reduce ε), add regularization
- [ ] Model inversion attack test:
  - [ ] Attempt to reconstruct PII from classification model via repeated queries
  - [ ] Success criteria: ≤0.1% success rate in extracting identifiable PII (per SR-Data Level 1)
  - [ ] If >0.1%: Strengthen differential privacy, limit model output detail, API rate limiting

**Chaos Testing for Data Systems**:
- [ ] Inject failures into data security systems:
  - [ ] Database unavailable: Verify graceful degradation (fallback to pattern matching, queue classification requests)
  - [ ] DLP service crash: Verify fail-safe behavior (block by default if configured, or alert-only with logging)
  - [ ] Model serving failure: Verify rollback to previous model version or rule-based classification
  - [ ] Cross-border transfer restriction: Verify code blocks transfer when mechanism (SCC, adequacy decision) unavailable

#### 6. Automated Security Scanning with AI-Specific Rules

**SAST with AI Data Security Rules**:
- [ ] Run SEMGREP with prompt injection detection rules (see rules above)
- [ ] Run Bandit for Python data handling security:
  - Hardcoded secrets in classification/DLP code
  - SQL injection vulnerabilities in data access code
  - Insecure encryption (weak algorithms, ECB mode)
- [ ] Run CodeQL for data flow analysis:
  - Track sensitive data flows (PII from database → logs = violation)
  - Detect data exfiltration paths (PII → external API without DLP check)

**Sensitive Data in Code Detection**:
- [ ] Scan code for accidental PII logging:
  - Use regex to detect PII patterns in log statements
  - Flag: `logger.info(f"Processing user {ssn}")` ← SSN in logs
- [ ] Scan code for hardcoded test data:
  - Detect real-looking PII in test fixtures, example data
  - Require: Use synthetic/anonymized test data only

**Dependency Vulnerability Scanning**:
- [ ] Scan AI/ML dependencies for vulnerabilities:
  - TensorFlow, PyTorch, scikit-learn vulnerabilities (CVE database)
  - Privacy libraries: Differential privacy libraries, encryption libraries
  - DLP libraries: Pattern matching, NLP libraries
- [ ] Scan compliance dependencies:
  - GDPR/CCPA automation libraries
  - Data retention enforcement libraries

---

### Key Success Indicators (Level 2)

**Outcome Metrics**:
1. **Prompt Injection Prevention**: Zero prompt injection vulnerabilities detected in production (SEMGREP rules + manual review catch all instances)
2. **Privacy Attack Resistance**: ≤55% membership inference accuracy, ≤0.1% model inversion success (privacy guarantees validated)
3. **Compliance Validation**: 100% of GDPR/CCPA/HIPAA code reviewed by compliance expert before production
4. **Performance Validation**: 100% of code performance-profiled, meets latency/throughput requirements

**Process Metrics**:
1. **AI-Specific Review Coverage**: 100% of LLM-based code reviewed for prompt injection (SEMGREP + manual checklist)
2. **Privacy Impact Assessment**: 100% of code processing personal data has PIA during review
3. **Adversarial Testing**: Quarterly red team review of privacy-preserving implementations
4. **Automated Scanning**: 100% of code scanned with AI-specific SAST rules before merge

---

## Level 3: Industry-Leading Implementation Review

### Core Objectives
1. Implement formal verification of critical privacy properties (mathematical proofs of differential privacy, k-anonymity)
2. Deploy AI-assisted code review for data security and privacy code
3. Achieve continuous quality optimization with quantified implementation review ROI
4. Contribute privacy-preserving implementation patterns to open-source community
5. Receive industry recognition for privacy engineering excellence

### Key Activities

#### 1. Formal Verification of Privacy Properties

**Differential Privacy Formal Verification**:
- [ ] Mathematical proof that code implements differential privacy correctly:
  - Prove: Noise addition mechanism satisfies ε-differential privacy for specified ε
  - Prove: Privacy budget tracking correctly prevents budget exhaustion
  - Prove: Composition theorem applied correctly for multiple queries
  - Tools: Use theorem provers (Coq, Isabelle) or formal verification frameworks (EasyCrypt for differential privacy)
- [ ] Automated verification of privacy budgets:
  - Static analysis tool tracks ε consumption across code paths
  - Verify: No code path exceeds privacy budget
  - Alerting: Flag code changes that increase ε beyond threshold

**K-Anonymity Formal Verification**:
- [ ] Prove anonymization algorithm achieves k-anonymity for all input datasets:
  - Prove: Every record is indistinguishable from at least k-1 others
  - Prove: L-diversity satisfied (diverse sensitive attributes within k-anonymous groups)
  - Prove: T-closeness satisfied (sensitive attribute distribution in group close to overall distribution)
- [ ] Automated k-anonymity validation:
  - Test anonymization code on diverse datasets (synthetic data with known properties)
  - Verify: k ≥ specified threshold for all records
  - Coverage: ≥5 critical privacy properties formally verified per SR-Data Level 3

**Data Deletion Completeness Proof**:
- [ ] Prove deletion algorithm deletes all instances of data:
  - Prove: Deletion workflow visits all data stores (databases, caches, logs, backups, archives)
  - Prove: Deletion eventually completes within 30 days (liveness property)
  - Prove: Deleted data cannot be reconstructed from remaining data
- [ ] Model checking for deletion workflow:
  - Model deletion workflow as state machine
  - Use model checker (TLA+, Alloy) to verify all states eventually reach "deletion complete"
  - Verify: No states where data partially deleted (atomicity)

**Access Control Formal Verification**:
- [ ] Prove access control logic prevents unauthorized data access:
  - Prove: AI service accounts never have write access to production data (safety property)
  - Prove: Data access granted only when user has appropriate role AND purpose (authorization correctness)
  - Prove: Time-limited credentials expire correctly (temporal properties)
- [ ] Information flow analysis:
  - Prove: PII never flows to unauthorized destinations (logs, external APIs) without DLP check
  - Tools: Use information flow type systems or taint analysis

#### 2. AI-Assisted Code Review for Data Security

**AI Code Review Assistant Deployment**:
- [ ] AI tool analyzes data security code and suggests improvements:
  - Input: Pull request diff, code context, historical vulnerability patterns
  - AI Analysis:
    - Detect common data security bugs (PII in logs, weak encryption, SQL injection, prompt injection)
    - Suggest privacy improvements (add differential privacy, reduce data access scope, implement soft-delete)
    - Identify performance issues (inefficient classification, database query optimization)
    - Flag compliance gaps (missing GDPR consent check, no audit logging)
  - Output: Prioritized suggestions with severity, remediation guidance, code examples
- [ ] AI learning from historical code reviews:
  - Past code review findings → training data for AI
  - AI learns organization-specific patterns (common vulnerabilities, coding conventions)
  - AI accuracy improves over time (fewer false positives, more relevant suggestions)
- [ ] Human-AI collaboration:
  - AI provides preliminary review (catches common issues instantly)
  - Human reviewers focus on complex issues (business logic, regulatory interpretation, design decisions)
  - Result: ≥30% faster code reviews (per SR-Data Level 3 target), ≥90% defect detection (up from ≥80% Level 1)

**AI-Powered Privacy Analysis**:
- [ ] AI identifies privacy risks in data handling code:
  - Data minimization opportunities: "This code collects 20 user fields but only uses 5. Consider removing unnecessary fields."
  - Purpose limitation violations: "This marketing code accesses customer data collected for order fulfillment. Violates purpose limitation."
  - Retention policy gaps: "This data has no retention policy. Add auto-deletion after X days."
  - Cross-border flow risks: "This API call sends EU citizen data to US server. Verify Standard Contractual Clauses in place."

**Automated Security Pattern Recognition**:
- [ ] AI recognizes secure coding patterns and anti-patterns:
  - Secure patterns: "Code uses parameterized queries (good - SQL injection prevention)"
  - Anti-patterns: "Code uses ECB encryption mode (bad - use GCM for authenticated encryption)"
  - AI suggests pattern-based improvements: "Replace custom crypto with vetted library (libsodium, cryptography.io)"

#### 3. Continuous Quality Optimization with Quantified ROI

**Implementation Review Metrics Dashboard**:
- [ ] Real-time dashboard tracking code review effectiveness:
  - Metrics: Review turnaround time, defects found per 100 LOC, defect escape rate (bugs found in production), review quality score
  - Trends: Improving over time (faster reviews, higher defect detection, fewer escapes)
- [ ] Automated alerts when metrics degrade:
  - Alert: Review turnaround time >2 business days → notify team lead
  - Alert: Defect escape rate increases >10% week-over-week → investigate root cause

**Root Cause Analysis for Escaped Defects**:
- [ ] For defects that escape code review and reach production:
  - RCA process: Why did code review miss this bug?
  - Checklist update: Add item to code review checklist to catch this class of bug
  - AI assistant retraining: Include bug pattern in AI training data
  - Reviewer training: Share escaped defect in team learning session
- [ ] Continuous improvement cycle:
  - Quarterly code review retrospectives: What's working? What needs improvement?
  - Checklist evolution: Add new items for emerging threats (prompt injection, new privacy regulations)
  - Process optimization: Streamline reviews, reduce toil, improve reviewer experience

**Implementation Review ROI Quantification**:
- [ ] **Defect Prevention Cost Savings**:
  - Cost to fix in code review: 1x
  - Cost to fix in production: 10x-100x (data breach = massive cost)
  - Calculation: (Code review defects found) × (Average cost to fix in production - Cost in review) = Savings
  - Example: 200 defects found in review × (10x multiplier × $500 avg fix cost) = $1M savings
- [ ] **Privacy Incident Avoidance**:
  - Historical privacy incidents: GDPR fines, CCPA penalties, breach costs, customer lawsuits
  - Code review prevented incidents: Prompt injection caught before production, PII logging prevented, unauthorized data access blocked
  - Quantified: ≥$X million in potential fines/lawsuits prevented per year
- [ ] **Compliance Audit Performance**:
  - Faster audit evidence production: Code review records provide audit trail (≤24 hours to produce evidence per SR-Data Level 3)
  - Fewer audit findings: ≥60% reduction in privacy/security audit findings (per SR-Data Level 3)
  - Regulatory recognition: Positive regulator feedback on code review rigor
- [ ] **Overall ROI**:
  - Total cost: Reviewer time (hours × fully-loaded rate), AI tools, training, formal verification tools
  - Total savings: Defect prevention + privacy incidents avoided + compliance improvements + faster time-to-market (less rework)
  - Target: Implementation review ROI ≥3:1 (benefits exceed costs by 3x, per SR-Data Level 3)

#### 4. Open-Source Contribution and Industry Leadership

**Open-Source Privacy-Preserving Implementation Patterns**:
- [ ] Publish reusable privacy code patterns:
  - Differential privacy implementation patterns (Python, Java, Go)
  - Data anonymization utilities (k-anonymity, l-diversity algorithms)
  - Secure data deletion libraries (multi-store deletion, verification)
  - GDPR/CCPA automation frameworks (DSAR fulfillment, deletion workflows)
  - Prompt injection prevention libraries (input sanitization, output validation)
- [ ] Open-source licensing: Apache 2.0, MIT, or Creative Commons for documentation
- [ ] Impact: ≥100 GitHub stars or active community adoption, used by ≥5 external organizations

**Privacy Engineering Tools Development**:
- [ ] Publish open-source privacy engineering tools:
  - SEMGREP rules for privacy violations (PII in logs, weak encryption, prompt injection)
  - CodeQL queries for data flow analysis (PII → unauthorized destinations)
  - Differential privacy testing framework (validate ε guarantees)
  - K-anonymity validation tool (verify anonymization correctness)
- [ ] Tool documentation: Comprehensive guides, examples, integration with CI/CD
- [ ] Community engagement: Respond to issues, accept pull requests, maintain actively

**Standards Participation and Contribution**:
- [ ] Active participation in privacy engineering standards:
  - ISO 27701 (Privacy Information Management System)
  - NIST Privacy Framework
  - OWASP AI Security & Privacy
  - IEEE Privacy Engineering standards
  - W3C Privacy Interest Group
- [ ] Contribution: ≥2 standards working groups, regular meeting participation, draft contributions
- [ ] Thought leadership: Present privacy engineering best practices at standards meetings, influence future standards

**Conference Presentations and Publications**:
- [ ] Present privacy engineering implementation patterns at conferences:
  - Target: ≥2 external presentations per year
  - Conferences: IAPP Global Privacy Summit, RSA Conference, USENIX Security, Black Hat, DEF CON Privacy Village
  - Topics: Formal verification of differential privacy, prompt injection prevention, GDPR automation, privacy-preserving ML
- [ ] Publish whitepapers and blog posts:
  - Topics: Implementation review ROI for privacy code, privacy attack testing, code review for GDPR compliance
  - Target: ≥4 publications per year
  - Audience: Privacy engineers, security engineers, compliance professionals

#### 5. Industry Recognition for Privacy Engineering Excellence

**Awards and Recognition**:
- [ ] Industry awards for privacy engineering excellence:
  - IAPP Privacy Innovation Award
  - CSA Cloud Security Innovation Award
  - AI ethics and privacy awards
  - Demonstrates thought leadership and best-in-class implementation practices

**Regulatory Recognition**:
- [ ] Positive feedback from privacy regulators during audits:
  - Example: Supervisory authority commends implementation review rigor, cites as best practice exemplar
  - Example: Regulator references organization's open-source privacy tools in guidance documents
  - No regulatory fines or enforcement actions (code review prevents violations)

**Academic Collaboration**:
- [ ] Research partnerships with universities on privacy engineering:
  - Topics: Formal verification of privacy properties, automated privacy testing, privacy-preserving ML implementation
  - Output: Joint research publications (≥1 per year), guest lectures, curriculum development
- [ ] Student programs: Internships focused on privacy engineering, mentorship for privacy researchers

**Customer and Partner Recognition**:
- [ ] Customer testimonials about privacy engineering excellence:
  - Examples: "Superior data protection gave us confidence to share sensitive data", "Privacy engineering maturity enabled partnership"
  - Quantified: Contracts won due to privacy program maturity (≥$X million ARR), premium pricing for privacy leadership
- [ ] Industry peer recognition:
  - Invited to speak at peer companies about privacy engineering practices
  - Other organizations adopt published tools/patterns
  - Privacy engineering community leadership (mentorship, knowledge sharing)

**Certification and Compliance Excellence**:
- [ ] ISO 27701 certification (Privacy Information Management System)
- [ ] SOC 2 Type II with privacy trust service criteria
- [ ] Privacy engineering maturity recognized in RFP responses (competitive advantage)

---

### Key Success Indicators (Level 3)

**Outcome Metrics**:
1. **Formal Verification Coverage**: ≥5 critical privacy properties formally verified (differential privacy, k-anonymity, access control, data deletion)
2. **AI-Assisted Review Effectiveness**: ≥30% faster reviews, ≥90% defect detection (up from ≥80% Level 1)
3. **Implementation Review ROI**: ≥3:1 ROI (benefits exceed costs by 3x through defect prevention, incident avoidance, compliance improvements)
4. **Open-Source Impact**: ≥100 GitHub stars, privacy tools/patterns used by ≥5 external organizations
5. **Industry Recognition**: ≥1 significant award or industry recognition for privacy engineering excellence

**Process Metrics**:
1. **Automated Privacy Analysis**: 100% of code automatically analyzed for privacy risks (AI-assisted review)
2. **Escaped Defect Rate**: ≤5% of privacy/security bugs escape code review to production (down from ≤20% baseline)
3. **Audit Performance**: ≥60% reduction in privacy/security audit findings, ≤24 hours to produce audit evidence
4. **Continuous Improvement**: Code review quality metrics improve year-over-year (faster, more effective, higher satisfaction)

**Technical Metrics**:
1. **Privacy Guarantees Validated**: 100% of differential privacy implementations formally verified (mathematical proof or empirical validation)
2. **Test Coverage**: ≥90% unit test coverage for privacy-critical code (up from ≥80% Level 1)
3. **Static Analysis**: Zero high-severity SAST findings in production code (all caught in review)

---

## Practice Integration

**Design Review (DR)**: IR validates data security designs correctly implemented
**Security Testing (ST)**: ST validates classification accuracy, DLP effectiveness
**Issue Management (IM)**: IR catches vulnerabilities VM would later detect
**Environment Hardening (EH)**: IR reviews data storage hardening implementation
**Monitoring & Logging (ML)**: IR reviews data access logging implementation

---

## Conclusion

Implementation Review for Data ensures AI data security systems correctly classify data, prevent leakage, preserve privacy, and comply with regulations. Level 1 establishes comprehensive code review covering classification models, DLP enforcement, privacy-preserving AI, compliance automation, and data storage security. Level 2 adds privacy impact assessments and adversarial reviews. Level 3 achieves formal verification and research leadership in privacy engineering.

---

**Document Information**:
- **Practice**: Implementation Review (IR)
- **Domain**: Data
- **HAIAMM Version**: 2.0
- **Maturity Levels**: 3 (Foundational, Comprehensive, Industry-Leading)
- **Last Updated**: 2025-12-25
