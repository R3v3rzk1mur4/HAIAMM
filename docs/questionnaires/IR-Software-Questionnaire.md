# Implementation Review (IR) - Software Domain
## HAIAMM Assessment Questionnaire v3.0

**Practice:** Implementation Review (IR)
**Domain:** Software
**Purpose:** Assess organizational maturity in reviewing AI code security system implementations for correctness, reliability, security, and performance
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
**Objective:** Verify that AI code security system implementations are correct, tested, secure, and performant

### **Question 1: Mandatory Code Review Process**

**Q1.1:** Do you enforce a mandatory code review process with 100% pull request coverage, defined review participants (peer reviewer + security reviewer for sensitive code), review timelines (≤2 business days for standard reviews, ≤4 hours for critical fixes), and validation that implementation matches approved design specifications?

**Evidence Required:**
- [ ] 100% code review coverage enforced (all pull requests reviewed before merge to main branch)
- [ ] Review participants defined (peer reviewer = AI security engineer, security reviewer for authentication/encryption/data handling code)
- [ ] Review timeline SLAs established (standard reviews ≤2 business days, critical fixes ≤4 hours, re-reviews ≤1 day)
- [ ] Design validation process verified (reviewers check code matches approved design documents from DR practice)
- [ ] Review checklist used (code quality, security, performance, testing criteria)
- [ ] Review tools configured (GitHub PR reviews, GitLab merge requests, code review platforms)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Pull request review coverage | ___% | ___% | 100% | ☐ | |
| Standard review turnaround time (P95) | ___ days | ___ days | <=2 days | ☐ | |
| Critical fix review turnaround time (P95) | ___ hrs | ___ hrs | <=4 hrs | ☐ | |
| PRs with security reviewer involvement (sensitive code) | ___% | ___% | 100% | ☐ | |

**Metric Collection Guidance:**
- **PR review coverage**: `reviewed_PRs / total_merged_PRs × 100` over trailing 30 days. Source: git repository metadata, PR tracking system. Measured continuously
- **Standard review turnaround**: P95 of time from PR creation to first substantive review for non-critical PRs. Source: PR timestamps in GitHub/GitLab. Measured weekly
- **Critical fix turnaround**: P95 of time from critical PR creation to approval. Critical = production bug, security fix. Source: PR labels + timestamps. Measured weekly
- **Security reviewer coverage**: `sensitive_PRs_with_security_review / total_sensitive_PRs × 100`. Sensitive = changes to auth, encryption, data handling. Source: PR labels + reviewer participation. Measured monthly

**Answer:**
- ☐ **Fully Mature** (Evidence complete + >=3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of mandatory code review process)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### **Question 2: AI Model Implementation Review**

**Q1.2:** Do you review AI model implementations including model architecture matching approved design, hyperparameters documented and justified, reproducibility (random seeds set), model versioning, secure model serialization (encrypted model files), training code with no data leakage, and inference code with preprocessing matching training?

**Evidence Required:**
- [ ] Model architecture reviewed (matches approved design spec, layer configurations correct, activation functions appropriate)
- [ ] Hyperparameters documented (learning rate, batch size, epochs, regularization justified in code comments or design doc)
- [ ] Reproducibility verified (random seeds set for NumPy, PyTorch, TensorFlow; deterministic mode enabled where possible)
- [ ] Model versioning implemented (model files tagged with version, experiment tracking with MLflow/Weights & Biases)
- [ ] Model serialization secure (model files encrypted at rest, encryption keys managed via secrets manager)
- [ ] Training code reviewed (train/val/test split correct with no leakage, data augmentation appropriate without bias introduction, training loop correct)
- [ ] Inference code reviewed (preprocessing matches training preprocessing exactly, model loading robust with error handling, inference performance optimized)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Model implementations matching approved design | ___% | ___% | 100% | ☐ | |
| Model training runs with reproducible results (same hyperparams/seed → same accuracy ±2%) | ___% | ___% | >=95% | ☐ | |
| Model files encrypted at rest | ___% | ___% | 100% | ☐ | |
| Inference accuracy degradation from training (due to preprocessing mismatch) | ___% | ___% | <=2% | ☐ | |

**Metric Collection Guidance:**
- **Design match rate**: Manual review of model implementations vs. approved design specs quarterly. Formula: `models_matching_design / total_models_reviewed × 100`. Source: design review records + implementation audit
- **Reproducibility rate**: Re-run training with same hyperparameters and seed, compare final accuracy to original. Formula: `reproducible_runs / total_reproduction_attempts × 100`. Reproducible = accuracy within ±2%. Source: MLOps experiment logs. Test monthly
- **Model encryption coverage**: `encrypted_model_files / total_model_files × 100`. Source: storage encryption audit, secrets manager logs. Verified weekly
- **Inference accuracy degradation**: `(training_accuracy - production_inference_accuracy) / training_accuracy × 100` averaged across models. Source: model evaluation pipeline. Measured per model deployment

**Answer:**
- ☐ **Fully Mature** (Evidence complete + >=3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of AI model implementation review)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### **Question 3: Data Pipeline Implementation Review**

**Q1.3:** Do you review data pipeline implementations including data collection code (read-only credentials, rate limiting, error handling, privacy - no sensitive data logged), data processing code (input validation, null handling, transformation correctness, performance optimization, idempotency), and feedback loop code (schema validation, training data update logic)?

**Evidence Required:**
- [ ] Data collection code reviewed (repository access uses read-only credentials, API rate limiting respected with backoff logic, error handling for API failures with circuit breakers, data privacy verified no PII logged, data provenance tracked)
- [ ] Data processing code reviewed (input validation sanitizes untrusted input, null/missing value handling correct, data transformations validated and tested, performance optimized avoids O(n²), idempotent re-running safe)
- [ ] Feedback loop code reviewed (feedback collection schema validated, feedback validation distinguishes signal from noise, training data update safe with versioning, model retraining trigger logic tested)
- [ ] Pipeline monitoring verified (data quality checks, error rate tracking, processing latency monitoring)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Data pipeline error rate (failed processing jobs) | ___% | ___% | <=1% | ☐ | |
| PII exposure incidents from data pipelines | ___ | ___ | 0 | ☐ | |
| Data transformation correctness (spot checks pass) | ___% | ___% | >=99% | ☐ | |
| Pipeline processing latency (P95) | ___ min | ___ min | <=30 min | ☐ | |

**Metric Collection Guidance:**
- **Pipeline error rate**: `failed_pipeline_runs / total_pipeline_runs × 100` over trailing 30 days. Failed = exception, data quality failure, timeout. Source: pipeline orchestration logs (Airflow, Prefect). Measured daily
- **PII exposure incidents**: Count of incidents where PII was logged, exposed, or leaked via data pipelines. Source: security incident tracker, log analysis. Measured continuously
- **Transformation correctness**: Manual spot check of >=100 random transformed records quarterly. Formula: `correct_transformations / total_spot_checked × 100`. Source: data validation test suite. Quarterly
- **Processing latency**: P95 time from data collection trigger to processed output available. Source: pipeline execution timestamps. Measured per pipeline run

**Answer:**
- ☐ **Fully Mature** (Evidence complete + >=3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of data pipeline implementation review)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### **Question 4: Integration Implementation Review**

**Q1.4:** Do you review integration implementations including IDE plugin code (≤3s latency, async UI operations, memory leak prevention, error handling without crashes), CI/CD integration code (proper exit codes, incremental analysis, caching, ≤10% build time increase, fail-safe mode), and API implementation (input validation, authentication, RBAC authorization, rate limiting, versioning)?

**Evidence Required:**
- [ ] IDE plugin code reviewed (real-time analysis latency ≤3 seconds, UI updates asynchronous don't block IDE, memory leak prevention with proper cleanup, error handling doesn't crash IDE, configuration storage secure)
- [ ] CI/CD integration reviewed (pipeline integration uses correct exit codes, incremental analysis only changed code, caching strategy with proper invalidation, performance budget ≤10% build time, fail-safe mode graceful degradation)
- [ ] API implementation reviewed (input validation on all endpoints prevents injection, authentication secure token handling, authorization RBAC enforced all operations, rate limiting prevents abuse, API versioning backward compatible)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| IDE plugin real-time analysis latency (P95) | ___ sec | ___ sec | <=3 sec | ☐ | |
| CI/CD build time increase from security analysis | ___% | ___% | <=10% | ☐ | |
| API authentication bypass incidents | ___ | ___ | 0 | ☐ | |
| API rate limit effectiveness (abuse attempts blocked) | ___% | ___% | >=99% | ☐ | |

**Metric Collection Guidance:**
- **IDE plugin latency**: P95 of time from code edit to analysis results displayed. Source: IDE plugin telemetry, performance monitoring. Measured per analysis operation
- **Build time increase**: `(build_time_with_security_analysis - baseline_build_time) / baseline_build_time × 100` averaged across projects. Source: CI/CD pipeline timing data. Measured per build
- **Auth bypass incidents**: Count of successful authentication bypass attempts (penetration tests, security incidents). Source: security test results, incident tracker. Measured continuously
- **Rate limit effectiveness**: `blocked_abuse_attempts / total_detected_abuse_attempts × 100`. Abuse = exceeding rate limits. Source: API gateway logs, rate limiter metrics. Measured daily

**Answer:**
- ☐ **Fully Mature** (Evidence complete + >=3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of integration implementation review)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### **Question 5: Infrastructure Code Review**

**Q1.5:** Do you review infrastructure code including Kubernetes manifests (resource limits, health checks, replica configuration), secrets management (no hardcoded credentials, use secrets manager), environment-specific configurations, rolling updates and rollback procedures, and database code (schema migrations, indexes, connection pooling, SQL injection prevention, backup/recovery)?

**Evidence Required:**
- [ ] Kubernetes manifests reviewed (resource limits CPU/memory set, liveness/readiness probes configured, replica count appropriate for HA, pod security policies enforced)
- [ ] Secrets management reviewed (zero hardcoded credentials in configs, secrets manager used AWS Secrets Manager/HashiCorp Vault, secret rotation implemented)
- [ ] Environment configs reviewed (dev/staging/prod separated, environment variables validated, config drift monitoring)
- [ ] Deployment code reviewed (rolling updates configured zero-downtime, rollback procedures tested and documented, deployment health monitoring)
- [ ] Database code reviewed (schema migrations tested and reversible, indexes created for query performance, connection pooling prevents exhaustion, parameterized queries prevent SQL injection, backup/recovery tested)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Hardcoded credentials in infrastructure code | ___ | ___ | 0 | ☐ | |
| Deployment rollback success rate | ___% | ___% | >=95% | ☐ | |
| Database query performance (P95 latency) | ___ ms | ___ ms | <=200 ms | ☐ | |
| SQL injection vulnerabilities in production code | ___ | ___ | 0 | ☐ | |

**Metric Collection Guidance:**
- **Hardcoded credentials**: Count of credentials found in infrastructure code via automated scanning (git-secrets, TruffleHog). Source: security scanner output. Scanned per commit
- **Rollback success rate**: `successful_rollbacks / total_rollback_attempts × 100` over trailing 12 months. Successful = system returns to previous stable state. Source: deployment logs, incident reports. Reviewed quarterly
- **Database query latency**: P95 of query execution time for application queries. Source: database performance monitoring (pg_stat_statements, slow query log). Measured continuously
- **SQL injection vulns**: Count of SQL injection vulnerabilities found in production code via security testing or incidents. Source: security test reports, vulnerability scanner, incidents. Measured continuously

**Answer:**
- ☐ **Fully Mature** (Evidence complete + >=3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of infrastructure code review)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### **Question 6: Security Implementation Review**

**Q1.6:** Do you review security implementations including authentication code (bcrypt/scrypt password hashing, secure session management, OAuth/SAML integration, MFA implementation), encryption code (AES-256/approved algorithms, secure key management, TLS 1.3, encryption at rest for sensitive data), and access control code (least privilege, RBAC implementation, input sanitization, audit logging)?

**Evidence Required:**
- [ ] Authentication code reviewed (password hashing uses bcrypt/scrypt/argon2 with salt, session management uses secure random tokens with expiration, OAuth/SAML integration validates state parameter and tokens, MFA implemented correctly TOTP/WebAuthn)
- [ ] Encryption code reviewed (encryption algorithms approved AES-256/ChaCha20-Poly1305, key management secure keys not in code with rotation, TLS 1.3 with strong cipher suites, encryption at rest for model files/training data/findings)
- [ ] Access control code reviewed (least privilege applied service accounts minimal permissions, RBAC implementation checks roles on all operations, input sanitization prevents injection/XSS, audit logging all security actions)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Authentication bypass vulnerabilities in production | ___ | ___ | 0 | ☐ | |
| Sensitive data encrypted at rest | ___% | ___% | 100% | ☐ | |
| RBAC authorization check coverage (security-sensitive operations) | ___% | ___% | 100% | ☐ | |
| Security audit log completeness (critical actions logged) | ___% | ___% | >=99% | ☐ | |

**Metric Collection Guidance:**
- **Authentication bypass vulns**: Count of authentication bypass vulnerabilities in production code. Source: security testing results, penetration tests, vulnerability scanner, security incidents. Measured continuously
- **Encryption at rest coverage**: `sensitive_data_fields_encrypted / total_sensitive_data_fields × 100`. Sensitive = model files, training data, security findings, PII. Source: data encryption audit. Reviewed quarterly
- **RBAC check coverage**: `security_sensitive_operations_with_RBAC_check / total_security_sensitive_operations × 100`. Source: code review audit, automated security testing. Reviewed monthly
- **Audit log completeness**: `critical_actions_logged / total_critical_actions_observed × 100`. Critical = authentication, authorization changes, data access, config changes. Source: log analysis vs. operation inventory. Measured weekly

**Answer:**
- ☐ **Fully Mature** (Evidence complete + >=3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of security implementation review)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### **Question 7: Test Coverage Review**

**Q1.7:** Do you review test coverage including unit tests (≥80% coverage, edge cases, error paths, mocking), integration tests (end-to-end workflows, external integrations, database operations, performance tests), and security tests (fuzzing, authentication/authorization tests, adversarial robustness tests)?

**Evidence Required:**
- [ ] Unit test coverage reviewed (≥80% code coverage for critical paths, edge cases tested null/empty/boundary values, error paths tested exception handling, mock dependencies correctly isolate units)
- [ ] Integration test coverage reviewed (end-to-end workflows tested code submission to finding generation, external integrations tested repository access/tool APIs, database operations tested CRUD correct, performance tests latency/throughput under load)
- [ ] Security test coverage reviewed (input validation tested fuzzing/injection attempts, authentication tests password attempts/token handling, authorization tests access control enforcement, adversarial robustness tests model evasion attempts)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Unit test code coverage (critical code paths) | ___% | ___% | >=80% | ☐ | |
| Integration test pass rate on merge to main | ___% | ___% | >=95% | ☐ | |
| Security test coverage (auth/authz/input validation) | ___% | ___% | >=80% | ☐ | |
| Defects caught by tests vs. production | ___% | ___% | >=80% | ☐ | |

**Metric Collection Guidance:**
- **Unit test coverage**: Line coverage percentage from coverage tool (coverage.py, JaCoCo, Istanbul) for critical code paths. Source: CI/CD coverage reports. Measured per build
- **Integration test pass rate**: `passing_integration_test_runs / total_integration_test_runs × 100` on main branch. Source: CI/CD test results. Measured per merge
- **Security test coverage**: `security_test_cases_passing / total_required_security_test_cases × 100`. Required = auth, authz, input validation, session management. Source: security test suite inventory. Reviewed monthly
- **Defects caught in tests**: `defects_found_in_testing / (defects_found_in_testing + defects_found_in_production) × 100` over trailing 6 months. Source: bug tracker with discovery phase tags. Reviewed quarterly

**Answer:**
- ☐ **Fully Mature** (Evidence complete + >=3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of test coverage review)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### **Question 8: Automated Code Analysis**

**Q1.8:** Do you review automated code analysis including static analysis tools (language-specific linters pylint/eslint/rubocop/golangci-lint, security scanners Bandit/Brakeman/gosec, dependency scanners for vulnerable libraries), and quality metrics (code duplication ≤5%, function length ≤50 lines, file length ≤500 lines, naming conventions followed)?

**Evidence Required:**
- [ ] Static analysis tools configured (language linters pylint/eslint/rubocop/golangci-lint enabled in CI, security scanners Bandit/Brakeman/gosec integrated, dependency scanners check vulnerable libraries, cyclomatic complexity threshold ≤15)
- [ ] Quality metrics enforced (code duplication ≤5% via SonarQube/CodeClimate, function length ≤50 lines, file length ≤500 lines, naming conventions clear and consistent)
- [ ] Tool integration verified (automated checks run on every PR, blocking failures prevent merge, results visible to reviewers)
- [ ] False positive management (triage process for false positives, suppression rules documented and reviewed)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| PRs passing automated static analysis on first attempt | ___% | ___% | >=90% | ☐ | |
| Security scanner findings (high/critical severity) | ___ | ___ | <=5/quarter | ☐ | |
| Code duplication percentage | ___% | ___% | <=5% | ☐ | |
| Vulnerable dependencies in production | ___ | ___ | 0 critical/high | ☐ | |

**Metric Collection Guidance:**
- **Static analysis pass rate**: `PRs_passing_all_checks_first_run / total_PRs × 100` over trailing 30 days. Source: CI/CD check results. Measured weekly
- **Security scanner findings**: Count of high/critical severity findings from Bandit/Brakeman/gosec per quarter. Source: security scanner reports aggregated. Reviewed quarterly
- **Code duplication**: Percentage of duplicated code blocks from SonarQube/CodeClimate analysis. Source: code quality platform dashboard. Measured per analysis run
- **Vulnerable dependencies**: Count of critical/high severity vulnerabilities in production dependencies from scanner (Dependabot, Snyk, npm audit). Source: dependency scanner reports. Measured weekly

**Answer:**
- ☐ **Fully Mature** (Evidence complete + >=3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of automated code analysis)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### **Question 9: Prompt Injection Security Review**

**Q1.9:** Do you review LLM integration code for prompt injection defenses including prompt construction (input sanitization, structural delimiters for system/user prompts, no credentials in prompts), output validation (LLM outputs validated before execution, allowlist for actions), context window management (scope limits, per-user isolation), RAG security (document validation, PII removal), and tool calling (parameter validation, function allowlist, execution logging)?

**Evidence Required:**
- [ ] Prompt construction reviewed (user input sanitized removes/escapes special characters and instructions, system and user prompts separated via structural delimiters JSON/XML, no credentials/API keys/PII in system prompts)
- [ ] Output validation reviewed (LLM outputs validated before execution code/commands parsed and checked, allowlist validation only permitted operations executable, allowlist complete and restrictive)
- [ ] Context window management reviewed (context limited to required scope max window size enforced, context isolation per user/session User A never sees User B's context)
- [ ] RAG implementation reviewed if applicable (documents sanitized before knowledge base ingestion, PII removed from retrieved documents before LLM processing, metadata sanitized no injection in doc properties)
- [ ] Tool calling reviewed if applicable (function parameters validated type/range/allowlist, allowlist of permitted functions enforced minimal and necessary, function execution logged user/timestamp/function/parameters/result)
- [ ] Error handling reviewed (LLM errors don't leak system prompts or internal state, graceful degradation on LLM failure)
- [ ] Test coverage reviewed (prompt injection test cases exist and pass, system prompt extraction tests verify zero successful extractions)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Prompt injection vulnerabilities in production LLM integrations | ___ | ___ | 0 | ☐ | |
| LLM integrations using structural prompt separation | ___% | ___% | 100% | ☐ | |
| LLM-generated actions validated before execution | ___% | ___% | 100% | ☐ | |
| Prompt injection test coverage (intent×technique×evasion) | ___% | ___% | >=80% | ☐ | |

**Metric Collection Guidance:**
- **Prompt injection vulns**: Count of prompt injection vulnerabilities found in production LLM integrations via security testing or incidents. Source: penetration test results, security scanner, incident tracker. Measured continuously
- **Structural separation adoption**: `LLM_integrations_with_structural_separation / total_LLM_integrations × 100`. Structural = JSON/XML delimiters, not string concatenation. Source: code review audit. Reviewed quarterly
- **Output validation coverage**: `LLM_actions_with_validation / total_LLM_generated_actions × 100`. Actions = code execution, function calls, API calls. Source: LLM integration audit. Reviewed monthly
- **Test coverage**: `tested_combinations / total_combinations × 100`. Total = 13 intents × 18 techniques × 20 evasions from Arcanum taxonomy (subset tested). Source: prompt injection test suite. Reviewed quarterly

**Answer:**
- ☐ **Fully Mature** (Evidence complete + >=3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of prompt injection security review)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

## Level 2: Advanced Implementation Review
**Objective:** Verify advanced review capabilities including threat modeling, performance profiling, and compliance review

### **Question 10: Threat Modeling During Code Review**

**Q2.1:** Do you perform threat modeling during code review including STRIDE analysis of code changes (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege), threat model updates per review, and security design pattern enforcement?

**Evidence Required:**
- [ ] STRIDE analysis process defined (reviewers apply STRIDE framework to code changes, threat model template provided, training on STRIDE analysis for reviewers)
- [ ] Threat model updates verified (threat model updated when code introduces new attack surface, security requirements derived from threat analysis, mitigation tracking in threat model)
- [ ] Security design patterns enforced (defense in depth, fail secure, least privilege, input validation, secure defaults enforced in reviews)
- [ ] Threat modeling documentation reviewed (threat model artifacts stored with code, threat model review part of security-sensitive PR approval)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Security-sensitive PRs with completed STRIDE analysis | ___% | ___% | 100% | ☐ | |
| Threat model coverage (components with documented threat models) | ___% | ___% | >=80% | ☐ | |
| Security design pattern violations caught in review | ___ | ___ | >=90% caught | ☐ | |
| Security vulnerabilities traced to missing threat analysis | ___% | ___% | <=5% | ☐ | |

**Metric Collection Guidance:**
- **STRIDE analysis coverage**: `security_PRs_with_STRIDE_analysis / total_security_PRs × 100`. Security PRs = auth, authz, encryption, data handling. Source: PR review checklist completion. Measured monthly
- **Threat model coverage**: `components_with_threat_models / total_security_critical_components × 100`. Source: threat model repository inventory. Reviewed quarterly
- **Pattern violation detection**: `pattern_violations_caught_in_review / total_pattern_violations_introduced × 100`. Total = violations caught in review + violations found in testing/production. Source: code review findings + security test results. Measured quarterly
- **Vulnerabilities from missing threat analysis**: `vulnerabilities_due_to_missing_threat_model / total_vulnerabilities_found × 100` over trailing 12 months. Source: vulnerability root cause analysis. Reviewed annually

**Answer:**
- ☐ **Fully Mature** (Evidence complete + >=3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of threat modeling during code review)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### **Question 11: Performance Profiling Before Production**

**Q2.2:** Do you perform performance profiling before production including profiling for latency and throughput bottlenecks, bottleneck identification in critical code paths, and optimization of hot paths with measurable performance improvements?

**Evidence Required:**
- [ ] Performance profiling process defined (profiling required for performance-critical PRs, profiling tools configured cProfile/perf/pprof, profiling results reviewed before merge)
- [ ] Bottleneck identification verified (critical code paths identified, profiling identifies CPU/memory/I/O bottlenecks, flame graphs reviewed)
- [ ] Hot path optimization reviewed (optimization applied to hot paths, optimization impact measured before/after, regression testing verifies correctness maintained)
- [ ] Performance budgets enforced (latency budgets defined per operation, throughput budgets defined, budget violations caught in review)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Performance-critical PRs with profiling results | ___% | ___% | >=90% | ☐ | |
| Performance regressions caught in review vs. production | ___% | ___% | >=80% | ☐ | |
| Hot path optimization impact (average performance improvement) | ___% | ___% | >=30% | ☐ | |
| API operations meeting latency budgets | ___% | ___% | >=95% | ☐ | |

**Metric Collection Guidance:**
- **Profiling coverage**: `performance_PRs_with_profiling / total_performance_critical_PRs × 100`. Performance-critical = data processing, ML inference, API endpoints. Source: PR review checklist. Measured monthly
- **Regression detection rate**: `regressions_caught_in_review / (regressions_caught_in_review + regressions_found_in_production) × 100` over trailing 6 months. Source: performance test results + production monitoring alerts. Reviewed quarterly
- **Optimization impact**: Average percentage improvement in latency/throughput from hot path optimizations. Formula: `avg((baseline - optimized) / baseline × 100)`. Source: before/after profiling results. Measured per optimization
- **Budget compliance**: `operations_meeting_budget / total_operations_with_budget × 100`. Source: performance monitoring vs. budget definitions. Measured weekly

**Answer:**
- ☐ **Fully Mature** (Evidence complete + >=3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of performance profiling before production)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### **Question 12: Compliance Code Review**

**Q2.3:** Do you perform compliance code review including GDPR/HIPAA requirements validated in code (data minimization, consent management, right to erasure, data retention), accessibility review for UI components (WCAG 2.1 Level AA), and regulatory compliance validation specific to your industry?

**Evidence Required:**
- [ ] GDPR/HIPAA code review process defined (compliance requirements mapped to code, data handling reviewed for compliance, consent management implementation reviewed, data retention policies enforced in code)
- [ ] Accessibility review process defined (UI components reviewed for WCAG 2.1 AA, automated accessibility testing integrated axe/Pa11y, keyboard navigation verified, screen reader compatibility tested)
- [ ] Regulatory compliance validation (industry-specific regulations identified, compliance requirements validated in code review, compliance documentation updated)
- [ ] Compliance test coverage verified (automated compliance tests, manual compliance audits, compliance violations caught in review)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Data handling code with GDPR/HIPAA compliance review | ___% | ___% | 100% | ☐ | |
| UI components meeting WCAG 2.1 AA standards | ___% | ___% | >=90% | ☐ | |
| Compliance violations caught in review vs. audit | ___% | ___% | >=75% | ☐ | |
| Regulatory compliance findings (external audits) | ___ | ___ | <=2/year | ☐ | |

**Metric Collection Guidance:**
- **Compliance review coverage**: `data_handling_PRs_with_compliance_review / total_data_handling_PRs × 100`. Data handling = PII collection, storage, processing, deletion. Source: PR review checklist. Measured monthly
- **WCAG compliance**: `accessible_UI_components / total_UI_components × 100`. Accessible = passes automated testing + manual review. Source: accessibility test results. Reviewed quarterly
- **Violation detection rate**: `compliance_violations_caught_in_review / (violations_in_review + violations_in_audit) × 100` over trailing 12 months. Source: review findings + audit reports. Reviewed annually
- **External audit findings**: Count of compliance findings from external audits (GDPR, HIPAA, SOC2, etc.) per year. Source: audit reports. Reviewed annually

**Answer:**
- ☐ **Fully Mature** (Evidence complete + >=3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of compliance code review)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

## Level 3: Industry-Leading Implementation Review
**Objective:** Verify research-grade techniques including AI-assisted review, formal verification, and open-source contribution

### **Question 13: AI-Assisted Code Review**

**Q3.1:** Do you use AI-assisted code review including AI suggesting improvements and detecting patterns, AI learning from historical reviews, and human-AI collaboration achieving >=30% faster reviews while maintaining or improving quality?

**Evidence Required:**
- [ ] AI review assistance implemented (AI tool integrated into code review workflow GitHub Copilot/Amazon CodeGuru/DeepCode, AI suggests security vulnerabilities/performance issues/code quality improvements, AI learns from accepted/rejected suggestions)
- [ ] Historical review learning verified (AI trained on historical code reviews and findings, AI pattern detection improves over time, AI suggestions personalized to team coding style)
- [ ] Human-AI collaboration measured (reviewers use AI suggestions as starting point, human reviewers validate and augment AI findings, collaboration workflow optimized)
- [ ] Quality maintenance verified (review quality with AI >= review quality without AI, false positive rate acceptable, AI explanations improve reviewer understanding)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Code review turnaround time reduction with AI assistance | ___% | ___% | >=30% faster | ☐ | |
| AI-detected issues vs. human-only reviews | ___% | ___% | >=20% more | ☐ | |
| Review quality with AI (defects caught per review) | ___ | ___ | >= baseline | ☐ | |
| Reviewer satisfaction with AI assistance | ___% | ___% | >=80% | ☐ | |

**Metric Collection Guidance:**
- **Turnaround time reduction**: `(baseline_review_time - AI_assisted_review_time) / baseline_review_time × 100`. Baseline = reviews without AI from prior period. Source: PR timestamp analysis. Measured monthly
- **AI issue detection improvement**: `issues_found_with_AI / issues_found_without_AI × 100 - 100`. Compare AI-assisted reviews to human-only historical baseline. Source: review finding analysis. Measured quarterly
- **Review quality maintenance**: Average defects caught per review (found in testing/production after code review). Compare AI-assisted period to baseline. Source: defect tracking with review correlation. Measured quarterly
- **Reviewer satisfaction**: Survey code reviewers on AI assistance value. Formula: percentage rating >=4/5 on Likert scale. Source: quarterly reviewer survey. Quarterly

**Answer:**
- ☐ **Fully Mature** (Evidence complete + >=3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of AI-assisted code review)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### **Question 14: Formal Verification**

**Q3.2:** Do you use formal verification for critical code paths including formal specifications (TLA+, Coq, Dafny), mathematical proofs of correctness for security-critical algorithms, and verification of concurrency properties (no deadlocks, no race conditions)?

**Evidence Required:**
- [ ] Formal specification process defined (critical algorithms identified for formal verification, specification language selected TLA+/Coq/Dafny/Z3, specifications written by trained engineers)
- [ ] Correctness proofs verified (mathematical proofs that code satisfies specifications, proof checking automated with theorem provers, proof coverage for security-critical properties)
- [ ] Concurrency verification reviewed (concurrent algorithms formally verified, deadlock freedom proven, race condition freedom proven, liveness properties verified)
- [ ] Implementation-to-specification mapping verified (code matches formal specification, refinement proofs completed, specification maintained with code changes)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Critical algorithms with formal specifications | ___% | ___% | >=50% | ☐ | |
| Concurrency bugs in formally verified components | ___ | ___ | 0 | ☐ | |
| Correctness property violations in production | ___ | ___ | 0 | ☐ | |
| Formal verification coverage (security-critical code paths) | ___% | ___% | >=30% | ☐ | |

**Metric Collection Guidance:**
- **Formal spec coverage**: `critical_algorithms_with_formal_specs / total_critical_algorithms × 100`. Critical = authentication, authorization, cryptography, access control. Source: formal verification inventory. Reviewed semi-annually
- **Concurrency bugs**: Count of concurrency-related bugs (race conditions, deadlocks, atomicity violations) in formally verified components. Source: bug tracker filtered by component + concurrency tag. Measured continuously
- **Property violations**: Count of formal correctness properties violated in production for formally verified code. Source: runtime assertions, monitoring, incidents. Measured continuously
- **Verification coverage**: `verified_code_lines / total_security_critical_code_lines × 100`. Source: formal verification tool output + code inventory. Reviewed quarterly

**Answer:**
- ☐ **Fully Mature** (Evidence complete + >=3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of formal verification)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### **Question 15: Open-Source Contribution & Quantified ROI**

**Q3.3:** Do you contribute to open-source secure coding standards and projects, publish your organization's secure coding guidelines, contribute security improvements to open-source AI security tools, and measure code review ROI with >=50:1 benefit-to-cost ratio (defects prevented vs. review effort)?

**Evidence Required:**
- [ ] Open-source standards contribution verified (contributions to OWASP AI Security, NIST AI RMF, or similar standards bodies, secure coding guidelines published publicly, participation in industry working groups)
- [ ] Open-source tool contribution verified (security improvements contributed to open-source SAST/DAST/security tools, bug fixes and features contributed, community engagement maintained)
- [ ] Public secure coding guidelines published (organization's AI security coding standards published, guidelines include concrete examples and rationale, guidelines maintained and updated)
- [ ] Code review ROI measured (cost = reviewer time investment, benefit = defects prevented × cost per production defect, ROI ratio calculated and tracked)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Open-source contributions per year (commits, PRs, publications) | ___ | ___ | >=12 | ☐ | |
| Published secure coding guidelines (documents available publicly) | ___ | ___ | >=1 | ☐ | |
| Code review ROI (benefit from prevented defects / cost of reviews) | ___:1 | ___:1 | >=50:1 | ☐ | |
| Industry recognition for secure coding leadership | ___ | ___ | >=1 award/citation | ☐ | |

**Metric Collection Guidance:**
- **Open-source contributions**: Count of commits, pull requests, standards publications, conference presentations per year. Source: GitHub activity, standards body records, conference proceedings. Reviewed annually
- **Published guidelines**: Count of publicly accessible secure coding guideline documents. Source: public website, GitHub repository, published papers. Reviewed annually
- **Code review ROI**: Formula: `(defects_prevented_by_review × cost_per_production_defect) / (review_hours × reviewer_hourly_cost)`. Defects prevented = historical rate of defects per KLOC × code reviewed. Cost per production defect = incident response + fix cost (industry average $5,000-$10,000). Source: review metrics + incident cost tracking. Calculated annually
- **Industry recognition**: Count of awards, citations, keynote invitations, media mentions for secure coding practices. Source: awards database, citation tracking. Reviewed annually

**Answer:**
- ☐ **Fully Mature** (Evidence complete + >=3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of open-source contribution or ROI measurement)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

## Scoring Methodology

### Per-Question Scoring

| Answer | Score | Criteria |
|--------|-------|----------|
| Fully Mature | 1.0 | Evidence complete + >=75% of outcome metrics meet targets (>=3 of 4 metrics) |
| Implemented | 0.67 | Evidence complete + 50-74% of outcome metrics meet targets (2 of 4 metrics) |
| Partial | 0.33 | Evidence partially complete + <50% of metrics meet targets (<2 metrics) |
| Not Implemented | 0.0 | No evidence of implementation review |

### Level Scoring

- **L1 Score** = Average of all L1 question scores (Q1.1 through Q1.9)
- **L2 Score** = Average of all L2 question scores (Q2.1 through Q2.3) × (1 if L1 >= 1.0, else 0)
- **L3 Score** = Average of all L3 question scores (Q3.1 through Q3.3) × (1 if L2 >= 1.0, else 0)

### Practice Score

**IR-Software Practice Score = L1 + L2 + L3** (Maximum: 3.0)

| Score Range | Interpretation |
|-------------|---------------|
| 0.0 - 0.5 | Initial - No systematic implementation review for AI security code |
| 0.5 - 1.0 | Developing - Basic code reviews established but metrics not tracked |
| 1.0 - 1.5 | Defined - Comprehensive L1 reviews with measurable quality targets |
| 1.5 - 2.0 | Managed - Advanced threat modeling, profiling, and compliance reviews |
| 2.0 - 2.5 | Optimizing - AI-assisted review and formal verification adopted |
| 2.5 - 3.0 | Industry-Leading - Full formal verification, AI-assisted review, and open-source leadership |

### Score Calculation Example

```
Example Organization:
  Q1.1 = 1.0  (Fully Mature)    Q1.6 = 1.0  (Fully Mature)
  Q1.2 = 0.67 (Implemented)     Q1.7 = 0.67 (Implemented)
  Q1.3 = 0.67 (Implemented)     Q1.8 = 1.0  (Fully Mature)
  Q1.4 = 1.0  (Fully Mature)    Q1.9 = 0.67 (Implemented)
  Q1.5 = 1.0  (Fully Mature)

  L1 Score = (1.0+0.67+0.67+1.0+1.0+1.0+0.67+1.0+0.67) / 9 = 0.85

  Since L1 (0.85) < 1.0, L2 is gated:
  L2 Score = 0 (must achieve L1 >= 1.0 first)
  L3 Score = 0 (gated by L2)

  Practice Score = 0.85 + 0 + 0 = 0.85 (Developing)

  Action: Improve Q1.2 (model implementation), Q1.3 (data pipeline),
  Q1.7 (test coverage), and Q1.9 (prompt injection security) from
  Implemented to Fully Mature to unlock Level 2.
```

---

**Document Information:** Practice: Implementation Review (IR) | Domain: Software | HAIAMM v3.0 | Last Updated: 2026-02-10
