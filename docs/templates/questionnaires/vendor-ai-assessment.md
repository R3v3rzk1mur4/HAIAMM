# Vendor AI Assessment Questionnaire

**Purpose:** Evaluate third-party AI services, models, and vendors for security risks.

**When to Use:**
- Evaluating new AI vendors or services
- Annual vendor security review
- Before integrating third-party AI/ML models
- Assessing AI API providers

**Time to Complete:** 1-2 hours (may require vendor input)

---

## Vendor Information

| Field | Value |
|-------|-------|
| Vendor Name | |
| Product/Service | |
| Assessment Date | |
| Assessor | |
| Business Owner | |
| Contract Value | |
| Data Classification | ☐ Public ☐ Internal ☐ Confidential ☐ Restricted |

---

## Section 1: Company & Compliance

### 1.1 Company Background

| # | Question | Response | Notes |
|---|----------|----------|-------|
| 1.1.1 | How long has the vendor been providing AI services? | | |
| 1.1.2 | What is the vendor's primary business? | | |
| 1.1.3 | Where is the vendor headquartered? | | |
| 1.1.4 | Where is data processed/stored geographically? | | |
| 1.1.5 | Does the vendor have AI-specific security certifications? | | |

### 1.2 Compliance & Certifications

| # | Question | Yes | No | N/A | Evidence |
|---|----------|-----|-----|-----|----------|
| 1.2.1 | Is the vendor SOC 2 Type II certified? | ☐ | ☐ | ☐ | |
| 1.2.2 | Is the vendor ISO 27001 certified? | ☐ | ☐ | ☐ | |
| 1.2.3 | Does the vendor comply with GDPR? | ☐ | ☐ | ☐ | |
| 1.2.4 | Does the vendor comply with CCPA? | ☐ | ☐ | ☐ | |
| 1.2.5 | Is the vendor compliant with EU AI Act (if applicable)? | ☐ | ☐ | ☐ | |
| 1.2.6 | Does the vendor have a public security policy? | ☐ | ☐ | ☐ | |
| 1.2.7 | Does the vendor undergo regular penetration testing? | ☐ | ☐ | ☐ | |
| 1.2.8 | Can the vendor provide audit reports? | ☐ | ☐ | ☐ | |

**Section 1 Score:** ___/16

---

## Section 2: Data Handling

### 2.1 Data Processing

| # | Question | Response | Risk Level |
|---|----------|----------|------------|
| 2.1.1 | What data will be sent to the vendor's AI service? | | ☐H ☐M ☐L |
| 2.1.2 | Is data used to train or improve the vendor's models? | | ☐H ☐M ☐L |
| 2.1.3 | Can training on customer data be disabled? | | ☐H ☐M ☐L |
| 2.1.4 | How long is data retained by the vendor? | | ☐H ☐M ☐L |
| 2.1.5 | Can data be deleted on request? | | ☐H ☐M ☐L |

### 2.2 Data Security

| # | Question | Yes | No | N/A | Evidence |
|---|----------|-----|-----|-----|----------|
| 2.2.1 | Is data encrypted in transit (TLS 1.2+)? | ☐ | ☐ | ☐ | |
| 2.2.2 | Is data encrypted at rest? | ☐ | ☐ | ☐ | |
| 2.2.3 | Are customer data isolated from other customers? | ☐ | ☐ | ☐ | |
| 2.2.4 | Is PII/sensitive data filtered or masked? | ☐ | ☐ | ☐ | |
| 2.2.5 | Is there a data processing agreement (DPA)? | ☐ | ☐ | ☐ | |
| 2.2.6 | Does the vendor log access to customer data? | ☐ | ☐ | ☐ | |
| 2.2.7 | Can customer access logs be provided? | ☐ | ☐ | ☐ | |
| 2.2.8 | Is cross-border data transfer compliant? | ☐ | ☐ | ☐ | |

**Section 2 Score:** ___/16

---

## Section 3: Model Security

### 3.1 Model Provenance

| # | Question | Response | Notes |
|---|----------|----------|-------|
| 3.1.1 | What models power the service (e.g., GPT-4, Claude)? | | |
| 3.1.2 | Are models fine-tuned on specific data? | | |
| 3.1.3 | What is the source of training data? | | |
| 3.1.4 | Has training data been audited for bias/toxicity? | | |
| 3.1.5 | Is model versioning documented and communicated? | | |

### 3.2 Model Security Controls

| # | Question | Yes | No | N/A | Evidence |
|---|----------|-----|-----|-----|----------|
| 3.2.1 | Are there guardrails against harmful outputs? | ☐ | ☐ | ☐ | |
| 3.2.2 | Is prompt injection protection implemented? | ☐ | ☐ | ☐ | |
| 3.2.3 | Is jailbreak prevention in place? | ☐ | ☐ | ☐ | |
| 3.2.4 | Can content filtering be configured? | ☐ | ☐ | ☐ | |
| 3.2.5 | Is there protection against model extraction? | ☐ | ☐ | ☐ | |
| 3.2.6 | Are model outputs validated for safety? | ☐ | ☐ | ☐ | |
| 3.2.7 | Does the vendor conduct red team testing? | ☐ | ☐ | ☐ | |
| 3.2.8 | Is there a model card or documentation available? | ☐ | ☐ | ☐ | |

**Section 3 Score:** ___/16

---

## Section 4: API & Integration Security

### 4.1 Authentication & Access

| # | Question | Yes | No | N/A | Evidence |
|---|----------|-----|-----|-----|----------|
| 4.1.1 | Is API authentication required (API keys, OAuth)? | ☐ | ☐ | ☐ | |
| 4.1.2 | Can API keys be rotated? | ☐ | ☐ | ☐ | |
| 4.1.3 | Is MFA available for account access? | ☐ | ☐ | ☐ | |
| 4.1.4 | Are role-based access controls available? | ☐ | ☐ | ☐ | |
| 4.1.5 | Can IP allowlisting be configured? | ☐ | ☐ | ☐ | |
| 4.1.6 | Are API keys scoped (limited permissions)? | ☐ | ☐ | ☐ | |

### 4.2 Rate Limiting & Abuse Prevention

| # | Question | Yes | No | N/A | Evidence |
|---|----------|-----|-----|-----|----------|
| 4.2.1 | Is rate limiting enforced? | ☐ | ☐ | ☐ | |
| 4.2.2 | Are rate limits configurable? | ☐ | ☐ | ☐ | |
| 4.2.3 | Is abuse detection in place? | ☐ | ☐ | ☐ | |
| 4.2.4 | Are usage limits enforceable (cost controls)? | ☐ | ☐ | ☐ | |
| 4.2.5 | Is there protection against token/resource exhaustion? | ☐ | ☐ | ☐ | |

**Section 4 Score:** ___/22

---

## Section 5: Operational Security

### 5.1 Availability & Reliability

| # | Question | Response | Notes |
|---|----------|----------|-------|
| 5.1.1 | What is the SLA for uptime? | | |
| 5.1.2 | What is the average latency? | | |
| 5.1.3 | Is there a status page available? | | |
| 5.1.4 | What disaster recovery capabilities exist? | | |
| 5.1.5 | What is the RTO/RPO? | | |

### 5.2 Incident Response

| # | Question | Yes | No | N/A | Evidence |
|---|----------|-----|-----|-----|----------|
| 5.2.1 | Does the vendor have an incident response plan? | ☐ | ☐ | ☐ | |
| 5.2.2 | Will customers be notified of security incidents? | ☐ | ☐ | ☐ | |
| 5.2.3 | What is the notification timeline for incidents? | Response: | | |
| 5.2.4 | Is there a security contact or bug bounty program? | ☐ | ☐ | ☐ | |
| 5.2.5 | Can incident logs be provided to customers? | ☐ | ☐ | ☐ | |

### 5.3 Change Management

| # | Question | Yes | No | N/A | Evidence |
|---|----------|-----|-----|-----|----------|
| 5.3.1 | Are API changes communicated in advance? | ☐ | ☐ | ☐ | |
| 5.3.2 | Is there API versioning? | ☐ | ☐ | ☐ | |
| 5.3.3 | Are breaking changes announced with lead time? | ☐ | ☐ | ☐ | |
| 5.3.4 | Is there a deprecation policy? | ☐ | ☐ | ☐ | |

**Section 5 Score:** ___/18

---

## Section 6: Agent & Tool Security (If Applicable)

*Complete this section if the vendor provides AI agent capabilities or tool use.*

### 6.1 Agent Capabilities

| # | Question | Yes | No | N/A | Evidence |
|---|----------|-----|-----|-----|----------|
| 6.1.1 | Does the service support autonomous agent actions? | ☐ | ☐ | ☐ | |
| 6.1.2 | Can tool/function permissions be restricted? | ☐ | ☐ | ☐ | |
| 6.1.3 | Is there human-in-the-loop capability? | ☐ | ☐ | ☐ | |
| 6.1.4 | Are agent actions logged and auditable? | ☐ | ☐ | ☐ | |
| 6.1.5 | Can agent scope be limited (sandboxed)? | ☐ | ☐ | ☐ | |
| 6.1.6 | Is there a kill switch for agent actions? | ☐ | ☐ | ☐ | |
| 6.1.7 | Are inter-agent communications secured? | ☐ | ☐ | ☐ | |
| 6.1.8 | Is there protection against goal hijacking? | ☐ | ☐ | ☐ | |

**Section 6 Score:** ___/16 (or N/A)

---

## Section 7: Contractual & Legal

### 7.1 Terms & Agreements

| # | Question | Yes | No | N/A | Evidence |
|---|----------|-----|-----|-----|----------|
| 7.1.1 | Are acceptable use terms clear? | ☐ | ☐ | ☐ | |
| 7.1.2 | Is there liability for AI-generated content? | ☐ | ☐ | ☐ | |
| 7.1.3 | Are IP rights for outputs clearly defined? | ☐ | ☐ | ☐ | |
| 7.1.4 | Is there indemnification for security breaches? | ☐ | ☐ | ☐ | |
| 7.1.5 | Can the contract be terminated with data deletion? | ☐ | ☐ | ☐ | |
| 7.1.6 | Is there audit rights clause? | ☐ | ☐ | ☐ | |
| 7.1.7 | Are security requirements in the contract? | ☐ | ☐ | ☐ | |
| 7.1.8 | Is there a right to security assessment? | ☐ | ☐ | ☐ | |

**Section 7 Score:** ___/16

---

## Assessment Summary

### Scores by Section

| Section | Score | Max | Percentage | Risk |
|---------|-------|-----|------------|------|
| 1. Company & Compliance | | 16 | % | ☐H ☐M ☐L |
| 2. Data Handling | | 16 | % | ☐H ☐M ☐L |
| 3. Model Security | | 16 | % | ☐H ☐M ☐L |
| 4. API & Integration | | 22 | % | ☐H ☐M ☐L |
| 5. Operational Security | | 18 | % | ☐H ☐M ☐L |
| 6. Agent Security | | 16 | % | ☐H ☐M ☐L ☐N/A |
| 7. Contractual & Legal | | 16 | % | ☐H ☐M ☐L |
| **TOTAL** | | 120 | % | |

### Risk Rating

| Score Range | Risk Level | Recommendation |
|-------------|------------|----------------|
| 90-100% | Low | Approve with standard monitoring |
| 70-89% | Medium | Approve with additional controls |
| 50-69% | High | Approve with risk acceptance |
| <50% | Critical | Do not approve without remediation |

### Overall Vendor Risk: ☐ Low ☐ Medium ☐ High ☐ Critical

---

## Key Findings

### Critical Issues (Must Address)

1.
2.
3.

### High Risk Items

1.
2.
3.

### Recommendations

1.
2.
3.

---

## OWASP Risks Evaluated

| Risk | Covered | Notes |
|------|---------|-------|
| LLM01 - Prompt Injection | ☐ | Section 3.2 |
| LLM02 - Sensitive Info Disclosure | ☐ | Section 2 |
| LLM03 - Supply Chain | ☐ | Section 3.1 |
| LLM04 - Data Poisoning | ☐ | Section 3.1 |
| LLM06 - Excessive Agency | ☐ | Section 6 |
| ASI02 - Tool Misuse | ☐ | Section 6 |
| ASI04 - Agentic Supply Chain | ☐ | Section 3, 6 |

---

## Decision

### Recommendation

- [ ] **Approve** - Vendor meets security requirements
- [ ] **Approve with Conditions** - Requires specific controls/mitigations
- [ ] **Defer** - Requires additional information
- [ ] **Reject** - Does not meet security requirements

### Conditions (if applicable)

1.
2.
3.

### Required Mitigations

1.
2.
3.

---

## Sign-Off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Security Assessor | | | |
| Business Owner | | | |
| Security Lead | | | |
| Procurement (if applicable) | | | |

---

## Reassessment Schedule

| Event | Timeline |
|-------|----------|
| Next scheduled assessment | |
| Trigger for reassessment | Contract renewal, major version change, incident |
| Assessment owner | |

---

## Document Information

| Field | Value |
|-------|-------|
| HAIAMM Version | 2.2 |
| Questionnaire Version | 1.0 |
| Last Updated | January 2026 |
