# Design Review Practice – Infrastructure Domain
## HAIAMM v2.1 One-Pager

### Practice Overview

Design Review for Infrastructure domain ensures AI-powered cloud and network security system designs are reviewed for multi-cloud support, safe remediation, scalability, and blast radius protection before implementation.

**Scope**: Reviews for AI infrastructure security (CSPM, network detection, IaC security) covering model design, multi-cloud integration, remediation safety, real-time detection architecture, and infrastructure deployment.

---

### Level 1: Foundational Design Review

**Key Review Criteria**:

**Multi-Cloud Design**:
- [ ] Cloud provider coverage defined (AWS, Azure, GCP support requirements)
- [ ] API integration design for each cloud (read vs write access)
- [ ] Resource discovery architecture (how discover all cloud resources?)
- [ ] Cross-cloud normalization strategy (common risk scoring framework)

**Remediation Safety Design**:
- [ ] Graduated automation levels defined (alert-only, auto-remediate low-risk, manual high-risk)
- [ ] Blast radius limits documented (max resources affected per remediation)
- [ ] Change validation designed (pre-change impact assessment, post-change verification)
- [ ] Rollback mechanisms designed (how undo failed remediations?)

**Detection Architecture**:
- [ ] Real-time detection design (streaming vs polling, latency requirements)
- [ ] Configuration baseline approach (how establish "good" state?)
- [ ] Anomaly detection strategy (unsupervised learning for unusual configurations)
- [ ] Alert correlation design (cross-resource, cross-cloud)

**Infrastructure Deployment**:
- [ ] Deployment model selected (cloud-native, on-premise, hybrid)
- [ ] Scalability strategy (handle millions of cloud resources)
- [ ] High availability design (multi-region, failover)
- [ ] Performance targets (scan X resources in Y time)

**Success Indicators**:
- 100% of infrastructure AI designs reviewed before implementation
- ≥90% of designs approved without major rework
- Zero production incidents from design flaws in first 6 months

---

**Document Information**: Practice: Design Review (DR) | Domain: Infrastructure | HAIAMM v2.1 | Last Updated: 2025-12-25
