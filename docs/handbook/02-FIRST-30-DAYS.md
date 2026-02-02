![HAIAMM Logo](../images/HAIAMM_logo.png)

# HAIAMM First 30 Days

**A practical day-by-day implementation roadmap**

[Back to Index](00-INDEX.md) | [Quick Start](01-QUICK-START.md) | [Assessment Checklist](07-ASSESSMENT-CHECKLIST.md)

---

## Overview

This guide provides a structured 30-day roadmap to establish foundational AI security controls. By the end of 30 days, you'll have:

- Complete inventory of AI systems
- Initial threat assessment
- Core security controls implemented
- Basic monitoring in place
- Documented policies and metrics

**Prerequisites:**
- Executive sponsorship for AI security initiative
- Access to AI system documentation and configurations
- 2-4 hours per day dedicated to this program

---

## Week 1: Discovery (Days 1-7)

**Goal:** Understand what AI systems exist and who owns them.

### Day 1: Kickoff & Stakeholder Alignment

**Objective:** Establish program foundation and get stakeholder buy-in.

**Actions:**
- [ ] Meet with CISO/security leadership to confirm scope
- [ ] Identify key stakeholders (ML engineering, DevOps, compliance)
- [ ] Create shared communication channel (Slack, Teams)
- [ ] Review existing AI/ML policies (if any)
- [ ] Schedule Week 1 stakeholder meetings

**Deliverable:** Program charter with scope, stakeholders, and timeline

**Time:** 3-4 hours

---

### Day 2: AI System Discovery - Internal

**Objective:** Identify all internally developed AI systems.

**Actions:**
- [ ] Query cloud accounts for AI/ML services (SageMaker, Vertex AI, Azure ML)
- [ ] Search code repositories for ML frameworks (PyTorch, TensorFlow, LangChain)
- [ ] Review CI/CD pipelines for model deployments
- [ ] Interview ML engineering leads
- [ ] Check internal wiki/docs for AI project documentation

**Deliverable:** Initial AI system inventory (internal)

```markdown
## AI System Inventory - Internal

| System | Type | Owner | Environment | Data Access | Status |
|--------|------|-------|-------------|-------------|--------|
| | | | | | |
```

**Time:** 4-5 hours

---

### Day 3: AI System Discovery - Third Party

**Objective:** Identify all third-party AI services in use.

**Actions:**
- [ ] Review cloud billing for AI API charges (OpenAI, Anthropic, etc.)
- [ ] Check procurement records for AI tool purchases
- [ ] Survey teams for AI tool usage (ChatGPT, Copilot, etc.)
- [ ] Review SSO/identity logs for AI service authentications
- [ ] Check browser extensions for AI tools

**Deliverable:** Third-party AI vendor inventory

```markdown
## AI Vendor Inventory

| Vendor | Service | Department | Data Shared | Contract Status |
|--------|---------|------------|-------------|-----------------|
| | | | | |
```

**Time:** 3-4 hours

---

### Day 4: Shadow AI Discovery

**Objective:** Identify unauthorized or unknown AI usage.

**Actions:**
- [ ] Analyze network traffic for AI API endpoints
- [ ] Review expense reports for AI subscriptions
- [ ] Send organization-wide AI usage survey
- [ ] Check DLP logs for AI service data transfers
- [ ] Interview department heads about team AI usage

**Deliverable:** Shadow AI assessment report

**Time:** 4-5 hours

---

### Day 5: Data Flow Mapping

**Objective:** Understand what data flows to/from AI systems.

**Actions:**
- [ ] For each AI system, document input data sources
- [ ] Identify output destinations and consumers
- [ ] Classify data sensitivity levels (PII, confidential, public)
- [ ] Map data residency and compliance requirements
- [ ] Identify cross-border data transfers

**Deliverable:** AI data flow diagrams

```
[Data Source] → [AI System] → [Output Consumer]
     ↓               ↓              ↓
 Classification   Processing    Usage Context
```

**Time:** 4-5 hours

---

### Day 6: Risk Owner Assignment

**Objective:** Establish accountability for each AI system.

**Actions:**
- [ ] Assign risk owner to each AI system
- [ ] Define risk owner responsibilities
- [ ] Create RACI matrix for AI security
- [ ] Schedule recurring risk review meetings
- [ ] Document escalation paths

**Deliverable:** AI security RACI matrix

| Activity | Security Team | Risk Owner | ML Engineering | Executive |
|----------|---------------|------------|----------------|-----------|
| Risk Assessment | R | A | C | I |
| Remediation | C | A | R | I |
| Monitoring | R | I | C | I |
| Incident Response | R | A | C | I |

**Time:** 2-3 hours

---

### Day 7: Week 1 Review & Planning

**Objective:** Consolidate findings and plan Week 2.

**Actions:**
- [ ] Compile complete AI system inventory
- [ ] Calculate initial risk scores per system
- [ ] Identify top 5 highest-risk systems
- [ ] Present findings to stakeholders
- [ ] Plan Week 2 priorities

**Deliverable:** Week 1 summary report with risk rankings

**Time:** 3-4 hours

---

## Week 2: Foundation (Days 8-14)

**Goal:** Implement foundational security controls for highest-risk systems.

### Day 8: Threat Assessment - Top Risk System

**Objective:** Complete threat assessment for highest-risk AI system.

**Actions:**
- [ ] Identify system assets (models, data, APIs)
- [ ] Enumerate threat actors (external, internal, AI-specific)
- [ ] Map attack vectors (prompt injection, data poisoning, etc.)
- [ ] Assess likelihood and impact per threat
- [ ] Prioritize threats by risk score

**Deliverable:** Threat model for top-risk system

**HAIAMM Reference:** [TA - Threat Assessment](../practices/TA-Software-OnePager.md)

**Time:** 4-5 hours

---

### Day 9: Security Requirements Definition

**Objective:** Define security requirements for AI systems.

**Actions:**
- [ ] Define input validation requirements
- [ ] Specify output handling rules
- [ ] Document authentication/authorization requirements
- [ ] Set data protection requirements
- [ ] Define logging and monitoring requirements

**Deliverable:** AI Security Requirements Specification

```markdown
## AI Security Requirements

### Input Security
- REQ-IN-001: All user inputs must be validated for length (<10K chars)
- REQ-IN-002: Prompt injection patterns must be detected and blocked
- REQ-IN-003: Input sources must be authenticated

### Output Security
- REQ-OUT-001: All outputs must be sanitized before rendering
- REQ-OUT-002: PII must be detected and redacted
- REQ-OUT-003: Output tokens must be rate-limited
```

**HAIAMM Reference:** [SR - Security Requirements](../practices/SR-Software-OnePager.md)

**Time:** 3-4 hours

---

### Day 10: Quick Win - Input Validation

**Objective:** Implement input validation on production AI endpoints.

**Actions:**
- [ ] Deploy input length validation
- [ ] Implement basic prompt injection detection
- [ ] Add input logging (redacted for PII)
- [ ] Configure rate limiting per user
- [ ] Test validation with sample attacks

**Deliverable:** Input validation deployed, test results documented

**Code Example:**
```python
def validate_ai_input(user_input: str, user_id: str) -> tuple[bool, str]:
    # Length check
    if len(user_input) > 10000:
        log_security_event("input_too_long", user_id)
        return False, "Input exceeds maximum length"

    # Injection pattern check
    if detect_injection_pattern(user_input):
        log_security_event("injection_attempt", user_id)
        return False, "Invalid input detected"

    return True, ""
```

**Time:** 4-5 hours

---

### Day 11: Quick Win - Output Filtering

**Objective:** Implement output security controls.

**Actions:**
- [ ] Deploy PII detection on outputs
- [ ] Implement output encoding for web display
- [ ] Add output logging (redacted)
- [ ] Configure output token limits
- [ ] Test with PII injection attempts

**Deliverable:** Output filtering deployed, test results documented

**Time:** 4-5 hours

---

### Day 12: Quick Win - Access Controls

**Objective:** Implement proper access controls for AI systems.

**Actions:**
- [ ] Review current AI system access controls
- [ ] Implement role-based access for AI APIs
- [ ] Configure API authentication (API keys → OAuth)
- [ ] Remove shared credentials
- [ ] Document access control matrix

**Deliverable:** Access control audit and improvements

**Time:** 3-4 hours

---

### Day 13: Logging & Alerting Setup

**Objective:** Establish AI security monitoring foundation.

**Actions:**
- [ ] Configure AI system audit logging
- [ ] Set up log aggregation (SIEM integration)
- [ ] Create security alerts for:
  - Injection attempts
  - Unusual usage patterns
  - Error rate spikes
  - PII in outputs
- [ ] Test alert delivery

**Deliverable:** AI security monitoring dashboard

**HAIAMM Reference:** [ML - Monitoring & Logging](../practices/ML-Software-OnePager.md)

**Time:** 4-5 hours

---

### Day 14: Week 2 Review

**Objective:** Assess progress and prepare for Week 3.

**Actions:**
- [ ] Review implemented controls
- [ ] Test security controls end-to-end
- [ ] Document remaining gaps
- [ ] Update risk scores based on controls
- [ ] Plan Week 3 priorities

**Deliverable:** Week 2 control implementation summary

**Time:** 3-4 hours

---

## Week 3: Controls (Days 15-21)

**Goal:** Expand security controls and establish operational processes.

### Day 15: Environment Hardening - API Security

**Objective:** Harden AI API infrastructure.

**Actions:**
- [ ] Enable TLS 1.3 for all AI endpoints
- [ ] Implement request signing/validation
- [ ] Configure WAF rules for AI-specific attacks
- [ ] Set up DDoS protection
- [ ] Implement IP allowlisting for sensitive endpoints

**Deliverable:** Hardened API configuration documentation

**HAIAMM Reference:** [EH - Environment Hardening](../practices/EH-Infrastructure-OnePager.md)

**Time:** 4-5 hours

---

### Day 16: Environment Hardening - Model Security

**Objective:** Secure model storage and execution.

**Actions:**
- [ ] Encrypt models at rest
- [ ] Implement model access logging
- [ ] Configure model versioning
- [ ] Set up model integrity verification
- [ ] Create model rollback procedure

**Deliverable:** Model security hardening checklist completed

**Time:** 3-4 hours

---

### Day 17: Agent Tool Security (If Applicable)

**Objective:** Secure AI agent tool access.

**Actions:**
- [ ] Inventory all agent tools
- [ ] Implement tool permission policies
- [ ] Configure tool usage logging
- [ ] Add rate limits per tool
- [ ] Test tool access restrictions

**Deliverable:** Agent tool security configuration

**HAIAMM Reference:** [Top 10 Agentic Risks - ASI02](04-TOP10-AGENTIC-RISKS.md#asi02-tool-misuse--exploitation)

**Time:** 4-5 hours

---

### Day 18: Incident Response Planning

**Objective:** Create AI-specific incident response procedures.

**Actions:**
- [ ] Define AI security incident categories
- [ ] Create incident severity classification
- [ ] Document response procedures per category
- [ ] Define escalation paths
- [ ] Create communication templates

**Deliverable:** AI Incident Response Playbook

```markdown
## AI Incident Categories

| Category | Severity | Response Time | Example |
|----------|----------|---------------|---------|
| Prompt Injection | Medium | 4 hours | Detected injection attempt |
| Data Leakage | High | 1 hour | PII in AI output |
| Model Compromise | Critical | 15 min | Suspected model poisoning |
| Agent Misbehavior | Critical | 15 min | Unauthorized actions |
```

**HAIAMM Reference:** [IM - Issue Management](../practices/IM-Processes-OnePager.md)

**Time:** 4-5 hours

---

### Day 19: Security Testing - Initial

**Objective:** Conduct initial security testing of AI systems.

**Actions:**
- [ ] Run prompt injection test suite
- [ ] Test for data leakage (PII, system prompts)
- [ ] Test rate limiting effectiveness
- [ ] Verify access control enforcement
- [ ] Test agent tool restrictions (if applicable)

**Deliverable:** Initial security test report

**Test Cases:**
```
[ ] Prompt Injection - Direct
[ ] Prompt Injection - Indirect (document-based)
[ ] System Prompt Extraction
[ ] PII Injection and Detection
[ ] Rate Limit Bypass
[ ] Authentication Bypass
[ ] Tool Permission Bypass
```

**HAIAMM Reference:** [ST - Security Testing](../practices/ST-Software-OnePager.md)

**Time:** 5-6 hours

---

### Day 20: Vulnerability Remediation

**Objective:** Address findings from security testing.

**Actions:**
- [ ] Prioritize findings by severity
- [ ] Create remediation tickets
- [ ] Implement critical/high fixes
- [ ] Schedule medium/low fixes
- [ ] Retest fixed vulnerabilities

**Deliverable:** Remediation tracking spreadsheet

**Time:** 4-5 hours

---

### Day 21: Week 3 Review

**Objective:** Consolidate control implementations.

**Actions:**
- [ ] Document all implemented controls
- [ ] Update risk assessment with mitigations
- [ ] Review outstanding vulnerabilities
- [ ] Prepare governance documentation
- [ ] Plan Week 4 activities

**Deliverable:** Week 3 summary with control coverage matrix

**Time:** 3-4 hours

---

## Week 4: Governance (Days 22-30)

**Goal:** Establish ongoing governance, policies, and measurement.

### Day 22: Policy Development

**Objective:** Create AI security policy framework.

**Actions:**
- [ ] Draft AI Acceptable Use Policy
- [ ] Create AI Development Security Standards
- [ ] Define AI Vendor Assessment Requirements
- [ ] Document Data Handling for AI Systems
- [ ] Obtain initial policy approvals

**Deliverable:** AI Security Policy Suite (draft)

**HAIAMM Reference:** [PC - Policy & Compliance](../practices/PC-Processes-OnePager.md)

**Time:** 4-5 hours

---

### Day 23: Training & Awareness

**Objective:** Launch AI security awareness program.

**Actions:**
- [ ] Create AI security awareness presentation
- [ ] Develop secure AI development guidelines
- [ ] Schedule training sessions
- [ ] Create quick reference guides
- [ ] Set up training tracking

**Deliverable:** AI Security Training Materials

**Topics to Cover:**
1. AI-specific threats (prompt injection, data poisoning)
2. Secure AI development practices
3. Incident reporting procedures
4. Policy compliance requirements

**HAIAMM Reference:** [EG - Education & Guidance](../practices/EG-Processes-OnePager.md)

**Time:** 4-5 hours

---

### Day 24: Metrics Framework

**Objective:** Establish AI security metrics and KPIs.

**Actions:**
- [ ] Define key security metrics
- [ ] Set up metric collection
- [ ] Create security dashboard
- [ ] Establish baseline measurements
- [ ] Define metric targets

**Deliverable:** AI Security Metrics Dashboard

**Key Metrics:**
| Metric | Target | Current | Measurement |
|--------|--------|---------|-------------|
| Systems Inventoried | 100% | | Weekly |
| Critical Vulns Open | 0 | | Daily |
| Injection Detection Rate | >90% | | Weekly |
| Mean Time to Detect | <5 min | | Per incident |
| Policy Compliance | >95% | | Monthly |

**HAIAMM Reference:** [SM - Strategy & Metrics](../practices/SM-Software-OnePager.md)

**Time:** 4-5 hours

---

### Day 25: Vendor Security Assessment

**Objective:** Assess third-party AI vendor security.

**Actions:**
- [ ] Create AI vendor security questionnaire
- [ ] Send questionnaires to priority vendors
- [ ] Review vendor security documentation
- [ ] Assess data processing agreements
- [ ] Document vendor risk ratings

**Deliverable:** AI Vendor Risk Assessment Report

**Assessment Areas:**
- Data handling and privacy
- Security certifications (SOC 2, ISO 27001)
- Incident response capabilities
- Model security practices
- Contractual security requirements

**Time:** 4-5 hours

---

### Day 26: Architecture Review

**Objective:** Review AI system architecture for security.

**Actions:**
- [ ] Document current AI architecture
- [ ] Identify security gaps in design
- [ ] Recommend architecture improvements
- [ ] Prioritize architecture changes
- [ ] Create architecture security roadmap

**Deliverable:** AI Architecture Security Review

**HAIAMM Reference:** [SA - Secure Architecture](../practices/SA-Software-OnePager.md)

**Time:** 4-5 hours

---

### Day 27: Continuous Monitoring Setup

**Objective:** Establish ongoing security monitoring.

**Actions:**
- [ ] Configure continuous vulnerability scanning
- [ ] Set up configuration drift detection
- [ ] Implement log analysis rules
- [ ] Create anomaly detection baselines
- [ ] Document monitoring procedures

**Deliverable:** Continuous monitoring runbook

**Time:** 4-5 hours

---

### Day 28: Compliance Mapping

**Objective:** Map AI security to compliance requirements.

**Actions:**
- [ ] Identify applicable regulations (AI Act, GDPR, etc.)
- [ ] Map HAIAMM controls to requirements
- [ ] Identify compliance gaps
- [ ] Document evidence requirements
- [ ] Create compliance tracking

**Deliverable:** AI Compliance Mapping Matrix

**Time:** 3-4 hours

---

### Day 29: Program Documentation

**Objective:** Document the complete AI security program.

**Actions:**
- [ ] Compile all deliverables
- [ ] Create program overview document
- [ ] Document processes and procedures
- [ ] Create onboarding guide for new team members
- [ ] Archive project artifacts

**Deliverable:** AI Security Program Documentation Package

**Time:** 4-5 hours

---

### Day 30: Final Review & Next Steps

**Objective:** Complete program launch and plan next quarter.

**Actions:**
- [ ] Present program to executive stakeholders
- [ ] Review metrics and achievements
- [ ] Identify remaining gaps
- [ ] Create Q2 roadmap
- [ ] Celebrate launch!

**Deliverable:** 30-Day Summary Report & Q2 Roadmap

**Summary Template:**
```markdown
## 30-Day AI Security Program Summary

### Achievements
- [ ] X AI systems inventoried
- [ ] X critical vulnerabilities remediated
- [ ] X security controls implemented
- [ ] X policies drafted/approved
- [ ] X team members trained

### Key Metrics
- Detection Rate: X%
- Systems Covered: X%
- Open Critical Vulns: X

### Q2 Priorities
1. [Priority 1]
2. [Priority 2]
3. [Priority 3]
```

**Time:** 4-5 hours

---

## Checklist Summary

### Week 1: Discovery
- [ ] Day 1: Kickoff & Alignment
- [ ] Day 2: Internal AI Discovery
- [ ] Day 3: Third-Party AI Discovery
- [ ] Day 4: Shadow AI Discovery
- [ ] Day 5: Data Flow Mapping
- [ ] Day 6: Risk Owner Assignment
- [ ] Day 7: Week 1 Review

### Week 2: Foundation
- [ ] Day 8: Threat Assessment
- [ ] Day 9: Security Requirements
- [ ] Day 10: Input Validation
- [ ] Day 11: Output Filtering
- [ ] Day 12: Access Controls
- [ ] Day 13: Logging & Alerting
- [ ] Day 14: Week 2 Review

### Week 3: Controls
- [ ] Day 15: API Hardening
- [ ] Day 16: Model Security
- [ ] Day 17: Agent Tool Security
- [ ] Day 18: Incident Response
- [ ] Day 19: Security Testing
- [ ] Day 20: Remediation
- [ ] Day 21: Week 3 Review

### Week 4: Governance
- [ ] Day 22: Policy Development
- [ ] Day 23: Training
- [ ] Day 24: Metrics Framework
- [ ] Day 25: Vendor Assessment
- [ ] Day 26: Architecture Review
- [ ] Day 27: Continuous Monitoring
- [ ] Day 28: Compliance Mapping
- [ ] Day 29: Documentation
- [ ] Day 30: Final Review

---

## Document Information

| Field | Value |
|-------|-------|
| Document | First 30 Days Implementation Guide |
| HAIAMM Version | 2.0 |
| Last Updated | January 2026 |

---

**Next Steps:**
- [Assessment Checklist](07-ASSESSMENT-CHECKLIST.md) - Ongoing assessment
- [Maturity Roadmap](06-MATURITY-ROADMAP.md) - Level 2 planning
- [Tools & Resources](08-TOOLS-RESOURCES.md) - Recommended tools

[Back to Index](00-INDEX.md)
