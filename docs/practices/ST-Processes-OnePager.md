# Security Testing Practice – Processes Domain
## HAIAMM v2.1 One-Pager

### Practice Overview

Security Testing for Processes validates that AI security orchestration systems correctly triage alerts, execute remediations safely, integrate with security tools reliably, and maintain system stability under adversarial conditions.

---

### Level 1: Key Testing Criteria

**Alert Triage Testing**:
- [ ] **Classification Accuracy Testing**: Test true positive detection
  - Test Dataset: Historical alerts (labeled true/false positives)
  - Success Criteria: ≥95% true positive detection, ≥70% precision
- [ ] **Severity Scoring Testing**: Test severity assignment accuracy
  - Success Criteria: ≥85% agreement with expert severity assignments
- [ ] **Priority Testing**: Test priority assignment logic
  - Success Criteria: High-priority incidents escalated within ≤5 minutes

**Orchestration Safety Testing**:
- [ ] **Blast Radius Testing**: Validate blast radius limits enforced
  - Method: Attempt orchestration exceeding limits (>50 IPs, >20 accounts, >5 systems)
  - Success Criteria: 100% of limit violations blocked
- [ ] **Rollback Testing**: Test automated rollback for failed actions
  - Method: Inject failures during execution, validate rollback
  - Success Criteria: 100% successful rollback, no residual changes
- [ ] **Pre-Change Simulation Testing**: Test impact assessment accuracy
  - Success Criteria: High-risk changes correctly identified, require approval
- [ ] **Post-Change Verification Testing**: Test change validation
  - Success Criteria: Failed changes detected within ≤1 minute, rollback triggered

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
- Triage accuracy: ≥95% true positive detection, ≥70% precision
- Safety: Zero production outages from AI automation, 100% rollback success rate
- Performance: MTTR ≤10 hours, ≥70% automation rate
- Integration reliability: ≥99.9% tool integration uptime

---

**Document Information**: Practice: Security Testing (ST) | Domain: Processes | HAIAMM v2.1 | Last Updated: 2025-12-25
