# Monitoring & Logging Practice – Data Domain
## HAIAMM v2.1 One-Pager

### Practice Overview

Monitoring & Logging for Data ensures AI data security systems have comprehensive observability for data classification, DLP enforcement, privacy protection, and compliance—capturing data access, classification decisions, DLP events, and privacy metrics for security, compliance, and optimization.

---

### Level 1: Key Monitoring & Logging Activities

**Data Access Logging**:
- [ ] **Sensitive Data Access**: Log all access to classified data
  - Coverage: Restricted, Confidential, PII, PHI, financial data
  - Context: User, data classification, resource, timestamp, action (read/write/delete)
  - Purpose: GDPR Article 30 compliance, HIPAA audit trails, insider threat detection
  - Retention: Per regulation (GDPR 3 years, HIPAA 6 years, PCI-DSS 1 year)
- [ ] **Database Query Logging**: Log sensitive database queries
  - Coverage: Queries accessing sensitive tables/columns, bulk downloads
  - Context: User, query, rows returned, timestamp
  - Alerts: Alert on unusual query patterns (bulk exports, off-hours access)
- [ ] **Object Storage Access Logging**: Log S3, Blob Storage, GCS access
  - Coverage: Read, write, delete operations on sensitive buckets
  - Context: User, object, action, source IP, timestamp
  - Purpose: Detect unauthorized access, data exfiltration

**Data Classification Logging**:
- [ ] **Classification Decisions**: Log AI classification results
  - Events: Data classified, classification updated, manual override
  - Context: Data item, classification (Public/Internal/Confidential/Restricted), confidence score
  - Purpose: Audit classification accuracy, tune model
- [ ] **Classification Model Performance**: Monitor classification accuracy
  - Metrics: Precision, recall, F1 score, false positive rate
  - Tracking: Real-time metrics, daily/weekly aggregation
  - Alerts: Alert if accuracy drops below threshold (≤90%)
- [ ] **Manual Classification Overrides**: Log manual classification changes
  - Context: User, original classification, new classification, justification
  - Purpose: Identify classification errors, training data for model improvement

**DLP Event Logging**:
- [ ] **DLP Policy Violations**: Log all DLP events
  - Events: Data blocked, data alerted, data logged
  - Context: User, data type, channel (email, chat, upload), action taken
  - Severity: Critical (Restricted data to external), High (Confidential to internal), Medium (policy warning)
- [ ] **Exfiltration Attempts**: Log attempted data exfiltration
  - Detection: Sensitive data sent to external email, unauthorized cloud sync, USB transfer
  - Context: User, data classification, destination, volume, blocked/allowed
  - Alerts: Alert security team on exfiltration attempts
- [ ] **DLP False Positives**: Log false positive feedback
  - Events: User reports false positive, analyst reviews, classification updated
  - Purpose: Tune DLP rules, improve accuracy, reduce user friction
  - Metrics: False positive rate (target: ≤5%)

**Privacy Monitoring**:
- [ ] **Differential Privacy Metrics**: Monitor privacy budget consumption
  - Metrics: Privacy budget (epsilon) consumed, queries performed, budget remaining
  - Alerts: Alert when privacy budget nearing exhaustion (≥80% consumed)
  - Purpose: Prevent privacy budget depletion, enforce query limits
- [ ] **Federated Learning Monitoring**: Monitor distributed model training
  - Metrics: Participants, model accuracy, gradient updates, aggregation rounds
  - Privacy: Monitor for gradient inversion attempts, data leakage
- [ ] **Anonymization/Pseudonymization Tracking**: Log privacy-preserving operations
  - Events: Data anonymized, pseudonymized, aggregated for analytics
  - Purpose: Audit privacy protection measures, compliance evidence

**Compliance Logging**:
- [ ] **GDPR Compliance Logging**:
  - [ ] Log data subject access requests (SARs), responses
  - [ ] Log data deletion requests, execution
  - [ ] Log consent collection, updates, withdrawals
  - [ ] Log cross-border data transfers
  - Retention: ≥3 years per GDPR Article 30
- [ ] **CCPA Compliance Logging**:
  - [ ] Log opt-out requests, execution
  - [ ] Log data portability requests
  - [ ] Log "Do Not Sell" enforcement
- [ ] **Data Retention Enforcement Logging**:
  - [ ] Log data retention policies applied
  - [ ] Log automatic data deletion events
  - [ ] Log retention policy violations (data older than retention period)

**Data Lifecycle Monitoring**:
- [ ] **Data Creation Logging**: Log creation of sensitive data
  - Events: New sensitive data created, classified, encryption applied
  - Context: Data classification, creator, timestamp, storage location
- [ ] **Data Modification Logging**: Log changes to sensitive data
  - Context: User, data item, changes made, timestamp
  - Purpose: Audit trail, detect unauthorized modifications
- [ ] **Data Deletion Logging**: Log data deletion events
  - Events: Data deleted, retention policy applied, GDPR deletion request
  - Context: Data item, deletion reason, user, timestamp, verification
  - Purpose: Compliance evidence, prevent accidental deletion

**Storage Security Monitoring**:
- [ ] **Encryption Monitoring**: Monitor encryption status
  - Coverage: All data stores (databases, object storage, file systems)
  - Metrics: % data encrypted at rest, % connections encrypted in transit
  - Alerts: Alert on unencrypted data, encryption disabled
  - Targets: 100% sensitive data encrypted
- [ ] **Backup Monitoring**: Monitor backup status and integrity
  - Metrics: Backup success rate, backup age, restore test results
  - Alerts: Alert on backup failures, missing backups, failed restore tests
  - Retention: Track backup retention compliance

**Data Transfer Monitoring**:
- [ ] **Data Movement Logging**: Log data transfers
  - Events: Data copied, transferred, synchronized
  - Context: Source, destination, volume, user, timestamp
  - Alerts: Alert on large data transfers, unusual destinations
- [ ] **Cross-Border Transfer Monitoring**: Monitor data residency compliance
  - Detection: Data transferred outside permitted regions
  - Alerts: Alert on cross-border transfers violating data residency requirements
  - Purpose: GDPR compliance, data sovereignty

**Performance Monitoring**:
- [ ] **Classification Performance**: Monitor classification latency and throughput
  - Metrics: Documents classified per hour, latency per document
  - Targets: ≤100ms per document, ≥10,000 documents/hour
- [ ] **DLP Performance**: Monitor DLP scanning performance
  - Metrics: Scan latency, throughput, false positive rate
  - Targets: ≤100ms per document, ≤5% false positive rate
- [ ] **Query Performance**: Monitor data access performance
  - Metrics: Query latency, slow queries, connection pool usage
  - Optimization: Identify slow queries, add indexes, optimize

**Alerting and Response**:
- [ ] **Security Alerts**: Alert on critical data security events
  - Critical: Mass data exfiltration, public data exposure, encryption disabled
  - High: DLP violations, unauthorized access to Restricted data
  - Medium: Classification errors, compliance gaps
  - Routing: Page on-call for critical, ticket for high/medium
- [ ] **Compliance Alerts**: Alert on compliance violations
  - Events: Retention policy violations, GDPR deadline approaching, missing consent
  - Purpose: Ensure timely compliance, prevent violations

**Success Indicators**:
- Data access logging: 100% sensitive data access logged
- Classification accuracy: ≥90% classification accuracy maintained
- DLP effectiveness: ≥85% exfiltration attempts blocked, ≤5% false positives
- Privacy compliance: Zero privacy budget exhaustion incidents, zero user content leaks
- Compliance: 100% GDPR/CCPA requirements logged, zero violations

---

**Document Information**: Practice: Monitoring & Logging (ML) | Domain: Data | HAIAMM v2.1 | Last Updated: 2025-12-25
