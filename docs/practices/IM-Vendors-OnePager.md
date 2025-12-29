# Issue Management Practice – Vendors Domain
## HAIAMM v2.1 One-Pager

### Practice Overview

Issue Management for Vendors ensures AI vendor risk management systems systematically identify, assess, prioritize, and remediate vulnerabilities in vendor systems, vendor-provided software (SBOMs), and vendor risk management platforms themselves.

---

### Level 1: Key Issue Management Activities

**Vendor Platform Vulnerabilities**:
- [ ] **Vendor Risk Platform Scanning**: Scan vendor risk management platforms
  - Platforms: BitSight, SecurityScorecard, RiskRecon, Prevalent
  - Coverage: Platform CVEs, API vulnerabilities, misconfigurations
  - Frequency: Daily CVE monitoring, weekly configuration scans
  - SLA: Critical platform CVEs ≤24 hours, High ≤7 days
- [ ] **Platform Integration Security**: Secure integrations with vendor data sources
  - Sources: Questionnaire systems, breach databases, SBOM repositories, threat intel feeds
  - Coverage: API authentication, authorization, injection vulnerabilities, credential security
  - Testing: API security scanning, penetration testing

**Vendor Software Vulnerabilities (SBOM)**:
- [ ] **SBOM Vulnerability Scanning**: Scan vendor-provided SBOMs for CVEs
  - Scope: All vendor-provided software, cloud services, SaaS dependencies
  - Tools: SBOM analysis tools, CVE databases (NVD, OSV)
  - Frequency: Daily SBOM scans, immediate scan on new SBOM ingestion
  - Coverage: Direct dependencies + transitive dependencies (≥5 levels deep)
- [ ] **Vulnerability Prioritization**: Prioritize vendor software vulnerabilities
  - Factors: Vendor criticality, exploitability, affected components, compensating controls
  - SLA: Critical vendor vulnerabilities ≤48 hours (vendor response), High ≤7 days
- [ ] **Vendor Notification**: Notify vendors of vulnerabilities in their software
  - Process: Identify vulnerability → notify vendor → track remediation → verify fix
  - Escalation: Escalate to vendor management if remediation SLA missed

**Vendor Security Incident Tracking**:
- [ ] **Breach Monitoring**: Monitor vendor security breaches
  - Sources: Breach databases, vendor disclosures, threat intel, news monitoring
  - Frequency: Real-time monitoring, alerts within ≤24 hours of disclosure
  - Response: Assess impact → notify stakeholders → require vendor remediation plan
- [ ] **Vendor Incident Response**: Track vendor incident remediation
  - Tracking: Vendor incident response timeline, remediation steps, verification
  - SLA: Critical vendor incidents require remediation plan ≤48 hours
  - Validation: Verify vendor remediation (request evidence, audit, testing)

**Vendor Risk Score Impact**:
- [ ] **Vulnerability-Driven Risk Adjustment**: Update vendor risk scores based on vulnerabilities
  - Impact: Critical vulnerabilities increase vendor risk score
  - Triggers: Major breach, unpatched critical CVE >30 days, repeated security incidents
  - Outcome: Risk score increase → enhanced monitoring, remediation requirements, vendor review
- [ ] **Remediation Tracking**: Track vendor vulnerability remediation
  - Metrics: Vendor MTTR, % vulnerabilities remediated within SLA, repeat vulnerabilities
  - Reporting: Vendor security scorecards, executive dashboards

**Supply Chain Issue Management**:
- [ ] **Subprocessor Vulnerabilities**: Track vulnerabilities in vendor subprocessors
  - Scope: Vendor dependencies (≥3 levels: vendor → subprocessor → sub-subprocessor)
  - Process: Request subprocessor SBOMs, scan for vulnerabilities, track remediation
  - Risk: Subprocessor vulnerability impacts vendor, impacts your organization
- [ ] **Dependency Concentration Risk**: Identify shared vulnerable components
  - Detection: Same vulnerable library used by multiple vendors
  - Risk: Single vulnerability affects multiple vendors simultaneously
  - Mitigation: Diversify vendors, implement compensating controls

**Remediation Workflows**:
- [ ] **Vendor Remediation Requests**: Request vendors remediate vulnerabilities
  - Process: Identify vulnerability → notify vendor → set remediation deadline → track progress
  - SLA: Critical vendor vulnerabilities ≤30 days, High ≤60 days
  - Escalation: Escalate to vendor account manager, contract review if SLA missed
- [ ] **Compensating Controls**: Implement controls when vendor remediation delayed
  - Examples: Enhanced monitoring, network segmentation, input validation, rate limiting
  - Documentation: Track compensating controls, remove when vendor patches
- [ ] **Vendor Contract Review**: Review contracts for persistent security issues
  - Triggers: Repeated vulnerabilities, missed remediation SLAs, major breaches
  - Options: Renegotiate security terms, add security requirements, consider vendor replacement

**Vulnerability Metrics**:
- [ ] **Vendor Vulnerability Count**: Track vulnerabilities per vendor
  - Breakdown: By severity (Critical, High, Medium, Low), by vendor
  - Trend: Decreasing vulnerabilities indicates improving vendor security
- [ ] **Vendor MTTR**: Mean time for vendors to remediate vulnerabilities
  - Target: Critical ≤30 days, High ≤60 days
  - Benchmark: Compare vendor MTTR against industry averages
- [ ] **SBOM Coverage**: % vendors providing SBOMs
  - Target: ≥80% of software vendors provide SBOMs
  - Trend: Increasing SBOM adoption improves supply chain visibility
- [ ] **Breach Impact**: Vendors affected by security breaches
  - Metric: % vendors with security incidents in past 12 months
  - Target: ≤10% of vendors with incidents

**Success Indicators**:
- SBOM coverage: ≥80% of software vendors provide SBOMs
- Vulnerability detection: Vendor vulnerabilities detected within ≤24 hours
- Vendor MTTR: Critical ≤30 days, High ≤60 days
- Breach response: All vendor breaches assessed within ≤24 hours

---

**Document Information**: Practice: Issue Management (IM) | Domain: Vendors | HAIAMM v2.1 | Last Updated: 2025-12-25
