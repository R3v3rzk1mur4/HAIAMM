# OWASP Top 10 for LLM Applications - HAIAMM Mapping

**Security controls for LLM application risks**

[Back to Index](00-INDEX.md) | [Quick Start](01-QUICK-START.md) | [Agentic Risks](04-TOP10-AGENTIC-RISKS.md)

---

## Overview

The OWASP Top 10 for LLM Applications (2025) identifies critical security risks for systems using Large Language Models. This document maps each risk to HAIAMM practices with measurable outcomes and practical guidance.

---

## Risk Summary Matrix

| ID | Risk | Severity | Primary Practices | Domain Focus |
|----|------|----------|-------------------|--------------|
| LLM01 | Prompt Injection | Critical | SR, ST, EH | Software, Endpoints |
| LLM02 | Sensitive Information Disclosure | High | PC, DR, ML | Data, Software |
| LLM03 | Supply Chain | High | SA, IM, EH | Vendors, Software |
| LLM04 | Data and Model Poisoning | High | TA, DR, ST | Data, Software |
| LLM05 | Improper Output Handling | High | SR, IR, ST | Software, Endpoints |
| LLM06 | Excessive Agency | Critical | SA, PC, ML | Processes, Software |
| LLM07 | System Prompt Leakage | Medium | EH, ST, ML | Software, Endpoints |
| LLM08 | Vector and Embedding Weaknesses | High | SA, ST, EH | Data, Infrastructure |
| LLM09 | Misinformation | Medium | DR, ST, ML | Software, Processes |
| LLM10 | Unbounded Consumption | Medium | SR, EH, ML | Infrastructure, Software |

---

## LLM01: Prompt Injection

### Risk Description

Attackers manipulate LLM behavior through crafted inputs that override system instructions or inject malicious commands.

**Attack Types:**
- **Direct Injection:** User inputs that attempt to override system prompts
- **Indirect Injection:** Malicious content in external data sources (documents, web pages)

### HAIAMM Practice Mapping

| Practice | Role | Domain |
|----------|------|--------|
| **SR** (Security Requirements) | Define input validation rules | Software |
| **ST** (Security Testing) | Test for injection vulnerabilities | Software |
| **EH** (Environment Hardening) | Implement input sanitization | Endpoints |

### Measurable Outcomes

**Outcome 1: Injection Detection Rate**
- **Target:** >90% of known injection patterns detected
- **Formula:** `Detected Attempts / Total Test Cases × 100`
- **Data Source:** Security testing results, WAF logs
- **Validation:** Quarterly red team testing with updated attack patterns

**Outcome 2: Input Validation Coverage**
- **Target:** 100% of user inputs validated before LLM processing
- **Formula:** `Validated Inputs / Total Inputs × 100`
- **Data Source:** Input validation gateway logs

**Outcome 3: False Positive Rate**
- **Target:** <5% of legitimate inputs blocked
- **Formula:** `Blocked Legitimate Inputs / Total Legitimate Inputs × 100`

### Implementation Actions

```python
# Example: Basic prompt injection detection
INJECTION_PATTERNS = [
    r"ignore\s+(all\s+)?previous\s+instructions",
    r"you\s+are\s+now\s+a",
    r"disregard\s+(your\s+)?programming",
    r"forget\s+(everything|all)",
    r"system\s*:\s*",
    r"<\|.*?\|>",  # Common prompt delimiters
]

def detect_injection(user_input: str) -> tuple[bool, str]:
    """Detect potential prompt injection attempts."""
    import re
    for pattern in INJECTION_PATTERNS:
        if re.search(pattern, user_input, re.IGNORECASE):
            return True, pattern
    return False, ""
```

### Quick Wins
1. Implement input length limits (block >10K character inputs)
2. Add pattern-based injection detection
3. Use separate system/user message channels
4. Log all inputs for forensic analysis

---

## LLM02: Sensitive Information Disclosure

### Risk Description

LLMs expose sensitive data through training data memorization, prompt context leakage, or overly verbose responses.

### HAIAMM Practice Mapping

| Practice | Role | Domain |
|----------|------|--------|
| **PC** (Policy & Compliance) | Define data handling policies | Data |
| **DR** (Design Review) | Review data flow architecture | Software |
| **ML** (Monitoring & Logging) | Monitor for data leakage | Data |

### Measurable Outcomes

**Outcome 1: PII Detection in Outputs**
- **Target:** <0.1% of outputs contain PII
- **Formula:** `Outputs with PII / Total Outputs × 100`
- **Data Source:** Output scanning logs
- **Validation:** Sample 1% of outputs for manual review

**Outcome 2: Sensitive Data Masking**
- **Target:** 100% of sensitive fields masked in logs
- **Formula:** `Masked Fields / Total Sensitive Fields × 100`

**Outcome 3: Data Classification Coverage**
- **Target:** >95% of data sources classified
- **Formula:** `Classified Sources / Total Sources × 100`

### Implementation Actions

```python
# Example: Output PII scanning
import re

PII_PATTERNS = {
    "ssn": r"\b\d{3}-\d{2}-\d{4}\b",
    "credit_card": r"\b\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}\b",
    "email": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",
    "phone": r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b",
}

def scan_for_pii(text: str) -> list[dict]:
    """Scan text for PII patterns."""
    findings = []
    for pii_type, pattern in PII_PATTERNS.items():
        matches = re.findall(pattern, text)
        if matches:
            findings.append({"type": pii_type, "count": len(matches)})
    return findings
```

### Quick Wins
1. Implement output PII scanning
2. Add data classification to training data
3. Use output filters for sensitive patterns
4. Audit prompt context for unnecessary data

---

## LLM03: Supply Chain

### Risk Description

Compromised pre-trained models, poisoned training data, or vulnerable dependencies introduce security risks.

### HAIAMM Practice Mapping

| Practice | Role | Domain |
|----------|------|--------|
| **SA** (Secure Architecture) | Design secure model pipeline | Vendors |
| **IM** (Issue Management) | Track model vulnerabilities | Software |
| **EH** (Environment Hardening) | Secure model storage | Vendors |

### Measurable Outcomes

**Outcome 1: Model Provenance Verification**
- **Target:** 100% of production models have verified provenance
- **Formula:** `Verified Models / Total Models × 100`

**Outcome 2: Dependency Vulnerability Coverage**
- **Target:** 0 critical vulnerabilities in dependencies
- **Formula:** Count of critical CVEs in active dependencies

**Outcome 3: Model Update Latency**
- **Target:** <48 hours to patch critical model vulnerabilities
- **Formula:** `Patch Applied Timestamp - Advisory Timestamp`

### Implementation Actions

- Verify model checksums from trusted sources
- Scan ML frameworks for vulnerabilities (PyTorch, TensorFlow, etc.)
- Implement model versioning and rollback capability
- Use private model registries with access controls

### Quick Wins
1. Create model inventory with sources
2. Enable dependency scanning in CI/CD
3. Subscribe to model provider security advisories
4. Implement model checksum verification

---

## LLM04: Data and Model Poisoning

### Risk Description

Malicious data in training, fine-tuning, or RAG pipelines corrupts model behavior.

### HAIAMM Practice Mapping

| Practice | Role | Domain |
|----------|------|--------|
| **TA** (Threat Assessment) | Identify poisoning vectors | Data |
| **DR** (Design Review) | Review data pipeline security | Data |
| **ST** (Security Testing) | Test for poisoning resilience | Software |

### Measurable Outcomes

**Outcome 1: Data Validation Coverage**
- **Target:** 100% of training data validated
- **Formula:** `Validated Records / Total Records × 100`

**Outcome 2: RAG Content Integrity**
- **Target:** 100% of RAG sources from trusted origins
- **Formula:** `Trusted Sources / Total Sources × 100`

**Outcome 3: Poisoning Detection Rate**
- **Target:** >80% of poisoning attempts detected
- **Formula:** `Detected Attempts / Total Injection Attempts × 100`

### Implementation Actions

- Implement data source allowlisting
- Add content validation for RAG ingestion
- Monitor for sudden model behavior changes
- Use data provenance tracking

### Quick Wins
1. Inventory all data sources feeding the model
2. Implement source verification for RAG
3. Add anomaly detection on model outputs
4. Create data quality metrics

---

## LLM05: Improper Output Handling

### Risk Description

LLM outputs are used unsafely, leading to XSS, SQL injection, or code execution when outputs are rendered or processed.

### HAIAMM Practice Mapping

| Practice | Role | Domain |
|----------|------|--------|
| **SR** (Security Requirements) | Define output handling rules | Software |
| **IR** (Implementation Review) | Review output processing implementation | Software |
| **ST** (Security Testing) | Test output handling | Endpoints |

### Measurable Outcomes

**Outcome 1: Output Sanitization Coverage**
- **Target:** 100% of LLM outputs sanitized before use
- **Formula:** `Sanitized Outputs / Total Outputs × 100`

**Outcome 2: Injection Prevention**
- **Target:** 0 successful secondary injections via LLM output
- **Formula:** Count of incidents where LLM output caused injection

### Implementation Actions

```python
# Example: Output sanitization for web display
import html

def sanitize_for_html(llm_output: str) -> str:
    """Sanitize LLM output for safe HTML rendering."""
    # Escape HTML entities
    sanitized = html.escape(llm_output)
    # Remove potential script patterns
    sanitized = re.sub(r'javascript:', '', sanitized, flags=re.IGNORECASE)
    return sanitized

def sanitize_for_sql(llm_output: str) -> str:
    """Never use LLM output directly in SQL - use parameters."""
    # This is an anti-pattern warning
    raise ValueError("Never interpolate LLM output into SQL queries")
```

### Quick Wins
1. Treat all LLM outputs as untrusted input
2. Use parameterized queries (never interpolate outputs)
3. Implement context-aware output encoding
4. Add output validation before processing

---

## LLM06: Excessive Agency

### Risk Description

LLM applications are granted too much autonomy, leading to unintended actions with real-world consequences.

### HAIAMM Practice Mapping

| Practice | Role | Domain |
|----------|------|--------|
| **SA** (Secure Architecture) | Design bounded agency | Processes |
| **PC** (Policy & Compliance) | Define agency limits | Software |
| **ML** (Monitoring & Logging) | Monitor autonomous actions | Software |

### Measurable Outcomes

**Outcome 1: Action Scope Compliance**
- **Target:** 100% of LLM actions within defined scope
- **Formula:** `In-Scope Actions / Total Actions × 100`

**Outcome 2: Human Override Availability**
- **Target:** 100% of high-risk actions have human override option
- **Formula:** `Actions with Override / High-Risk Actions × 100`

**Outcome 3: Autonomy Level Tracking**
- **Target:** All agents classified by autonomy level
- **Formula:** `Classified Agents / Total Agents × 100`

### Implementation Actions

- Define action allowlists per LLM application
- Implement approval workflows for high-impact actions
- Add rate limits on autonomous actions
- Create "kill switch" for immediate agent disablement

### Quick Wins
1. Document all actions each LLM can take
2. Implement action allowlisting
3. Add human-in-the-loop for destructive operations
4. Create emergency shutdown procedure

---

## LLM07: System Prompt Leakage

### Risk Description

System prompts containing sensitive instructions, business logic, or security controls are exposed through crafted queries.

### HAIAMM Practice Mapping

| Practice | Role | Domain |
|----------|------|--------|
| **EH** (Environment Hardening) | Protect system prompts | Software |
| **ST** (Security Testing) | Test for prompt leakage | Endpoints |
| **ML** (Monitoring & Logging) | Detect leakage attempts | Software |

### Measurable Outcomes

**Outcome 1: Leakage Attempt Detection**
- **Target:** >90% of leakage attempts detected
- **Formula:** `Detected Attempts / Total Test Attempts × 100`

**Outcome 2: System Prompt Exposure**
- **Target:** 0 successful system prompt extractions
- **Formula:** Count of confirmed leakage incidents

### Implementation Actions

```python
# Example: System prompt protection patterns
LEAKAGE_PATTERNS = [
    r"what\s+(is|are)\s+your\s+(system\s+)?instructions",
    r"repeat\s+(your\s+)?system\s+prompt",
    r"show\s+(me\s+)?your\s+rules",
    r"ignore\s+and\s+(output|print|show)",
]

def detect_leakage_attempt(user_input: str) -> bool:
    """Detect attempts to extract system prompt."""
    for pattern in LEAKAGE_PATTERNS:
        if re.search(pattern, user_input, re.IGNORECASE):
            return True
    return False
```

### Quick Wins
1. Avoid sensitive data in system prompts
2. Implement leakage attempt detection
3. Add "do not reveal" instructions (defense in depth)
4. Test with common leakage prompts

---

## LLM08: Vector and Embedding Weaknesses

### Risk Description

Vulnerabilities in RAG implementations and vector stores lead to information disclosure or manipulation.

### HAIAMM Practice Mapping

| Practice | Role | Domain |
|----------|------|--------|
| **SA** (Secure Architecture) | Design secure RAG architecture | Data |
| **ST** (Security Testing) | Test embedding security | Infrastructure |
| **EH** (Environment Hardening) | Secure vector stores | Data |

### Measurable Outcomes

**Outcome 1: Access Control Enforcement**
- **Target:** 100% of vector queries respect access controls
- **Formula:** `Authorized Queries / Total Queries × 100`

**Outcome 2: Embedding Integrity**
- **Target:** 100% of embeddings from verified sources
- **Formula:** `Verified Embeddings / Total Embeddings × 100`

### Implementation Actions

- Implement row-level security in vector stores
- Validate embedding sources before ingestion
- Add access control checks at retrieval time
- Monitor for unusual query patterns

### Quick Wins
1. Audit vector store access controls
2. Implement source tracking for embeddings
3. Add query logging and monitoring
4. Test cross-tenant data isolation

---

## LLM09: Misinformation

### Risk Description

LLMs generate false or misleading information (hallucinations) that users trust as factual.

### HAIAMM Practice Mapping

| Practice | Role | Domain |
|----------|------|--------|
| **DR** (Design Review) | Review accuracy requirements | Software |
| **ST** (Security Testing) | Test for hallucination rates | Processes |
| **ML** (Monitoring & Logging) | Monitor accuracy metrics | Software |

### Measurable Outcomes

**Outcome 1: Factual Accuracy Rate**
- **Target:** >95% accuracy for factual claims
- **Formula:** `Correct Claims / Total Verifiable Claims × 100`
- **Validation:** Sample-based human review

**Outcome 2: Citation Coverage**
- **Target:** >90% of factual claims cite sources
- **Formula:** `Cited Claims / Total Factual Claims × 100`

### Implementation Actions

- Implement grounding with verified sources
- Add confidence scoring to outputs
- Use retrieval augmentation for factual queries
- Display uncertainty indicators to users

### Quick Wins
1. Add "AI-generated" disclaimers
2. Implement RAG for factual queries
3. Train users on LLM limitations
4. Add feedback mechanism for corrections

---

## LLM10: Unbounded Consumption

### Risk Description

LLMs consume excessive resources through denial of service attacks or inefficient queries.

### HAIAMM Practice Mapping

| Practice | Role | Domain |
|----------|------|--------|
| **SR** (Security Requirements) | Define resource limits | Infrastructure |
| **EH** (Environment Hardening) | Implement rate limiting | Software |
| **ML** (Monitoring & Logging) | Monitor resource usage | Infrastructure |

### Measurable Outcomes

**Outcome 1: Rate Limit Enforcement**
- **Target:** 100% of API endpoints rate-limited
- **Formula:** `Rate-Limited Endpoints / Total Endpoints × 100`

**Outcome 2: Cost Anomaly Detection**
- **Target:** >90% of cost spikes detected within 1 hour
- **Formula:** `Detected Spikes / Total Spikes × 100`

**Outcome 3: Resource Budget Compliance**
- **Target:** <5% budget overruns
- **Formula:** `Actual Cost / Budgeted Cost × 100`

### Implementation Actions

```python
# Example: Token-based rate limiting
from collections import defaultdict
from time import time

class TokenRateLimiter:
    def __init__(self, tokens_per_minute: int):
        self.limit = tokens_per_minute
        self.usage = defaultdict(list)

    def check(self, user_id: str, tokens: int) -> bool:
        now = time()
        minute_ago = now - 60

        # Clean old entries
        self.usage[user_id] = [
            (t, tok) for t, tok in self.usage[user_id]
            if t > minute_ago
        ]

        # Calculate current usage
        current = sum(tok for _, tok in self.usage[user_id])

        if current + tokens > self.limit:
            return False

        self.usage[user_id].append((now, tokens))
        return True
```

### Quick Wins
1. Implement per-user rate limiting
2. Add token budgets per request
3. Set up cost alerting
4. Implement request timeout limits

---

## Document Information

| Field | Value |
|-------|-------|
| Document | OWASP Top 10 for LLM Applications - HAIAMM Mapping |
| HAIAMM Version | 2.2 |
| OWASP LLM Version | 2025 |
| Last Updated | January 2026 |

---

**Related Documents:**
- [Quick Start Guide](01-QUICK-START.md)
- [Top 10 Agentic Risks](04-TOP10-AGENTIC-RISKS.md)
- [Risk-Practice Matrix](05-RISK-PRACTICE-MATRIX.md)
- [Tools & Resources](08-TOOLS-RESOURCES.md)

[Back to Index](00-INDEX.md)
