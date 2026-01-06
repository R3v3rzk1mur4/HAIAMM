# Education & Guidance (EG) - Software Domain
## HAIAMM Assessment Questionnaire v2.0

**Practice:** Education & Guidance (EG)
**Domain:** Software
**Purpose:** Assess organizational maturity in education and guidance for Human Assisted Intelligence in secure software development

---

## Instructions

- Answer each question honestly based on **current, implemented practices** (not plans or aspirations)
- **"Yes" requires evidence** - Document proof for each affirmative answer
- **Answer progressively** - Complete all Level 1 questions before Level 2
- **Level progression** - Achieve ALL questions at lower level before advancing
- **Partial implementation = "No"** - Practice must be complete and systematic

---

## Level 1: Foundational
**Objective:** Establish foundational secure coding training and AI software security awareness

### Question 1: Foundational Secure Coding Training with AI Security Tool Introduction

**Q1.1:** Have all developers received foundational secure coding training that covers secure coding principles, common vulnerability patterns (OWASP Top 10, CWE Top 25), AI security tool capabilities and limitations, and how AI security tools integrate into development workflows?

**Evidence Required:**
- [ ] Foundational secure coding training program documented
- [ ] Training content includes:
  - Secure coding principles (input validation, authentication/authorization, encryption, least privilege)
  - Common vulnerability patterns (SQL injection, XSS, authentication bypass, insecure deserialization)
  - AI Security Tool Overview (SAST/DAST/SCA scanners, AI code review, GitHub Copilot Autofix, IDE security plugins)
  - AI Tool Capabilities (what AI can detect: code vulnerabilities, insecure dependencies, security anti-patterns)
  - AI Tool Limitations (what AI misses: business logic flaws, context-dependent risks, false positives, novel patterns)
  - Developer Workflow Integration (IDE plugins, PR checks, CI/CD pipeline gates, security dashboards)
- [ ] Language and framework-specific training available for primary tech stacks
- [ ] Training delivered to different audiences (developers, DevOps, QA, managers, AppSec teams)
- [ ] Training completion ≥80% of development organization
- [ ] Training materials updated within last 12 months

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

### Question 2: Security Awareness Campaigns and Developer Responsibility

**Q1.2:** Are security awareness campaigns actively communicating AI-assisted secure development value, real-world security vulnerability impacts, and developer security responsibility through multiple communication channels?

**Evidence Required:**
- [ ] Active security awareness program documented
- [ ] Awareness campaign content includes:
  - Security Vulnerability Real-World Impact (real breach stories, vulnerability consequences)
  - AI Security Wins (success stories where AI prevented vulnerabilities before production)
  - Secure Development Value (customer trust, regulatory compliance, reduced incident costs)
  - Developer Security Responsibility (security is part of professional software engineering)
  - Shift-Left Benefits (finding vulnerabilities early is cheaper and faster)
  - AI Security Tool Transparency (what AI tools do, privacy protections for code analysis)
- [ ] Multiple communication channels active:
  - Engineering all-hands presentations on security (at least quarterly)
  - Developer-focused security blog, newsletter, or Slack/Teams channel
  - Demo sessions showing AI security tools in action
  - Secure coding tips in development documentation
  - Lunch-and-learn sessions on security topics
- [ ] Developer security awareness measured (surveys, voluntary tool adoption, security discussions increasing)
- [ ] Evidence of positive security culture (security seen as enabler, not blocker)

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

### Question 3: Basic Secure Coding Guidance and Training Completion Tracking

**Q1.3:** Is basic secure coding guidance available for the primary programming languages and frameworks in use, with documented tracking of training completion showing ≥80% of developers have completed foundational secure coding training?

**Evidence Required:**
- [ ] Secure coding guidance available for primary tech stacks in use
- [ ] Guidance accessible to developers (developer portal, documentation, IDE integration)
- [ ] Guidance includes:
  - Basic secure coding patterns for each primary language/framework
  - Common vulnerability remediation examples
  - Links to AI security tool documentation
  - Quick-reference checklists for secure coding
- [ ] Training completion tracking system implemented
- [ ] Training completion metrics:
  - ≥80% of developers completed foundational secure coding training
  - Tracking by role, team, or tech stack
  - New developer onboarding includes security training
- [ ] Training completion data reviewed at least quarterly
- [ ] Evidence of training driving behavior change (developers using AI security tools, asking security questions)

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

**Level 1 Score:** _____ / 3 questions answered "Yes"

**Level 1 Achieved:** ☐ Yes (3/3) ☐ No (< 3/3)

---

## Level 2: Comprehensive
**Objective:** Implement comprehensive role-based training with hands-on labs and detailed secure coding guidance

**Prerequisites:** ALL Level 1 questions must be "Yes" to proceed to Level 2

### Question 4: Role-Based Training Programs with Hands-On Vulnerability Labs

**Q2.1:** Are comprehensive, tech-stack-specific secure coding training programs implemented with role-based content (backend, frontend, mobile, DevOps, security champions) and hands-on vulnerability remediation labs using AI security tools in realistic development scenarios?

**Evidence Required:**
- [ ] Role-based training programs developed and delivered:
  - Backend Developers (API security, database security, authentication/authorization, server-side vulnerabilities)
  - Frontend Developers (XSS prevention, CSP, CORS, authentication flows, client-side security)
  - Mobile Developers (iOS/Android security: secure data storage, authentication, SSL pinning)
  - DevOps Engineers (Secure CI/CD pipelines, infrastructure-as-code security, container security, secrets management)
  - Security Champions (Advanced training: threat modeling, security architecture, mentor training)
- [ ] Hands-on vulnerability labs implemented:
  - Vulnerability Remediation Exercises (practice fixing real vulnerabilities with AI assistance)
  - Secure Code Writing Labs (practice writing secure code from scratch)
  - AI Security Tool Training (hands-on practice with SAST/DAST, interpreting findings, tuning false positives)
  - Threat Modeling Workshops (practice threat modeling applications)
  - Secure Code Review Practice (peer review exercises, GitHub Copilot code evaluation)
  - Dependency Security Labs (SCA tool usage, updating vulnerable dependencies)
- [ ] Realistic training scenarios:
  - Labs based on real vulnerability types found in organization's code
  - CTF exercises or bug bounty-style challenges
  - Integration with actual development tools (run labs in real IDEs with AI tools)
- [ ] Training effectiveness tracked (completion rates, lab performance, post-training assessments)

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

### Question 5: Comprehensive Secure Coding Guidance and Reference Materials

**Q2.2:** Are secure coding standards and comprehensive reference materials maintained and kept current for all tech stacks in use, including AI-augmented guidance with secure code patterns, vulnerability remediation guides, and secure design patterns accessible at point of need?

**Evidence Required:**
- [ ] Comprehensive secure coding guidance maintained for all tech stacks:
  - Secure Coding Standards (organization-specific standards for each tech stack)
  - Vulnerability Remediation Guides (step-by-step fix guidance for common vulnerability types)
  - Secure Design Patterns (reference architectures, OAuth2 implementation, JWT authentication, encryption patterns)
  - Technology-Specific Security Guides (Spring Security, React security, Django security hardening)
  - AI Security Finding Interpretation (how to interpret SAST alerts, understanding severity ratings)
  - Secure Coding Checklists (API security checklist, authentication checklist, code review security checklist)
- [ ] AI-augmented guidance implemented:
  - Examples of secure code patterns with explanations
  - Common AI false positive patterns (help developers distinguish true vs. false findings)
  - GitHub Copilot secure prompt engineering guidance
  - AI-generated remediation examples
- [ ] Reference materials accessible at point of need:
  - Searchable developer portal with security documentation
  - Integrated into development environments (IDE plugins providing secure coding tips)
  - Linked from AI security tool findings (contextual help)
  - Code snippet repositories (secure code examples developers can copy/paste)
- [ ] Guidance kept current (quarterly review and update, updated when new vulnerability patterns emerge)
- [ ] Developer feedback integration (improve clarity based on questions)

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

### Question 6: Training Effectiveness Measurement and Developer Satisfaction

**Q2.3:** Is training effectiveness measured through security defect metrics (vulnerability density reduction), AI security tool usage improvements (false positive rates decreasing, finding acceptance rates increasing), and developer satisfaction with AI security tools improving?

**Evidence Required:**
- [ ] Security defect metrics tracked over time:
  - Vulnerability density (vulnerabilities per 1000 LOC) trending downward
  - Critical vulnerabilities in production trending downward
  - Time to remediate vulnerabilities decreasing
  - Historical data (≥6 months) showing improvement trends
- [ ] AI security tool usage improvements measured:
  - False positive rates decreasing from tuning (trending toward <10%)
  - Finding acceptance rates (% of AI findings developers fix vs. dismiss)
  - Time to remediate AI-detected vulnerabilities
  - Developer override rates and justifications tracked
- [ ] Developer satisfaction with AI security tools measured:
  - Regular developer surveys (at least annually)
  - AI security tools seen as helpful vs. hindering (majority positive)
  - Training quality satisfaction tracked
  - Developer feedback collected and acted upon
- [ ] Security integrated into code review culture:
  - Security discussed in PR reviews (evidence from code review comments)
  - Security questions in sprint retrospectives
  - Developers proactively asking security questions
- [ ] Evidence of training ROI (reduced vulnerability remediation costs, faster security review cycles)

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

**Level 2 Score:** _____ / 3 questions answered "Yes"

**Level 2 Achieved:** ☐ Yes (3/3) ☐ No (< 3/3)

---

## Level 3: Industry-Leading
**Objective:** Establish continuous learning culture with security champions and lead industry software security education

**Prerequisites:** ALL Level 2 questions must be "Yes" to proceed to Level 3

### Question 7: Security Champions Program with Continuous Learning

**Q3.1:** Is there an active security champions network with designated security advocates in each development team, continuous learning opportunities (secure coding guilds, security innovation time, internal conferences), and evidence of cross-team secure coding knowledge sharing?

**Evidence Required:**
- [ ] Security Champions Network established:
  - Developers in each team designated as security advocates (20-30% time allocation)
  - Champions Responsibilities defined (promote secure coding, code review security focus, answer security questions)
  - Advanced Champions Training provided (threat modeling, security architecture, advanced vulnerability analysis)
  - Champions Community active (regular meetings at least monthly, case studies, cross-team collaboration)
  - Champions Recognition program (visibility, career development, performance review recognition)
  - Champions Mentorship (1:1 secure coding guidance, pair programming on security features)
- [ ] Continuous secure coding learning opportunities:
  - Secure Coding Guilds (communities of practice for secure development, language-specific guilds)
  - Security Innovation Time (dedicated time for security skill development, CTF participation)
  - Conference and Training support (SANS courses, Black Hat, OWASP events, local security meetups)
  - Internal Security Conference (annual internal AppSec conference with talks, vendor presentations)
  - Secure Coding Challenges (monthly security challenges, rewards, gamification)
  - Open-Source Security Contributions encouraged
- [ ] Evidence of cross-team knowledge sharing (champions share learnings across teams, documented knowledge transfer)
- [ ] Active champions participation (≥70% of teams have active security champions)
- [ ] Champions avoiding burnout (workload balanced, support from AppSec team, clear scope)

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

### Question 8: Industry Secure Coding Education Contributions

**Q3.2:** Does your organization publish contributions to industry secure coding education through conference presentations, open-source training materials, OWASP contributions, academic partnerships, or secure coding standards development with documented industry impact?

**Evidence Required:**
- [ ] Industry secure coding education contributions (at least 2 per year):
  - Conference Presentations (OWASP AppSec, developer conferences, tech stack-specific events)
  - Open-Source Training Materials (vulnerability labs, secure code examples, AI security tool tutorials)
  - OWASP Contributions (OWASP Top 10, ASVS, secure coding guides, testing guides)
  - Academic Partnerships (guest lectures, capstone project mentorship, internship programs)
  - Secure Coding Standards contributions (language security working groups, framework security documentation)
  - AI Security Tool Feedback (provide feedback to AI security vendors to improve developer experience)
- [ ] Public evidence of contributions:
  - Published presentations, blog posts, white papers
  - Open-source repositories with training materials
  - OWASP project contributions documented
  - Academic collaboration agreements or guest lecture invitations
- [ ] Documented industry impact:
  - Training materials adopted by other organizations
  - Conference presentations well-attended (attendee counts, positive feedback)
  - OWASP contributions merged or recognized
  - Vendor product improvements based on feedback
- [ ] Industry recognition as thought leader in AI-assisted secure development

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

### Question 9: Rigorous Training Effectiveness Measurement and Security Defect Reduction

**Q3.3:** Is training effectiveness rigorously measured with quantified security defect reduction, security test coverage improvements, developer competency assessments, demonstrated training ROI, and continuous improvement cycles?

**Evidence Required:**
- [ ] Security defect reduction quantified:
  - Vulnerabilities per 1000 LOC reduced by ≥30% year-over-year
  - Critical vulnerabilities in production reduced by ≥50% year-over-year
  - Time to remediate vulnerabilities reduced by ≥40%
  - Historical data (≥12 months) showing sustained improvement
- [ ] Security test coverage improvements tracked:
  - Security-focused unit tests increasing
  - Integration tests with security scenarios increasing
  - Automated security tests coverage ≥80% of critical functionality
- [ ] Developer competency assessments:
  - Regular secure coding assessments (baseline and post-training)
  - CTF performance tracked
  - Security certifications attainment tracked
  - Developer skill level improvements documented
- [ ] Training ROI quantified:
  - Reduced vulnerability remediation costs calculated
  - Faster security review cycles measured
  - Reduced production security incidents calculated
  - ROI target ≥3:1 achieved or tracked toward
- [ ] Continuous improvement cycle implemented:
  - Quarterly secure development training reviews with data-driven improvements
  - Training focused on vulnerability types still appearing in code
  - Developer feedback drives training format and content improvements
  - Personalized learning paths based on developer tech stack and skill level
- [ ] Secure development culture evidenced by voluntary security behaviors (proactive threat modeling, security test writing, champions engagement)

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

**Level 3 Score:** _____ / 3 questions answered "Yes"

**Level 3 Achieved:** ☐ Yes (3/3) ☐ No (< 3/3)

---

## Practice Score Calculation

### Simplified Scoring (Recommended)

```
Level 1 Achieved (all 3 "Yes"): 1.0 point
Level 2 Achieved (all 3 "Yes"): +1.0 point (total 2.0)
Level 3 Achieved (all 3 "Yes"): +1.0 point (total 3.0)
```

**EG-Software Practice Score:** _______ / 3.0

### Precise Scoring (For Formal Audits)

```
L1_score = (L1 "Yes" answers) / 3
L2_score = (L2 "Yes" answers) / 3 × L1_score
L3_score = (L3 "Yes" answers) / 3 × L2_score

Practice Score = L1_score + L2_score + L3_score
```

**EG-Software Practice Score (Precise):** _______ / 3.0

---

## Assessment Summary

**Assessment Date:** _________________________________

**Assessor(s):** _____________________________________

**HAI System(s) Assessed:** __________________________

**Overall Maturity Level:**
- ☐ Level 0 (Score < 1.0): Ad-hoc, minimal secure coding education
- ☐ Level 1 (Score 1.0 - 1.9): Foundational secure coding training and awareness campaigns
- ☐ Level 2 (Score 2.0 - 2.9): Comprehensive role-based training with hands-on labs and detailed guidance
- ☐ Level 3 (Score 3.0): Continuous learning culture with security champions and industry leadership

**Strengths:**

_________________________________________________________________

**Gaps:**

_________________________________________________________________

**Priority Improvements:**

_________________________________________________________________

**Re-Assessment Date:** _________________________________

---

## Evidence Repository

Link all evidence documents here for audit trail:

| Question | Evidence Document | Location | Date | Owner |
|----------|------------------|----------|------|-------|
| Q1.1 | | | | |
| Q1.2 | | | | |
| Q1.3 | | | | |
| Q2.1 | | | | |
| Q2.2 | | | | |
| Q2.3 | | | | |
| Q3.1 | | | | |
| Q3.2 | | | | |
| Q3.3 | | | | |

---

## Education & Guidance Specific Notes

**Training Programs Covered:**
- [ ] Foundational secure coding training (OWASP Top 10, CWE Top 25)
- [ ] AI security tool training (SAST/DAST/SCA capabilities and limitations)
- [ ] Role-based training (backend, frontend, mobile, DevOps, security champions)
- [ ] Hands-on vulnerability labs (remediation exercises, threat modeling, code review)
- [ ] Language/framework-specific training (Java, Python, JavaScript, Go, etc.)

**Awareness Campaign Elements:**
- [ ] Security vulnerability real-world impact (breach stories, consequences)
- [ ] AI security wins (success stories, vulnerabilities prevented)
- [ ] Developer security responsibility messaging
- [ ] Shift-left benefits communication
- [ ] Multiple communication channels (all-hands, blog, Slack, demos, lunch-and-learns)

**Secure Coding Guidance Types:**
- [ ] Secure coding standards (organization-specific for each tech stack)
- [ ] Vulnerability remediation guides (step-by-step fix guidance)
- [ ] Secure design patterns (OAuth2, JWT, encryption patterns)
- [ ] Technology-specific security guides (Spring Security, React security, Django security)
- [ ] AI security finding interpretation guidance
- [ ] Secure coding checklists (API security, authentication, code review)

**Security Champions Program (Level 3):**
- [ ] Security champions network established (20-30% time allocation)
- [ ] Champions responsibilities defined (promote secure coding, mentor peers)
- [ ] Advanced champions training provided
- [ ] Champions community active (regular meetings, knowledge sharing)
- [ ] Champions recognition program
- [ ] Continuous learning opportunities (guilds, innovation time, conferences, internal conference, challenges)

**Training Effectiveness Metrics:**
- [ ] Security defect reduction (vulnerabilities per 1000 LOC, critical vulnerabilities in production)
- [ ] AI security tool effectiveness (false positive rates, finding acceptance rates, time to remediate)
- [ ] Developer competency assessments (baseline and post-training, CTF performance, certifications)
- [ ] Training ROI quantified (reduced remediation costs, faster security reviews, reduced incidents)
- [ ] Developer satisfaction tracked (AI tools seen as helpful, training quality)
- [ ] Security test coverage improvements

---

**Document Version:** 2.0
**Last Updated:** 2025-12-29
**Next Review:** Quarterly or after significant HAI system changes
