![HAIAMM Logo](images/HAIAMM_logo.png)

# HAIAMM Competitive Analysis

**How HAIAMM compares to other AI security frameworks and models**

**Version:** 2.2
**Last Updated:** January 2026

---

## Executive Summary

HAIAMM occupies a unique position in the AI security landscape. While most frameworks ask "Is your AI system secure?", HAIAMM asks "Is your AI system doing security well?" This is a genuinely different question that existing frameworks don't address.

---

## Framework Landscape

### What Each Framework Answers

| Framework | Primary Question |
|-----------|------------------|
| **NIST AI RMF** | How do we govern AI risk? |
| **ISO/IEC 42001** | How do we manage AI systems? |
| **OWASP LLM Top 10** | What vulnerabilities exist in LLMs? |
| **OWASP Agentic Top 10** | What risks exist in AI agents? |
| **MITRE ATLAS** | What adversarial techniques target AI? |
| **EU AI Act** | What compliance is required for AI? |
| **OWASP SAMM** | How mature is our software security? |
| **HAIAMM** | Is AI-operated security actually effective? |

### The Gap HAIAMM Fills

The core insight is valid: AI agents are no longer just being secured—they ARE the security program. When Darktrace autonomously blocks threats, when GitHub Copilot Autofix merges security patches, when AI GRC tools generate compliance evidence, someone needs to ask: "Are these AI security operations actually working?"

No existing framework addresses this question systematically.

---

## Detailed Comparisons

### HAIAMM vs. NIST AI RMF

| Aspect | NIST AI RMF | HAIAMM |
|--------|-------------|--------|
| **Focus** | AI system risk governance | AI-operated security effectiveness |
| **Scope** | All AI systems | AI doing security work |
| **Structure** | 4 functions (Govern, Map, Measure, Manage) | 4 functions, 12 practices, 6 domains |
| **Maturity levels** | No | Yes (L1, L2, L3) |
| **Measurable outcomes** | General guidance | Specific formulas and targets |
| **Implementation guidance** | Playbook (high-level) | First 30 Days (day-by-day) |
| **Interactive tooling** | No | Yes (Verifhai) |

**Relationship:** Complementary. NIST AI RMF helps govern AI systems broadly. HAIAMM helps assess AI systems specifically doing security work.

---

### HAIAMM vs. ISO/IEC 42001

| Aspect | ISO 42001 | HAIAMM |
|--------|-----------|--------|
| **Focus** | AI management system | AI security operations |
| **Approach** | Certification standard | Maturity model |
| **Cost** | Paid standard | Free/open source |
| **Flexibility** | Prescriptive controls | Adaptable practices |
| **Industry adoption** | Growing (ISO brand) | Emerging |

**Relationship:** Complementary. ISO 42001 provides management system certification. HAIAMM provides operational security assessment for AI-operated security specifically.

---

### HAIAMM vs. OWASP Top 10 (LLM & Agentic)

| Aspect | OWASP Top 10 Lists | HAIAMM |
|--------|-------------------|--------|
| **Type** | Risk catalog | Maturity model |
| **Structure** | 10 risks per list | 12 practices × 6 domains × 3 levels |
| **Implementation guidance** | Mitigations per risk | Full practice workflows |
| **Progress tracking** | No | Yes (maturity levels) |
| **Measurable outcomes** | No | Yes (formulas, targets) |
| **Interactive tooling** | No | Yes (Verifhai) |

**Relationship:** HAIAMM incorporates OWASP. Every LLM and Agentic risk is mapped to specific HAIAMM practices with measurable outcomes. OWASP identifies WHAT risks exist; HAIAMM shows HOW to address them systematically.

---

### HAIAMM vs. MITRE ATLAS

| Aspect | MITRE ATLAS | HAIAMM |
|--------|-------------|--------|
| **Focus** | Adversarial threat taxonomy | Security assurance maturity |
| **Purpose** | Threat intelligence | Security improvement |
| **Structure** | Attack techniques matrix | Practice maturity model |
| **Use case** | Red team planning, threat modeling | Program assessment, improvement |

**Relationship:** Complementary. MITRE ATLAS informs HAIAMM's Threat Assessment (TA) practice. ATLAS identifies attack techniques; HAIAMM assesses organizational readiness to defend against them.

---

### HAIAMM vs. OWASP SAMM

| Aspect | OWASP SAMM | HAIAMM |
|--------|------------|--------|
| **Focus** | Software security maturity | AI-operated security maturity |
| **Target** | Human development teams | AI agents doing security |
| **Practices** | 15 practices | 12 practices |
| **Domains** | 5 business functions | 6 security domains |
| **AI-specific** | No | Yes |
| **Open source** | Yes | Yes |

**Relationship:** Parallel models for different eras. SAMM assesses human software security programs. HAIAMM assesses AI-operated security programs. Organizations may need both.

**Important:** HAIAMM is NOT derived from SAMM. While both are maturity models, HAIAMM was designed specifically for AI security operations with different practices, domains, and assessment criteria.

---

## Positioning Map

```
                    Specificity to AI Security
                              ▲
                         High │
                              │
         HAIAMM ●             │
                              │
    ISO 42001 ●               │     ● OWASP LLM Top 10
                              │     ● OWASP Agentic Top 10
                              │     ● MITRE ATLAS
    NIST AI RMF ●             │
                              │
                              │
                              │
    ISO 27001 ●               │
    OWASP SAMM ●              │
                              │
         Low  │               │
    ◄─────────┴───────────────┼─────────────────────────►
    Governance                │              Technical
    Focus                     │              Focus
              Operational Focus
```

**HAIAMM's unique position:** High AI specificity + Operational focus (not just governance or technical risks).

---

## HAIAMM Strengths

### 1. Unique Positioning
No other framework specifically addresses AI agents running security operations. This is a real and growing use case:
- Darktrace AI (autonomous threat response)
- GitHub Copilot Autofix (automated remediation)
- AI GRC tools (compliance automation)
- Wiz AI (continuous pentesting)

### 2. Practical Structure
12 practices × 6 domains × 3 levels is manageable. Not trying to boil the ocean. Clear progression path from Level 1 (Foundation) to Level 3 (Optimized).

### 3. OWASP Alignment
Full mapping to established Top 10 lists (LLM and Agentic) provides:
- Credibility through association with recognized standards
- Actionable risk-to-practice mapping
- Strategic coverage validation

### 4. Measurable Outcomes
The v2.2 addition of formulas and data sources is significant:
- Most maturity models stop at "do you have this?"
- HAIAMM answers "is it working?"
- Specific targets (>90% hijack detection, <4hr MTTD)
- Defined measurement formulas and data sources

### 5. Verifhai Interactive Tooling
Interactive mentor that builds artifacts, not just questionnaires:
- `/verifhai practice sr` builds security requirements
- `/verifhai review` analyzes code for AI-specific risks
- Hands-on guidance, not just assessment

### 6. Open Source Model
Following proven OpenSAMM approach:
- Free framework drives adoption
- Paid services (certification, training) provide validation
- Community contributions improve the model

---

## HAIAMM Weaknesses / Honest Concerns

### 1. Adoption Chicken-and-Egg
A maturity model's value comes from industry adoption and benchmarking data. HAIAMM is new, so "Level 2 certified" doesn't carry weight yet until there's a critical mass of assessments.

**Mitigation:** Focus on early adopter case studies, publish anonymized benchmarking data as it accumulates.

### 2. Validation Gap
The measurable outcomes are well-designed in theory, but haven't been battle-tested:
- Are the targets (>90% hijack detection, <4hr MTTD) realistic?
- Do the formulas capture what matters?
- Are data sources actually available in production environments?

**Mitigation:** Treat v2.2 targets as starting points. Publish validation studies. Adjust targets based on real-world data.

### 3. Overlap Concerns
Organizations already drowning in frameworks (NIST CSF, ISO 27001, SOC 2, PCI-DSS, etc.) may resist adding another. "Framework fatigue" is real.

**Mitigation:** Strong "complementary not competing" messaging. Show how HAIAMM maps to existing compliance requirements. Position as extension, not replacement.

### 4. Scope Creep Risk
6 domains × 12 practices × 3 levels = 216 practice-domain combinations. Could become unwieldy as AI security evolves and new practices are needed.

**Mitigation:** Maintain discipline on core framework. Use extension mechanisms for specialized domains rather than expanding core model.

### 5. AI Security Moving Fast
Framework designed in 2024-2025 may not anticipate 2027 AI architectures:
- Multi-agent systems
- Autonomous agent networks
- AI-to-AI security operations
- Novel attack vectors

**Mitigation:** Built-in evolution mechanism. Regular version updates. Community-driven practice additions.

### 6. Certification Authority Gap
Who certifies HAIAMM assessments? Without established certification bodies, "HAIAMM Level 2 Certified" lacks the weight of "ISO 27001 Certified."

**Mitigation:** Establish certification program early. Partner with recognized security organizations. Build assessor training program.

---

## Competitive Advantages

### vs. Generic Frameworks (NIST, ISO)
- More specific to AI security operations
- Actionable implementation guidance (First 30 Days)
- Interactive tooling (Verifhai)
- Measurable outcomes, not just controls

### vs. Risk Lists (OWASP Top 10, MITRE ATLAS)
- Full maturity model, not just risk identification
- Progress tracking through levels
- Implementation workflows
- Organizational assessment, not just technical risks

### vs. Software Security Models (SAMM)
- Designed for AI-operated security era
- Addresses AI agent effectiveness
- AI-specific practices and assessment criteria
- Complementary for organizations with both human and AI security operations

---

## Strategic Recommendations

### For HAIAMM Success

1. **Build adoption momentum**
   - Early adopter program with published case studies
   - Free self-assessment drives awareness
   - Community contributions validate and improve

2. **Establish credibility**
   - Validation studies with real metrics
   - Academic partnerships for research
   - Regulatory alignment (EU AI Act mapping)

3. **Integrate, don't compete**
   - Clear mapping to existing frameworks
   - Position as "AI security layer" on top of existing programs
   - Tooling that exports to compliance formats

4. **Evolve with the field**
   - Regular version updates (annual minimum)
   - Community RFC process for new practices
   - Backwards compatibility for certified organizations

---

## Conclusion

HAIAMM is solving a real problem that will only grow as AI agents increasingly run security operations. The framework is well-designed with practical structure, OWASP alignment, measurable outcomes, and interactive tooling.

**Compared to alternatives:**
- More practical than NIST AI RMF (which is high-level guidance)
- More comprehensive than OWASP Top 10 lists (which are just risk catalogs)
- More AI-specific than SAMM (which is general software security)
- Less established than ISO standards (which have decades of adoption)

**The challenge is adoption.** Success depends on building the ecosystem: early adopters, case studies, certification authority, community validation, and regulatory recognition.

**Bottom line:** The concept is sound, the timing is right, and the execution in v2.2 is solid. HAIAMM has the potential to become the standard for AI-operated security assurance—but potential must be converted to adoption.

---

## Document Information

| Field | Value |
|-------|-------|
| Document | Competitive Analysis |
| HAIAMM Version | 2.2 |
| Last Updated | January 2026 |

---

**Related Documents:**
- [Quick Start Guide](handbook/01-QUICK-START.md)
- [OWASP Top 10 Agentic Risks](handbook/04-TOP10-AGENTIC-RISKS.md)
- [OWASP Top 10 LLM Risks](handbook/03-TOP10-LLM-RISKS.md)
- [HAIAMM + Verifhai Pitch Deck](HAIAMM-VERIFHAI-PITCH-DECK.md)
