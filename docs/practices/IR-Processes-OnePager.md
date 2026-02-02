# Implementation Review Practice – Processes Domain
## HAIAMM v2.0 One-Pager

### Practice Overview

Implementation Review for Processes ensures AI security orchestration implementations are safe, reliable, and maintain system stability while enabling rapid incident response.

---

### Level 1: Key Review Criteria

**Alert Triage Implementation**:
- [ ] **ML Classification Model Code Review**: Verify model implementation correctness
  - Model Loading: Model loaded from file (pickle, joblib, ONNX), version checked (ensure correct model version deployed)
  - Feature Extraction: Code extracts features correctly (source IP, destination IP, protocol, ports, user, timestamp, alert metadata), matches training feature order
  - Preprocessing: Input normalization (scale numeric features), encoding (categorical → numeric), missing value handling (impute or flag)
  - Inference: Model inference code correct (predict method called with correct input shape), output correctly interpreted (probabilities → class labels)
  - Performance: Inference latency ≤100ms per alert (real-time triage), batch processing for high volume (≥1,000 alerts/second)
  - Validation: Test with known inputs (verify correct classifications), edge cases (malformed alerts, missing fields, extreme values)
- [ ] **Feature Extraction Code Review**: Verify feature engineering correctness
  - Alert Parsing: Code parses alert JSON/XML correctly, handles malformed alerts gracefully (log error, skip alert)
  - Enrichment: Threat intel enrichment (IP reputation lookup, domain age, geolocation), asset enrichment (criticality, owner, department)
  - Feature Engineering: Time-based features (hour of day, day of week, business hours flag), contextual features (user login frequency, first-time source IP)
  - Error Handling: Enrichment API failures handled gracefully (use cached data, proceed without enrichment, don't crash)
  - Validation: Test feature extraction with sample alerts, verify all features populated correctly
- [ ] **Severity Scoring Algorithm Review**: Verify severity adjustment logic
  - Base Severity: Extracted from alert metadata (Critical, High, Medium, Low)
  - Context Adjustment: Code correctly applies multipliers (asset criticality × exploitability × business impact)
  - Scoring Formula: `final_score = base_severity * asset_criticality * exploitability * business_impact`, scores normalized to 0-100
  - Edge Cases: Handle missing context (default to medium criticality), divide-by-zero (protect against zero multipliers)
  - Validation: Test with various inputs, verify severity adjustments correct, spot-check against expert assessments
- [ ] **Priority Assignment Logic Review**: Verify queueing logic
  - Priority Calculation: Code calculates priority correctly (severity + age + resource_availability + analyst_expertise)
  - Queue Implementation: Priority queue correctly implemented (higher priority alerts dequeue first), FIFO within same priority
  - Starvation Prevention: Low-priority alerts escalate after threshold (age >24 hours → escalate priority)
  - SLA Integration: Alerts approaching SLA deadline auto-escalate (time remaining <20% of SLA)
  - Validation: Test priority queue (insert various priority alerts, verify dequeue order correct)

**Orchestration Engine Implementation**:
- [ ] **Workflow Execution Code Review**: Verify orchestration implementation
  - DAG Representation: Workflow graph correctly represented (nodes = actions, edges = dependencies), stored as adjacency list or matrix
  - Topological Sort: Code correctly orders workflow steps (dependencies executed before dependents), detects cycles (reject cyclic workflows)
  - Parallel Execution: Independent steps execute in parallel (ThreadPoolExecutor, asyncio, Celery), dependent steps execute sequentially
  - Step Execution: Each step correctly invoked (function call, API call, tool integration), parameters passed correctly
  - Validation: Test with various workflows (linear, branching, diamond dependencies), verify correct execution order
- [ ] **State Persistence Code Review**: Verify state management implementation
  - State Storage: Workflow state persisted to database (PostgreSQL, MongoDB, Redis) after each step completion
  - State Fields: Current step ID, completed step IDs, pending step IDs, step outputs (serialized JSON), error history, execution metadata
  - Atomicity: State updates atomic (use database transactions), prevent partial state writes
  - Resume Logic: Code correctly resumes from last completed step (query database for workflow state, skip completed steps, execute pending steps)
  - Validation: Test crash recovery (kill process mid-workflow, restart, verify resumes correctly without duplicate actions)
- [ ] **Timeout and Retry Logic Review**: Verify failure handling implementation
  - Timeout Implementation: Each step has timeout (using signal.alarm, asyncio.wait_for, threading.Timer), timeout triggers error handler
  - Retry Logic: Exponential backoff correctly implemented (delays: 1s, 2s, 4s, 8s, 16s), max retries enforced (3-5 attempts)
  - Circuit Breaker: Circuit breaker pattern implemented (track consecutive failures, open circuit after threshold, close after cooldown)
  - Error Classification: Transient errors (timeout, rate limit) retry automatically, permanent errors (404, 401) fail immediately without retry
  - Validation: Test timeout handling (mock slow API), test retry logic (mock transient failures), test circuit breaker (mock persistent failures)
- [ ] **Error Handling Code Review**: Verify graceful degradation implementation
  - Exception Handling: All external calls wrapped in try-except (API calls, database operations, file I/O)
  - Error Propagation: Errors propagated correctly (step failure triggers workflow error handler), error context preserved (stack trace, error message)
  - Fallback Actions: Fallback logic implemented (if EDR fails, try firewall), fallback correctly triggered on primary failure
  - Workflow Continuation: Non-critical step failures don't abort workflow (mark step failed, continue with remaining steps)
  - Validation: Test error handling (inject failures at various points), verify workflow doesn't crash, verify error logging

**Safety Mechanisms Implementation**:
- [ ] **Blast Radius Limits Code Review**: Verify impact containment enforcement
  - Hard-Coded Limits: Maximum values defined as constants (MAX_IP_BLOCKS=50, MAX_ACCOUNT_DISABLES=20, MAX_HOST_ISOLATIONS=5)
  - Enforcement: Code checks action scope against limits before execution (if ip_count > MAX_IP_BLOCKS: raise SafetyViolation)
  - Rate Limiting: Track actions per time period (actions_per_hour, actions_per_day), enforce daily/hourly limits
  - Exception Handling: Critical asset exceptions enforced (production servers require approval regardless of count)
  - Validation: Test limit enforcement (attempt action exceeding limit, verify rejection), test rate limiting
- [ ] **Graduated Automation Levels Code Review**: Verify automation maturity implementation
  - Level Configuration: Each action has automation level attribute (level: "alert_only" | "recommend" | "auto_execute_reversible" | "auto_execute_irreversible")
  - Level Enforcement: Code correctly enforces level (Level 0: notify only, Level 1: await approval, Level 2/3: execute automatically with appropriate checks)
  - Approval Integration: Level 1 actions trigger approval workflow, execution blocked until approval received
  - Override Support: Analysts can override automation level per action (force manual approval for normally-automated action)
  - Validation: Test each automation level (verify correct behavior per level), test approval workflows
- [ ] **Pre-Change Validation Code Review**: Verify impact assessment implementation
  - Dry-Run Mode: Code supports simulation mode (execute workflow without applying changes), simulated results returned to analyst
  - Precondition Checks: Code validates preconditions before action (host reachable, account active, firewall rule doesn't exist)
  - Impact Assessment: Code estimates impact (network blocks: estimate affected users, account disables: check user activity, host isolations: check running services)
  - Simulation Accuracy: Dry-run results match actual execution (no discrepancies between simulation and reality)
  - Validation: Test dry-run mode (run workflow in simulation, verify no actual changes), test precondition checks
- [ ] **Post-Change Verification Code Review**: Verify success confirmation implementation
  - Verification Queries: After action execution, code queries system state (firewall: verify IP blocked, AD: verify account disabled, EDR: verify host isolated)
  - Success Criteria: Clear success criteria defined per action type (IP in firewall block list, account status = disabled, host isolation state = true)
  - Timeout: Verification has timeout (≤30 seconds), timeout treated as verification failure
  - Failure Handling: Verification failure triggers rollback (if action claims success but verification fails, attempt rollback)
  - Validation: Test verification logic (execute action, verify success detection), test failure detection (mock failed action)
- [ ] **Rollback Code Review**: Verify undo implementation
  - Rollback Actions: Inverse actions correctly implemented (block IP → unblock IP, disable account → enable account, isolate host → de-isolate host)
  - Rollback Triggers: Code correctly triggers rollback (post-change verification failed, analyst manual rollback request, automated rollback on adverse impact)
  - Rollback Validation: Rollback success verified (query system state after rollback, confirm restored to pre-action state)
  - Irreversible Action Handling: Irreversible actions (delete files, reset passwords) flagged as non-rollbackable, documented
  - Validation: Test rollback for all reversible actions (execute action, rollback, verify state restored), verify irreversible actions cannot rollback
- [ ] **Kill Switch Code Review**: Verify emergency stop implementation
  - Kill Switch Endpoint: API endpoint or command for kill switch activation (POST /api/killswitch, CLI command soar-kill-switch)
  - Effect: Kill switch immediately sets global flag (AUTOMATION_DISABLED=True), all playbook execution checks flag before proceeding
  - Graceful Shutdown: In-flight workflows complete current step (atomic), new workflows blocked from starting
  - Re-Enable Process: Requires privileged action to re-enable (manager approval, audit log entry), includes root cause analysis requirement
  - Validation: Test kill switch (activate, verify automation stops), test re-enable process (verify approval required)

**Tool Integration Implementation**:
- [ ] **API Integration Code Review**: Verify tool integration correctness per tool
  - Authentication: Credentials retrieved from secrets manager (HashiCorp Vault, AWS Secrets Manager), API keys/tokens correctly formatted in headers
  - API Endpoints: Correct endpoints used (SIEM query: /api/search, EDR isolate: /api/v1/hosts/{id}/isolate, Firewall block: /api/policies/blocklist)
  - Request Construction: Request parameters correctly constructed (query syntax, filter expressions, action payloads), content-type headers correct (application/json)
  - Response Parsing: Response JSON correctly parsed, relevant fields extracted (query results, action confirmation, error messages)
  - Validation: Test each integration with real API (or mock), verify correct requests sent, verify responses correctly handled
- [ ] **Error Handling Per Integration Review**: Verify integration resilience
  - Circuit Breaker: Each integration has circuit breaker (track failures, open after 5 consecutive failures, close after 5-minute cooldown)
  - Retry Logic: Exponential backoff implemented per integration (1s, 2s, 4s, 8s, 16s), max retries enforced
  - Error Classification: HTTP errors correctly classified (500/503 = transient → retry, 401/404 = permanent → fail immediately)
  - Fallback: Fallback logic implemented (if primary tool fails, try backup tool), fallback correctly triggered
  - Validation: Test error handling per integration (mock API failures, network timeouts, rate limits), verify retry/fallback logic
- [ ] **Data Normalization Code Review**: Verify schema transformation
  - Field Mapping: Tool-specific fields correctly mapped to common schema (OCSF, ECS), mapping logic correct (nested field extraction, type conversion)
  - Missing Field Handling: Code handles missing fields gracefully (use default values, omit optional fields, don't crash)
  - Type Conversion: Data types correctly converted (timestamp strings → datetime objects, IP strings → IP address objects)
  - Validation: Test normalization with sample data from each tool, verify all fields correctly mapped, verify no data loss
- [ ] **Credential Management Review**: Verify secure credential handling
  - Secrets Storage: API keys stored in secrets manager (not hardcoded, not in config files, not in environment variables directly)
  - Secrets Retrieval: Code retrieves secrets at runtime (on-demand, cached for limited time), secrets never logged
  - Secrets Rotation: Code supports credential rotation (no hardcoded credentials, fetch fresh credentials on each use or cache with TTL)
  - Least Privilege: API keys have minimal required permissions (read-only for queries, write permissions only for action APIs)
  - Validation: Review secrets management code, verify no secrets in codebase (git log, environment files), test rotation support

**Human Oversight Implementation**:
- [ ] **Approval Workflow Code Review**: Verify human-in-the-loop implementation
  - Approval Trigger: High-risk actions correctly trigger approval workflow (delete files, reset passwords, disable critical accounts)
  - Approval Request: Approval request sent to analyst (via API, email, Slack), includes action details (what, why, estimated impact)
  - Approval Wait: Workflow pauses until approval received (blocks execution, timeout after configured period)
  - Approval Decision: Code correctly handles approval (approved → continue execution, rejected → abort workflow, timeout → queue for manual review)
  - Validation: Test approval workflow (trigger high-risk action, verify approval request sent, test approve/reject/timeout paths)
- [ ] **Escalation Logic Code Review**: Verify tiered escalation implementation
  - Escalation Triggers: Code correctly triggers escalation (severity threshold, SLA breach, analyst request)
  - Tier Routing: Alerts correctly routed to appropriate tier (Critical → Tier 2, SLA breach → escalate one tier)
  - Escalation Notification: Escalation notifications sent correctly (email, Slack, PagerDuty), include escalation reason
  - Escalation Tracking: Escalations logged (who, when, why, outcome), metrics tracked (escalation rate, resolution time per tier)
  - Validation: Test escalation triggers, verify correct tier routing, verify notifications sent
- [ ] **Override Mechanism Code Review**: Verify analyst override implementation
  - Override Types: Code supports all override types (override AI classification, override recommendation, disable automation for specific playbook)
  - Override Justification: Override requires justification (required field in UI/API), justification captured and logged
  - Override Effect: Override correctly applied (workflow execution reflects override, AI decision ignored)
  - Override Tracking: All overrides logged (who, what, when, why), fed back to model training pipeline
  - Validation: Test override workflows (submit override, verify applied correctly), verify logging comprehensive
- [ ] **Audit Logging Code Review**: Verify comprehensive logging
  - Log Coverage: All actions logged (playbook executions, approvals, overrides, escalations, automation decisions)
  - Log Fields: Logs include required fields (timestamp, user, action type, target, result, justification if applicable)
  - Log Storage: Logs persisted to SIEM or log aggregation system (Splunk, Elasticsearch), immutable (write-once)
  - Log Retention: Logs retained per compliance requirements (≥7 years for security logs)
  - Validation: Review logging code, verify all actions logged, verify log fields complete, test log ingestion to SIEM

**Resilience Implementation**:
- [ ] **Queue Implementation Review**: Verify message queue robustness
  - Queue Technology: Queue implementation reviewed (RabbitMQ, Kafka, Redis Streams, AWS SQS), appropriate for scale
  - Persistence: Queue messages persisted to disk (survive restarts), messages not lost on crash
  - Capacity: Queue capacity sufficient (≥10,000 messages), backpressure handled (reject new messages when full, alert on high queue depth)
  - Priority: Priority queue implemented (Critical alerts bypass queue, processed first)
  - Validation: Load test queue (inject 10,000 messages), verify no message loss, measure throughput
- [ ] **Graceful Degradation Code Review**: Verify failure mode handling
  - AI Model Failure: Code falls back to rule-based triage when ML model unavailable, alerts sent on model downtime
  - Tool Failure: Code continues workflow with available tools when integration fails, marks failed tool actions as manual
  - Database Failure: Code operates in degraded mode when state database unavailable (in-memory state only, alert on database outage)
  - Degradation Alerts: Code alerts when operating in degraded mode, specifies what's degraded
  - Validation: Test each degradation scenario (kill model, kill tool API, kill database), verify graceful fallback
- [ ] **Health Monitoring Code Review**: Verify observability implementation
  - Service Health Metrics: Code exposes health metrics (uptime, API response time, queue depth, throughput), metrics scraped by Prometheus/CloudWatch
  - Model Performance Metrics: ML model metrics exposed (accuracy, precision, recall, inference latency), tracked over time
  - Integration Health: Each integration's health tracked (API availability, response time, error rate, circuit breaker state)
  - Dashboard: Metrics visualized in dashboard (Grafana, Datadog), alerts configured for anomalies
  - Validation: Review metrics collection code, verify all critical metrics tracked, test dashboard (simulate failures, verify alerts)
- [ ] **Circuit Breaker Code Review**: Verify circuit breaker implementation
  - State Management: Circuit breaker state correctly managed (closed → open after threshold failures, open → half-open after timeout, half-open → closed after success)
  - Failure Tracking: Consecutive failures correctly tracked per integration, reset on success
  - Threshold Configuration: Failure threshold configurable (default: 5 failures), timeout configurable (default: 5 minutes)
  - Open Circuit Behavior: When circuit open, calls fail fast (don't attempt API call, immediately return error)
  - Validation: Test circuit breaker (trigger consecutive failures, verify circuit opens, verify cooldown, verify circuit closes on success)

**Test Coverage**:
- [ ] **Safety Tests Review**: Verify safety validation testing
  - Blast Radius Tests: Test that limits are enforced (attempt to block 100 IPs, verify rejection at 50), test rate limiting
  - Automation Level Tests: Test graduated automation (verify Level 0 doesn't execute, Level 1 requires approval, Level 2 auto-executes)
  - Rollback Tests: Test rollback for all reversible actions (block then unblock, disable then enable, isolate then de-isolate)
  - Kill Switch Tests: Test emergency stop (activate kill switch, verify all automation halts, test re-enable process)
  - Coverage: ≥95% of safety mechanisms tested, zero safety bypasses possible
- [ ] **Integration Tests Review**: Verify tool integration testing
  - Per-Integration Tests: Each tool integration tested (SIEM query, EDR isolate, Firewall block, IAM disable, Ticket create)
  - End-to-End Tests: Complete workflows tested (phishing response: SIEM query → EDR isolate → Firewall block → Ticket create)
  - Error Path Tests: Error handling tested per integration (API timeout, rate limit, authentication failure, malformed response)
  - Mock vs Real: Critical integrations tested against real APIs (production or staging), low-risk integrations can use mocks
  - Coverage: ≥90% of tool integrations tested, all critical workflows tested end-to-end
- [ ] **Chaos Tests Review**: Verify resilience testing
  - Failure Injection: Tests inject failures (kill AI model, kill tool API, kill database, network partition, high latency)
  - Graceful Degradation Validation: Tests verify system continues operating (degraded functionality acceptable, no crashes)
  - Recovery Validation: Tests verify system recovers when failures resolve (services restart, state restored, automation resumes)
  - Chaos Schedule: Chaos tests run regularly (weekly in staging, monthly in production during maintenance window)
  - Coverage: All failure scenarios tested, graceful degradation verified for each
- [ ] **Performance Tests Review**: Verify scalability testing
  - Throughput Tests: Test alert processing throughput (inject 10,000 alerts, measure processing rate, target: ≥1,000 alerts/minute)
  - Latency Tests: Measure end-to-end latency (alert arrival to action execution, target: p95 ≤5 minutes for Critical alerts)
  - Concurrency Tests: Test concurrent workflow executions (run 100 workflows simultaneously, verify no deadlocks, no race conditions)
  - Load Tests: Test system under sustained load (sustained high alert volume for 24 hours, verify no performance degradation)
  - Coverage: Performance targets validated, bottlenecks identified and documented

**Success Indicators**:
- **Safety Validated**: Zero production outages from AI automation in testing, ≤1% rollback rate, blast radius limits never exceeded
- **Code Quality**: ≥80% code coverage, zero critical security vulnerabilities (SAST scan), zero hardcoded secrets
- **Reliability**: ≥99.9% workflow completion rate, state persistence verified (100% crash recovery tests pass)
- **Performance**: MTTR reduction ≥50% vs. manual response, alert processing throughput ≥1,000 alerts/minute, p95 latency ≤5 minutes
- **Integration Quality**: ≥90% of tool integrations tested, all critical workflows tested end-to-end
- **Test Coverage**: ≥95% of safety mechanisms tested, ≥90% integration test coverage, chaos tests pass for all failure scenarios

---

### Level 2: Advanced Implementation Review

**AI Model Implementation Review**:
- [ ] **Model Explainability**: Review AI decision transparency implementation
  - SHAP Values: Code generates SHAP values for each prediction (explains feature contributions to decision)
  - Explainability UI: Analyst dashboard shows why AI made decision (top contributing features, confidence score)
  - Counterfactual Explanations: Code generates counterfactuals ("if feature X changed to Y, classification would flip")
  - Validation: Test explainability (verify SHAP values correct, verify UI displays explanations correctly)
- [ ] **Model Fairness**: Review bias mitigation implementation
  - Bias Testing: Code tests model for bias (measure accuracy across protected classes, detect disparate impact)
  - Fairness Metrics: Demographic parity, equalized odds, calibration across groups
  - Mitigation: If bias detected, model retrained with fairness constraints or dataset rebalanced
  - Validation: Test fairness metrics, verify no discriminatory bias in production model

**Stream Processing Implementation Review**:
- [ ] **Real-Time Processing**: Review streaming architecture implementation
  - Stream Processing Framework: Kafka Streams, Apache Flink, AWS Kinesis reviewed for correctness
  - Event Processing: Events processed in order, exactly-once semantics enforced (no duplicate processing)
  - State Management: Stateful processing correctly implemented (windowing, aggregation, join operations)
  - Validation: Test stream processing (inject events, verify correct processing, verify exactly-once delivery)
- [ ] **Event Sourcing**: Review event sourcing implementation
  - Event Store: All state changes stored as events (append-only log), state reconstructable from events
  - Event Replay: Code supports event replay (reprocess events to rebuild state), snapshots for performance
  - Validation: Test event replay (corrupt state, rebuild from events, verify correctness)

**Property-Based Testing Review**:
- [ ] **Hypothesis Testing**: Review property-based test implementation
  - Properties Defined: Invariants defined (risk score always 0-100, workflows always terminate, no deadlocks possible)
  - Hypothesis Framework: Tests use Hypothesis library (generates random inputs, tests properties hold)
  - Test Coverage: Properties tested with ≥10,000 randomly generated inputs
  - Validation: Review properties (ensure comprehensive), verify tests pass, investigate failures

**Mutation Testing Review**:
- [ ] **Test Quality Assessment**: Review mutation testing implementation
  - Mutation Tool: mutmut (Python), PIT (Java), Stryker (JavaScript) configured correctly
  - Mutation Score: ≥80% of mutations detected by tests (kill rate ≥0.80)
  - Critical Path Focus: Safety-critical code has ≥90% mutation score
  - Validation: Run mutation testing, review surviving mutants, add tests to kill them

**Success Indicators - Level 2**:
- **Model Explainability**: SHAP values generated for ≥95% of predictions, analyst satisfaction ≥80% with explanations
- **Model Fairness**: Zero statistically significant bias detected across protected classes
- **Stream Processing**: Exactly-once semantics verified, ≥99.99% event processing accuracy
- **Property-Based Testing**: All invariants hold for ≥10,000 random inputs
- **Mutation Testing**: ≥80% overall mutation score, ≥90% on safety-critical code

---

### Level 3: Research-Grade Implementation Review

**Formal Verification Review**:
- [ ] **TLA+ Specification**: Review formal specification implementation
  - Specification: Critical components specified in TLA+ (workflow execution, state management, safety mechanisms)
  - Model Checking: TLC model checker verifies properties (no deadlocks, safety properties hold, liveness properties satisfied)
  - Implementation Mapping: Code matches specification (manual review or automated verification)
  - Validation: Review TLA+ specs, verify model checking results, ensure spec-code alignment
- [ ] **Verified Implementation**: Review formally verified code
  - Verified Subset: Safety-critical code implemented in verified language (Dafny, F*, Coq)
  - Proof Obligations: All proof obligations discharged (pre/post-conditions, invariants, termination)
  - Code Extraction: Verified code extracted to production language (OCaml, C, Rust)
  - Validation: Review proofs, verify extraction correctness, test extracted code

**Federated Learning Review**:
- [ ] **Privacy-Preserving Learning**: Review federated learning implementation
  - Architecture: Model trained across multiple organizations without sharing raw data
  - Privacy Guarantees: Differential privacy enforced (ε-differential privacy with ε ≤ 1.0)
  - Secure Aggregation: Gradient aggregation uses secure multi-party computation (no single party sees gradients)
  - Validation: Test privacy (verify no data leakage), measure accuracy improvement (federated vs. single-org)

**Autonomous Incident Response Review**:
- [ ] **LLM-Powered Investigation**: Review AI investigation implementation
  - Investigation Workflow: LLM queries logs, correlates events, forms hypotheses, executes investigative actions
  - Decision Making: LLM makes containment decisions (block IP, isolate host, disable account) with confidence scores
  - Human Oversight: High-confidence decisions (≥95%) auto-execute, low-confidence escalate to analyst
  - Validation: Test with historical incidents, measure accuracy (autonomous decisions vs. expert decisions)

**Success Indicators - Level 3**:
- **Formal Verification**: Safety-critical components formally verified, zero specification violations in production
- **Federated Learning**: ≥10% accuracy improvement vs. single-org model, ε ≤ 1.0 differential privacy verified
- **Autonomous IR**: ≥50% of incidents fully autonomous, ≥95% decision accuracy vs. experts

---

**Document Information**: Practice: Implementation Review (IR) | Domain: Processes | HAIAMM v2.0 | Last Updated: 2025-12-30
