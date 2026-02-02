# AI System Pre-Deployment Security Review

**Purpose:** Security questionnaire to complete before deploying AI systems to production.

**When to Use:**
- Before first production deployment
- Major version updates
- Significant architecture changes
- New integrations or data sources

**Time to Complete:** 30-60 minutes

**Related:** [Deployment Readiness Checklist](../checklists/deployment-readiness-checklist.md)

---

## System Information

| Field | Value |
|-------|-------|
| System Name | |
| Version | |
| Deployment Date | |
| Environment | ☐ Production ☐ Staging |
| System Type | ☐ LLM App ☐ AI Agent ☐ RAG ☐ ML Model ☐ Other |
| Risk Classification | ☐ High ☐ Medium ☐ Low |
| Reviewer | |
| System Owner | |

---

## Section 1: Design & Architecture

| # | Question | Yes | Partial | No | N/A | Notes |
|---|----------|-----|---------|-----|-----|-------|
| 1.1 | Is system architecture documented and current? | ☐ | ☐ | ☐ | ☐ | |
| 1.2 | Are data flows documented? | ☐ | ☐ | ☐ | ☐ | |
| 1.3 | Are trust boundaries clearly defined? | ☐ | ☐ | ☐ | ☐ | |
| 1.4 | Has a threat model been completed? | ☐ | ☐ | ☐ | ☐ | |
| 1.5 | Is least privilege applied to all components? | ☐ | ☐ | ☐ | ☐ | |
| 1.6 | Are external dependencies documented? | ☐ | ☐ | ☐ | ☐ | |
| 1.7 | Has design review been completed? | ☐ | ☐ | ☐ | ☐ | |

**Section 1 Score:** ___/14

---

## Section 2: Input Security

| # | Question | Yes | Partial | No | N/A | Notes |
|---|----------|-----|---------|-----|-----|-------|
| 2.1 | Is input length limited? | ☐ | ☐ | ☐ | ☐ | Max: ___ |
| 2.2 | Is input format validated? | ☐ | ☐ | ☐ | ☐ | |
| 2.3 | Is rate limiting implemented? | ☐ | ☐ | ☐ | ☐ | Rate: ___ |
| 2.4 | Are prompt injection patterns blocked? | ☐ | ☐ | ☐ | ☐ | |
| 2.5 | Is the system prompt protected from extraction? | ☐ | ☐ | ☐ | ☐ | |
| 2.6 | Is user input separated from system instructions? | ☐ | ☐ | ☐ | ☐ | |
| 2.7 | Are encoding attacks handled? | ☐ | ☐ | ☐ | ☐ | |
| 2.8 | Is content filtering applied to inputs? | ☐ | ☐ | ☐ | ☐ | |

**Section 2 Score:** ___/16

---

## Section 3: Output Security

| # | Question | Yes | Partial | No | N/A | Notes |
|---|----------|-----|---------|-----|-----|-------|
| 3.1 | Is output validated before delivery? | ☐ | ☐ | ☐ | ☐ | |
| 3.2 | Is PII filtered from outputs? | ☐ | ☐ | ☐ | ☐ | |
| 3.3 | Are sensitive patterns blocked? | ☐ | ☐ | ☐ | ☐ | |
| 3.4 | Is output length limited? | ☐ | ☐ | ☐ | ☐ | Max: ___ |
| 3.5 | Are error messages sanitized? | ☐ | ☐ | ☐ | ☐ | |
| 3.6 | Is harmful content filtered? | ☐ | ☐ | ☐ | ☐ | |
| 3.7 | Are hallucinations mitigated? | ☐ | ☐ | ☐ | ☐ | |
| 3.8 | Is output format validated? | ☐ | ☐ | ☐ | ☐ | |

**Section 3 Score:** ___/16

---

## Section 4: Authentication & Authorization

| # | Question | Yes | Partial | No | N/A | Notes |
|---|----------|-----|---------|-----|-----|-------|
| 4.1 | Is authentication required? | ☐ | ☐ | ☐ | ☐ | Method: |
| 4.2 | Is authorization enforced? | ☐ | ☐ | ☐ | ☐ | |
| 4.3 | Are API keys/secrets managed securely? | ☐ | ☐ | ☐ | ☐ | |
| 4.4 | Are secrets rotatable? | ☐ | ☐ | ☐ | ☐ | |
| 4.5 | Is session management secure? | ☐ | ☐ | ☐ | ☐ | |
| 4.6 | Are there no hardcoded credentials? | ☐ | ☐ | ☐ | ☐ | |
| 4.7 | Is audit logging enabled for access? | ☐ | ☐ | ☐ | ☐ | |

**Section 4 Score:** ___/14

---

## Section 5: Data Protection

| # | Question | Yes | Partial | No | N/A | Notes |
|---|----------|-----|---------|-----|-----|-------|
| 5.1 | Is data classified appropriately? | ☐ | ☐ | ☐ | ☐ | |
| 5.2 | Is data encrypted in transit (TLS)? | ☐ | ☐ | ☐ | ☐ | |
| 5.3 | Is data encrypted at rest? | ☐ | ☐ | ☐ | ☐ | |
| 5.4 | Is PII minimized? | ☐ | ☐ | ☐ | ☐ | |
| 5.5 | Are retention policies defined? | ☐ | ☐ | ☐ | ☐ | Period: |
| 5.6 | Is data deletion capability available? | ☐ | ☐ | ☐ | ☐ | |
| 5.7 | Is data lineage tracked? | ☐ | ☐ | ☐ | ☐ | |

**Section 5 Score:** ___/14

---

## Section 6: Agent/Tool Security (If Applicable)

*Complete if system includes AI agent capabilities or tool use.*

| # | Question | Yes | Partial | No | N/A | Notes |
|---|----------|-----|---------|-----|-----|-------|
| 6.1 | Are tool permissions explicitly defined? | ☐ | ☐ | ☐ | ☐ | |
| 6.2 | Is tool execution sandboxed? | ☐ | ☐ | ☐ | ☐ | |
| 6.3 | Are dangerous tools restricted? | ☐ | ☐ | ☐ | ☐ | |
| 6.4 | Is human approval required for sensitive actions? | ☐ | ☐ | ☐ | ☐ | |
| 6.5 | Are agent actions logged? | ☐ | ☐ | ☐ | ☐ | |
| 6.6 | Is there a kill switch? | ☐ | ☐ | ☐ | ☐ | |
| 6.7 | Can actions be rolled back? | ☐ | ☐ | ☐ | ☐ | |
| 6.8 | Are resource limits enforced? | ☐ | ☐ | ☐ | ☐ | |

**Section 6 Score:** ___/16 (or N/A)

---

## Section 7: Monitoring & Logging

| # | Question | Yes | Partial | No | N/A | Notes |
|---|----------|-----|---------|-----|-----|-------|
| 7.1 | Are all interactions logged? | ☐ | ☐ | ☐ | ☐ | |
| 7.2 | Are security events logged? | ☐ | ☐ | ☐ | ☐ | |
| 7.3 | Is log storage secured? | ☐ | ☐ | ☐ | ☐ | |
| 7.4 | Is log retention adequate (30+ days)? | ☐ | ☐ | ☐ | ☐ | |
| 7.5 | Are alerts configured for security events? | ☐ | ☐ | ☐ | ☐ | |
| 7.6 | Is anomaly detection enabled? | ☐ | ☐ | ☐ | ☐ | |
| 7.7 | Can incidents be investigated from logs? | ☐ | ☐ | ☐ | ☐ | |

**Section 7 Score:** ___/14

---

## Section 8: Testing & Validation

| # | Question | Yes | Partial | No | N/A | Notes |
|---|----------|-----|---------|-----|-----|-------|
| 8.1 | Has prompt injection testing been performed? | ☐ | ☐ | ☐ | ☐ | |
| 8.2 | Has jailbreak testing been performed? | ☐ | ☐ | ☐ | ☐ | |
| 8.3 | Has data extraction testing been performed? | ☐ | ☐ | ☐ | ☐ | |
| 8.4 | Have authentication tests passed? | ☐ | ☐ | ☐ | ☐ | |
| 8.5 | Have authorization tests passed? | ☐ | ☐ | ☐ | ☐ | |
| 8.6 | Are all critical/high findings resolved? | ☐ | ☐ | ☐ | ☐ | |
| 8.7 | Has implementation review been completed? | ☐ | ☐ | ☐ | ☐ | |
| 8.8 | Has load/stress testing been performed? | ☐ | ☐ | ☐ | ☐ | |

**Section 8 Score:** ___/16

---

## Section 9: Operational Readiness

| # | Question | Yes | Partial | No | N/A | Notes |
|---|----------|-----|---------|-----|-----|-------|
| 9.1 | Is runbook/playbook documented? | ☐ | ☐ | ☐ | ☐ | |
| 9.2 | Is incident response plan ready? | ☐ | ☐ | ☐ | ☐ | |
| 9.3 | Is rollback procedure documented and tested? | ☐ | ☐ | ☐ | ☐ | |
| 9.4 | Is emergency shutdown documented? | ☐ | ☐ | ☐ | ☐ | |
| 9.5 | Is on-call coverage established? | ☐ | ☐ | ☐ | ☐ | |
| 9.6 | Are escalation contacts current? | ☐ | ☐ | ☐ | ☐ | |
| 9.7 | Is monitoring verified working? | ☐ | ☐ | ☐ | ☐ | |

**Section 9 Score:** ___/14

---

## Assessment Summary

### Scores by Section

| Section | Score | Max | % | Pass |
|---------|-------|-----|---|------|
| 1. Design & Architecture | | 14 | | ☐ |
| 2. Input Security | | 16 | | ☐ |
| 3. Output Security | | 16 | | ☐ |
| 4. Auth & Authz | | 14 | | ☐ |
| 5. Data Protection | | 14 | | ☐ |
| 6. Agent/Tool (if applicable) | | 16 | | ☐ |
| 7. Monitoring & Logging | | 14 | | ☐ |
| 8. Testing & Validation | | 16 | | ☐ |
| 9. Operational Readiness | | 14 | | ☐ |
| **TOTAL** | | 134 | | |

### Pass Criteria

- Each section must score **≥70%** to pass
- **No critical findings** unresolved
- **All "must have" items** from deployment checklist complete

---

## Findings

### Critical (Must Resolve Before Deployment)

| # | Finding | Section | Owner | Status |
|---|---------|---------|-------|--------|
| 1 | | | | |
| 2 | | | | |

### High (Resolve Within 7 Days Post-Deploy)

| # | Finding | Section | Owner | Status |
|---|---------|---------|-------|--------|
| 1 | | | | |
| 2 | | | | |

### Medium (Resolve Within 30 Days)

| # | Finding | Section | Owner | Status |
|---|---------|---------|-------|--------|
| 1 | | | | |
| 2 | | | | |

---

## Decision

### Deployment Recommendation

- [ ] **Approved** - All criteria met
- [ ] **Approved with Conditions** - Deploy with specific mitigations
- [ ] **Not Approved** - Critical issues must be resolved

### Conditions (if applicable)

1.
2.
3.

### Risk Acceptance (if applicable)

| Risk | Accepted By | Date | Expiration |
|------|-------------|------|------------|
| | | | |

---

## Sign-Off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Security Reviewer | | | |
| System Owner | | | |
| Engineering Lead | | | |

---

## Post-Deployment

- [ ] 24-hour monitoring review scheduled
- [ ] 7-day review scheduled
- [ ] 30-day review scheduled
- [ ] Findings tracked in issue system

---

## Document Information

| Field | Value |
|-------|-------|
| HAIAMM Version | 2.0 |
| Questionnaire Version | 1.0 |
| Last Updated | January 2026 |
