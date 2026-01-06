![HAIAMM Logo](../images/HAIAMM_logo.png)

# HAIAMM Quick Start Guide

**Get started securing your AI systems in 10 minutes**

[Back to Index](00-INDEX.md)

---

## What is HAIAMM?

HAIAMM (Human-Assisted Intelligence Assurance Maturity Model) is a practical framework for securing AI systems. It covers everything from simple LLM integrations to fully autonomous agent deployments across six security domains and twelve practices.

**Core Principle:** Security that actually works, measured by outcomes, not checkboxes.

---

## Who is This For?

- **Security teams** responsible for AI/ML system security
- **Engineering teams** building LLM applications or AI agents
- **CISOs and security leaders** establishing AI security programs
- **Compliance teams** addressing AI-specific regulatory requirements

---

## Pick Your Path

### What are you building?

```
                    ┌─────────────────────────────────────┐
                    │     What are you working on?        │
                    └─────────────────┬───────────────────┘
                                      │
            ┌─────────────────────────┼─────────────────────────┐
            │                         │                         │
            ▼                         ▼                         ▼
    ┌───────────────┐       ┌─────────────────┐       ┌─────────────────┐
    │ LLM App       │       │ AI Agents       │       │ AI Security     │
    │ (chatbot,     │       │ (autonomous,    │       │ Program         │
    │ copilot, RAG) │       │ tool-using)     │       │ (enterprise)    │
    └───────┬───────┘       └────────┬────────┘       └────────┬────────┘
            │                        │                         │
            ▼                        ▼                         ▼
    ┌───────────────┐       ┌─────────────────┐       ┌─────────────────┐
    │ Top 10 LLM    │       │ Top 10 Agentic  │       │ First 30 Days   │
    │ Risks         │       │ Risks           │       │ Roadmap         │
    └───────────────┘       └─────────────────┘       └─────────────────┘
```

**Choose your path:**

| If you're... | Go to... |
|--------------|----------|
| Building an LLM chatbot, copilot, or RAG system | [Top 10 LLM Risks](03-TOP10-LLM-RISKS.md) |
| Deploying autonomous AI agents with tool access | [Top 10 Agentic Risks](04-TOP10-AGENTIC-RISKS.md) |
| Establishing an enterprise AI security program | [First 30 Days](02-FIRST-30-DAYS.md) |
| Assessing current AI security posture | [Assessment Checklist](07-ASSESSMENT-CHECKLIST.md) |
| Looking for specific tools | [Tools & Resources](08-TOOLS-RESOURCES.md) |

---

## 5 Quick Wins You Can Do Today

These actions take less than 1 hour each and immediately improve your AI security:

### 1. Inventory Your AI Systems (30 min)

**Action:** Create a list of all AI/ML systems in your environment.

```markdown
## AI System Inventory Template

| System Name | Type | Data Access | Tool Access | Owner | Risk Level |
|-------------|------|-------------|-------------|-------|------------|
| Support Bot | LLM  | Customer data | None | @alice | Medium |
| Code Agent  | Agent | Source code | Git, Shell | @bob | High |
| RAG Search  | LLM  | Internal docs | None | @carol | Medium |
```

**Why:** You can't secure what you don't know exists. Shadow AI is real.

---

### 2. Add Input Validation (30 min)

**Action:** Implement basic input validation on all LLM endpoints.

```python
# Simple input validation example
def validate_llm_input(user_input: str) -> bool:
    # Length limits
    if len(user_input) > 10000:
        return False

    # Basic injection patterns (expand based on your threat model)
    dangerous_patterns = [
        "ignore previous instructions",
        "ignore all instructions",
        "system prompt",
        "you are now",
    ]

    lower_input = user_input.lower()
    for pattern in dangerous_patterns:
        if pattern in lower_input:
            log_security_event("prompt_injection_attempt", user_input)
            return False

    return True
```

**Why:** Prompt injection is the #1 LLM vulnerability. Basic filtering stops naive attacks.

---

### 3. Enable Output Logging (20 min)

**Action:** Log all LLM inputs and outputs (with PII redaction).

```python
import hashlib
import logging

security_logger = logging.getLogger("ai_security")

def log_llm_interaction(user_id: str, input_text: str, output_text: str):
    """Log LLM interactions for security monitoring."""
    security_logger.info({
        "event": "llm_interaction",
        "user_id_hash": hashlib.sha256(user_id.encode()).hexdigest()[:16],
        "input_length": len(input_text),
        "output_length": len(output_text),
        "timestamp": datetime.utcnow().isoformat(),
        # Store full content in secure, access-controlled storage
        "content_ref": store_encrypted(input_text, output_text)
    })
```

**Why:** You need visibility to detect attacks and investigate incidents.

---

### 4. Restrict Agent Permissions (30 min)

**Action:** Apply least privilege to any AI agent with tool access.

```yaml
# Agent permission configuration example
agent_permissions:
  code_assistant:
    allowed_tools:
      - read_file      # Read-only file access
      - search_code    # Search codebase
    denied_tools:
      - write_file     # No write access
      - execute_shell  # No shell access
      - send_email     # No external communication
    rate_limits:
      api_calls_per_minute: 10
      tokens_per_request: 4000
    data_access:
      - source_code: read
      - secrets: none
      - production_data: none
```

**Why:** ASI02 (Tool Misuse) and ASI03 (Privilege Abuse) are top agent risks.

---

### 5. Define Your "Kill Switch" (15 min)

**Action:** Document how to immediately disable AI systems in an emergency.

```markdown
## AI Emergency Response Procedures

### Immediate Shutdown
1. **API Gateway:** Disable routes matching `/api/ai/*` in load balancer
2. **Feature Flag:** Set `AI_ENABLED=false` in config service
3. **Network:** Block outbound to `api.openai.com`, `api.anthropic.com`

### Contacts
- AI Platform Lead: @alice (555-0100)
- Security On-Call: @security-oncall (555-0200)
- Incident Commander: Use #incident-response Slack

### Post-Incident
- Preserve logs before rotation
- Document timeline in incident tracker
- Schedule post-mortem within 48 hours
```

**Why:** When an AI system misbehaves, you need to stop it fast.

---

## Understanding the Framework

### The 6 Domains (What to Secure)

| Domain | Covers | Example Concerns |
|--------|--------|------------------|
| **Software** | AI code, models, apps | Model vulnerabilities, code injection |
| **Infrastructure** | Compute, storage, network | GPU access, model storage, API security |
| **Endpoints** | APIs, UIs, integrations | Prompt injection, output validation |
| **Data** | Training data, I/O, pipelines | Poisoning, privacy, bias |
| **Processes** | Governance, compliance | Model approval, change control |
| **Vendors** | Third-party AI services | API provider risk, model provenance |

### The 12 Practices (How to Secure)

| Category | Practices | Purpose |
|----------|-----------|---------|
| ![Governance](../images/governance_small_logo.png) **Governance** | SM, PC, EG | Strategy, policies, training |
| ![Building](../images/building_small_logo.png) **Building** | TA, SR, SA | Threats, requirements, architecture |
| ![Verification](../images/verification_small_logo.png) **Verification** | DR, IR, ST | Design review, implementation review, testing |
| ![Operations](../images/operations_small_logo.png) **Operations** | IM, EH, ML | Issues, hardening, monitoring |

### The 3 Maturity Levels (How Well)

| Level | Name | You're Here If... |
|-------|------|-------------------|
| **1** | Foundation | Ad-hoc security, individual efforts, basic awareness |
| **2** | Structured | Documented processes, consistent execution, defined roles |
| **3** | Optimized | Measured outcomes, continuous improvement, automation |

---

## What's Different About AI Security?

Traditional application security doesn't fully address AI-specific risks:

| Traditional Security | AI-Specific Extension |
|---------------------|----------------------|
| SQL injection | **Prompt injection** - manipulating LLM behavior |
| Input validation | **Semantic validation** - understanding intent |
| Access control | **Tool access control** - what can the AI do? |
| Data protection | **Training data protection** - poisoning prevention |
| Logging | **Reasoning logging** - why did the AI decide this? |
| Incident response | **AI rollback** - reverting to safe model versions |

---

## Common Starting Points by Role

### For Security Engineers
1. Start with [Assessment Checklist](07-ASSESSMENT-CHECKLIST.md)
2. Focus on [Top 10 Agentic Risks](04-TOP10-AGENTIC-RISKS.md)
3. Implement controls from [Environment Hardening](../practices/EH-Software-OnePager.md)

### For ML/AI Engineers
1. Read [Top 10 LLM Risks](03-TOP10-LLM-RISKS.md)
2. Review [Secure Architecture](../practices/SA-Software-OnePager.md)
3. Implement [Security Testing](../practices/ST-Software-OnePager.md)

### For Security Leaders
1. Start with [First 30 Days](02-FIRST-30-DAYS.md)
2. Use [Risk-Practice Matrix](05-RISK-PRACTICE-MATRIX.md) for prioritization
3. Build roadmap using [Maturity Roadmap](06-MATURITY-ROADMAP.md)

### For Compliance Teams
1. Review [Policy & Compliance](../practices/PC-Processes-OnePager.md)
2. Map requirements using [Risk-Practice Matrix](05-RISK-PRACTICE-MATRIX.md)
3. Document with [Assessment Checklist](07-ASSESSMENT-CHECKLIST.md)

---

## Frequently Asked Questions

### How long does a full assessment take?
- **Quick self-assessment:** 30 minutes ([Assessment Checklist](07-ASSESSMENT-CHECKLIST.md))
- **Full domain assessment:** 2-4 hours per domain
- **Complete assessment:** 2-3 days for all 6 domains

### Where should we start?
- **Most organizations:** Start with Software and Data domains
- **Agent deployments:** Prioritize based on [Top 10 Agentic Risks](04-TOP10-AGENTIC-RISKS.md)
- **Regulatory pressure:** Start with Processes domain (governance, compliance)

### What maturity level should we target?
- **Level 1:** Minimum for any production AI system
- **Level 2:** Standard for business-critical AI systems
- **Level 3:** Required for high-risk AI (financial, healthcare, autonomous)

### How does HAIAMM relate to other frameworks?
- **OWASP Top 10 for LLMs:** HAIAMM practices address all 10 risks
- **OWASP Agentic Top 10:** Full mapping in [Top 10 Agentic Risks](04-TOP10-AGENTIC-RISKS.md)
- **NIST AI RMF:** Complementary - HAIAMM provides implementation details
- **ISO 42001:** HAIAMM supports ISO 42001 control implementation

---

## Next Steps

**Choose your next action:**

| Goal | Action |
|------|--------|
| Quick security improvements | Complete the 5 Quick Wins above |
| Comprehensive AI agent security | [Top 10 Agentic Risks](04-TOP10-AGENTIC-RISKS.md) |
| LLM application security | [Top 10 LLM Risks](03-TOP10-LLM-RISKS.md) |
| Build a security program | [First 30 Days](02-FIRST-30-DAYS.md) |
| Assess current state | [Assessment Checklist](07-ASSESSMENT-CHECKLIST.md) |
| Find specific tools | [Tools & Resources](08-TOOLS-RESOURCES.md) |

---

## Document Information

| Field | Value |
|-------|-------|
| Practice | Quick Start Guide |
| HAIAMM Version | 2.2 |
| Last Updated | January 2026 |

[Back to Index](00-INDEX.md) | [First 30 Days](02-FIRST-30-DAYS.md) | [Assessment Checklist](07-ASSESSMENT-CHECKLIST.md)
