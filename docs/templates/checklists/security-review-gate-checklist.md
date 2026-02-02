# AI Security Review Gate Checklist

**Purpose:** Quick security review checklist for AI system changes during development.

**When to Use:**
- Pull requests with AI/LLM components
- New AI feature development
- Changes to AI system security controls
- Pre-merge security gates

**Time to Complete:** 15-30 minutes

---

## Review Information

| Field | Value |
|-------|-------|
| PR/Change ID | |
| System | |
| Reviewer | |
| Date | |
| Change Type | ☐ New Feature ☐ Bug Fix ☐ Security Fix ☐ Refactor ☐ Config |

---

## Quick Risk Assessment

**Does this change involve:**

- [ ] New LLM/AI model integration → High scrutiny
- [ ] New tool/API access for agents → High scrutiny
- [ ] Changes to input validation → High scrutiny
- [ ] Changes to output handling → High scrutiny
- [ ] Changes to authentication/authorization → High scrutiny
- [ ] Changes to data handling → Medium scrutiny
- [ ] Changes to logging/monitoring → Medium scrutiny
- [ ] UI/UX changes only → Standard review
- [ ] Documentation only → Minimal review

**Risk Level:** ☐ High ☐ Medium ☐ Low

---

## 1. Secrets & Credentials

- [ ] **No hardcoded secrets**
  - No API keys in code
  - No passwords in code
  - No tokens in code

- [ ] **Secrets properly managed**
  - Environment variables used
  - Secret manager integration
  - No secrets in logs

- [ ] **No secrets in version control**
  - .gitignore configured
  - No secrets in commit history

**Quick Check:**
```bash
# Search for potential secrets
grep -r "api_key\|password\|secret\|token" --include="*.py" --include="*.js" --include="*.ts"
```

☐ Pass ☐ Fail ☐ N/A

---

## 2. Input Handling

- [ ] **User input validated**
  - Length limits enforced
  - Type validation present
  - Encoding handled

- [ ] **Injection prevention**
  - No direct string concatenation to prompts
  - Input sanitization applied
  - Parameterized where possible

- [ ] **Rate limiting considered**
  - Limits defined for new endpoints
  - Existing limits not bypassed

**Red Flags:**
```python
# BAD: Direct concatenation
prompt = f"User asked: {user_input}"

# GOOD: Structured input
messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": sanitize(user_input)}
]
```

☐ Pass ☐ Fail ☐ N/A

---

## 3. Output Handling

- [ ] **Output validated before use**
  - Format validated
  - Length checked
  - Content sanitized

- [ ] **Sensitive data filtered**
  - PII patterns checked
  - Internal data not exposed
  - System prompts protected

- [ ] **Error handling secure**
  - No stack traces to users
  - No internal details leaked
  - Generic error messages

**Red Flags:**
```python
# BAD: Raw output to user
return llm_response.content

# GOOD: Validated output
validated = validate_output(llm_response.content)
return sanitize_pii(validated)
```

☐ Pass ☐ Fail ☐ N/A

---

## 4. Authentication & Authorization

- [ ] **Auth required for new endpoints**
  - Authentication enforced
  - Authorization checked
  - Appropriate access level

- [ ] **No auth bypass**
  - Existing auth not weakened
  - No new unauthenticated paths
  - Token handling secure

- [ ] **Least privilege applied**
  - Minimal permissions requested
  - No privilege escalation
  - Scope appropriately limited

☐ Pass ☐ Fail ☐ N/A

---

## 5. Agent/Tool Security (If Applicable)

*Skip if change doesn't involve AI agents or tool use.*

- [ ] **Tool permissions appropriate**
  - Only necessary tools enabled
  - Dangerous tools restricted
  - Permission boundaries clear

- [ ] **Actions bounded**
  - Resource limits defined
  - Execution sandboxed
  - Network access restricted

- [ ] **Human oversight maintained**
  - Sensitive actions require approval
  - Audit trail preserved
  - Override capability exists

☐ Pass ☐ Fail ☐ N/A

---

## 6. Data Handling

- [ ] **Data classification respected**
  - Sensitive data identified
  - Handling appropriate to classification
  - No data exposure

- [ ] **Privacy maintained**
  - PII minimized
  - Consent respected
  - Retention limits honored

- [ ] **No training data leakage**
  - Test data not in production
  - Training data properly isolated
  - No cross-contamination

☐ Pass ☐ Fail ☐ N/A

---

## 7. Logging & Monitoring

- [ ] **Appropriate logging added**
  - Security-relevant events logged
  - No sensitive data in logs
  - Log level appropriate

- [ ] **Existing logging not broken**
  - Log formats maintained
  - Log destinations unchanged
  - Correlation IDs preserved

- [ ] **Alerting considered**
  - New failure modes covered
  - Thresholds appropriate
  - Alert fatigue avoided

☐ Pass ☐ Fail ☐ N/A

---

## 8. Dependencies & Supply Chain

- [ ] **New dependencies reviewed**
  - Source verified
  - License compatible
  - Security advisories checked

- [ ] **Versions pinned appropriately**
  - No floating versions for security-critical packages
  - Lock files updated
  - Reproducible builds

- [ ] **No known vulnerabilities**
  - Dependency scan run
  - Critical/high vulns addressed
  - Risk accepted for others

**Quick Check:**
```bash
# For Python
pip-audit

# For Node.js
npm audit

# For general
snyk test
```

☐ Pass ☐ Fail ☐ N/A

---

## 9. AI-Specific Checks

- [ ] **Prompt injection mitigated**
  - System prompts protected
  - User/system separation clear
  - Injection patterns considered

- [ ] **Model behavior bounded**
  - Guardrails in place
  - Unexpected behavior handled
  - Fallback behavior defined

- [ ] **Context window managed**
  - Token limits respected
  - Truncation handled securely
  - No context leakage

**OWASP Risks Considered:**

| Risk | Relevant | Mitigated |
|------|----------|-----------|
| LLM01 - Prompt Injection | ☐ | ☐ |
| LLM02 - Sensitive Info Disclosure | ☐ | ☐ |
| LLM05 - Improper Output Handling | ☐ | ☐ |
| LLM06 - Excessive Agency | ☐ | ☐ |
| LLM07 - System Prompt Leakage | ☐ | ☐ |
| ASI01 - Agent Goal Hijack | ☐ | ☐ |
| ASI02 - Tool Misuse | ☐ | ☐ |
| ASI03 - Privilege Abuse | ☐ | ☐ |

☐ Pass ☐ Fail ☐ N/A

---

## 10. Testing

- [ ] **Security tests added/updated**
  - New security test cases
  - Existing tests pass
  - Edge cases covered

- [ ] **Manual testing performed**
  - Happy path tested
  - Error paths tested
  - Abuse scenarios considered

- [ ] **No test credentials in code**
  - Test secrets separate
  - Mock data used
  - No production data in tests

☐ Pass ☐ Fail ☐ N/A

---

## Review Summary

### Results

| Section | Result |
|---------|--------|
| 1. Secrets & Credentials | ☐ Pass ☐ Fail ☐ N/A |
| 2. Input Handling | ☐ Pass ☐ Fail ☐ N/A |
| 3. Output Handling | ☐ Pass ☐ Fail ☐ N/A |
| 4. Auth & Authz | ☐ Pass ☐ Fail ☐ N/A |
| 5. Agent/Tool Security | ☐ Pass ☐ Fail ☐ N/A |
| 6. Data Handling | ☐ Pass ☐ Fail ☐ N/A |
| 7. Logging & Monitoring | ☐ Pass ☐ Fail ☐ N/A |
| 8. Dependencies | ☐ Pass ☐ Fail ☐ N/A |
| 9. AI-Specific Checks | ☐ Pass ☐ Fail ☐ N/A |
| 10. Testing | ☐ Pass ☐ Fail ☐ N/A |

### Findings

| Finding | Severity | Status |
|---------|----------|--------|
| | ☐ Critical ☐ High ☐ Medium ☐ Low | ☐ Fix Required ☐ Accepted |
| | ☐ Critical ☐ High ☐ Medium ☐ Low | ☐ Fix Required ☐ Accepted |
| | ☐ Critical ☐ High ☐ Medium ☐ Low | ☐ Fix Required ☐ Accepted |

### Decision

- [ ] **Approved** - No security concerns
- [ ] **Approved with conditions** - Minor fixes required before merge
- [ ] **Blocked** - Security issues must be resolved

**Conditions/Required Changes:**


### Sign-Off

**Reviewer:** _________________ **Date:** _____________

**Developer Acknowledgment:** _________________ **Date:** _____________

---

## Quick Reference: Common Issues

### Top 5 AI Security Code Smells

1. **Direct prompt concatenation**
   ```python
   # BAD
   prompt = "Analyze: " + user_input
   ```

2. **Unvalidated LLM output**
   ```python
   # BAD
   exec(llm_response.content)
   ```

3. **Hardcoded API keys**
   ```python
   # BAD
   client = OpenAI(api_key="sk-...")
   ```

4. **Missing rate limits**
   ```python
   # BAD - unlimited calls
   @app.route("/chat")
   def chat(): ...
   ```

5. **Excessive tool permissions**
   ```python
   # BAD
   tools = ["*"]  # All tools enabled
   ```

---

## Document Information

| Field | Value |
|-------|-------|
| HAIAMM Version | 2.0 |
| Checklist Version | 1.0 |
| Last Updated | January 2026 |

---

*Use `/verifhai-review` for AI-assisted code review.*
