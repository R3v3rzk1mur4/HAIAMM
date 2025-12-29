# Monitoring & Logging Practice – Infrastructure Domain
## HAIAMM v2.1 One-Pager

### Practice Overview

Monitoring & Logging for Infrastructure ensures AI cloud and network security systems have comprehensive observability across multi-cloud environments—capturing configuration changes, security events, remediation actions, and performance metrics for threat detection, compliance, and operational excellence.

---

### Level 1: Key Monitoring & Logging Activities

**Cloud Audit Logging**:
- [ ] **Comprehensive Cloud Logging**: Enable all cloud audit logs
  - AWS: CloudTrail (all regions, all events), VPC Flow Logs, S3 access logs, RDS logs
  - Azure: Activity Log, Resource Logs, NSG Flow Logs, Storage Analytics
  - GCP: Cloud Audit Logs (admin, data access, system events), VPC Flow Logs
  - Retention: ≥90 days in SIEM, ≥1 year in cold storage
- [ ] **Configuration Change Logging**: Log all infrastructure changes
  - Tools: AWS Config, Azure Policy, GCP Config Connector
  - Events: Resource creation/modification/deletion, policy changes, security group changes
  - Context: Who, what, when, before/after values
  - Purpose: Audit trail, compliance, rollback capability

**Security Event Logging**:
- [ ] **IAM Activity Logging**: Log all IAM operations
  - Events: User creation/deletion, role assumption, policy changes, login attempts
  - Context: User, action, timestamp, source IP, MFA status
  - Alerts: Alert on suspicious IAM activity (unusual role assumption, privilege escalation)
- [ ] **Network Activity Logging**: Log network traffic and security events
  - VPC Flow Logs: Source/destination IPs, ports, protocols, bytes, accept/reject
  - Firewall Logs: Security group/NSG/firewall rule matches, blocks
  - Purpose: Detect network attacks, unauthorized access, data exfiltration
- [ ] **Threat Detection Logging**: Log security findings
  - Tools: AWS GuardDuty, Azure Defender, GCP Security Command Center
  - Events: Suspicious API calls, compromised credentials, malware, cryptomining
  - Integration: Forward findings to SIEM, ticket system

**Remediation Action Logging**:
- [ ] **Automated Remediation Logging**: Log all AI remediation actions
  - Events: Misconfiguration detected, remediation triggered, actions taken, results
  - Context: Resource affected, issue found, action taken, success/failure
  - Approval: Log approval requests, approvals, rejections
  - Purpose: Audit AI decisions, investigate unintended changes
- [ ] **Blast Radius Tracking**: Monitor remediation scope
  - Metrics: Number of resources affected per remediation action
  - Alerts: Alert if blast radius limit approached or exceeded
  - Validation: Verify blast radius limits enforced
- [ ] **Rollback Logging**: Log rollback actions
  - Events: Remediation failure detected, rollback triggered, rollback completed
  - Context: Failed action, reason, rollback steps, final state
  - Purpose: Validate rollback mechanisms, investigate failures

**Configuration Monitoring**:
- [ ] **Configuration Drift Detection**: Monitor for unauthorized changes
  - Baseline: Establish approved configuration baselines
  - Detection: Continuous monitoring, detect deviations from baseline
  - Alerts: Alert on drift (unauthorized changes, misconfigurations)
  - Remediation: Auto-remediate drift or alert for manual review
- [ ] **Compliance Monitoring**: Monitor compliance with security policies
  - Frameworks: CIS Benchmarks, PCI-DSS, HIPAA, custom policies
  - Tools: AWS Security Hub, Azure Policy, GCP Security Command Center
  - Metrics: Compliance score, non-compliant resources, trend over time

**Performance Monitoring**:
- [ ] **Cloud Resource Utilization**: Monitor cloud resource usage
  - Metrics: CPU, memory, network, disk I/O per resource
  - Cost: Track cost per service, identify cost optimization opportunities
  - Alerts: Alert on resource exhaustion, unusual usage spikes
- [ ] **API Performance**: Monitor cloud API latency and errors
  - Metrics: API call latency, error rate, throttling events
  - Alerts: Alert on API degradation, rate limiting
- [ ] **Detection Latency**: Monitor time-to-detect misconfigurations
  - Metric: Time from misconfiguration to detection (target: ≤5 minutes)
  - Purpose: Validate real-time monitoring effectiveness

**Multi-Cloud Correlation**:
- [ ] **Cross-Cloud Log Aggregation**: Centralize logs from all clouds
  - Integration: Forward AWS, Azure, GCP logs to unified SIEM
  - Normalization: Normalize to common schema (map cloud-specific fields)
  - Benefits: Unified view, cross-cloud attack detection, consistent alerting
- [ ] **Cross-Cloud Security Posture**: Monitor security across all clouds
  - Dashboard: Unified security dashboard (misconfigurations, vulnerabilities, incidents across clouds)
  - Metrics: Compliance score per cloud, security findings per cloud
  - Trends: Track security posture improvement over time

**Network Monitoring**:
- [ ] **Network Connectivity Monitoring**: Monitor network health
  - Metrics: Network latency, packet loss, bandwidth utilization
  - Tools: VPC Reachability Analyzer, Network Watcher, VPC Flow Logs
  - Alerts: Alert on connectivity issues, routing problems
- [ ] **Network Security Monitoring**: Detect network-based attacks
  - Coverage: Port scans, DDoS, lateral movement, data exfiltration
  - Tools: VPC Flow Logs analysis, IDS/IPS, SIEM correlation
  - Alerts: Alert on suspicious network patterns

**Alerting and Incident Response**:
- [ ] **Security Alerts**: Alert on critical security events
  - Critical: Public S3 bucket, admin account compromise, GuardDuty high-severity findings
  - High: Misconfiguration, unauthorized access attempts, policy violations
  - Medium: Compliance violations, configuration drift
  - Routing: Page on-call for critical, ticket for high/medium
- [ ] **Alert Enrichment**: Add context to alerts
  - Context: Resource metadata, related events, threat intelligence
  - Purpose: Enable faster triage, better decision-making
- [ ] **Incident Timeline**: Correlate events for incident investigation
  - Process: Link related logs (IAM changes, network traffic, config changes)
  - Purpose: Reconstruct attack timeline, determine blast radius

**Success Indicators**:
- Logging coverage: 100% of cloud accounts/regions logging enabled
- Log completeness: ≥99% of logs delivered to SIEM
- Detection latency: ≥90% of misconfigurations detected within ≤5 minutes
- Remediation logging: 100% of automated actions logged
- Alert quality: ≤5% false positive rate

---

**Document Information**: Practice: Monitoring & Logging (ML) | Domain: Infrastructure | HAIAMM v2.1 | Last Updated: 2025-12-25
