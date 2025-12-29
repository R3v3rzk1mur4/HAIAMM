# Environment Hardening Practice – Processes Domain
## HAIAMM v2.1 One-Pager

### Practice Overview

Environment Hardening for Processes ensures AI security orchestration (SOAR) systems are deployed with secure configurations, hardened integrations, blast radius protections, and defense-in-depth controls to prevent automation abuse and maintain operational safety.

---

### Level 1: Key Hardening Activities

**SOAR Platform Hardening**:
- [ ] **Platform Configuration Hardening**: Secure SOAR platform settings
  - Authentication: Strong authentication, MFA for all accounts
  - Network: Restrict network access (private IPs, firewall rules)
  - Encryption: TLS for all connections, encrypt sensitive data at rest
  - Patching: Apply platform patches within SLA (Critical ≤24h, High ≤7d)
  - Benchmarks: Apply vendor security best practices
- [ ] **Access Control**: Least privilege for SOAR users
  - RBAC: Role-based access (viewer, analyst, admin, automation engineer)
  - Separation: Separate playbook creation, approval, execution permissions
  - Review: Quarterly access reviews, remove unused accounts

**Playbook Hardening**:
- [ ] **Playbook Security Review**: Review playbooks before deployment
  - Coverage: Hardcoded credentials, injection flaws, insufficient validation, logic errors
  - Process: Security review required before production deployment
  - Approval: Require approval for high-risk playbooks (modify infrastructure, delete data)
- [ ] **Input Validation**: Validate all playbook inputs
  - Coverage: Alert data, user inputs, external data sources
  - Approach: Whitelist validation, sanitize inputs, reject unexpected data
  - Protection: Prevent injection attacks (command injection, SQL injection)
- [ ] **Playbook Signing**: Sign playbooks to prevent tampering
  - Method: Digital signatures, verify before execution
  - Benefit: Ensure playbook integrity, detect unauthorized modifications

**Blast Radius Protection**:
- [ ] **Hard-Coded Limits**: Enforce maximum automated actions
  - Network: ≤50 IPs blocked per action
  - Accounts: ≤20 accounts disabled per action
  - Systems: ≤5 systems isolated per action
  - Enforcement: Hard-coded in orchestration engine, cannot be bypassed
- [ ] **Rate Limiting**: Prevent excessive automation
  - Limits: Maximum actions per minute, per hour, per day
  - Circuit Breaker: Stop automation if limits exceeded, require manual review
- [ ] **Approval Workflows**: Require approval for high-risk actions
  - High-Risk: Infrastructure changes, bulk account actions, data deletion, system isolation
  - Process: Automation pauses, sends approval request, waits for approval
  - Timeout: Auto-reject if no approval within time limit (e.g., 30 minutes)

**Rollback Hardening**:
- [ ] **Pre-Change Snapshots**: Snapshot state before automation
  - Coverage: Network rules, account states, system configurations
  - Purpose: Enable rollback to previous state
- [ ] **Rollback Testing**: Test rollback mechanisms
  - Frequency: Quarterly rollback tests
  - Validation: Verify rollback restores previous state, no residual changes
- [ ] **Automated Rollback**: Auto-rollback on failure
  - Triggers: Action failure, post-change verification failure, error detected
  - Implementation: Automated rollback within ≤5 minutes of failure detection

**Integration Hardening**:
- [ ] **Credential Management**: Secure integration credentials
  - Storage: Store credentials in secrets manager (Vault, AWS Secrets Manager)
  - Rotation: Rotate credentials quarterly, immediately on compromise
  - Least Privilege: Integration accounts have minimal required permissions
- [ ] **API Security**: Secure SOAR API integrations
  - Authentication: Require authentication for all API calls
  - Authorization: Validate permissions before operations
  - Rate Limiting: Prevent API abuse, enforce rate limits
  - Logging: Log all API calls, audit for anomalies
- [ ] **Integration Isolation**: Isolate integrations from each other
  - Approach: Separate service accounts per integration
  - Benefit: Compromise of one integration doesn't affect others

**Audit and Logging Hardening**:
- [ ] **Comprehensive Logging**: Log all automation actions
  - Coverage: Playbook execution, actions taken, approvals, failures, rollbacks
  - Format: Structured logging (JSON), include context (user, timestamp, playbook, target)
  - Retention: ≥90 days in SIEM, ≥1 year in cold storage
- [ ] **Audit Trail Integrity**: Protect logs from tampering
  - Methods: Write-once storage, log signing, separate log infrastructure
  - Access Control: Restrict log access, audit log access
- [ ] **Security Monitoring**: Monitor SOAR for abuse
  - Anomalies: Unusual playbook execution patterns, excessive actions, failed approvals
  - Alerts: Alert on anomalies, potential abuse, security incidents

**Graduated Automation Hardening**:
- [ ] **Automation Levels**: Implement graduated automation
  - Level 1 - Alert Only: AI generates alert, no automated action
  - Level 2 - Recommend: AI recommends action, analyst decides
  - Level 3 - Auto-Execute Reversible: AI auto-executes, can rollback (e.g., block IP)
  - Level 4 - Auto-Execute Irreversible: AI auto-executes, cannot rollback (e.g., delete data)
  - Default: Start with Level 1-2, gradually enable Level 3-4 with validation
- [ ] **Automation Safeguards**: Implement safeguards per level
  - Level 3: Require rollback capability, blast radius limits, approval override option
  - Level 4: Require approval workflow, extensive logging, post-action review

**Testing and Validation**:
- [ ] **Playbook Testing**: Test playbooks before production
  - Staging: Test in staging environment (simulate production)
  - Dry Run: Execute playbook without making changes, validate logic
  - Validation: Verify playbook works correctly, doesn't cause unintended effects
- [ ] **Chaos Testing**: Test SOAR resilience under failure
  - Scenarios: Kill services, inject errors, simulate integration failures
  - Validation: Verify graceful degradation, no data loss, recovery within SLA

**Resilience Hardening**:
- [ ] **Queue Hardening**: Ensure queue reliability
  - Durability: Persist queue to disk, survive service restarts
  - Monitoring: Alert on queue depth (potential backlog), message age
  - Overflow Handling: Reject new messages if queue full (prevent memory exhaustion)
- [ ] **Service Redundancy**: Eliminate single points of failure
  - Architecture: Deploy multiple SOAR instances, load balance
  - Failover: Auto-failover to standby instance on primary failure
- [ ] **Health Checks**: Monitor SOAR health
  - Liveness: Is service running? (restart if not)
  - Readiness: Is service ready? (remove from rotation if not)
  - Dependencies: Monitor integration health, alert on failures

**Success Indicators**:
- Platform security: ≥95% patched within SLA, 100% MFA enforcement
- Blast radius: 100% of automated actions within blast radius limits
- Rollback: 100% successful rollback in testing, ≤5 minute rollback time
- Approval: 100% of high-risk actions require approval, zero bypasses
- Logging: 100% of automation actions logged, logs protected from tampering

---

**Document Information**: Practice: Environment Hardening (EH) | Domain: Processes | HAIAMM v2.1 | Last Updated: 2025-12-25
