# Policy & Compliance (PC)
## Vendors Domain - HAIAMM v2.0

---

### Practice Overview

**Objective:** Establish and maintain policies governing HAI vendor security and demonstrate compliance with third-party risk management requirements

**Description:** Build and maintain policies, standards, and compliance programs that govern how AI agents operate vendor security and third-party risk management functions. Ensure AI-driven vendor security decisions (vendor risk assessments, continuous monitoring, security questionnaire analysis, supply chain threat detection) are auditable, defensible, and meet regulatory and contractual third-party risk requirements.

**Context:** Organizations must establish clear policies for AI agents that manage vendor security - defining acceptable AI autonomy for vendor risk scoring, security assessment automation, and supply chain threat detection. Auditors, regulators, and customers scrutinize third-party risk management, requiring documented policies, justification for vendor approval decisions, and evidence that HAI vendor security balances risk mitigation with business enablement.

---

## Maturity Level 1
### Objective: Establish foundational policies for HAI vendor security and third-party risk management

At this level, organizations create initial policies governing AI agent operations in vendor security and identify applicable compliance and contractual requirements for third-party risk.

#### Activities

**A) Establish policies for AI agent operations in vendor security and third-party risk management**

Create foundational policies that define acceptable use of AI agents for vendor security operations. Document what AI agents can and cannot do autonomously regarding vendor risk assessment, security questionnaire analysis, continuous monitoring, and supply chain threat detection.

Initial policy elements:
- **AI Agent Scope**: Define which vendor security functions AI agents may perform (vendor discovery, security questionnaire pre-analysis, risk scoring, contract review for security clauses, continuous security monitoring of vendors)
- **Vendor Decision Boundaries**: Specify what vendor decisions AI can make autonomously vs. requiring human approval (AI can pre-score vendor risk, humans must approve vendor onboarding for critical/high-risk vendors)
- **Supply Chain Risk Policies**: Define AI's role in software supply chain security (AI can scan dependencies for vulnerabilities, AI monitors open-source libraries, AI detects malicious packages)
- **Data Sharing with Vendors**: Policies governing AI vendor tools that process organizational data (vendor DPAs required, data residency requirements, approved vendor AI tools list)
- **Vendor Classification**: Establish vendor risk tiers with different AI oversight requirements (critical vendors require enhanced due diligence, low-risk vendors allow more AI autonomy)
- **Audit Trail Requirements**: Require logging of all AI vendor security decisions (vendor risk assessments, approval recommendations, security findings, questionnaire analysis)

Example policy statements:
- "AI agents may autonomously analyze vendor security questionnaires and pre-score vendor risk, but human vendor risk committee must approve all critical vendor onboarding decisions"
- "AI supply chain scanning must analyze all software dependencies before deployment, blocking known malicious packages automatically"
- "All AI vendor risk scoring decisions must be explainable and logged for audit purposes"
- "SaaS AI security tools (CASB, SSPM, SCA) must have executed DPAs and comply with data residency requirements before deployment"

**B) Identify and document third-party risk compliance and contractual requirements**

Inventory applicable regulatory frameworks, industry standards, and contractual obligations that govern third-party risk management, and identify specific requirements that apply when AI agents operate vendor security functions.

Compliance framework identification:
- **Regulatory Requirements**: GDPR Article 28 (processor requirements), HIPAA Business Associate requirements, PCI-DSS Requirement 12.8 (service provider management), FFIEC vendor management guidance
- **Industry Standards**: SOC 2 vendor management controls, ISO 27001 A.15 supplier relationships, NIST CSF Third-Party Risk Management
- **Contractual Obligations**: Customer vendor security requirements (banks, healthcare, government requiring vendor due diligence), MSA security commitments, insurance policy requirements
- **Supply Chain Standards**: NIST SSDF (Secure Software Development Framework), EO 14028 SBOM requirements, SLSA supply chain levels

Document third-party risk requirements specific to HAI vendor security:
- **Vendor Due Diligence**: Does AI vendor assessment meet due diligence requirements (SOC 2 Type II requirement for vendor reviews, customer contractual vendor security requirements)?
- **Subprocessor Management**: Does AI support GDPR Article 28 subprocessor notification and approval requirements?
- **Continuous Monitoring**: Does AI continuous vendor monitoring meet regulatory expectations (FFIEC ongoing monitoring, PCI-DSS annual vendor reviews)?
- **Supply Chain Transparency**: Can AI provide required supply chain transparency (SBOM generation, dependency tracking, license compliance)?
- **Vendor Incident Response**: How does AI support vendor breach notification requirements (GDPR Article 33, HIPAA breach notification)?

---

## Maturity Level 2
### Objective: Implement comprehensive vendor risk policies with continuous monitoring and supply chain security

At this level, organizations enforce detailed policies for AI vendor security with vendor classification-based governance, and regularly validate third-party risk management effectiveness through assessments and audits.

#### Activities

**A) Implement vendor classification-based policies with supply chain security governance**

Expand foundational policies into comprehensive vendor risk governance framework that specifies AI requirements, due diligence procedures, and continuous monitoring for different vendor risk classifications.

Comprehensive policy components:
- **Vendor Risk Classification Policies**: Detailed policies for each vendor tier (critical/high/medium/low) specifying AI assessment depth, human oversight requirements, reassessment frequency
- **Security Questionnaire Automation**: AI-assisted questionnaire analysis with validation rules (AI flags inconsistencies, auto-scores standardized questions, escalates concerning responses)
- **Contract Review Automation**: AI reviews vendor contracts for required security clauses (data protection provisions, breach notification SLAs, audit rights, liability limitations)
- **Fourth-Party Risk**: Policies for managing vendor's vendors (subprocessor approval workflows, fourth-party security requirements, AI monitoring of subprocessor changes)
- **Vendor Onboarding Workflow**: Documented AI-human workflow for vendor approval (AI pre-assessment → security review → vendor risk committee → ongoing monitoring)
- **Vendor Offboarding**: Policies for secure vendor termination (AI validates data deletion, access revocation, contract closure)

Supply chain security governance:
- **Software Composition Analysis (SCA)**: AI scans all dependencies for vulnerabilities and malicious code (open-source libraries, commercial components, transitive dependencies)
- **SBOM Requirements**: Require vendors provide SBOMs (Software Bill of Materials), AI analyzes for risks
- **Package Repository Security**: AI monitors internal package repositories for supply chain attacks (typosquatting, dependency confusion, malicious updates)
- **Vendor Compromise Detection**: AI detects vendor breach indicators (unusual data access patterns, credential compromise, supply chain attacks)
- **License Compliance**: AI validates open-source license compliance (GPL contamination risks, incompatible licenses, licensing obligations)

**B) Conduct regular vendor security validation and third-party risk audits**

Establish regular vendor security validation processes including AI-assisted audits, penetration testing of vendor integrations, and continuous monitoring of vendor security posture.

Vendor validation activities:
- **Vendor Security Reviews**: Quarterly reviews of critical vendor security posture (AI analyzes vendor SOC 2 reports, security certifications, vulnerability disclosures)
- **Vendor Performance Metrics**: Monthly tracking of vendor security metrics (SLA compliance, incident response times, security finding remediation velocity)
- **Vendor Audit Evidence**: AI collects and organizes vendor audit evidence (SOC 2 reports, ISO 27001 certificates, penetration test results, security questionnaires)
- **Vendor Integration Testing**: Annual security testing of vendor integrations (API security, data flow analysis, privilege escalation risks)
- **Vendor Breach Simulation**: Tabletop exercises for vendor breach scenarios (how would we respond to vendor ransomware, vendor data breach, vendor outage?)

Third-party risk audits:
- **Internal Vendor Audits**: Quarterly internal reviews of vendor risk management program (sample AI vendor assessments, validate policy adherence, review vendor approval decisions)
- **Vendor Reassessment**: Annual or triggered reassessment of vendors (AI monitors for vendor security incidents, compliance lapses, ownership changes requiring reassessment)
- **Vendor Concentration Risk**: AI analyzes vendor concentration (single vendor failures, geographic concentration, shared infrastructure risks)
- **Vendor Exit Risk**: Assessment of switching costs and vendor lock-in (can we replace critical vendor if needed?)

---

## Maturity Level 3
### Objective: Demonstrate continuous vendor compliance monitoring and lead supply chain security standards

At this level, organizations achieve continuous vendor risk monitoring, automated supply chain threat detection, and contribute to industry third-party risk and supply chain security standards.

#### Activities

**A) Implement continuous vendor risk monitoring with automated supply chain threat intelligence**

Deploy automated vendor risk monitoring that continuously validates vendor security posture and supply chain integrity, with real-time threat detection and automated risk scoring updates.

Continuous vendor monitoring capabilities:
- **Real-Time Vendor Risk Dashboards**: Live visibility into vendor security posture (vendor risk score trends, security incidents at vendors, compliance status, contract renewal dates)
- **Automated Vendor Security Intelligence**: Continuous collection of vendor security signals (breach disclosures, vulnerability announcements, dark web mentions, security rating changes from third-party services)
- **Supply Chain Threat Intelligence**: AI monitors supply chain for threats (malicious package detection, dependency vulnerabilities, supply chain attack indicators, compromised vendor credentials)
- **Vendor Security Scoring**: Continuous AI risk scoring based on multiple signals (security questionnaires, certifications, breach history, security ratings, financial health)
- **Automated Vendor Alerts**: Immediate notification when vendor risk changes (vendor breached, SOC 2 report expired, critical vulnerability in vendor product, vendor acquired by higher-risk entity)
- **Predictive Vendor Risk**: AI predicts vendor security failures before they occur (vendor showing concerning patterns, financial distress indicators, security program degradation)

Advanced supply chain security:
- **Continuous SBOM Analysis**: Real-time analysis of software bill of materials (new vulnerable components, malicious dependency injection, license violations)
- **Build Provenance Verification**: Validate software supply chain integrity (SLSA compliance, build attestations, reproducible builds)
- **Dependency Graph Analysis**: AI maps entire dependency tree (transitive dependencies, dependency confusion risks, abandoned packages)
- **Supply Chain Attack Detection**: Detect supply chain compromises in real-time (unusual package updates, compromised developer accounts, malicious commits)
- **Zero Trust Vendor Access**: Implement zero trust for vendor access (just-in-time access, continuous verification, least privilege for vendor accounts)

**B) Lead development of third-party risk and supply chain security AI standards**

Engage with industry groups, regulators, and supply chain security initiatives to shape HAI vendor security standards, with focus on explainability, vendor privacy, and supply chain transparency.

Industry engagement activities:
- **Standards Development**: Participate in third-party risk standards for AI (ISO 27001 A.15 AI guidance, NIST supply chain risk management for AI, SBOM standards development)
- **Supply Chain Security Leadership**: Contribute to supply chain security initiatives (OpenSSF, SLSA framework, SBOM tooling, package repository security standards)
- **Vendor Assessment Standardization**: Advocate for standardized vendor security assessments (common questionnaire frameworks, reduce vendor assessment fatigue, shared vendor assessments)
- **AI Vendor Risk Benchmarking**: Lead industry benchmarking of AI vendor risk practices (vendor risk maturity, assessment effectiveness, supply chain security posture)
- **Vendor Transparency Standards**: Advocate for vendor security transparency (vendor security scorecards, public breach disclosure timelines, security program visibility)

Emerging vendor risk practices:
- **Vendor Security Scorecards**: Implement transparent vendor security ratings (objective criteria, regular updates, vendor appeals process)
- **Shared Vendor Assessments**: Participate in shared assessment programs (CAIQ, SIG questionnaires, industry consortiums to reduce duplicate vendor assessments)
- **Vendor Security Incentives**: Tie vendor contract terms to security performance (security SLAs with penalties, security improvement incentives, breach liability provisions)
- **Supply Chain Risk Sharing**: Industry collaboration on supply chain threats (shared threat intel on malicious packages, coordinated vulnerability disclosure, supply chain incident response)
- **Ethical AI Vendor Practices**: Ensure AI vendor assessments are fair (avoid discriminatory vendor scoring, transparency in AI risk decisions, vendor right to explanation)

Value of vendor security leadership:
- Influence vendor security standards (shape requirements vendors must meet)
- Reduce vendor assessment burden (shared assessments, standardized frameworks)
- Improve supply chain security (industry-wide threat sharing, coordinated response)
- Competitive advantage (superior vendor risk management capabilities)
- Customer trust (demonstrate mature third-party risk program)

---

## Key Success Indicators

**Level 1:**
- Written policies exist governing AI agent operations in vendor security and third-party risk management
- Compliance and contractual requirements documented and mapped to AI vendor security functions
- Vendor classification framework defined with different AI oversight levels
- Basic audit trail capability (AI vendor security decisions are logged)

**Level 2:**
- Comprehensive vendor classification-based policies implemented with supply chain security governance
- Regular vendor validation conducted (quarterly security reviews, annual vendor audits, vendor integration testing)
- AI-assisted vendor security questionnaire analysis with human validation implemented
- Software Composition Analysis (SCA) deployed for supply chain security
- Vendor security successfully passes compliance audits (SOC 2 vendor management, ISO 27001 A.15, customer audits)

**Level 3:**
- Continuous vendor risk monitoring deployed with real-time vendor security dashboards
- Automated supply chain threat intelligence with SBOM analysis and dependency scanning
- Published contributions to third-party risk and supply chain security standards
- Active participation in shared vendor assessment programs and supply chain security initiatives
- Zero critical vendor risk findings in external audits or customer assessments

---

## Common Pitfalls

**Level 1:**
- ❌ Policies focus on vendor contracts not vendor security (legal compliance without security substance)
- ❌ Vendor classification too simple (all vendors treated same regardless of risk, criticality, or data access)
- ❌ No supply chain security consideration (focus only on direct vendors, ignore software dependencies)
- ❌ Audit trail incomplete (logs show vendor approved but not AI risk assessment rationale)
- ❌ Vendor policies created in isolation (not aligned with procurement, legal, business stakeholders)

**Level 2:**
- ❌ Vendor assessments are point-in-time only (no continuous monitoring, risk changes between annual reviews)
- ❌ Security questionnaires are checkbox exercises (vendors copy-paste answers, no validation, AI analysis ignored)
- ❌ Supply chain scanning generates noise (too many low-severity dependency findings, teams ignore alerts)
- ❌ Fourth-party risk ignored (don't monitor vendor's vendors, subprocessor risks unmanaged)
- ❌ Vendor offboarding neglected (no process to ensure data deletion, access revocation when vendor relationship ends)

**Level 3:**
- ❌ Continuous monitoring creates alert fatigue (too many vendor risk alerts, teams ignore signals)
- ❌ Automated vendor scoring lacks explainability (can't explain to vendors why they scored poorly, vendors dispute AI decisions)
- ❌ Supply chain threat intel is reactive not proactive (detect attacks after exploitation, not before)
- ❌ Industry engagement is performative (join standards bodies but don't implement recommendations)
- ❌ Over-reliance on third-party security ratings (trust external ratings without validation, ratings miss critical risks)

---

## Practice Maturity Questions

**Level 1:**
1. Do you have documented policies governing how AI agents operate vendor security and third-party risk management functions?
2. Have you identified and documented compliance requirements (GDPR Article 28, HIPAA BAA, PCI-DSS 12.8, SOC 2) that apply to HAI vendor security?
3. Is a vendor classification framework defined with different AI oversight requirements based on vendor risk and criticality?

**Level 2:**
1. Are comprehensive vendor classification-based policies implemented with supply chain security governance (SCA, SBOM, dependency scanning)?
2. Do you conduct regular vendor validation (quarterly security reviews, annual audits, vendor integration testing) with AI assistance?
3. Are fourth-party risks (vendor's vendors, subprocessors) managed with AI monitoring and approval workflows?

**Level 3:**
1. Do you have continuous vendor risk monitoring with real-time visibility into vendor security posture and supply chain threats?
2. Is automated supply chain threat intelligence deployed with SBOM analysis, dependency scanning, and malicious package detection?
3. Does your organization actively contribute to third-party risk and supply chain security standards development and participate in shared assessment programs?

---

## Compliance & Third-Party Risk Considerations

HAI vendor security must address specific regulatory and contractual requirements:

### GDPR (EU General Data Protection Regulation)
- **Article 28**: Processor requirements - Vendor DPAs required, vendor security obligations documented
- **Article 28(2)**: Subprocessor approval - AI monitors subprocessor changes, approval workflows implemented
- **Article 28(3)(h)**: Vendor audit rights - Contracts include audit rights, AI facilitates vendor audits
- **Article 33**: Vendor breach notification - Vendors must notify within 24 hours, AI monitors vendor breaches

### HIPAA (Healthcare)
- **Business Associate Agreements**: AI validates vendor BAAs executed before PHI access
- **§164.314(a)(2)(i)**: Subcontractor agreements - Chain of BAAs for vendor's vendors
- **§164.308(b)(1)**: Written contracts - AI reviews vendor contracts for required HIPAA provisions
- **Vendor breach notification**: Vendors must report PHI breaches, AI tracks vendor breach notifications

### PCI-DSS (Payment Card Industry)
- **Requirement 12.8**: Service provider management - Maintain list of vendors with cardholder data access
- **Requirement 12.8.2**: Written agreements - Vendors acknowledge PCI-DSS responsibility
- **Requirement 12.8.4**: Vendor PCI-DSS monitoring - AI monitors vendor PCI-DSS compliance status
- **Requirement 12.8.5**: Information maintenance - Maintain records of vendor PCI-DSS compliance

### SOC 2 Type II (Service Organizations)
- **CC9.2**: Vendor risk management - Policies and procedures for vendor risk assessment
- **CC9.2**: Vendor monitoring - Ongoing monitoring of vendor performance and security
- **Subservice organizations**: Carve-out vs. inclusive approach, AI tracks vendor SOC 2 reports

### Supply Chain Security Standards
- **NIST SSDF**: Secure Software Development Framework for vendor software
- **EO 14028**: SBOM requirements for federal software procurement
- **SLSA**: Supply chain levels for software artifacts (build provenance, integrity verification)
- **ISO 27036**: Security in supplier relationships

Organizations must ensure AI vendor security operations meet third-party risk regulatory requirements, contractual obligations, and supply chain security standards with appropriate audit trails and continuous monitoring.

---

**Document Version:** HAIAMM v2.0
**Practice:** Policy & Compliance (PC)
**Domain:** Vendors
**Last Updated:** December 2025
**Author:** Verifhai
