# Implementation Review (IR) - Processes Domain
## HAIAMM Assessment Questionnaire v3.0

**Practice:** Implementation Review (IR)
**Domain:** Processes
**Purpose:** Assess organizational maturity in reviewing AI security orchestration and automated response implementations for safety, reliability, and effectiveness
**Version:** v3.0
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
**Objective:** Verify safety, reliability, and correctness of AI security orchestration implementations

### Question 1: ML Classification Model Review (Alert Triage)

**Q1.1:** Have you conducted a comprehensive code review of your ML-based alert triage classification model implementation, verifying model loading, feature extraction accuracy, preprocessing logic, inference correctness, and performance characteristics?

**Evidence Required:**
- [ ] Code review documentation covering model loading (pickle/joblib/ONNX), version checking, and deployment validation
- [ ] Feature extraction verification confirming correct extraction of source IP, destination IP, protocol, ports, user, timestamp, and alert metadata matching training feature order
- [ ] Preprocessing validation for input normalization, categorical encoding, and missing value handling
- [ ] Inference logic verification ensuring correct input shape, proper probability-to-label conversion, and output interpretation
- [ ] Performance testing results demonstrating inference latency ≤100ms per alert and batch processing ≥1,000 alerts/second
- [ ] Test results with known inputs, edge cases (malformed alerts, missing fields, extreme values)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Model inference latency p95 | ___ms | ___ms | ≤100ms | ☐ | |
| Batch processing throughput | ___alerts/sec | ___alerts/sec | ≥1,000 alerts/sec | ☐ | |
| % of test cases passing (known inputs + edge cases) | ___% | ___% | 100% | ☐ | |
| Code coverage of ML model implementation | ___% | ___% | ≥90% | ☐ | |

**Metric Collection Guidance:**
- **Model inference latency p95**: Measure time from model.predict() call to result return for 1,000+ sample alerts using performance profiling (cProfile, line_profiler); calculate 95th percentile; collect during load testing; frequency: weekly during development, monthly in production
- **Batch processing throughput**: Send batches of 1,000 alerts through model; measure total processing time; calculate alerts/second; use production alert samples or synthetic test data; frequency: weekly
- **% of test cases passing**: Count passing tests divided by total tests in model test suite; include unit tests for model loading, feature extraction, preprocessing, inference; run in CI/CD pipeline; frequency: every commit
- **Code coverage**: Use coverage.py (Python) or equivalent; run test suite with coverage instrumentation; report line coverage of model implementation code; frequency: every PR review

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of ML model code review)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### Question 2: Feature Extraction & Severity Scoring Review

**Q1.2:** Have you reviewed and validated the feature extraction, enrichment, and severity scoring algorithms used in your alert triage implementation, ensuring correct parsing, contextual enrichment, and severity adjustment logic?

**Evidence Required:**
- [ ] Alert parsing code review confirming correct JSON/XML parsing and graceful handling of malformed alerts
- [ ] Enrichment logic verification for threat intelligence (IP reputation), asset enrichment (criticality, owner, department)
- [ ] Feature engineering validation for time-based features (hour, day, business hours) and contextual features (user login frequency, first-time source IP)
- [ ] Severity scoring algorithm review confirming formula: final_score = base_severity × asset_criticality × exploitability × business_impact, normalized 0-100
- [ ] Edge case handling verification (missing context defaults, divide-by-zero protection)
- [ ] Validation test results comparing severity adjustments against expert assessments

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| % of alerts successfully parsed without errors | ___% | ___% | ≥99.5% | ☐ | |
| % of alerts successfully enriched with threat intel and asset data | ___% | ___% | ≥95% | ☐ | |
| Correlation between AI severity scores and expert assessments (Spearman's ρ) | ___ | ___ | ≥0.85 | ☐ | |
| % of edge cases handled gracefully without crashes | ___% | ___% | 100% | ☐ | |

**Metric Collection Guidance:**
- **% of alerts parsed successfully**: Monitor parsing exception rate in logs; calculate (total_alerts - parsing_errors) / total_alerts × 100%; collect from application logs or monitoring dashboard; frequency: daily
- **% of alerts enriched**: Track enrichment success rate; count alerts with populated enrichment fields / total alerts × 100%; query from alert database or SIEM; frequency: daily
- **Correlation with expert assessments**: Collect sample of 100+ alerts; have security experts manually score severity; calculate Spearman rank correlation between AI scores and expert scores using scipy.stats.spearmanr; frequency: quarterly
- **% of edge cases handled**: Create test suite of edge cases (null values, extreme values, malformed data); run tests; count passed / total × 100%; automate in CI/CD; frequency: every release

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of feature extraction review)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### Question 3: Orchestration Engine Review

**Q1.3:** Have you conducted a comprehensive review of your orchestration engine implementation, validating workflow DAG representation, parallel execution logic, state persistence, and crash recovery capabilities?

**Evidence Required:**
- [ ] DAG representation code review confirming correct adjacency list/matrix implementation, topological sorting, and cycle detection
- [ ] Parallel execution verification for independent steps (ThreadPoolExecutor/asyncio/Celery) and sequential execution of dependent steps
- [ ] Step execution code review confirming correct function/API invocation and parameter passing
- [ ] State persistence validation ensuring atomic database updates (PostgreSQL/MongoDB/Redis) after each step completion
- [ ] Resume logic testing demonstrating correct recovery from last completed step without duplicate actions
- [ ] Crash recovery test results showing successful workflow resumption after process termination

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| % of crash recovery tests passed (workflow resumes correctly without duplicates) | ___% | ___% | 100% | ☐ | |
| % reduction in execution time for workflows with parallel steps vs sequential | ___% | ___% | ≥40% | ☐ | |
| State persistence latency p95 (time to write state to database) | ___ms | ___ms | ≤200ms | ☐ | |
| % of workflows with cyclic dependencies detected and rejected | ___% | ___% | 100% | ☐ | |

**Metric Collection Guidance:**
- **% of crash recovery tests passed**: Create test suite that kills workflow process at random steps; attempt resume; verify correct step resumption and no duplicate actions; count successful tests / total tests × 100%; run in integration testing; frequency: every release
- **% reduction in execution time**: Measure execution time for workflows with parallelizable steps when run sequentially vs parallel; calculate (sequential_time - parallel_time) / sequential_time × 100%; test with representative workflows; frequency: quarterly
- **State persistence latency p95**: Instrument state write operations; measure time from step completion to database commit confirmation; calculate 95th percentile; collect from APM tool (New Relic, DataDog); frequency: weekly
- **% of cyclic workflows rejected**: Create test suite with workflows containing cycles; submit to orchestration engine; verify rejection; count rejections / total cyclic workflows × 100%; automate in unit tests; frequency: every commit

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of orchestration engine review)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### Question 4: Timeout, Retry & Error Handling Review

**Q1.4:** Have you reviewed the timeout, retry, circuit breaker, and error handling implementation in your orchestration workflows, ensuring proper failure classification, exponential backoff, and graceful degradation?

**Evidence Required:**
- [ ] Timeout implementation review confirming use of signal.alarm/asyncio.wait_for/threading.Timer and proper timeout trigger handling
- [ ] Retry logic verification showing exponential backoff (1s→2s→4s→8s→16s) with max 3-5 attempts configured
- [ ] Circuit breaker pattern implementation review tracking consecutive failures, open/half-open/closed state transitions
- [ ] Error classification logic confirming transient errors (timeout, rate limit) retry automatically while permanent errors (404, 401) fail immediately
- [ ] Fallback action testing and workflow continuation verification for non-critical step failures
- [ ] Test results demonstrating timeout handling, retry behavior, and circuit breaker state management

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| % of external API calls protected by timeout mechanisms | ___% | ___% | 100% | ☐ | |
| % of transient failures successfully resolved by retry logic | ___% | ___% | ≥85% | ☐ | |
| Circuit breaker activation rate (times/week during normal operations) | ___ | ___ | ≤5/week | ☐ | |
| % of workflows completing despite non-critical step failures | ___% | ___% | ≥90% | ☐ | |

**Metric Collection Guidance:**
- **% of API calls with timeout**: Code analysis to identify all external API calls; verify each has timeout parameter or wrapper; count protected calls / total calls × 100%; use static analysis tools; frequency: every release
- **% of transient failures resolved by retry**: Monitor retry attempts in logs; filter for transient error codes; calculate successful retries / total retry attempts × 100%; aggregate from application logs; frequency: weekly
- **Circuit breaker activation rate**: Count circuit breaker state transitions to "open" per week; query from monitoring system or application metrics; baseline during steady-state operations; frequency: weekly
- **% of workflows completing with failures**: Track workflows with at least one failed non-critical step that still completed; divide by total workflows with non-critical failures × 100%; query from workflow execution database; frequency: weekly

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of timeout/retry/error handling review)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### Question 5: Blast Radius & Safety Mechanisms Review

**Q1.5:** Have you reviewed the implementation of blast radius limits, graduated automation levels, pre-change validation, and post-change verification mechanisms to ensure safe execution of automated security actions?

**Evidence Required:**
- [ ] Hard-coded limit verification (MAX_IP_BLOCKS=50, MAX_ACCOUNT_DISABLES=20, MAX_HOST_ISOLATIONS=5) with enforcement code review
- [ ] Rate limiting implementation review tracking actions per hour/day with limit enforcement
- [ ] Critical asset exception handling confirmation (production servers require approval regardless of count)
- [ ] Graduated automation level configuration review: alert_only → recommend → auto_execute_reversible → auto_execute_irreversible
- [ ] Pre-change validation review: dry-run mode, precondition checks, impact assessment implementation
- [ ] Post-change verification review: state query implementation, success criteria validation, ≤30s timeout enforcement, rollback trigger on verification failure
- [ ] Test results demonstrating limit enforcement, level compliance, and verification accuracy

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| % of automated actions blocked by blast radius limits when appropriate | ___% | ___% | 100% (0% limit violations) | ☐ | |
| % of high-risk actions requiring approval at appropriate automation level | ___% | ___% | 100% | ☐ | |
| % of automated actions successfully verified post-execution | ___% | ___% | ≥98% | ☐ | |
| % of failed post-change verifications triggering automatic rollback | ___% | ___% | 100% | ☐ | |

**Metric Collection Guidance:**
- **% of actions blocked by limits**: Monitor limit violation attempts in logs; verify all violations blocked; calculate blocked_violations / total_violation_attempts × 100%; should be 100% (no violations pass through); collect from audit logs; frequency: daily
- **% of high-risk actions requiring approval**: Define high-risk actions (irreversible, critical assets); track approval workflow triggers; calculate high_risk_with_approval / total_high_risk × 100%; query from workflow database; frequency: weekly
- **% of actions verified**: Count automated actions with completed post-change verification / total automated actions × 100%; exclude manual actions; query from action execution logs; frequency: daily
- **% of failed verifications triggering rollback**: Track verification failures; confirm rollback initiated; calculate rollbacks_triggered / verification_failures × 100%; monitor from orchestration logs; frequency: weekly

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of safety mechanism review)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### Question 6: Rollback & Kill Switch Review

**Q1.6:** Have you reviewed the rollback action implementation and kill switch mechanism, ensuring proper inverse action logic, rollback triggers, validation, irreversible action handling, and emergency automation shutdown capabilities?

**Evidence Required:**
- [ ] Rollback action code review confirming correct inverse operations (block→unblock, disable→enable, isolate→de-isolate)
- [ ] Rollback trigger verification: verification failure, manual analyst request, adverse impact detection
- [ ] Rollback validation implementation ensuring state restoration confirmation through system queries
- [ ] Irreversible action handling review with proper flagging and documentation of non-rollbackable actions
- [ ] Kill switch implementation review: API endpoint/command availability, global AUTOMATION_DISABLED flag, graceful current-step completion
- [ ] Re-enable process validation requiring manager approval and root cause analysis documentation
- [ ] Test results demonstrating rollback execution, kill switch activation, and re-enable procedures

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| % of reversible automated actions with implemented and tested rollback procedures | ___% | ___% | 100% | ☐ | |
| Rollback success rate (state correctly restored) | ___% | ___% | ≥98% | ☐ | |
| Kill switch response time (from activation to automation stop) | ___sec | ___sec | ≤60 seconds | ☐ | |
| % of kill switch re-enable attempts requiring documented RCA | ___% | ___% | 100% | ☐ | |

**Metric Collection Guidance:**
- **% of actions with rollback procedures**: Inventory all reversible automated action types; verify each has implemented and tested rollback code; calculate actions_with_rollback / total_reversible_actions × 100%; audit code and test suites; frequency: quarterly
- **Rollback success rate**: Track rollback executions; verify state restoration through post-rollback verification; calculate successful_rollbacks / total_rollback_attempts × 100%; query from rollback execution logs; frequency: weekly
- **Kill switch response time**: During kill switch tests, measure time from activation API call to last new workflow blocked; use test environment; calculate median and p95; frequency: monthly testing
- **% of re-enable with RCA**: Track kill switch re-enable events; verify each has linked incident report or RCA document; calculate re_enables_with_RCA / total_re_enables × 100%; audit from change management system; frequency: per incident

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of rollback/kill switch review)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### Question 7: Tool Integration Review

**Q1.7:** Have you conducted comprehensive reviews of all security tool integrations (SIEM, EDR, firewall, IAM), verifying authentication, API correctness, request/response handling, error handling, data normalization, and credential management?

**Evidence Required:**
- [ ] Authentication review confirming credentials retrieved from secrets manager (HashiCorp Vault, AWS Secrets Manager) and correct API key/token formatting
- [ ] API endpoint verification for each integration (SIEM query: /api/search, EDR isolate: /api/v1/hosts/{id}/isolate, Firewall block: /api/policies/blocklist)
- [ ] Request construction validation: correct query syntax, filter expressions, action payloads, content-type headers
- [ ] Response parsing verification: correct JSON parsing, field extraction (query results, action confirmations, error messages)
- [ ] Per-integration error handling review: circuit breaker, retry logic, error classification, fallback mechanisms
- [ ] Data normalization code review: field mapping to common schema (OCSF/ECS), type conversion, missing field handling
- [ ] Credential management validation: runtime retrieval, rotation support, least privilege verification, no secrets in logs/code

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| % of tool integrations using secrets manager for credentials | ___% | ___% | 100% | ☐ | |
| % of tool integration API calls with successful response parsing | ___% | ___% | ≥99% | ☐ | |
| % of integrations with implemented circuit breaker and retry logic | ___% | ___% | 100% | ☐ | |
| Number of credential rotation events completed successfully in past 90 days | ___ | ___ | ≥1 per integration | ☐ | |

**Metric Collection Guidance:**
- **% using secrets manager**: Audit all tool integration configurations; verify credentials retrieved from secrets manager (not hardcoded, not environment variables); count compliant_integrations / total_integrations × 100%; code review and config audit; frequency: quarterly
- **% of successful response parsing**: Monitor API call response parsing in logs; calculate (total_api_calls - parsing_errors) / total_api_calls × 100%; aggregate from application monitoring; frequency: weekly
- **% with circuit breaker/retry**: Code review to verify each integration has circuit breaker and retry implementation; count protected_integrations / total_integrations × 100%; static analysis; frequency: every release
- **Credential rotation events**: Track credential rotation activities in secrets manager audit logs; count successful rotations per integration in past 90 days; query from Vault/AWS Secrets Manager logs; frequency: quarterly

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of tool integration review)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### Question 8: Human Oversight Review

**Q1.8:** Have you reviewed the implementation of human oversight mechanisms including approval workflows, escalation logic, override capabilities, and comprehensive audit logging for all automated security decisions and actions?

**Evidence Required:**
- [ ] Approval workflow code review: high-risk action triggers, approval request generation with action details and impact, workflow pause until approval, proper handling of approve/reject/timeout
- [ ] Escalation logic verification: severity threshold triggers, SLA breach detection, tier routing implementation (Critical→Tier 2), notification delivery
- [ ] Override mechanism review: support for classification/recommendation override, justification requirement enforcement, feedback to model training pipeline
- [ ] Audit logging implementation review: comprehensive action coverage (playbook executions, approvals, overrides, escalations), required field completeness (timestamp, user, action type, target, result, justification)
- [ ] Log storage validation: SIEM forwarding, immutability (write-once), ≥7 year retention compliance
- [ ] Audit trail testing confirming all critical actions logged with complete context

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| % of high-risk automated actions requiring and receiving approval | ___% | ___% | 100% | ☐ | |
| % of analyst overrides with documented justification | ___% | ___% | 100% | ☐ | |
| % of automated actions with complete audit log entries (all required fields) | ___% | ___% | ≥99.5% | ☐ | |
| Audit log retention compliance (years of historical logs available) | ___years | ___years | ≥7 years | ☐ | |

**Metric Collection Guidance:**
- **% of high-risk actions with approval**: Define high-risk action types; track executions requiring approval; verify approval received before execution; calculate approved_actions / total_high_risk_actions × 100%; query from workflow database; frequency: weekly
- **% of overrides with justification**: Track analyst override events; verify each has non-empty justification field; calculate overrides_with_justification / total_overrides × 100%; query from audit logs; frequency: weekly
- **% with complete audit logs**: Sample audit log entries; check for all required fields (timestamp, user, action_type, target, result, justification if override); calculate complete_entries / sampled_entries × 100%; automated validation script; frequency: weekly
- **Audit log retention**: Query oldest audit log entry timestamp; calculate years from oldest to current date; verify against retention policy; query from SIEM or log storage system; frequency: quarterly

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of human oversight review)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### Question 9: Resilience & Test Coverage Review

**Q1.9:** Have you reviewed the implementation of queue resilience, graceful degradation, health monitoring, and comprehensive test coverage including safety tests (≥95%), integration tests (≥90%), chaos tests, and performance validation?

**Evidence Required:**
- [ ] Queue implementation review: RabbitMQ/Kafka/SQS configuration, message persistence, capacity ≥10,000 messages, priority queue support
- [ ] Graceful degradation verification: ML model failure→rule-based fallback, tool failure→manual escalation, database failure→in-memory state mode
- [ ] Health monitoring review: service/model/integration metrics exposed, Prometheus/Grafana dashboards configured, anomaly alerts
- [ ] Safety test coverage analysis: blast radius limit tests, automation level enforcement tests, rollback tests, kill switch tests (≥95% coverage target)
- [ ] Integration test validation: per-integration tests, end-to-end workflow tests, error path coverage (≥90% target)
- [ ] Chaos testing results: failure injection scenarios (model failure, API failure, database failure, network issues), graceful degradation validation
- [ ] Performance test results: ≥1,000 alerts/min throughput, p95 ≤5min latency for Critical alerts, concurrency testing

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Safety mechanism test coverage | ___% | ___% | ≥95% | ☐ | |
| Integration test coverage | ___% | ___% | ≥90% | ☐ | |
| Alert processing throughput | ___alerts/min | ___alerts/min | ≥1,000 alerts/min | ☐ | |
| Critical alert end-to-end latency p95 | ___min | ___min | ≤5 minutes | ☐ | |

**Metric Collection Guidance:**
- **Safety mechanism test coverage**: Identify all safety mechanisms (limits, levels, rollbacks, kill switch); count test cases covering each; calculate covered_mechanisms / total_mechanisms × 100%; analyze test suite with coverage tools; frequency: every release
- **Integration test coverage**: Run integration test suite with coverage instrumentation; measure line coverage of integration code; use pytest-cov or similar; report coverage percentage; frequency: every PR
- **Alert processing throughput**: Load test with production-like alert volume; measure alerts processed per minute at steady state; use JMeter or custom load generator; calculate mean throughput; frequency: monthly
- **Critical alert latency p95**: Track end-to-end time from alert ingestion to action completion for Critical severity alerts; calculate 95th percentile latency; query from APM or workflow logs; frequency: weekly

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of resilience/test coverage review)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

**Level 1 Score:** _____ / 9 questions answered "Implemented" or better

**Level 1 Achieved:** ☐ Yes (9/9 at Implemented or Fully Mature) ☐ No

---

## Level 2: Advanced Implementation Review
**Objective:** Review advanced AI capabilities, stream processing, and rigorous testing methodologies

**Prerequisites:** ALL Level 1 questions must be "Implemented" or "Fully Mature" to proceed to Level 2

### Question 10: ML Model Explainability & Fairness Review

**Q2.1:** Have you reviewed the implementation of ML model explainability mechanisms (SHAP values, explainability UI, counterfactual explanations) and fairness testing (bias detection across protected classes, fairness metrics, mitigation strategies)?

**Evidence Required:**
- [ ] SHAP value generation code review: integration with model inference, feature contribution calculation for each prediction
- [ ] Explainability UI implementation review: analyst dashboard displaying top contributing features, confidence scores, decision rationale
- [ ] Counterfactual explanation generation: "what-if" scenario implementation showing how feature changes affect classification
- [ ] Bias testing implementation: accuracy measurement across protected classes (gender, race, age if applicable), disparate impact detection
- [ ] Fairness metrics calculation: demographic parity, equalized odds, calibration across groups
- [ ] Mitigation implementation: fairness constraints in model training, dataset rebalancing procedures
- [ ] Validation testing results confirming explainability accuracy and absence of discriminatory bias

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| % of ML predictions with generated SHAP values | ___% | ___% | ≥95% | ☐ | |
| Analyst satisfaction with explainability UI (survey score 1-5) | ___ | ___ | ≥4.0 | ☐ | |
| Maximum disparate impact ratio across protected classes | ___ | ___ | ≤1.2 (within 20%) | ☐ | |
| % of fairness metrics within acceptable thresholds | ___% | ___% | 100% (all metrics) | ☐ | |

**Metric Collection Guidance:**
- **% with SHAP values**: Monitor ML prediction events; count predictions with generated SHAP values / total predictions × 100%; track in model serving logs; frequency: daily
- **Analyst satisfaction**: Quarterly survey asking analysts to rate explainability UI usefulness (1=not useful, 5=very useful); calculate mean score; survey via Google Forms or internal tool; frequency: quarterly
- **Maximum disparate impact ratio**: For each protected class pair, calculate (selection_rate_group_A / selection_rate_group_B); find maximum ratio; should be ≤1.2; analyze using fairness testing framework (Fairlearn, AIF360); frequency: monthly
- **% of fairness metrics in threshold**: Define acceptable ranges for demographic parity (±0.1), equalized odds (±0.1), calibration (±0.05); calculate metrics; count in_threshold / total_metrics × 100%; run fairness audit script; frequency: monthly

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of explainability/fairness review)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### Question 11: Stream Processing & Event Sourcing Review

**Q2.2:** Have you reviewed the implementation of real-time stream processing architecture (Kafka Streams/Flink) including event processing, exactly-once semantics, state management, event sourcing, and property-based testing with formally defined invariants?

**Evidence Required:**
- [ ] Stream processing framework code review: Kafka Streams/Apache Flink/AWS Kinesis implementation, event ordering guarantees
- [ ] Exactly-once semantics verification: deduplication mechanisms, idempotent processing, transaction support
- [ ] Stateful processing review: windowing operations, aggregations, stream joins, state checkpointing
- [ ] Event sourcing implementation: append-only event log, state reconstruction from events, snapshot mechanisms for performance
- [ ] Event replay capability testing: state corruption recovery, historical analysis, debugging support
- [ ] Property-based testing implementation: Hypothesis framework usage, invariant definitions (risk score 0-100, workflow termination, deadlock freedom)
- [ ] Test results showing properties hold for ≥10,000 randomly generated inputs

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Event processing accuracy (exactly-once delivery rate) | ___% | ___% | ≥99.99% | ☐ | |
| State reconstruction success rate (from event replay) | ___% | ___% | 100% | ☐ | |
| Number of defined invariants tested with property-based testing | ___ | ___ | ≥5 invariants | ☐ | |
| % of property-based tests passing with 10,000+ random inputs | ___% | ___% | 100% | ☐ | |

**Metric Collection Guidance:**
- **Exactly-once delivery rate**: Monitor stream processing metrics; track duplicate processing events; calculate (total_events - duplicates) / total_events × 100%; query from Kafka/Flink metrics or application logs; frequency: daily
- **State reconstruction success rate**: Periodically trigger event replay to rebuild state; compare reconstructed state to current state; calculate successful_reconstructions / total_reconstruction_tests × 100%; automated testing weekly; frequency: weekly
- **Number of invariants**: Count distinct property-based test invariants in test suite (e.g., "risk_score_bounded", "workflow_terminates", "no_deadlocks", "state_consistency", "action_idempotency"); code review of Hypothesis tests; frequency: quarterly
- **% of property tests passing**: Run property-based test suite with Hypothesis; count tests with 100% pass rate across 10,000+ generated inputs; calculate passing_tests / total_property_tests × 100%; CI/CD pipeline; frequency: every commit

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of stream processing/event sourcing review)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### Question 12: Mutation Testing Review

**Q2.3:** Have you implemented mutation testing to assess test suite quality, achieving ≥80% overall mutation score and ≥90% mutation score for safety-critical code, with investigation and remediation of surviving mutants?

**Evidence Required:**
- [ ] Mutation testing tool configuration: mutmut (Python), PIT (Java), or Stryker (JavaScript) properly integrated into CI/CD
- [ ] Mutation score metrics: overall codebase mutation kill rate ≥80%, safety-critical code mutation kill rate ≥90%
- [ ] Safety-critical code identification: blast radius limits, automation levels, rollback logic, kill switch clearly marked
- [ ] Surviving mutant analysis: investigation reports for mutants not killed by tests
- [ ] Test improvements: new test cases added to kill previously surviving mutants
- [ ] Regular mutation testing execution in CI/CD pipeline

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Overall mutation score (% of mutants killed) | ___% | ___% | ≥80% | ☐ | |
| Safety-critical code mutation score | ___% | ___% | ≥90% | ☐ | |
| % of surviving mutants with documented investigation | ___% | ___% | 100% | ☐ | |
| Number of new tests added to kill surviving mutants in past quarter | ___ | ___ | ≥10 tests | ☐ | |

**Metric Collection Guidance:**
- **Overall mutation score**: Run mutation testing tool (mutmut/PIT/Stryker); calculate killed_mutants / total_mutants × 100%; extract from mutation testing report JSON/XML; frequency: weekly
- **Safety-critical mutation score**: Tag safety-critical code modules; run mutation testing with filter; calculate killed_mutants_critical / total_mutants_critical × 100%; use tool's filtering capabilities; frequency: weekly
- **% surviving mutants investigated**: Count surviving mutants with linked investigation issue or comment; divide by total surviving mutants × 100%; track in JIRA/GitHub issues; frequency: monthly
- **New tests added**: Track test commits with mutation testing tag/label; count new test cases added to kill mutants; query from version control and test suite analysis; frequency: quarterly

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of mutation testing)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

**Level 2 Score:** _____ / 3 questions answered "Implemented" or better

**Level 2 Achieved:** ☐ Yes (3/3 at Implemented or Fully Mature) ☐ No

---

## Level 3: Research-Grade Implementation Review
**Objective:** Verify formal verification, privacy-preserving federated learning, and autonomous incident response implementations

**Prerequisites:** ALL Level 2 questions must be "Implemented" or "Fully Mature" to proceed to Level 3

### Question 13: Formal Verification Review

**Q3.1:** Have you implemented formal verification for safety-critical components using TLA+ specifications and model checking, with verified implementation in languages like Dafny, F*, or Coq, demonstrating zero specification violations?

**Evidence Required:**
- [ ] TLA+ specifications for critical components: workflow execution engine, state management, safety mechanisms (blast radius limits, kill switch)
- [ ] TLC model checker results: no deadlocks detected, safety properties verified (limits never exceeded), liveness properties satisfied (workflows terminate)
- [ ] Implementation-to-specification mapping: traceability documentation showing code implements TLA+ spec
- [ ] Formally verified code: safety-critical subset implemented in Dafny/F*/Coq with discharged proof obligations
- [ ] Code extraction: verified code extracted to production language (OCaml, C, Rust) with correctness guarantees
- [ ] Verification regression testing: TLA+ model checking in CI/CD, re-verification on specification changes

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| % of safety-critical components with formal TLA+ specifications | ___% | ___% | 100% | ☐ | |
| Number of safety properties verified by TLC model checker | ___ | ___ | ≥10 properties | ☐ | |
| % of verified code proof obligations successfully discharged | ___% | ___% | 100% | ☐ | |
| Number of specification violations detected in production (past 12 months) | ___ | ___ | 0 violations | ☐ | |

**Metric Collection Guidance:**
- **% with TLA+ specs**: Inventory safety-critical components (from architecture documentation); count components with completed TLA+ spec files; calculate components_with_specs / total_critical_components × 100%; audit spec repository; frequency: quarterly
- **Number of verified properties**: Count distinct safety and liveness properties in TLA+ specifications that pass TLC model checking; extract from TLC output logs; examples: NoDeadlock, WorkflowsTerminate, LimitsNeverExceeded, StateConsistency; frequency: per release
- **% proof obligations discharged**: For verified code modules (Dafny/F*/Coq), count total proof obligations and successful discharges; calculate discharged / total × 100%; extract from verification tool output; frequency: per release
- **Specification violations in production**: Monitor production incidents; identify violations of formally specified invariants; count incidents; should be zero; track in incident management system with "formal-verification" tag; frequency: monthly review

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of formal verification)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### Question 14: Federated Learning Review

**Q3.2:** Have you implemented privacy-preserving federated learning to train AI models across multiple organizations without sharing raw data, with differential privacy guarantees (ε≤1.0) and secure multi-party computation for gradient aggregation?

**Evidence Required:**
- [ ] Federated learning architecture: multi-organization model training infrastructure without raw data sharing
- [ ] Differential privacy implementation: ε-differential privacy with ε≤1.0, privacy budget tracking, noise injection mechanisms
- [ ] Secure aggregation: secure multi-party computation (SMPC) protocol implementation ensuring no single party sees individual gradients
- [ ] Privacy guarantees verification: formal privacy analysis, privacy budget accounting, privacy leakage testing
- [ ] Model performance comparison: federated model accuracy vs single-organization baseline, minimum ≥10% improvement target
- [ ] Participant organizations: ≥3 organizations participating in federated training

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Differential privacy epsilon (ε) value | ___ | ___ | ≤1.0 | ☐ | |
| Model accuracy improvement vs single-org baseline | ___% | ___% | ≥10% improvement | ☐ | |
| Number of organizations participating in federated training | ___ | ___ | ≥3 orgs | ☐ | |
| % of privacy leakage tests passed (no data reconstruction possible) | ___% | ___% | 100% | ☐ | |

**Metric Collection Guidance:**
- **Differential privacy ε**: Calculate cumulative privacy budget (ε) from all federated learning rounds using privacy accounting mechanisms (Rényi DP, moments accountant); extract from federated learning framework logs; verify ε≤1.0; frequency: per training cycle
- **Accuracy improvement**: Baseline: train model on single organization's data; Federated: train on all organizations' data via federated learning; compare accuracy metrics; calculate (federated_accuracy - baseline_accuracy) / baseline_accuracy × 100%; test on hold-out dataset; frequency: quarterly
- **Number of participating orgs**: Count distinct organizations contributing data/gradients to federated training; verify active participation (not just registered); query from federated learning coordination server; frequency: monthly
- **% privacy tests passed**: Run privacy leakage attack suite (membership inference, model inversion, gradient leakage attacks); verify all attacks fail to reconstruct data; calculate passed_tests / total_tests × 100%; security research team testing; frequency: quarterly

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of federated learning)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### Question 15: Autonomous Incident Response Review

**Q3.3:** Have you implemented LLM-powered autonomous incident investigation and response capabilities, with automated log querying, event correlation, hypothesis formation, containment decisions with confidence scores, and human oversight for low-confidence scenarios?

**Evidence Required:**
- [ ] LLM investigation workflow implementation: automated log querying, event correlation across multiple data sources, hypothesis formation
- [ ] Autonomous decision-making: LLM generates containment decisions (block IP, isolate host, disable account) with confidence scores
- [ ] Confidence-based escalation: high-confidence decisions (≥95%) auto-execute, low-confidence (<95%) escalate to analyst
- [ ] Human oversight integration: analyst review interface, override capabilities, feedback mechanisms
- [ ] Performance validation: comparison of autonomous decisions against expert analyst decisions on historical incidents
- [ ] Minimum performance thresholds: ≥50% incidents fully autonomous, ≥95% decision accuracy vs experts

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| % of incidents handled fully autonomously (no human intervention) | ___% | ___% | ≥50% | ☐ | |
| Decision accuracy vs expert analysts (on historical incident validation set) | ___% | ___% | ≥95% | ☐ | |
| Mean time to containment for autonomous incidents | ___min | ___min | ≤15 minutes | ☐ | |
| % of low-confidence decisions correctly escalated to humans | ___% | ___% | 100% | ☐ | |

**Metric Collection Guidance:**
- **% fully autonomous**: Track incident investigations from start to resolution; count incidents with zero human interventions / total incidents × 100%; exclude incidents requiring approval by design; query from incident management system; frequency: weekly
- **Decision accuracy vs experts**: Create validation set of 100+ historical incidents with known-good expert decisions; run LLM through same incidents; compare decisions (correct action, correct target, correct timing); calculate matching_decisions / total_decisions × 100%; quarterly evaluation
- **Mean time to containment**: For autonomous incidents, measure time from incident detection to first containment action executed; calculate mean across all autonomous incidents; query from incident timestamps; frequency: weekly
- **% low-confidence escalated**: Track LLM decisions with confidence <95%; verify each triggered analyst escalation (no auto-execution); calculate properly_escalated / total_low_confidence × 100%; audit from workflow logs; frequency: weekly

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of autonomous incident response)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

**Level 3 Score:** _____ / 3 questions answered "Implemented" or better

**Level 3 Achieved:** ☐ Yes (3/3 at Implemented or Fully Mature) ☐ No

---

## Scoring Methodology

### Per-Question Scoring

Each question is scored on a 4-tier scale based on **Evidence Completeness** and **Outcome Metrics Achievement**:

| Tier | Score | Criteria |
|------|-------|----------|
| **Fully Mature** | 1.0 | Evidence complete + ≥75% of metrics meet targets (≥3 of 4 metrics met) |
| **Implemented** | 0.67 | Evidence complete + 50-74% of metrics meet targets (2 of 4 metrics met) |
| **Partial** | 0.33 | Evidence partially complete + <50% metrics meet targets (<2 metrics met) |
| **Not Implemented** | 0.0 | No evidence of implementation or review |

### Level Scoring

**Level 1:** Sum of scores for Q1.1 through Q1.9 (maximum: 9.0)
- **Level 1 gate:** ALL 9 questions must score ≥0.67 (Implemented or Fully Mature) to unlock Level 2

**Level 2:** Sum of scores for Q2.1 through Q2.3 (maximum: 3.0)
- **Gated by Level 1:** Can only score Level 2 if Level 1 gate achieved (all L1 ≥0.67)
- **Level 2 gate:** ALL 3 questions must score ≥0.67 (Implemented or Fully Mature) to unlock Level 3

**Level 3:** Sum of scores for Q3.1 through Q3.3 (maximum: 3.0)
- **Gated by Level 2:** Can only score Level 3 if Level 2 gate achieved (all L2 ≥0.67)

### Practice Score Calculation

**Implementation Review (IR) - Processes Domain Total Score:**

```
IR_Processes_Score = Level_1_Score + Level_2_Score + Level_3_Score
Maximum Possible Score: 15.0 (9.0 + 3.0 + 3.0)
```

### Maturity Interpretation

| Score Range | Maturity Level | Interpretation |
|-------------|----------------|----------------|
| 0.0 - 2.9 | **Initial** | Minimal implementation review processes; significant gaps in validation |
| 3.0 - 5.9 | **Developing** | Some implementation reviews conducted; incomplete coverage |
| 6.0 - 8.9 | **Comprehensive** | Solid Level 1 implementation review practices; systematic validation |
| 9.0 - 11.9 | **Advanced** | Level 1 fully mature + Level 2 practices; advanced review techniques |
| 12.0 - 14.9 | **Leading** | Levels 1-2 fully mature + Level 3 practices emerging; research-grade methods |
| 15.0 | **Research-Grade** | All levels fully mature; formal verification and autonomous systems validated |

### Worked Example Calculation

**Example Organization Scores:**

**Level 1 Questions (Q1.1 - Q1.9):**
- Q1.1 (ML Model Review): Fully Mature = 1.0
- Q1.2 (Feature Extraction): Implemented = 0.67
- Q1.3 (Orchestration): Fully Mature = 1.0
- Q1.4 (Timeout/Retry): Implemented = 0.67
- Q1.5 (Safety Mechanisms): Fully Mature = 1.0
- Q1.6 (Rollback/Kill Switch): Fully Mature = 1.0
- Q1.7 (Tool Integration): Implemented = 0.67
- Q1.8 (Human Oversight): Fully Mature = 1.0
- Q1.9 (Resilience/Testing): Implemented = 0.67

**Level 1 Score:** 1.0 + 0.67 + 1.0 + 0.67 + 1.0 + 1.0 + 0.67 + 1.0 + 0.67 = **7.68**
**Level 1 Gate:** ✓ Achieved (all ≥0.67) → Level 2 unlocked

**Level 2 Questions (Q2.1 - Q2.3):**
- Q2.1 (Explainability/Fairness): Implemented = 0.67
- Q2.2 (Stream Processing): Partial = 0.33
- Q2.3 (Mutation Testing): Implemented = 0.67

**Level 2 Score:** 0.67 + 0.33 + 0.67 = **1.67**
**Level 2 Gate:** ✗ Not achieved (Q2.2 <0.67) → Level 3 locked

**Level 3 Questions (Q3.1 - Q3.3):**
- Cannot score (Level 2 gate not achieved)

**Level 3 Score:** **0.0** (locked)

**Total IR-Processes Score:** 7.68 + 1.67 + 0.0 = **9.35**
**Maturity Level:** **Advanced** (9.0 - 11.9 range)

---

**Document Information:** Practice: Implementation Review (IR) | Domain: Processes | HAIAMM v3.0 | Last Updated: 2026-02-21
