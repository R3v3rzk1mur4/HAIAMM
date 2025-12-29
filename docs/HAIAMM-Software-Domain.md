# HAIAMM v1.0 - Software Domain
## Security of AI Model Code, Applications, and Integration Layers

**Domain:** Software
**Version:** 1.0
**Last Updated:** December 2025

[← Back to Index](./HAIAMM-v1.0-Documentation-Index.md)

---

## Executive Summary

The Software Domain addresses security throughout the AI software development lifecycle, from model training code to production applications. This includes:

- **AI Model Code:** Training scripts, model architectures, inference code
- **Application Software:** User-facing applications leveraging AI
- **Integration Layers:** APIs, microservices, data pipelines
- **Development Tools:** IDEs, version control, CI/CD for AI

**Key Risks Addressed:**
- Model theft and reverse engineering
- Adversarial attacks on models
- Code injection in training pipelines
- Insecure AI API implementations
- Supply chain attacks on AI libraries

**Business Impact:**
- Protects intellectual property (model architectures)
- Prevents model manipulation and poisoning
- Ensures reliable AI system behavior
- Reduces security incidents in production
- Maintains compliance with AI regulations

---

## Domain Structure

### Business Functions

| Function | Focus | Practices |
|----------|-------|-----------|
| **Governance** | Strategy, policy, and education for AI software | SM, PC, EG |
| **Engineering** | Building secure AI software | TA, SR, SA |
| **Verification** | Testing AI software security | DR, CR, ST |
| **Operations** | Running secure AI systems | IM, EH, OE |

### Practice Summary

| ID | Practice Name | Level 1 Focus | Level 2 Focus | Level 3 Focus |
|----|--------------|--------------|--------------|--------------|
| SM | Strategy & Metrics | Create strategy | Measure goals | Optimize spending |
| PC | Policy & Compliance | Identify requirements | Document policies | Enforce compliance |
| EG | Education & Guidance | Awareness training | Role-based training | Culture of security |
| TA | Threat Assessment | Identify threats | Risk modeling | Attack modeling |
| SR | Security Requirements | High-level requirements | Detailed requirements | Vendor requirements |
| SA | Secure Architecture | Architecture review | Reference architectures | Validation |
| DR | Design Review | Point reviews | Complete reviews | Ongoing reviews |
| CR | Code Review | Checklist reviews | Automated + manual | Integrated reviews |
| ST | Security Testing | Penetration testing | Automated testing | Requirements-driven testing |
| IM | Issue Management | Track defects | Track status | Metrics-driven |
| EH | Environment Hardening | Configuration | Patching | Advanced hardening |
| OE | Operational Enablement | Documentation | Training | Incident drills |

---

## Governance Business Function

### Strategy & Metrics (SM)

**Objective:** Establish unified strategic roadmap for AI software security within the organization.

**Description:** Build and maintain an assurance program to better understand and manage AI software security risk. This includes defining security goals, measuring progress, and aligning security spending with business priorities.

#### Maturity Level 1: Establish AI Software Security Strategy

**Objective:** Create a documented strategy for improving AI software security.

**Activities:**
- Estimate overall business risk profile for AI systems
- Build and maintain an assurance program roadmap
- Identify key stakeholders and champions
- Document current AI software inventory

**Assessment Criteria:**

| ID | Question | Evidence Examples |
|----|----------|-------------------|
| SM-SW-L1-Q1 | Do you have a documented AI software security strategy? | Strategy document, roadmap, presentation to leadership |
| SM-SW-L1-Q2 | Is there a strategic plan for improving AI software security? | Multi-year roadmap, quarterly goals, improvement plans |
| SM-SW-L1-Q3 | Do you have management buy-in for AI security initiatives? | Approved budget, executive sponsor, steering committee |

**Success Metrics:**
- ✅ Strategy document reviewed and approved by leadership
- ✅ Security roadmap covers 12+ months
- ✅ At least 50% of AI projects aware of security strategy
- ✅ Dedicated budget allocated for AI security

**Personnel Required:**
- **CISO or Security Director** (10-15 hours): Strategy development, stakeholder engagement
- **AI/ML Lead** (10-15 hours): Technical input, AI-specific risks
- **Product Manager** (5-10 hours): Business alignment, prioritization
- **Engineering Manager** (5-10 hours): Feasibility assessment, resource planning

**Time to Implement:** 1-2 months
**Effort Estimate:** 1-2 person-months
**Cost Range:** $15,000 - $30,000 (labor)

**Dependencies:**
- None (foundational practice)

**Recommended First Practice:** Yes - start here before other practices

---

#### Maturity Level 2: Measure Security Goals for AI Software

**Objective:** Classify AI software by business risk and measure achievement of security goals.

**Activities:**
- Classify AI software components based on business risk (High/Medium/Low)
- Establish security goals tailored to each classification
- Implement metrics to track goal achievement
- Regularly review and adjust classifications

**Assessment Criteria:**

| ID | Question | Evidence Examples |
|----|----------|-------------------|
| SM-SW-L2-Q1 | Have you classified AI software components by business risk? | Classification scheme, asset inventory with risk ratings |
| SM-SW-L2-Q2 | Do you have tailored security goals for different AI software types? | Risk-based security requirements, testing depth by classification |
| SM-SW-L2-Q3 | Do you measure achievement of AI software security goals? | Security dashboards, KPI tracking, quarterly reports |

**Success Metrics:**
- ✅ 100% of AI software classified by risk
- ✅ Security requirements documented for each risk level
- ✅ Metrics collected for 80%+ of security goals
- ✅ Quarterly reviews of metric trends
- 📊 **Average security goal achievement:** >70%
- 📊 **High-risk applications with approved exceptions:** <10%

**Personnel Required:**
- **Security Architect** (20-30 hours): Classification framework, security goals
- **AI/ML Engineers** (15-25 hours each, 2-3 people): System inventory, risk assessment
- **Data Analyst** (10-15 hours): Metrics dashboard, reporting
- **Compliance Manager** (5-10 hours): Regulatory alignment

**Time to Implement:** 3-4 months
**Effort Estimate:** 3-5 person-months
**Cost Range:** $45,000 - $75,000 (labor + tools)

**Dependencies:**
- **SM Level 1 (this practice)**: Must have strategy before measuring
- **TA Level 1**: Threat understanding helps inform risk classification
- **SR Level 1**: Requirements help define goals

**Recommended Sequence:**
1. Complete SM Level 1
2. Start TA Level 1 (parallel track)
3. Then advance to SM Level 2

---

#### Maturity Level 3: Align Security Spending with Business Risk

**Objective:** Optimize security investments based on quantitative risk analysis and industry benchmarks.

**Activities:**
- Conduct periodic industry-wide cost comparisons
- Collect and analyze historical security spending data
- Calculate ROI for security initiatives
- Adjust budget allocation based on risk and effectiveness

**Assessment Criteria:**

| ID | Question | Evidence Examples |
|----|----------|-------------------|
| SM-SW-L3-Q1 | Do you benchmark AI software security costs against industry standards? | Industry reports, peer comparisons, consulting assessments |
| SM-SW-L3-Q2 | Do you track historical AI software security expenditure and ROI? | Multi-year spending data, ROI calculations, value demonstrations |
| SM-SW-L3-Q3 | Are AI software security investments aligned with business risk? | Risk-adjusted budgets, spend analysis by application tier |

**Success Metrics:**
- ✅ Annual benchmarking against 3+ industry sources
- ✅ 3+ years of historical spending data tracked
- ✅ ROI calculated for major security initiatives
- ✅ Security spend varies proportionally with risk classification
- 📊 **Security spend as % of AI development budget:** 8-15% (industry average)
- 📊 **ROI for security initiatives:** >200% (incident cost avoidance)
- 📊 **Budget variance from plan:** <10%

**Personnel Required:**
- **CFO/Finance Manager** (10-15 hours): Budget analysis, ROI calculation
- **Security Operations Manager** (15-20 hours): Historical data collection, reporting
- **Business Analyst** (20-30 hours): Benchmarking research, comparative analysis
- **CISO** (5-10 hours): Strategy alignment, executive reporting

**Time to Implement:** 4-6 months
**Effort Estimate:** 4-6 person-months
**Cost Range:** $60,000 - $90,000 (labor + research subscriptions)

**Dependencies:**
- **SM Level 2 (this practice)**: Need classification and metrics first
- **All Level 1 practices**: Cost data from all security activities
- **IM Level 2**: Issue tracking provides incident cost data

**Recommended Sequence:**
1. Achieve Level 2 maturity in SM, TA, SR
2. Establish 12+ months of metrics history
3. Then advance to SM Level 3

---

### Policy & Compliance (PC)

**Objective:** Understand and meet external compliance and regulatory requirements for AI systems while driving internal security standards.

**Description:** Establish policies and standards for AI software security, ensure compliance with regulations (GDPR, AI Act, etc.), and maintain documentation for audit purposes.

#### Maturity Level 1: Identify AI Compliance Obligations

**Objective:** Understand regulatory requirements affecting AI software and establish compliance tracking.

**Activities:**
- Identify applicable AI regulations (EU AI Act, GDPR, sector-specific)
- Document compliance obligations for each AI system
- Establish process to monitor regulatory changes
- Create compliance checklist for new AI projects

**Assessment Criteria:**

| ID | Question | Evidence Examples |
|----|----------|-------------------|
| PC-SW-L1-Q1 | Have you identified regulatory requirements affecting AI software? | Compliance matrix, regulatory inventory, legal assessments |
| PC-SW-L1-Q2 | Do you maintain documentation of AI software compliance obligations? | Compliance register, requirement mapping, system documentation |
| PC-SW-L1-Q3 | Do you monitor changes to AI software regulations? | Regulatory watch process, change log, alert subscriptions |

**Success Metrics:**
- ✅ All applicable regulations identified and documented
- ✅ Compliance obligations mapped to AI systems
- ✅ Regulatory monitoring process established
- ✅ Compliance checklist used in 80%+ of new projects
- 📊 **Regulatory changes identified within:** 30 days of publication
- 📊 **Compliance documentation completeness:** >90%

**Personnel Required:**
- **Legal/Compliance Manager** (15-25 hours): Regulatory research, obligation mapping
- **Privacy Officer** (10-15 hours): GDPR/privacy requirements
- **AI Ethics Lead** (10-15 hours): AI-specific regulations (if available)
- **Security Manager** (5-10 hours): Technical compliance translation

**Time to Implement:** 2-3 months
**Effort Estimate:** 2-3 person-months
**Cost Range:** $30,000 - $45,000 (labor + legal consultation)

**Dependencies:**
- **SM Level 1**: Strategy helps prioritize compliance efforts
- None (can start independently)

**Recommended First Practice:** Yes for regulated industries

---

#### Maturity Level 2: Document AI Security Policies

**Objective:** Establish formal, documented security policies for AI software development and operations.

**Activities:**
- Create AI-specific security policies
- Conduct regular policy compliance audits
- Communicate policies to development teams
- Establish policy exception process

**Assessment Criteria:**

| ID | Question | Evidence Examples |
|----|----------|-------------------|
| PC-SW-L2-Q1 | Do you have documented security policies for AI software? | Policy documents, standards, procedures |
| PC-SW-L2-Q2 | Do you audit AI software for policy compliance? | Audit reports, compliance scores, remediation plans |
| PC-SW-L2-Q3 | Are AI software policies communicated to relevant teams? | Training records, policy awareness surveys, acknowledgments |

**Success Metrics:**
- ✅ Comprehensive policy covering all AI software activities
- ✅ Quarterly compliance audits conducted
- ✅ 100% of team members trained on policies
- ✅ Policy exceptions tracked and reviewed
- 📊 **Policy compliance rate:** >85%
- 📊 **Audit findings closed within SLA:** >80%
- 📊 **Policy training completion:** >95%

**Personnel Required:**
- **Information Security Manager** (25-35 hours): Policy development, review cycles
- **Legal Counsel** (10-15 hours): Legal review, risk assessment
- **Internal Auditor** (15-25 hours): Audit framework, compliance testing
- **Training Coordinator** (10-15 hours): Communication plan, training delivery

**Time to Implement:** 4-6 months
**Effort Estimate:** 4-6 person-months
**Cost Range:** $60,000 - $90,000 (labor + audit tools)

**Dependencies:**
- **PC Level 1 (this practice)**: Regulations inform policies
- **SM Level 1**: Strategy aligns with policies
- **EG Level 1**: Training requires policies to exist

**Recommended Sequence:**
1. Complete PC Level 1 and SM Level 1
2. Draft policies (2-3 months)
3. Then implement PC Level 2

---

#### Maturity Level 3: Enforce AI Compliance with Consequences

**Objective:** Make compliance mandatory with formal enforcement, and continuously measure effectiveness.

**Activities:**
- Establish communication plan for regulators and auditors
- Implement automated policy compliance checks
- Enforce policy compliance with consequences
- Measure and report compliance effectiveness

**Assessment Criteria:**

| ID | Question | Evidence Examples |
|----|----------|-------------------|
| PC-SW-L3-Q1 | Do you have a communication plan for AI software regulators? | Regulator engagement plan, audit readiness procedures |
| PC-SW-L3-Q2 | Is AI software policy compliance mandatory and enforced? | Enforcement procedures, violation records, consequences applied |
| PC-SW-L3-Q3 | Do you measure effectiveness of AI software compliance activities? | Compliance metrics, trend analysis, effectiveness reports |

**Success Metrics:**
- ✅ Formal regulator communication process established
- ✅ Automated compliance checks in CI/CD
- ✅ 100% of violations result in documented action
- ✅ Quarterly effectiveness reviews conducted
- 📊 **Automated compliance check coverage:** >90% of policies
- 📊 **Policy violations:** Decreasing trend year-over-year
- 📊 **Audit findings (external):** Zero critical findings
- 📊 **Mean time to remediate violations:** <30 days

**Personnel Required:**
- **Chief Compliance Officer** (10-15 hours): Regulator relationships, enforcement
- **DevSecOps Engineer** (30-40 hours): Automated compliance tooling
- **Legal/Regulatory Affairs** (15-20 hours): Regulator communications
- **Quality Assurance Manager** (10-15 hours): Effectiveness measurement

**Time to Implement:** 6-9 months
**Effort Estimate:** 6-9 person-months
**Cost Range:** $90,000 - $135,000 (labor + automation tools)

**Dependencies:**
- **PC Level 2 (this practice)**: Must have policies before enforcing
- **CR Level 2 or ST Level 2**: Automated checks need code review/testing infrastructure
- **IM Level 2**: Issue tracking for compliance violations

**Recommended Sequence:**
1. Achieve Level 2 in PC, CR, and IM
2. Implement automation tooling (3-4 months)
3. Then advance to PC Level 3

---

### Education & Guidance (EG)

**Objective:** Provide security training and guidance to all personnel involved in AI software development and operations.

**Description:** Build a security-aware culture through training programs, secure coding guidelines, and ongoing education specific to AI security challenges.

#### Maturity Level 1: AI Security Awareness Training

**Objective:** Ensure all staff working with AI systems have basic security awareness.

**Activities:**
- Develop AI security awareness materials
- Conduct annual security training for all staff
- Provide secure AI coding guidelines
- Establish security champion program

**Assessment Criteria:**

| ID | Question | Evidence Examples |
|----|----------|-------------------|
| EG-SW-L1-Q1 | Do you provide AI security awareness training? | Training curriculum, attendance records, materials |
| EG-SW-L1-Q2 | Are secure AI coding guidelines available? | Guidelines document, wiki, code examples |
| EG-SW-L1-Q3 | Do you have AI security champions in teams? | Champion list, meeting notes, program charter |

**Success Metrics:**
- ✅ Annual training program established
- ✅ 95%+ of staff complete training
- ✅ Secure coding guidelines published and accessible
- ✅ Security champions in all AI development teams
- 📊 **Training completion rate:** >95%
- 📊 **Post-training assessment scores:** >80%
- 📊 **Security champion activity:** Monthly meetings

**Personnel Required:**
- **Security Trainer** (30-40 hours): Curriculum development, training delivery
- **AI Security Specialist** (20-30 hours): AI-specific content, guidelines
- **Technical Writer** (15-25 hours): Guidelines documentation
- **HR/Training Coordinator** (10-15 hours): Logistics, tracking

**Time to Implement:** 2-3 months
**Effort Estimate:** 3-4 person-months
**Cost Range:** $45,000 - $60,000 (labor + training platform)

**Dependencies:**
- **SM Level 1**: Strategy defines training priorities
- **PC Level 1 or 2**: Policies provide training content
- None (can start independently)

**Recommended First Practice:** Yes for culture building

---

#### Maturity Level 2: Role-Specific AI Security Training

**Objective:** Provide in-depth, role-specific security training for AI developers, data scientists, and operators.

**Activities:**
- Develop role-specific training tracks (ML engineers, data scientists, DevOps)
- Provide hands-on security labs and workshops
- Conduct quarterly refresher training
- Measure training effectiveness through assessments

**Assessment Criteria:**

| ID | Question | Evidence Examples |
|----|----------|-------------------|
| EG-SW-L2-Q1 | Do you have role-specific AI security training? | Training tracks, role-based curricula, skill matrices |
| EG-SW-L2-Q2 | Do you provide hands-on AI security labs? | Lab environments, workshop materials, completion records |
| EG-SW-L2-Q3 | Do you measure training effectiveness? | Assessment results, skills gap analysis, feedback surveys |

**Success Metrics:**
- ✅ 3+ role-specific training tracks available
- ✅ 80%+ of technical staff complete role training
- ✅ Hands-on labs for common AI attack scenarios
- ✅ Quarterly training completion reports
- 📊 **Role training completion:** >80% per role
- 📊 **Hands-on lab completion:** >70%
- 📊 **Skills assessment improvement:** +20% post-training
- 📊 **Security issues from trained vs untrained:** 50% reduction

**Personnel Required:**
- **Senior Security Engineer** (40-50 hours): Advanced content, lab design
- **ML Security Researcher** (30-40 hours): Attack scenarios, research
- **DevOps Security Lead** (20-30 hours): Operational security content
- **Instructional Designer** (20-30 hours): Learning experience, assessments

**Time to Implement:** 4-6 months
**Effort Estimate:** 5-7 person-months
**Cost Range:** $75,000 - $105,000 (labor + lab infrastructure)

**Dependencies:**
- **EG Level 1 (this practice)**: Baseline training must exist
- **TA Level 1 or 2**: Threat understanding informs training
- **CR Level 1 or ST Level 1**: Real-world findings provide training material

**Recommended Sequence:**
1. Complete EG Level 1
2. Gather 6+ months of security findings
3. Then implement EG Level 2

---

#### Maturity Level 3: Security Culture and Continuous Learning

**Objective:** Embed security into organizational culture with continuous learning and improvement.

**Activities:**
- Establish continuous learning program (lunch-and-learns, reading groups)
- Integrate security into performance reviews
- Gamify security training (CTFs, bug bounty internal programs)
- Measure cultural indicators (security attitude surveys)

**Assessment Criteria:**

| ID | Question | Evidence Examples |
|----|----------|-------------------|
| EG-SW-L3-Q1 | Do you have a continuous AI security learning program? | Learning platform, content library, engagement metrics |
| EG-SW-L3-Q2 | Is security integrated into performance evaluations? | Review criteria, security KPIs, recognition program |
| EG-SW-L3-Q3 | Do you measure security culture maturity? | Culture surveys, attitude assessments, trend analysis |

**Success Metrics:**
- ✅ Monthly security learning activities
- ✅ Security criteria in 100% of technical role reviews
- ✅ Internal CTF or bug bounty program running
- ✅ Annual culture surveys show improvement
- 📊 **Continuous learning participation:** >60% of technical staff
- 📊 **Security as performance factor:** 100% of reviews
- 📊 **Security culture score:** >75/100
- 📊 **Voluntary security initiative participation:** >40%
- 📊 **Security-related innovation submissions:** >10/quarter

**Personnel Required:**
- **Security Culture Lead** (ongoing, 20% FTE): Program management, content
- **Learning & Development Manager** (15-20 hours): Platform, gamification
- **HR Business Partner** (10-15 hours): Performance review integration
- **Security Researchers** (ongoing, various): Content creation, challenges

**Time to Implement:** 6-12 months
**Effort Estimate:** 8-12 person-months
**Cost Range:** $120,000 - $180,000 (labor + platforms + rewards)

**Dependencies:**
- **EG Level 2 (this practice)**: Role training must be mature
- **SM Level 2**: Metrics inform culture measurement
- **Multiple Level 2 practices**: Mature security program needed

**Recommended Sequence:**
1. Achieve Level 2 in EG, SM, and 2+ other practices
2. Build learning platform and content (3-6 months)
3. Then advance to EG Level 3

---

## Quick Reference: Governance Practices

### Maturity Dependencies

```
Level 3
  │
  ├─ SM-3 (depends on: SM-2, TA-2, SR-2, IM-2)
  ├─ PC-3 (depends on: PC-2, CR-2 or ST-2, IM-2)
  └─ EG-3 (depends on: EG-2, SM-2, multiple Level-2 practices)
  │
Level 2
  │
  ├─ SM-2 (depends on: SM-1, TA-1, SR-1)
  ├─ PC-2 (depends on: PC-1, SM-1, EG-1)
  └─ EG-2 (depends on: EG-1, TA-1, CR-1 or ST-1)
  │
Level 1
  │
  ├─ SM-1 (no dependencies - START HERE)
  ├─ PC-1 (minimal dependencies)
  └─ EG-1 (minimal dependencies)
```

### Recommended Implementation Sequence

**Phase 1 (Months 1-3):** Foundation
1. SM Level 1 - Strategy
2. EG Level 1 - Awareness
3. PC Level 1 - Compliance (if regulated)

**Phase 2 (Months 4-6):** Structure
4. TA Level 1 - Threats (Engineering function)
5. SR Level 1 - Requirements (Engineering function)
6. SM Level 2 - Metrics

**Phase 3 (Months 7-12):** Maturity
7. PC Level 2 - Policies
8. EG Level 2 - Role Training
9. CR Level 1 or ST Level 1 - Verification

**Phase 4 (Year 2+):** Optimization
10. SM Level 3 - Optimization
11. PC Level 3 - Enforcement
12. EG Level 3 - Culture

---

## Assessment Worksheet: Governance

**Assessment Date:** _________________
**Assessor(s):** _________________
**Assessment Team:** _________________

### Strategy & Metrics (SM)

| Level | Question | Yes | Partial | No | Evidence | Notes |
|-------|----------|-----|---------|----| ---------|-------|
| **L1** | Do you have a documented AI software security strategy? | ☐ | ☐ | ☐ | | |
| **L1** | Is there a strategic plan for improving AI software security? | ☐ | ☐ | ☐ | | |
| **L1** | Do you have management buy-in for AI security initiatives? | ☐ | ☐ | ☐ | | |
| **L2** | Have you classified AI software components by business risk? | ☐ | ☐ | ☐ | | |
| **L2** | Do you have tailored security goals for different AI software types? | ☐ | ☐ | ☐ | | |
| **L2** | Do you measure achievement of AI software security goals? | ☐ | ☐ | ☐ | | |
| **L3** | Do you benchmark AI software security costs against industry standards? | ☐ | ☐ | ☐ | | |
| **L3** | Do you track historical AI software security expenditure and ROI? | ☐ | ☐ | ☐ | | |
| **L3** | Are AI software security investments aligned with business risk? | ☐ | ☐ | ☐ | | |

**SM Maturity Score:** Level ___ (achieved when ≥80% Yes for all lower levels)

### Policy & Compliance (PC)

| Level | Question | Yes | Partial | No | Evidence | Notes |
|-------|----------|-----|---------|----| ---------|-------|
| **L1** | Have you identified regulatory requirements affecting AI software? | ☐ | ☐ | ☐ | | |
| **L1** | Do you maintain documentation of AI software compliance obligations? | ☐ | ☐ | ☐ | | |
| **L1** | Do you monitor changes to AI software regulations? | ☐ | ☐ | ☐ | | |
| **L2** | Do you have documented security policies for AI software? | ☐ | ☐ | ☐ | | |
| **L2** | Do you audit AI software for policy compliance? | ☐ | ☐ | ☐ | | |
| **L2** | Are AI software policies communicated to relevant teams? | ☐ | ☐ | ☐ | | |
| **L3** | Do you have a communication plan for AI software regulators? | ☐ | ☐ | ☐ | | |
| **L3** | Is AI software policy compliance mandatory and enforced? | ☐ | ☐ | ☐ | | |
| **L3** | Do you measure effectiveness of AI software compliance activities? | ☐ | ☐ | ☐ | | |

**PC Maturity Score:** Level ___ (achieved when ≥80% Yes for all lower levels)

### Education & Guidance (EG)

| Level | Question | Yes | Partial | No | Evidence | Notes |
|-------|----------|-----|---------|----|----- ----|-------|
| **L1** | Do you provide AI security awareness training? | ☐ | ☐ | ☐ | | |
| **L1** | Are secure AI coding guidelines available? | ☐ | ☐ | ☐ | | |
| **L1** | Do you have AI security champions in teams? | ☐ | ☐ | ☐ | | |
| **L2** | Do you have role-specific AI security training? | ☐ | ☐ | ☐ | | |
| **L2** | Do you provide hands-on AI security labs? | ☐ | ☐ | ☐ | | |
| **L2** | Do you measure training effectiveness? | ☐ | ☐ | ☐ | | |
| **L3** | Do you have a continuous AI security learning program? | ☐ | ☐ | ☐ | | |
| **L3** | Is security integrated into performance evaluations? | ☐ | ☐ | ☐ | | |
| **L3** | Do you measure security culture maturity? | ☐ | ☐ | ☐ | | |

**EG Maturity Score:** Level ___ (achieved when ≥80% Yes for all lower levels)

**Overall Governance Maturity:** ___ (average of SM, PC, EG)

---

**Next Steps:**
1. Identify highest priority gaps
2. Review dependencies before prioritizing improvements
3. Estimate resources needed (see personnel sections)
4. Create improvement roadmap
5. Schedule follow-up assessment

---

[← Back to Index](./HAIAMM-v1.0-Documentation-Index.md) | [Next: Engineering Function →](#engineering-business-function)
