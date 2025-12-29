# Security Testing Practice – Vendors Domain
## HAIAMM v2.1 One-Pager

### Practice Overview

Security Testing for Vendors validates that AI vendor risk management systems correctly assess vendor risk, integrate data sources reliably, detect security incidents promptly, analyze SBOMs accurately, and maintain compliance at scale.

---

### Level 1: Key Testing Criteria

**Risk Assessment Testing**:
- [ ] **Risk Scoring Accuracy Testing**: Test risk score agreement with experts
  - Test Dataset: 100+ vendors with expert-assigned risk scores
  - Success Criteria: ≥85% agreement with expert assessments
- [ ] **Risk Tier Classification Testing**: Test vendor tier assignment
  - Success Criteria: ≥90% accuracy on tier classification (Critical/High/Medium/Low)
- [ ] **Risk Prioritization Testing**: Test vendor risk × business criticality
  - Success Criteria: High-priority vendors correctly identified for immediate review

**Data Integration Testing**:
- [ ] **Multi-Source Integration Testing**: Test all data source integrations
  - Sources: Questionnaires, BitSight, SecurityScorecard, breach databases, SBOMs, threat intel
  - Success Criteria: All sources integrate correctly, handle API errors gracefully
- [ ] **Entity Resolution Testing**: Test vendor matching across sources
  - Success Criteria: ≥95% accuracy matching same vendor across sources
- [ ] **Data Normalization Testing**: Test common schema mapping
  - Success Criteria: All vendor data correctly normalized to common format

**Continuous Monitoring Testing**:
- [ ] **Change Detection Testing**: Test detection of vendor status changes
  - Changes: Security rating drops, breaches, certification expiration, M&A activity
  - Success Criteria: All critical changes detected within ≤24 hours
- [ ] **Alert Latency Testing**: Test breach detection speed
  - Success Criteria: Vendor breaches detected ≤24 hours from public disclosure
- [ ] **Monitoring Frequency Testing**: Test tier-based monitoring
  - Success Criteria: Critical vendors monitored daily, High weekly, Medium monthly

**SBOM Analysis Testing**:
- [ ] **SBOM Parsing Testing**: Test SBOM format support
  - Formats: SPDX, CycloneDX
  - Success Criteria: 100% of valid SBOMs parsed correctly
- [ ] **Vulnerability Scanning Testing**: Test CVE matching accuracy
  - Test Dataset: Known vulnerable packages, clean packages
  - Success Criteria: ≥95% vulnerable package detection, ≤5% false positives
- [ ] **Transitive Dependency Testing**: Test dependency graph depth
  - Success Criteria: Dependencies traced ≥5 levels deep
- [ ] **Supply Chain Attack Testing**: Test detection of malicious packages
  - Tests: Typosquatting, suspicious package updates, anomalous behavior
  - Success Criteria: ≥80% of supply chain attack indicators detected

**Compliance Testing**:
- [ ] **Regulatory Mapping Testing**: Test jurisdiction detection
  - Success Criteria: Correct regulatory requirements identified for all jurisdictions
- [ ] **Automated Compliance Checking**: Test contract analysis
  - Success Criteria: ≥85% of compliance gaps detected automatically
- [ ] **Multi-Jurisdiction Testing**: Test GDPR, CCPA, HIPAA, PCI-DSS support
  - Success Criteria: All regulatory requirements validated correctly
- [ ] **Compliance Reporting Testing**: Test audit report generation
  - Success Criteria: Reports contain all required evidence, exportable formats

**Vendor Ecosystem Testing**:
- [ ] **Dependency Mapping Testing**: Test subprocessor discovery
  - Success Criteria: Dependencies mapped ≥3 levels deep (vendor → subprocessor → sub-subprocessor)
- [ ] **Concentration Risk Testing**: Test shared dependency detection
  - Success Criteria: All single points of failure identified
- [ ] **Graph Database Testing**: Test dependency graph queries
  - Success Criteria: Graph queries complete ≤1 second for typical org (1,000 vendors)

**Performance and Scalability Testing**:
- [ ] **Vendor Scale Testing**: Test system with large vendor portfolio
  - Success Criteria: Supports ≥1,000 vendors without degradation
- [ ] **Assessment Throughput Testing**: Test vendor assessments per hour
  - Success Criteria: ≥100 vendor assessments/hour
- [ ] **SBOM Processing Testing**: Test SBOM analysis throughput
  - Success Criteria: ≥50 SBOMs/hour

**Adversarial Testing**:
- [ ] **Risk Score Manipulation Testing**: Test if vendors can game risk scores
  - Method: Simulate vendor attempts to inflate scores
  - Success Criteria: ≥80% of gaming attempts detected
- [ ] **Data Source Poisoning Testing**: Test robustness against bad data
  - Method: Inject false vendor information into sources
  - Success Criteria: Bad data detected, flagged for review

**Resilience Testing**:
- [ ] **Data Source Failure Testing**: Test behavior when sources unavailable
  - Success Criteria: System continues with available sources, alerts on missing data
- [ ] **API Rate Limit Testing**: Test handling of API throttling
  - Success Criteria: Graceful backoff, retry logic works correctly
- [ ] **Breach Database Lag Testing**: Test staleness detection
  - Success Criteria: Alerts when breach data >7 days old

**Success Indicators**:
- Risk assessment accuracy: ≥85% agreement with expert assessments
- Coverage: ≥95% of vendors assessed, ≥80% SBOM coverage for software vendors
- Monitoring: Breach detection ≤24 hours, all critical changes detected
- Compliance: 100% of regulatory requirements validated in testing
- Scale: Supports ≥1,000 vendors with ≥99.9% system availability

---

**Document Information**: Practice: Security Testing (ST) | Domain: Vendors | HAIAMM v2.1 | Last Updated: 2025-12-25
