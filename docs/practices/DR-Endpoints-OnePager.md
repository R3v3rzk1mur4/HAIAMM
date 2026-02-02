# Design Review Practice – Endpoints Domain
## HAIAMM v2.0 One-Pager

### Practice Overview

Design Review for Endpoints ensures AI endpoint security system designs balance comprehensive threat detection with device performance, user privacy, and cross-platform support.

**Scope**: Reviews for AI endpoint security (EDR/XDR, behavioral analytics) covering on-device vs cloud analysis, privacy-preserving telemetry, automated response safety, and cross-platform architecture.

---

### Level 1: Foundational Design Review

**Key Review Criteria**:

**AI Detection Design**:
- [ ] On-device model design (lightweight models, resource constraints ≤5% CPU, ≤200MB memory)
- [ ] Cloud analysis design (heavy models, accuracy vs latency trade-offs)
- [ ] Hybrid approach justified (what runs on-device vs cloud?)
- [ ] Behavioral analytics design (UEBA, anomaly detection baseline approach)

**Privacy-Preserving Design**:
- [ ] Data minimization strategy (collect only security-relevant data, not user content)
- [ ] BYOD privacy protection (work/personal data separation)
- [ ] GDPR compliance design (data retention ≤90 days, right to deletion)
- [ ] Differential privacy considered (aggregate telemetry anonymization)

**Response Safety Design**:
- [ ] Automated response levels defined (alert, isolate, remediate, reimage)
- [ ] User notification design (when warn user before action?)
- [ ] False positive handling (user override process, rollback capabilities)
- [ ] Blast radius limits (max endpoints affected per auto-response)

**Cross-Platform Design**:
- [ ] Platform coverage (Windows, macOS, Linux, iOS, Android)
- [ ] Platform-specific constraints addressed (macOS ESF, Linux eBPF, mobile app sandboxing)
- [ ] Unified detection logic with platform-specific implementations
- [ ] Agent update mechanism (OTA updates, staged rollout, rollback)

**Success Indicators**:
- 100% of endpoint AI designs reviewed
- Performance targets met: ≤5% CPU, ≤200MB memory, ≤3% battery impact
- Privacy compliance: Zero GDPR violations from design

---

**Document Information**: Practice: Design Review (DR) | Domain: Endpoints | HAIAMM v2.0 | Last Updated: 2025-12-25
