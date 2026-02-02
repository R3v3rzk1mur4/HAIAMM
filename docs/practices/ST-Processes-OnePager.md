# Security Testing Practice – Processes Domain
## HAIAMM v2.0 One-Pager

### Practice Overview

Security Testing for Processes validates that AI security orchestration systems correctly triage alerts, execute remediations safely, integrate with security tools reliably, and maintain system stability under adversarial conditions.

---

### Level 1: Key Testing Criteria

**Alert Triage Testing**:
- [ ] **Classification Accuracy Testing**: Test ML model true positive detection
  - Test Dataset: ≥1,000 historical alerts with expert labels (balanced: 50% true positives, 50% false positives/benign)
  - Test Method: Run alerts through ML classifier, compare predictions to expert labels
  - Metrics: Accuracy, precision (≥70%), recall (≥95%), F1-score (≥80%), confusion matrix analysis
  - Success Criteria: ≥95% true positive detection (recall), ≥70% precision (minimize false positives)
  - Edge Cases: Test with novel attack types (zero-day), adversarial alerts (crafted to evade), noisy alerts (malformed data)
  - Validation: Cross-validate results (k-fold), test on multiple time periods (ensure model doesn't overfit to specific period)
- [ ] **Severity Scoring Testing**: Test AI severity adjustment accuracy
  - Test Dataset: ≥500 alerts with expert-assigned severity scores
  - Test Method: Run alerts through severity scoring algorithm, compare AI scores to expert scores
  - Success Criteria: ≥85% agreement with expert severity assignments (±10 points on 0-100 scale), severity tier agreement ≥90% (Critical/High/Medium/Low)
  - Context Testing: Verify context correctly adjusts severity (production server = higher severity, test environment = lower severity)
  - Validation: Spot-check severity adjustments with analysts, iterate on scoring formula based on feedback
- [ ] **Priority Testing**: Test alert prioritization logic
  - Test Scenarios: High-severity + high-criticality asset (should be top priority), low-severity + approaching SLA (should escalate)
  - Test Method: Insert test alerts into queue, measure time to analyst assignment
  - Success Criteria: High-priority incidents escalated within ≤5 minutes, Critical alerts bypass queue (immediate assignment)
  - Starvation Testing: Verify low-priority alerts eventually escalate (age >24 hours), not indefinitely delayed
  - Validation: Review priority queue over time, ensure no alerts stuck indefinitely
- [ ] **False Positive Reduction Testing**: Test FP minimization
  - Test Dataset: Known false positive alerts (≥200 samples)
  - Test Method: Run FPs through classifier, measure FP rate
  - Success Criteria: ≤30% false positive rate (precision ≥70%), demonstrate improvement over baseline (rule-based triage)
  - Tuning: If FP rate too high, adjust model threshold, retrain with more FP examples
- [ ] **Alert Deduplication Testing**: Test duplicate detection
  - Test Scenarios: Same alert triggered multiple times (same source, destination, signature), alerts from related campaign
  - Success Criteria: Duplicates correctly identified and aggregated (1,000 duplicates → 1 incident), related alerts correctly grouped
  - Validation: Verify deduplication doesn't suppress distinct attacks (similar but different alerts not merged incorrectly)

**Orchestration Safety Testing**:
- [ ] **Blast Radius Testing**: Validate blast radius limits enforced in all scenarios
  - Test Method: Attempt playbook execution with excessive scope (block 100 IPs, disable 50 accounts, isolate 20 hosts)
  - Success Criteria: 100% of limit violations blocked before execution (action rejected at orchestration layer), error logged, alert sent
  - Limit Types Tested: Network blocks (≤50 IPs), account disables (≤20), host isolations (≤5), rate limits (≤100 actions/hour, ≤500/day)
  - Exception Testing: Verify critical asset exceptions work (production server requires approval even if under limit)
  - Validation: Test all action types with over-limit requests, verify none execute, verify appropriate error messages
- [ ] **Rollback Testing**: Test automated rollback for all reversible actions
  - Test Actions: Block IP → unblock IP, disable account → enable account, isolate host → de-isolate host, add firewall rule → remove firewall rule
  - Test Method: Execute action, inject failure (post-change verification fails, analyst triggers manual rollback), verify rollback executes
  - Success Criteria: 100% successful rollback for reversible actions, system state restored to pre-action state, no residual changes
  - Rollback Validation: Query system state after rollback (IP unblocked in firewall, account active in AD, host connected in EDR)
  - Irreversible Action Testing: Verify irreversible actions (delete files, reset passwords) cannot rollback, flagged appropriately, require extra approval
  - Validation: Test rollback for each reversible action type, measure rollback success rate, investigate failures
- [ ] **Pre-Change Simulation Testing**: Test dry-run mode accuracy
  - Test Method: Run playbooks in simulation mode (no actual changes), compare simulation results to actual execution results
  - Success Criteria: High-risk changes correctly identified in simulation (delete files, disable critical accounts, isolate production servers), simulations ≥95% accurate vs. actual execution
  - Impact Assessment Testing: Verify impact estimates correct (blocked IPs = estimated affected users, disabled accounts = estimated service disruption)
  - Validation: Run same playbook in simulation then production, compare results, verify simulation accurately predicted outcomes
- [ ] **Post-Change Verification Testing**: Test change success validation
  - Test Scenarios: Successful action (IP blocked in firewall), failed action (firewall API error, IP not blocked)
  - Test Method: Execute actions, mock verification queries, verify system detects success/failure correctly
  - Success Criteria: Failed changes detected within ≤1 minute of execution, rollback automatically triggered on failure
  - Verification Timeout Testing: Verify verification has timeout (≤30 seconds), timeout treated as failure (triggers rollback)
  - Validation: Test verification for all action types, test with successful and failed actions, verify rollback triggers appropriately
- [ ] **Kill Switch Testing**: Test emergency automation halt
  - Test Method: Trigger kill switch (API call, CLI command), verify all automation stops immediately
  - Success Criteria: All playbook executions halt within ≤10 seconds, new playbooks blocked from starting, in-flight actions complete current step gracefully
  - Re-Enable Testing: Verify automation cannot re-enable without manager approval, root cause analysis required
  - Validation: Test kill switch during active playbook execution, verify graceful shutdown, test re-enable process

**Adversarial Testing**:
- [ ] **Alert Manipulation Testing**: Test if attackers can manipulate triage
  - Method: Craft alerts to evade detection or trigger false positives
  - Success Criteria: ≥85% of manipulation attempts detected
- [ ] **Orchestration Abuse Testing**: Test protection against abuse
  - Method: Attempt to trigger excessive remediation (DoS), unauthorized actions
  - Success Criteria: All abuse attempts blocked, alerts generated
- [ ] **Approval Bypass Testing**: Test approval workflow enforcement
  - Success Criteria: 100% of high-risk actions require approval, no bypass

**Integration Testing**:
- [ ] **Multi-Tool Integration Testing**: Test all tool integrations
  - Tools: SIEM, EDR, firewall, cloud, ticketing (≥80% of org tools)
  - Success Criteria: All integrations work correctly, handle errors gracefully
- [ ] **API Error Handling Testing**: Test behavior when tool APIs fail
  - Success Criteria: Circuit breaker triggers, graceful degradation, alerts generated
- [ ] **Data Normalization Testing**: Test common schema mapping
  - Success Criteria: All tool data correctly normalized to common format

**Workflow Execution Testing**:
- [ ] **Playbook Testing**: Test workflow execution correctness
  - Test Playbooks: Phishing response, ransomware response, DDoS response
  - Success Criteria: 100% of workflow steps execute correctly
- [ ] **Parallel Execution Testing**: Test concurrent workflow execution
  - Success Criteria: Multiple workflows execute without interference
- [ ] **Timeout and Retry Testing**: Test timeout handling
  - Success Criteria: Workflows timeout correctly, retries work with exponential backoff

**Performance Testing**:
- [ ] **Alert Processing Throughput**: Test alerts processed per hour
  - Success Criteria: ≥1,000 alerts/hour
- [ ] **MTTR Testing**: Test mean time to respond/remediate
  - Success Criteria: MTTR ≤10 hours (vs baseline)
- [ ] **Automation Rate Testing**: Test percentage of automated responses
  - Success Criteria: ≥70% of alerts auto-triaged, ≥50% auto-remediated

**Resilience Testing**:
- [ ] **Service Failure Testing**: Kill orchestration services, test recovery
  - Success Criteria: System recovers ≤5 minutes, no workflow data loss
- [ ] **Queue Overflow Testing**: Test behavior under alert spikes
  - Success Criteria: Queue buffers handle spikes, no alert loss
- [ ] **Tool Unavailability Testing**: Test behavior when security tools unavailable
  - Success Criteria: Workflows adapt (skip unavailable tools), alerts generated

**Human Oversight Testing**:
- [ ] **Approval Workflow Testing**: Test approval routing and escalation
  - Success Criteria: Approvals reach correct reviewers, escalate after timeout
- [ ] **Override Testing**: Test analyst override mechanism
  - Success Criteria: Analysts can override AI decisions, overrides logged
- [ ] **Audit Testing**: Test spot-check auditing (≥10% random sample)
  - Success Criteria: Audit system captures all actions, generates audit reports

**Compliance Testing**:
- [ ] **Audit Logging Testing**: Test all security-relevant actions logged
  - Success Criteria: 100% of actions logged with sufficient detail
- [ ] **Compliance Playbook Testing**: Test regulatory requirement playbooks
  - Success Criteria: All compliance workflows execute correctly

**Success Indicators**:
- **Triage Accuracy**: ≥95% true positive detection (recall), ≥70% precision, ≥80% F1-score
- **Safety**: Zero production outages from AI automation in testing, 100% blast radius limits enforced, 100% rollback success rate
- **Performance**: MTTR ≤10 hours (vs. 40 hours manual baseline), ≥70% automation rate, ≥1,000 alerts/hour throughput
- **Integration Reliability**: ≥99.9% tool integration uptime, ≥90% of integrations tested
- **Adversarial Robustness**: ≥85% adversarial attack detection, zero successful approval bypasses
- **Resilience**: System recovers within ≤5 minutes from all tested failures, zero workflow data loss

---

### Level 2: Advanced Security Testing

**AI-Powered Test Generation**:
- [ ] **LLM-Generated Test Cases**: Use AI to generate comprehensive test cases
  - Input: Playbook specification, expected behavior, safety requirements
  - LLM Output: Test cases covering normal paths, edge cases, failure scenarios, adversarial attacks
  - Success Criteria: AI generates ≥100 test cases per playbook, ≥80% are valid and useful, discover ≥5 new edge cases not previously tested
  - Validation: Human review of AI-generated tests, run tests to verify correctness
- [ ] **Mutation-Based Fuzzing**: AI-guided fuzzing for SOAR workflows
  - Method: Mutate playbook inputs (alter alert fields, change action parameters, inject malformed data), test system behavior
  - Success Criteria: Discover ≥10 new bugs or edge cases through fuzzing, all discovered issues fixed
  - Coverage: Fuzz all playbook input types (alert data, API responses, user inputs)

**Chaos Engineering**:
- [ ] **Failure Injection Testing**: Systematically inject failures
  - Failures: Kill AI model service, kill tool API, kill database, network partition, high latency (500ms-5s), disk full
  - Test Method: Inject failure during playbook execution, verify graceful degradation, measure recovery time
  - Success Criteria: System continues operating (degraded OK), recovers within ≤5 minutes, zero data loss, zero workflow corruption
  - Chaos Schedule: Run chaos tests weekly in staging, monthly in production (maintenance window)
- [ ] **Byzantine Failure Testing**: Test with arbitrary/malicious failures
  - Scenarios: Tool API returns corrupt data, database returns inconsistent state, network duplicates/reorders messages
  - Success Criteria: System detects Byzantine failures (data validation), doesn't trust corrupt data, degrades gracefully

**Formal Verification Testing**:
- [ ] **Model Checking**: Verify safety properties exhaustively
  - Tool: TLC (TLA+ model checker), Alloy Analyzer
  - Properties: Blast radius never exceeded, no deadlocks in workflows, rollback always possible for reversible actions
  - Success Criteria: All safety properties verified (no counterexamples), model checking complete for all critical workflows
  - Validation: Review TLA+ specifications, verify model checking results, ensure specification matches implementation

**Success Indicators - Level 2**:
- **AI Test Generation**: ≥100 test cases per playbook generated, ≥80% valid, ≥5 new edge cases discovered
- **Chaos Engineering**: System passes all chaos tests, ≤5 minute recovery time, zero data loss
- **Formal Verification**: All critical safety properties formally verified, zero specification violations

---

### Level 3: Research-Grade Security Testing

**Autonomous Red Teaming**:
- [ ] **AI-Powered Penetration Testing**: LLM-based red team agent
  - Capability: AI agent attempts to compromise SOAR system (evade triage, bypass approvals, trigger excessive automation, exfiltrate data)
  - Attack Vectors: Adversarial alerts, SOAR API exploitation, workflow manipulation, insider threats
  - Success Criteria: Discover ≥10 security vulnerabilities through autonomous red teaming, all vulnerabilities patched
  - Continuous: Run autonomous red team monthly, track vulnerability discovery rate over time
- [ ] **Multi-Agent Attack Simulation**: Coordinated multi-agent attacks
  - Scenario: Multiple AI agents coordinate attack (one evades detection, one triggers automation abuse, one exploits discovered vulnerabilities)
  - Success Criteria: System withstands coordinated attacks, all attack attempts detected and blocked

**Verified Testing**:
- [ ] **Proof-Carrying Tests**: Tests with formal correctness proofs
  - Method: Write tests in proof-assistant language (Coq, Isabelle), prove tests correctly validate specified properties
  - Properties: Test proves blast radius limits enforced, test proves rollback correctness, test proves no unauthorized actions
  - Success Criteria: Safety-critical tests have formal correctness proofs, zero false positives/negatives from verified tests

**Research Publications**:
- [ ] **Open-Source SOAR Testing Framework**: Publish testing tools
  - Framework: Complete SOAR testing suite (triage accuracy tests, safety tests, chaos tests, adversarial tests)
  - License: Apache 2.0 or MIT
  - Community: ≥10,000 GitHub stars, used by ≥100 organizations
- [ ] **Academic Publications**: Publish SOAR testing research
  - Venues: IEEE S&P, USENIX Security, ACM CCS, NDSS
  - Topics: AI-powered test generation, chaos engineering for SOAR, adversarial robustness testing, formal verification
  - Success Criteria: ≥3 publications in top-tier security conferences

**Success Indicators - Level 3**:
- **Autonomous Red Teaming**: ≥10 vulnerabilities discovered monthly, all patched before production
- **Verified Testing**: Safety-critical tests formally verified, zero test correctness bugs
- **Research Impact**: ≥10,000 GitHub stars on testing framework, ≥3 academic publications

---

**Document Information**: Practice: Security Testing (ST) | Domain: Processes | HAIAMM v2.0 | Last Updated: 2025-12-30
