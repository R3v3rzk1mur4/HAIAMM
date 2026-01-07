# HAIAMM Level 1: Foundation Checklist

**Maturity Level:** Foundation (Basic understanding, ad-hoc activities, individual effort)

**Purpose:** Establish baseline AI security capabilities across all 12 HAIAMM practices.

**Estimated Effort:** 2-4 weeks for initial implementation

---

## Instructions

- Check items as you complete them: `- [x]`
- Each practice requires **all items checked** to achieve Level 1
- Focus on one function at a time for manageable progress
- Use `/verifhai-practice [practice-code]` for guided implementation

---

## Governance Function

### SM - Strategy & Metrics

> *Define AI security strategy and measure effectiveness*

- [ ] **AI System Inventory**: Document all AI/ML systems in your environment
  - System name, type (LLM, agent, ML model)
  - Data access level
  - Tool/API access
  - Owner/team responsible

- [ ] **Risk Awareness**: Identify top 3-5 AI security risks for your organization
  - Reference: [OWASP Top 10 for LLMs](../../handbook/03-TOP10-LLM-RISKS.md)
  - Reference: [OWASP Top 10 for Agentic Apps](../../handbook/04-TOP10-AGENTIC-RISKS.md)

- [ ] **Basic Metrics**: Track at least one security metric
  - Examples: # of AI systems inventoried, # of security reviews completed
  - Frequency: Monthly review minimum

- [ ] **Stakeholder Identification**: Know who owns AI security decisions
  - Security team contact
  - AI/ML engineering contact
  - Executive sponsor (if applicable)

**Level 1 Complete When:** You can answer "What AI systems do we have and who owns their security?"

---

### PC - Policy & Compliance

> *Establish policies and ensure regulatory compliance*

- [ ] **Acceptable Use Policy**: Document basic AI usage guidelines
  - What data can be sent to AI systems
  - What AI systems are approved for use
  - Prohibited uses (if any)

- [ ] **Regulatory Awareness**: Identify applicable AI regulations
  - EU AI Act applicability
  - Industry-specific requirements (HIPAA, PCI-DSS, etc.)
  - Data privacy implications (GDPR, CCPA)

- [ ] **Incident Reporting**: Define how to report AI security incidents
  - Who to contact
  - What information to include
  - Response expectations

- [ ] **Third-Party AI Policy**: Document rules for external AI services
  - Approved vendors list
  - Data sharing restrictions
  - Approval process for new AI tools

**Level 1 Complete When:** Basic AI usage guidelines exist and are communicated.

---

### EG - Education & Guidance

> *Train teams on AI security best practices*

- [ ] **Awareness Material**: Create or curate basic AI security training
  - What is prompt injection?
  - What are AI-specific risks?
  - How to report concerns

- [ ] **Role-Based Guidance**: Identify who needs AI security training
  - Developers building AI features
  - Users interacting with AI systems
  - Security team members

- [ ] **Resource Library**: Collect reference materials
  - OWASP AI resources
  - Vendor security documentation
  - Internal guidelines

- [ ] **Communication Channel**: Establish way to share AI security updates
  - Slack channel, email list, or wiki page
  - Regular update cadence (monthly minimum)

**Level 1 Complete When:** Team members know where to find AI security guidance.

---

## Building Function

### TA - Threat Assessment

> *Identify and prioritize AI-specific threats*

- [ ] **Threat Identification**: List AI-specific threats relevant to your systems
  - Prompt injection attacks
  - Data poisoning risks
  - Model theft/extraction
  - Agent misuse scenarios

- [ ] **Risk Mapping**: Map threats to your AI systems
  - Which systems are vulnerable to which threats?
  - What's the potential impact?

- [ ] **Threat Actors**: Identify who might attack your AI systems
  - External attackers
  - Malicious insiders
  - Automated attacks

- [ ] **Basic Threat Model**: Document threats for at least one critical AI system
  - System description
  - Data flows
  - Trust boundaries
  - Identified threats

**Level 1 Complete When:** You can describe the top threats to your AI systems.

---

### SR - Security Requirements

> *Define security requirements for AI systems*

- [ ] **Input Requirements**: Define input validation rules
  - Maximum input length
  - Prohibited content patterns
  - Rate limiting thresholds

- [ ] **Output Requirements**: Define output handling rules
  - Sensitive data filtering
  - Response length limits
  - Format validation

- [ ] **Access Requirements**: Define who/what can access AI systems
  - Authentication requirements
  - Authorization levels
  - API key management

- [ ] **Data Requirements**: Define data handling rules
  - What data can be processed
  - Retention policies
  - Privacy requirements

**Level 1 Complete When:** Basic security requirements exist for AI system inputs and outputs.

---

### SA - Secure Architecture

> *Design secure AI system architectures*

- [ ] **Architecture Documentation**: Document AI system architecture
  - Components and their interactions
  - Data flow diagrams
  - External dependencies

- [ ] **Trust Boundaries**: Identify trust boundaries in AI systems
  - User input boundary
  - LLM/model boundary
  - Tool/API boundary

- [ ] **Least Privilege**: Apply basic least privilege to AI agents
  - Minimal tool access
  - Restricted data access
  - Limited network access

- [ ] **Separation**: Keep AI components appropriately isolated
  - Separate environments (dev/staging/prod)
  - Network segmentation where feasible

**Level 1 Complete When:** AI system architecture is documented with clear trust boundaries.

---

## Verification Function

### DR - Design Review

> *Review AI system designs for security flaws*

- [ ] **Review Process**: Define when design reviews happen
  - New AI system deployments
  - Significant changes to existing systems
  - New tool/API integrations

- [ ] **Review Checklist**: Create basic design review checklist
  - Are trust boundaries defined?
  - Is least privilege applied?
  - Are inputs validated?
  - Are outputs sanitized?

- [ ] **Documentation**: Require design documentation for reviews
  - Architecture diagrams
  - Data flow descriptions
  - Security considerations

- [ ] **Review Record**: Track completed design reviews
  - Date, system, reviewer
  - Findings and resolutions

**Level 1 Complete When:** New AI systems receive basic security design review.

---

### IR - Implementation Review

> *Review AI implementations for vulnerabilities*

- [ ] **Code Review Practice**: Include security in AI code reviews
  - Check for hardcoded secrets
  - Verify input validation
  - Review error handling

- [ ] **Review Triggers**: Define when implementation reviews occur
  - Pull requests with AI components
  - Security-sensitive changes
  - Before production deployment

- [ ] **Common Issues Checklist**: Document common AI security issues to check
  - Prompt injection vulnerabilities
  - Sensitive data exposure
  - Improper error messages

- [ ] **Review Documentation**: Record implementation review outcomes
  - Issues found
  - Remediation actions
  - Sign-off

**Level 1 Complete When:** AI code changes receive security-focused review.

---

### ST - Security Testing

> *Test AI systems for security weaknesses*

- [ ] **Basic Testing**: Perform manual security testing on AI systems
  - Try common prompt injection patterns
  - Test input validation boundaries
  - Verify output filtering

- [ ] **Test Cases**: Document AI security test cases
  - Prompt injection attempts
  - Jailbreak attempts
  - Data extraction attempts

- [ ] **Testing Tools**: Identify tools for AI security testing
  - Garak, PyRIT, or similar
  - Manual testing procedures

- [ ] **Test Results**: Document and track test findings
  - Vulnerabilities discovered
  - Severity ratings
  - Remediation status

**Level 1 Complete When:** AI systems are manually tested for common vulnerabilities.

---

## Operations Function

### IM - Issue Management

> *Track and remediate security issues*

- [ ] **Issue Tracking**: Track AI security issues in a system
  - Use existing ticketing (Jira, GitHub Issues)
  - Include severity, status, owner

- [ ] **Severity Definitions**: Define severity levels for AI security issues
  - Critical: Active exploitation, data breach
  - High: Exploitable vulnerability
  - Medium: Potential vulnerability
  - Low: Best practice gap

- [ ] **Remediation Process**: Define how issues get fixed
  - Assignment process
  - Timeline expectations
  - Verification of fixes

- [ ] **Issue Review**: Regularly review open issues
  - Weekly minimum for critical/high
  - Monthly for medium/low

**Level 1 Complete When:** AI security issues are tracked and remediated systematically.

---

### EH - Environment Hardening

> *Secure AI runtime environments*

- [ ] **Basic Hardening**: Apply fundamental security controls
  - API authentication required
  - HTTPS/TLS for all communications
  - Secrets not hardcoded

- [ ] **Input Validation**: Implement basic input controls
  - Length limits enforced
  - Rate limiting enabled
  - Basic content filtering

- [ ] **Output Controls**: Implement basic output controls
  - Sensitive pattern filtering
  - Response size limits
  - Error message sanitization

- [ ] **Access Controls**: Restrict access to AI systems
  - Authentication required
  - Authorization enforced
  - Audit logging enabled

**Level 1 Complete When:** Basic security controls protect AI system interfaces.

---

### ML - Monitoring & Logging

> *Monitor AI systems for security events*

- [ ] **Basic Logging**: Log AI system interactions
  - User/session identifier (hashed)
  - Input received (or reference)
  - Output generated (or reference)
  - Timestamp

- [ ] **Log Storage**: Store logs securely
  - Access-controlled storage
  - Minimum 30-day retention
  - Tamper protection

- [ ] **Anomaly Awareness**: Know what abnormal looks like
  - Unusual request volumes
  - Suspicious input patterns
  - Error rate spikes

- [ ] **Alert Capability**: Ability to detect obvious issues
  - Error rate monitoring
  - Availability monitoring
  - Manual review capability

**Level 1 Complete When:** AI interactions are logged and basic monitoring exists.

---

## Level 1 Completion Summary

### Checklist Totals

| Function | Practice | Items | Complete |
|----------|----------|-------|----------|
| Governance | SM | 4 | ☐ |
| Governance | PC | 4 | ☐ |
| Governance | EG | 4 | ☐ |
| Building | TA | 4 | ☐ |
| Building | SR | 4 | ☐ |
| Building | SA | 4 | ☐ |
| Verification | DR | 4 | ☐ |
| Verification | IR | 4 | ☐ |
| Verification | ST | 4 | ☐ |
| Operations | IM | 4 | ☐ |
| Operations | EH | 4 | ☐ |
| Operations | ML | 4 | ☐ |
| **Total** | **12** | **48** | |

### Sign-Off

- [ ] All 48 items completed
- [ ] Evidence documented for each practice
- [ ] Assessment recorded in tracking system

**Assessment Date:** ________________

**Assessed By:** ________________

**Next Step:** [Level 2 Structured Checklist](level2-structured-checklist.md)

---

## Document Information

| Field | Value |
|-------|-------|
| HAIAMM Version | 2.2 |
| Checklist Version | 1.0 |
| Last Updated | January 2026 |

---

*Use `/verifhai-assess` to get AI-assisted guidance on completing this checklist.*
