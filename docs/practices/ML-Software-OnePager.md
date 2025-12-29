# Monitoring & Logging Practice – Software Domain
## HAIAMM v2.1 One-Pager

### Practice Overview

Monitoring & Logging for Software ensures AI code security systems have comprehensive observability—capturing security events, performance metrics, system health, and audit trails for security detection, incident response, debugging, compliance, and continuous improvement.

**Scope**: Monitoring and logging for:
- AI model operations (inference, training, accuracy, drift)
- Application security (authentication, authorization, attacks, vulnerabilities)
- System performance (latency, throughput, resource usage, errors)
- Security events (suspicious activity, policy violations, anomalies)
- Compliance and audit (data access, configuration changes, user actions)

**Why This Matters**: Without visibility, you're blind to attacks, performance issues, and compliance violations. Comprehensive monitoring and logging enable threat detection, incident response, troubleshooting, compliance evidence, and data-driven optimization.

---

### Level 1: Foundational Monitoring & Logging

### Core Objectives
1. Establish comprehensive logging across all AI system components
2. Implement centralized log aggregation and retention
3. Deploy security monitoring and alerting
4. Monitor system health and performance
5. Track AI model performance and drift
6. Ensure compliance and audit logging
7. Enable incident investigation and forensics

### Key Activities

#### 1. Security Event Logging

**Authentication and Authorization Logging**:
- [ ] **Login Events**: Log all authentication attempts
  - Success: User ID, timestamp, source IP, MFA status, session ID
  - Failure: User ID, timestamp, source IP, failure reason (wrong password, account locked)
  - Frequency: Real-time logging, no sampling
- [ ] **Authorization Events**: Log access control decisions
  - Allowed: User, resource, action, timestamp, policy matched
  - Denied: User, resource, action, timestamp, reason (insufficient permissions)
  - Use Case: Audit who accessed what, detect unauthorized access attempts
- [ ] **Session Management**: Log session lifecycle
  - Events: Session created, renewed, expired, invalidated (logout, timeout)
  - Context: Session ID, user, duration, termination reason
- [ ] **Privilege Escalation**: Log admin/privileged actions
  - Events: Sudo usage, admin console access, IAM role assumption
  - Context: User, action, timestamp, justification (if required)

**Application Security Events**:
- [ ] **API Security Events**: Log API requests and security checks
  - Requests: Endpoint, method, user, timestamp, parameters (sanitized)
  - Security: Authentication failures, authorization denials, rate limiting, input validation failures
  - Anomalies: Unusual request patterns, suspicious parameters, potential attacks
- [ ] **Input Validation Failures**: Log rejected inputs
  - Context: Input type, rejection reason (SQL injection, XSS, etc.), user, timestamp
  - Purpose: Detect attack attempts, tune validation rules
- [ ] **Security Policy Violations**: Log policy violations
  - Examples: Weak password attempts, MFA bypass attempts, suspicious file uploads
  - Action: Log violation, alert security team, block if necessary

**Attack Detection Logging**:
- [ ] **Injection Attempts**: Log SQL injection, command injection, XSS attempts
  - Detection: WAF blocks, input validation failures, suspicious queries
  - Context: Attack vector, payload (sanitized), source IP, user
- [ ] **Brute Force Attempts**: Log credential brute force, API abuse
  - Detection: Failed login threshold, excessive API calls
  - Response: Rate limiting triggered, account lockout, IP block
- [ ] **Vulnerability Exploitation**: Log exploitation attempts
  - Detection: Path traversal, SSRF, deserialization attacks
  - Source: WAF, IDS/IPS, application logs

#### 2. AI Model Monitoring and Logging

**Model Inference Logging**:
- [ ] **Inference Requests**: Log model prediction requests (privacy-preserving)
  - Context: Model version, timestamp, input features (no user content), prediction, confidence
  - Sampling: 100% for audit, 1-10% with details for analysis (avoid data leakage)
  - Privacy: Never log user code, PII, sensitive data
- [ ] **Model Decisions**: Log security decisions made by AI
  - Examples: Vulnerability detected, alert triaged, risk score assigned
  - Context: Input (sanitized), model output, confidence, explanation (if available)
  - Purpose: Audit AI decisions, detect bias, validate accuracy

**Model Performance Monitoring**:
- [ ] **Accuracy Metrics**: Track model accuracy over time
  - Metrics: Precision, recall, F1 score, false positive rate, false negative rate
  - Frequency: Real-time calculation, daily/weekly aggregation
  - Alerts: Alert if accuracy drops below threshold (e.g., ≤85%)
- [ ] **Model Drift Detection**: Detect data drift, concept drift
  - Data Drift: Input distribution changes (monitor feature statistics)
  - Concept Drift: Input-output relationship changes (monitor accuracy trends)
  - Alerts: Alert on significant drift, trigger model retraining
- [ ] **Explainability Logging**: Log model explanations
  - Purpose: Audit why model made decision, debug false positives/negatives
  - Content: Feature importance, explanation text, reasoning
  - Use Case: Developer sees "flagged as SQL injection due to 'SELECT' keyword in comment"

**Model Training Logging**:
- [ ] **Training Jobs**: Log model training executions
  - Context: Training data version, hyperparameters, training duration, final metrics
  - Results: Model version, accuracy, test performance
  - Purpose: Reproducibility, audit trail, compare model versions
- [ ] **Model Deployment**: Log model deployments
  - Context: Model version, deployment timestamp, deployer, rollout percentage
  - Validation: Pre-deployment testing results, production validation results
  - Rollback: Log rollbacks, reasons

#### 3. System Performance Monitoring

**Application Performance Monitoring (APM)**:
- [ ] **Request Latency**: Monitor API/request response time
  - Metrics: P50, P95, P99 latency
  - Granularity: Per endpoint, per service
  - Alerts: Alert if P95 exceeds SLA (e.g., >500ms)
- [ ] **Throughput**: Monitor requests per second
  - Metrics: Total requests, requests per endpoint, error rate
  - Capacity Planning: Track throughput trends, predict capacity needs
- [ ] **Error Rate**: Monitor application errors
  - Metrics: 4xx errors (client errors), 5xx errors (server errors)
  - Alerts: Alert on error rate spike (>5% of requests)
  - Investigation: Log error details (stack trace, context) for debugging

**Resource Utilization Monitoring**:
- [ ] **CPU and Memory**: Monitor compute resource usage
  - Metrics: CPU %, memory %, per service/pod/instance
  - Alerts: Alert if usage exceeds threshold (CPU >80%, memory >85%)
  - Auto-Scaling: Trigger auto-scaling based on resource usage
- [ ] **Disk and Network**: Monitor storage and network usage
  - Metrics: Disk I/O, disk space, network bandwidth, network errors
  - Alerts: Disk space <20%, network saturation
- [ ] **Container/Pod Metrics**: Monitor containerized workloads
  - Metrics: Container restarts, pod crashes, resource limits hit
  - Tools: Prometheus, Grafana, Kubernetes metrics

**Database Performance**:
- [ ] **Query Performance**: Monitor database query latency
  - Metrics: Slow queries (>1 second), query volume, connection pool usage
  - Optimization: Identify and optimize slow queries, add indexes
- [ ] **Database Health**: Monitor database availability and errors
  - Metrics: Connection errors, replication lag, deadlocks
  - Alerts: Alert on database connection failures, high replication lag

**Dependency Monitoring**:
- [ ] **External Service Health**: Monitor third-party APIs, services
  - Metrics: Response time, error rate, availability
  - Circuit Breaker: Automatically stop calling failing services
  - Alerts: Alert on external service degradation

#### 4. Security Monitoring and Alerting

**Real-Time Security Monitoring**:
- [ ] **SIEM Integration**: Send logs to SIEM for security analysis
  - Tools: Splunk, ELK Stack, Sumo Logic, Azure Sentinel
  - Logs: All security events, authentication, authorization, attacks, anomalies
  - Correlation: SIEM correlates events, detects attack patterns
- [ ] **Security Correlation Rules**: Detect multi-stage attacks
  - Examples: Brute force followed by successful login, privilege escalation after access
  - Response: Generate high-severity alerts, trigger investigation
- [ ] **Anomaly Detection**: Detect unusual behavior
  - Baseline: Establish baseline for normal behavior (login patterns, API usage, data access)
  - Detection: ML-based anomaly detection, statistical outlier detection
  - Alerts: Alert on significant deviations (unusual login location, excessive API calls)

**Security Alerting**:
- [ ] **Alert Triage and Prioritization**: Classify alerts by severity
  - Critical: Active exploitation, data breach, account compromise
  - High: Potential attack, repeated policy violations, anomalous behavior
  - Medium: Suspicious activity, failed attacks, configuration issues
  - Low: Informational, low-risk violations
- [ ] **Alert Routing**: Route alerts to appropriate teams
  - Critical/High: Page on-call security engineer, SOC analyst
  - Medium: Ticket to security team, review next business day
  - Low: Log for review, weekly summary
- [ ] **Alert Fatigue Prevention**: Minimize false positives
  - Tuning: Tune correlation rules, anomaly detection thresholds
  - Suppression: Suppress known false positives, noisy alerts
  - Goal: ≤5% false positive rate

**Threat Intelligence Integration**:
- [ ] **IOC Monitoring**: Monitor for indicators of compromise
  - Sources: Threat intel feeds (IP blacklists, malware hashes, CVEs)
  - Detection: Match logs against IOCs, alert on matches
  - Examples: Connection to known malicious IP, vulnerability exploit attempt

#### 5. Compliance and Audit Logging

**Audit Trail Requirements**:
- [ ] **Data Access Logging**: Log all access to sensitive data
  - Events: Read, write, delete operations on regulated data (PII, PHI, financial)
  - Context: User, resource, timestamp, action, justification (if required)
  - Purpose: GDPR Article 30 (record of processing), HIPAA audit trails
- [ ] **Configuration Change Logging**: Log all system configuration changes
  - Events: Security settings, access policies, encryption keys, network rules
  - Context: Who, what, when, before/after values
  - Purpose: Audit trail, rollback capability, compliance evidence
- [ ] **Administrative Action Logging**: Log privileged actions
  - Events: User creation/deletion, role assignment, policy changes
  - Context: Admin user, action, timestamp, target user/resource
  - Purpose: Insider threat detection, compliance

**Compliance-Specific Logging**:
- [ ] **GDPR Compliance Logging**:
  - [ ] Log consent collection and updates
  - [ ] Log data subject access requests (SARs)
  - [ ] Log data deletion requests and execution
  - [ ] Log cross-border data transfers
  - Retention: ≥3 years per GDPR Article 30
- [ ] **HIPAA Compliance Logging**:
  - [ ] Log all PHI access (who accessed what patient data)
  - [ ] Log PHI modifications and deletions
  - [ ] Log security incidents involving PHI
  - Retention: ≥6 years per HIPAA
- [ ] **PCI-DSS Compliance Logging**:
  - [ ] Log all access to cardholder data
  - [ ] Log authentication attempts (success and failure)
  - [ ] Log administrative actions
  - Retention: ≥1 year (≥3 months online) per PCI-DSS

**Log Retention and Protection**:
- [ ] **Log Retention Policies**: Define retention periods
  - Security Logs: ≥90 days hot (SIEM), ≥1 year cold (archive)
  - Compliance Logs: Per regulation (GDPR 3 years, HIPAA 6 years, PCI-DSS 1 year)
  - General Logs: 30 days hot, 90 days cold
- [ ] **Log Integrity**: Protect logs from tampering
  - Methods: Write-once storage (S3 Object Lock), log signing, immutable storage
  - Access Control: Restrict log deletion, separate log infrastructure from application
  - Validation: Periodically verify log integrity (signatures, checksums)

#### 6. Logging Best Practices

**Structured Logging**:
- [ ] **JSON Logging**: Use structured log format (JSON)
  - Benefits: Machine-parsable, easy to query, supports complex data
  - Fields: Timestamp, level, message, context (user, IP, request ID, service)
  - Example: `{"timestamp": "2025-12-25T10:00:00Z", "level": "ERROR", "message": "Authentication failed", "user": "john@example.com", "ip": "192.168.1.1"}`
- [ ] **Consistent Schema**: Use standard logging schema
  - Standards: Common Event Format (CEF), OpenTelemetry, ECS (Elastic Common Schema)
  - Benefits: Interoperability, easier SIEM integration

**Sensitive Data Handling**:
- [ ] **Never Log Secrets**: Never log passwords, tokens, encryption keys
  - Sanitization: Redact sensitive fields before logging
  - Example: Log `{"user": "john", "password": "REDACTED"}` not actual password
- [ ] **Privacy-Preserving Logging**: Minimize PII in logs
  - Approach: Log user IDs (not names), hash IPs, avoid logging user content
  - Purpose: GDPR compliance, privacy protection
- [ ] **Log Sanitization**: Remove/redact sensitive data from logs
  - Auto-Redaction: Automatically redact patterns (credit cards, SSNs, API keys)
  - Manual Review: Review logs before sharing externally

**Correlation and Context**:
- [ ] **Request IDs**: Use correlation IDs to track requests across services
  - Implementation: Generate request ID at entry point, propagate through all services
  - Benefits: Trace request path, debug distributed systems
- [ ] **User Context**: Include user context in all logs
  - Fields: User ID, session ID, tenant ID, IP address
  - Purpose: Audit user actions, investigate user-specific issues

**Log Levels**:
- [ ] **Appropriate Log Levels**: Use log levels correctly
  - ERROR: Errors requiring immediate attention (service down, critical failures)
  - WARN: Warnings (degraded performance, recoverable errors, suspicious activity)
  - INFO: Normal operations (API requests, authentication, configuration changes)
  - DEBUG: Detailed debugging information (variable values, function calls)
  - Production: Log at INFO level, enable DEBUG for troubleshooting

#### 7. Centralized Log Aggregation

**Log Collection**:
- [ ] **Agents/Shippers**: Deploy log collection agents
  - Tools: Fluentd, Filebeat, Logstash, CloudWatch Agent
  - Coverage: All servers, containers, applications, network devices
  - Reliability: Buffer logs locally if SIEM unavailable, retry on failure
- [ ] **Log Forwarding**: Forward logs to centralized SIEM
  - Protocol: Syslog, HTTP, Kafka (high throughput)
  - Security: Encrypt logs in transit (TLS), authenticate log sources

**Log Storage and Indexing**:
- [ ] **Hot Storage**: Fast access for recent logs (≤90 days)
  - Tools: Elasticsearch, Splunk, CloudWatch Logs Insights
  - Purpose: Real-time search, security investigation, troubleshooting
- [ ] **Cold Storage**: Long-term archival (>90 days)
  - Tools: S3, Azure Blob, Google Cloud Storage
  - Purpose: Compliance retention, historical analysis
  - Cost: Lower cost per GB, slower access

**Log Search and Analysis**:
- [ ] **Log Search Interface**: Enable log search and filtering
  - Features: Full-text search, field filters, time range, regex
  - Tools: Kibana (ELK), Splunk Search, CloudWatch Logs Insights
- [ ] **Log Dashboards**: Visualize log data
  - Dashboards: Security events, application performance, errors, model metrics
  - Tools: Grafana, Kibana, Splunk Dashboards

#### 8. Incident Investigation and Forensics

**Incident Response Support**:
- [ ] **Timeline Reconstruction**: Reconstruct attack timeline from logs
  - Process: Correlate logs across services, identify attack path, determine scope
  - Tools: SIEM correlation, log analysis scripts
- [ ] **Forensic Log Preservation**: Preserve logs for investigation
  - Process: Immediately snapshot logs, protect from deletion/modification
  - Legal Hold: Preserve logs for legal proceedings, regulatory investigations

**Root Cause Analysis**:
- [ ] **Error Investigation**: Debug errors and failures using logs
  - Process: Search for error, review context, trace request path, identify root cause
  - Resolution: Fix bug, improve error handling, prevent recurrence
- [ ] **Performance Troubleshooting**: Diagnose performance issues
  - Process: Identify slow requests, review database queries, check resource usage
  - Optimization: Optimize queries, add caching, scale resources

---

### Key Success Indicators

**Coverage Metrics**:
1. **Logging Coverage**: 100% of services, components emit logs
2. **Security Event Coverage**: ≥95% of security events logged (authentication, authorization, attacks)
3. **Compliance Coverage**: 100% of required compliance events logged (data access, changes, admin actions)

**Quality Metrics**:
1. **Log Completeness**: ≥99% of logs successfully delivered to SIEM
2. **Log Latency**: ≥95% of logs ingested within ≤60 seconds
3. **Structured Logging**: ≥90% of logs in structured format (JSON)

**Security Metrics**:
1. **Alert Quality**: ≤5% false positive rate for security alerts
2. **Detection Time**: ≥90% of attacks detected within ≤5 minutes
3. **Investigation Time**: Mean time to investigate (MTTI) ≤30 minutes for critical alerts

**Operational Metrics**:
1. **Availability**: ≥99.9% logging infrastructure uptime
2. **Retention Compliance**: 100% of logs retained per policy
3. **Query Performance**: ≥95% of log queries complete within ≤10 seconds

---

## Level 2: Comprehensive Monitoring & Logging

**Enhanced Practices**:
- Distributed tracing (trace requests across microservices)
- User behavior analytics (detect insider threats, account compromise)
- Advanced anomaly detection (ML-based behavioral baselines)
- Synthetic monitoring (proactive health checks, simulated transactions)
- Predictive analytics (predict failures, capacity issues before they occur)

---

## Level 3: Industry-Leading Monitoring & Logging

**Advanced Practices**:
- AI-powered incident detection and triage (AI analyzes logs, auto-triages incidents)
- Continuous compliance validation (real-time compliance monitoring)
- Open telemetry (contribute to open-source observability standards)
- Public transparency reports (publish security metrics, incident statistics)
- Chaos engineering with observability (inject failures, validate monitoring catches them)

---

## Practice Integration

**Threat Assessment (TA)**: ML detects threats identified in TA
**Security Requirements (SR)**: ML validates SR compliance (logging requirements)
**Issue Management (IM)**: ML tracks vulnerability remediation
**Environment Hardening (EH)**: ML monitors hardening compliance, configuration drift
**Security Testing (ST)**: ML captures test results, validates coverage
**Incident Response**: ML provides logs for investigation, forensics

---

## Conclusion

Monitoring & Logging for Software ensures AI code security systems have comprehensive observability for security detection, incident response, debugging, compliance, and optimization. Level 1 establishes security logging, AI model monitoring, performance monitoring, SIEM integration, and compliance logging. Level 2 adds distributed tracing and user behavior analytics. Level 3 achieves AI-powered incident detection and continuous compliance validation.

---

**Document Information**:
- **Practice**: Monitoring & Logging (ML)
- **Domain**: Software
- **HAIAMM Version**: 2.1
- **Maturity Levels**: 3 (Foundational, Comprehensive, Industry-Leading)
- **Last Updated**: 2025-12-25
