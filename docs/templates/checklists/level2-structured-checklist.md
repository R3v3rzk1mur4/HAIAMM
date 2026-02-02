# HAIAMM Level 2: Structured Checklist

**Maturity Level:** Structured (Documented requirements, consistent processes, defined roles)

**Prerequisite:** [Level 1 Foundation Checklist](level1-foundation-checklist.md) completed

**Purpose:** Formalize AI security processes with documented procedures, consistent execution, and defined responsibilities.

**Estimated Effort:** 1-3 months for full implementation

---

## Instructions

- Complete Level 1 before starting Level 2
- Check items as you complete them: `- [x]`
- Each practice requires **all items checked** to achieve Level 2
- Level 2 builds on Level 1 - maintain all Level 1 activities

---

## Governance Function

### SM - Strategy & Metrics (Level 2)

> *Formalized strategy with consistent metrics collection*

- [ ] **Documented Strategy**: Written AI security strategy document
  - Vision and objectives
  - Scope and boundaries
  - Roles and responsibilities
  - Review cadence (annual minimum)

- [ ] **Metrics Program**: Systematic metrics collection
  - Defined KPIs (3-5 minimum)
  - Automated collection where possible
  - Monthly reporting cadence
  - Trend tracking over time

- [ ] **Risk Register**: Maintained AI risk register
  - All identified AI risks documented
  - Risk owners assigned
  - Regular review (quarterly minimum)
  - Linked to controls

- [ ] **Program Reviews**: Regular strategy review meetings
  - Quarterly review cadence
  - Stakeholder participation
  - Documented decisions and actions

- [ ] **Budget Allocation**: Dedicated AI security resources
  - Identified budget line items
  - Resource allocation documented
  - Investment tracking

**Level 2 Complete When:** AI security strategy is documented and metrics are consistently tracked.

---

### PC - Policy & Compliance (Level 2)

> *Formalized policies with compliance monitoring*

- [ ] **Comprehensive Policy Set**: Complete AI security policies
  - AI acceptable use policy (formalized)
  - AI development security policy
  - AI vendor/third-party policy
  - AI data handling policy

- [ ] **Policy Governance**: Policy management process
  - Version control
  - Approval workflow
  - Annual review cycle
  - Exception process

- [ ] **Compliance Mapping**: Regulatory requirements mapped
  - Requirements identified per regulation
  - Controls mapped to requirements
  - Gap analysis documented
  - Remediation plans

- [ ] **Compliance Monitoring**: Regular compliance checks
  - Scheduled assessments
  - Evidence collection
  - Finding tracking
  - Reporting to stakeholders

- [ ] **Policy Training**: Mandatory policy awareness
  - Training completion tracking
  - Annual refresher requirement
  - New hire onboarding inclusion

**Level 2 Complete When:** Policies are formalized, governed, and compliance is actively monitored.

---

### EG - Education & Guidance (Level 2)

> *Structured training program with role-based curriculum*

- [ ] **Training Program**: Formalized AI security training
  - Defined curriculum
  - Role-based tracks
  - Completion requirements
  - Effectiveness measurement

- [ ] **Role-Based Training**: Specific training by role
  - Developers: Secure AI development
  - Security: AI threat detection
  - Users: Safe AI usage
  - Leadership: AI risk governance

- [ ] **Training Materials**: Maintained training content
  - Current with latest threats
  - Version controlled
  - Reviewed annually
  - Multiple formats (docs, videos, hands-on)

- [ ] **Knowledge Base**: Centralized AI security knowledge
  - Searchable documentation
  - Best practices library
  - FAQ and troubleshooting
  - Regular updates

- [ ] **Training Metrics**: Track training effectiveness
  - Completion rates
  - Assessment scores
  - Feedback collection
  - Improvement actions

**Level 2 Complete When:** Structured training program exists with role-based curriculum.

---

## Building Function

### TA - Threat Assessment (Level 2)

> *Systematic threat modeling with consistent methodology*

- [ ] **Threat Modeling Methodology**: Documented approach
  - Chosen methodology (STRIDE, PASTA, AI-specific)
  - Templates and guides
  - Tool selection
  - Training for practitioners

- [ ] **Systematic Coverage**: All AI systems threat modeled
  - Inventory linked to threat models
  - Prioritization criteria
  - Coverage tracking
  - Update triggers defined

- [ ] **Threat Intelligence**: Active threat monitoring
  - AI threat feeds subscribed
  - OWASP updates tracked
  - Vendor advisories monitored
  - Internal threat sharing

- [ ] **Threat Library**: Maintained threat catalog
  - AI-specific threats documented
  - Attack patterns cataloged
  - Mitigations mapped
  - Regular updates

- [ ] **Integration**: Threat assessment in SDLC
  - Triggered for new systems
  - Required for major changes
  - Results inform requirements
  - Tracked in project workflow

**Level 2 Complete When:** Threat modeling is systematic and integrated into development.

---

### SR - Security Requirements (Level 2)

> *Standardized requirements with traceability*

- [ ] **Requirements Catalog**: Standard AI security requirements
  - Categorized by domain/type
  - Mapped to risks and controls
  - Versioned and maintained
  - Rationale documented

- [ ] **Requirements Process**: Formal requirements definition
  - Stakeholder input process
  - Review and approval workflow
  - Change management
  - Requirements repository

- [ ] **Traceability**: Requirements linked throughout lifecycle
  - Requirements → Design
  - Requirements → Implementation
  - Requirements → Testing
  - Requirements → Controls

- [ ] **Risk-Based Selection**: Requirements based on risk
  - Risk assessment informs requirements
  - Proportional to system criticality
  - Documented justification
  - Exception process

- [ ] **Verification Criteria**: Testable requirements
  - Acceptance criteria defined
  - Test cases linked
  - Verification methods specified
  - Pass/fail criteria clear

**Level 2 Complete When:** Security requirements are standardized, cataloged, and traceable.

---

### SA - Secure Architecture (Level 2)

> *Reference architectures with consistent patterns*

- [ ] **Reference Architecture**: Documented secure AI patterns
  - Approved architecture patterns
  - Security controls embedded
  - Technology standards
  - Anti-patterns documented

- [ ] **Architecture Review Board**: Governance for AI architecture
  - Review process defined
  - Approval criteria
  - Exception handling
  - Decision documentation

- [ ] **Security Patterns**: Reusable security components
  - Input validation patterns
  - Output filtering patterns
  - Authentication/authorization patterns
  - Logging/monitoring patterns

- [ ] **Architecture Standards**: Documented standards
  - Technology choices
  - Integration patterns
  - Data flow requirements
  - Deployment requirements

- [ ] **Architecture Documentation**: Maintained architecture artifacts
  - System architecture diagrams
  - Data flow diagrams
  - Trust boundary documentation
  - Component specifications

**Level 2 Complete When:** Reference architectures exist and architecture reviews are consistent.

---

## Verification Function

### DR - Design Review (Level 2)

> *Formal review process with defined criteria*

- [ ] **Review Process**: Documented design review procedure
  - Triggers and scope
  - Participants and roles
  - Review criteria
  - Outcome documentation

- [ ] **Review Criteria**: Standardized evaluation checklist
  - Security requirements coverage
  - Threat mitigation
  - Architecture compliance
  - Risk acceptance

- [ ] **Review Board**: Designated reviewers
  - Qualified reviewers identified
  - Training requirements
  - Rotation/coverage
  - Escalation path

- [ ] **Review Tracking**: Systematic tracking of reviews
  - All reviews recorded
  - Findings tracked
  - Remediation verified
  - Metrics collected

- [ ] **Review Integration**: Design review in SDLC
  - Gate/milestone integration
  - Required before implementation
  - Sign-off requirements
  - Tool integration

**Level 2 Complete When:** Design reviews follow documented process with consistent criteria.

---

### IR - Implementation Review (Level 2)

> *Systematic code review with AI security focus*

- [ ] **Review Process**: Documented implementation review procedure
  - Scope and triggers
  - Review methodology
  - Tool requirements
  - Documentation standards

- [ ] **AI Security Checklist**: Specific AI security review items
  - Prompt injection prevention
  - Output validation
  - Secrets management
  - Error handling
  - Logging compliance

- [ ] **Automated Analysis**: Tool-assisted review
  - SAST integration
  - AI-specific analyzers
  - Dependency scanning
  - Configuration checks

- [ ] **Review Coverage**: Consistent review coverage
  - All AI code reviewed
  - Coverage metrics tracked
  - Gap identification
  - Remediation process

- [ ] **Review Documentation**: Recorded review outcomes
  - Findings documented
  - Severity assigned
  - Remediation tracked
  - Lessons learned captured

**Level 2 Complete When:** Implementation reviews are systematic with AI-specific checklists.

---

### ST - Security Testing (Level 2)

> *Structured testing program with automated tools*

- [ ] **Testing Program**: Documented AI security testing approach
  - Test types and scope
  - Testing schedule
  - Tool requirements
  - Reporting standards

- [ ] **Test Suite**: Maintained AI security test cases
  - Prompt injection tests
  - Jailbreak attempts
  - Data extraction tests
  - Boundary testing
  - Abuse case testing

- [ ] **Automated Testing**: Integrated automated testing
  - CI/CD integration
  - Scheduled scans
  - Regression testing
  - Results tracking

- [ ] **Testing Tools**: Standardized tooling
  - Tools selected and approved
  - Configuration documented
  - Training provided
  - Maintenance process

- [ ] **Testing Metrics**: Track testing effectiveness
  - Coverage metrics
  - Finding trends
  - False positive rates
  - Remediation times

**Level 2 Complete When:** Security testing is automated and integrated into CI/CD.

---

## Operations Function

### IM - Issue Management (Level 2)

> *Structured issue tracking with SLAs*

- [ ] **Issue Process**: Documented issue management procedure
  - Intake and triage
  - Assignment and escalation
  - Resolution workflow
  - Closure criteria

- [ ] **SLA Definitions**: Service level agreements for issues
  - Response time by severity
  - Resolution time targets
  - Escalation triggers
  - Exception process

- [ ] **Issue Workflow**: Defined issue lifecycle
  - Status definitions
  - Transition rules
  - Required fields
  - Automation where possible

- [ ] **Reporting**: Regular issue reporting
  - Open issue counts
  - SLA compliance
  - Trend analysis
  - Stakeholder reports

- [ ] **Root Cause Analysis**: Systematic RCA for significant issues
  - RCA triggers defined
  - Methodology documented
  - Findings tracked
  - Preventive actions

**Level 2 Complete When:** Issues are managed with defined SLAs and systematic tracking.

---

### EH - Environment Hardening (Level 2)

> *Standardized hardening with configuration management*

- [ ] **Hardening Standards**: Documented hardening requirements
  - Baseline configurations
  - Security settings
  - Prohibited configurations
  - Exception process

- [ ] **Configuration Management**: Systematic configuration control
  - Configuration inventory
  - Change management
  - Version control
  - Drift detection

- [ ] **Hardening Automation**: Automated hardening application
  - Infrastructure as code
  - Configuration automation
  - Compliance checking
  - Remediation automation

- [ ] **Hardening Verification**: Regular verification of hardening
  - Scheduled scans
  - Compliance checks
  - Gap identification
  - Remediation tracking

- [ ] **Hardening Documentation**: Maintained hardening artifacts
  - Current configurations
  - Rationale documentation
  - Exception records
  - Audit evidence

**Level 2 Complete When:** Hardening is standardized and configuration is managed systematically.

---

### ML - Monitoring & Logging (Level 2)

> *Centralized monitoring with alerting and correlation*

- [ ] **Monitoring Strategy**: Documented monitoring approach
  - What to monitor
  - Alert thresholds
  - Response procedures
  - Tool selection

- [ ] **Centralized Logging**: Aggregated log management
  - All AI systems logging
  - Central log repository
  - Retention policies enforced
  - Access controls

- [ ] **Alerting System**: Automated alert generation
  - Alert rules defined
  - Severity levels
  - Notification routing
  - Escalation procedures

- [ ] **Correlation Capability**: Log correlation and analysis
  - Cross-system correlation
  - Pattern detection
  - Baseline comparison
  - Investigation support

- [ ] **Monitoring Dashboards**: Operational visibility
  - Real-time dashboards
  - KPI tracking
  - Trend visualization
  - Stakeholder views

**Level 2 Complete When:** Monitoring is centralized with automated alerting and correlation.

---

## Level 2 Completion Summary

### Checklist Totals

| Function | Practice | Items | Complete |
|----------|----------|-------|----------|
| Governance | SM | 5 | ☐ |
| Governance | PC | 5 | ☐ |
| Governance | EG | 5 | ☐ |
| Building | TA | 5 | ☐ |
| Building | SR | 5 | ☐ |
| Building | SA | 5 | ☐ |
| Verification | DR | 5 | ☐ |
| Verification | IR | 5 | ☐ |
| Verification | ST | 5 | ☐ |
| Operations | IM | 5 | ☐ |
| Operations | EH | 5 | ☐ |
| Operations | ML | 5 | ☐ |
| **Total** | **12** | **60** | |

### Prerequisites Verified

- [ ] Level 1 Foundation checklist completed
- [ ] Level 1 activities maintained
- [ ] Resources allocated for Level 2

### Sign-Off

- [ ] All 60 items completed
- [ ] Evidence documented for each practice
- [ ] Assessment recorded in tracking system
- [ ] Level 1 maintenance confirmed

**Assessment Date:** ________________

**Assessed By:** ________________

**Next Step:** [Level 3 Optimized Checklist](level3-optimized-checklist.md)

---

## Document Information

| Field | Value |
|-------|-------|
| HAIAMM Version | 2.0 |
| Checklist Version | 1.0 |
| Last Updated | January 2026 |

---

*Use `/verifhai-measure` for comprehensive maturity assessment assistance.*
