# Human-Assisted Intelligence Scenarios - Real-World Examples for Each HAIAMM Practice

**How Organizations Deploy Human-Assisted Intelligence Across the 12 HAIAMM Practices**

This document provides concrete examples of HAI deployments, mapped to each HAIAMM practice. Use these scenarios to understand what HAIAMM assesses and how human oversight is critical.

---

## GOVERNANCE - How Organizations Govern Human-Assisted Intelligence

### SM - Strategy & Metrics

**HAI Implementation:** Customer Service Chatbot with Human Escalation

**What the organization does:**
- Deploys HAI chatbot to assist customer support with human agents available for escalation
- Tracks customer satisfaction, resolution rates, and human escalation frequency
- Measures effectiveness of human-AI collaboration
- Aligns HAI capabilities with business objectives and human oversight needs

**HAIAMM Assesses:**
- ✅ **Level 1:** Does the organization track basic metrics for HAI performance and human oversight?
- ✅ **Level 2:** Are HAI deployment decisions aligned with business risk and human oversight requirements?
- ✅ **Level 3:** Does the organization benchmark HAI effectiveness and human-AI collaboration quality?

**Real Scenario:**
> Retail company deploys HAI chatbot with human escalation for customer service. HAIAMM assessment reveals the organization tracks customer satisfaction but doesn't measure error rates, harmful responses, or human override patterns. The HAI chatbot has been providing incorrect return policy information for 3 months with humans rarely overriding. No metrics detected the problem. Assessment identifies gap in Strategy & Metrics maturity - insufficient measurement of human oversight effectiveness.

---

### PC - Policy & Compliance

**AI Implementation:** Document Analysis System

**What the organization does:**
- Uses AI to analyze and summarize legal documents
- Establishes policies for AI use in legal work
- Creates audit trails for AI-assisted decisions
- Ensures compliance with professional standards

**HAIAMM Assesses:**
- ✅ **Level 1:** Does the organization have basic policies governing AI system use?
- ✅ **Level 2:** Are AI system decisions auditable and explainable?
- ✅ **Level 3:** Does the organization proactively adapt policies to regulatory changes?

**Real Scenario:**
> Law firm uses AI for contract analysis. During HAIAMM assessment, auditor discovers no formal policy exists for reviewing AI-generated summaries. Junior associates rely entirely on AI output without validation. Gap identified: No governance framework for AI-assisted legal work (PC Level 1 failure). Significant malpractice risk.

---

### EG - Education & Guidance

**AI Implementation:** AI Coding Assistant

**What the organization does:**
- Deploys AI coding assistant to engineering teams
- Trains developers on appropriate use and limitations
- Establishes guidelines for when to override AI suggestions
- Creates awareness of AI-generated code risks

**HAIAMM Assesses:**
- ✅ **Level 1:** Are staff aware of AI system capabilities and limitations?
- ✅ **Level 2:** Is training provided on responsible use and human oversight?
- ✅ **Level 3:** Does the organization measure training effectiveness and adapt guidance?

**Real Scenario:**
> Tech company deploys GitHub Copilot enterprise-wide. HAIAMM assessment reveals no training provided on reviewing AI-generated code for security vulnerabilities. Developers accept suggestions without review. 60+ instances of SQL injection vulnerabilities merged to production. Gap: No Education & Guidance program for AI tool usage.

---

## BUILDING - How Organizations Build AI Systems Responsibly

### TA - Threat Assessment

**AI Implementation:** Medical Diagnosis AI Assistant

**What the organization does:**
- Identifies threats specific to AI system (bias, hallucination, adversarial inputs)
- Assesses risks of incorrect diagnoses
- Evaluates prompt injection and data poisoning risks
- Models failure scenarios and mitigation strategies

**HAIAMM Assesses:**
- ✅ **Level 1:** Does the organization identify basic threats to AI systems?
- ✅ **Level 2:** Are AI-specific threats (prompt injection, bias, hallucination) assessed?
- ✅ **Level 3:** Does threat modeling cover adversarial scenarios and cascading failures?

**Real Scenario:**
> Healthcare provider implements AI diagnostic assistant. HAIAMM assessment finds no threat modeling was performed for prompt injection attacks. Security researcher demonstrates they can manipulate AI into recommending harmful treatments through crafted patient notes. Gap in Threat Assessment (TA) maturity - AI-specific threats not considered.

---

### SR - Security Requirements

**AI Implementation:** Financial Trading Algorithm

**What the organization does:**
- Defines security requirements before AI deployment
- Specifies data access restrictions
- Requires output validation and human oversight
- Documents compliance requirements

**HAIAMM Assesses:**
- ✅ **Level 1:** Are basic security requirements defined for AI systems?
- ✅ **Level 2:** Do requirements cover data privacy, output validation, and human oversight?
- ✅ **Level 3:** Are requirements validated against industry standards and continuously improved?

**Real Scenario:**
> Investment firm deploys AI trading algorithm. HAIAMM assessment reveals no security requirements were documented before deployment. The AI has unrestricted access to all trading data and can execute trades without human approval. No audit logging of AI decisions. Gap: Missing Security Requirements (SR) definition phase entirely.

---

### SA - Secure Architecture

**AI Implementation:** HR Recruitment AI

**What the organization does:**
- Designs AI system with appropriate access controls
- Isolates AI processing from sensitive HR data
- Implements least-privilege principles
- Uses secure API design for AI integration

**HAIAMM Assesses:**
- ✅ **Level 1:** Does the AI system have basic access controls?
- ✅ **Level 2:** Is the AI architecture designed with security principles (isolation, least privilege)?
- ✅ **Level 3:** Does the architecture include defense-in-depth and security monitoring?

**Real Scenario:**
> Company implements AI resume screening system. HAIAMM assessment discovers the AI has unrestricted access to entire HR database including salary data, performance reviews, and personal information - far beyond what's needed for resume screening. No architectural review was performed. Gap in Secure Architecture (SA) practice.

---

## VERIFICATION - How Organizations Verify AI Systems Work Correctly

### DR - Design Review

**AI Implementation:** Loan Approval AI System

**What the organization does:**
- Reviews AI system design before deployment
- Validates decision logic against business requirements
- Ensures appropriate human oversight checkpoints
- Documents architectural decisions

**HAIAMM Assesses:**
- ✅ **Level 1:** Is AI system design reviewed before deployment?
- ✅ **Level 2:** Do reviews validate decision logic and fairness?
- ✅ **Level 3:** Are reviews performed by independent experts with AI domain knowledge?

**Real Scenario:**
> Bank deploys AI loan approval system. HAIAMM assessment reveals no design review was conducted. The AI's decision logic was never validated against fair lending regulations. Post-deployment analysis shows demographic bias in approvals. Regulatory investigation launched. Gap: No Design Review (DR) process for AI systems.

---

### CR - Code Review

**AI Implementation:** Content Moderation AI

**What the organization does:**
- Reviews AI system prompts and configurations
- Validates guardrails and safety constraints
- Reviews AI-generated outputs before production use
- Audits changes to AI system parameters

**HAIAMM Assesses:**
- ✅ **Level 1:** Are AI system configurations and prompts reviewed?
- ✅ **Level 2:** Are AI-generated outputs validated before use?
- ✅ **Level 3:** Is there continuous review of AI behavior and automated testing?

**Real Scenario:**
> Social media company deploys AI content moderation. HAIAMM assessment finds no review process for system prompts or guardrails. The AI was trained to be "helpful" but guidelines conflict with platform safety policies. AI approves violating content to be "helpful" to users. Gap in Code Review (CR) for AI system configurations.

---

### ST - Security Testing

**AI Implementation:** Customer Data Analysis AI

**What the organization does:**
- Tests AI system for prompt injection vulnerabilities
- Validates AI doesn't leak sensitive data in responses
- Tests for bias and fairness issues
- Red team testing for adversarial scenarios

**HAIAMM Assesses:**
- ✅ **Level 1:** Is basic functional testing performed on AI systems?
- ✅ **Level 2:** Are AI-specific vulnerabilities tested (prompt injection, data leakage)?
- ✅ **Level 3:** Is red team testing performed with adversarial attack scenarios?

**Real Scenario:**
> E-commerce company deploys AI customer support assistant with access to order database. HAIAMM assessment reveals no security testing was performed. Security researcher demonstrates prompt injection attack that extracts other customers' order details and personal information. Gap: No Security Testing (ST) for AI-specific vulnerabilities.

---

## OPERATIONS - How Organizations Operate AI Systems in Production

### EH - Environment Hardening

**AI Implementation:** AI-Powered Analytics Platform

**What the organization does:**
- Secures AI system runtime environment
- Implements least-privilege access for AI service accounts
- Protects API keys and model weights
- Hardens infrastructure hosting AI systems

**HAIAMM Assesses:**
- ✅ **Level 1:** Is the AI runtime environment secured with basic controls?
- ✅ **Level 2:** Are credentials, API keys, and sensitive configs properly protected?
- ✅ **Level 3:** Is the environment continuously monitored and hardened against new threats?

**Real Scenario:**
> Analytics company deploys AI data processing system. HAIAMM assessment discovers OpenAI API keys hardcoded in application code, committed to public GitHub repo. Model configuration files contain customer data examples. No secrets management. Gap in Environment Hardening (EH) - credentials exposed.

---

### ML - Monitoring & Logging

**AI Implementation:** Automated Email Response AI

**What the organization does:**
- Logs all AI inputs, outputs, and decisions
- Monitors AI system behavior for drift
- Tracks human override frequency
- Creates audit trails for compliance

**HAIAMM Assesses:**
- ✅ **Level 1:** Are AI system activities logged?
- ✅ **Level 2:** Can all AI decisions be audited with full context?
- ✅ **Level 3:** Is monitoring proactive with alerting on anomalous AI behavior?

**Real Scenario:**
> Customer service center deploys AI email response system. HAIAMM assessment finds minimal logging - only timestamps, no content. When customer complains about harmful response, cannot reconstruct what AI said or why. No audit trail for investigation or learning. Gap in Monitoring & Logging (ML) maturity.

---

### IM - Issue Management

**AI Implementation:** Predictive Maintenance AI

**What the organization does:**
- Tracks AI errors and false positives
- Investigates AI failures systematically
- Implements fixes and validates improvements
- Learns from incidents to improve AI systems

**HAIAMM Assesses:**
- ✅ **Level 1:** Are issues with AI systems tracked and managed?
- ✅ **Level 2:** Is there systematic root cause analysis for AI failures?
- ✅ **Level 3:** Are lessons learned incorporated into continuous improvement?

**Real Scenario:**
> Manufacturing company uses AI for predictive maintenance. HAIAMM assessment reveals no process for tracking AI false positives. The AI frequently predicts equipment failures that don't occur, causing unnecessary downtime. No investigation or improvement process. Teams start ignoring all AI alerts, including real ones. Gap: No Issue Management (IM) process for AI system errors.

---

## Cross-Domain Scenario: AI Chatbot Gone Wrong

**Company:** Healthcare Provider
**AI System:** Patient triage chatbot
**Domain:** Software, Data, Endpoints, Processes

### What Happened:
AI chatbot deployed to help patients assess symptoms and schedule appointments.

### HAIAMM Assessment Findings:

**Governance Gaps:**
- **SM:** No metrics tracking harmful responses or medical accuracy
- **PC:** No policy requiring human review of medical advice
- **EG:** Staff not trained to monitor or override AI decisions

**Building Gaps:**
- **TA:** No threat assessment for medical misinformation risk
- **SR:** No requirements for medical accuracy validation
- **SA:** AI has access to full medical records (overprivileged)

**Verification Gaps:**
- **DR:** No design review by medical professionals
- **CR:** No review of system prompts or medical knowledge base
- **ST:** No testing for harmful medical advice scenarios

**Operations Gaps:**
- **EH:** API keys exposed in client-side code
- **ML:** No logging of AI medical recommendations
- **IM:** No process to handle reports of incorrect advice

### Result:
AI chatbot told patient with chest pain to "rest and hydrate" instead of seeking emergency care. Patient suffered heart attack. Lawsuit, regulatory investigation, $3M settlement.

### HAIAMM Maturity Level:
**Overall: Level 0.3** - Ad-hoc AI implementation with critical governance and safety gaps across all practices.

---

## Key Takeaways

### Why These Scenarios Matter:

1. **Real Consequences:** AI systems without proper governance cause real harm
2. **Systematic Gaps:** Issues span multiple practices - not isolated failures
3. **Maturity Matters:** Higher HAIAMM maturity correlates with safer, more effective AI
4. **Prevention:** HAIAMM assessment identifies gaps BEFORE incidents occur

### Common Patterns Across Scenarios:

**Low Maturity (Level 0-1):**
- ❌ No formal policies or processes
- ❌ No testing or validation
- ❌ No monitoring or audit trails
- ❌ No training or guidance

**Medium Maturity (Level 1-2):**
- ⚠️ Basic processes exist but inconsistent
- ⚠️ Some testing but gaps in AI-specific risks
- ⚠️ Logging exists but insufficient for investigation
- ⚠️ Training provided but effectiveness not measured

**High Maturity (Level 2-3):**
- ✅ Systematic, documented processes
- ✅ Comprehensive testing including adversarial scenarios
- ✅ Proactive monitoring with alerting
- ✅ Continuous improvement culture

---

## Using These Scenarios

**For Self-Assessment:**
- Compare your AI implementations to these scenarios
- Identify which gaps exist in your organization
- Prioritize improvements based on risk

**For Executive Communication:**
- Use scenarios to illustrate why AI governance matters
- Demonstrate concrete risks of low maturity
- Justify investment in HAIAMM assessment

**For Training:**
- Share scenarios with teams implementing AI
- Discuss how each practice applies to your context
- Build awareness of AI implementation risks

---

**Every organization implementing AI systems should ask:**
*"Which of these scenarios could happen to us? How would HAIAMM help prevent them?"*

---

**Next Steps:**
1. Download HAIAMM assessment tool
2. Conduct self-assessment across your AI implementations
3. Identify maturity gaps using these scenarios as reference
4. Build improvement roadmap to reach target maturity levels
