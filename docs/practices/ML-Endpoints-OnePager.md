# Monitoring & Logging Practice – Endpoints Domain
## HAIAMM v2.0 One-Pager

### Practice Overview

Monitoring & Logging for Endpoints ensures AI endpoint security systems have comprehensive observability across all endpoint devices—capturing security events, agent health, threat detections, and system performance for threat detection, incident response, and compliance.

---

### Level 1: Key Monitoring & Logging Activities

**Security Event Logging**:
- [ ] **Threat Detection Logging**: Log all malware and threat detections
  - Events: Malware detected, ransomware blocked, behavioral anomaly detected
  - Context: Threat type, file path, hash, user, endpoint, action taken (quarantine, block, alert)
  - Privacy: Log threat indicators only, no user file content
  - Retention: ≥90 days in SIEM, ≥1 year for compliance
- [ ] **Endpoint Activity Logging**: Log security-relevant endpoint events
  - Process Activity: Process creation/termination, command-line arguments, parent process
  - Network Activity: Connections, DNS queries, data transfers
  - File Activity: File creation/modification/deletion (sensitive locations)
  - Registry Activity (Windows): Registry key creation/modification
  - Purpose: Behavioral analysis, threat hunting, incident investigation
- [ ] **Authentication Logging**: Log endpoint login activity
  - Events: User login/logout, failed logins, privilege escalation
  - Context: User, timestamp, method (password, biometric), success/failure
  - Alerts: Alert on repeated failed logins, unusual login times

**Agent Health Monitoring**:
- [ ] **Agent Status Monitoring**: Monitor endpoint agent health
  - Status: Running, stopped, crashed, unresponsive, updating
  - Metrics: Agent uptime, last check-in time, version
  - Alerts: Alert if agent offline >30 minutes, repeated crashes
  - Coverage: Track % endpoints with healthy agents (target: ≥98%)
- [ ] **Agent Performance Monitoring**: Monitor agent resource usage
  - Metrics: CPU %, memory usage, disk I/O, network usage
  - Thresholds: Alert if CPU >5%, memory >200MB (exceeds design limits)
  - Purpose: Detect agent malfunctions, performance issues
- [ ] **Agent Update Monitoring**: Monitor agent update status
  - Metrics: Agent version distribution, update success/failure rate
  - Alerts: Alert on update failures, incompatible versions
  - Rollout Tracking: Monitor staged rollout progress (canary → full deployment)

**Endpoint Configuration Monitoring**:
- [ ] **Configuration Compliance**: Monitor endpoint security configuration
  - Coverage: Disk encryption, firewall status, OS patch level, password policy
  - Benchmarks: CIS Benchmarks for Windows, macOS, Linux
  - Alerts: Alert on non-compliant endpoints (encryption disabled, firewall off)
  - Metrics: % endpoints compliant (target: ≥95%)
- [ ] **Configuration Drift Detection**: Detect unauthorized configuration changes
  - Baseline: Approved security configurations
  - Detection: Detect deviations (security settings changed, agent tampered with)
  - Remediation: Auto-remediate drift or alert for manual review

**Privacy-Preserving Telemetry**:
- [ ] **Privacy Compliance**: Ensure telemetry doesn't leak user data
  - Policy: Never log user file content, personal data, passwords
  - Logging: Log threat indicators (hashes, signatures), not user content
  - Validation: Regular audits of telemetry data, zero PII/user content
- [ ] **BYOD Separation**: Monitor work/personal data separation
  - Coverage: Agent monitors work apps/data only on BYOD
  - Validation: Verify no personal data captured
  - Compliance: GDPR, CCPA compliance for BYOD telemetry

**Threat Hunting and Investigation**:
- [ ] **Endpoint Query Capability**: Enable on-demand endpoint queries
  - Tools: Live query (Osquery, EDR query languages)
  - Use Cases: Threat hunting (search for IOCs across all endpoints), investigation
  - Examples: "Find all endpoints with suspicious process X", "Check registry key Y"
- [ ] **Forensic Data Collection**: Collect detailed forensic data on-demand
  - Data: Memory dump, disk image, process list, network connections
  - Triggers: Security incident, suspected compromise
  - Privacy: Collect only from compromised endpoints, secure storage

**Cross-Platform Monitoring**:
- [ ] **Windows Monitoring**: Windows-specific event logging
  - Logs: Windows Event Log (Security, System, Application), Sysmon, ETW
  - Coverage: Login events, process creation, network connections, registry changes
- [ ] **macOS Monitoring**: macOS-specific event logging
  - Logs: Unified Logging, Endpoint Security Framework (ESF) events
  - Coverage: Process execution, file events, network events
- [ ] **Linux Monitoring**: Linux-specific event logging
  - Logs: auditd, eBPF events, syslog
  - Coverage: Process execution, syscalls, file access, network activity
- [ ] **Mobile Monitoring**: Mobile device security monitoring
  - iOS: MDM logs, app installation, device compliance
  - Android: MDM logs, SafetyNet attestation, app permissions
  - Alerts: Jailbreak/root detection, non-compliant apps

**Performance Metrics**:
- [ ] **Detection Performance**: Monitor threat detection effectiveness
  - Metrics: Malware detection rate, false positive rate, detection latency
  - Targets: ≥95% detection, ≤5% false positives, ≤60s detection latency
- [ ] **Response Performance**: Monitor response action effectiveness
  - Metrics: Time to isolate, time to quarantine, isolation success rate
  - Targets: Network isolation ≤60 seconds, quarantine ≤10 seconds
- [ ] **Scanning Performance**: Monitor real-time scanning overhead
  - Metrics: File access latency increase, system performance impact
  - Targets: ≤100ms latency increase, ≤5% CPU usage

**Alerting and Incident Response**:
- [ ] **Threat Alerts**: Alert on endpoint threats
  - Critical: Active ransomware, confirmed malware execution, data exfiltration
  - High: Suspicious behavior, potential compromise, repeated attacks
  - Medium: Policy violations, unsuccessful attacks
  - Routing: Page on-call for critical, ticket for high/medium
- [ ] **Automated Response Tracking**: Log automated response actions
  - Actions: Process terminated, file quarantined, network isolated
  - Context: Threat, action taken, result, user notified
  - Purpose: Audit automated responses, validate effectiveness

**Compliance and Audit Logging**:
- [ ] **Endpoint Compliance Logging**: Log compliance-relevant events
  - GDPR: Log data access on endpoints, data transfers, deletions
  - HIPAA: Log PHI access from endpoints
  - Retention: Per regulatory requirements (GDPR 3 years, HIPAA 6 years)
- [ ] **Agent Action Logging**: Log all agent actions for audit
  - Events: Scans performed, files scanned, threats detected, actions taken
  - Purpose: Compliance evidence, incident investigation

**Success Indicators**:
- Agent coverage: ≥98% endpoints with healthy agents
- Detection effectiveness: ≥95% malware detection, ≤5% false positives
- Logging coverage: 100% security events logged
- Privacy compliance: Zero user content leakage incidents
- Performance: ≤5% CPU, ≤200MB memory, ≤100ms latency impact

---

**Document Information**: Practice: Monitoring & Logging (ML) | Domain: Endpoints | HAIAMM v2.0 | Last Updated: 2025-12-25
