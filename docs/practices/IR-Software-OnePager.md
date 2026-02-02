# Implementation Review Practice – Software Domain
## HAIAMM v2.0 One-Pager

### Practice Overview

Implementation Review for Software ensures AI code security system implementations correctly realize approved designs, follow secure coding practices, and meet quality standards before deployment.

**Scope**: Code reviews for:
- AI model implementations (training scripts, inference code)
- Data pipeline implementations (ETL, preprocessing, labeling)
- Integration implementations (IDE plugins, CI/CD integrations, APIs)
- Infrastructure code (deployment configs, Kubernetes manifests, Terraform)
- Security implementations (authentication, encryption, access controls)

**Why This Matters**: Even well-designed AI systems fail if poorly implemented. Implementation reviews catch bugs, security vulnerabilities, performance issues, and code quality problems before production deployment.

---

### Level 1: Foundational Implementation Review

### Core Objectives
1. Establish mandatory code review process for all AI security system code
2. Define code review criteria and automated checks
3. Implement peer review with security focus
4. Validate implementation matches approved design
5. Check for common vulnerabilities and anti-patterns
6. Review test coverage and quality

### Key Activities

#### 1. Code Review Process

**Review Triggers**:
- All code changes via pull requests (100% review coverage)
- Pre-merge reviews (code reviewed before merging to main branch)
- Security-focused reviews for authentication, encryption, data handling code

**Review Participants**:
- **Code Author**: Submits PR with description, test results
- **Primary Reviewer**: Another AI security engineer (peer review)
- **Security Reviewer**: Security expert for sensitive code paths
- **Automated Tools**: Static analysis, linters, security scanners

**Review Timeline**:
- Code reviews completed within ≤2 business days
- Critical bug fixes: ≤4 hours
- Feedback addressed and re-review within ≤1 day

#### 2. AI Model Implementation Review

**Model Code Quality**:
- [ ] Model architecture matches approved design
- [ ] Hyperparameters documented and justified
- [ ] Random seeds set for reproducibility
- [ ] Model versioning implemented (track model versions)
- [ ] Model serialization secure (encryption for model files)

**Training Code Review**:
- [ ] Training data loading correct (no data leakage between train/val/test)
- [ ] Data augmentation appropriate (doesn't introduce bias)
- [ ] Training loop correct (proper epochs, batching, optimization)
- [ ] Validation during training (early stopping, checkpointing)
- [ ] Training metrics logged (loss, accuracy, precision, recall)

**Inference Code Review**:
- [ ] Preprocessing matches training preprocessing (crucial for accuracy)
- [ ] Model loading robust (handle missing model files gracefully)
- [ ] Inference performance optimized (batching, caching where appropriate)
- [ ] Error handling for edge cases (malformed input, out-of-memory)
- [ ] Explainability code generates useful explanations

#### 3. Data Pipeline Implementation Review

**Data Collection Code**:
- [ ] Repository access uses read-only credentials
- [ ] API rate limiting respected (avoid throttling)
- [ ] Error handling for API failures (retry logic, circuit breakers)
- [ ] Data privacy: No sensitive data logged or exposed
- [ ] Data provenance tracked (where data came from)

**Data Processing Code**:
- [ ] Input validation (sanitize untrusted input)
- [ ] Data type handling correct (handle nulls, missing values)
- [ ] Data transformations correct and tested
- [ ] Performance optimized (avoid O(n²) algorithms on large datasets)
- [ ] Idempotency (re-running doesn't cause issues)

**Feedback Loop Code**:
- [ ] Feedback collection code validated (correct schema, no data loss)
- [ ] Feedback validation logic correct (distinguish signal from noise)
- [ ] Training data update logic safe (no accidental deletion, versioning)
- [ ] Model retraining trigger logic tested

#### 4. Integration Implementation Review

**IDE Plugin Code**:
- [ ] Real-time analysis performs within latency budget (≤3 seconds)
- [ ] UI updates don't block IDE (async operations)
- [ ] Memory leaks prevented (proper cleanup)
- [ ] Error handling doesn't crash IDE
- [ ] Configuration properly stored (user preferences)

**CI/CD Integration Code**:
- [ ] Pipeline integration correct (proper exit codes)
- [ ] Incremental analysis works (only changed code analyzed)
- [ ] Caching implemented correctly (cache invalidation strategy)
- [ ] Performance meets budget (≤10% build time increase)
- [ ] Fail-safe mode implemented (graceful degradation if AI unavailable)

**API Implementation**:
- [ ] Input validation on all endpoints (prevent injection attacks)
- [ ] Authentication implemented correctly (secure token handling)
- [ ] Authorization checked on all operations (RBAC enforced)
- [ ] Rate limiting implemented (prevent abuse)
- [ ] API versioning handled (backward compatibility)

#### 5. Infrastructure Code Review

**Deployment Code**:
- [ ] Kubernetes manifests correct (resource limits, health checks, replicas)
- [ ] Secrets management secure (no hardcoded credentials, use secrets manager)
- [ ] Environment-specific configs separated (dev, staging, prod)
- [ ] Rolling updates configured (zero-downtime deployments)
- [ ] Rollback procedures tested

**Database Code**:
- [ ] Schema migration scripts correct and tested
- [ ] Indexes created for performance (analyze query patterns)
- [ ] Connection pooling configured (prevent connection exhaustion)
- [ ] SQL injection prevented (parameterized queries, ORM)
- [ ] Backup and recovery tested

#### 6. Security Implementation Review

**Authentication Code**:
- [ ] Password handling secure (bcrypt/scrypt, salted)
- [ ] Session management secure (random tokens, expiration, secure cookies)
- [ ] OAuth/SAML integration correct (state parameter, token validation)
- [ ] MFA implemented correctly (TOTP, WebAuthn)

**Encryption Code**:
- [ ] Encryption algorithms approved (AES-256, ChaCha20-Poly1305)
- [ ] Key management secure (keys not in code, rotation implemented)
- [ ] TLS configuration secure (TLS 1.3, strong cipher suites)
- [ ] Encryption at rest for sensitive data (model files, training data, findings)

**Access Control Code**:
- [ ] Least privilege principle applied (service accounts minimal permissions)
- [ ] RBAC implementation correct (role checks on all operations)
- [ ] Input sanitization (prevent code injection, XSS, etc.)
- [ ] Audit logging implemented (all security-relevant actions logged)

#### 7. Test Coverage Review

**Unit Test Coverage**:
- [ ] Test coverage ≥80% for critical code paths
- [ ] Edge cases tested (null inputs, empty lists, boundary values)
- [ ] Error paths tested (exception handling validated)
- [ ] Mock dependencies correctly (isolate unit being tested)

**Integration Test Coverage**:
- [ ] End-to-end workflows tested (from code submission to finding generation)
- [ ] External integrations tested (repository access, tool APIs)
- [ ] Database operations tested (CRUD operations work correctly)
- [ ] Performance tests (latency, throughput under load)

**Security Test Coverage**:
- [ ] Input validation tested (fuzzing, injection attempts)
- [ ] Authentication tests (password attempts, token handling)
- [ ] Authorization tests (access control enforcement)
- [ ] Adversarial robustness tests (model evasion attempts)

#### 8. Automated Code Analysis

**Static Analysis Tools**:
- [ ] Language-specific linters (pylint, eslint, rubocop, golangci-lint)
- [ ] Security scanners (Bandit for Python, Brakeman for Ruby, gosec for Go)
- [ ] Dependency scanners (check for vulnerable libraries)
- [ ] Code complexity metrics (cyclomatic complexity ≤15)

**Quality Metrics**:
- [ ] Code duplication ≤5% (DRY principle)
- [ ] Function length reasonable (≤50 lines per function)
- [ ] File length reasonable (≤500 lines per file)
- [ ] Clear naming conventions followed

#### 9. Prompt Injection Security Review *(derived from Arcanum PI Taxonomy by Jason Haddix, CC BY 4.0)*

For AI software security systems integrating LLMs (code review assistants, security chatbots, AI-powered SAST/DAST), conduct specialized code review to validate prompt injection defenses.

**LLM Integration Code Review Checklist**:

**Prompt Construction Review**:
- [ ] User input sanitized before inclusion in prompts
  - Check: Input validation removes/escapes special characters, instructions
  - Anti-pattern: Directly concatenating user input into system prompts
- [ ] System prompts and user prompts separated via structural delimiters
  - Good: `{"system": "...", "user": "..."}` or XML tags `<system>...</system><user>...</user>`
  - Bad: String concatenation of system and user content
- [ ] No credentials, API keys, or PII in system prompts
  - Check: System prompts contain only logic, no sensitive data
  - Review: All system prompt content for accidental data inclusion

**Output Validation Review**:
- [ ] LLM outputs validated before execution
  - Check: Code/commands generated by LLM parsed and validated before running
  - Anti-pattern: Directly executing LLM-generated code without validation
- [ ] Allowlist validation for LLM-generated actions
  - Check: Only permitted operations (from allowlist) can be executed
  - Review: Allowlist is complete and restrictive

**Context Window Management Review**:
- [ ] Context limited to required scope (no unbounded history)
  - Check: Maximum context window size enforced (e.g., ≤10 interactions)
  - Anti-pattern: Accumulating unlimited conversation history
- [ ] Context isolation per user/session
  - Check: User A's context never accessible to User B
  - Review: Context storage and retrieval logic for isolation

**Input Validation Review**:
- [ ] Prompt injection pattern detection implemented
  - Check: Input scanned for keywords (ignore, system, instruction), role-playing attempts
  - Review: Detection patterns comprehensive and up-to-date
- [ ] Rate limiting prevents enumeration/DoS
  - Check: Per-user rate limits enforced (e.g., 100 requests/minute)
  - Review: Rate limiting configuration appropriate for use case

**RAG Implementation Review** (if applicable):
- [ ] Documents sanitized before ingestion into knowledge base
  - Check: Documents scanned for embedded instructions before adding to RAG
  - Anti-pattern: Blindly ingesting external documents without validation
- [ ] PII removed from retrieved documents before LLM processing
  - Check: PII redaction applied to RAG retrieval results
- [ ] Metadata sanitized (no prompt injection in doc metadata)
  - Check: File metadata, document properties scanned for malicious content

**Tool Calling/Function Execution Review** (if applicable):
- [ ] Function parameters validated before execution
  - Check: Type validation, range validation, allowlist enforcement
  - Example: IP address parameter validated as valid IPv4/IPv6, no embedded instructions
- [ ] Allowlist of permitted functions enforced
  - Check: Only explicitly allowed functions can be called by LLM
  - Review: Allowlist is minimal and necessary
- [ ] Function execution logged for audit
  - Check: All LLM-triggered function calls logged with parameters
  - Review: Logging includes user, timestamp, function, parameters, result

**Error Handling Review**:
- [ ] LLM errors don't leak system prompts or internal state
  - Check: Error messages sanitized, no system prompt content in errors
  - Review: Error handling paths for information disclosure
- [ ] Graceful degradation on LLM failure
  - Check: System remains functional if LLM unavailable
  - Anti-pattern: Hard dependency on LLM availability

**Testing Review**:
- [ ] Prompt injection test cases exist and pass
  - Check: Unit tests for common injection patterns (role-playing, encoding, etc.)
  - Review: Test coverage for Arcanum taxonomy (13 intents, 18 techniques, 20 evasions)
- [ ] System prompt extraction tests exist and pass
  - Check: Tests verify system prompt cannot be extracted
  - Success: Zero successful extractions in all test cases

**Common Anti-Patterns to Flag**:
- ❌ Direct string concatenation: `f"You are a security assistant. {user_input}"`
- ❌ No input validation: Accepting all user input without sanitization
- ❌ Credentials in prompts: System prompt contains API keys, passwords
- ❌ Unbounded context: Accumulating unlimited conversation history
- ❌ Blind execution: Running LLM-generated code without validation
- ❌ No rate limiting: Unlimited LLM API calls per user
- ❌ Missing delimiters: System and user content in single string
- ❌ RAG poisoning: No document validation before knowledge base ingestion

**Review Success Criteria**:
- Zero high-severity prompt injection vulnerabilities
- All LLM integrations use structural prompt separation
- All user inputs validated, all outputs validated before execution
- No credentials/PII in system prompts
- Prompt injection test coverage ≥80% (intent×technique×evasion combinations)

**Reference**: See TA-Software, SR-Software, and ST-Software for threat analysis, requirements, and testing methodology.

---

### Key Success Indicators

**Outcome Metrics**:
1. **Defect Detection**: ≥80% of bugs caught in code review (before testing/production)
2. **Security Vulnerability Prevention**: ≥90% of security issues caught in review
3. **Review Coverage**: 100% of code changes reviewed before merge
4. **Test Coverage**: ≥80% unit test coverage for all production code

**Process Metrics**:
1. **Review Turnaround**: ≥95% of reviews completed within 2 business days
2. **Review Quality**: ≥3 substantive comments per 100 lines of code changed
3. **Rework Rate**: ≤20% of PRs require major rework after review
4. **Automated Check Pass Rate**: ≥90% of PRs pass automated checks first time

---

## Level 2: Comprehensive Implementation Review

**Enhanced Review Practices**:
- Threat modeling during code review (STRIDE analysis of code changes)
- Performance profiling (identify bottlenecks before production)
- Accessibility review (for UI components)
- Compliance code review (GDPR, HIPAA requirements in code)

---

## Level 3: Industry-Leading Implementation Review

**Advanced Practices**:
- AI-assisted code review (AI suggests improvements, detects patterns)
- Formal verification for critical code paths
- Continuous code quality dashboards
- Contribution to open-source secure coding standards

---

## Practice Integration

**Design Review (DR)**: IR validates implementation matches approved design
**Security Testing (ST)**: IR reviews test code, ST validates test effectiveness
**Secure Development (SD)**: IR enforces SD secure coding standards

---

## Conclusion

Implementation Review for Software ensures AI code security systems are correctly implemented with high quality and security. Level 1 establishes systematic peer review with comprehensive checklists and automated tools. Level 2 adds threat modeling and performance analysis. Level 3 achieves AI-assisted review and formal verification.

---

**Document Information**:
- **Practice**: Implementation Review (IR)
- **Domain**: Software
- **HAIAMM Version**: 2.0
- **Maturity Levels**: 3 (Foundational, Comprehensive, Industry-Leading)
- **Last Updated**: 2025-12-25
