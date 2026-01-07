# AI Security Incident Response Checklist

**Purpose:** Guide response to security incidents involving AI systems.

**When to Use:**
- AI system behaving unexpectedly
- Suspected prompt injection attack
- Data breach involving AI systems
- AI agent taking unauthorized actions
- Model theft or extraction attempt
- Any security incident involving AI/LLM/ML systems

**Severity Levels:**
- **SEV-1 (Critical):** Active exploitation, data breach, safety risk
- **SEV-2 (High):** Exploitable vulnerability, significant risk
- **SEV-3 (Medium):** Potential vulnerability, limited risk
- **SEV-4 (Low):** Minor issue, best practice gap

---

## Incident Information

| Field | Value |
|-------|-------|
| Incident ID | |
| Date/Time Detected | |
| Reported By | |
| Severity | ☐ SEV-1 ☐ SEV-2 ☐ SEV-3 ☐ SEV-4 |
| Status | ☐ Investigating ☐ Containing ☐ Eradicating ☐ Recovering ☐ Closed |
| Incident Commander | |
| Affected System(s) | |

---

## Phase 1: Detection & Triage (First 15 Minutes)

### Initial Assessment

- [ ] **Confirm the incident**
  - Verify this is a real security incident
  - Rule out false positives
  - Initial severity assessment

- [ ] **Identify affected systems**
  - Which AI systems are involved?
  - What data may be affected?
  - What tools/APIs may be compromised?

- [ ] **Assign severity level**
  - SEV-1: Immediate response, all hands
  - SEV-2: Urgent response within 1 hour
  - SEV-3: Response within 4 hours
  - SEV-4: Response within 24 hours

- [ ] **Notify appropriate personnel**
  - Incident Commander assigned
  - Security team notified
  - On-call engineer notified
  - Management notified (SEV-1/2)

### Initial Questions

| Question | Answer |
|----------|--------|
| What happened? | |
| When did it start? | |
| What AI systems are affected? | |
| Is the attack ongoing? | |
| What data may be exposed? | |
| What actions has the AI taken? | |

---

## Phase 2: Containment (First 1 Hour)

### Immediate Containment Actions

**For ALL AI Incidents:**

- [ ] **Preserve evidence**
  - Screenshot current state
  - Export relevant logs immediately
  - Document timeline of events
  - Preserve LLM interaction history

- [ ] **Assess containment options**
  - Can we isolate without full shutdown?
  - What's the business impact of containment?
  - Who needs to approve shutdown?

**For Prompt Injection / Jailbreak:**

- [ ] **Block attacking user/IP (if identified)**
- [ ] **Add malicious pattern to blocklist**
- [ ] **Review recent interactions for similar attacks**
- [ ] **Enable enhanced input logging**

**For Agent Misbehavior:**

- [ ] **Activate kill switch / disable agent**
- [ ] **Revoke agent's tool permissions**
- [ ] **Audit recent agent actions**
- [ ] **Identify and reverse unauthorized actions**

**For Data Breach / Exfiltration:**

- [ ] **Isolate affected data stores**
- [ ] **Revoke compromised credentials**
- [ ] **Enable enhanced access logging**
- [ ] **Assess what data was accessed**

**For Model Theft / Extraction:**

- [ ] **Rate limit or block API access**
- [ ] **Review unusual API usage patterns**
- [ ] **Assess intellectual property exposure**
- [ ] **Consider model watermarking verification**

### Kill Switch Procedures

**Emergency Shutdown Options:**

| Method | Command/Action | Impact |
|--------|----------------|--------|
| Feature Flag | Set `AI_ENABLED=false` | Disables all AI features |
| API Gateway | Block routes `/api/ai/*` | Stops external AI API access |
| Network | Block outbound to AI providers | Stops external AI calls |
| Instance | Stop AI service containers | Full AI service shutdown |

- [ ] **Kill switch activated (if needed)**
  - Method used: _____________
  - Time activated: _____________
  - Activated by: _____________

---

## Phase 3: Investigation (Hours 1-4)

### Evidence Collection

- [ ] **Collect logs**
  - AI interaction logs
  - Application logs
  - Infrastructure logs
  - Network logs
  - Access logs

- [ ] **Timeline reconstruction**
  - First malicious activity
  - Attack progression
  - Detection point
  - Response actions

- [ ] **Attack analysis**
  - Attack vector identified
  - Attacker techniques
  - Indicators of compromise (IOCs)
  - Full scope of impact

### AI-Specific Investigation

**For Prompt Injection:**
- [ ] What was the malicious prompt?
- [ ] How did it bypass controls?
- [ ] What actions did it cause?
- [ ] Are similar attacks present in logs?

**For Agent Misbehavior:**
- [ ] What triggered the misbehavior?
- [ ] What actions did the agent take?
- [ ] What data did it access?
- [ ] What tools did it misuse?

**For Data Exfiltration:**
- [ ] What data was exposed?
- [ ] How was it extracted?
- [ ] Who received the data?
- [ ] What's the sensitivity level?

### Root Cause Analysis

| Question | Finding |
|----------|---------|
| What vulnerability was exploited? | |
| Why did detection take this long? | |
| What controls failed? | |
| What controls worked? | |
| Was this preventable? | |

---

## Phase 4: Eradication (Hours 4-24)

### Remove Threat

- [ ] **Patch vulnerability**
  - Input validation strengthened
  - Output filtering enhanced
  - Permissions restricted
  - Other: _____________

- [ ] **Clean affected systems**
  - Malicious data removed
  - Compromised components replaced
  - Corrupted state reset
  - Cache cleared if needed

- [ ] **Update protections**
  - New detection rules added
  - Blocklists updated
  - Monitoring enhanced
  - Controls hardened

### Verification

- [ ] **Verify threat removed**
  - Vulnerability no longer exploitable
  - Malicious artifacts removed
  - No persistence mechanisms remain

- [ ] **Test fixes**
  - Patches tested in staging
  - No regressions introduced
  - Security tests pass

---

## Phase 5: Recovery (Hours 24-72)

### Restore Operations

- [ ] **Plan recovery sequence**
  - Order of system restoration
  - Validation checkpoints
  - Rollback triggers

- [ ] **Restore systems**
  - AI services restarted
  - Features re-enabled
  - Access restored
  - Monitoring confirmed working

- [ ] **Validate functionality**
  - Core features working
  - Security controls active
  - No residual issues

### Enhanced Monitoring

- [ ] **Implement enhanced monitoring**
  - Additional logging enabled
  - New alerts configured
  - Increased scrutiny period
  - Manual review schedule

---

## Phase 6: Post-Incident (Within 2 Weeks)

### Documentation

- [ ] **Complete incident report**
  - Executive summary
  - Timeline of events
  - Impact assessment
  - Root cause analysis
  - Actions taken
  - Lessons learned

- [ ] **Update documentation**
  - Runbooks updated
  - Incident response plan revised
  - Detection rules documented
  - Architecture diagrams updated

### Lessons Learned

- [ ] **Conduct post-mortem meeting**
  - All stakeholders included
  - Blameless discussion
  - Improvement actions identified
  - Owners assigned

- [ ] **Create improvement tickets**
  - Detection improvements
  - Prevention improvements
  - Response improvements
  - Training needs

### Communication

- [ ] **Internal communication complete**
  - Stakeholders briefed
  - Lessons shared
  - Training scheduled if needed

- [ ] **External communication (if required)**
  - Customer notification (if data breach)
  - Regulatory notification (if required)
  - Public disclosure (if appropriate)

---

## AI-Specific Post-Incident Actions

### Model & Training Data Review

- [ ] **Assess model integrity**
  - Was the model tampered with?
  - Is retraining needed?
  - Are weights compromised?

- [ ] **Review training data**
  - Was training data poisoned?
  - Is data cleanup needed?
  - Are data sources still trusted?

### Trust & Safety Review

- [ ] **Review guardrails**
  - Are current guardrails sufficient?
  - What new guardrails are needed?
  - How can bypasses be prevented?

- [ ] **Review permissions**
  - Are tool permissions appropriate?
  - Is least privilege enforced?
  - Are human checkpoints adequate?

---

## Contact List

| Role | Name | Contact | Backup |
|------|------|---------|--------|
| Incident Commander | | | |
| Security Lead | | | |
| AI/ML Lead | | | |
| Infrastructure Lead | | | |
| Legal/Compliance | | | |
| Communications | | | |
| Executive Sponsor | | | |

---

## Quick Reference: Common AI Incidents

### Prompt Injection Response

1. Block attacking user/IP
2. Add pattern to blocklist
3. Review similar interactions
4. Patch input validation
5. Enable enhanced monitoring

### Agent Misbehavior Response

1. Activate kill switch
2. Revoke tool permissions
3. Audit and reverse actions
4. Identify trigger
5. Strengthen guardrails

### Data Exfiltration Response

1. Isolate data sources
2. Revoke credentials
3. Assess data exposure
4. Notify affected parties
5. Strengthen output filtering

### Model Extraction Response

1. Rate limit API access
2. Review usage patterns
3. Assess IP exposure
4. Consider watermark verification
5. Enhance API protections

---

## Incident Severity Escalation Matrix

| Condition | Escalate To |
|-----------|-------------|
| Any data breach | Legal, Executive, Privacy Officer |
| Customer data exposed | Customer Success, Legal |
| PII exposed | Privacy Officer, Legal |
| Agent took harmful action | Executive, Safety Team |
| Regulatory implications | Compliance, Legal |
| Media attention likely | Communications, Executive |
| Active ongoing attack | Security Leadership, Executive |

---

## Document Information

| Field | Value |
|-------|-------|
| HAIAMM Version | 2.2 |
| Checklist Version | 1.0 |
| Last Updated | January 2026 |

---

*Report incidents immediately. When in doubt, escalate.*
