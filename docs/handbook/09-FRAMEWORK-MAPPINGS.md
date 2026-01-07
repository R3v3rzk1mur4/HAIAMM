![HAIAMM Logo](../images/HAIAMM_logo.png)

# Appendix: Framework Mappings

**HAIAMM alignment with BSIMM, OpenSAMM, NIST AI RMF, and NIST CSF 2.0**

[Back to Index](00-INDEX.md) | [Competitive Analysis](../HAIAMM-COMPETITIVE-ANALYSIS.md)

---

> **Note on Framework Mappings**
>
> These mappings show how HAIAMM practices align with established security frameworks. Mappings are approximate—each framework has unique scope and terminology. Use these to demonstrate compliance overlap and identify complementary controls.

---

## Overview

HAIAMM is designed to complement, not replace, existing security frameworks. This appendix provides detailed mappings to help organizations:

1. **Demonstrate compliance** - Show how HAIAMM addresses requirements from other frameworks
2. **Identify gaps** - Find where HAIAMM provides AI-specific coverage others lack
3. **Integrate programs** - Align HAIAMM with existing security maturity initiatives
4. **Communicate value** - Translate HAIAMM practices to familiar framework terminology

---

## Framework Comparison Summary

| Framework | Focus | Structure | AI-Specific |
|-----------|-------|-----------|-------------|
| **HAIAMM** | AI-operated security | 4 functions, 12 practices, 6 domains | ✅ Yes |
| **BSIMM** | Software security (descriptive) | 4 domains, 12 practices, 128 activities | ❌ No |
| **OpenSAMM v1.0** | Software security (prescriptive) | 4 functions, 12 practices | ❌ No |
| **NIST AI RMF** | AI risk management | 4 functions, multiple categories | ✅ Yes |
| **NIST CSF 2.0** | Cybersecurity | 6 functions, 22 categories | ❌ No |

---

## HAIAMM × BSIMM Mapping

### Overview

BSIMM (Building Security In Maturity Model) is a descriptive model based on observations from 130+ organizations. It measures what organizations actually do, not what they should do.

**Key Difference:** BSIMM describes software security practices; HAIAMM prescribes AI-operated security practices.

### Domain Alignment

| HAIAMM Function | BSIMM Domain |
|-----------------|--------------|
| Governance | Governance |
| Building | Intelligence + SSDL Touchpoints |
| Verification | SSDL Touchpoints |
| Operations | Deployment |

### Practice-to-Practice Mapping

| HAIAMM Practice | BSIMM Practice | Alignment | Notes |
|-----------------|----------------|-----------|-------|
| **SM** Strategy & Metrics | SM (Strategy & Metrics) | 🟢 Strong | Nearly identical scope |
| **PC** Policy & Compliance | CP (Compliance & Policy) | 🟢 Strong | HAIAMM adds AI regulations |
| **EG** Education & Guidance | T (Training) | 🟢 Strong | HAIAMM adds AI-specific training |
| **TA** Threat Assessment | AM (Attack Models) | 🟡 Moderate | HAIAMM includes AI threat modeling |
| **SR** Security Requirements | SR (Standards & Requirements) | 🟢 Strong | HAIAMM adds AI boundaries (CAN/CANNOT/MUST) |
| **SA** Secure Architecture | SFD (Security Features & Design) | 🟡 Moderate | HAIAMM adds agent orchestration |
| **DR** Design Review | AA (Architecture Analysis) | 🟢 Strong | Similar scope |
| **IR** Implementation Review | CR (Code Review) | 🟢 Strong | HAIAMM adds AI-specific patterns |
| **ST** Security Testing | ST (Security Testing) | 🟢 Strong | HAIAMM adds prompt injection, red team |
| **IM** Issue Management | CMVM (Config & Vuln Management) | 🟡 Moderate | HAIAMM adds AI incident categories |
| **EH** Environment Hardening | SE (Software Environment) | 🟡 Moderate | HAIAMM adds agent sandboxing |
| **ML** Monitoring & Logging | CMVM + PT | 🟡 Moderate | HAIAMM adds behavioral anomaly detection |

### BSIMM Activities → HAIAMM Coverage

#### Governance Domain

| BSIMM Activity | HAIAMM Practice | Coverage |
|----------------|-----------------|----------|
| SM1.1 Publish process | SM L1 | ✅ Covered |
| SM1.4 Identify gate locations | SM L2 | ✅ Covered |
| SM2.1 Publish data internally | SM L2 | ✅ Covered |
| SM2.2 Enforce gates | SM L3 | ✅ Covered |
| CP1.1 Unify regulatory pressures | PC L1 | ✅ Covered |
| CP1.2 Create policy | PC L1 | ✅ Covered |
| CP2.1 Implement controls | PC L2 | ✅ Covered |
| T1.1 Conduct awareness training | EG L1 | ✅ Covered |
| T1.7 Deliver on-demand training | EG L2 | ✅ Covered |
| T2.5 Host security events | EG L3 | ✅ Covered |

#### Intelligence Domain

| BSIMM Activity | HAIAMM Practice | Coverage |
|----------------|-----------------|----------|
| AM1.2 Gather attack intelligence | TA L1 | ✅ Covered |
| AM1.5 Create technology-specific patterns | TA L2 | ✅ Covered + AI patterns |
| AM2.1 Have attack stories | TA L2 | ✅ Covered |
| SFD1.1 Build security features | SA L1 | ✅ Covered |
| SFD2.1 Leverage secure design patterns | SA L2 | ✅ Covered + AI patterns |
| SR1.1 Create security standards | SR L1 | ✅ Covered |
| SR1.2 Create security portal | SR L2 | ✅ Covered |

#### SSDL Touchpoints Domain

| BSIMM Activity | HAIAMM Practice | Coverage |
|----------------|-----------------|----------|
| AA1.1 Standardize descriptions | DR L1 | ✅ Covered |
| AA1.2 Perform design review | DR L1 | ✅ Covered |
| AA2.1 Define and use AA process | DR L2 | ✅ Covered |
| CR1.2 Use automated tools | IR L1 | ✅ Covered |
| CR1.4 Make review mandatory | IR L2 | ✅ Covered |
| CR2.6 Use custom rules | IR L2 | ✅ Covered + AI rules |
| ST1.1 Integrate in QA | ST L1 | ✅ Covered |
| ST1.3 Drive tests with design review | ST L2 | ✅ Covered |
| ST2.1 Include abuse cases | ST L2 | ✅ Covered + AI abuse |

#### Deployment Domain

| BSIMM Activity | HAIAMM Practice | Coverage |
|----------------|-----------------|----------|
| CMVM1.1 Emergency response | IM L1 | ✅ Covered |
| CMVM1.2 Track bugs in operations | IM L1 | ✅ Covered |
| CMVM2.1 Have incident response | IM L2 | ✅ Covered |
| SE1.1 OS patching | EH L1 | ✅ Covered |
| SE1.2 Network monitoring | ML L1 | ✅ Covered |
| SE2.2 Application monitoring | ML L2 | ✅ Covered |
| PT1.1 Use external pen testers | ST L2 | ✅ Covered |
| PT1.2 Feed to defect tracking | IM L2 | ✅ Covered |

### HAIAMM Additions Beyond BSIMM

| HAIAMM Capability | BSIMM Gap |
|-------------------|-----------|
| AI agent goal integrity | Not addressed |
| Prompt injection testing | Not addressed |
| Agent permission boundaries | Not addressed |
| AI behavioral anomaly detection | Not addressed |
| Multi-agent coordination security | Not addressed |
| AI supply chain (model provenance) | Partially addressed |
| Human-AI trust exploitation | Not addressed |

---

## HAIAMM × OpenSAMM v1.0 Mapping

### Overview

OpenSAMM (Software Assurance Maturity Model) v1.0 is a prescriptive framework for software security programs. HAIAMM was designed with awareness of OpenSAMM's structure.

**Key Difference:** OpenSAMM addresses human software development; HAIAMM addresses AI-operated security.

### Function Alignment

| HAIAMM Function | OpenSAMM v1.0 Function |
|-----------------|------------------------|
| Governance | Governance |
| Building | Construction |
| Verification | Verification |
| Operations | Deployment |

### Practice-to-Practice Mapping

| HAIAMM Practice | OpenSAMM v1.0 Practice | Alignment |
|-----------------|------------------------|-----------|
| **SM** Strategy & Metrics | Strategy & Metrics | 🟢 Direct |
| **PC** Policy & Compliance | Policy & Compliance | 🟢 Direct |
| **EG** Education & Guidance | Education & Guidance | 🟢 Direct |
| **TA** Threat Assessment | Threat Assessment | 🟢 Direct |
| **SR** Security Requirements | Security Requirements | 🟢 Direct |
| **SA** Secure Architecture | Secure Architecture | 🟢 Direct |
| **DR** Design Review | Design Review | 🟢 Direct |
| **IR** Implementation Review | Code Review | 🟢 Direct (renamed) |
| **ST** Security Testing | Security Testing | 🟢 Direct |
| **IM** Issue Management | Vulnerability Management | 🟢 Direct (renamed) |
| **EH** Environment Hardening | Environment Hardening | 🟢 Direct |
| **ML** Monitoring & Logging | Operational Enablement | 🟡 Extended |

### Maturity Level Alignment

| Level | HAIAMM | OpenSAMM v1.0 |
|-------|--------|---------------|
| 1 | Foundation | Initial understanding, ad-hoc |
| 2 | Structured | Documented, consistent process |
| 3 | Optimized | Measured, continuous improvement |

### Key Differences

| Aspect | OpenSAMM v1.0 | HAIAMM |
|--------|---------------|--------|
| **Target** | Human development teams | AI agents doing security |
| **Domains** | Single (software) | Six (software, infra, endpoints, data, processes, vendors) |
| **Risk Focus** | Application vulnerabilities | AI-specific risks (ASI01-10, LLM01-10) |
| **Metrics** | Development process metrics | AI effectiveness metrics |
| **Architecture** | Application security patterns | Agent orchestration patterns |

---

## HAIAMM × NIST AI RMF Mapping

### Overview

NIST AI RMF (AI Risk Management Framework) provides guidance for managing AI system risks. It focuses on trustworthy AI characteristics.

**Key Difference:** NIST AI RMF asks "Is your AI system secure?" HAIAMM asks "Is your AI system doing security well?"

### Function Alignment

| NIST AI RMF Function | HAIAMM Practices | Relationship |
|---------------------|------------------|--------------|
| **GOVERN** | SM, PC, EG | Governance alignment |
| **MAP** | TA, SR | Risk identification |
| **MEASURE** | DR, IR, ST | Assessment and testing |
| **MANAGE** | IM, EH, ML | Operational management |

### Detailed Category Mapping

#### GOVERN Function → HAIAMM

| NIST AI RMF Category | HAIAMM Practice | Alignment |
|---------------------|-----------------|-----------|
| GOVERN 1 (Policies & Processes) | PC L1-L3 | 🟢 Strong |
| GOVERN 2 (Accountability) | SM L2-L3 | 🟢 Strong |
| GOVERN 3 (Workforce) | EG L1-L3 | 🟡 Moderate |
| GOVERN 4 (Culture) | EG L2-L3 | 🟡 Moderate |
| GOVERN 5 (Stakeholders) | SM L2 | 🟡 Moderate |
| GOVERN 6 (Third-party) | SA L2 (Vendors domain) | 🟢 Strong |

#### MAP Function → HAIAMM

| NIST AI RMF Category | HAIAMM Practice | Alignment |
|---------------------|-----------------|-----------|
| MAP 1 (Context) | TA L1 | 🟢 Strong |
| MAP 2 (Categorization) | TA L1-L2 | 🟢 Strong |
| MAP 3 (Capabilities) | SR L1 | 🟡 Moderate |
| MAP 4 (Risk Mapping) | TA L2 | 🟢 Strong |
| MAP 5 (Impact) | TA L2-L3 | 🟢 Strong |

#### MEASURE Function → HAIAMM

| NIST AI RMF Category | HAIAMM Practice | Alignment |
|---------------------|-----------------|-----------|
| MEASURE 1 (Metrics) | SM L2-L3 | 🟢 Strong |
| MEASURE 2 (Testing) | ST L1-L3 | 🟢 Strong |
| MEASURE 3 (Tracking) | ML L2-L3 | 🟢 Strong |
| MEASURE 4 (Feedback) | IM L2-L3 | 🟡 Moderate |

#### MANAGE Function → HAIAMM

| NIST AI RMF Category | HAIAMM Practice | Alignment |
|---------------------|-----------------|-----------|
| MANAGE 1 (Prioritize) | IM L1-L2 | 🟢 Strong |
| MANAGE 2 (Response) | IM L2-L3 | 🟢 Strong |
| MANAGE 3 (Third-party) | SA (Vendors) L2 | 🟢 Strong |
| MANAGE 4 (Documentation) | SM L2, IM L2 | 🟢 Strong |

### HAIAMM Additions Beyond NIST AI RMF

| HAIAMM Capability | NIST AI RMF Gap |
|-------------------|-----------------|
| AI security testing specifics | General guidance only |
| Agent architecture patterns | Not addressed |
| Implementation review details | Not addressed |
| Environment hardening specifics | General guidance only |
| OWASP risk mapping | Not addressed |
| Measurable security outcomes | Limited metrics guidance |

---

## HAIAMM × NIST CSF 2.0 Mapping

### Overview

NIST CSF 2.0 (Cybersecurity Framework) is the leading cybersecurity framework. Version 2.0 added a GOVERN function.

**Key Difference:** NIST CSF covers all cybersecurity; HAIAMM focuses on AI security operations.

### Function Alignment

| NIST CSF 2.0 Function | HAIAMM Practices | Relationship |
|----------------------|------------------|--------------|
| **GOVERN (GV)** | SM, PC, EG | Direct governance alignment |
| **IDENTIFY (ID)** | TA, SR | Risk identification |
| **PROTECT (PR)** | SA, DR, IR, EH | Preventive controls |
| **DETECT (DE)** | ST, ML | Detection capabilities |
| **RESPOND (RS)** | IM | Incident response |
| **RECOVER (RC)** | IM | Recovery activities |

### Category-to-Practice Mapping

#### GOVERN Function

| CSF Category | HAIAMM Practice | Coverage |
|--------------|-----------------|----------|
| GV.OC (Org Context) | SM L1 | ✅ Covered |
| GV.RM (Risk Mgmt Strategy) | SM L1-L2 | ✅ Covered |
| GV.RR (Roles & Responsibilities) | SM L2 | ✅ Covered |
| GV.PO (Policy) | PC L1-L3 | ✅ Covered |
| GV.OV (Oversight) | SM L2-L3 | ✅ Covered |
| GV.SC (Supply Chain) | SA (Vendors) L1-L3 | ✅ Covered |

#### IDENTIFY Function

| CSF Category | HAIAMM Practice | Coverage |
|--------------|-----------------|----------|
| ID.AM (Asset Mgmt) | SM L1 | ✅ Covered (AI inventory) |
| ID.RA (Risk Assessment) | TA L1-L3 | ✅ Covered |
| ID.IM (Improvement) | SM L3 | ✅ Covered |

#### PROTECT Function

| CSF Category | HAIAMM Practice | Coverage |
|--------------|-----------------|----------|
| PR.AA (Access Control) | SR L1, EH L1 | ✅ Covered |
| PR.AT (Training) | EG L1-L3 | ✅ Covered |
| PR.DS (Data Security) | SA (Data) L1-L3 | ✅ Covered |
| PR.PS (Platform Security) | EH L1-L3 | ✅ Covered |
| PR.IR (Resilience) | SA L2, EH L2 | ✅ Covered |

#### DETECT Function

| CSF Category | HAIAMM Practice | Coverage |
|--------------|-----------------|----------|
| DE.CM (Continuous Monitoring) | ML L1-L3 | ✅ Covered |
| DE.AE (Adverse Event Analysis) | ML L2-L3 | ✅ Covered |

#### RESPOND Function

| CSF Category | HAIAMM Practice | Coverage |
|--------------|-----------------|----------|
| RS.MA (Incident Mgmt) | IM L1-L3 | ✅ Covered |
| RS.AN (Analysis) | IM L2 | ✅ Covered |
| RS.CO (Communication) | IM L2-L3 | ✅ Covered |
| RS.MI (Mitigation) | IM L2-L3 | ✅ Covered |

#### RECOVER Function

| CSF Category | HAIAMM Practice | Coverage |
|--------------|-----------------|----------|
| RC.RP (Recovery Plan) | IM L2 | ✅ Covered |
| RC.CO (Communication) | IM L2-L3 | ✅ Covered |

### HAIAMM Additions Beyond NIST CSF

| HAIAMM Capability | NIST CSF Gap |
|-------------------|--------------|
| AI-specific threat modeling | General risk assessment |
| Prompt injection controls | Not addressed |
| Agent behavioral monitoring | General monitoring |
| AI architecture review | General design review |
| OWASP AI risk alignment | Not addressed |

---

## Consolidated Mapping Matrix

### HAIAMM Practices → All Frameworks

| HAIAMM | BSIMM | OpenSAMM v1.0 | NIST AI RMF | NIST CSF 2.0 |
|--------|-------|---------------|-------------|--------------|
| **SM** | SM | Strategy & Metrics | GOVERN 1-2, MEASURE 1 | GV.RM, GV.OV |
| **PC** | CP | Policy & Compliance | GOVERN 1 | GV.PO |
| **EG** | T | Education & Guidance | GOVERN 3-4 | PR.AT |
| **TA** | AM | Threat Assessment | MAP 1-5 | ID.RA |
| **SR** | SR | Security Requirements | MAP 3 | PR.AA |
| **SA** | SFD | Secure Architecture | GOVERN 6, MANAGE 3 | GV.SC, PR.PS |
| **DR** | AA | Design Review | MEASURE 2 | PR.IR |
| **IR** | CR | Code Review | MEASURE 2 | PR.PS |
| **ST** | ST + PT | Security Testing | MEASURE 2-3 | DE.CM |
| **IM** | CMVM | Vulnerability Mgmt | MANAGE 1-2, 4 | RS.*, RC.* |
| **EH** | SE | Environment Hardening | MANAGE 1 | PR.PS, PR.IR |
| **ML** | CMVM | Operational Enablement | MEASURE 3, MANAGE 4 | DE.CM, DE.AE |

---

## Gap Analysis

### What HAIAMM Adds

| Capability | Traditional Frameworks | HAIAMM |
|------------|----------------------|--------|
| AI agent goal integrity | ❌ Not addressed | ✅ ASI01, TA, SR |
| Prompt injection defense | ❌ Not addressed | ✅ LLM01, ST, EH |
| Agent permission boundaries | ❌ Not addressed | ✅ SR (CAN/CANNOT/MUST) |
| Multi-agent coordination | ❌ Not addressed | ✅ ASI07, SA, ML |
| AI behavioral anomaly detection | ❌ Limited | ✅ ML L2-L3 |
| Rogue agent detection | ❌ Not addressed | ✅ ASI10, ML, IM |
| AI supply chain (models) | ⚠️ Partial | ✅ Vendors domain |
| Measurable AI outcomes | ❌ Limited | ✅ Full methodology |

### Framework Selection Guide

| If you need... | Use HAIAMM + |
|----------------|--------------|
| Software security baseline | BSIMM or OpenSAMM |
| Enterprise cybersecurity | NIST CSF 2.0 |
| AI governance compliance | NIST AI RMF |
| Regulatory compliance (EU AI Act) | NIST AI RMF + HAIAMM |
| Insurance requirements | NIST CSF 2.0 + HAIAMM |

---

## Implementation Recommendations

### Organizations Using BSIMM

1. Map existing BSIMM activities to HAIAMM practices
2. Add HAIAMM's AI-specific activities to your SSI
3. Use HAIAMM domains to extend coverage to AI systems
4. Report HAIAMM maturity alongside BSIMM scores

### Organizations Using OpenSAMM

1. HAIAMM practices align directly—extend existing assessments
2. Add HAIAMM's 6 domains for comprehensive AI coverage
3. Use HAIAMM's OWASP mappings for AI risk prioritization
4. Leverage HAIAMM's measurement methodology

### Organizations Using NIST AI RMF

1. Use HAIAMM for implementation details NIST AI RMF lacks
2. Map HAIAMM outcomes to NIST AI RMF subcategories
3. Use HAIAMM practices for operational AI security
4. HAIAMM provides the "how" to NIST AI RMF's "what"

### Organizations Using NIST CSF

1. Add HAIAMM for AI-specific security controls
2. Map HAIAMM to CSF Profiles for AI systems
3. Use HAIAMM maturity levels for CSF Implementation Tiers
4. Extend CSF categories with HAIAMM AI practices

---

## Document Information

| Field | Value |
|-------|-------|
| Document | Framework Mappings (Appendix) |
| HAIAMM Version | 2.2 |
| Frameworks Mapped | BSIMM, OpenSAMM v1.0, NIST AI RMF, NIST CSF 2.0 |
| Last Updated | January 2026 |

---

**Sources:**
- BSIMM 15 (2025) - bsimm.com
- OpenSAMM v1.0 - opensamm.org
- NIST AI RMF 1.0 (2023) - NIST AI 100-1
- NIST CSF 2.0 (2024) - NIST CSWP 29

---

**Related Documents:**
- [Competitive Analysis](../HAIAMM-COMPETITIVE-ANALYSIS.md)
- [Risk-Practice Matrix](05-RISK-PRACTICE-MATRIX.md)
- [Assessment Checklist](07-ASSESSMENT-CHECKLIST.md)

[Back to Index](00-INDEX.md)
