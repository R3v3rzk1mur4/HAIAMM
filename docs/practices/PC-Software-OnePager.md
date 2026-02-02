# Policy & Compliance (PC)
## Software Domain - HAIAMM v2.0

---

### Practice Overview

**Objective:** Establish and maintain policies governing AI-operated software security and demonstrate compliance with secure development requirements

**Description:** Build and maintain policies, standards, and compliance programs that govern how AI agents operate software security functions. Ensure AI-driven software security decisions (code vulnerability detection, automated security testing, AI-assisted code review, security gate enforcement) are auditable, accurate, and meet regulatory and development governance requirements.

**Context:** Organizations must establish clear policies for AI agents that secure software development - defining acceptable AI autonomy for code scanning, security test automation, and deployment gate enforcement. Auditors and development leadership scrutinize AI software security decisions that impact development velocity, requiring documented policies, justification for security findings, and evidence that AI-operated software security balances security rigor with development efficiency.

---

## Maturity Level 1
### Objective: Establish foundational policies for AI-operated software security

At this level, organizations create initial policies governing AI agent operations in software security and identify applicable compliance and secure development requirements.

#### Activities

**A) Establish policies for AI agent operations in software security**

Create foundational policies that define acceptable use of AI agents for software security operations. Document what AI agents can and cannot do autonomously regarding code vulnerability detection, security testing, code review, and deployment gate enforcement.

Initial policy elements:
- **AI Agent Scope**: Define which software security functions AI agents may perform (SAST/DAST scanning, SCA dependency analysis, security testing, AI code review, security gate enforcement in CI/CD)
- **Deployment Gate Authority**: Specify what security decisions AI can make autonomously vs. requiring override (AI can fail builds for critical vulnerabilities, developers can override low-severity findings with justification)
- **Finding Quality Standards**: Define accuracy requirements for AI security findings (AI SAST must maintain <20% false positive rate, AI security findings must be actionable)
- **Developer Experience Policies**: Require AI security tools integrate cleanly into development workflow (AI provides findings in IDE, PR comments, CI/CD pipeline - not separate tools developers must check)
- **Security vs. Velocity Balance**: Define acceptable security gate impact (AI security checks must complete in <10 minutes, cannot block all deployments - risk-based approach)
- **Audit Trail Requirements**: Require logging of all AI software security decisions (vulnerabilities detected, security gate decisions, developer overrides with justification)

Example policy statements:
- "AI SAST/DAST tools may autonomously scan all code commits but require security team review before blocking production deployments for non-critical findings"
- "AI-detected critical vulnerabilities (SQL injection, RCE, authentication bypass) automatically fail CI/CD builds; developers may not override without AppSec approval"
- "All AI security findings must include remediation guidance; findings without actionable fix recommendations will not block deployments"
- "AI security gate failures must be logged with vulnerability details and developer response (fixed, risk accepted, false positive) for audit purposes"

**B) Identify and document compliance and secure development requirements**

Inventory applicable regulatory frameworks and secure development standards that govern software security, and identify specific requirements that apply when AI agents operate software security functions.

Compliance framework identification:
- **Secure Development Standards**: OWASP ASVS, NIST SSDF (Secure Software Development Framework), ISO 27034 (Application Security)
- **Regulatory Requirements**: PCI-DSS Requirement 6 (Secure Development), HIPAA §164.308(a)(8) (Evaluation), SOX controls for financial application security
- **Industry Frameworks**: BSIMM, SAMM, Building Security In Maturity Model (BSIMM)
- **Customer Requirements**: Vendor security questionnaires requiring secure development evidence

Document compliance requirements specific to AI-operated software security:
- **Vulnerability Scanning**: Does AI code scanning meet mandatory scanning requirements (PCI-DSS Requirement 6.3.2 code review, HIPAA risk analysis)?
- **Security Testing**: Does AI security testing meet testing requirements (OWASP ASVS verification, penetration testing standards)?
- **Code Review**: Does AI code review satisfy secure development requirements (two-person review, security-focused review)?
- **Remediation**: Does AI support timely vulnerability remediation (PCI-DSS Requirement 6.2 patching timelines)?
- **Audit Evidence**: Can you demonstrate to auditors that AI software security is effective (vulnerability trends, false positive rates, remediation times)?

---

## Maturity Level 2
### Objective: Implement comprehensive software security policies with application risk-based governance

At this level, organizations enforce detailed policies for AI software security with application-specific requirements, and regularly validate effectiveness through security testing and developer feedback.

#### Activities

**A) Implement application risk-based policies with developer experience governance**

Expand foundational policies into comprehensive software security governance framework that specifies AI requirements, quality standards, and developer workflows for different application risk levels.

Comprehensive policy components:
- **Application Risk Classification Policies**: Detailed policies for each application tier (critical/high/medium/low) specifying AI scanning depth, security gate strictness, review requirements
- **Technology Stack Policies**: Different AI tool selection for different tech stacks (AI tools with proven effectiveness for Java/C# may differ from Python/JavaScript tools)
- **Security Finding Severity Policies**: Clear criteria for vulnerability severity with corresponding actions (critical = block deployment + immediate fix, high = fix within sprint, medium/low = backlog)
- **False Positive Handling**: Documented procedures for developers to report and resolve false positives (false positive report form, AppSec team SLA for review, AI tool tuning based on feedback)
- **Developer Training Requirements**: Require training on AI security tools and secure coding (developers must understand AI findings to remediate effectively)
- **Remediation SLA Policies**: Define time limits for fixing AI-detected vulnerabilities based on severity (critical within 24 hours, high within 7 days, medium within 30 days)

Developer experience governance:
- **Tool Integration Requirements**: AI security tools must integrate into developer workflow (IDE plugins, PR checks, CI/CD stages - not standalone portals)
- **Finding Presentation Standards**: AI findings must be developer-friendly (clear descriptions, remediation examples, links to secure coding guidance)
- **Override Procedures**: Documented, auditable process for developers to override AI findings (justification required, AppSec review for critical findings)
- **Feedback Mechanisms**: Developers can report tool friction, false positives, or missing features (continuous improvement of AI security tools)

**B) Conduct regular software security validation and penetration testing including AI tools**

Establish regular validation processes for AI software security effectiveness, including penetration testing of applications scanned by AI and validation of AI detection accuracy.

Validation activities:
- **Vulnerability Detection Validation**: Quarterly testing of AI security tool effectiveness (inject known vulnerabilities, measure AI detection rates, validate true positive rates)
- **False Positive Audits**: Monthly review of AI false positives (sample developer-reported false positives, tune AI tools to reduce noise)
- **Penetration Testing**: Include review of AI security findings in penetration tests (did pentesters find vulnerabilities AI missed? Did AI generate false positives pentesters disproved?)
- **Benchmark Testing**: Annual benchmark of AI security tools against standard test suites (OWASP Benchmark, NIST SAMATE, vendor-neutral comparisons)
- **Developer Satisfaction Surveys**: Regular surveys on AI security tool usefulness and friction (track developer satisfaction trends, identify tool improvements)

Security testing validation:
- **AI Tool Efficacy**: Validate AI security tools detect vulnerabilities before production (track how many production incidents involved vulnerabilities AI should have detected)
- **Coverage Validation**: Ensure AI security tools achieve required code coverage (verify SAST/DAST scan all application components)
- **AI vs. Manual Comparison**: Periodically compare AI findings to manual security review (understand AI strengths and gaps)

---

## Maturity Level 3
### Objective: Demonstrate continuous software security compliance and lead secure development AI standards

At this level, organizations achieve continuous software security validation, automated security gate enforcement with quality controls, and contribute to industry secure development AI standards.

#### Activities

**A) Implement continuous security validation with AI-assisted remediation**

Deploy continuous software security validation that monitors AI tool effectiveness in real-time, with AI-assisted vulnerability remediation to accelerate secure development.

Continuous validation capabilities:
- **Real-Time Security Dashboards**: Live visibility into software security posture (vulnerability density trends, AI finding accuracy, remediation velocity, security gate pass rates)
- **Automated Effectiveness Testing**: Continuous validation of AI security tool detection (daily injection of test vulnerabilities, automated measurement of AI detection rates)
- **Trend Analysis**: Track software security trends over time (vulnerability density decreasing? False positive rate improving? Remediation time reducing?)
- **AI-Assisted Remediation**: AI tools suggest or auto-apply security fixes (GitHub Copilot Autofix, AI-generated patches with developer review)
- **Security Regression Detection**: AI detects when code changes re-introduce previously fixed vulnerabilities
- **Automated Security Evidence**: Continuous generation of compliance evidence (vulnerability scan results, remediation records, security testing reports)

AI-assisted secure development:
- **Proactive Security Guidance**: AI provides security recommendations during coding (IDE suggestions for secure patterns, real-time vulnerability detection as code is written)
- **Automated Security Testing**: AI generates and executes security test cases based on code changes
- **Intelligent Finding Prioritization**: AI prioritizes remediation based on exploitability, business impact, and attack surface
- **Security Debt Tracking**: AI helps manage security technical debt (track unresolved findings, predict security debt accumulation)

**B) Lead development of AI secure development standards and explainable AI security findings**

Engage with secure development community and standards bodies to shape AI software security standards, with focus on AI finding accuracy, explainability, and developer productivity.

Industry engagement activities:
- **Standards Development**: Participate in secure development standards for AI (OWASP AI security tools guidance, NIST SSDF AI integration, IEEE secure development standards)
- **AI Tool Benchmarking**: Contribute to and use independent AI security tool benchmarks (support vendor-neutral tool comparisons)
- **Explainable AI Findings**: Advocate for and implement explainable AI security findings (developers can understand WHY AI flagged code, not just THAT it flagged code)
- **Open-Source Security Tools**: Contribute to open-source AI security tools (OWASP projects, community security scanners, shared vulnerability datasets)
- **Developer-Friendly AI**: Shape AI security tools to enhance not obstruct developer productivity (push vendors for better UX, lower false positive rates, actionable remediation)

Secure development AI standards:
- **Finding Quality Standards**: Establish industry standards for AI security finding quality (minimum true positive rates, maximum false positive rates)
- **Remediation Guidance Standards**: Require AI findings include remediation guidance (code examples, secure alternatives, fix validation)
- **Developer Override Ethics**: Standards for when developers can override AI findings (balance security rigor with development autonomy)
- **AI Code Generation Security**: Standards for AI-generated code security (Copilot, ChatGPT code must meet security requirements)

Value of secure development leadership:
- Influence AI security tool vendors (shape product development toward developer needs)
- Competitive advantage (superior AI secure development capabilities)
- Attract development talent (developers want to work with AI-enhanced secure development)
- Customer trust (demonstrable secure development maturity)

---

## Key Success Indicators

**Level 1:**
- Written policies exist governing AI agent operations in software security
- Compliance requirements documented and mapped to AI software security functions
- Finding quality standards defined (acceptable false positive rates, actionable remediation guidance)
- Basic audit trail capability (AI security decisions and developer overrides are logged)

**Level 2:**
- Comprehensive application risk-based policies implemented with developer experience governance
- Regular validation conducted (quarterly AI tool testing, monthly false positive audits, annual penetration testing)
- Developer feedback mechanisms implemented and acted upon
- False positive rate trends tracked and improving
- AI software security successfully passes compliance audits

**Level 3:**
- Continuous security validation deployed with real-time dashboards and trend analysis
- AI-assisted remediation capabilities implemented (AI suggests or auto-applies security fixes)
- Published contributions to secure development AI standards and benchmarking
- Active participation in AI security tool efficacy standards development
- Zero critical application security findings in production that AI tools should have detected

---

## Common Pitfalls

**Level 1:**
- ❌ Policies ignore developer experience (AI security gates block all deployments, developers bypass tools)
- ❌ Finding quality standards undefined (AI generates excessive false positives, developers lose trust)
- ❌ No override procedures (developers cannot ship despite business need, or override without accountability)
- ❌ Compliance requirements listed but not mapped to AI capabilities (unclear how AI meets PCI-DSS code review requirement)
- ❌ Audit trail incomplete (logs show AI found vulnerability but not developer response)

**Level 2:**
- ❌ Application risk classification too coarse (all apps treated same, no risk-based approach)
- ❌ Validation is infrequent (annual only, doesn't catch AI tool drift or emerging vulnerability types)
- ❌ False positive handling is manual and slow (AppSec team overwhelmed, developers frustrated)
- ❌ Developer feedback collected but not acted upon (surveys show low satisfaction, no tool improvements)
- ❌ Penetration testing doesn't validate AI findings (pentesters and AI findings never compared)

**Level 3:**
- ❌ Continuous validation generates noise not insights (too many dashboards, no actionable trends)
- ❌ AI-assisted remediation generates insecure fixes (auto-applied patches introduce new vulnerabilities)
- ❌ Industry engagement is performative (join standards bodies but don't contribute)
- ❌ Explainability is marketing not substance (AI "explains" findings with jargon, not clear reasoning)
- ❌ Over-reliance on AI security (reduce manual security review too much, miss vulnerabilities AI cannot detect)

---

## Practice Maturity Questions

**Level 1:**
1. Do you have documented policies governing how AI agents operate software security functions (code scanning, security testing, deployment gates)?
2. Have you identified and documented compliance requirements (PCI-DSS, HIPAA, OWASP ASVS) that apply to AI-operated software security?
3. Are finding quality standards defined with acceptable false positive rates and remediation guidance requirements?

**Level 2:**
1. Are comprehensive application risk-based policies implemented with developer experience governance?
2. Do you conduct regular validation (quarterly AI tool testing, monthly false positive audits) of AI software security effectiveness?
3. Are developer feedback mechanisms implemented with evidence of tool improvement based on feedback?

**Level 3:**
1. Do you have continuous security validation with real-time visibility into AI software security effectiveness?
2. Are AI-assisted remediation capabilities implemented to accelerate vulnerability fixes?
3. Does your organization actively contribute to secure development AI standards and tool benchmarking?

---

## Compliance & Secure Development Considerations

AI-operated software security must address specific regulatory and industry requirements:

### PCI-DSS (Payment Card Industry)
- **Requirement 6.3.2**: Code review for applications - AI code review meets requirement if validated effective
- **Requirement 6.2**: Security vulnerabilities - AI helps identify and remediate vulnerabilities timely
- **Requirement 11.3**: Penetration testing - AI security testing may supplement but not replace penetration testing

### OWASP ASVS (Application Security Verification Standard)
- **Level 1/2/3**: AI security tools can help achieve ASVS verification levels
- **Finding Accuracy**: AI tools must detect ASVS requirements violations accurately
- **Evidence**: AI scan results provide verification evidence for ASVS assessment

### NIST SSDF (Secure Software Development Framework)
- **PO.3**: Implement supporting toolchains - AI security tools part of secure development toolchain
- **PW.8**: Review and/or analyze code - AI SAST/code review meets requirement with validation
- **PS.1**: Protect all forms of code - AI SCA protects dependencies, SAST protects application code

### SOX (Sarbanes-Oxley for Financial Apps)
- **Change Management**: AI security gates in CI/CD support SOX change management controls
- **Access Controls**: AI monitors code for access control vulnerabilities in financial applications
- **Audit Evidence**: AI security logs provide SOX audit evidence for secure development

Organizations must ensure AI software security tools meet secure development and regulatory requirements with appropriate validation and audit trails.

---

**Document Version:** HAIAMM v2.0
**Practice:** Policy & Compliance (PC)
**Domain:** Software
**Last Updated:** December 2025
**Author:** Verifhai
