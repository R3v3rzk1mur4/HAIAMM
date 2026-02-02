# HAIAMM - Human Assisted Intelligence Assurance Maturity Model

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/R3v3rzk1mur4/HAIAMM.svg?style=social&label=Star)](https://github.com/R3v3rzk1mur4/HAIAMM)

**What is Human Assisted Intelligence (HAI)?**
Human Assisted Intelligence (HAI) refers to systems or technologies that combine human cognitive capacities with artificial intelligence to enhance automation, creativity, problem solving, decision making. Unlike fully autonomous AI, HAI relies on human input alongside machine learning to improve its effectiveness.

![alt text](<HAIAMM-Image03_47_44 PM.png>)

**HAIAMM v2.0, or the Human Assisted Intelligence Assurance Maturity Model version 2.0, is a framework designed to help organizations develop and implement effective Human Assisted Intelligence assurance strategies. This model enables organizations to assess their current HAI governance and security practices, establish improvement roadmaps, and ensure that trust, safety, and appropriate human oversight are integrated into their HAI systems and operations.**

**The Critical Question:** You're implementing Human Assisted Intelligence across your organization - but how do you ensure it delivers trust, safety, and security with proper governance and human oversight?

**HAIAMM's Answer:** A quantifiable maturity assessment across 12 practices and 6 domains for comprehensive HAI assurance.

## 🌟 Open Source & Community-Driven

**HAIAMM is 100% free and open source** - following the successful Software Assurance Maturity Model V1.0:
- ✅ **Framework**: Free to use, adapt, and share (CC BY-SA 4.0)
- ✅ **Software**: Open source assessment tool (MIT License)
- ✅ **Community**: Contributions welcome from security professionals worldwide

**[Get Started](#installation)** | **[Contribute](CONTRIBUTING.md)**

---

## Why This Matters NOW

### The Human Assisted Intelligence Challenge

Organizations are designing and implementing Human Assisted Intelligence or AI to augment critical functions:

- **Automation Workflows**: HAI systems handling business processes with human oversight
- **Security Testing & Code Analysis**: AI-powered vulnerability scanning, SAST/DAST tools, automated code review
- **Customer Service**: Chatbots and virtual assistants with human escalation pathways
- **Decision Support**: HAI providing recommendations with human approval and validation
- **Data Processing**: HAI assisting humans in analysis, pattern detection, and insights generation

**The Problem:** Organizations are deploying HAI at scale, but have **NO comprehensive framework or plan to ensure trust, safety, security, proper governance, and human oversight.**

### Why HAIAMM Fills a Critical Gap

**1. COMPREHENSIVE APPROACH - Trust, Safety, and Security**
- **NIST AI RMF**: Focuses on AI risk management (important but narrow)
- **ISO 27001**: Traditional security controls (pre-HAI era)
- **HAIAMM**: Flexible, and yet offers complete framework for governance, building, verification, and operations of Human Assisted Intelligence
- **Focus:** Foundational practices ensuring trust, safety, and security of HAI solutions
- Addresses the full lifecycle of HAI deployment

**2. HUMAN OVERSIGHT - Ensuring Appropriate Control**
- HAI systems assist human decision-making that impacts business, customers, and operations
- Organizations need to demonstrate proper human oversight and accountability
- HAIAMM provides framework for measuring and improving human-AI collaboration
- **Human Assisted Intelligence requires mature governance and oversight practices**

**3. OPERATIONAL MATURITY - Beyond Compliance**
- Not just "is it secure?" but "does it deliver trust, safety, and security with proper human oversight?"
- Assesses governance, building, verification, and operations
- Helps organizations build mature HAI practices
- **Enables sustainable, scalable HAI adoption**

**4. REGULATORY READINESS - Compliance Coming**
- EU AI Act: Requires governance and human oversight for high-risk AI systems
- Industry regulations: Increasing scrutiny of AI-assisted decision-making
- Board oversight: Need to demonstrate responsible HAI deployment
- **HAIAMM provides the assessment framework for compliance**

**5. ACCOUNTABILITY - "Who's Responsible?"**
- When HAI system assists in a wrong decision, who's accountable?
- How do you prove appropriate human oversight of HAI operations?
- HAIAMM provides governance framework and audit trail

### What HAIAMM Assesses

**Not:** "Is your AI system secure?" (that's one part, addressed by NIST AI RMF)
**Instead:** "Is your organization mature in how it governs, builds, verifies, and operates Human-Assisted Intelligence?"

Example Questions HAIAMM Answers:
- ✅ Do you have proper governance for HAI deployment?
- ✅ Are HAI decisions aligned with business risk with appropriate human oversight?
- ✅ Can humans appropriately oversee and override HAI recommendations?
- ✅ Are your HAI systems built with security and safety requirements?
- ✅ Do you have processes to verify HAI behaviors before deployment?

---

## Features

- **🎯 Tiered Assessment Approach**: Choose your assessment depth based on needs and time available
  - **Tier 1 (Foundation)**: Quick 20-30 minute baseline covering critical domains (24 questions)
  - **Tier 2 (Standard)**: Comprehensive 3-4 hour operational assessment (208 questions)
  - **Tier 3 (Comprehensive)**: Full 12-16 hour maturity assessment for compliance (468 questions)
- **Multi-Domain Architecture**: Comprehensive coverage across 6 security domains (Software, Data, Infrastructure, Vendors, Processes, Endpoints)
- **Dynamic Questionnaires**: Tier-based questionnaire generation adapts to your selected assessment level
- **Domain-Specific Assessment**: Filter and assess individual domains or perform comprehensive cross-domain analysis
- **Maturity Scoring**: Automated calculation of maturity levels (0-3) for each security practice with domain-level aggregation
- **Interactive Dashboards**: Rich visualizations using Plotly (radar charts showing all 6 domains, multi-domain heatmaps, bar charts)
- **Export & Encryption**: Save assessments in JSON/CSV format with mandatory PGP encryption
- **Version Control**: Track assessment history with undo/redo functionality
- **Roadmap Planning**: Create and track HAIAMM implementation roadmaps across domains
- **Progress Tracking**: Compare assessments over time to measure improvements across all security domains

## Tiered Assessment System

HAIAMM v2.0 implements a flexible tiered approach with streamlined questions for improved efficiency:

| Tier | Name | Time | Questions | Domains | Use Case |
|------|------|------|-----------|---------|----------|
| **1** | Foundation | 20-30 min | 24 | Software, Data | Quick baseline, executive briefing, quarterly checks |
| **2** | Standard | 3-4 hours | 192 | +Infrastructure, Endpoints | Operational assessment, improvement planning |
| **3** | Comprehensive | 12-16 hours | 432 | All 6 domains | Compliance, audit, industry benchmarking |

**v2.0 Improvements:**
- ⚡ **12 focused practices** - Streamlined from 13 (removed Operational Enablement)
- 🚀 **40% faster** assessment times across all tiers
- 📉 **432 questions** (down from 702) - 38% fewer questions
- 📈 **Progressive depth** - start small, expand as needed
- ✅ **Flexible** - choose the right level for your organization

See [docs/TIER-IMPLEMENTATION-SUMMARY.md](docs/TIER-IMPLEMENTATION-SUMMARY.md) for complete details.

## HAIAMM Coverage - Human Assisted Intelligence Domains

### 6 Domains for Comprehensive HAI Assessment

1. **Software**: HAI applications, models, code, AI-assisted development, security testing tools
2. **Data**: Training/operational data, privacy, quality, governance of human-AI data interactions
3. **Infrastructure**: Cloud/on-premise platforms, security testing, deployment environments, scaling with human oversight
4. **Vendors**: Third-party HAI services, vendor management, supply chain for HAI components
5. **Processes**: Business workflows involving HAI, governance procedures, compliance, automation
6. **Endpoints**: User interfaces, APIs, security testing, integration points where humans interact with HAI

### 4 Business Functions - How Organizations Build and Deploy Human Assisted Intelligence

Each domain assesses 4 business functions that organizations perform:

1. **Governance**: How you govern, measure, and educate around HAI with human oversight
   - Strategy & Metrics, Policy & Compliance, Education & Guidance

2. **Building**: How you design and build HAI systems with appropriate security controls
   - Threat Assessment, Security Requirements, Secure Architecture

3. **Verification**: How you verify HAI systems work correctly and safely with human validation
   - Design Review, Implementation Review, Security Testing

4. **Operations**: How you operate and maintain HAI systems with human monitoring
   - Environment Hardening, Issue Management, Monitoring & Logging

### Model Statistics (v2.0)
- **6 Domains** covering comprehensive HAI security landscape
- **4 Business Functions**
- **72 Security Practice Instances** (12 practices × 6 domains)
- **3 Maturity Levels** (3 per practice instance)
- **Assessment Criteria** (reduced from 702 in v1.0)

**v2.0 Changes:**
- **Question Reduction**: Streamlined from 3 questions per practice level to 2 questions per level
- **Practice Simplification**: Reduced from 13 to 12 practices (removed Operational Enablement)
- **12 Core Practices** for assessing Human Assisted Intelligence:

### GOVERNANCE - "How do you govern HAI with human oversight?"

**SM - Strategy & Metrics**
- Are HAI activities aligned with business objectives and risk?
- Do you measure effectiveness and human oversight of HAI?
- Example: Tracking business outcomes, error rates, and human override frequency for HAI systems

**PC - Policy & Compliance**
- Do you have policies governing HAI deployment with human oversight requirements?
- Are HAI-assisted decisions auditable and explainable?
- Example: Can you show auditors the governance process and human oversight for HAI?

**EG - Education & Guidance**
- Are staff trained on collaborating with and overseeing HAI?
- Do people know when and how to override HAI recommendations?
- Example: Training employees to critically evaluate HAI recommendations before acting

### BUILDING - "How do you build HAI with human controls?"

**TA - Threat Assessment**
- Do you identify threats and risks specific to HAI systems?
- Have you assessed adversarial risks like prompt injection or data poisoning?
- Example: Threat modeling identifies risks in your HAI chatbot with human oversight gaps

**SR - Security Requirements**
- Do you define security and safety requirements for HAI?
- Are human oversight requirements documented before deployment?
- Example: Defining requirements for data privacy, output validation, and mandatory human review

**SA - Secure Architecture**
- Are HAI systems designed with security controls and human oversight points?
- Do you follow secure design principles for human-AI collaboration?
- Example: HAI systems have appropriate access controls with human approval gates

### VERIFICATION - "How do you verify HAI works correctly with human validation?"

**DR - Design Review**
- Do you review HAI system designs before deployment?
- Are human oversight mechanisms validated by appropriate experts?
- Example: Architecture review validates that HAI decision logic includes human validation

**IR - Implementation Review**
- Do you review prompts, configurations, and code for HAI?
- Are HAI-generated outputs reviewed by humans before use?
- Example: Reviewing system prompts and human override mechanisms before deploying HAI assistant

**ST - Security Testing**
- Do you test HAI systems for security vulnerabilities?
- Can you verify HAI behaves safely with appropriate human controls?
- Example: Testing HAI for prompt injection, bias, and human override functionality

### OPERATIONS - "How do you operate HAI with human monitoring?"

**EH - Environment Hardening**
- Are HAI runtime environments properly secured?
- Do you protect API keys, credentials, and sensitive configurations?
- Example: HAI systems run with least-privilege access and human-controlled secrets management

**ML - Monitoring & Logging**
- Do you monitor HAI behavior and human interactions?
- Can you audit what HAI recommended and what humans decided?
- Example: Logging HAI recommendations, human decisions, and override patterns for audit trails

**IM - Issue Management**
- How do you handle issues and errors from HAI?
- Do you track and learn from HAI failures and human corrections?
- Example: Process for investigating HAI errors, human overrides, and improving human-AI collaboration

---

Each of the 72 practice instances has 3 maturity levels with specific assessment criteria tailored for responsible Human Assisted Intelligence.

**HAIAMM uses a dual-license model (same as SAMM):**

- **Framework & Content:** [Creative Commons Attribution-ShareAlike 4.0 (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/)
  - HAIAMM framework, methodology, documentation, assessment content
  - Free to use, adapt, and share with attribution

- **Software & Tools:** [MIT License](https://opensource.org/licenses/MIT)
  - Desktop application source code, tools, and utilities
  - Free to use, modify, and distribute

See [LICENSE](LICENSE) file for complete details.

**Attribution:** When using HAIAMM framework, please credit:
> Based on OpenSAMM future directions by Pravir Chandra 03/27/2015

---

## HAIAMM Handbook

The **HAIAMM Handbook** provides practical guidance for implementing AI security using the HAIAMM framework. Whether you're securing a simple LLM integration or deploying autonomous AI agents, the handbook offers actionable steps, risk mappings, and assessment tools.

### Table of Contents

| Chapter | Title | Description |
|---------|-------|-------------|
| [00](docs/handbook/00-COVER.md) | Cover | Handbook cover and version information |
| [01](docs/handbook/01-QUICK-START.md) | Quick Start Guide | Get started securing your AI systems in 10 minutes |
| [02](docs/handbook/02-FIRST-30-DAYS.md) | First 30 Days | Day-by-day implementation roadmap |
| [03](docs/handbook/03-TOP10-LLM-RISKS.md) | OWASP Top 10 for LLM Applications | Security controls mapped to LLM application risks |
| [04](docs/handbook/04-TOP10-AGENTIC-RISKS.md) | OWASP Top 10 for Agentic Applications | Security controls for autonomous AI agent risks |
| [05](docs/handbook/05-RISK-PRACTICE-MATRIX.md) | Risk-Practice Matrix | Which HAIAMM practices address which risks |
| [06](docs/handbook/06-MATURITY-ROADMAP.md) | Maturity Roadmap | Level 1 → 2 → 3 progression guide |
| [07](docs/handbook/07-ASSESSMENT-CHECKLIST.md) | Assessment Checklist | Rapid 30-minute self-assessment |
| [08](docs/handbook/08-TOOLS-RESOURCES.md) | Tools & Resources | Recommended tools organized by practice |

**[View Full Handbook](docs/HAIAMM-Handbook.md)** - Complete consolidated handbook document

---

## References

- [OpenSAMM v1.0 Documentation](https://opensamm.org/downloads/SAMM-1.0.pdf)
- HAIAMM extends SAMM v1.0 with multi-domain architecture for comprehensive assessment of Human-Assisted Intelligence governance, building, verification, and operations with appropriate human oversight
