# AI System Deployment Readiness Checklist

**Purpose:** Verify an AI system is ready for production deployment from a security perspective.

**When to Use:** Before deploying any AI system (LLM application, AI agent, ML model) to production.

**Completion Requirement:** All MUST items checked; SHOULD items assessed with documented exceptions.

---

## System Information

| Field | Value |
|-------|-------|
| System Name | |
| System Type | ☐ LLM App ☐ AI Agent ☐ ML Model ☐ RAG System ☐ Other |
| Deployment Date | |
| Environment | ☐ Production ☐ Staging ☐ Other: _______ |
| Risk Level | ☐ High ☐ Medium ☐ Low |
| Owner | |
| Reviewer | |

---

## 1. Documentation Requirements

### MUST Have

- [ ] **System architecture documented**
  - Components and interactions
  - Data flows
  - External dependencies

- [ ] **Security requirements documented**
  - Input/output requirements
  - Access control requirements
  - Data handling requirements

- [ ] **Threat model completed**
  - AI-specific threats identified
  - Mitigations documented
  - Residual risks accepted

- [ ] **Runbook/playbook available**
  - Operational procedures
  - Troubleshooting guides
  - Escalation paths

### SHOULD Have

- [ ] **Design review completed and signed off**
- [ ] **Implementation review completed**
- [ ] **Security testing report available**

---

## 2. Input Security

### MUST Have

- [ ] **Input validation implemented**
  - Maximum length limits enforced
  - Character/encoding validation
  - Format validation

- [ ] **Rate limiting configured**
  - Per-user limits defined
  - Per-API limits defined
  - Limits tested under load

- [ ] **Prompt injection mitigations**
  - System prompt protection
  - Input sanitization
  - Known pattern blocking

### SHOULD Have

- [ ] **Content filtering for harmful inputs**
- [ ] **Input logging enabled (with PII handling)**
- [ ] **Abuse detection capabilities**

### Verification

```
Test: Send oversized input (>limit)
Expected: Rejected with appropriate error
Result: ☐ Pass ☐ Fail

Test: Send known injection pattern
Expected: Blocked or sanitized
Result: ☐ Pass ☐ Fail

Test: Exceed rate limit
Expected: Requests throttled
Result: ☐ Pass ☐ Fail
```

---

## 3. Output Security

### MUST Have

- [ ] **Output validation implemented**
  - Response format validation
  - Length limits enforced
  - Sensitive data filtering

- [ ] **PII/sensitive data filtering**
  - Patterns defined
  - Filtering tested
  - False positive rate acceptable

- [ ] **Error handling sanitized**
  - No stack traces exposed
  - No internal details leaked
  - User-friendly messages

### SHOULD Have

- [ ] **Output logging enabled**
- [ ] **Content safety filtering**
- [ ] **Citation/attribution where applicable**

### Verification

```
Test: Attempt to extract system prompt
Expected: Request blocked or prompt not revealed
Result: ☐ Pass ☐ Fail

Test: Trigger error condition
Expected: Generic error, no internals exposed
Result: ☐ Pass ☐ Fail

Test: Request PII in output
Expected: PII filtered or refused
Result: ☐ Pass ☐ Fail
```

---

## 4. Authentication & Authorization

### MUST Have

- [ ] **Authentication required**
  - Auth mechanism: _____________
  - Token/session management
  - Secure credential handling

- [ ] **Authorization enforced**
  - Access controls defined
  - Role-based access implemented
  - Least privilege applied

- [ ] **API key/secret management**
  - No hardcoded secrets
  - Secrets in secure storage
  - Rotation capability

### SHOULD Have

- [ ] **Multi-factor authentication (for sensitive operations)**
- [ ] **Session timeout configured**
- [ ] **Audit trail for access**

### Verification

```
Test: Access without authentication
Expected: 401 Unauthorized
Result: ☐ Pass ☐ Fail

Test: Access with insufficient permissions
Expected: 403 Forbidden
Result: ☐ Pass ☐ Fail

Test: Check for hardcoded secrets
Expected: None found
Result: ☐ Pass ☐ Fail
```

---

## 5. Agent-Specific Controls (If Applicable)

*Skip this section if not deploying an AI agent with tool access.*

### MUST Have

- [ ] **Tool permissions defined**
  - Allowed tools listed
  - Denied tools listed
  - Permission boundaries documented

- [ ] **Tool execution sandboxed**
  - Isolation mechanism: _____________
  - Resource limits set
  - Network restrictions applied

- [ ] **Human-in-the-loop for sensitive actions**
  - Sensitive actions defined
  - Approval workflow implemented
  - Override capability available

- [ ] **Kill switch available**
  - Shutdown mechanism documented
  - Tested and verified working
  - Multiple personnel can activate

### SHOULD Have

- [ ] **Action logging and replay capability**
- [ ] **Rollback mechanism for tool actions**
- [ ] **Anomaly detection for agent behavior**

### Verification

```
Test: Agent attempts unauthorized tool
Expected: Action blocked
Result: ☐ Pass ☐ Fail

Test: Activate kill switch
Expected: Agent stops immediately
Result: ☐ Pass ☐ Fail

Test: Sensitive action without approval
Expected: Action queued for approval
Result: ☐ Pass ☐ Fail
```

---

## 6. Data Security

### MUST Have

- [ ] **Data classification applied**
  - Data types identified
  - Sensitivity levels assigned
  - Handling requirements defined

- [ ] **Encryption in transit**
  - TLS 1.2+ required
  - Certificate valid
  - No mixed content

- [ ] **Encryption at rest**
  - Storage encrypted
  - Key management defined
  - Backup encryption verified

- [ ] **Data retention defined**
  - Retention periods documented
  - Deletion procedures
  - Compliance requirements met

### SHOULD Have

- [ ] **Data lineage tracked**
- [ ] **PII minimization implemented**
- [ ] **Data access logging**

### Verification

```
Test: Check TLS configuration
Expected: TLS 1.2+, valid cert
Result: ☐ Pass ☐ Fail

Test: Verify storage encryption
Expected: Data encrypted at rest
Result: ☐ Pass ☐ Fail

Test: Check for PII in logs
Expected: PII masked or absent
Result: ☐ Pass ☐ Fail
```

---

## 7. Monitoring & Logging

### MUST Have

- [ ] **Interaction logging enabled**
  - Inputs logged (or hashed reference)
  - Outputs logged (or hashed reference)
  - Timestamps and user context

- [ ] **Security event logging**
  - Auth failures logged
  - Rate limit hits logged
  - Blocked requests logged

- [ ] **Log storage secured**
  - Access controlled
  - Retention configured
  - Tamper protection

- [ ] **Basic alerting configured**
  - Error rate alerts
  - Availability alerts
  - Security event alerts

### SHOULD Have

- [ ] **Anomaly detection enabled**
- [ ] **Dashboard available**
- [ ] **Log correlation with SIEM**

### Verification

```
Test: Generate security event
Expected: Event logged and visible
Result: ☐ Pass ☐ Fail

Test: Verify log retention
Expected: Meets retention requirement
Result: ☐ Pass ☐ Fail

Test: Trigger alert condition
Expected: Alert generated
Result: ☐ Pass ☐ Fail
```

---

## 8. Operational Readiness

### MUST Have

- [ ] **Incident response plan**
  - AI-specific procedures
  - Escalation contacts
  - Communication templates

- [ ] **Rollback capability**
  - Previous version available
  - Rollback procedure tested
  - Rollback time acceptable

- [ ] **On-call coverage**
  - On-call rotation defined
  - Contact information current
  - Escalation path documented

- [ ] **Emergency shutdown procedure**
  - Documented and accessible
  - Multiple people authorized
  - Tested within last 90 days

### SHOULD Have

- [ ] **Capacity planning completed**
- [ ] **Disaster recovery plan**
- [ ] **Business continuity plan**

---

## 9. Compliance & Governance

### MUST Have

- [ ] **Regulatory requirements identified**
  - Applicable regulations listed
  - Compliance verified
  - Gaps documented

- [ ] **Policy compliance verified**
  - AI acceptable use policy
  - Data handling policy
  - Security policy

- [ ] **Approval obtained**
  - Security sign-off
  - Business owner approval
  - Compliance approval (if required)

### SHOULD Have

- [ ] **Privacy impact assessment completed**
- [ ] **Ethical review completed (for high-risk AI)**
- [ ] **Third-party audit (for critical systems)**

---

## 10. Security Testing Results

### MUST Have

- [ ] **Prompt injection testing completed**
  - Test cases: _____ / _____ passed
  - Critical findings: _____ (must be 0)
  - High findings: _____ (must be 0 or accepted)

- [ ] **Authentication/authorization testing completed**
  - Test cases: _____ / _____ passed
  - Bypass attempts blocked

- [ ] **Input validation testing completed**
  - Boundary testing done
  - Malformed input handled

### SHOULD Have

- [ ] **Penetration testing completed**
- [ ] **Red team exercise (for high-risk systems)**
- [ ] **Third-party security assessment**

---

## Deployment Decision

### Summary

| Category | MUST Items | Completed | SHOULD Items | Completed |
|----------|------------|-----------|--------------|-----------|
| Documentation | 4 | /4 | 3 | /3 |
| Input Security | 3 | /3 | 3 | /3 |
| Output Security | 3 | /3 | 3 | /3 |
| Auth & Authz | 3 | /3 | 3 | /3 |
| Agent Controls* | 4 | /4 | 3 | /3 |
| Data Security | 4 | /4 | 3 | /3 |
| Monitoring | 4 | /4 | 3 | /3 |
| Operations | 4 | /4 | 3 | /3 |
| Compliance | 3 | /3 | 3 | /3 |
| Security Testing | 3 | /3 | 3 | /3 |

*If applicable

### Exceptions

Document any SHOULD items not completed with justification:

| Item | Justification | Accepted By | Date |
|------|---------------|-------------|------|
| | | | |
| | | | |

### Sign-Off

**Security Review:**
- [ ] All MUST items completed
- [ ] All exceptions documented and accepted
- [ ] Residual risks acceptable

**Approved for Deployment:** ☐ Yes ☐ No ☐ Conditional

**Conditions (if applicable):**


**Signatures:**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Security Reviewer | | | |
| System Owner | | | |
| Compliance (if required) | | | |

---

## Post-Deployment

- [ ] Monitoring verified working in production
- [ ] Alerts verified working
- [ ] First 24-hour review scheduled
- [ ] 30-day review scheduled

---

## Document Information

| Field | Value |
|-------|-------|
| HAIAMM Version | 2.0 |
| Checklist Version | 1.0 |
| Last Updated | January 2026 |

---

*Use `/verifhai-review` for AI-assisted deployment readiness assessment.*
