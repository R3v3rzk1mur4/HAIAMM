# Design Review Practice – Vendors Domain
## HAIAMM v2.1 One-Pager

### Practice Overview

Design Review for Vendors ensures AI vendor risk management system designs handle scale (thousands of vendors), limited visibility (vendor systems are black boxes), and regulatory complexity.

**Scope**: Reviews for AI vendor risk systems covering risk assessment models, multi-source data integration, continuous monitoring, SBOM analysis, compliance automation, and vendor ecosystem intelligence.

---

### Level 1: Foundational Design Review

**Key Review Criteria**:

**Risk Assessment Design**:
- [ ] Multi-factor risk scoring model (security posture, data handling, compliance, incidents, financials)
- [ ] ML classification approach (vendor risk tier: Critical, High, Medium, Low)
- [ ] Risk prioritization logic (vendor risk × business criticality)
- [ ] Accuracy targets (≥85% agreement with human experts)

**Data Integration Design**:
- [ ] Multi-source integration (questionnaires, security ratings, breach databases, SBOMs, threat intel)
- [ ] Vendor entity resolution strategy (match same vendor across sources)
- [ ] Data normalization approach (common vendor schema)
- [ ] API integration design (BitSight, SecurityScorecard, breach APIs)

**Continuous Monitoring Design**:
- [ ] Event-driven vs polling architecture (vendor status changes)
- [ ] Monitoring frequency by vendor tier (Critical: daily, High: weekly, Medium: monthly)
- [ ] Change detection design (rating drops, breaches, certification expiration)
- [ ] Alert latency targets (breach detection ≤24 hours)

**SBOM Analysis Design**:
- [ ] SBOM collection architecture (vendor portal, API integration, metadata extraction)
- [ ] SBOM parsing support (SPDX, CycloneDX formats)
- [ ] Vulnerability scanning design (CVE matching, transitive dependency analysis ≥5 levels)
- [ ] Supply chain attack detection (typosquatting, suspicious packages, anomalous updates)

**Compliance Automation Design**:
- [ ] Regulatory requirement mapping (jurisdiction detection, requirement database)
- [ ] Automated compliance checking (contract analysis, evidence collection)
- [ ] Multi-jurisdiction support (GDPR, CCPA, HIPAA, PCI-DSS)
- [ ] Compliance reporting design (auto-generate audit reports)

**Vendor Ecosystem Design**:
- [ ] Dependency network mapping (vendor → subprocessors → sub-subprocessors ≥3 levels)
- [ ] Concentration risk detection (shared subprocessors, single points of failure)
- [ ] Graph database design for dependencies

**Success Indicators**:
- 100% of vendor AI designs reviewed
- Coverage targets met: ≥95% of vendors assessed, ≥80% SBOM coverage for software vendors
- Compliance: Zero vendor-related regulatory violations from design flaws

---

**Document Information**: Practice: Design Review (DR) | Domain: Vendors | HAIAMM v2.1 | Last Updated: 2025-12-25
