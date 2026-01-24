# NLnet NGI Zero Commons Fund Application
## HAIAMM + Verifhai: Open Source AI Security Maturity Framework

**Application Deadline:** February 1, 2026
**Requested Amount:** €45,000
**Project Duration:** 12 months

---

## 1. Project Summary

**Project Name:** HAIAMM - Human Assisted Intelligence Assurance Maturity Model

**One-line description:** An open source framework and interactive tool (Verifhai) for assessing and improving the security of AI agents operating in critical security roles.

**Abstract (250 words):**

As AI agents increasingly perform security-critical operations—autonomous threat detection, automated vulnerability remediation, compliance evidence generation—no standardized framework exists to assess whether these AI security operations are actually effective and trustworthy.

HAIAMM (Human Assisted Intelligence Assurance Maturity Model) fills this gap. It's an open source maturity framework with 12 security practices across 6 domains, providing organizations with measurable outcomes for AI-operated security programs. Version 2.2 achieves 95% alignment with OWASP Top 10 for LLM and Agentic Applications.

Verifhai is the interactive implementation tool—a CLI mentor that guides practitioners through building security artifacts, conducting assessments, and reviewing code for AI-specific vulnerabilities. Unlike traditional questionnaire-based assessment tools, Verifhai helps users CREATE security documentation, not just evaluate it.

This project requests funding to:
1. Develop a web-based assessment platform for broader accessibility
2. Create multilingual documentation (German, French, Spanish)
3. Build integration APIs for existing security toolchains
4. Establish a community contribution framework with open governance

The project directly supports NLnet's mission of an open, trustworthy internet by ensuring AI systems making security decisions operate transparently and effectively. As the EU AI Act enforcement begins in 2026, organizations need open frameworks—not proprietary vendor solutions—to demonstrate AI governance compliance.

All outputs will be released under Apache 2.0 (code) and CC BY 4.0 (documentation), ensuring perpetual open access.

---

## 2. Project Details

### 2.1 Problem Statement

**The Paradigm Shift:**
- 1990-2020: Humans perform security operations
- 2020-2024: Humans assisted by AI
- 2025+: AI agents perform security operations, humans oversee

**Real-World Impact:**
AI security agents are already making thousands of autonomous decisions:
- Darktrace autonomously blocks threats
- GitHub Copilot Autofix auto-merges security patches
- AI GRC tools generate compliance evidence
- Wiz AI runs continuous penetration testing

**The Gap:**
Existing frameworks (NIST AI RMF, ISO 42001, OWASP SAMM) don't address a critical question: "Is our AI-operated security program actually effective?"

- ISO 27001 assesses human controls
- NIST CSF assesses human processes
- OWASP SAMM assesses human development
- **Nothing assesses AI-operated security**

**Risk Amplification:**
When human analysts make mistakes, impact is limited. When AI agents make mistakes, they affect entire classes of systems simultaneously. A 2025 incident saw an AI testing agent miss ALL GraphQL vulnerabilities for 9 months because it was only trained on REST APIs—200+ critical vulnerabilities ignored, resulting in €4M+ breach costs.

### 2.2 Solution: HAIAMM + Verifhai

**HAIAMM Framework (Already Built):**
- 4 business functions: Governance, Building, Verification, Operations
- 12 security practices with detailed implementation guidance
- 6 domains: Software, Data, Infrastructure, Vendors, Processes, Endpoints
- 3 maturity levels: Foundational → Comprehensive → Industry-Leading
- 432 assessment questions with measurable outcomes
- Full OWASP Top 10 mapping (LLM + Agentic Applications)

**Verifhai Tool (Already Built):**
- Interactive CLI mentor integrated with Claude Code
- Commands: `/verifhai start`, `/verifhai assess`, `/verifhai practice`, `/verifhai review`
- Builds security artifacts (requirements, threat assessments, architecture reviews)
- Code review for AI-specific vulnerabilities (prompt injection, goal hijacking, tool misuse)

### 2.3 Proposed Work (NLnet Funding)

**Deliverable 1: Web Assessment Platform (€18,000)**
- Browser-based assessment interface for non-CLI users
- Self-service maturity scoring with visualization
- Export to PDF/CSV for compliance documentation
- Anonymized benchmarking data contribution (opt-in)
- Technology: TypeScript, Cloudflare Pages, SQLite (local-first)

**Deliverable 2: Multilingual Documentation (€9,000)**
- German translation (EU AI Act primary language)
- French translation (major EU market)
- Spanish translation (global reach)
- Community translation infrastructure for additional languages

**Deliverable 3: Integration APIs (€12,000)**
- REST API for CI/CD pipeline integration
- SARIF export for security toolchain compatibility
- SPDX/CycloneDX integration for supply chain visibility
- Webhook support for automated assessment triggers

**Deliverable 4: Community Governance Framework (€6,000)**
- RFC process for practice additions
- Contributor guidelines and code of conduct
- Technical steering committee charter
- Annual versioning and backwards compatibility policy

### 2.4 Timeline

| Month | Deliverable | Milestone |
|-------|-------------|-----------|
| 1-2 | Web Platform | MVP with core assessment flow |
| 3-4 | Web Platform | Full feature set, benchmarking |
| 5-6 | Translations | German + French complete |
| 7-8 | Translations | Spanish + infrastructure |
| 9-10 | APIs | REST API + SARIF export |
| 11-12 | APIs + Governance | Full integration + governance docs |

---

## 3. Relevance to NGI Zero Commons

### 3.1 Digital Commons Contribution

HAIAMM contributes to open digital infrastructure by:

1. **Open Standards for AI Security:** No proprietary vendor lock-in for AI governance
2. **Interoperability:** OWASP alignment ensures compatibility with existing security frameworks
3. **Accessibility:** Free framework democratizes AI security assessment beyond large enterprises
4. **Transparency:** Open methodology allows public scrutiny and improvement

### 3.2 Alignment with NGI Goals

**Trustworthy Internet:**
AI agents are increasingly part of internet infrastructure (security monitoring, threat response, content moderation). HAIAMM ensures these systems operate transparently with human oversight.

**Human-Centric Technology:**
The "Human Assisted Intelligence" paradigm keeps humans in control. HAIAMM's "Least Agency Principle" ensures AI systems assist rather than replace human decision-making.

**Open Source Ecosystem:**
Following OWASP's proven model—free framework drives adoption, community contributions improve quality, paid certification provides validation without restricting access.

### 3.3 European Relevance

**EU AI Act Compliance:**
The EU AI Act (enforcement June 2026) requires documented oversight for high-risk AI systems. AI agents making security decisions qualify. HAIAMM provides the assessment framework organizations need—built on open standards, not proprietary solutions.

**Digital Sovereignty:**
European organizations need open frameworks to assess AI security without dependence on US-based proprietary tools. HAIAMM fills this gap.

---

## 4. Technical Approach

### 4.1 Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    HAIAMM Ecosystem                          │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────────┐      ┌──────────────────────────────┐ │
│  │  Verifhai CLI    │      │  Web Assessment Platform     │ │
│  │  (Existing)      │      │  (NLnet Funded)              │ │
│  └────────┬─────────┘      └─────────────┬────────────────┘ │
│           │                              │                   │
│           └──────────────┬───────────────┘                   │
│                          │                                   │
│                          ▼                                   │
│           ┌──────────────────────────────┐                   │
│           │    HAIAMM Core Framework     │                   │
│           │    (JSON Data Model)         │                   │
│           │    - 12 practices            │                   │
│           │    - 6 domains               │                   │
│           │    - 432 questions           │                   │
│           └──────────────┬───────────────┘                   │
│                          │                                   │
│           ┌──────────────┴───────────────┐                   │
│           ▼                              ▼                   │
│  ┌──────────────────┐      ┌──────────────────────────────┐ │
│  │  Integration API │      │  Benchmarking Database       │ │
│  │  (NLnet Funded)  │      │  (Anonymized, Opt-in)        │ │
│  └──────────────────┘      └──────────────────────────────┘ │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 4.2 Technology Stack

- **Frontend:** TypeScript, Svelte/SvelteKit (lightweight, accessible)
- **Backend:** Cloudflare Workers (edge deployment, no server maintenance)
- **Database:** SQLite with Turso (local-first, privacy-preserving)
- **API:** OpenAPI 3.1 specification
- **Documentation:** Markdown, MkDocs (static generation)
- **Translations:** Weblate (community translation platform)

### 4.3 Privacy & Security

- **Local-First Assessment:** All assessment data can be stored locally
- **Opt-In Benchmarking:** Anonymized data sharing only with explicit consent
- **No Tracking:** No analytics that identify individual organizations
- **Open Audit:** All code open source for security review

---

## 5. Team & Background

### 5.1 Project Lead

**[Your Name]**
- Security professional with experience in AI security assessment
- Creator of HAIAMM framework and Verifhai tool
- Background in security maturity models (SAMM, BSIMM)
- Active contributor to OWASP community

### 5.2 Relevant Experience

- Developed HAIAMM v1.0-v2.2 over 18 months
- Built Verifhai interactive assessment tool
- Conducted pilot assessments with early adopter organizations
- Contributed to OWASP Top 10 for LLM Applications

### 5.3 Open Source Commitment

All project outputs will be released under:
- **Code:** Apache 2.0 License
- **Documentation:** Creative Commons Attribution 4.0 (CC BY 4.0)
- **Data Models:** Open Database License (ODbL)

---

## 6. Budget

| Category | Amount | Description |
|----------|--------|-------------|
| **Web Platform Development** | €18,000 | Frontend, backend, deployment infrastructure |
| **Translation Services** | €9,000 | Professional translation + community infrastructure |
| **API Development** | €12,000 | REST API, SARIF export, webhook support |
| **Community Governance** | €6,000 | RFC process, documentation, steering committee |
| **Total** | €45,000 | |

### 6.1 Budget Justification

- **Web Platform:** 360 hours @ €50/hour average (mix of development, design, testing)
- **Translations:** €3,000 per language × 3 languages
- **APIs:** 240 hours @ €50/hour average
- **Governance:** 120 hours @ €50/hour average

---

## 7. Sustainability

### 7.1 Post-Funding Sustainability

**Community Model (OWASP-style):**
- Free framework drives adoption
- Community contributions improve quality
- Paid certification provides validation revenue

**Revenue Streams (Post-Grant):**
1. **Certification Services:** Third-party assessment and certification
2. **Training Programs:** Certified HAIAMM Assessor training
3. **Enterprise Support:** Priority support and custom implementation
4. **Consulting:** Gap remediation and architecture guidance

### 7.2 Community Building

- Monthly community calls for contributors
- Annual HAIAMM summit (virtual, free)
- Recognition program for significant contributors
- Academic partnership for research validation

---

## 8. Links & References

**Existing Resources:**
- GitHub Repository: [HAIAMM repo URL]
- Documentation: [HAIAMM handbook URL]
- Verifhai Demo: [Demo URL or video]

**Related Standards:**
- OWASP Top 10 for LLM Applications: https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/
- OWASP Top 10 for Agentic Applications: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework

---

## 9. Contact Information

**Primary Contact:** [Your Name]
**Email:** [Your Email]
**Location:** [Your Location]
**Timezone:** [Your Timezone]

---

**Application Submitted:** [Date]
**NLnet Program:** NGI Zero Commons Fund
**Requested Amount:** €45,000

---

*This application is submitted for the NLnet NGI Zero Commons Fund February 1, 2026 deadline.*
