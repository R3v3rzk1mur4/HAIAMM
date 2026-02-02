
# HAIAMM Handbook v2.0

## Human Assisted Intelligence Assurance Maturity Model

**Practical Security for AI Systems, LLM Applications, and Autonomous Agents**

---

> **Note on Code Examples**
>
> Code snippets throughout this handbook are **illustrative examples only**. They are intended to demonstrate security concepts and provide context for implementation patterns—not to serve as production-ready code. Always adapt examples to your specific environment, follow your organization's coding standards, and conduct thorough security reviews before deployment.

---

## What is HAIAMM?

HAIAMM is a comprehensive framework for securing Human-Assisted Intelligence (HAI) systems. It provides actionable guidance for organizations building, deploying, and operating AI applications—from simple LLM integrations to fully autonomous agent systems.

**HAIAMM is NOT another checkbox compliance framework.** It's a practical roadmap with:
- Measurable outcomes (not just activities)
- Risk-based prioritization (address real threats first)
- Implementation guidance (time, cost, effort estimates)
- Tool recommendations (what to actually use)

---

## How to Use This Handbook

### Pick Your Starting Point

| Your Situation | Start Here |
|----------------|------------|
| "I have 10 minutes" | [Quick Start Guide](01-QUICK-START.md) |
| "I'm building with LLMs" | [Top 10 LLM Risks](03-TOP10-LLM-RISKS.md) |
| "I'm deploying AI agents" | [Top 10 Agentic Risks](04-TOP10-AGENTIC-RISKS.md) |
| "I need to assess our security" | [Assessment Checklist](07-ASSESSMENT-CHECKLIST.md) |
| "I want a structured program" | [First 30 Days](02-FIRST-30-DAYS.md) |
| "Show me everything" | Keep reading below |

---

## Quick Links

- [Quick Start Guide](01-QUICK-START.md) - Get started in 5-10 minutes
- [First 30 Days](02-FIRST-30-DAYS.md) - Day-by-day implementation roadmap
- [OWASP Top 10 for Agentic Apps](04-TOP10-AGENTIC-RISKS.md) - Priority security risks for AI agents
- [OWASP Top 10 for LLMs](03-TOP10-LLM-RISKS.md) - Security risks for LLM applications
- [Risk-Practice Matrix](05-RISK-PRACTICE-MATRIX.md) - Which practices address which risks
- [Maturity Roadmap](06-MATURITY-ROADMAP.md) - Level 1 → 2 → 3 progression
- [Assessment Checklist](07-ASSESSMENT-CHECKLIST.md) - Quick self-assessment (30 min)
- [Tools & Resources](08-TOOLS-RESOURCES.md) - Recommended tools by practice
- [Framework Mappings](09-FRAMEWORK-MAPPINGS.md) - BSIMM, OpenSAMM, NIST AI RMF, NIST CSF alignment

---

## The HAIAMM Framework

### Six Security Domains

HAIAMM organizes AI security into six domains, each addressing a critical aspect of HAI systems:

| Domain | Focus | Key Concerns |
|--------|-------|--------------|
| **Software** | AI model code, applications, integrations | Model vulnerabilities, code security, CI/CD |
| **Infrastructure** | Compute, storage, networks | GPU security, cloud services, distributed training |
| **Endpoints** | APIs, UIs, integration points | Prompt injection, output validation, access control |
| **Data** | Training data, model I/O, pipelines | Data poisoning, privacy, bias, lineage |
| **Processes** | Governance, compliance, operations | Model governance, ethics, regulatory compliance |
| **Vendors** | Third-party AI services and tools | Supply chain, model provenance, vendor risk |

### Twelve Security Practices

Each domain contains four business functions with twelve practices:

---

### ![Governance](../images/governance_logo.png) Governance

*How you govern AI security agents*

| Practice | Code | Purpose |
|----------|------|---------|
| Strategy & Metrics | SM | Define AI security strategy and measure effectiveness |
| Policy & Compliance | PC | Establish policies and ensure regulatory compliance |
| Education & Guidance | EG | Train teams on AI security best practices |

---

### ![Building](../images/building_small_logo.png) Building

*How you build AI agents securely*

| Practice | Code | Purpose |
|----------|------|---------|
| Threat Assessment | TA | Identify and prioritize AI-specific threats |
| Security Requirements | SR | Define security requirements for AI systems |
| Secure Architecture | SA | Design secure AI system architectures |

---

### ![Verification](../images/verification_thumbnail_small_logo.png) Verification

*How you verify AI agents work correctly*

| Practice | Code | Purpose |
|----------|------|---------|
| Design Review | DR | Review AI system designs for security flaws |
| Implementation Review | IR | Review AI implementations for vulnerabilities |
| Security Testing | ST | Test AI systems for security weaknesses |

---

### ![Operations](../images/operations_thumbnail_small_logo.png) Operations

*How you run AI agents safely*

| Practice | Code | Purpose |
|----------|------|---------|
| Issue Management | IM | Track and remediate security issues |
| Environment Hardening | EH | Secure AI runtime environments |
| Monitoring & Logging | ML | Monitor AI systems for security events |

### Three Maturity Levels

Each practice has three maturity levels:

| Level | Name | Characteristics |
|-------|------|-----------------|
| **1** | Foundation | Basic understanding, ad-hoc activities, individual effort |
| **2** | Structured | Documented requirements, consistent processes, defined roles |
| **3** | Optimized | Quantitative management, continuous improvement, measured outcomes |

---

## Domain Deep Dives

### Software Domain

Security of AI model code, application software, and integration layers.

**One-Pagers:**
- [SM - Strategy & Metrics](../practices/SM-Software-OnePager.md)
- [PC - Policy & Compliance](../practices/PC-Software-OnePager.md)
- [EG - Education & Guidance](../practices/EG-Software-OnePager.md)
- [TA - Threat Assessment](../practices/TA-Software-OnePager.md)
- [SR - Security Requirements](../practices/SR-Software-OnePager.md)
- [SA - Secure Architecture](../practices/SA-Software-OnePager.md)
- [DR - Design Review](../practices/DR-Software-OnePager.md)
- [IR - Implementation Review](../practices/IR-Software-OnePager.md)
- [ST - Security Testing](../practices/ST-Software-OnePager.md)
- [IM - Issue Management](../practices/IM-Software-OnePager.md)
- [EH - Environment Hardening](../practices/EH-Software-OnePager.md)
- [ML - Monitoring & Logging](../practices/ML-Software-OnePager.md)

### Infrastructure Domain

Security of compute, storage, and network infrastructure supporting AI workloads.

**One-Pagers:**
- [SM - Strategy & Metrics](../practices/SM-Infrastructure-OnePager.md)
- [PC - Policy & Compliance](../practices/PC-Infrastructure-OnePager.md)
- [EG - Education & Guidance](../practices/EG-Infrastructure-OnePager.md)
- [TA - Threat Assessment](../practices/TA-Infrastructure-OnePager.md)
- [SR - Security Requirements](../practices/SR-Infrastructure-OnePager.md)
- [SA - Secure Architecture](../practices/SA-Infrastructure-OnePager.md)
- [DR - Design Review](../practices/DR-Infrastructure-OnePager.md)
- [IR - Implementation Review](../practices/IR-Infrastructure-OnePager.md)
- [ST - Security Testing](../practices/ST-Infrastructure-OnePager.md)
- [IM - Issue Management](../practices/IM-Infrastructure-OnePager.md)
- [EH - Environment Hardening](../practices/EH-Infrastructure-OnePager.md)
- [ML - Monitoring & Logging](../practices/ML-Infrastructure-OnePager.md)

### Endpoints Domain

Security of APIs, user interfaces, and integration points for AI systems.

**One-Pagers:**
- [SM - Strategy & Metrics](../practices/SM-Endpoints-OnePager.md)
- [PC - Policy & Compliance](../practices/PC-Endpoints-OnePager.md)
- [EG - Education & Guidance](../practices/EG-Endpoints-OnePager.md)
- [TA - Threat Assessment](../practices/TA-Endpoints-OnePager.md)
- [SR - Security Requirements](../practices/SR-Endpoints-OnePager.md)
- [SA - Secure Architecture](../practices/SA-Endpoints-OnePager.md)
- [DR - Design Review](../practices/DR-Endpoints-OnePager.md)
- [IR - Implementation Review](../practices/IR-Endpoints-OnePager.md)
- [ST - Security Testing](../practices/ST-Endpoints-OnePager.md)
- [IM - Issue Management](../practices/IM-Endpoints-OnePager.md)
- [EH - Environment Hardening](../practices/EH-Endpoints-OnePager.md)
- [ML - Monitoring & Logging](../practices/ML-Endpoints-OnePager.md)

### Data Domain

Security of training data, model inputs/outputs, and data pipelines.

**One-Pagers:**
- [SM - Strategy & Metrics](../practices/SM-Data-OnePager.md)
- [PC - Policy & Compliance](../practices/PC-Data-OnePager.md)
- [EG - Education & Guidance](../practices/EG-Data-OnePager.md)
- [TA - Threat Assessment](../practices/TA-Data-OnePager.md)
- [SR - Security Requirements](../practices/SR-Data-OnePager.md)
- [SA - Secure Architecture](../practices/SA-Data-OnePager.md)
- [DR - Design Review](../practices/DR-Data-OnePager.md)
- [IR - Implementation Review](../practices/IR-Data-OnePager.md)
- [ST - Security Testing](../practices/ST-Data-OnePager.md)
- [IM - Issue Management](../practices/IM-Data-OnePager.md)
- [EH - Environment Hardening](../practices/EH-Data-OnePager.md)
- [ML - Monitoring & Logging](../practices/ML-Data-OnePager.md)

### Processes Domain

Governance, compliance, and operational processes for AI systems.

**One-Pagers:**
- [SM - Strategy & Metrics](../practices/SM-Processes-OnePager.md)
- [PC - Policy & Compliance](../practices/PC-Processes-OnePager.md)
- [EG - Education & Guidance](../practices/EG-Processes-OnePager.md)
- [TA - Threat Assessment](../practices/TA-Processes-OnePager.md)
- [SR - Security Requirements](../practices/SR-Processes-OnePager.md)
- [SA - Secure Architecture](../practices/SA-Processes-OnePager.md)
- [DR - Design Review](../practices/DR-Processes-OnePager.md)
- [IR - Implementation Review](../practices/IR-Processes-OnePager.md)
- [ST - Security Testing](../practices/ST-Processes-OnePager.md)
- [IM - Issue Management](../practices/IM-Processes-OnePager.md)
- [EH - Environment Hardening](../practices/EH-Processes-OnePager.md)
- [ML - Monitoring & Logging](../practices/ML-Processes-OnePager.md)

### Vendors Domain

Security of third-party AI services, models, and vendor relationships.

**One-Pagers:**
- [SM - Strategy & Metrics](../practices/SM-Vendors-OnePager.md)
- [PC - Policy & Compliance](../practices/PC-Vendors-OnePager.md)
- [EG - Education & Guidance](../practices/EG-Vendors-OnePager.md)
- [TA - Threat Assessment](../practices/TA-Vendors-OnePager.md)
- [SR - Security Requirements](../practices/SR-Vendors-OnePager.md)
- [SA - Secure Architecture](../practices/SA-Vendors-OnePager.md)
- [DR - Design Review](../practices/DR-Vendors-OnePager.md)
- [IR - Implementation Review](../practices/IR-Vendors-OnePager.md)
- [ST - Security Testing](../practices/ST-Vendors-OnePager.md)
- [IM - Issue Management](../practices/IM-Vendors-OnePager.md)
- [EH - Environment Hardening](../practices/EH-Vendors-OnePager.md)
- [ML - Monitoring & Logging](../practices/ML-Vendors-OnePager.md)

---

## Risk-Based Prioritization

HAIAMM maps directly to industry-recognized AI security risks:

### OWASP Top 10 for Agentic Applications (2026)
| Risk | Primary HAIAMM Practices |
|------|-------------------------|
| ASI01: Agent Goal Hijack | TA, SR, ST |
| ASI02: Tool Misuse & Exploitation | SA, PC, ML |
| ASI03: Identity & Privilege Abuse | SR, EH, ML |
| ASI04: Agentic Supply Chain | TA, SA, IM |
| ASI05: Unexpected Code Execution | SR, ST, EH |
| ASI06: Memory & Context Poisoning | DR, ST, EH |
| ASI07: Insecure Inter-Agent Comm | SA, SR, ML |
| ASI08: Cascading Failures | SA, IM, ML |
| ASI09: Human-Agent Trust Exploitation | EG, PC, ML |
| ASI10: Rogue Agents | TA, ML, IM |

[Full Agentic Risk Details](04-TOP10-AGENTIC-RISKS.md)

### OWASP Top 10 for LLM Applications (2025)
| Risk | Primary HAIAMM Practices |
|------|-------------------------|
| LLM01: Prompt Injection | SR, ST, EH |
| LLM02: Sensitive Information Disclosure | PC, DR, ML |
| LLM03: Supply Chain | SA, IM, EH |
| LLM04: Data and Model Poisoning | TA, DR, ST |
| LLM05: Improper Output Handling | SR, IR, ST |
| LLM06: Excessive Agency | SA, PC, ML |
| LLM07: System Prompt Leakage | EH, ST, ML |
| LLM08: Vector and Embedding Weaknesses | SA, ST, EH |
| LLM09: Misinformation | DR, ST, ML |
| LLM10: Unbounded Consumption | SR, EH, ML |

[Full LLM Risk Details](03-TOP10-LLM-RISKS.md)

---

## Getting Help

### Assessment Support
- [Self-Assessment Checklist](07-ASSESSMENT-CHECKLIST.md) - 30-minute rapid assessment
- [Risk-Practice Matrix](05-RISK-PRACTICE-MATRIX.md) - Find which practices to prioritize

### Implementation Guidance
- [First 30 Days](02-FIRST-30-DAYS.md) - Day-by-day implementation roadmap
- [Maturity Roadmap](06-MATURITY-ROADMAP.md) - Level progression guidance
- [Tools & Resources](08-TOOLS-RESOURCES.md) - Recommended tools by practice

### Community
- GitHub: [HAIAMM Repository](https://github.com/YOUR_ORG/HAIAMM)
- License: Creative Commons Attribution-ShareAlike 4.0

---

## Document Information

| Field | Value |
|-------|-------|
| Version | 2.0 |
| Last Updated | January 2026 |
| Status | Active |

---

**Next Steps:**
- New to HAIAMM? Start with the [Quick Start Guide](01-QUICK-START.md)
- Building AI agents? Jump to [Top 10 Agentic Risks](04-TOP10-AGENTIC-RISKS.md)
- Ready to assess? Use the [Assessment Checklist](07-ASSESSMENT-CHECKLIST.md)
