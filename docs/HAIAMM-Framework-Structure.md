# HAIAMM Framework Structure
## Canonical Reference Document

**Version:** 1.0
**Last Updated:** 2025-12-28
**Purpose:** Authoritative source for HAIAMM structure, terminology, and organization

---

## Official Name

**Human Assisted Intelligence Assurance Maturity Model (HAIAMM)**

- ✅ "Human Assisted Intelligence" (no hyphen between Assisted and Intelligence)
- ✅ Abbreviated as "HAI" when referring to systems
- ✅ Full name: HAIAMM (not HAI-AMM)

---

## Framework Purpose

HAIAMM provides a maturity framework for organizations designing and implementing artificial intelligence solutions to:

- **Automate workflows** - AI systems handling business processes
- **Conduct tasks and analysis** - Security testing, code analysis for vulnerabilities, data processing
- **Provide customer service automation** - Chatbots, virtual assistants, automated support
- **Assist human decision-making** - Recommendation systems, decision support tools

**Core Focus:** Foundational practices to ensure **trust, safety, and security** of Human Assisted Intelligence solutions.

---

## Framework Foundation

**Based on:** OWASP OpenSAMM v1.0 with extensions from Pravir Chandra's "Future Directions" (3/27/2015)

**Key Innovations:**
1. **Multi-Domain Architecture** - 6 domains covering complete technology stack
2. **HAI-Specific Practices** - Adapted for AI/ML systems and human oversight
3. **Maturity-Based Assessment** - Progressive capability building (Level 0 → 3)

---

## 6 Security Domains

**Domain Order (Canonical):**

1. **Software** - AI applications, models, code, development pipelines
2. **Data** - Training data, operational data, privacy, quality, governance
3. **Infrastructure** - Cloud/on-premise platforms, deployment environments, scaling
4. **Vendors** - Third-party AI services, supply chain, vendor risk management
5. **Processes** - Business workflows, governance procedures, compliance, automation
6. **Endpoints** - User interfaces, APIs, integration points, access controls

**Coverage:** Each practice is assessed across all 6 domains = 72 practice-domain combinations

---

## 4 Business Functions

Organizations building and deploying HAI solutions perform 4 business functions:

### 1. Governance
**Purpose:** How you govern, measure, and educate around HAI

**Practices:**
- Strategy & Metrics (SM)
- Policy & Compliance (PC)
- Education & Guidance (EG)

---

### 2. Building
**Purpose:** How you design and build HAI systems responsibly

**Practices:**
- Threat Assessment (TA)
- Security Requirements (SR)
- Secure Architecture (SA)

---

### 3. Verification
**Purpose:** How you verify HAI systems work correctly and safely

**Practices:**
- Design Review (DR)
- Implementation Review (IR)
- Security Testing (ST)

---

### 4. Operations
**Purpose:** How you operate and maintain HAI systems in production

**Practices:**
- Environment Hardening (EH)
- Issue Management (IM)
- Monitoring & Logging (ML)

---

## 12 Security Practices (Canonical List)

**Practice codes and full names:**

| Code | Practice Name | Business Function | Focus |
|------|--------------|-------------------|-------|
| **SM** | Strategy & Metrics | Governance | Strategic roadmap, metrics, ROI measurement |
| **PC** | Policy & Compliance | Governance | Policies, standards, regulatory compliance |
| **EG** | Education & Guidance | Governance | Training, awareness, secure development guidance |
| **TA** | Threat Assessment | Building | Threat identification, risk assessment, attack modeling |
| **SR** | Security Requirements | Building | Functional/non-functional requirements, acceptance criteria |
| **SA** | Secure Architecture | Building | Architecture design, technology selection, security controls |
| **DR** | Design Review | Verification | Design review before implementation, architectural validation |
| **IR** | Implementation Review | Verification | Code review, configuration review, peer review |
| **ST** | Security Testing | Verification | Testing for vulnerabilities, adversarial robustness, compliance |
| **EH** | Environment Hardening | Operations | Runtime security, access controls, encryption, baselines |
| **IM** | Issue Management | Operations | Vulnerability tracking, remediation, defect management |
| **ML** | Monitoring & Logging | Operations | Security logging, monitoring, alerting, audit trails |

**Total:** 12 practices

---

## Practice-Domain Matrix

**Complete Coverage:** 12 practices × 6 domains = **72 combinations**

**Example:**
- TA-Software: Threat Assessment for Software domain
- SR-Data: Security Requirements for Data domain
- ML-Endpoints: Monitoring & Logging for Endpoints domain

**Matrix Visualization:**

```
              Software  Data  Infrastructure  Vendors  Processes  Endpoints
SM                ✓       ✓         ✓           ✓         ✓          ✓
PC                ✓       ✓         ✓           ✓         ✓          ✓
EG                ✓       ✓         ✓           ✓         ✓          ✓
TA                ✓       ✓         ✓           ✓         ✓          ✓
SR                ✓       ✓         ✓           ✓         ✓          ✓
SA                ✓       ✓         ✓           ✓         ✓          ✓
DR                ✓       ✓         ✓           ✓         ✓          ✓
IR                ✓       ✓         ✓           ✓         ✓          ✓
ST                ✓       ✓         ✓           ✓         ✓          ✓
EH                ✓       ✓         ✓           ✓         ✓          ✓
IM                ✓       ✓         ✓           ✓         ✓          ✓
ML                ✓       ✓         ✓           ✓         ✓          ✓

Total: 72 practice-domain combinations
```

---

## 3 Maturity Levels

Each practice-domain combination has **3 maturity levels:**

### Level 1: Foundational
- **Focus:** Essential practices for minimally viable HAI governance
- **Characteristics:** Basic processes, documented, happening at least once
- **Example:** "We have documented security requirements for this HAI system"

### Level 2: Comprehensive
- **Focus:** Systematic, organization-wide practices
- **Characteristics:** Repeatable, measured, integrated into workflows
- **Example:** "Security requirements are reviewed quarterly and tracked in compliance dashboard"

### Level 3: Industry-Leading
- **Focus:** Optimization, innovation, industry contribution
- **Characteristics:** Continuous improvement, research, public transparency
- **Example:** "We publish security requirements as industry best practices and contribute to standards"

**Scoring:** 0.0 (no practices) → 3.0 (all Level 3 achieved)

**Industry Benchmarks:**
- First assessment: 0.3 - 0.8 (typical)
- After 6 months: 0.8 - 1.3
- After 12 months: 1.2 - 1.8
- Mature programs (2+ years): 1.8 - 2.5

---

## Terminology Standards

### Capitalization
- ✅ "Human Assisted Intelligence" (when spelled out)
- ✅ "HAI" (abbreviation for systems)
- ✅ "HAIAMM" (framework name)
- ✅ Practice names capitalized: "Strategy & Metrics", "Design Review"
- ✅ Business functions capitalized: "Governance", "Building", "Verification", "Operations"
- ✅ Domains capitalized: "Software", "Data", "Infrastructure", "Vendors", "Processes", "Endpoints"

### Hyphenation
- ❌ "Human-Assisted Intelligence" (incorrect - no hyphen)
- ✅ "Human Assisted Intelligence" (correct)
- ✅ "HAI system" (not "HAI-system")
- ✅ "practice-domain combination" (hyphenated compound modifier)

### Abbreviations
- **HAI** = Human Assisted Intelligence (systems/solutions)
- **HAIAMM** = Human Assisted Intelligence Assurance Maturity Model (framework)
- **SM** = Strategy & Metrics
- **PC** = Policy & Compliance
- **EG** = Education & Guidance
- **TA** = Threat Assessment
- **SR** = Security Requirements
- **SA** = Secure Architecture
- **DR** = Design Review
- **IR** = Implementation Review
- **ST** = Security Testing
- **EH** = Environment Hardening
- **IM** = Issue Management
- **ML** = Monitoring & Logging

---

## Core Principles

**1. Human Oversight**
- HAI systems **assist** humans, not replace them
- Humans maintain decision authority
- Human oversight is required, not optional
- Human-AI collaboration quality is measured

**2. Trust, Safety, and Security**
- **Trust:** Reliable, explainable, fair AI systems
- **Safety:** AI systems that don't cause harm
- **Security:** Protection from adversarial threats and vulnerabilities

**3. Progressive Maturity**
- Start at Level 1 (foundational)
- Progress systematically to Level 2 (comprehensive)
- Achieve Level 3 (industry-leading) over time
- Continuous improvement, not one-time compliance

**4. Evidence-Based Assessment**
- Objective, verifiable criteria
- Documentation required for "Yes" answers
- Honest self-assessment for improvement
- Regular re-assessment (quarterly/semi-annual)

**5. Domain Coverage**
- Assess all 6 domains for comprehensive view
- No single domain is sufficient
- Cross-domain dependencies matter
- Prioritize based on risk

---

## Use Cases (Canonical Examples)

**HAI systems that HAIAMM addresses:**

1. **Security Testing & Code Analysis**
   - AI-powered SAST/DAST tools
   - Vulnerability scanning with AI prioritization
   - Automated code review assistants
   - Security configuration analysis

2. **Customer Service Automation**
   - Chatbots with human escalation
   - Virtual assistants for customer support
   - Automated ticket triage and routing
   - Knowledge base assistants

3. **Workflow Automation**
   - AI-assisted business process automation
   - Document processing and classification
   - Data entry and validation
   - Compliance automation and reporting

4. **Decision Support**
   - AI recommendations with human approval
   - Risk assessment and prioritization
   - Resource allocation optimization
   - Fraud detection with human review

5. **Content Generation**
   - AI-assisted content creation with human editing
   - Code generation with developer review
   - Report generation with human validation
   - Translation and summarization

**Common Thread:** All examples involve **AI assisting humans**, not autonomous AI systems.

---

## What HAIAMM is NOT

**HAIAMM is not designed for:**
- ❌ Fully autonomous AI systems (no human oversight)
- ❌ General AI ethics frameworks (broader scope than HAIAMM)
- ❌ AI model development best practices only (HAIAMM covers full lifecycle)
- ❌ AI risk management frameworks only (HAIAMM covers trust, safety, security, and maturity)

**HAIAMM complements:**
- ✅ NIST AI Risk Management Framework (adds maturity assessment)
- ✅ ISO/IEC 27001 (extends for HAI-specific controls)
- ✅ OWASP SAMM (adds multi-domain + HAI-specific practices)
- ✅ Industry regulations (EU AI Act, etc.) - provides implementation framework

---

## Assessment Method

**HAIAMM uses questionnaire-based assessment** (similar to OpenSAMM v1.0):

**Process:**
1. Select scope (HAI system to assess)
2. Answer questions (6-9 per practice, across 3 levels)
3. Calculate scores (per practice, overall maturity)
4. Analyze results (strengths, gaps, risk areas)
5. Create roadmap (prioritized improvements)

**Scoring:**
- Answer ALL Level 1 questions "Yes" → Achieved Level 1 (score: 1.0)
- Answer ALL Level 2 questions "Yes" → Achieved Level 2 (score: 2.0)
- Answer ALL Level 3 questions "Yes" → Achieved Level 3 (score: 3.0)
- Overall maturity = Average of 12 practice scores

**Frequency:** Quarterly or semi-annual re-assessment

---

## Documentation Standards

**When writing about HAIAMM:**

1. **Always use full name first:** "Human Assisted Intelligence Assurance Maturity Model (HAIAMM)" then "HAIAMM" thereafter
2. **Practice order:** Always list in Governance → Building → Verification → Operations order
3. **Domain order:** Always list as Software, Data, Infrastructure, Vendors, Processes, Endpoints
4. **Emphasize human oversight:** HAI systems assist humans, humans maintain authority
5. **Focus on trust, safety, security:** Not just one aspect
6. **Include use case examples:** Security testing, chatbots, automation, code analysis
7. **Reference OpenSAMM foundation:** Acknowledge lineage and extensions

---

## Version Control

**This document is the canonical reference for HAIAMM structure.**

**When making changes:**
1. Update this document first
2. Propagate changes to all documentation consistently
3. Update version numbers and change logs
4. Notify documentation maintainers

**Change Log:**
- v1.0 (2025-12-28): Initial canonical structure document created

---

## References

**Foundation:**
- OWASP OpenSAMM v1.0 - Base maturity model methodology
- Pravir Chandra, "OpenSAMM Future Directions" (3/27/2015) - Multi-domain architecture inspiration

**Alignment:**
- NIST AI Risk Management Framework
- ISO/IEC 27001:2022
- ISO/IEC 42001:2023 (AI Management Systems)
- OWASP Top 10 for LLM Applications

---

**This is the authoritative structure document for HAIAMM. All other documentation must align with these definitions.**
