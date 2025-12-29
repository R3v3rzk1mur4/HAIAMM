# Design Review Practice – Data Domain
## HAIAMM v2.1 One-Pager

### Practice Overview

Design Review for Data domain ensures AI data security system designs protect sensitive data while enabling business operations, maintaining privacy, and ensuring regulatory compliance.

**Scope**: Reviews for AI data security (classification, DLP, privacy automation) covering classification models, multi-channel DLP, privacy-preserving AI, compliance automation, and data lineage.

---

### Level 1: Foundational Design Review

**Key Review Criteria**:

**Classification Design**:
- [ ] Multi-modal classification (text, images, structured data approaches)
- [ ] Classification accuracy targets (≥92% structured, ≥88% unstructured data)
- [ ] Context-aware classification design (same data, different sensitivity in different contexts)
- [ ] Real-time vs batch classification strategy

**DLP Architecture Design**:
- [ ] Multi-channel coverage (email, endpoint, network, cloud DLP)
- [ ] Inline vs out-of-band design (real-time blocking vs post-analysis)
- [ ] Policy engine design (centralized policy management)
- [ ] False positive reduction strategy (≤8% target)

**Privacy-Preserving AI Design**:
- [ ] Data minimization in AI processing (metadata-only analysis where possible)
- [ ] AI service account access controls (read-only, least privilege)
- [ ] Anonymization of training data (no actual PII in models)
- [ ] Differential privacy integration (privacy budget ε ≤10)

**Compliance Automation Design**:
- [ ] GDPR automation (Article 15 Access, Article 17 Deletion, Article 20 Portability)
- [ ] CCPA automation (Do Not Sell tracking, consumer rights)
- [ ] Data retention enforcement design (auto-delete beyond retention)
- [ ] Multi-jurisdiction support (GDPR, CCPA, HIPAA, PCI-DSS)

**Data Lineage Design**:
- [ ] Automated lineage discovery approach
- [ ] Data flow mapping strategy
- [ ] Cross-border flow detection (GDPR/PIPL compliance)

**Success Indicators**:
- 100% of data AI designs reviewed
- Privacy-by-design validated: Zero AI-caused data exposure incidents
- Compliance targets met: DSAR fulfillment in ≤7 days (vs 30-day legal limit)

---

**Document Information**: Practice: Design Review (DR) | Domain: Data | HAIAMM v2.1 | Last Updated: 2025-12-25
