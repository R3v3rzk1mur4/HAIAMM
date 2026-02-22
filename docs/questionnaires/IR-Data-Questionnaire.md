# Implementation Review (IR) - Data Domain
## HAIAMM Assessment Questionnaire v3.0

**Practice:** Implementation Review (IR)
**Domain:** Data
**Purpose:** Assess organizational maturity in reviewing AI data security system implementations for correctness, reliability, privacy preservation, and regulatory compliance
**Scoring Model:** Evidence + Outcome Metrics (see Scoring Methodology below)

---

## Instructions

- Answer each question honestly based on **current, implemented practices** (not plans or aspirations)
- Each question has two components: **Evidence** (what you did) and **Outcome Metrics** (how well it worked)
- **Scoring uses 4 tiers:** Fully Mature (1.0), Implemented (0.67), Partial (0.33), Not Implemented (0.0)
- **Answer progressively** - Complete all Level 1 questions before Level 2
- **Level progression** - Achieve ALL questions at lower level before advancing
- **Baseline first** - Record current metric values before setting targets

---

## Level 1: Comprehensive Implementation Review
**Objective:** Verify that AI data security system implementations correctly classify, protect, and comply with regulations

---

### **Question 1: Data Classification Model Review**

**Q1.1:** Have you conducted comprehensive implementation review of your data classification model code validating that the model architecture matches approved design, achieves ≥90% accuracy on sensitive data types, implements correct feature engineering, includes secure model versioning and serialization, and has validated training/retraining pipelines?

**Evidence Required:**
- [ ] Model architecture implementation matches approved design document (layers, parameters, activation functions verified)
- [ ] Model accuracy validation on diverse test dataset (≥90% accuracy on SSN, credit cards, API keys, PII, PHI)
- [ ] Feature engineering code reviewed (extracts relevant classification signals: context, patterns, metadata)
- [ ] Model versioning implemented (track classification model versions, link predictions to model version)
- [ ] Model serialization secure (encrypted model files, integrity verification, access controls)
- [ ] Training data collection reviewed (no sensitive data leakage, proper sanitization)
- [ ] Training pipeline validated (data splitting correct, no train/test contamination)
- [ ] Retraining triggers implemented (accuracy drops, new data types, drift detection)
- [ ] Model evaluation metrics tracked (precision, recall, F1 by data type, confusion matrices)
- [ ] A/B testing implementation reviewed (compare new vs current model before full rollout)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Classification accuracy (sensitive data) | ___%  | ___% | ≥90% | ☐ | |
| Model training reproducibility | ___%  | ___% | 100% | ☐ | |
| Model versioning coverage | ___%  | ___% | 100% | ☐ | |
| Feature engineering defects found | ___ bugs | ___ bugs | 0 critical bugs | ☐ | |

**Metric Collection Guidance:**
- **Classification accuracy**: Test model on labeled dataset with known sensitive data types; calculate (correct predictions / total predictions); measure monthly after retraining
- **Model training reproducibility**: Re-run training pipeline 5 times with same data/seed; measure if same model produced (checksums match); verify quarterly
- **Model versioning coverage**: Count predictions with model version tag / total predictions; query production logs; measure weekly
- **Feature engineering defects**: Code review findings + production bugs in feature extraction logic; track in issue tracker; count per release cycle

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of classification model review)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### **Question 2: Pattern Matching Implementation Review**

**Q1.2:** Have you conducted implementation review of pattern matching code validating that regex patterns comprehensively cover all sensitive data types (SSN, credit cards, API keys), pattern matching is performance-optimized (no catastrophic backtracking), context analysis code reduces false positives, and multi-language support is tested?

**Evidence Required:**
- [ ] Regex patterns comprehensive (covers SSN, credit cards, API keys, PII, international formats)
- [ ] Pattern matching performance optimized (efficient regex, no exponential backtracking, timeout mechanisms)
- [ ] Catastrophic backtracking prevention validated (regex complexity analysis, test with adversarial inputs)
- [ ] Context analysis code reviewed (reduces false positives via surrounding text analysis)
- [ ] Multi-language support tested (handles English, Spanish, French, German, Chinese, etc. correctly)
- [ ] Pattern updates versioned (track pattern changes over time, A/B test new patterns)
- [ ] False positive reduction logic validated (context-aware detection, confidence scoring)
- [ ] Pattern matching latency measured (≤100ms per document)
- [ ] Edge cases tested (partial matches, multi-line patterns, Unicode handling)
- [ ] Pattern collision detection (overlapping patterns handled correctly)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Pattern matching latency (p95) | ___ms | ___ms | ≤100ms | ☐ | |
| False positive rate | ___%  | ___% | ≤8% | ☐ | |
| Regex catastrophic backtracking incidents | ___ incidents | ___ incidents | 0 incidents | ☐ | |
| Multi-language coverage | ___% | ___% | ≥90% | ☐ | |

**Metric Collection Guidance:**
- **Pattern matching latency (p95)**: Instrument pattern matching function; measure duration for 95th percentile of documents; collect from production logs; measure daily
- **False positive rate**: Human review sample of 200 pattern matches; count false positives; calculate (false positives / total matches); measure monthly
- **Regex catastrophic backtracking incidents**: Monitor for regex timeouts or CPU spikes during pattern matching; count incidents; query monitoring system; measure weekly
- **Multi-language coverage**: Test patterns on documents in target languages; calculate (languages correctly handled / total target languages); validate quarterly

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of pattern matching review)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### **Question 3: DLP Real-Time Scanning Review**

**Q1.3:** Have you conducted implementation review of DLP real-time scanning code validating that scanning latency meets budget (≤100ms per document), asynchronous processing is correct (doesn't block user operations), resource limits are enforced, error handling is robust, and all required channels are monitored (email, chat, file upload, clipboard, API, cloud sync, USB)?

**Evidence Required:**
- [ ] Scanning performance validated (latency ≤100ms per document for real-time channels)
- [ ] Asynchronous processing reviewed (non-blocking implementation, doesn't freeze user operations)
- [ ] Resource limits enforced (memory limits, CPU limits, timeout mechanisms per scan)
- [ ] Error handling robust (scanner crashes don't affect applications, graceful degradation)
- [ ] Scan result caching implemented (avoid re-scanning identical content, cache invalidation logic)
- [ ] Channel monitoring comprehensive:
  - [ ] Email scanning integrated (SMTP hooks, API integration, inline scanning)
  - [ ] Chat scanning implemented (Slack, Teams, enterprise chat platforms)
  - [ ] File upload scanning (web uploads, cloud sync, file shares)
  - [ ] Clipboard monitoring (copy/paste operations on endpoints)
  - [ ] API monitoring (REST API requests/responses containing data)
  - [ ] Cloud sync monitoring (Dropbox, Google Drive, OneDrive)
  - [ ] Removable media monitoring (USB drives, external disks)
- [ ] Scanning accuracy validated (detection rate, false positive rate by channel)
- [ ] Performance under load tested (concurrent scans, throughput validation)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Real-time scanning latency (p95) | ___ms | ___ms | ≤100ms | ☐ | |
| DLP scanning throughput | ___ docs/hr | ___ docs/hr | ≥10,000 docs/hr | ☐ | |
| Channel monitoring coverage | ___% | ___% | 100% | ☐ | |
| Scanner crash incidents | ___ incidents/mo | ___ incidents/mo | 0 incidents/mo | ☐ | |

**Metric Collection Guidance:**
- **Real-time scanning latency (p95)**: Instrument DLP scanning function; measure time from scan request to result; calculate 95th percentile; collect from production telemetry; measure daily
- **DLP scanning throughput**: Count documents scanned per hour during peak periods; query DLP system metrics; measure weekly
- **Channel monitoring coverage**: Count monitored channels / total required channels (email, chat, upload, clipboard, API, cloud sync, USB); validate monthly
- **Scanner crash incidents**: Count DLP service crashes or unhandled exceptions; query error logs and monitoring alerts; measure monthly

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of DLP scanning review)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### **Question 4: DLP Detection & Enforcement Review**

**Q1.4:** Have you conducted implementation review of DLP detection and enforcement mechanisms validating that vector embedding similarity detection is correct, threshold tuning balances detection vs false positives, alert generation and deduplication work properly, and enforcement mechanisms (blocking, redaction, quarantine, user notification, override workflow, audit logging) are implemented safely?

**Evidence Required:**
- [ ] Vector embedding similarity detection reviewed (semantic matching for data variants, embedding model validated)
- [ ] Threshold tuning validated (balance detection rate vs false positive rate, documented rationale)
- [ ] Alert generation logic tested (proper severity assignment, alert routing, escalation)
- [ ] Deduplication logic reviewed (avoid duplicate alerts for same data transfer, collision detection)
- [ ] Context-aware detection validated (considers user role, destination, data sensitivity)
- [ ] Enforcement mechanisms reviewed:
  - [ ] Blocking mechanism safe (doesn't corrupt files, graceful failure modes)
  - [ ] Redaction preserves document structure (redact sensitive parts, keep rest intact)
  - [ ] User notification clear (explains what was blocked, why, override process)
  - [ ] Quarantine mechanism secure (encrypted quarantine storage, access controls)
  - [ ] Override workflow implemented (analysts can approve false positives, approval tracking)
  - [ ] Audit logging comprehensive (all DLP actions logged for compliance)
- [ ] Fail-safe behavior validated (what happens if DLP service unavailable)
- [ ] Performance impact measured (enforcement doesn't significantly degrade user experience)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| DLP detection rate (exfiltration attempts) | ___%  | ___% | ≥85% | ☐ | |
| DLP false positive rate | ___%  | ___% | ≤8% | ☐ | |
| Alert deduplication effectiveness | ___%  | ___% | ≥95% | ☐ | |
| Enforcement action audit coverage | ___%  | ___% | 100% | ☐ | |

**Metric Collection Guidance:**
- **DLP detection rate**: Test with simulated exfiltration attempts (known sensitive data transfers); calculate (blocked transfers / total attempts); run red team exercises quarterly
- **DLP false positive rate**: Human review sample of 200 DLP blocks; count false positives; calculate (false positives / total blocks); measure monthly
- **Alert deduplication effectiveness**: Count duplicate alerts prevented / total potential duplicates; analyze alert correlation logic; measure weekly
- **Enforcement action audit coverage**: Count enforcement actions with audit logs / total enforcement actions; query audit system; validate monthly

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of DLP enforcement review)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### **Question 5: Privacy-Preserving AI Review**

**Q1.5:** Have you conducted implementation review of privacy-preserving AI mechanisms (federated learning, differential privacy, homomorphic encryption) validating that client-side training is correct, secure gradient aggregation prevents gradient inspection, differential privacy noise addition implements proper Laplace/Gaussian noise for epsilon/delta guarantees, privacy budget tracking is enforced, and homomorphic encryption uses vetted libraries with correct key management?

**Evidence Required:**
- [ ] Federated Learning implementation reviewed (if applicable):
  - [ ] Client-side training correct (local model training on endpoint data, no data centralization)
  - [ ] Gradient aggregation secure (secure aggregation protocol prevents gradient inspection)
  - [ ] Model distribution safe (encrypted model distribution to clients)
  - [ ] Convergence validation (federated model achieves target accuracy)
  - [ ] Byzantine-robust aggregation (handles malicious clients attempting poisoning)
- [ ] Differential Privacy implementation reviewed (if applicable):
  - [ ] Noise addition correct (proper Laplace/Gaussian noise for specified epsilon/delta)
  - [ ] Privacy budget tracking (epsilon consumption tracked per user/query, enforced)
  - [ ] Query limits enforced (prevent privacy budget exhaustion)
  - [ ] Composition theorem applied correctly (for multiple queries on same data)
  - [ ] Privacy guarantees validated (mathematical proof or empirical validation)
- [ ] Homomorphic Encryption implementation reviewed (if applicable):
  - [ ] Encryption library vetted (uses Microsoft SEAL, HElib, or other established libraries)
  - [ ] Encrypted computation correctness (results match unencrypted computation)
  - [ ] Key management secure (encryption keys protected, rotated, access controlled)
  - [ ] Performance acceptable (latency within bounds for use case)
  - [ ] Decryption safeguards (only authorized services can decrypt results)
- [ ] Privacy guarantees tested (membership inference resistance, model inversion resistance)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Differential privacy epsilon budget | ε = ___ | ε = ___ | ε ≤ 1.0 | ☐ | |
| Privacy budget tracking coverage | ___%  | ___% | 100% | ☐ | |
| Federated learning convergence accuracy | ___%  | ___% | ≥85% | ☐ | |
| Homomorphic encryption correctness | ___%  | ___% | 100% | ☐ | |

**Metric Collection Guidance:**
- **Differential privacy epsilon budget**: Review privacy parameters in code; calculate total epsilon for typical query workload; validate with privacy engineer; measure per release
- **Privacy budget tracking coverage**: Count queries with budget tracking / total privacy-sensitive queries; audit code paths; validate monthly
- **Federated learning convergence accuracy**: Test federated model on holdout dataset; calculate accuracy; compare to centralized model baseline; measure after each training round
- **Homomorphic encryption correctness**: Run test suite comparing encrypted vs unencrypted computation results; calculate (matching results / total tests); validate quarterly

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of privacy-preserving AI review)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### **Question 6: Compliance Automation Review**

**Q1.6:** Have you conducted implementation review of compliance automation code validating that GDPR requirements (subject access requests, data deletion, portability, consent management, rectification, automated retention enforcement) and CCPA requirements (opt-out mechanism, do-not-sell enforcement, deletion within 45 days) are implemented correctly, data retention policies are enforced automatically, and cross-border transfer controls (residency enforcement, transfer logging) are validated?

**Evidence Required:**
- [ ] GDPR Implementation reviewed (if applicable):
  - [ ] Data Subject Access Request (SAR) code retrieves all user data across systems (databases, logs, backups, caches)
  - [ ] Data deletion code complete (deletes from all systems, verified deletion, quarantine period)
  - [ ] Data portability exports data in machine-readable format (JSON, XML)
  - [ ] Consent management validates consent before processing personal data
  - [ ] Right to rectification implemented (users can correct their data)
  - [ ] Automated deletion after retention period (no manual intervention needed)
- [ ] CCPA Implementation reviewed (if applicable):
  - [ ] Opt-out mechanism implemented (users can opt out of data sale)
  - [ ] "Do Not Sell" enforcement (no data sharing when user opted out)
  - [ ] Data disclosure provides categories of data collected
  - [ ] CCPA-specific deletion (deletion within 45 days of request)
- [ ] Data Retention Implementation reviewed:
  - [ ] Retention policies enforced in code (hard-coded retention periods, policy engine)
  - [ ] Automated deletion triggers (scheduled jobs, event-driven deletion)
  - [ ] Deletion verification (confirm data actually deleted, not just marked)
  - [ ] Legal hold support (prevent deletion when legal hold active)
- [ ] Cross-Border Transfer Controls reviewed:
  - [ ] Data residency enforcement (data never leaves permitted regions)
  - [ ] Transfer logging (log all cross-border data movements)
  - [ ] Standard Contractual Clauses (SCC) validation before transfer

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| DSAR fulfillment completeness (recall) | ___%  | ___% | ≥95% | ☐ | |
| Data deletion completeness (recall) | ___%  | ___% | ≥95% | ☐ | |
| Retention policy enforcement coverage | ___%  | ___% | 100% | ☐ | |
| Cross-border transfer violations | ___ violations | ___ violations | 0 violations | ☐ | |

**Metric Collection Guidance:**
- **DSAR fulfillment completeness**: Test DSAR code with known test user data; calculate (data instances retrieved / total known instances); run test suite quarterly
- **Data deletion completeness**: Test deletion code with known test data; verify data deleted from all systems; calculate (deleted instances / total instances); validate quarterly
- **Retention policy enforcement coverage**: Count data types with automated retention enforcement / total data types; audit code and configurations; measure monthly
- **Cross-border transfer violations**: Monitor data flows for unauthorized cross-border transfers; count violations detected; query DLP and network monitoring; measure weekly

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of compliance automation review)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### **Question 7: Data Storage Security Review**

**Q1.7:** Have you conducted implementation review of data storage security validating that database connections use TLS, credentials are not hardcoded, SQL injection prevention is comprehensive (parameterized queries), access control is enforced, encryption at rest is enabled, object storage has proper ACLs and encryption enforcement, encryption implementations use approved algorithms (AES-256, KMS key management, rotation), and backups are encrypted with automated restore testing?

**Evidence Required:**
- [ ] Database Security Code reviewed:
  - [ ] Connection security (TLS 1.2+ for all database connections)
  - [ ] Credential management (no hardcoded credentials, secrets manager integration)
  - [ ] SQL injection prevention (parameterized queries, ORM usage, input validation)
  - [ ] Access control enforcement (RBAC at application layer, least privilege)
  - [ ] Encryption at rest enabled (TDE, column-level encryption for sensitive fields)
  - [ ] Query logging (log queries accessing sensitive data for audit)
- [ ] Object Storage Security reviewed:
  - [ ] Bucket ACL enforcement (no public buckets, private access enforced)
  - [ ] Encryption enforcement (reject unencrypted uploads, enforce SSE or CSE)
  - [ ] Versioning enabled (protect against accidental deletion)
  - [ ] Lifecycle policies (auto-delete old data per retention policy)
  - [ ] Access logging enabled (S3 access logs, Azure Storage Analytics)
  - [ ] Pre-signed URL security (short expiration ≤1 hour, least privilege)
- [ ] Encryption Implementation reviewed:
  - [ ] Approved algorithms (AES-256, ChaCha20-Poly1305, not DES/3DES)
  - [ ] Key management secure (keys in KMS, not in code/config)
  - [ ] Key rotation implemented (automated annual rotation minimum)
  - [ ] Initialization vectors unique and random (no IV reuse)
  - [ ] Authenticated encryption (GCM mode, not ECB mode)
  - [ ] Crypto library usage correct (uses vetted libraries: libsodium, cryptography.io, not custom crypto)
- [ ] Backup Security reviewed:
  - [ ] Backup encryption (backups encrypted before storage)
  - [ ] Backup access control (separate permissions for backup vs production)
  - [ ] Automated restore testing (quarterly restore tests, validation)
  - [ ] Immutable backups (object lock prevents deletion/modification)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Hardcoded credentials found in code | ___ instances | ___ instances | 0 instances | ☐ | |
| SQL injection vulnerabilities | ___ vulns | ___ vulns | 0 vulns | ☐ | |
| Encryption at rest coverage | ___%  | ___% | 100% | ☐ | |
| Backup restore success rate | ___%  | ___% | ≥95% | ☐ | |

**Metric Collection Guidance:**
- **Hardcoded credentials**: Run secret scanning tools (TruffleHog, git-secrets, Semgrep); count detected instances; scan on every commit; measure weekly
- **SQL injection vulnerabilities**: Run SAST tools (Bandit, Semgrep, CodeQL) + manual code review; count vulnerable query patterns; measure per release
- **Encryption at rest coverage**: Audit data stores (databases, object storage, file systems); calculate (encrypted stores / total stores); validate quarterly
- **Backup restore success rate**: Test quarterly backup restoration; calculate (successful restores / total restore attempts); document test results

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of data storage security review)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### **Question 8: Test Coverage Review**

**Q1.8:** Have you conducted implementation review validating comprehensive test coverage including unit tests (≥80% coverage for classification, DLP, privacy mechanisms, compliance automation), integration tests (end-to-end DLP, channel integration, database operations, compliance workflows), performance tests (classification ≤100ms, DLP ≥10K docs/hr), and security tests (adversarial evasion, privacy attacks, injection vulnerabilities, access control)?

**Evidence Required:**
- [ ] Unit Test Coverage reviewed:
  - [ ] Classification model tests (accuracy on diverse datasets, edge cases)
  - [ ] DLP detection tests (known sensitive data, known benign data, boundary cases)
  - [ ] Privacy mechanism tests (differential privacy correctness, encryption correctness)
  - [ ] Compliance automation tests (GDPR/CCPA workflows, deletion completeness)
  - [ ] Code coverage ≥80% for critical paths (measured with coverage tools)
- [ ] Integration Test Coverage reviewed:
  - [ ] End-to-end DLP tests (data scanned, classified, blocked/allowed correctly)
  - [ ] Channel integration tests (all DLP channels tested: email, chat, upload, API)
  - [ ] Database integration tests (CRUD operations with encryption, access control)
  - [ ] Compliance workflow tests (SAR, deletion, portability end-to-end)
- [ ] Performance Test Coverage reviewed:
  - [ ] Classification latency tests (≤100ms per document at p95)
  - [ ] DLP scanning throughput tests (≥10,000 documents/hour)
  - [ ] Database query performance tests (≤100ms for typical queries)
  - [ ] Scalability tests (performance with millions of documents)
- [ ] Security Test Coverage reviewed:
  - [ ] Adversarial evasion tests (attempt to evade classification with obfuscation)
  - [ ] Privacy attack tests (membership inference, model inversion)
  - [ ] Injection vulnerability tests (SQL injection, XSS in data fields, prompt injection)
  - [ ] Access control tests (verify unauthorized access blocked)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Unit test code coverage | ___%  | ___% | ≥80% | ☐ | |
| Integration test coverage (critical paths) | ___%  | ___% | ≥90% | ☐ | |
| Performance test pass rate | ___%  | ___% | 100% | ☐ | |
| Security test defects found | ___ defects | ___ defects | ≥5 defects/release | ☐ | |

**Metric Collection Guidance:**
- **Unit test code coverage**: Run coverage tool (coverage.py, JaCoCo, Istanbul); measure line/branch coverage; collect from CI/CD pipeline; measure per commit
- **Integration test coverage**: Count critical user paths with integration tests / total critical paths; document in test plan; validate monthly
- **Performance test pass rate**: Run performance test suite; calculate (tests meeting SLA / total tests); measure per release; track trends
- **Security test defects found**: Count security issues discovered by security test suite; track in issue tracker; measure per release (finding defects is success)

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of test coverage review)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### **Question 9: Automated Security Scanning**

**Q1.9:** Have you implemented automated security scanning as part of implementation review including SAST tools (Bandit, Semgrep, CodeQL) for data handling code, hardcoded secret detection (TruffleHog, git-secrets), sensitive data in logs detection, and dependency vulnerability scanning for AI/ML libraries (TensorFlow, PyTorch, scikit-learn, privacy libraries)?

**Evidence Required:**
- [ ] SAST for data handling code integrated:
  - [ ] Bandit scans Python code for security issues (hardcoded credentials, SQL injection, weak crypto)
  - [ ] Semgrep with custom rules for data security patterns (PII in logs, prompt injection, insecure encryption)
  - [ ] CodeQL for data flow analysis (PII flows to unauthorized destinations)
  - [ ] Scan results integrated into PR workflow (blocking for critical findings)
- [ ] Hardcoded secret detection integrated:
  - [ ] TruffleHog scans git history for secrets
  - [ ] git-secrets prevents committing credentials
  - [ ] Pre-commit hooks enforce secret scanning
  - [ ] Regular scans of entire codebase (weekly)
- [ ] Sensitive data in logs detection:
  - [ ] Automated scanning for PII patterns in log statements
  - [ ] Code review checklist includes log statement review
  - [ ] Logging framework sanitizes sensitive data automatically
- [ ] Dependency vulnerability scanning:
  - [ ] AI/ML library vulnerabilities tracked (TensorFlow, PyTorch, scikit-learn CVEs)
  - [ ] Privacy library vulnerabilities monitored (differential privacy, encryption libraries)
  - [ ] DLP library vulnerabilities tracked (pattern matching, NLP libraries)
  - [ ] Automated dependency updates (Dependabot, Renovate)
  - [ ] Vulnerability remediation SLA (critical: ≤7 days, high: ≤30 days)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| SAST scan coverage | ___%  | ___% | 100% | ☐ | |
| Hardcoded secrets found (pre-production) | ___ secrets | ___ secrets | ≥3 secrets/quarter | ☐ | |
| Sensitive data in logs incidents | ___ incidents | ___ incidents | 0 incidents | ☐ | |
| Dependency vulnerabilities (unfixed >30 days) | ___ vulns | ___ vulns | 0 critical/high | ☐ | |

**Metric Collection Guidance:**
- **SAST scan coverage**: Count code commits scanned / total commits; query CI/CD pipeline results; measure weekly
- **Hardcoded secrets found**: Count secrets detected by scanning tools before production; track in security dashboard; measure quarterly (finding secrets is success)
- **Sensitive data in logs incidents**: Monitor production logs for PII patterns; count detection incidents; query log analysis tools; measure weekly
- **Dependency vulnerabilities unfixed**: Query vulnerability scanner; count critical/high vulnerabilities open >30 days; measure weekly; track remediation time

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of automated security scanning)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

**Level 1 Summary:**

**Questions Answered:** _____ / 9

**Level 1 Score Calculation:**
- Sum of question scores (0.0, 0.33, 0.67, or 1.0 per question): _____
- Level 1 Average: _____ / 9 = _____

**Level 1 Gate:** ☐ Passed (L1 Average ≥ 1.0) ☐ Not Passed (L1 Average < 1.0)

**Note:** You must achieve Level 1 Average ≥ 1.0 (all questions at least "Fully Mature" or compensating strength) to proceed to Level 2.

---

## Level 2: Advanced Implementation Review
**Objective:** Integrate AI-specific security review, privacy impact assessment, adversarial testing, and chaos engineering

**Prerequisites:** Level 1 Average ≥ 1.0 required to score Level 2

---

### **Question 10: AI-Specific Code Review (Prompt Injection + Model Security)**

**Q2.1:** Have you implemented AI-specific code review for Human Assisted Intelligence systems including SEMGREP rules for prompt injection detection, manual code review checklist covering prompt construction security (input sanitization, system/user prompt separation, no credentials in prompts), input/output validation, RAG document security, DSAR automation security, model serving security (rate limiting, auth, versioning, rollback), and model privacy protection (differential privacy validation, output limiting)?

**Evidence Required:**
- [ ] SEMGREP rules for prompt injection implemented and enforced in CI/CD
- [ ] Manual prompt injection review checklist used for all LLM code:
  - [ ] Prompt construction: User input sanitized, system/user prompts separated, no credentials/PII in prompts
  - [ ] Input validation: Data validated before LLM processing, metadata sanitized, file type validation
  - [ ] Output validation: LLM outputs validated before applying access decisions, anomaly detection, confidence thresholds
  - [ ] RAG security: Documents validated before ingestion, access controls, versioning
  - [ ] DSAR automation: Human review required for PII-heavy responses, request validation
- [ ] Model serving security reviewed:
  - [ ] API rate limiting prevents abuse and model extraction
  - [ ] Authentication/authorization enforced
  - [ ] Model versioning tracks which model made each decision
  - [ ] Model rollback capability tested
- [ ] Model privacy protection validated:
  - [ ] Differential privacy implementation validated (epsilon budget enforced)
  - [ ] Model output limiting prevents excessive information leakage
  - [ ] Query logging for abuse detection

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Prompt injection vulnerabilities (found in review) | ___ vulns | ___ vulns | ≥2 vulns/quarter | ☐ | |
| LLM code review coverage | ___%  | ___% | 100% | ☐ | |
| Model API abuse incidents | ___ incidents | ___ incidents | 0 incidents | ☐ | |
| Differential privacy budget violations | ___ violations | ___ violations | 0 violations | ☐ | |

**Metric Collection Guidance:**
- **Prompt injection vulnerabilities found**: Count prompt injection issues detected in code review; track in security findings; measure quarterly (finding vulnerabilities is success)
- **LLM code review coverage**: Count LLM-related PRs with prompt injection checklist / total LLM PRs; audit code review records; measure monthly
- **Model API abuse incidents**: Monitor API usage for anomalies (excessive queries, extraction attempts); count incidents; query monitoring system; measure weekly
- **Differential privacy budget violations**: Track epsilon budget consumption; count instances exceeding budget; query privacy tracking system; measure weekly

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of AI-specific code review)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### **Question 11: Privacy Impact Assessment During Code Review**

**Q2.2:** Have you integrated Privacy Impact Assessment (PIA) into the code review process validating that data minimization is implemented (code only collects/accesses/retains data necessary for stated purpose), purpose limitation is enforced (no data repurposing), consent management is validated, data subject rights (GDPR Article 15/17) are correctly implemented with ≥95% recall, and Data Processing Agreements (DPA) are verified for third-party AI services?

**Evidence Required:**
- [ ] Data minimization validated in code review:
  - [ ] Code only collects data necessary for stated purpose (no excessive collection)
  - [ ] Code only accesses data required for operation (AI service accounts scoped: read-only, time-limited)
  - [ ] Code deletes data when no longer needed (retention enforcement)
- [ ] Purpose limitation validated:
  - [ ] Code only uses data for stated security purpose (no repurposing for analytics/marketing)
  - [ ] Purpose-based access control enforced (data tagged with purpose)
- [ ] Consent management validated:
  - [ ] Code checks consent before processing personal data
  - [ ] Code respects consent withdrawals (stops processing, deletes data)
  - [ ] Consent linked to data (audit trail)
- [ ] Data subject rights implementation validated:
  - [ ] GDPR Article 15 (Access): Code retrieves ≥95% of individual's data
  - [ ] GDPR Article 17 (Deletion): Code deletes ≥95% with ≥99% verification
  - [ ] Soft-delete with ≥30-day quarantine before hard delete
  - [ ] Legal hold checks before deletion
- [ ] DPA compliance for third-party AI services:
  - [ ] Code verifies DPA before sending data to vendor API
  - [ ] Data residency enforced (sensitive data stays in approved jurisdictions)
  - [ ] Vendor sub-processor validation

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Data minimization opportunities identified | ___ opportunities | ___ opportunities | ≥5 opportunities/quarter | ☐ | |
| DSAR recall (data retrieval completeness) | ___%  | ___% | ≥95% | ☐ | |
| Deletion recall (deletion completeness) | ___%  | ___% | ≥95% | ☐ | |
| DPA coverage (third-party AI services) | ___%  | ___% | 100% | ☐ | |

**Metric Collection Guidance:**
- **Data minimization opportunities**: Code review findings where unnecessary data collection/access identified; count opportunities per quarter; track in review records
- **DSAR recall**: Test DSAR code with known test data; calculate (data instances retrieved / total instances); run quarterly validation; measure with test suite
- **Deletion recall**: Test deletion code with known test data; calculate (instances deleted / total instances); validate with post-deletion scans; measure quarterly
- **DPA coverage**: Count third-party AI services with DPA / total services; audit vendor contracts; validate quarterly; track in compliance system

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of privacy impact assessment in code review)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### **Question 12: Adversarial Review & Chaos Testing**

**Q2.3:** Have you implemented adversarial review and chaos testing for data security implementations including red team reviews attempting to bypass differential privacy, model inversion, membership inference, prompt injection, and classification poisoning, with privacy attack success criteria (membership inference ≤55%, model inversion ≤0.1%), and chaos testing injecting failures (database unavailable, DLP crash, model failure, cross-border restriction) to validate graceful degradation?

**Evidence Required:**
- [ ] Red team adversarial reviews conducted quarterly:
  - [ ] Attempt to bypass differential privacy (query manipulation, composition attacks)
  - [ ] Attempt model inversion (reconstruct training data from model outputs)
  - [ ] Attempt membership inference (determine if data was in training set)
  - [ ] Attempt prompt injection (manipulate LLM-based classification/DLP)
  - [ ] Attempt classification poisoning (corrupt training data via feedback)
- [ ] Privacy attack testing with success criteria:
  - [ ] Membership inference attack accuracy ≤55% (barely better than random 50%)
  - [ ] Model inversion success rate ≤0.1% (extracting identifiable PII)
  - [ ] If criteria not met: Strengthen privacy (reduce epsilon, add regularization, rate limiting)
- [ ] Chaos testing for data systems:
  - [ ] Database unavailable: Verify graceful degradation (fallback to pattern matching, queue requests)
  - [ ] DLP service crash: Verify fail-safe behavior (block by default or alert-only with logging)
  - [ ] Model serving failure: Verify rollback to previous model or rule-based classification
  - [ ] Cross-border restriction: Verify blocking when transfer mechanism unavailable
- [ ] Chaos testing results documented and mitigations implemented
- [ ] Adversarial review findings tracked and remediated

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Membership inference attack accuracy | ___%  | ___% | ≤55% | ☐ | |
| Model inversion success rate | ___%  | ___% | ≤0.1% | ☐ | |
| Chaos test graceful degradation rate | ___%  | ___% | 100% | ☐ | |
| Red team findings remediation time | ___ days | ___ days | ≤30 days | ☐ | |

**Metric Collection Guidance:**
- **Membership inference attack accuracy**: Red team attempts to identify if specific records were in training data; calculate (correct identifications / total attempts); run quarterly; target near-random (50%)
- **Model inversion success rate**: Red team attempts to reconstruct PII from model; calculate (successful reconstructions / total attempts); run quarterly; document in security report
- **Chaos test graceful degradation**: Inject failures; count systems with graceful degradation / total systems tested; measure per chaos test round (quarterly)
- **Red team findings remediation time**: Calculate average days from finding to remediation for red team issues; track in issue tracker; measure per red team engagement

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of adversarial review and chaos testing)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

**Level 2 Summary:**

**Questions Answered:** _____ / 3

**Level 2 Score Calculation:**
- Sum of question scores (0.0, 0.33, 0.67, or 1.0 per question): _____
- Level 2 Average: _____ / 3 = _____
- Level 2 Gated Score: L2 Average × Gate (Gate = 1 if L1 ≥ 1.0, else 0): _____

**Level 2 Gate:** ☐ Passed (L2 Average ≥ 1.0 AND L1 ≥ 1.0) ☐ Not Passed

**Note:** You must achieve Level 2 Average ≥ 1.0 AND Level 1 ≥ 1.0 to proceed to Level 3.

---

## Level 3: Industry-Leading Implementation Review
**Objective:** Achieve formal verification, AI-assisted code review, quantified ROI, and open-source leadership

**Prerequisites:** Level 1 Average ≥ 1.0 AND Level 2 Average ≥ 1.0 required to score Level 3

---

### **Question 13: Formal Verification of Privacy Properties**

**Q3.1:** Have you implemented formal verification of critical privacy properties including mathematical proofs that differential privacy implementation is correct (using Coq, Isabelle, or EasyCrypt), k-anonymity/l-diversity/t-closeness proofs, data deletion completeness proofs (using TLA+ or Alloy model checking), access control formal verification (AI service accounts never have write access), and information flow analysis proving PII never flows to unauthorized destinations?

**Evidence Required:**
- [ ] Differential privacy formal verification:
  - [ ] Mathematical proof that noise addition satisfies epsilon-differential privacy
  - [ ] Proof that privacy budget tracking prevents budget exhaustion
  - [ ] Proof that composition theorem applied correctly
  - [ ] Theorem prover used (Coq, Isabelle, EasyCrypt for differential privacy)
  - [ ] Automated static analysis tracks epsilon consumption across code paths
- [ ] K-anonymity formal verification:
  - [ ] Proof that anonymization achieves k-anonymity for all inputs
  - [ ] L-diversity proof (diverse sensitive attributes within groups)
  - [ ] T-closeness proof (sensitive attribute distribution in group close to overall)
  - [ ] Automated validation on test datasets
- [ ] Data deletion completeness proof:
  - [ ] Proof that deletion workflow visits all data stores
  - [ ] Liveness proof: deletion completes within 30 days
  - [ ] Proof that deleted data cannot be reconstructed
  - [ ] Model checking for deletion workflow (TLA+, Alloy)
- [ ] Access control formal verification:
  - [ ] Proof that AI service accounts never have write access to production data
  - [ ] Proof that access granted only with appropriate role AND purpose
  - [ ] Temporal properties: time-limited credentials expire correctly
- [ ] Information flow analysis:
  - [ ] Proof that PII never flows to unauthorized destinations without DLP check
  - [ ] Taint analysis or information flow type systems used
- [ ] Coverage: ≥5 critical privacy properties formally verified

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Privacy properties formally verified | ___ properties | ___ properties | ≥5 properties | ☐ | |
| Formal verification coverage (critical code) | ___%  | ___% | ≥80% | ☐ | |
| Verification-found defects | ___ defects | ___ defects | ≥3 defects/year | ☐ | |
| Formal verification proof confidence | ___%  | ___% | 100% | ☐ | |

**Metric Collection Guidance:**
- **Privacy properties formally verified**: Count properties with mathematical proofs or model checking verification; document in security architecture; measure annually
- **Formal verification coverage**: Calculate (lines of critical privacy code formally verified / total critical privacy code); measure per release; track in verification reports
- **Verification-found defects**: Count bugs/design flaws discovered during formal verification process; track in issue tracker; measure annually (finding defects is success)
- **Formal verification proof confidence**: Expert review of proofs; calculate (proofs validated by independent expert / total proofs); measure annually; peer review required

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of formal verification)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### **Question 14: AI-Assisted Code Review for Data Security**

**Q3.2:** Have you deployed AI-assisted code review tools that analyze data security code and suggest improvements (detecting common data security bugs, suggesting privacy improvements, identifying performance issues, flagging compliance gaps) with AI learning from historical reviews, achieving human-AI collaboration benefits (≥30% faster reviews, ≥90% defect detection compared to ≥80% Level 1 baseline)?

**Evidence Required:**
- [ ] AI code review assistant deployed and integrated into PR workflow:
  - [ ] AI detects common data security bugs (PII in logs, weak encryption, SQL injection, prompt injection)
  - [ ] AI suggests privacy improvements (add differential privacy, reduce data access scope, implement soft-delete)
  - [ ] AI identifies performance issues (inefficient classification, database query optimization opportunities)
  - [ ] AI flags compliance gaps (missing GDPR consent check, no audit logging)
  - [ ] AI outputs prioritized suggestions with severity, remediation guidance, code examples
- [ ] AI learning from historical code reviews:
  - [ ] Past code review findings used as training data
  - [ ] AI learns organization-specific patterns (common vulnerabilities, coding conventions)
  - [ ] AI accuracy improves over time (fewer false positives, more relevant suggestions)
  - [ ] Feedback loop: human reviewers rate AI suggestions, AI learns from ratings
- [ ] Human-AI collaboration workflow:
  - [ ] AI provides preliminary review (catches common issues instantly)
  - [ ] Human reviewers focus on complex issues (business logic, regulatory interpretation, design)
  - [ ] Review process ≥30% faster than baseline
  - [ ] Defect detection ≥90% (up from ≥80% Level 1 baseline)
- [ ] AI privacy analysis identifies risks:
  - [ ] Data minimization opportunities
  - [ ] Purpose limitation violations
  - [ ] Retention policy gaps
  - [ ] Cross-border flow risks

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Code review speed improvement | ___% | ___% | ≥30% faster | ☐ | |
| Defect detection rate | ___%  | ___% | ≥90% | ☐ | |
| AI suggestion accuracy (accepted/total) | ___%  | ___% | ≥70% | ☐ | |
| Privacy risks identified by AI | ___ risks/mo | ___ risks/mo | ≥10 risks/mo | ☐ | |

**Metric Collection Guidance:**
- **Code review speed improvement**: Measure average time per review before/after AI deployment; calculate percentage reduction; track in review analytics; measure monthly
- **Defect detection rate**: Calculate (defects found in review + production / total defects); track in issue tracker; compare to Level 1 baseline (≥80%); measure quarterly
- **AI suggestion accuracy**: Count AI suggestions accepted by reviewers / total AI suggestions; track reviewer feedback; measure monthly; adjust AI based on feedback
- **Privacy risks identified by AI**: Count privacy issues flagged by AI per month (data minimization, purpose limitation, retention gaps); track in review logs; measure monthly

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of AI-assisted code review)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### **Question 15: Quantified ROI & Open-Source Leadership**

**Q3.3:** Have you quantified implementation review ROI demonstrating defect prevention cost savings, privacy incident avoidance, compliance audit performance improvements (≥60% fewer findings, ≤24-hour evidence production), achieving overall ROI ≥3:1 (benefits exceed costs by 3x), and demonstrated open-source leadership by publishing privacy-preserving implementation patterns, participating in ≥2 standards working groups, presenting at ≥2 external conferences per year, with tools/patterns used by ≥5 external organizations?

**Evidence Required:**
- [ ] Implementation review ROI quantified:
  - [ ] Defect prevention cost savings: (Defects found in review) × (Cost to fix in production - Cost in review)
  - [ ] Privacy incident avoidance: Potential GDPR fines, CCPA penalties, breach costs prevented
  - [ ] Compliance audit performance: Faster evidence production (≤24 hours), ≥60% reduction in audit findings
  - [ ] Overall ROI calculation: (Total savings) / (Total costs) ≥ 3:1
  - [ ] Total costs: Reviewer time, AI tools, training, formal verification tools
  - [ ] ROI tracked annually with documented methodology
- [ ] Open-source privacy patterns published:
  - [ ] Differential privacy implementation patterns (Python, Java, Go)
  - [ ] Data anonymization utilities (k-anonymity, l-diversity)
  - [ ] Secure data deletion libraries (multi-store deletion, verification)
  - [ ] GDPR/CCPA automation frameworks (DSAR fulfillment, deletion workflows)
  - [ ] Prompt injection prevention libraries
  - [ ] Impact: ≥100 GitHub stars OR used by ≥5 external organizations
- [ ] Standards participation:
  - [ ] Active participation in ≥2 privacy engineering standards (ISO 27701, NIST Privacy Framework, OWASP AI Security, IEEE Privacy, W3C Privacy)
  - [ ] Regular meeting participation, draft contributions
- [ ] Conference presentations and publications:
  - [ ] ≥2 external presentations per year (IAPP, RSA, USENIX, Black Hat, DEF CON)
  - [ ] Topics: Formal verification, prompt injection prevention, GDPR automation, privacy-preserving ML
  - [ ] ≥4 publications per year (whitepapers, blog posts)
- [ ] Industry recognition (awards, regulatory commendations, customer testimonials)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Implementation review ROI | ___:1 | ___:1 | ≥3:1 | ☐ | |
| Audit findings reduction | ___%  | ___% | ≥60% reduction | ☐ | |
| Audit evidence production time | ___ hours | ___ hours | ≤24 hours | ☐ | |
| Open-source adoption (external orgs) | ___ orgs | ___ orgs | ≥5 orgs | ☐ | |

**Metric Collection Guidance:**
- **Implementation review ROI**: Calculate annually: (Defect prevention savings + Incident avoidance + Compliance improvements) / (Reviewer costs + Tool costs); document methodology; track year-over-year
- **Audit findings reduction**: Compare privacy/security audit findings year-over-year; calculate percentage reduction; track in audit reports; measure annually
- **Audit evidence production time**: Measure time from auditor request to evidence delivery; calculate average across all audit requests; track in compliance system; measure per audit
- **Open-source adoption**: Count external organizations using published tools/patterns (GitHub analytics, community feedback, direct outreach); measure annually; document case studies

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of ROI quantification and open-source leadership)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

**Level 3 Summary:**

**Questions Answered:** _____ / 3

**Level 3 Score Calculation:**
- Sum of question scores (0.0, 0.33, 0.67, or 1.0 per question): _____
- Level 3 Average: _____ / 3 = _____
- Level 3 Gated Score: L3 Average × Gate (Gate = 1 if L1 ≥ 1.0 AND L2 ≥ 1.0, else 0): _____

**Level 3 Achievement:** ☐ Achieved (L3 Average ≥ 1.0 AND L2 ≥ 1.0 AND L1 ≥ 1.0) ☐ Not Achieved

---

## Scoring Methodology

### Per-Question Scoring

Each question is scored based on Evidence completion and Outcome Metrics achievement:

| Answer Tier | Score | Criteria |
|-------------|-------|----------|
| **Fully Mature** | 1.0 | Evidence complete (all checkboxes) + ≥3 of 4 outcome metrics meet targets |
| **Implemented** | 0.67 | Evidence complete + 2 of 4 outcome metrics meet targets |
| **Partial** | 0.33 | Evidence partially complete (≥50% checkboxes) + <2 metrics meet targets |
| **Not Implemented** | 0.0 | No evidence of this review practice |

### Level Scoring with Gating

**Level 1 Score:**
- Calculate: Average of all Level 1 question scores (9 questions)
- Formula: L1 Score = (Q1 + Q2 + Q3 + Q4 + Q5 + Q6 + Q7 + Q8 + Q9) / 9
- Gate: None (Level 1 is always scored)

**Level 2 Score:**
- Calculate: Average of all Level 2 question scores (3 questions)
- Formula: L2 Score = [(Q10 + Q11 + Q12) / 3] × Gate
- Gate: Gate = 1 if L1 Score ≥ 1.0, else Gate = 0
- **Level 2 questions score 0 unless Level 1 is fully achieved**

**Level 3 Score:**
- Calculate: Average of all Level 3 question scores (3 questions)
- Formula: L3 Score = [(Q13 + Q14 + Q15) / 3] × Gate
- Gate: Gate = 1 if L1 Score ≥ 1.0 AND L2 Score ≥ 1.0, else Gate = 0
- **Level 3 questions score 0 unless Level 1 AND Level 2 are fully achieved**

**Practice Score:**
- Total Score = L1 Score + L2 Score + L3 Score
- Maximum possible: 3.0 (1.0 per level)
- Minimum possible: 0.0

### Interpretation

| Score Range | Maturity Level | Interpretation |
|-------------|----------------|----------------|
| 0.0 - 0.5 | **Initial** | Ad-hoc implementation review, minimal systematic practices |
| 0.5 - 1.0 | **Developing** | Some Level 1 practices in place, inconsistent application |
| 1.0 - 1.5 | **Defined** | Level 1 complete, some Level 2 practices emerging |
| 1.5 - 2.0 | **Managed** | Level 1 complete, Level 2 in progress, systematic and measured |
| 2.0 - 2.5 | **Optimized** | Level 1 & 2 complete, some Level 3 practices, continuous improvement |
| 2.5 - 3.0 | **Industry-Leading** | All levels complete, formal verification, AI-assisted review, demonstrated ROI and leadership |

### Worked Example

**Example Scenario:**
- Level 1: 7 questions "Fully Mature" (1.0), 2 questions "Implemented" (0.67)
  - L1 Score = (7 × 1.0 + 2 × 0.67) / 9 = 8.34 / 9 = 0.93
  - Gate for L2 = 0 (L1 < 1.0)
- Level 2: 2 questions "Fully Mature" (1.0), 1 question "Implemented" (0.67)
  - L2 Score = [(2 × 1.0 + 1 × 0.67) / 3] × 0 = 0.89 × 0 = **0.0** (gated out)
- Level 3: Not attempted
  - L3 Score = 0.0

**Total Practice Score:** 0.93 + 0.0 + 0.0 = **0.93** → **Developing** maturity level

**Interpretation:** Organization has most Level 1 practices but hasn't achieved full comprehensive coverage required to unlock Level 2. Focus should be on strengthening the 2 "Implemented" areas to reach 1.0 threshold.

---

## Next Steps

1. **Complete baseline assessment** - Answer all Level 1 questions first, document current state
2. **Collect baseline metrics** - Measure current values for all outcome metrics
3. **Identify gaps** - Focus on questions scored "Partial" or "Not Implemented"
4. **Set targets** - Define realistic metric targets and timelines
5. **Implement improvements** - Address evidence gaps and metric deficiencies
6. **Re-assess quarterly** - Track progress, update metrics, adjust targets
7. **Advance progressively** - Only pursue Level 2 after achieving L1 ≥ 1.0

---

**Document Information:** Practice: Implementation Review (IR) | Domain: Data | HAIAMM v3.0 | Last Updated: 2026-02-21
