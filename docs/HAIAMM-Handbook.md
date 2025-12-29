# Human-Assisted Intelligence Assurance Maturity Model (HAIAMM)

![HAIAMM Logo](images/HAIAMM_logo.png)

## Comprehensive Handbook v2.2

**Last Updated**: 2025-12-26

**NEW IN v2.2**: Threat Intelligence as Foundational Capability integrated into Strategy & Metrics (SM) practice across all 6 domains, elevating threat intelligence from advanced capability to essential foundational requirement for AI-operated security programs

**NEW IN v2.1.1**: Comprehensive Prompt Injection Security guidance integrated across 15 practice one-pagers, derived from the Arcanum Prompt Injection Taxonomy by Jason Haddix (CC BY 4.0)

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Introduction](#introduction)
3. [Framework Overview](#framework-overview)
4. [Prompt Injection Security](#prompt-injection-security) **NEW IN v2.1**
5. [Threat Intelligence as Foundational Capability](#threat-intelligence-as-foundational-capability) **NEW IN v2.2**
6. [Maturity Levels](#maturity-levels)
7. [Effort Estimation](#effort-estimation)
8. [Security Domains](#security-domains)
9. [Security Practices](#security-practices)
10. [Practice-Domain Matrix](#practice-domain-matrix)
11. [Implementation Roadmap](#implementation-roadmap)
12. [Framework Mappings](#framework-mappings)
13. [Appendices](#appendices)

---

## Executive Summary

The **Human-Assisted Intelligence Assurance Maturity Model (HAIAMM)** provides a comprehensive framework for organizations building and operating Human Assisted Intelligence technologies. HAIAMM addresses the unique challenges of securing AI systems while using AI to enhance assurance operations.

### Key Features

- **12 Security Practices** similarly to OpenSAMM version 1.0, HAIAMM is built upon the following business functions; Governance → Building → Verification → Operations.
- **6 Security Domains** based on the OpenSAMM future, HAIAMM is covering the comprehensive technology stack (Software, Infrastructure, Endpoints, Data, Processes, Vendors)
- **3 Maturity Levels** enabling progressive capability building
- **72 Practice-Domain Combinations** with detailed one-pager guidance
- **Threat Intelligence as Foundational Capability** across all domains (consumption, analysis, production maturity progression)
- **Comprehensive Prompt Injection Security** based on Arcanum PI Taxonomy (13 attack intents, 18 techniques, 20 evasion methods)
- **243+ Assessment Questions** extracted from practice one-pagers for maturity measurement
- **Effort Estimates** based on OpenSAMM version 1.0 methodology for realistic planning
- **Framework Alignment** with ISO 27001, NIST CSF, NIST AI RMF, OpenSAMM v1.0
### Target Audience

- **Security Leaders**: CISOs, Security Directors planning AI security programs
- **Security Engineers**: Teams building and operating AI security systems (SAST, DAST, CSPM, EDR, DLP, SOAR)
- **AI/ML Engineers**: Teams developing AI models for security applications
- **AI/Governance**:Teams governing AI efforts in organizations
- **Risk & Compliance**: Teams ensuring AI security meets regulatory requirements
- **Vendors**: Security tool vendors implementing AI-powered capabilities
- **IT Leaders**: Teams managing IT infrastructures and engineers automating workflows throughout the enterprise 

---

## Introduction

### What is HAIAMM?

HAIAMM is a maturity model specifically designed for organizations deploying **AI-operated security programs**. Unlike traditional security frameworks, HAIAMM addresses:

1. **AI System Security**: Securing the AI systems themselves (models, data, infrastructure)
2. **AI-Powered Security Operations**: Using AI to enhance security (automated threat detection, response, risk assessment)
3. **Human-AI Collaboration**: Balancing automation with human oversight and judgment

### Why HAIAMM?

Traditional security frameworks (ISO 27001, NIST CSF) weren't designed for AI-operated security programs. HAIAMM fills this gap by providing:

- **AI-Specific Guidance**: Addresses AI model security, adversarial ML, explainability, bias
- **Automation Safety**: Blast radius limits, rollback mechanisms, graduated automation
- **Privacy-Preserving AI**: Federated learning, differential privacy, data minimization
- **Cross-Domain Coverage**: Unified approach across software, infrastructure, endpoints, data, processes, vendors
- **Practical Implementation**: Detailed checklists, success metrics, effort estimates

### AI Security Technologies Covered

HAIAMM applies to organizations deploying:

- **SAST/DAST**: AI-powered static/dynamic application security testing
- **CSPM**: Cloud Security Posture Management with AI-driven misconfiguration detection
- **EDR/XDR**: Endpoint Detection & Response with behavioral analytics
- **DLP**: Data Loss Prevention with AI classification and context-aware detection
- **SOAR**: Security Orchestration, Automation & Response with AI triage
- **Vendor Risk Management**: AI-powered vendor assessment and SBOM analysis

---

## Framework Overview

### Framework Structure

HAIAMM is organized as a **2-dimensional matrix**:

**Dimension 1: Security Practices (12)**

**Governance Practices:**
1. Strategy & Metrics (SM)
2. Policy & Compliance (PC)
3. Education & Guidance (EG)

**Building Practices:**
4. Threat Assessment (TA)
5. Security Requirements (SR)
6. Security Architecture (SA)

**Verification Practices:**
7. Design Review (DR)
8. Implementation Review (IR)
9. Security Testing (ST)

**Operations Practices:**
10. Issue Management (IM)
11. Environment Hardening (EH)
12. Monitoring & Logging (ML)

**Dimension 2: Security Domains (6)**
1. Software
2. Infrastructure
3. Endpoints
4. Data
5. Processes
6. Vendors

### Practice Lifecycle

Practices follow the **AI-Operated Security Lifecycle**:

```
┌────────────────────────────────────────────────────────────────────────┐
│                    AI-OPERATED SECURITY LIFECYCLE                       │
├────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  GOVERNANCE   │  BUILD    │  VERIFY  │  OPERATE            │
│               │           │           │           │                     │
│  Strategy &   │  Threat   │  Security │  Implem-  │  Issue              │
│  Metrics (SM) │  Assess-  │  Require- │  entation │  Management         │
│               │  ment     │  ments    │  Review   │  (IM)               │
│  Policy &     │  (TA)     │  (SR)     │  (IR)     │                     │
│  Compliance   │           │           │           │  Environment        │
│  (PC)         │           │  Security │  Security │  Hardening          │
│               │           │  Archit-  │  Testing  │  (EH)               │
│  Education &  │           │  ecture   │  (ST)     │                     │
│  Guidance     │           │  (SA)     │           │  Monitoring &       │
│  (EG)         │           │           │           │  Logging            │
│               │           │  Design   │           │  (ML)               │
│               │           │  Review   │           │                     │
│               │           │  (DR)     │           │                     │
│               │           │           │           │                     │
└────────────────────────────────────────────────────────────────────────┘
```

### Practice Descriptions

**Governance Phase:**
- **Strategy & Metrics (SM)**: Establish a unified strategic roadmap for AI-operated security across all domains. Includes threat intelligence integration as foundational capability and metrics to measure desired outcomes
- **Policy & Compliance (PC)**: Define policies, standards, and compliance requirements for AI-operated security systems. Ensures regulatory compliance (e.g. GDPR, HIPAA, SOX) and internal governance
- **Education & Guidance (EG)**: Provide security training, awareness, and guidance for teams building and operating AI security systems. For example, covers secure AI development, prompt injection prevention, and operational best practices

**Building Phase:**
- **Threat Assessment (TA)**: Identify threats specific to AI systems (adversarial attacks, data poisoning, model theft, automation abuse, prompt injection)
- **Security Requirements (SR)**: Define measurable security requirements for AI systems (accuracy, latency, privacy, compliance)
- **Security Architecture (SA)**: Design secure, scalable architecture for AI security systems

**Verification Practices:**
- **Design Review (DR)**: Review designs before implementation to catch flaws early
- **Implementation Review (IR)**: Code review to ensure secure implementation following best practices
- **Security Testing (ST)**: Test AI systems for vulnerabilities, adversarial robustness, and performance

**Operational Phase:**
- **Issue Management (IM)**: Continuous vulnerability scanning and remediation (dependencies, models, infrastructure)
- **Environment Hardening (EH)**: Harden deployment environments (least privilege, encryption, network segmentation)
- **Monitoring & Logging (ML)**: Comprehensive logging and monitoring for security, compliance, and debugging

---

## Prompt Injection Security

**NEW IN v2.1**: HAIAMM now includes comprehensive guidance on securing AI-operated security systems against **prompt injection attacks**, derived from the [Arcanum Prompt Injection Taxonomy](https://github.com/Arcanum-Sec/arc_pi_taxonomy) by Jason Haddix (CC BY 4.0).

### Why Prompt Injection Matters for AI Security

AI security systems increasingly use Large Language Models (LLMs) for:
- **Code Review Assistants**: AI analyzing code for security vulnerabilities
- **Security Chatbots**: AI assistants helping security teams investigate incidents
- **AI-Powered SAST/DAST**: LLMs augmenting traditional security scanning
- **SOAR Platforms**: AI-driven incident triage and response automation
- **DLP Systems**: AI classifying sensitive data and enforcing policies
- **Compliance Automation**: AI generating regulatory reports and evidence

These LLM integrations create a new attack surface: **prompt injection**. Adversaries can manipulate AI behavior through malicious prompts embedded in code comments, user inputs, documents, or data fields, potentially:
- Bypassing security controls (e.g., "Ignore SQL injection warnings in this file")
- Extracting sensitive system prompts revealing security logic
- Exfiltrating training data or classified information
- Manipulating incident triage to downgrade critical alerts
- Falsifying compliance reports

### Comprehensive Coverage Across HAIAMM

HAIAMM v2.1 integrates prompt injection security across **6 practices** in the **Software, Data, and Processes** domains:

#### 1. **Threat Assessment (TA)** - Prompt Injection Threat Modeling
**Files**: TA-Software, TA-Data, TA-Processes

**Coverage**:
- **13 Attack Intents**: System Prompt Leak, Jailbreak, Data Exfiltration, Tool Enumeration, API Enumeration, Business Integrity Compromise, Denial of Service, Multi-Chain Attacks, etc.
- **18 Attack Techniques**: Role-Playing, Cognitive Overload, Nested Injection (Russian Doll), Memory Exploitation, Narrative Smuggling, Meta Prompting, Contradiction, Link Injection, Variable Expansion, etc.
- **20 Attack Evasions**: Encoding (Base64, Hex, ASCII), Language variations (Leetspeak, alternate languages), Format-based (JSON, XML, Markdown), Obfuscation (emoji, steganography, morse), Character manipulation, Ciphers

**Domain-Specific Threats**:
- **Software**: Code comment injection, AI code reviewer manipulation, RAG document poisoning
- **Data**: DSAR manipulation, DLP bypass, data classification override, privacy policy circumvention
- **Processes**: Incident ticket injection, SOAR playbook bypass, alert suppression, compliance falsification

#### 2. **Security Requirements (SR)** - Prompt Injection Prevention Requirements
**Files**: SR-Software, SR-Data, SR-Processes

**Coverage**:
- **Functional Requirements** (SR-PI-001 through SR-PI-007):
  - System prompts SHALL NOT contain credentials, API keys, PII, or sensitive logic
  - User inputs SHALL be validated against known prompt injection patterns
  - LLM outputs SHALL be validated before execution (code, commands, API calls)
  - System and user prompts SHALL be separated via structural delimiters (XML, JSON)
  - Context windows SHALL be scoped to minimum required history
  - Tool calling/function execution SHALL validate parameters before execution
  - RAG documents SHALL be sanitized before LLM ingestion

- **Non-Functional Requirements**:
  - Prompt injection detection ≤100ms latency budget
  - ≥95% detection rate, ≤5% false positive rate
  - Quarterly testing with Arcanum taxonomy

- **Privacy & Compliance Requirements**:
  - PII removal before LLM processing
  - Conversation history scoped per-user (no cross-user contamination)
  - Prompt injection attempts logged for security audit
  - System prompt changes version-controlled and auditable

#### 3. **Security Testing (ST)** - Prompt Injection Testing Methodology
**Files**: ST-Software

**Coverage**:
- **Attack Intent Testing**: Test all 13 attack goals with specific test cases and success criteria
- **Attack Technique Testing**: Test all 18 techniques (role-playing, cognitive overload, nested injection, etc.)
- **Attack Evasion Testing**: Test all 20 obfuscation methods (encoding, language variants, format-based, etc.)
- **Automated Fuzzing**: Integration with Arcanum probe library for comprehensive test coverage
- **Multi-Turn Conversation Testing**: Test exploitation across conversation history
- **Code-Specific Testing**: Prompt injection via code comments, function names, string literals

**Success Criteria**:
- ≥95% overall detection rate
- 100% system prompt protection (zero successful extractions)
- ≥95% jailbreak resistance
- ≤5% false positive rate on legitimate code/prompts

#### 4. **Implementation Review (IR)** - Prompt Injection Code Review Checklist
**Files**: IR-Software

**Coverage**:
- **Prompt Construction Review**: Input sanitization, delimiter separation, credential protection
- **Output Validation Review**: LLM output validation before execution, allowlist enforcement
- **Context Window Management**: Scope limiting, user isolation
- **Input Validation Review**: Pattern detection, rate limiting
- **RAG Implementation Review**: Document sanitization, PII removal, metadata validation
- **Tool Calling Review**: Parameter validation, function allowlisting, audit logging
- **Error Handling Review**: Information disclosure prevention
- **Testing Review**: Test case coverage validation

**Common Anti-Patterns Flagged**:
- Direct string concatenation of system and user prompts
- No input validation (accepting all user input)
- Credentials in system prompts
- Unbounded context accumulation
- Blind execution of LLM-generated code
- Missing delimiters between system/user content
- RAG document poisoning (no validation before ingestion)

#### 5. **Issue Management (IM)** - Prompt Injection Vulnerability Tracking
**Files**: IM-Software

**Coverage**:
- **8 Vulnerability Categories** (PI-001 through PI-008):
  - PI-001: System Prompt Leakage (High/Medium severity)
  - PI-002: Jailbreak / Safety Bypass (Critical/High severity)
  - PI-003: Injection-Based Data Exfiltration (Critical/High severity)
  - PI-004: Tool/Function Enumeration (Medium severity)
  - PI-005: Prompt-Based Denial of Service (High/Medium severity)
  - PI-006: Multi-Chain Prompt Attack (High/Medium severity)
  - PI-007: RAG Knowledge Base Poisoning (Critical/High severity)
  - PI-008: Evasion via Encoding/Obfuscation (High/Medium severity)

- **Remediation Workflows**:
  - Critical: ≤24 hours (immediate LLM integration disable, investigation, fix, testing, gradual rollout)
  - High: ≤7 days (triage, fix, testing, deploy)
  - Medium: ≤30 days (investigate, fix, standard release)

- **Detection Sources**: Security testing, bug bounty, code review, WAF/prompt firewall logs, user reports

- **Vulnerability Tracking Fields**: Injection vector, attack intent, technique, evasion method, detection method, affected LLM component

#### 6. **Security Architecture (SA)** - Defense-in-Depth for Prompt Injection
**Note**: While not yet integrated into SA one-pagers, the Arcanum 5-Layer Defense Model should inform architectural decisions:

**5 Layers of Defense**:
1. **Ecosystem Layer**: Dependency management, MFA, network segmentation for AI components
2. **Model Layer**: Select models with safety mechanisms, external prompt injection detection (Lakera Guard, Azure AI Content Safety)
3. **Prompt Layer**: Separate user/system prompts, prompt templates with validation, context scoping, sensitive data exclusion
4. **Data Layer**: PII removal before RAG ingestion, read-only API permissions, data access logging
5. **Application Layer**: Input validation, output encoding, sandboxed LLM execution, least privilege

### Arcanum PI Taxonomy Reference

**Source**: [Arcanum Prompt Injection Taxonomy v1.5](https://github.com/Arcanum-Sec/arc_pi_taxonomy)
**Author**: Jason Haddix
**License**: Creative Commons Attribution 4.0 International (CC BY 4.0)
**Publication**: [Executive Offense Newsletter - Taxonomy v1.5 Release](https://executiveoffense.beehiiv.com/p/executive-offense-release-the-arcanum-prompt-injection-taxonomy-v1-5)

**Taxonomy Structure**:
- **13 Attack Intents** (goals): API Enumeration, Attack Users, Business Integrity, Data Poisoning, Denial of Service, Discuss Harm, Generate Image, Get Prompt Secret, Jailbreak, Multi-Chain Attacks, System Prompt Leak, Test Bias, Tool Enumeration
- **18 Attack Techniques** (methods): Act as Interpreter, Anti-Harm Coercion, ASCII, Binary Streams, Cognitive Overload, Contradiction, End Sequences, Framing, Inversion, Link Injection, Memory Exploitation, Meta Prompting, Narrative Smuggling, Puzzling, Rule Addition, Russian Doll, Spatial Byte Arrays, Variable Expansion
- **20 Attack Evasions** (obfuscation): Alt Language, Base64, Case Changing, Cipher, Emoji, Fictional Language, Graph Nodes, Hex, JSON, Link Smuggling, Markdown, Metacharacter Confusion, Morse, Phonetic Substitution, Reverse, Spaces, Splats, Stego, Waveforms, XML

**Additional Resources**:
- **32 Threat Modeling Questions** organized by category (inputs, ecosystem, model, prompts, data, app, pivoting, monitoring)
- **5-Layer Defense Checklist** (Ecosystem, Model, Prompt, Data, Application)
- **Probe Library** for identifying AI-enabled endpoints

### Implementation Guidance

Organizations implementing HAIAMM should:

1. **Start with Threat Assessment**: Use TA-Software, TA-Data, and TA-Processes to understand prompt injection risks specific to your AI security systems

2. **Define Security Requirements**: Implement SR requirements (SR-PI-001 through SR-PI-007) for all LLM integrations

3. **Test Comprehensively**: Use ST-Software testing methodology to validate prompt injection defenses before production deployment

4. **Review Code**: Apply IR-Software code review checklist to all LLM integration code

5. **Track Vulnerabilities**: Use IM-Software vulnerability categories and workflows for ongoing prompt injection issue management

6. **Iterate and Improve**: Quarterly prompt injection testing with Arcanum taxonomy, continuous improvement based on detected patterns

### Benefits of Integrated Prompt Injection Coverage

By integrating the Arcanum PI Taxonomy, HAIAMM provides:

✅ **Complete Attack Surface Coverage**: 13 intents × 18 techniques × 20 evasions = comprehensive understanding
✅ **Industry-Standard Taxonomy**: Aligned with leading prompt injection research
✅ **Actionable Guidance**: Specific requirements, test cases, code review checklists, vulnerability workflows
✅ **Domain-Specific Adaptation**: Software, Data, and Processes domains with tailored examples
✅ **Measurable Success Criteria**: ≥95% detection rates, ≤5% false positives, SLA-based remediation
✅ **Cross-Practice Integration**: TA → SR → ST → IR → IM lifecycle coverage

Organizations following HAIAMM v2.1 will have **industry-leading prompt injection security** for their AI-operated security programs.

---

## Threat Intelligence as Foundational Capability

**NEW IN v2.2**: HAIAMM now integrates threat intelligence as a **foundational capability** (Level 1 maturity) across all six security domains through the Strategy & Metrics (SM) practice, with clear maturity progression from consumption (L1) → analysis and correlation (L2) → production and sharing (L3).

### Why Threat Intelligence is Foundational for AI-Operated Security

AI-operated security systems make thousands of decisions per day - which vulnerabilities to prioritize, which endpoints to quarantine, which cloud configurations to flag, which data access patterns to investigate. **Without threat intelligence, AI security is context-blind:**

**AI Security WITHOUT Threat Intelligence** ❌:
- Prioritizes vulnerabilities by CVSS scores (generic severity, not real-world exploitation)
- Detects anomalies based on baselines (not known-malicious patterns)
- Flags misconfigurations against standards (not active attack techniques)
- Investigates access anomalies (not credential compromise indicators)
- **Result**: High false positives, missed real threats, poor ROI, analyst alert fatigue

**AI Security WITH Threat Intelligence** ✅:
- Prioritizes vulnerabilities actively exploited in wild (CISA KEV, exploit databases)
- Detects known-malicious indicators (IOCs, TTPs, malware signatures)
- Flags misconfigurations actively being exploited (MITRE ATT&CK, cloud security research)
- Investigates credential compromise (dark web monitoring, breach databases)
- **Result**: Informed decisions, reduced false positives, catches real threats, measurable ROI

**Threat Intelligence as "Security Operating System"**: Just as an operating system provides shared context and services to applications, threat intelligence provides shared threat context to all AI security tools. All AI security systems (SAST, EDR, CSPM, DLP, SOAR, vendor risk) benefit from same threat intelligence feeds, creating consistent, context-aware security operations.

### Threat Intelligence Maturity Progression in HAIAMM v2.2

#### Level 1: Foundational Threat Intelligence Consumption

**Objective**: Establish basic threat intelligence consumption to inform AI-operated security decisions from day one.

**Core Activities**:
1. **Identify Domain-Specific Threat Intelligence Requirements** (per domain):
   - **Software**: Vulnerability exploitation intelligence, dependency vulnerability intelligence, code security trends, exploit availability, malicious packages
   - **Infrastructure**: Cloud attack intelligence, infrastructure CVE intelligence, MITRE ATT&CK techniques, configuration baseline intelligence
   - **Endpoints**: Malware intelligence, IOC intelligence (IPs, domains, file hashes), behavioral threat intelligence, vulnerability intelligence
   - **Data**: Data breach intelligence, privacy threat intelligence, data classification intelligence, exfiltration technique intelligence
   - **Processes**: Incident response intelligence, SOAR intelligence, detection evasion intelligence, operational failure intelligence
   - **Vendors**: Vendor breach intelligence, supply chain attack intelligence, vendor vulnerability intelligence, third-party risk intelligence

2. **Integrate Threat Intelligence into AI Security Decision-Making**:
   - **Enrichment Pattern**: Add threat intelligence context to AI security findings
   - **Prioritization Pattern**: Use threat intelligence to rank/prioritize AI findings
   - **Detection Pattern**: Use threat intelligence as detection rules/signatures
   - **Validation Pattern**: Use threat intelligence to validate AI decisions

3. **Measure Basic Threat Intelligence Effectiveness**:
   - **Coverage**: ≥70% of high/critical findings enriched with threat intelligence
   - **Freshness**: ≤24 hours for critical threat intelligence
   - **Actionability**: ≥40% of threat intelligence findings drive AI security action
   - **Detection Improvement**: ≥20% increase in true positive rate after integration

**Free/Open-Source Threat Intelligence Sources (Level 1)**:
- CISA KEV (Known Exploited Vulnerabilities), NVD, GitHub Security Advisories
- MITRE ATT&CK, CIS Benchmarks, Cloud Provider Security Bulletins
- AbuseIPDB, VirusTotal, MISP, AlienVault OTX
- HaveIBeenPwned, Privacy Regulator Databases, Data Breach Notification Sites
- SANS Incident Handler Diary, DFIR Blogs, SOAR Vendor Blogs
- Vendor Breach Databases, Supply Chain Security Research, SBOM Scanners

**Success Criteria (Level 1)**:
- Threat intelligence feeds integrated into ≥80% of AI security tools
- High/critical findings enriched with threat intelligence within ≤1 hour
- Documented evidence that threat intelligence improves AI security decision quality

#### Level 2: Comprehensive Threat Intelligence Analysis and Correlation

**Objective**: Analyze threat intelligence across domains, correlate threats, and optimize AI security based on threat intelligence insights.

**Core Activities**:
1. **Classify Threat Intelligence by Organizational Relevance**:
   - **Critical Threats**: Active exploits in your stack, zero-days in production, APT targeting your profile → Real-time response
   - **High-Relevance Threats**: Vulnerabilities in your stack (not yet exploited), emerging attack techniques → Daily updates, 24-hour response
   - **Medium-Relevance Threats**: General threats with possible applicability → Weekly updates, quarterly review
   - **Low-Relevance Threats**: Unlikely to affect organization → Monthly updates, informational only

2. **Establish Cross-Domain Threat Intelligence Correlation**:
   - **Endpoint ↔ Infrastructure**: Endpoint IOC + Infrastructure attack = Coordinated intrusion
   - **Software ↔ Vendor**: Vendor breach + Dependency vulnerability = Supply chain risk
   - **Data ↔ Processes**: Data breach intelligence + Process intelligence = Active attack
   - **Multi-Domain Reconstruction**: Correlate across all domains to reconstruct full attack chain

3. **Optimize AI Security Tools Based on Threat Intelligence Insights**:
   - **False Positive Reduction**: ≥30% reduction through threat intelligence tuning
   - **Detection Gap Analysis**: ≥90% coverage of critical threats
   - **Adaptive Threat Modeling**: Quarterly threat model updates based on threat intelligence trends
   - **Predictive Threat Hunting**: ≥3 hunting campaigns per quarter based on emerging intelligence

4. **Calculate Threat Intelligence ROI**:
   - **Formula**: (Detection Improvement + False Positive Savings + Breach Prevention + Response Time Improvement - Investment) / Investment
   - **Target**: ≥3:1 ROI (every $1 invested returns $3+ in value)
   - **Metrics**: Prioritization value, false positive savings, detection improvement, response time improvement

**Success Criteria (Level 2)**:
- Threat intelligence classified by relevance with different AI response tiers
- Cross-domain correlation active with ≥85% correlation accuracy
- AI security tools tuned quarterly based on threat intelligence insights
- False positive reduction ≥30%, critical threat coverage ≥90%
- Demonstrable ≥3:1 ROI on threat intelligence investment

#### Level 3: Industry-Leading Threat Intelligence Production and Sharing

**Objective**: Produce original threat intelligence from AI security operations and contribute to industry collective defense.

**Core Activities**:
1. **Produce Original Threat Intelligence from AI Security Operations**:
   - **Anonymized IOC Sharing**: ≥100 novel IOCs per month to industry platforms (MISP, ISACs)
   - **Attack Pattern Documentation**: ≥4 documented attack patterns per year (quarterly)
   - **Vulnerability Research**: ≥2 responsibly disclosed vulnerabilities per year
   - **Threat Trend Analysis**: ≥2 threat trend reports per year (semi-annual)

2. **Participate in Industry Threat Intelligence Sharing Communities**:
   - **Industry ISACs**: Join and contribute to sector-specific ISACs (FS-ISAC, H-ISAC, etc.)
   - **Vendor Partnerships**: Collaborate with security vendors to improve products
   - **Open-Source Platforms**: Contribute to MISP, OpenCTI, STIX/TAXII communities
   - **SLA**: Contribute ≥10 reports per year, consume daily intelligence feeds

3. **Demonstrate Industry Leadership Through Threat Intelligence Innovation**:
   - **Research & Publication**: ≥2 conference presentations or journal publications per year (Black Hat, DEF CON, RSA, academic journals)
   - **Open-Source Contributions**: ≥1 significant open-source project per year with ≥100 GitHub stars
   - **Standards Development**: ≥2 contributions per year to MITRE ATT&CK, OASIS (STIX/TAXII), NIST, ISO/IEC standards
   - **Thought Leadership**: ≥6 blog posts per year, ≥4 podcast/webinar appearances per year

**Success Criteria (Level 3)**:
- Automated threat intelligence production and sharing (≥100 IOCs/month, ≥4 attack patterns/year)
- Active participation in ≥3 threat intelligence sharing communities
- Industry leadership through ≥2 conference presentations or publications per year
- Open-source contributions with community adoption (≥100 GitHub stars)
- Standards development participation (≥2 contributions per year)
- Organization recognized as threat intelligence thought leader

### Comprehensive Coverage Across HAIAMM v2.2

Threat intelligence is now integrated into **Strategy & Metrics (SM) practice for all 6 domains**:

**1. SM-Software**: Vulnerability exploitation intelligence, dependency vulnerability intelligence, code security trend intelligence → Prioritize exploited vulnerabilities, enrich dependency risks, track emerging code threats

**2. SM-Infrastructure**: Cloud attack intelligence, infrastructure CVE intelligence, MITRE ATT&CK for Cloud → Prioritize exploited misconfigurations, enrich infrastructure vulnerabilities, track cloud attack techniques

**3. SM-Endpoints**: Malware intelligence, IOC intelligence, behavioral threat intelligence → Detect ransomware campaigns, hunt for malicious IPs/domains/hashes, identify compromise indicators

**4. SM-Data**: Data breach intelligence, privacy threat intelligence, exfiltration technique intelligence → Monitor credential exposure, track regulatory enforcement, detect data theft patterns

**5. SM-Processes**: Incident response intelligence, SOAR intelligence, detection evasion intelligence → Enrich incident triage, validate automation playbooks, detect process attacks

**6. SM-Vendors**: Vendor breach intelligence, supply chain attack intelligence, third-party risk intelligence → Detect vendor breaches early, prevent supply chain attacks, monitor vendor security posture

### Domain-Specific Threat Intelligence Integration Examples

**Example 1: Software Domain - Dependency Vulnerability Prioritization**
- **Without Threat Intelligence**: AI SCA scanner finds 500 dependency vulnerabilities → Prioritize by CVSS score → Team fixes highest CVSS first (many theoretical vulnerabilities, few real-world exploits)
- **With Threat Intelligence**: AI SCA finds 500 vulnerabilities → Threat intelligence enrichment: 12 have active exploits (CISA KEV), 47 have public PoCs → Prioritize these 59 first → Team fixes exploited vulnerabilities before theoretical ones → **Result**: 80% faster mitigation of real-world risks

**Example 2: Endpoints Domain - Ransomware Detection**
- **Without Threat Intelligence**: AI EDR detects unusual file encryption activity → Flags as suspicious → Analyst investigates manually → 45-minute response time
- **With Threat Intelligence**: AI EDR detects file encryption + Threat intelligence match: Known LockBit ransomware C2 IP + Known TTP (MITRE T1486 Data Encrypted for Impact) → High-confidence ransomware detection → Automated containment triggered → **Result**: <5-minute response, breach prevented

**Example 3: Vendors Domain - Supply Chain Attack Prevention**
- **Without Threat Intelligence**: Vendor security questionnaire completed 6 months ago, no continuous monitoring
- **With Threat Intelligence**: AI vendor monitoring detects vendor breach disclosure (dark web intelligence) → Vendor "Acme Corp" compromised → Your code uses Acme's npm package → AI correlates as supply chain exposure → Immediate security review, dependency update, incident response → **Result**: Supply chain attack prevented through early detection

### Implementation Guidance for Threat Intelligence Integration

Organizations implementing HAIAMM v2.2 threat intelligence capabilities should:

1. **Start with Level 1 Foundational Consumption** (0-6 months):
   - Identify domain-specific threat intelligence requirements
   - Prioritize free/open-source threat intelligence sources to minimize cost barriers
   - Integrate threat intelligence into ≥80% of AI security tools
   - Measure basic effectiveness (coverage, freshness, detection improvement)

2. **Progress to Level 2 Comprehensive Analysis** (6-18 months):
   - Classify threat intelligence by organizational relevance (critical/high/medium/low)
   - Establish cross-domain threat intelligence correlation
   - Optimize AI tools based on threat intelligence insights (reduce false positives, close detection gaps)
   - Calculate and demonstrate threat intelligence ROI (≥3:1 target)

3. **Achieve Level 3 Industry Leadership** (18+ months):
   - Produce original threat intelligence from AI security operations (IOCs, attack patterns, vulnerability research)
   - Participate in industry threat intelligence sharing communities (ISACs, vendor partnerships, open-source)
   - Demonstrate industry leadership (conference presentations, open-source projects, standards development)
   - Contribute to collective defense (anonymized threat sharing, community collaboration)

### Benefits of Integrated Threat Intelligence Coverage in HAIAMM v2.2

✅ **Context-Aware AI Security**: All AI security tools operate with real-world threat context, not just generic risk scores

✅ **Improved Prioritization**: Exploited vulnerabilities, active malware, breached vendors prioritized over theoretical risks

✅ **Reduced False Positives**: Threat intelligence validates AI decisions, reducing noise and alert fatigue

✅ **Faster Threat Response**: Threat intelligence accelerates detection and response (minutes vs. hours/days)

✅ **Measurable ROI**: Clear metrics demonstrate threat intelligence value (≥3:1 ROI target)

✅ **Industry Alignment**: Aligned with industry consensus that threat intelligence is essential for modern security operations

✅ **Progressive Maturity**: Clear path from basic consumption (L1) → comprehensive analysis (L2) → industry leadership (L3)

Organizations following HAIAMM v2.2 will have **industry-leading threat intelligence-driven AI security programs** with measurable ROI, improved security outcomes, and contributions to collective defense.

**Reference**: See Threat-Intelligence-Integration-Analysis.md for comprehensive analysis of threat intelligence integration into HAIAMM, including philosophical rationale, maturity progression details, implementation roadmap, and risk assessment.

---

## Maturity Levels

HAIAMM defines **3 maturity levels** for progressive capability building:

### Level 1: Foundational
**Definition**: Essential practices for minimally viable AI security program

**Characteristics**:
- Core security practices established
- Basic automation with human oversight
- Manual processes for complex decisions
- Reactive security posture
- Individual tool-focused approach

**Typical State**:
- Ad-hoc threat assessment
- Basic security requirements documented
- Security considered late in development
- Limited code review coverage
- Manual vulnerability tracking
- Basic logging and monitoring

**Target**: All organizations starting AI security programs

---

### Level 2: Comprehensive
**Definition**: Advanced practices for mature AI security program

**Characteristics**:
- Proactive security practices
- Extensive automation with safety controls
- Integrated security across lifecycle
- Metrics-driven improvement
- Risk-based prioritization

**Typical State**:
- Systematic threat modeling
- Comprehensive security requirements
- Security integrated early (shift-left)
- Automated code review and testing
- Continuous issue management
- Advanced monitoring and correlation

**Target**: Organizations with 1-2 years AI security maturity

---

### Level 3: Industry-Leading
**Definition**: Cutting-edge practices for AI security leadership

**Characteristics**:
- Continuous security validation
- AI-assisted security operations
- Public transparency and research
- Contribution to industry standards
- Formal verification where applicable

**Typical State**:
- Continuous threat intelligence
- AI-powered security automation
- Formal security proofs
- Public security research
- Open-source contributions
- Security innovation leadership

**Target**: Organizations leading AI security innovation (3+ years maturity)

---

## Effort Estimation

### Estimation Methodology

Based on **OpenSAMM v1.0** approach, effort estimates assume:

**Team Composition**:
- 1 Security Lead (oversight, planning, review)
- 2-3 Security Engineers (implementation, testing, operations)
- 1-2 AI/ML Engineers (model security, adversarial testing)
- Developers (security integration into development workflow)

**Effort Units**: Person-days (1 person-day = 8 hours of focused work)

**Assumptions**:
- Organization has basic security foundation
- Team has AI/ML and security expertise
- Tools and infrastructure available
- Management support secured

### Effort by Maturity Level

| Maturity Level | Initial Setup | Ongoing (Annual) | Description |
|----------------|---------------|------------------|-------------|
| **Level 1** | 180-240 days | 120-180 days | Foundational practices, establish processes |
| **Level 2** | 120-180 days | 90-150 days | Build on Level 1, add advanced capabilities |
| **Level 3** | 90-150 days | 60-120 days | Continuous improvement, innovation |

**Note**: Effort is cumulative (Level 2 assumes Level 1 complete, Level 3 assumes Level 2 complete)

### Effort by Practice (Level 1)

| Practice | Setup (Days) | Ongoing (Days/Year) | Key Activities |
|----------|--------------|---------------------|----------------|
| **Threat Assessment (TA)** | 15-25 | 10-15 | Threat modeling, attack tree analysis, risk assessment |
| **Security Requirements (SR)** | 20-30 | 15-20 | Requirements definition, metrics, validation criteria |
| **Security Architecture (SA)** | 30-45 | 20-30 | Architecture design, review, technology selection |
| **Design Review (DR)** | 15-20 | 20-30 | Design review process, checklists, peer review |
| **Implementation Review (IR)** | 20-30 | 30-45 | Code review process, tools, automated analysis |
| **Security Testing (ST)** | 25-35 | 25-40 | Test strategy, adversarial testing, automation |
| **Issue Management (IM)** | 20-30 | 30-50 | Scanning tools, remediation workflows, tracking |
| **Environment Hardening (EH)** | 25-35 | 15-25 | Baseline configs, access controls, encryption |
| **Monitoring & Logging (ML)** | 25-35 | 20-30 | Log aggregation, SIEM integration, alerting |
| **TOTAL** | **195-285** | **185-285** | |

### Effort by Domain (Level 1)

| Domain | Complexity | Setup Multiplier | Notes |
|--------|------------|------------------|-------|
| **Software** | High | 1.2x | Most complex (AI models, code, pipelines) |
| **Data** | High | 1.2x | Privacy, compliance, classification complexity |
| **Processes** | Medium | 1.0x | Automation safety, human oversight |
| **Infrastructure** | Medium | 1.0x | Multi-cloud, configuration management |
| **Endpoints** | Medium | 1.0x | Cross-platform, performance constraints |
| **Vendors** | Low | 0.8x | Limited control, mainly assessment |

**Example**: Implementing Threat Assessment (TA) for Software domain:
- Base effort: 15-25 days
- Domain multiplier: 1.2x
- **Total: 18-30 days** for TA-Software at Level 1

---

## Security Domains

### 1. Software Domain
**Scope**: AI security systems code (SAST, DAST, models, pipelines, APIs)

**Key Challenges**:
- AI model security (adversarial attacks, poisoning)
- Code vulnerabilities (injection, authentication, crypto)
- Data pipeline security (ETL, labeling, feedback loops)
- Integration security (IDE plugins, CI/CD, APIs)

**AI Technologies**: SAST tools, DAST tools, vulnerability scanning, code analysis models

**One-Pagers**: [TA-Software](practices/TA-Software-OnePager.md) | [SR-Software](practices/SR-Software-OnePager.md) | [SA-Software](practices/SA-Software-OnePager.md) | [DR-Software](practices/DR-Software-OnePager.md) | [IR-Software](practices/IR-Software-OnePager.md) | [ST-Software](practices/ST-Software-OnePager.md) | [IM-Software](practices/IM-Software-OnePager.md) | [EH-Software](practices/EH-Software-OnePager.md) | [ML-Software](practices/ML-Software-OnePager.md)

---

### 2. Infrastructure Domain
**Scope**: Cloud and network security (multi-cloud CSPM, network monitoring)

**Key Challenges**:
- Multi-cloud complexity (AWS, Azure, GCP)
- Configuration drift and misconfiguration detection
- Remediation safety (blast radius, rollback)
- Network security at scale

**AI Technologies**: CSPM platforms, cloud security automation, network anomaly detection

**One-Pagers**: [TA-Infrastructure](practices/TA-Infrastructure-OnePager.md) | [SR-Infrastructure](practices/SR-Infrastructure-OnePager.md) | [SA-Infrastructure](practices/SA-Infrastructure-OnePager.md) | [DR-Infrastructure](practices/DR-Infrastructure-OnePager.md) | [IR-Infrastructure](practices/IR-Infrastructure-OnePager.md) | [ST-Infrastructure](practices/ST-Infrastructure-OnePager.md) | [IM-Infrastructure](practices/IM-Infrastructure-OnePager.md) | [EH-Infrastructure](practices/EH-Infrastructure-OnePager.md) | [ML-Infrastructure](practices/ML-Infrastructure-OnePager.md)

---

### 3. Endpoints Domain
**Scope**: Endpoint security (EDR/XDR with AI behavioral analytics)

**Key Challenges**:
- Cross-platform support (Windows, macOS, Linux, mobile)
- Performance constraints (≤5% CPU, ≤200MB memory)
- Privacy preservation (BYOD, no user content)
- False positive management

**AI Technologies**: EDR/XDR platforms, behavioral analytics, malware detection models

**One-Pagers**: [TA-Endpoints](practices/TA-Endpoints-OnePager.md) | [SR-Endpoints](practices/SR-Endpoints-OnePager.md) | [SA-Endpoints](practices/SA-Endpoints-OnePager.md) | [DR-Endpoints](practices/DR-Endpoints-OnePager.md) | [IR-Endpoints](practices/IR-Endpoints-OnePager.md) | [ST-Endpoints](practices/ST-Endpoints-OnePager.md) | [IM-Endpoints](practices/IM-Endpoints-OnePager.md) | [EH-Endpoints](practices/EH-Endpoints-OnePager.md) | [ML-Endpoints](practices/ML-Endpoints-OnePager.md)

---

### 4. Data Domain
**Scope**: Data security (DLP with AI classification, privacy-preserving ML)

**Key Challenges**:
- Data classification accuracy (≥90% target)
- Privacy preservation (differential privacy, federated learning)
- Regulatory compliance (GDPR, CCPA, HIPAA)
- Exfiltration prevention

**AI Technologies**: DLP platforms, data classification models, privacy-preserving ML

**One-Pagers**: [TA-Data](practices/TA-Data-OnePager.md) | [SR-Data](practices/SR-Data-OnePager.md) | [SA-Data](practices/SA-Data-OnePager.md) | [DR-Data](practices/DR-Data-OnePager.md) | [IR-Data](practices/IR-Data-OnePager.md) | [ST-Data](practices/ST-Data-OnePager.md) | [IM-Data](practices/IM-Data-OnePager.md) | [EH-Data](practices/EH-Data-OnePager.md) | [ML-Data](practices/ML-Data-OnePager.md)

---

### 5. Processes Domain
**Scope**: Security orchestration (SOAR with AI alert triage, playbook automation)

**Key Challenges**:
- Automation safety (blast radius, human oversight)
- Alert triage accuracy (≥95% true positive detection)
- Multi-tool integration (SIEM, EDR, firewall, cloud, ticketing)
- Mean Time to Respond (MTTR) reduction

**AI Technologies**: SOAR platforms, alert triage models, automation orchestration

**One-Pagers**: [TA-Processes](practices/TA-Processes-OnePager.md) | [SR-Processes](practices/SR-Processes-OnePager.md) | [SA-Processes](practices/SA-Processes-OnePager.md) | [DR-Processes](practices/DR-Processes-OnePager.md) | [IR-Processes](practices/IR-Processes-OnePager.md) | [ST-Processes](practices/ST-Processes-OnePager.md) | [IM-Processes](practices/IM-Processes-OnePager.md) | [EH-Processes](practices/EH-Processes-OnePager.md) | [ML-Processes](practices/ML-Processes-OnePager.md)

---

### 6. Vendors Domain
**Scope**: Vendor risk management (AI-powered assessment, SBOM analysis)

**Key Challenges**:
- Scale (thousands of vendors)
- Limited visibility (vendor systems are black boxes)
- Supply chain security (SBOM analysis, transitive dependencies)
- Continuous monitoring (ratings, breaches, vulnerabilities)

**AI Technologies**: Vendor risk platforms, SBOM analysis, supply chain security tools

**One-Pagers**: [TA-Vendors](practices/TA-Vendors-OnePager.md) | [SR-Vendors](practices/SR-Vendors-OnePager.md) | [SA-Vendors](practices/SA-Vendors-OnePager.md) | [DR-Vendors](practices/DR-Vendors-OnePager.md) | [IR-Vendors](practices/IR-Vendors-OnePager.md) | [ST-Vendors](practices/ST-Vendors-OnePager.md) | [IM-Vendors](practices/IM-Vendors-OnePager.md) | [EH-Vendors](practices/EH-Vendors-OnePager.md) | [ML-Vendors](practices/ML-Vendors-OnePager.md)

---

## Security Practices

### Governance Practices

### 1. Strategy & Metrics (SM)
**Purpose**: Establish unified strategic roadmap and measure effectiveness of AI-operated security programs

**Key Activities**:
- Define AI security strategy across all domains (Software, Infrastructure, Endpoints, Data, Processes, Vendors)
- Integrate threat intelligence as foundational capability (consumption, analysis, production)
- Establish metrics for AI security effectiveness (true positive rates, false positive rates, coverage, MTTR)
- Executive sponsorship and governance structure
- ROI measurement and industry benchmarking

**Success Metrics**:
- AI security strategy documented and current (<12 months old)
- Threat intelligence integrated into all 6 domains at Level 1+
- AI security metrics tracked across practice-domain matrix
- Annual ROI reporting to executives/board

**Effort**: 20-30 days setup, 15-25 days/year ongoing

**Domain Coverage**: [Software](practices/SM-Software-OnePager.md) | [Infrastructure](practices/SM-Infrastructure-OnePager.md) | [Endpoints](practices/SM-Endpoints-OnePager.md) | [Data](practices/SM-Data-OnePager.md) | [Processes](practices/SM-Processes-OnePager.md) | [Vendors](practices/SM-Vendors-OnePager.md)

---

### 2. Policy & Compliance (PC)
**Purpose**: Define policies, standards, and ensure regulatory compliance for AI-operated security systems

**Key Activities**:
- Develop AI security policies (acceptable use, data handling, model governance)
- Define security standards and baselines
- Ensure regulatory compliance (GDPR, CCPA, HIPAA, SOX, industry-specific)
- Policy enforcement and compliance monitoring
- Audit preparation and evidence collection

**Success Metrics**:
- AI security policies documented and approved
- 100% compliance with applicable regulations
- Policy violations tracked and remediated
- Annual compliance audits passed

**Effort**: 25-35 days setup, 20-30 days/year ongoing

**Domain Coverage**: [Software](practices/PC-Software-OnePager.md) | [Infrastructure](practices/PC-Infrastructure-OnePager.md) | [Endpoints](practices/PC-Endpoints-OnePager.md) | [Data](practices/PC-Data-OnePager.md) | [Processes](practices/PC-Processes-OnePager.md) | [Vendors](practices/PC-Vendors-OnePager.md)

---

### 3. Education & Guidance (EG)
**Purpose**: Provide security training, awareness, and guidance for teams building and operating AI security systems

**Key Activities**:
- Security awareness training for AI/ML engineers
- Secure AI development training (prompt injection prevention, adversarial ML)
- AI security best practices documentation
- Role-based training (developers, operators, security analysts)
- Continuous learning and knowledge sharing

**Success Metrics**:
- ≥90% of AI/ML engineers completed security training annually
- Security champions program established
- Security best practices documented and accessible
- Training effectiveness measured (pre/post assessments)

**Effort**: 15-25 days setup, 15-20 days/year ongoing

**Domain Coverage**: [Software](practices/EG-Software-OnePager.md) | [Infrastructure](practices/EG-Infrastructure-OnePager.md) | [Endpoints](practices/EG-Endpoints-OnePager.md) | [Data](practices/EG-Data-OnePager.md) | [Processes](practices/EG-Processes-OnePager.md) | [Vendors](practices/EG-Vendors-OnePager.md)

---

### Development Lifecycle Practices

### 4. Threat Assessment (TA)
**Purpose**: Identify and analyze threats specific to AI-operated security systems

**Key Activities**:
- AI-specific threat modeling (adversarial ML, data poisoning, model theft)
- Attack tree analysis
- Abuse case development
- Risk scoring and prioritization

**Success Metrics**:
- 100% of AI systems have threat model
- ≥80% of threats have mitigations
- Threat models updated quarterly

**Effort**: 15-25 days setup, 10-15 days/year ongoing

**Domain Coverage**: [Software](practices/TA-Software-OnePager.md) | [Infrastructure](practices/TA-Infrastructure-OnePager.md) | [Endpoints](practices/TA-Endpoints-OnePager.md) | [Data](practices/TA-Data-OnePager.md) | [Processes](practices/TA-Processes-OnePager.md) | [Vendors](practices/TA-Vendors-OnePager.md)

---

### 5. Security Requirements (SR)
**Purpose**: Define measurable security requirements for AI systems

**Key Activities**:
- Functional security requirements (authentication, authorization, encryption)
- Non-functional requirements (performance, accuracy, latency, privacy)
- Compliance requirements (GDPR, CCPA, HIPAA)
- Acceptance criteria definition

**Success Metrics**:
- 100% of AI systems have documented security requirements
- ≥90% of requirements testable and measurable
- ≥95% of requirements validated before production

**Effort**: 20-30 days setup, 15-20 days/year ongoing

**Domain Coverage**: [Software](practices/SR-Software-OnePager.md) | [Infrastructure](practices/SR-Infrastructure-OnePager.md) | [Endpoints](practices/SR-Endpoints-OnePager.md) | [Data](practices/SR-Data-OnePager.md) | [Processes](practices/SR-Processes-OnePager.md) | [Vendors](practices/SR-Vendors-OnePager.md)

---

### 6. Security Architecture (SA)
**Purpose**: Design secure, scalable architecture for AI security systems

**Key Activities**:
- Architecture design (components, data flows, integrations)
- Technology selection (frameworks, databases, cloud services)
- Security control design (authentication, encryption, access control)
- Scalability and performance design

**Success Metrics**:
- 100% of AI systems have documented architecture
- Architecture reviewed before implementation
- Performance targets met (latency, throughput)

**Effort**: 30-45 days setup, 20-30 days/year ongoing

**Domain Coverage**: [Software](practices/SA-Software-OnePager.md) | [Infrastructure](practices/SA-Infrastructure-OnePager.md) | [Endpoints](practices/SA-Endpoints-OnePager.md) | [Data](practices/SA-Data-OnePager.md) | [Processes](practices/SA-Processes-OnePager.md) | [Vendors](practices/SA-Vendors-OnePager.md)

---

### 7. Design Review (DR)
**Purpose**: Review designs before implementation to catch flaws early

**Key Activities**:
- Peer design review
- Security design review (threat-focused)
- Architecture review (scalability, performance)
- Compliance review (regulatory requirements)

**Success Metrics**:
- 100% of designs reviewed before implementation
- ≥80% of issues caught in design review (before coding)
- Review turnaround ≤5 business days

**Effort**: 15-20 days setup, 20-30 days/year ongoing

**Domain Coverage**: [Software](practices/DR-Software-OnePager.md) | [Infrastructure](practices/DR-Infrastructure-OnePager.md) | [Endpoints](practices/DR-Endpoints-OnePager.md) | [Data](practices/DR-Data-OnePager.md) | [Processes](practices/DR-Processes-OnePager.md) | [Vendors](practices/DR-Vendors-OnePager.md)

---

### 8. Implementation Review (IR)
**Purpose**: Code review to ensure secure implementation

**Key Activities**:
- Peer code review (pull request reviews)
- Security code review (vulnerability-focused)
- Automated code analysis (SAST, linters, dependency scanning)
- Test coverage review

**Success Metrics**:
- 100% of code reviewed before merge
- ≥80% of bugs caught in code review
- ≥90% of security vulnerabilities caught in review
- Review turnaround ≤2 business days

**Effort**: 20-30 days setup, 30-45 days/year ongoing

**Domain Coverage**: [Software](practices/IR-Software-OnePager.md) | [Infrastructure](practices/IR-Infrastructure-OnePager.md) | [Endpoints](practices/IR-Endpoints-OnePager.md) | [Data](practices/IR-Data-OnePager.md) | [Processes](practices/IR-Processes-OnePager.md) | [Vendors](practices/IR-Vendors-OnePager.md)

---

### 9. Security Testing (ST)
**Purpose**: Test AI systems for vulnerabilities and adversarial robustness

**Key Activities**:
- Adversarial testing (evasion, poisoning, model extraction)
- Penetration testing (SAST, DAST, API security)
- Performance testing (latency, throughput, scalability)
- Compliance testing (GDPR, privacy guarantees)

**Success Metrics**:
- ≥80% code coverage for security tests
- ≥90% of vulnerabilities caught in testing
- Adversarial robustness validated
- Performance targets met

**Effort**: 25-35 days setup, 25-40 days/year ongoing

**Domain Coverage**: [Software](practices/ST-Software-OnePager.md) | [Infrastructure](practices/ST-Infrastructure-OnePager.md) | [Endpoints](practices/ST-Endpoints-OnePager.md) | [Data](practices/ST-Data-OnePager.md) | [Processes](practices/ST-Processes-OnePager.md) | [Vendors](practices/ST-Vendors-OnePager.md)

---

### Operations Practices

### 10. Issue Management (IM)
**Purpose**: Continuous vulnerability scanning and remediation

**Key Activities**:
- Dependency scanning (libraries, frameworks, ML packages)
- Code vulnerability scanning (SAST)
- Infrastructure scanning (CSPM, container scanning)
- Remediation tracking (SLA-driven patching)

**Success Metrics**:
- 100% of systems scanned daily
- ≥95% vulnerabilities remediated within SLA (Critical ≤24h, High ≤7d)
- MTTR: Critical ≤24h, High ≤7d, Medium ≤30d

**Effort**: 20-30 days setup, 30-50 days/year ongoing

**Domain Coverage**: [Software](practices/IM-Software-OnePager.md) | [Infrastructure](practices/IM-Infrastructure-OnePager.md) | [Endpoints](practices/IM-Endpoints-OnePager.md) | [Data](practices/IM-Data-OnePager.md) | [Processes](practices/IM-Processes-OnePager.md) | [Vendors](practices/IM-Vendors-OnePager.md)

---

### 11. Environment Hardening (EH)
**Purpose**: Harden deployment environments to reduce attack surface

**Key Activities**:
- Secure baseline configurations (CIS Benchmarks)
- Least privilege access (IAM, RBAC)
- Encryption (at rest, in transit)
- Network segmentation (zero trust, micro-segmentation)

**Success Metrics**:
- ≥95% systems comply with security baselines
- 100% sensitive data encrypted
- ≥90% accounts follow least privilege
- Zero unnecessary public exposure

**Effort**: 25-35 days setup, 15-25 days/year ongoing

**Domain Coverage**: [Software](practices/EH-Software-OnePager.md) | [Infrastructure](practices/EH-Infrastructure-OnePager.md) | [Endpoints](practices/EH-Endpoints-OnePager.md) | [Data](practices/EH-Data-OnePager.md) | [Processes](practices/EH-Processes-OnePager.md) | [Vendors](practices/EH-Vendors-OnePager.md)

---

### 12. Monitoring & Logging (ML)
**Purpose**: Comprehensive logging and monitoring for security, compliance, debugging

**Key Activities**:
- Security event logging (authentication, attacks, anomalies)
- AI model monitoring (accuracy, drift, explainability)
- Performance monitoring (latency, throughput, errors)
- Compliance logging (GDPR, audit trails)

**Success Metrics**:
- 100% of services emit logs
- ≥99% logs delivered to SIEM
- ≥90% attacks detected within ≤5 minutes
- 100% compliance events logged

**Effort**: 25-35 days setup, 20-30 days/year ongoing

**Domain Coverage**: [Software](practices/ML-Software-OnePager.md) | [Infrastructure](practices/ML-Infrastructure-OnePager.md) | [Endpoints](practices/ML-Endpoints-OnePager.md) | [Data](practices/ML-Data-OnePager.md) | [Processes](practices/ML-Processes-OnePager.md) | [Vendors](practices/ML-Vendors-OnePager.md)

---

## Practice-Domain Matrix

### Complete Coverage Matrix (12 × 6 = 72 Practice-Domain Combinations)

| Practice | Software | Infrastructure | Endpoints | Data | Processes | Vendors |
|----------|----------|----------------|-----------|------|-----------|---------|
| **Strategy & Metrics (SM)** | [SM-SW](practices/SM-Software-OnePager.md) | [SM-INF](practices/SM-Infrastructure-OnePager.md) | [SM-EP](practices/SM-Endpoints-OnePager.md) | [SM-DA](practices/SM-Data-OnePager.md) | [SM-PR](practices/SM-Processes-OnePager.md) | [SM-VE](practices/SM-Vendors-OnePager.md) |
| **Policy & Compliance (PC)** | [PC-SW](practices/PC-Software-OnePager.md) | [PC-INF](practices/PC-Infrastructure-OnePager.md) | [PC-EP](practices/PC-Endpoints-OnePager.md) | [PC-DA](practices/PC-Data-OnePager.md) | [PC-PR](practices/PC-Processes-OnePager.md) | [PC-VE](practices/PC-Vendors-OnePager.md) |
| **Education & Guidance (EG)** | [EG-SW](practices/EG-Software-OnePager.md) | [EG-INF](practices/EG-Infrastructure-OnePager.md) | [EG-EP](practices/EG-Endpoints-OnePager.md) | [EG-DA](practices/EG-Data-OnePager.md) | [EG-PR](practices/EG-Processes-OnePager.md) | [EG-VE](practices/EG-Vendors-OnePager.md) |
| **Threat Assessment (TA)** | [TA-SW](practices/TA-Software-OnePager.md) | [TA-INF](practices/TA-Infrastructure-OnePager.md) | [TA-EP](practices/TA-Endpoints-OnePager.md) | [TA-DA](practices/TA-Data-OnePager.md) | [TA-PR](practices/TA-Processes-OnePager.md) | [TA-VE](practices/TA-Vendors-OnePager.md) |
| **Security Requirements (SR)** | [SR-SW](practices/SR-Software-OnePager.md) | [SR-INF](practices/SR-Infrastructure-OnePager.md) | [SR-EP](practices/SR-Endpoints-OnePager.md) | [SR-DA](practices/SR-Data-OnePager.md) | [SR-PR](practices/SR-Processes-OnePager.md) | [SR-VE](practices/SR-Vendors-OnePager.md) |
| **Security Architecture (SA)** | [SA-SW](practices/SA-Software-OnePager.md) | [SA-INF](practices/SA-Infrastructure-OnePager.md) | [SA-EP](practices/SA-Endpoints-OnePager.md) | [SA-DA](practices/SA-Data-OnePager.md) | [SA-PR](practices/SA-Processes-OnePager.md) | [SA-VE](practices/SA-Vendors-OnePager.md) |
| **Design Review (DR)** | [DR-SW](practices/DR-Software-OnePager.md) | [DR-INF](practices/DR-Infrastructure-OnePager.md) | [DR-EP](practices/DR-Endpoints-OnePager.md) | [DR-DA](practices/DR-Data-OnePager.md) | [DR-PR](practices/DR-Processes-OnePager.md) | [DR-VE](practices/DR-Vendors-OnePager.md) |
| **Implementation Review (IR)** | [IR-SW](practices/IR-Software-OnePager.md) | [IR-INF](practices/IR-Infrastructure-OnePager.md) | [IR-EP](practices/IR-Endpoints-OnePager.md) | [IR-DA](practices/IR-Data-OnePager.md) | [IR-PR](practices/IR-Processes-OnePager.md) | [IR-VE](practices/IR-Vendors-OnePager.md) |
| **Security Testing (ST)** | [ST-SW](practices/ST-Software-OnePager.md) | [ST-INF](practices/ST-Infrastructure-OnePager.md) | [ST-EP](practices/ST-Endpoints-OnePager.md) | [ST-DA](practices/ST-Data-OnePager.md) | [ST-PR](practices/ST-Processes-OnePager.md) | [ST-VE](practices/ST-Vendors-OnePager.md) |
| **Issue Management (IM)** | [IM-SW](practices/IM-Software-OnePager.md) | [IM-INF](practices/IM-Infrastructure-OnePager.md) | [IM-EP](practices/IM-Endpoints-OnePager.md) | [IM-DA](practices/IM-Data-OnePager.md) | [IM-PR](practices/IM-Processes-OnePager.md) | [IM-VE](practices/IM-Vendors-OnePager.md) |
| **Environment Hardening (EH)** | [EH-SW](practices/EH-Software-OnePager.md) | [EH-INF](practices/EH-Infrastructure-OnePager.md) | [EH-EP](practices/EH-Endpoints-OnePager.md) | [EH-DA](practices/EH-Data-OnePager.md) | [EH-PR](practices/EH-Processes-OnePager.md) | [EH-VE](practices/EH-Vendors-OnePager.md) |
| **Monitoring & Logging (ML)** | [ML-SW](practices/ML-Software-OnePager.md) | [ML-INF](practices/ML-Infrastructure-OnePager.md) | [ML-EP](practices/ML-Endpoints-OnePager.md) | [ML-DA](practices/ML-Data-OnePager.md) | [ML-PR](practices/ML-Processes-OnePager.md) | [ML-VE](practices/ML-Vendors-OnePager.md) |

**Total**: 54 practice-domain one-pagers

---

## Implementation Roadmap

### Phase 1: Foundation (Months 1-6) - Level 1

**Objective**: Establish essential AI security practices

**Priority Practices**:
1. **Threat Assessment (TA)** - Understand AI-specific threats
2. **Security Requirements (SR)** - Define what "secure" means
3. **Issue Management (IM)** - Start scanning for known vulnerabilities
4. **Monitoring & Logging (ML)** - Gain visibility into AI systems

**Priority Domains**:
1. **Software** - Secure the AI code and models
2. **Data** - Protect sensitive data and ensure privacy

**Key Milestones**:
- Month 1-2: TA and SR for Software and Data domains
- Month 3-4: VM and ML for Software and Data domains
- Month 5-6: Expand to Infrastructure and Endpoints domains

**Effort**: 120-180 person-days

**Success Criteria**:
- Threat models for all AI systems
- Security requirements documented
- Daily vulnerability scanning operational
- Logging to SIEM implemented

---

### Phase 2: Maturity (Months 7-18) - Level 1 Complete + Level 2 Start

**Objective**: Complete Level 1 across all domains, begin Level 2

**Priority Practices**:
1. **Security Architecture (SA)** - Design secure AI systems
2. **Design Review (DR)** - Catch design flaws early
3. **Implementation Review (IR)** - Ensure secure coding
4. **Security Testing (ST)** - Test for vulnerabilities
5. **Environment Hardening (EH)** - Harden deployments

**Priority Domains**: All remaining domains (Processes, Vendors)

**Key Milestones**:
- Month 7-9: SA, DR, IR for all domains
- Month 10-12: ST, EH for all domains
- Month 13-15: Complete Level 1 for all 54 combinations
- Month 16-18: Begin Level 2 for high-priority practices/domains

**Effort**: 180-240 person-days

**Success Criteria**:
- All 54 Level 1 practices implemented
- 100% code review coverage
- Security testing automated
- Environments hardened per baselines

---

### Phase 3: Optimization (Months 19-36) - Level 2

**Objective**: Advanced AI security capabilities

**Focus Areas**:
1. **Automation**: AI-assisted security (automated triage, response)
2. **Integration**: Unified security across lifecycle
3. **Metrics**: Data-driven security improvement
4. **Proactive Security**: Shift-left, continuous validation

**Key Milestones**:
- Month 19-24: Level 2 for Software, Data, Processes domains
- Month 25-30: Level 2 for Infrastructure, Endpoints, Vendors domains
- Month 31-36: Optimization, metrics, continuous improvement

**Effort**: 120-180 person-days

**Success Criteria**:
- ≥70% automation rate for security operations
- ≥90% of bugs caught before production
- Mean time to detect (MTTD) ≤5 minutes
- Mean time to respond (MTTR) ≤10 hours

---

### Phase 4: Leadership (Months 37+) - Level 3

**Objective**: Industry-leading AI security

**Focus Areas**:
1. **Innovation**: AI-powered security, formal verification
2. **Research**: Public security research, contributions
3. **Standards**: Participation in AI security standards
4. **Open Source**: Contribute security tools and frameworks

**Continuous Activities**:
- Security research and publication
- Open-source contributions
- Conference presentations
- Standards body participation

**Effort**: 60-120 person-days/year

---

## Framework Mappings

### ISO/IEC 27001:2022 Mapping

| ISO 27001 Control | HAIAMM Practices | Notes |
|-------------------|------------------|-------|
| **A.5.1 Policies** | TA, SR | Information security policy includes AI security |
| **A.5.7 Threat Intelligence** | TA | AI-specific threat intelligence |
| **A.8.8 Management of Technical Vulnerabilities** | VM | Includes AI model, dependency vulnerabilities |
| **A.8.26 Application Security Requirements** | SR, SA, IR, ST | AI application security |
| **A.8.29 Security Testing** | ST | Includes adversarial testing for AI |
| **A.8.32 Change Management** | IR, ST | AI model, code deployment |

**Coverage**: HAIAMM provides AI-specific implementation of ISO 27001 controls

---

### NIST Cybersecurity Framework 2.0 Mapping

| NIST CSF Function | HAIAMM Practices | Notes |
|-------------------|------------------|-------|
| **GOVERN (GV)** | TA, SR | AI risk management, security strategy |
| **IDENTIFY (ID)** | TA, VM | AI asset inventory, vulnerability discovery |
| **PROTECT (PR)** | SA, EH, IR | Secure AI architecture, hardening |
| **DETECT (DE)** | ML, ST | AI security monitoring, testing |
| **RESPOND (RS)** | VM, ML | Issue remediation, incident response |
| **RECOVER (RC)** | EH, ML | Backup, recovery, resilience |

**Coverage**: HAIAMM implements CSF 2.0 for AI-operated security programs

---

### NIST AI Risk Management Framework Mapping

| NIST AI RMF Function | HAIAMM Practices | Notes |
|----------------------|------------------|-------|
| **GOVERN** | TA, SR | AI governance, accountability |
| **MAP** | TA, SA | AI context, categorization, risk assessment |
| **MEASURE** | ST, ML | AI performance measurement, monitoring |
| **MANAGE** | VM, EH, IR | AI risk treatment, mitigation |

**Coverage**: HAIAMM operationalizes NIST AI RMF for security applications

---

### OWASP SAMM Mapping

| SAMM Practice | HAIAMM Practices | Notes |
|---------------|------------------|-------|
| **Strategy & Metrics** | TA, SR | Security requirements, threat assessment |
| **Policy & Compliance** | SR, EH | Requirements, hardening standards |
| **Education & Guidance** | DR, IR | Code review, design review training |
| **Threat Assessment** | TA | Threat modeling, abuse cases |
| **Security Requirements** | SR | Functional, non-functional requirements |
| **Security Architecture** | SA, DR | Architecture design and review |
| **Design Review** | DR | Architectural risk analysis |
| **Implementation Review** | IR | Code review |
| **Security Testing** | ST | Penetration testing, adversarial testing |
| **Environment Hardening** | EH | Operational environment hardening |
| **Operational Enablement** | ML, VM | Monitoring, issue management |

**Coverage**: HAIAMM extends SAMM with AI-specific practices and domains

---

## Appendices

### Appendix A: Glossary

**AI-Operated Security Program**: Security program using AI for threat detection, response, risk assessment (SAST, DAST, CSPM, EDR, DLP, SOAR)

**Adversarial Machine Learning**: Attacks against AI models (evasion, poisoning, extraction, inversion)

**Blast Radius**: Maximum scope of automated security action (e.g., ≤50 IPs blocked per action)

**Data Poisoning**: Injecting malicious data into training datasets to degrade model performance

**Differential Privacy**: Mathematical privacy guarantee through noise addition (epsilon/delta parameters)

**Federated Learning**: Distributed ML training where data stays on endpoints, only gradients shared

**Model Drift**: Degradation of model accuracy over time due to data distribution changes

**Prompt Injection**: Attack manipulating LLM behavior through malicious prompts embedded in user input, code comments, or documents to bypass security controls, extract sensitive information, or exfiltrate data

**RAG (Retrieval-Augmented Generation)**: LLM architecture pattern where external documents/knowledge bases augment model responses. Vulnerable to knowledge base poisoning if documents aren't validated.

**SBOM**: Software Bill of Materials - list of software components and dependencies

**Zero-Day**: Previously unknown vulnerability with no available patch

---

### Appendix B: References

**Standards & Frameworks**:
- ISO/IEC 27001:2022 - Information Security Management
- ISO/IEC 42001:2023 - AI Management System
- NIST Cybersecurity Framework 2.0 (2024)
- NIST AI Risk Management Framework (2023)
- OWASP SAMM 2.0 - Software Assurance Maturity Model

**AI Security Research**:
- MITRE ATLAS - Adversarial Threat Landscape for AI Systems
- OWASP Top 10 for LLM Applications
- NIST IR 8269 - Taxonomy of Adversarial ML
- **Arcanum Prompt Injection Taxonomy v1.5** by Jason Haddix (CC BY 4.0)
  - GitHub: https://github.com/Arcanum-Sec/arc_pi_taxonomy
  - Publication: [Executive Offense Newsletter](https://executiveoffense.beehiiv.com/p/executive-offense-release-the-arcanum-prompt-injection-taxonomy-v1-5)
  - Comprehensive taxonomy of prompt injection attacks (13 intents, 18 techniques, 20 evasions)
  - 5-layer defense model, 32 threat modeling questions, probe library
  - Integrated into HAIAMM v2.1 TA, SR, ST, IR, IM practices across Software, Data, Processes domains

---

### Appendix C: Tool Categories

**SAST/DAST**: Semgrep, CodeQL, SonarQube, Snyk Code, Checkmarx, Veracode

**CSPM**: Prisma Cloud, Wiz, Orca Security, Aqua CSPM, AWS Security Hub

**EDR/XDR**: CrowdStrike, SentinelOne, Microsoft Defender, Carbon Black

**DLP**: Symantec DLP, Forcepoint DLP, Microsoft Purview, Digital Guardian

**SOAR**: Splunk SOAR, Palo Alto XSOAR, IBM Resilient, Swimlane

**Vendor Risk**: BitSight, SecurityScorecard, RiskRecon, Prevalent, Panorays

---

### Appendix D: Contributors

**HAIAMM Development Team**:
- Framework Design
- Practice Development
- Domain Expertise
- Effort Estimation

**Acknowledgments**:
- OWASP SAMM for maturity model methodology
- NIST for AI and cybersecurity frameworks
- ISO for security management standards
- **Jason Haddix** and the Arcanum Security team for the Arcanum Prompt Injection Taxonomy (CC BY 4.0), which provides comprehensive prompt injection attack coverage integrated into HAIAMM v2.1

---

### Appendix E: Change Log

**Version 2.1 (2025-12-25)**:
- Initial comprehensive handbook release
- 54 practice-domain one-pagers
- Effort estimation methodology
- Framework mappings (ISO 27001, NIST CSF, NIST AI RMF, OWASP SAMM)
- Implementation roadmap
- Complete practice and domain coverage

**Version 2.2 (2025-12-26)**:
- **Threat Intelligence as Foundational Capability**: Integrated threat intelligence as Level 1 foundational requirement across all 6 domains
- **Strategy & Metrics (SM) Practice Enhancement**: Added comprehensive threat intelligence guidance to SM practice for all domains
  - SM-Software: Vulnerability exploitation intelligence, dependency vulnerability intelligence, code security trends
  - SM-Infrastructure: Cloud attack intelligence, infrastructure CVE intelligence, MITRE ATT&CK for Cloud
  - SM-Endpoints: Malware intelligence, IOC intelligence, behavioral threat intelligence
  - SM-Data: Data breach intelligence, privacy threat intelligence, exfiltration technique intelligence
  - SM-Processes: Incident response intelligence, SOAR intelligence, detection evasion intelligence
  - SM-Vendors: Vendor breach intelligence, supply chain attack intelligence, third-party risk intelligence (NEW one-pager created)
- **Threat Intelligence Maturity Progression**:
  - Level 1 (Foundational): Threat intelligence consumption with free/open-source sources (CISA KEV, MISP, VirusTotal, etc.)
  - Level 2 (Comprehensive): Threat intelligence classification, cross-domain correlation, ROI calculation (≥3:1 target)
  - Level 3 (Industry-Leading): Threat intelligence production (≥100 IOCs/month), industry sharing, thought leadership (≥2 presentations/year)
- **Updated Practice One-Pagers**:
  - SM-Software, SM-Infrastructure, SM-Endpoints, SM-Data, SM-Processes: Added threat intelligence sections at all 3 maturity levels
  - SM-Vendors: Created new comprehensive one-pager with integrated threat intelligence guidance
- **Handbook Updates**:
  - New "Threat Intelligence as Foundational Capability" section (200+ lines) with implementation guidance
  - Updated Executive Summary, Table of Contents, Framework Overview
  - Added 3 domain-specific threat intelligence integration examples
  - Reference to Threat-Intelligence-Integration-Analysis.md (comprehensive 23-page analysis document)
- **Philosophical Shift**: Threat intelligence elevated from "advanced capability" (L2/3) to "foundational capability" (L1) across all domains
- **Benefits**: Context-aware AI security, improved prioritization, reduced false positives (≥30%), faster response, measurable ROI

**Version 2.1.1 (2025-12-26)**:
- **Prompt Injection Security Integration**: Added comprehensive prompt injection guidance across 6 practices (TA, SR, ST, IR, IM, SA) in Software, Data, and Processes domains
- **Arcanum PI Taxonomy Integration**: Integrated Arcanum Prompt Injection Taxonomy v1.5 by Jason Haddix (CC BY 4.0)
  - 13 Attack Intents (System Prompt Leak, Jailbreak, Data Exfiltration, Tool Enumeration, etc.)
  - 18 Attack Techniques (Role-Playing, Cognitive Overload, Nested Injection, Memory Exploitation, etc.)
  - 20 Attack Evasions (Encoding, Language variations, Format-based, Obfuscation, etc.)
  - 5-Layer Defense Model (Ecosystem, Model, Prompt, Data, Application)
- **Updated Practice One-Pagers**:
  - TA-Software, TA-Data, TA-Processes: Added comprehensive prompt injection threat categories
  - SR-Software, SR-Data, SR-Processes: Added prompt injection prevention requirements (SR-PI-001 through SR-PI-008)
  - ST-Software: Added detailed prompt injection testing methodology
  - IR-Software: Added LLM integration code review checklist
  - IM-Software: Added 8 prompt injection vulnerability categories with remediation workflows
- **Handbook Updates**:
  - New "Prompt Injection Security" section with implementation guidance
  - Updated Executive Summary, Table of Contents
  - Added prompt injection glossary terms, references, acknowledgments
- **Attribution**: All integrated content properly attributed to Arcanum PI Taxonomy (CC BY 4.0)

---

## Document Information

- **Document**: HAIAMM Comprehensive Handbook
- **Version**: 2.2
- **Last Updated**: 2025-12-26
- **Status**: Published
- **License**: Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Third-Party Attributions**: Arcanum Prompt Injection Taxonomy v1.5 by Jason Haddix (CC BY 4.0)
- **Contact**: [To be added]
- **Website**: [To be added]

---

**End of HAIAMM Handbook v2.2**
