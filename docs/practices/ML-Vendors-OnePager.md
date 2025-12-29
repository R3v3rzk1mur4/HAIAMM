# Monitoring & Logging Practice – Vendors Domain
## HAIAMM v2.1 One-Pager

### Practice Overview

Monitoring & Logging for Vendors ensures AI vendor risk management systems have comprehensive observability for vendor risk assessments, security incidents, SBOM analysis, and compliance—capturing all vendor security events and risk changes for timely response, compliance, and vendor accountability.

---

### Level 1: Key Monitoring & Logging Activities

**Vendor Risk Assessment Logging**:
- [ ] **Risk Score Calculations**: Log AI risk scoring decisions
  - Events: Vendor assessed, risk score calculated, risk tier assigned
  - Context: Vendor, risk factors (security posture, breaches, compliance), score, tier (Critical/High/Medium/Low)
  - Purpose: Audit risk assessments, validate model accuracy
- [ ] **Risk Score Changes**: Log vendor risk score updates
  - Events: Risk score increased/decreased, tier changed
  - Context: Vendor, old score, new score, reason (breach, rating drop, remediation)
  - Alerts: Alert on risk score increases, tier escalations
- [ ] **Manual Risk Overrides**: Log analyst manual risk adjustments
  - Context: Vendor, AI score, analyst score, justification
  - Purpose: Identify scoring errors, improve risk model

**Vendor Security Incident Logging**:
- [ ] **Breach Detection**: Log vendor security breaches
  - Events: Breach detected, source (breach database, disclosure, threat intel)
  - Context: Vendor, breach date, breach type, data exposed, detection latency
  - Alerts: Alert within ≤24 hours of breach disclosure
  - Purpose: Rapid response, impact assessment
- [ ] **Incident Response Tracking**: Log response to vendor incidents
  - Events: Incident assessed, impact determined, vendor contacted, remediation required
  - Context: Vendor, incident, impact on organization, remediation timeline
  - SLA Tracking: Monitor vendor remediation against SLA (Critical ≤30 days, High ≤60 days)
- [ ] **Incident Resolution**: Log incident closure
  - Context: Vendor, incident, remediation completed, verification evidence
  - Purpose: Track vendor responsiveness, compliance

**Vendor Monitoring Events**:
- [ ] **Security Rating Changes**: Log vendor security rating updates
  - Sources: BitSight, SecurityScorecard, RiskRecon
  - Events: Rating increased/decreased, thresholds crossed
  - Alerts: Alert on rating drops (≥10 point decrease)
- [ ] **Certification Changes**: Log vendor certification status changes
  - Events: Certification obtained, renewed, expired, revoked
  - Context: Vendor, certification type (ISO 27001, SOC 2, PCI-DSS)
  - Alerts: Alert on certification expiration (≤30 days), revocation
- [ ] **Vendor Status Changes**: Log vendor lifecycle events
  - Events: Vendor onboarded, contract renewed, contract terminated
  - Context: Vendor, status change, reason, timestamp
  - Purpose: Track vendor portfolio, compliance

**SBOM Analysis Logging**:
- [ ] **SBOM Ingestion**: Log SBOM collection and processing
  - Events: SBOM received, parsed, vulnerabilities scanned
  - Context: Vendor, SBOM format (SPDX, CycloneDX), component count, vulnerability count
  - Purpose: Track SBOM coverage (target: ≥80% software vendors)
- [ ] **Vulnerability Discovery**: Log vulnerabilities found in vendor SBOMs
  - Events: CVE detected in vendor software, severity, affected versions
  - Context: Vendor, component, CVE ID, CVSS score, exploitability
  - Alerts: Alert on critical/high vulnerabilities in vendor software
- [ ] **Vendor Notification**: Log vulnerability notifications to vendors
  - Events: Vendor notified, acknowledgment received, remediation deadline set
  - Context: Vendor, CVE, severity, SLA deadline
  - Purpose: Track vendor response times, compliance

**Supply Chain Monitoring**:
- [ ] **Subprocessor Tracking**: Log vendor subprocessor changes
  - Events: New subprocessor added, subprocessor removed, subprocessor changed
  - Context: Vendor, subprocessor, depth level, approval status
  - Alerts: Alert on new critical subprocessors, unapproved subprocessors
- [ ] **Dependency Risk Monitoring**: Monitor shared dependencies
  - Events: Vulnerable component shared by multiple vendors detected
  - Context: Component, vulnerability, affected vendors count
  - Alerts: Alert on concentration risk (single point of failure)

**Compliance Monitoring**:
- [ ] **Regulatory Compliance Tracking**: Monitor vendor compliance status
  - Requirements: GDPR, CCPA, HIPAA, PCI-DSS per applicable regulations
  - Events: Compliance verified, compliance gap detected, certification obtained
  - Alerts: Alert on compliance violations, certification expirations
- [ ] **Contract Compliance Monitoring**: Monitor vendor SLA compliance
  - Metrics: Vulnerability remediation SLA, incident response SLA, uptime SLA
  - Events: SLA met, SLA missed, SLA breach
  - Alerts: Alert on SLA violations, escalate to vendor management
- [ ] **Data Processing Agreement (DPA) Monitoring**: Track DPA compliance
  - Events: DPA signed, DPA updated, DPA breach detected
  - Purpose: GDPR compliance, vendor accountability

**Vendor Data Access Logging**:
- [ ] **Platform Access**: Log access to vendor risk management platform
  - Events: User login, vendor data viewed, risk assessment modified
  - Context: User, action, vendor, timestamp
  - Purpose: Audit trail, insider threat detection
- [ ] **Vendor Portal Access**: Log vendor self-service portal access
  - Events: Vendor login, questionnaire submitted, SBOM uploaded
  - Context: Vendor, action, timestamp
  - Purpose: Track vendor engagement, audit trail

**Integration Logging**:
- [ ] **Third-Party Integration Activity**: Log vendor data source API calls
  - Integrations: BitSight, SecurityScorecard, breach databases, SBOM repositories
  - Events: API call, endpoint, response, data retrieved
  - Errors: Log API failures, rate limiting, authentication errors
  - Purpose: Debug integration issues, validate data freshness
- [ ] **Data Synchronization**: Log vendor data updates
  - Events: Vendor data synchronized, source, records updated
  - Context: Source, vendor count, updates applied, timestamp
  - Purpose: Track data freshness, validate automation

**Performance Monitoring**:
- [ ] **Risk Assessment Performance**: Monitor assessment throughput
  - Metrics: Vendors assessed per hour, assessment latency
  - Targets: ≥100 vendors/hour, ≤5 minutes per vendor
- [ ] **SBOM Scanning Performance**: Monitor SBOM analysis throughput
  - Metrics: SBOMs scanned per hour, vulnerabilities identified
  - Targets: ≥50 SBOMs/hour
- [ ] **Monitoring Coverage**: Track vendor monitoring coverage
  - Metrics: % vendors monitored, monitoring frequency by tier
  - Targets: 100% vendors monitored, Critical daily, High weekly, Medium monthly

**Alerting and Response**:
- [ ] **Vendor Security Alerts**: Alert on critical vendor events
  - Critical: Vendor breach, critical vulnerability in vendor software, vendor de-certified
  - High: Vendor rating drop, high vulnerability, SLA violation
  - Medium: Certification expiration, compliance gap
  - Routing: Page on-call for critical vendor incidents
- [ ] **Vendor Risk Escalation**: Escalate high-risk vendors
  - Triggers: Risk score exceeds threshold, major breach, repeated violations
  - Process: Alert vendor management, contract review, potential termination

**Vendor Metrics and Reporting**:
- [ ] **Vendor Security Dashboard**: Real-time vendor risk visibility
  - Metrics: Vendor risk distribution, breaches, vulnerabilities, compliance status
  - Trends: Risk score trends, incident trends, compliance trends
- [ ] **Executive Reporting**: Periodic vendor risk reports
  - Content: High-risk vendors, recent breaches, remediation status, SBOM coverage
  - Audience: CISO, procurement, vendor management, legal

**Audit and Compliance Logging**:
- [ ] **Vendor Audit Logging**: Log vendor audit activities
  - Events: Audit scheduled, audit performed, audit findings, remediation
  - Context: Vendor, audit type (SOC 2, penetration test), findings, remediation
  - Purpose: Track vendor audit compliance, evidence for regulators
- [ ] **Vendor Termination Logging**: Log vendor offboarding
  - Events: Contract terminated, data deletion requested, deletion verified
  - Context: Vendor, termination reason, data deletion evidence
  - Purpose: Compliance evidence, audit trail

**Success Indicators**:
- Monitoring coverage: 100% of vendors monitored, ≥95% monitored per tier frequency
- Breach detection: All vendor breaches detected within ≤24 hours
- SBOM coverage: ≥80% of software vendors provide SBOMs
- Vulnerability tracking: 100% of vendor vulnerabilities logged, tracked to remediation
- Compliance: 100% of compliance events logged, zero regulatory violations

---

**Document Information**: Practice: Monitoring & Logging (ML) | Domain: Vendors | HAIAMM v2.1 | Last Updated: 2025-12-25
