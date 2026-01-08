# AI Security Incident Post-Mortem Questionnaire

**Purpose:** Structured analysis of AI/ML security incidents to identify root causes, improve defenses, and prevent recurrence.

**When to Use:**
- After any AI security incident is resolved
- Security near-misses with potential impact
- Discovered vulnerabilities (even if not exploited)
- Failed attacks that revealed weaknesses

**Time to Complete:** 1-2 hours

**Related:** [Incident Response Checklist](../checklists/incident-response-checklist.md)

---

## Incident Identification

| Field | Value |
|-------|-------|
| Incident ID | |
| Incident Title | |
| Date Detected | |
| Date Resolved | |
| Time to Detect (TTD) | |
| Time to Respond (TTR) | |
| Time to Remediate (TTM) | |
| Severity | ☐ Critical ☐ High ☐ Medium ☐ Low |
| Status | ☐ Resolved ☐ Mitigated ☐ Ongoing |
| Post-Mortem Lead | |
| Post-Mortem Date | |

---

## Section 1: Incident Summary

### 1.1 Executive Summary

| # | Question | Response |
|---|----------|----------|
| 1.1.1 | What happened in one paragraph? | |
| 1.1.2 | What was the business impact? | |
| 1.1.3 | How many users/systems affected? | |
| 1.1.4 | Was data compromised? If so, what type? | |
| 1.1.5 | Were there regulatory implications? | |

### 1.2 Incident Classification

| # | Question | Response |
|---|----------|----------|
| 1.2.1 | Incident Type | ☐ Prompt Injection ☐ Data Leak ☐ Model Manipulation ☐ Agent Hijack ☐ Denial of Service ☐ Supply Chain ☐ Other: |
| 1.2.2 | Attack Vector | ☐ Direct Input ☐ Indirect (Data) ☐ API Abuse ☐ Social Engineering ☐ Insider ☐ Other: |
| 1.2.3 | Affected AI System(s) | |
| 1.2.4 | OWASP Risk Category | ☐ LLM01-10: ___ ☐ ASI01-10: ___ |
| 1.2.5 | Was this a known risk? | ☐ Yes - documented ☐ Yes - not documented ☐ No |

---

## Section 2: Timeline & Detection

### 2.1 Timeline Reconstruction

| Phase | Date/Time | Duration | Description |
|-------|-----------|----------|-------------|
| Initial Compromise | | | |
| Attacker Activity | | | |
| First Indicator | | | |
| Detection | | | |
| Investigation Start | | | |
| Containment | | | |
| Eradication | | | |
| Recovery | | | |
| Incident Closed | | | |

### 2.2 Detection Analysis

| # | Question | Response | Gap Identified |
|---|----------|----------|----------------|
| 2.2.1 | How was the incident detected? | ☐ Automated alert ☐ User report ☐ Security team ☐ Third party ☐ Attacker disclosure | |
| 2.2.2 | Which monitoring system detected it? | | |
| 2.2.3 | Was there a detection delay? If so, why? | | |
| 2.2.4 | Were there earlier indicators we missed? | | |
| 2.2.5 | Did existing alerts fire correctly? | ☐ Yes ☐ No ☐ Partial | |
| 2.2.6 | Were logs sufficient for investigation? | ☐ Yes ☐ No ☐ Partial | |
| 2.2.7 | Was anomaly detection effective? | ☐ Yes ☐ No ☐ N/A | |

---

## Section 3: AI-Specific Analysis

### 3.1 Prompt Injection (If Applicable)

| # | Question | Yes | No | N/A | Details |
|---|----------|-----|-----|-----|---------|
| 3.1.1 | Was the attack via direct prompt injection? | ☐ | ☐ | ☐ | |
| 3.1.2 | Was the attack via indirect injection (data)? | ☐ | ☐ | ☐ | |
| 3.1.3 | Did the attack bypass input validation? | ☐ | ☐ | ☐ | |
| 3.1.4 | Was the system prompt extracted? | ☐ | ☐ | ☐ | |
| 3.1.5 | Did the attack use encoding/obfuscation? | ☐ | ☐ | ☐ | |
| 3.1.6 | Was the attack multi-turn/context-building? | ☐ | ☐ | ☐ | |

**Attack Pattern (if known):**
```
[Paste sanitized attack payload here]
```

### 3.2 Data Security (If Applicable)

| # | Question | Yes | No | N/A | Details |
|---|----------|-----|-----|-----|---------|
| 3.2.1 | Was training data accessed/extracted? | ☐ | ☐ | ☐ | |
| 3.2.2 | Was PII exposed in outputs? | ☐ | ☐ | ☐ | |
| 3.2.3 | Were RAG documents compromised? | ☐ | ☐ | ☐ | |
| 3.2.4 | Was conversation history leaked? | ☐ | ☐ | ☐ | |
| 3.2.5 | Did the model memorize sensitive data? | ☐ | ☐ | ☐ | |
| 3.2.6 | Were data isolation controls bypassed? | ☐ | ☐ | ☐ | |

### 3.3 Agent/Tool Security (If Applicable)

| # | Question | Yes | No | N/A | Details |
|---|----------|-----|-----|-----|---------|
| 3.3.1 | Was an agent's goal/behavior hijacked? | ☐ | ☐ | ☐ | |
| 3.3.2 | Were unauthorized tools executed? | ☐ | ☐ | ☐ | |
| 3.3.3 | Did agents exceed permission boundaries? | ☐ | ☐ | ☐ | |
| 3.3.4 | Was there privilege escalation? | ☐ | ☐ | ☐ | |
| 3.3.5 | Were inter-agent communications compromised? | ☐ | ☐ | ☐ | |
| 3.3.6 | Was the kill switch/circuit breaker effective? | ☐ | ☐ | ☐ | |
| 3.3.7 | Did cascading failures occur? | ☐ | ☐ | ☐ | |

### 3.4 Model Integrity (If Applicable)

| # | Question | Yes | No | N/A | Details |
|---|----------|-----|-----|-----|---------|
| 3.4.1 | Was the model manipulated/poisoned? | ☐ | ☐ | ☐ | |
| 3.4.2 | Were model weights accessed? | ☐ | ☐ | ☐ | |
| 3.4.3 | Was there model extraction/theft? | ☐ | ☐ | ☐ | |
| 3.4.4 | Were adversarial inputs used? | ☐ | ☐ | ☐ | |
| 3.4.5 | Was there supply chain compromise? | ☐ | ☐ | ☐ | |

---

## Section 4: Root Cause Analysis

### 4.1 Five Whys

| Level | Question | Answer |
|-------|----------|--------|
| Why 1 | Why did the incident occur? | |
| Why 2 | Why was [answer 1] possible? | |
| Why 3 | Why was [answer 2] possible? | |
| Why 4 | Why was [answer 3] possible? | |
| Why 5 | Why was [answer 4] possible? | |
| **Root Cause** | | |

### 4.2 Contributing Factors

| # | Factor Category | Present? | Description |
|---|-----------------|----------|-------------|
| 4.2.1 | Design flaw | ☐ Yes ☐ No | |
| 4.2.2 | Implementation bug | ☐ Yes ☐ No | |
| 4.2.3 | Configuration error | ☐ Yes ☐ No | |
| 4.2.4 | Missing control | ☐ Yes ☐ No | |
| 4.2.5 | Control bypass | ☐ Yes ☐ No | |
| 4.2.6 | Process failure | ☐ Yes ☐ No | |
| 4.2.7 | Human error | ☐ Yes ☐ No | |
| 4.2.8 | Third-party/vendor issue | ☐ Yes ☐ No | |
| 4.2.9 | Resource constraint | ☐ Yes ☐ No | |
| 4.2.10 | Insufficient testing | ☐ Yes ☐ No | |

### 4.3 HAIAMM Practice Gaps

*Which HAIAMM practices failed or were insufficient?*

| Practice | Gap Identified? | Description |
|----------|-----------------|-------------|
| SM - Strategy & Metrics | ☐ Yes ☐ No | |
| PC - Policy & Compliance | ☐ Yes ☐ No | |
| EG - Education & Guidance | ☐ Yes ☐ No | |
| TA - Threat Assessment | ☐ Yes ☐ No | |
| SR - Security Requirements | ☐ Yes ☐ No | |
| SA - Secure Architecture | ☐ Yes ☐ No | |
| DR - Design Review | ☐ Yes ☐ No | |
| IR - Implementation Review | ☐ Yes ☐ No | |
| ST - Security Testing | ☐ Yes ☐ No | |
| IM - Issue Management | ☐ Yes ☐ No | |
| EH - Environment Hardening | ☐ Yes ☐ No | |
| ML - Monitoring & Logging | ☐ Yes ☐ No | |

---

## Section 5: Response Evaluation

### 5.1 Response Effectiveness

| # | Question | Rating | Notes |
|---|----------|--------|-------|
| 5.1.1 | How quickly was incident detected? | ☐ Excellent ☐ Good ☐ Needs Improvement ☐ Poor | |
| 5.1.2 | How effective was initial containment? | ☐ Excellent ☐ Good ☐ Needs Improvement ☐ Poor | |
| 5.1.3 | How well did team coordinate? | ☐ Excellent ☐ Good ☐ Needs Improvement ☐ Poor | |
| 5.1.4 | Was communication clear and timely? | ☐ Excellent ☐ Good ☐ Needs Improvement ☐ Poor | |
| 5.1.5 | Were runbooks/playbooks helpful? | ☐ Excellent ☐ Good ☐ Needs Improvement ☐ Poor ☐ N/A | |
| 5.1.6 | Was escalation handled correctly? | ☐ Excellent ☐ Good ☐ Needs Improvement ☐ Poor | |
| 5.1.7 | Was external communication appropriate? | ☐ Excellent ☐ Good ☐ Needs Improvement ☐ Poor ☐ N/A | |

### 5.2 Response Gaps

| # | Question | Response |
|---|----------|----------|
| 5.2.1 | What slowed down the response? | |
| 5.2.2 | What information was missing? | |
| 5.2.3 | What tools were lacking? | |
| 5.2.4 | Were any response steps skipped? Why? | |
| 5.2.5 | What went well in the response? | |

---

## Section 6: Impact Assessment

### 6.1 Business Impact

| # | Impact Area | Affected? | Quantification |
|---|-------------|-----------|----------------|
| 6.1.1 | Revenue loss | ☐ Yes ☐ No | $ |
| 6.1.2 | Customer impact | ☐ Yes ☐ No | # affected: |
| 6.1.3 | Data breach | ☐ Yes ☐ No | Records: |
| 6.1.4 | Reputation damage | ☐ Yes ☐ No | |
| 6.1.5 | Regulatory notification required | ☐ Yes ☐ No | |
| 6.1.6 | Legal exposure | ☐ Yes ☐ No | |
| 6.1.7 | Operational disruption | ☐ Yes ☐ No | Hours: |
| 6.1.8 | Recovery costs | ☐ Yes ☐ No | $ |

### 6.2 Technical Impact

| # | Impact Area | Affected? | Details |
|---|-------------|-----------|---------|
| 6.2.1 | System availability | ☐ Yes ☐ No | |
| 6.2.2 | Data integrity | ☐ Yes ☐ No | |
| 6.2.3 | Data confidentiality | ☐ Yes ☐ No | |
| 6.2.4 | Model integrity | ☐ Yes ☐ No | |
| 6.2.5 | Infrastructure compromise | ☐ Yes ☐ No | |
| 6.2.6 | Third-party systems | ☐ Yes ☐ No | |

---

## Section 7: Remediation Actions

### 7.1 Immediate Actions (Completed)

| # | Action | Status | Owner | Completion Date |
|---|--------|--------|-------|-----------------|
| 1 | | ☐ Done | | |
| 2 | | ☐ Done | | |
| 3 | | ☐ Done | | |
| 4 | | ☐ Done | | |
| 5 | | ☐ Done | | |

### 7.2 Short-Term Improvements (Next 30 Days)

| # | Action | Priority | Owner | Target Date | HAIAMM Practice |
|---|--------|----------|-------|-------------|-----------------|
| 1 | | ☐ H ☐ M ☐ L | | | |
| 2 | | ☐ H ☐ M ☐ L | | | |
| 3 | | ☐ H ☐ M ☐ L | | | |
| 4 | | ☐ H ☐ M ☐ L | | | |
| 5 | | ☐ H ☐ M ☐ L | | | |

### 7.3 Long-Term Improvements (Next Quarter)

| # | Action | Priority | Owner | Target Date | HAIAMM Practice |
|---|--------|----------|-------|-------------|-----------------|
| 1 | | ☐ H ☐ M ☐ L | | | |
| 2 | | ☐ H ☐ M ☐ L | | | |
| 3 | | ☐ H ☐ M ☐ L | | | |
| 4 | | ☐ H ☐ M ☐ L | | | |
| 5 | | ☐ H ☐ M ☐ L | | | |

---

## Section 8: Prevention Measures

### 8.1 Detection Improvements

| # | Improvement | Description | Target Implementation |
|---|-------------|-------------|----------------------|
| 8.1.1 | New alerts | | |
| 8.1.2 | Log enhancements | | |
| 8.1.3 | Monitoring rules | | |
| 8.1.4 | Anomaly detection | | |

### 8.2 Defense Improvements

| # | Improvement | Description | Target Implementation |
|---|-------------|-------------|----------------------|
| 8.2.1 | Input validation | | |
| 8.2.2 | Output filtering | | |
| 8.2.3 | Access controls | | |
| 8.2.4 | Architecture changes | | |

### 8.3 Process Improvements

| # | Improvement | Description | Target Implementation |
|---|-------------|-------------|----------------------|
| 8.3.1 | Runbook updates | | |
| 8.3.2 | Training needs | | |
| 8.3.3 | Review process | | |
| 8.3.4 | Testing additions | | |

---

## Section 9: Lessons Learned

### 9.1 What Worked Well

1.
2.
3.

### 9.2 What Needs Improvement

1.
2.
3.

### 9.3 Surprises/Unexpected Findings

1.
2.
3.

### 9.4 Key Takeaways

| # | Lesson | Action Required |
|---|--------|-----------------|
| 1 | | |
| 2 | | |
| 3 | | |

---

## Section 10: Follow-Up

### 10.1 Action Tracking

| # | Action Item | Owner | Due Date | Status | Jira/Issue # |
|---|-------------|-------|----------|--------|--------------|
| 1 | | | | ☐ Open | |
| 2 | | | | ☐ Open | |
| 3 | | | | ☐ Open | |
| 4 | | | | ☐ Open | |
| 5 | | | | ☐ Open | |

### 10.2 Review Schedule

| Review Type | Date | Attendees | Notes |
|-------------|------|-----------|-------|
| 30-day action review | | | |
| 60-day effectiveness check | | | |
| Quarterly retrospective | | | |

### 10.3 Documentation Updates Required

| Document | Update Needed | Owner | Status |
|----------|---------------|-------|--------|
| Threat model | | | ☐ |
| Runbooks | | | ☐ |
| Architecture docs | | | ☐ |
| Training materials | | | ☐ |
| HAIAMM assessment | | | ☐ |

---

## Sign-Off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Incident Commander | | | |
| Security Lead | | | |
| Engineering Lead | | | |
| System Owner | | | |
| Executive Sponsor | | | |

---

## Distribution

| Audience | Deliverable | Date Sent |
|----------|-------------|-----------|
| Executive summary | | |
| Full post-mortem | | |
| Technical details | | |
| Lessons learned | | |

---

## Appendices

### Appendix A: Attack Timeline Diagram

*[Insert timeline visualization here]*

### Appendix B: Sanitized Attack Payloads

*[Include sanitized examples for training/testing]*

### Appendix C: Log Excerpts

*[Relevant log entries with sensitive data redacted]*

### Appendix D: Related Incidents

| Incident ID | Title | Date | Similarity |
|-------------|-------|------|------------|
| | | | |

---

## Document Information

| Field | Value |
|-------|-------|
| HAIAMM Version | 2.2 |
| Questionnaire Version | 1.0 |
| Last Updated | January 2026 |
