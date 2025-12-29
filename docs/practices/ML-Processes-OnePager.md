# Monitoring & Logging Practice – Processes Domain
## HAIAMM v2.1 One-Pager

### Practice Overview

Monitoring & Logging for Processes ensures AI security orchestration (SOAR) systems have comprehensive observability for automation actions, playbook executions, alert triage, and system health—capturing all orchestration decisions and actions for security, compliance, debugging, and continuous improvement.

---

### Level 1: Key Monitoring & Logging Activities

**Alert Triage Logging**:
- [ ] **Alert Classification Logging**: Log AI triage decisions
  - Events: Alert received, classification (true positive/false positive/investigate), severity assigned
  - Context: Alert source, alert type, classification confidence, reasoning
  - Purpose: Audit AI decisions, validate accuracy, tune model
- [ ] **Triage Model Performance**: Monitor classification accuracy
  - Metrics: True positive rate (≥95%), precision (≥70%), false positive rate
  - Tracking: Real-time metrics, daily/weekly aggregation
  - Alerts: Alert if accuracy drops below threshold
- [ ] **Manual Overrides**: Log analyst overrides of AI triage
  - Context: Alert, AI classification, analyst classification, reason for override
  - Purpose: Identify classification errors, training data for model improvement

**Playbook Execution Logging**:
- [ ] **Playbook Lifecycle**: Log complete playbook execution
  - Events: Playbook triggered, started, steps executed, completed/failed
  - Context: Playbook name, trigger (alert, schedule, manual), executor, duration
  - Steps: Log each playbook step (action, inputs, outputs, result)
  - Purpose: Audit trail, debugging, compliance
- [ ] **Automation Actions**: Log all actions taken by playbooks
  - Examples: IP blocked, account disabled, system isolated, ticket created
  - Context: Action, target (IP, account, system), timestamp, result (success/failure)
  - Approval: Log approval requests, approvals, rejections for high-risk actions
- [ ] **Playbook Errors**: Log playbook failures and errors
  - Context: Playbook, step failed, error message, stack trace
  - Purpose: Debug failures, improve error handling, prevent recurrence

**Orchestration Safety Logging**:
- [ ] **Blast Radius Tracking**: Log resources affected by automation
  - Metrics: IPs blocked, accounts disabled, systems isolated per action
  - Validation: Verify blast radius within limits (≤50 IPs, ≤20 accounts, ≤5 systems)
  - Alerts: Alert if blast radius limit approached or exceeded
- [ ] **Pre-Change Validation**: Log impact assessments before automation
  - Events: Validation performed, impact predicted, risk assessed
  - Context: Resources affected, potential impact, approval required
  - Purpose: Audit risk assessments, validate safety checks
- [ ] **Rollback Logging**: Log rollback actions
  - Events: Rollback triggered, rollback steps, rollback completed
  - Context: Failed action, reason, rollback success/failure
  - Purpose: Validate rollback mechanisms, investigate failures

**Integration Logging**:
- [ ] **Tool Integration Activity**: Log all integration API calls
  - Events: API call made, endpoint, parameters (sanitized), response
  - Context: Integration (SIEM, EDR, firewall), operation, timestamp, result
  - Purpose: Debug integration issues, audit tool usage
- [ ] **Integration Errors**: Log integration failures
  - Events: API timeout, authentication failure, rate limiting, service unavailable
  - Context: Integration, error type, error message, retry attempts
  - Alerts: Alert on repeated integration failures, circuit breaker triggered
- [ ] **Credential Usage**: Log secrets/credential access (not values)
  - Events: Credential retrieved from secrets manager, used for integration
  - Context: Which credential, which integration, timestamp
  - Purpose: Audit credential usage, detect anomalies

**Performance Monitoring**:
- [ ] **Alert Processing Performance**: Monitor alert triage throughput
  - Metrics: Alerts processed per hour, triage latency (alert → classification)
  - Targets: ≥1,000 alerts/hour, ≤30 seconds triage latency
- [ ] **Playbook Performance**: Monitor playbook execution performance
  - Metrics: Playbook execution time, step latency, success rate
  - Targets: ≥95% success rate, reasonable execution times per playbook
  - Optimization: Identify slow playbooks, optimize steps
- [ ] **Mean Time to Respond (MTTR)**: Track incident response speed
  - Metrics: Time from alert to containment, time to remediation
  - Target: MTTR ≤10 hours (vs manual baseline)
  - Trend: Track MTTR improvement over time

**Automation Metrics**:
- [ ] **Automation Rate**: Track % of alerts automated
  - Metrics: % alerts auto-triaged, % alerts auto-remediated
  - Targets: ≥70% auto-triaged, ≥50% auto-remediated
  - Trend: Increasing automation rate over time
- [ ] **False Automation**: Track incorrect automation actions
  - Detection: Playbook executed on false positive, incorrect action taken
  - Metrics: False automation rate (target: ≤2%)
  - Impact: Measure impact of false automation, prevent recurrence

**Approval Workflow Logging**:
- [ ] **Approval Requests**: Log all approval requests
  - Context: Playbook, action, risk level, approvers, timestamp
  - Purpose: Audit high-risk actions, track approval latency
- [ ] **Approval Decisions**: Log approval/rejection decisions
  - Context: Approver, decision (approve/reject), timestamp, justification
  - SLA Tracking: Monitor approval latency (target: ≤30 minutes)
- [ ] **Approval Timeouts**: Log approval timeouts
  - Events: Approval request timeout, default action (reject or escalate)
  - Purpose: Identify approval bottlenecks, adjust timeouts

**Human Oversight Logging**:
- [ ] **Manual Interventions**: Log analyst manual actions
  - Events: Analyst overrode AI, manually executed action, modified playbook
  - Context: User, action, reason, timestamp
  - Purpose: Understand when/why manual intervention needed, improve automation
- [ ] **Spot-Check Audits**: Log random audit samples
  - Events: Automation action selected for audit, audit result (correct/incorrect)
  - Coverage: ≥10% random sample of automated actions
  - Purpose: Validate automation quality, detect systematic errors

**Security Event Logging**:
- [ ] **SOAR Security Events**: Log SOAR platform security events
  - Events: Login attempts, unauthorized access, configuration changes, playbook modifications
  - Context: User, action, timestamp, source IP
  - Purpose: Detect SOAR compromise, insider threats
- [ ] **Playbook Abuse Detection**: Monitor for automation abuse
  - Anomalies: Unusual playbook execution patterns, excessive actions, failed approvals
  - Alerts: Alert on potential abuse, investigate

**Compliance and Audit Logging**:
- [ ] **Compliance Automation Logging**: Log compliance-related automation
  - Events: Compliance checks performed, violations detected, remediation applied
  - Context: Compliance framework (PCI-DSS, HIPAA), finding, remediation
  - Purpose: Compliance evidence, audit trail
- [ ] **Audit Trail Integrity**: Protect orchestration logs from tampering
  - Methods: Write-once storage, log signing, separate log infrastructure
  - Access Control: Restrict log deletion, audit log access

**Alerting and Incident Response**:
- [ ] **Orchestration Alerts**: Alert on SOAR system issues
  - Critical: SOAR platform down, all integrations failing, automation storm (excessive actions)
  - High: Integration failures, playbook errors, blast radius exceeded
  - Medium: Slow performance, approval delays
  - Routing: Page on-call for critical, ticket for high/medium
- [ ] **Automation Quality Alerts**: Alert on automation accuracy issues
  - Events: High false automation rate, triage accuracy drop, repeated playbook failures
  - Purpose: Maintain automation quality, trigger reviews

**Dashboards and Reporting**:
- [ ] **SOAR Dashboard**: Real-time orchestration visibility
  - Metrics: Alerts processed, automation rate, MTTR, playbook success rate
  - Health: Integration status, system performance, queue depth
- [ ] **Executive Reporting**: Periodic SOAR performance reports
  - Content: Automation metrics, MTTR trends, incidents handled, ROI
  - Audience: CISO, SOC management, IT leadership

**Success Indicators**:
- Logging coverage: 100% playbook executions logged, 100% automation actions logged
- Triage accuracy: ≥95% true positive detection, ≥70% precision
- Automation rate: ≥70% alerts auto-triaged, ≥50% auto-remediated
- MTTR: ≤10 hours (≥50% reduction vs manual response)
- Safety: Zero blast radius violations, 100% of rollbacks successful

---

**Document Information**: Practice: Monitoring & Logging (ML) | Domain: Processes | HAIAMM v2.1 | Last Updated: 2025-12-25
