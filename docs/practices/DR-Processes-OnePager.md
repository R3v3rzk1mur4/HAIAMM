# Design Review Practice – Processes Domain
## HAIAMM v2.1 One-Pager

### Practice Overview

Design Review for Processes ensures AI security orchestration and automation designs are safe, reliable, and maintainable while enabling rapid incident response.

**Scope**: Reviews for AI SOAR systems covering alert triage, orchestration engine, safety mechanisms, multi-tool integration, human oversight, and resilience.

---

### Level 1: Foundational Design Review

**Key Review Criteria**:

**Alert Triage Design**:
- [ ] ML model design for classification (true positive, false positive, requires investigation)
- [ ] Accuracy targets (≥95% true positive detection, ≥70% precision)
- [ ] Severity scoring approach (AI adjusts severity based on context)
- [ ] Priority assignment logic

**Orchestration Engine Design**:
- [ ] Playbook execution architecture (DAG-based workflows)
- [ ] Multi-tool coordination design (parallel execution, error handling)
- [ ] State management approach (workflow state persistence)
- [ ] Timeout and retry logic

**Safety Architecture Design**:
- [ ] Graduated automation levels (alert-only, recommend, auto-execute reversible, auto-execute irreversible)
- [ ] Blast radius limits (network blocks ≤50 IPs, account disables ≤20, system isolations ≤5)
- [ ] Change validation design (pre-change simulation, post-change verification)
- [ ] Rollback mechanisms (automated rollback for failed actions)

**Integration Design**:
- [ ] Security tool coverage (SIEM, EDR, firewall, cloud, ticketing - ≥80% of org tools)
- [ ] API integration patterns (query, action, webhook)
- [ ] Error handling (circuit breaker, retry with exponential backoff)
- [ ] Data normalization strategy (common schema like OCSF, ECS)

**Human Oversight Design**:
- [ ] Approval workflows (high-risk actions require human approval)
- [ ] Escalation architecture (tiered escalation based on severity)
- [ ] Override mechanisms (analysts can override AI decisions)
- [ ] Spot-check auditing (≥10% random sample of autonomous actions)

**Resilience Design**:
- [ ] Graceful degradation (behavior when AI or tools fail)
- [ ] Queue architecture (handle demand spikes without loss)
- [ ] Health monitoring (service availability, model performance, integration health)

**Success Indicators**:
- 100% of SOAR designs reviewed
- Safety validated: Zero production outages from AI automation
- Performance targets: MTTR ≤10 hours, ≥70% automation rate

---

**Document Information**: Practice: Design Review (DR) | Domain: Processes | HAIAMM v2.1 | Last Updated: 2025-12-25
