# HAIAMM Risk-Practice Matrix

**Which practices address which risks**

[Back to Index](00-INDEX.md) | [Agentic Risks](04-TOP10-AGENTIC-RISKS.md) | [LLM Risks](03-TOP10-LLM-RISKS.md)

---

## How to Use This Matrix

This matrix shows which HAIAMM practices address each security risk. Use it to:

1. **Prioritize practices** based on your risk profile
2. **Identify gaps** in your current security posture
3. **Plan assessments** for specific risk areas
4. **Allocate resources** to highest-impact practices

**Legend:**
- **P** = Primary practice (critical for addressing this risk)
- **S** = Secondary practice (supporting role)
- **-** = Not directly relevant

---

## OWASP Top 10 for Agentic Applications × HAIAMM Practices

| Risk | SM | PC | EG | TA | SR | SA | DR | IR | ST | IM | EH | ML |
|------|----|----|----|----|----|----|----|----|----|----|----|----|
| **ASI01** Agent Goal Hijack | S | S | - | **P** | **P** | S | S | - | **P** | S | S | **P** |
| **ASI02** Tool Misuse | S | **P** | - | S | S | **P** | S | - | S | S | S | **P** |
| **ASI03** Identity Abuse | S | S | - | S | **P** | S | - | - | S | S | **P** | **P** |
| **ASI04** Supply Chain | S | S | - | **P** | S | **P** | S | S | S | **P** | S | S |
| **ASI05** Code Execution | - | S | - | S | **P** | S | S | **P** | **P** | S | **P** | S |
| **ASI06** Memory Poisoning | S | - | - | S | S | S | **P** | - | **P** | S | **P** | S |
| **ASI07** Inter-Agent Comm | S | S | - | S | **P** | **P** | S | - | S | S | S | **P** |
| **ASI08** Cascading Failures | S | S | - | S | S | **P** | S | - | S | **P** | S | **P** |
| **ASI09** Trust Exploitation | S | **P** | **P** | S | S | S | S | - | S | S | - | **P** |
| **ASI10** Rogue Agents | S | S | - | **P** | S | S | S | - | S | **P** | S | **P** |

### Agentic Risk Priority by Practice

| Practice | Primary For | Secondary For | Priority Score |
|----------|-------------|---------------|----------------|
| **ML** Monitoring & Logging | 5 risks | 5 risks | **High** |
| **ST** Security Testing | 3 risks | 5 risks | **High** |
| **SR** Security Requirements | 3 risks | 5 risks | **High** |
| **TA** Threat Assessment | 3 risks | 5 risks | **High** |
| **SA** Secure Architecture | 3 risks | 5 risks | **High** |
| **EH** Environment Hardening | 3 risks | 5 risks | **High** |
| **PC** Policy & Compliance | 2 risks | 6 risks | Medium |
| **IM** Issue Management | 2 risks | 6 risks | Medium |
| **DR** Design Review | 1 risk | 5 risks | Medium |
| **IR** Implementation Review | 1 risk | 2 risks | Low |
| **EG** Education & Guidance | 1 risk | 1 risk | Low |
| **SM** Strategy & Metrics | 0 risks | 9 risks | Supporting |

---

## OWASP Top 10 for LLM Applications × HAIAMM Practices

| Risk | SM | PC | EG | TA | SR | SA | DR | IR | ST | IM | EH | ML |
|------|----|----|----|----|----|----|----|----|----|----|----|----|
| **LLM01** Prompt Injection | S | S | - | S | **P** | S | S | S | **P** | S | **P** | S |
| **LLM02** Info Disclosure | S | **P** | - | S | S | S | **P** | S | S | S | S | **P** |
| **LLM03** Supply Chain | S | S | - | S | S | **P** | S | S | S | **P** | **P** | S |
| **LLM04** Data Poisoning | S | S | - | **P** | S | S | **P** | - | **P** | S | S | S |
| **LLM05** Output Handling | - | S | - | S | **P** | S | S | **P** | **P** | S | S | S |
| **LLM06** Excessive Agency | S | **P** | S | S | S | **P** | S | - | S | S | S | **P** |
| **LLM07** Prompt Leakage | S | S | - | S | S | S | S | - | **P** | S | **P** | **P** |
| **LLM08** Vector Weaknesses | S | S | - | S | S | **P** | S | - | **P** | S | **P** | S |
| **LLM09** Misinformation | S | S | S | S | S | S | **P** | - | **P** | S | S | **P** |
| **LLM10** Unbounded Consumption | S | S | - | S | **P** | S | S | - | S | S | **P** | **P** |

### LLM Risk Priority by Practice

| Practice | Primary For | Secondary For | Priority Score |
|----------|-------------|---------------|----------------|
| **ST** Security Testing | 5 risks | 5 risks | **High** |
| **EH** Environment Hardening | 4 risks | 4 risks | **High** |
| **ML** Monitoring & Logging | 4 risks | 6 risks | **High** |
| **SR** Security Requirements | 3 risks | 5 risks | **High** |
| **SA** Secure Architecture | 3 risks | 5 risks | **High** |
| **DR** Design Review | 3 risks | 5 risks | **High** |
| **PC** Policy & Compliance | 2 risks | 7 risks | Medium |
| **IM** Issue Management | 1 risk | 8 risks | Medium |
| **TA** Threat Assessment | 1 risk | 7 risks | Medium |
| **IR** Implementation Review | 1 risk | 3 risks | Low |
| **EG** Education & Guidance | 0 risks | 2 risks | Low |
| **SM** Strategy & Metrics | 0 risks | 9 risks | Supporting |

---

## Combined Risk Coverage Matrix

### High-Priority Practices (Address 6+ Risks as Primary)

| Practice | Total Primary | Agentic Primary | LLM Primary |
|----------|---------------|-----------------|-------------|
| **ST** Security Testing | 8 | 3 | 5 |
| **ML** Monitoring & Logging | 9 | 5 | 4 |
| **EH** Environment Hardening | 7 | 3 | 4 |
| **SR** Security Requirements | 6 | 3 | 3 |
| **SA** Secure Architecture | 6 | 3 | 3 |

### Recommended Assessment Order

Based on risk coverage, assess practices in this order:

1. **Tier 1: Critical Coverage**
   - ST (Security Testing) - Addresses 8 primary risks
   - ML (Monitoring & Logging) - Addresses 9 primary risks
   - EH (Environment Hardening) - Addresses 7 primary risks

2. **Tier 2: High Coverage**
   - SR (Security Requirements) - Addresses 6 primary risks
   - SA (Secure Architecture) - Addresses 6 primary risks
   - TA (Threat Assessment) - Addresses 4 primary risks

3. **Tier 3: Supporting Coverage**
   - PC (Policy & Compliance)
   - DR (Design Review)
   - IM (Issue Management)

4. **Tier 4: Foundational**
   - SM (Strategy & Metrics)
   - EG (Education & Guidance)
   - IR (Implementation Review)

---

## Risk-to-Practice Quick Reference

### By Risk: What Practices to Implement

**If you're concerned about Prompt Injection (LLM01):**
- Primary: SR, ST, EH
- Focus: Input validation, injection testing, environment controls

**If you're concerned about Agent Goal Hijack (ASI01):**
- Primary: TA, SR, ST, ML
- Focus: Threat modeling, goal integrity requirements, behavioral monitoring

**If you're concerned about Tool Misuse (ASI02):**
- Primary: SA, PC, ML
- Focus: Tool access architecture, usage policies, invocation monitoring

**If you're concerned about Data Poisoning (LLM04):**
- Primary: TA, DR, ST
- Focus: Poisoning threat assessment, data review, integrity testing

**If you're concerned about Rogue Agents (ASI10):**
- Primary: TA, ML, IM
- Focus: Rogue threat modeling, behavioral detection, incident response

---

## Domain Focus by Risk

### Software Domain Risks
Most risks require Software domain practices:
- All LLM risks touch Software
- 8/10 Agentic risks are Software-primary

### Infrastructure Domain Risks
Critical for:
- ASI03 (Identity Abuse)
- ASI05 (Code Execution)
- ASI07 (Inter-Agent Communication)
- ASI08 (Cascading Failures)
- LLM10 (Unbounded Consumption)

### Data Domain Risks
Critical for:
- ASI06 (Memory Poisoning)
- LLM02 (Information Disclosure)
- LLM04 (Data Poisoning)
- LLM08 (Vector Weaknesses)

### Processes Domain Risks
Critical for:
- ASI08 (Cascading Failures)
- ASI09 (Trust Exploitation)
- ASI10 (Rogue Agents)
- LLM06 (Excessive Agency)

### Vendors Domain Risks
Critical for:
- ASI04 (Supply Chain)
- LLM03 (Supply Chain)

### Endpoints Domain Risks
Critical for:
- ASI02 (Tool Misuse)
- ASI09 (Trust Exploitation)
- LLM01 (Prompt Injection)
- LLM07 (Prompt Leakage)

---

## Using This Matrix for Gap Analysis

### Step 1: Identify Your Primary Risks

Select the top 5 risks most relevant to your environment:
- [ ] Risk 1: _______________
- [ ] Risk 2: _______________
- [ ] Risk 3: _______________
- [ ] Risk 4: _______________
- [ ] Risk 5: _______________

### Step 2: Map Primary Practices

For each risk, list the primary practices:
| Risk | Primary Practices |
|------|-------------------|
| | |
| | |
| | |

### Step 3: Identify Coverage Gaps

Check which practices appear most frequently:
| Practice | Count | Current Maturity | Gap |
|----------|-------|------------------|-----|
| | | | |
| | | | |

### Step 4: Prioritize Assessment

Focus on practices with:
1. Highest risk coverage
2. Lowest current maturity
3. Largest gap to target

---

## Document Information

| Field | Value |
|-------|-------|
| Document | Risk-Practice Matrix |
| HAIAMM Version | 2.2 |
| Last Updated | January 2026 |

---

**Related Documents:**
- [Top 10 Agentic Risks](04-TOP10-AGENTIC-RISKS.md)
- [Top 10 LLM Risks](03-TOP10-LLM-RISKS.md)
- [Assessment Checklist](07-ASSESSMENT-CHECKLIST.md)
- [Maturity Roadmap](06-MATURITY-ROADMAP.md)

[Back to Index](00-INDEX.md)
