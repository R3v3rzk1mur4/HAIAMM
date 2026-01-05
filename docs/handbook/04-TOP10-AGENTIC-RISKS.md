# OWASP Top 10 for Agentic Applications - HAIAMM Mapping

**Comprehensive security controls and measurement methodology for AI agent risks**

[Back to Index](00-INDEX.md) | [Quick Start](01-QUICK-START.md) | [LLM Risks](03-TOP10-LLM-RISKS.md)

---

## Overview

The OWASP Top 10 for Agentic Applications (2026) identifies the most critical security risks for autonomous AI systems. This document maps each risk to HAIAMM practices, provides measurable outcomes with full methodology, and offers practical implementation guidance.

**Why Agentic Risks Are Different:**
- Agents **act autonomously** - they don't just generate text, they take actions
- Agents **use tools** - file systems, APIs, databases, code execution
- Agents **chain decisions** - small errors cascade into major incidents
- Agents **persist state** - memory and context become attack surfaces

---

## Risk Summary Matrix

| ID | Risk | Severity | Likelihood | Primary Practices | Domain Focus |
|----|------|----------|------------|-------------------|--------------|
| ASI01 | Agent Goal Hijack | Critical | High | TA, SR, ST | Software, Processes |
| ASI02 | Tool Misuse & Exploitation | Critical | High | SA, PC, ML | Software, Endpoints |
| ASI03 | Identity & Privilege Abuse | Critical | Medium | SR, EH, ML | Infrastructure, Software |
| ASI04 | Agentic Supply Chain | High | Medium | TA, SA, IM | Vendors, Software |
| ASI05 | Unexpected Code Execution | Critical | Medium | SR, ST, EH | Software, Infrastructure |
| ASI06 | Memory & Context Poisoning | High | Medium | DR, ST, EH | Data, Software |
| ASI07 | Insecure Inter-Agent Comm | High | Low | SA, SR, ML | Software, Infrastructure |
| ASI08 | Cascading Failures | High | Medium | SA, IM, ML | Processes, Infrastructure |
| ASI09 | Human-Agent Trust Exploitation | Medium | High | EG, PC, ML | Processes, Endpoints |
| ASI10 | Rogue Agents | Critical | Low | TA, ML, IM | Software, Processes |

---

## ASI01: Agent Goal Hijack

### Risk Description

Attackers alter agent objectives through malicious content in documents, websites, or user inputs, causing the agent to pursue unintended goals such as data exfiltration, unauthorized actions, or serving attacker interests.

**Attack Vectors:**
- Malicious instructions embedded in documents the agent processes
- Adversarial content in web pages the agent browses
- User inputs that redefine agent objectives
- Poisoned context from previous interactions

**Real-World Impact:**
- Agent exfiltrates sensitive data to attacker-controlled endpoints
- Agent executes unauthorized transactions or modifications
- Agent bypasses human approval workflows
- Agent provides misleading information to users

### HAIAMM Practice Mapping

| Practice | Role | Domain |
|----------|------|--------|
| **TA** (Threat Assessment) | Identify goal hijack attack vectors | Software |
| **SR** (Security Requirements) | Define objective integrity requirements | Software |
| **ST** (Security Testing) | Test for goal hijack vulnerabilities | Software |
| **ML** (Monitoring & Logging) | Detect goal deviation at runtime | Processes |

### Measurable Outcomes

#### Outcome 1: Goal Hijack Detection Rate

**Target:** >90% of goal hijack attempts detected before action execution

**Measurement Formula:**
```
Detection Rate = (Detected Hijack Attempts / Total Hijack Attempts) × 100
```

**Data Sources:**
- Security testing results (red team exercises)
- Production monitoring alerts
- Incident reports

**Measurement Methodology:**
1. Conduct quarterly red team exercises with 50+ goal hijack test cases
2. Track detection by: input validation, behavioral analysis, human review
3. Categorize by attack vector (document, web, user input, context)
4. Calculate detection rate by vector and overall

**Validation:**
- Red team tests must include novel attack patterns (not just known signatures)
- Production detection must correlate with test results within 20%
- False positive rate must remain <10%

**Frequency:** Monthly for production metrics, Quarterly for red team validation

---

#### Outcome 2: Objective Integrity Verification

**Target:** 100% of high-risk agent actions verified against stated objectives

**Measurement Formula:**
```
Verification Coverage = (Verified High-Risk Actions / Total High-Risk Actions) × 100
```

**Data Sources:**
- Action classification logs
- Verification system audit trail
- Human approval records

**Measurement Methodology:**
1. Define "high-risk actions" (data access, external API calls, code execution)
2. Implement pre-action objective verification checkpoint
3. Log verification results with objective hash and action intent
4. Track bypass attempts and verification failures

**Validation:**
- Audit 5% of verified actions manually each month
- Verify classification accuracy through quarterly review
- Test verification system with adversarial inputs

**Frequency:** Continuous monitoring, Monthly reporting

---

#### Outcome 3: Mean Time to Detect Goal Deviation (MTTD)

**Target:** <5 minutes from goal deviation to alert

**Measurement Formula:**
```
MTTD = Σ(Alert Timestamp - Deviation Start) / Number of Deviations
```

**Data Sources:**
- Agent behavior logs with timestamps
- Alert system timestamps
- Incident timeline reconstructions

**Measurement Methodology:**
1. Instrument agents with behavioral telemetry
2. Define deviation indicators (unexpected tool use, data access patterns, output anomalies)
3. Correlate deviation start with alert generation
4. Track MTTD trend over time

**Validation:**
- Inject synthetic deviations monthly to test detection latency
- Compare automated detection with manual review findings
- Validate timestamp accuracy across systems

**Frequency:** Per-incident measurement, Monthly aggregation

---

#### Outcome 4: Successful Goal Hijack Rate

**Target:** <1% of goal hijack attempts succeed in production

**Measurement Formula:**
```
Success Rate = (Successful Hijacks / Total Hijack Attempts) × 100
```

**Data Sources:**
- Security incident reports
- Forensic analysis results
- Red team exercise outcomes

**Measurement Methodology:**
1. Define "successful hijack" (agent completed unintended action)
2. Track all suspected and confirmed hijack attempts
3. Categorize by outcome: blocked, detected-interrupted, successful
4. Calculate success rate with confidence intervals

**Validation:**
- All incidents classified by independent security analyst
- Quarterly comparison with industry benchmarks
- Annual third-party assessment

**Frequency:** Per-incident, Monthly reporting, Quarterly trending

---

### Implementation Guidance

**Level 1 (Foundation) - 40-60 hours:**
```
Week 1-2:
□ Document all agent objectives and allowed actions
□ Implement basic input validation for known hijack patterns
□ Add logging for agent objective changes
□ Define high-risk action categories
```

**Level 2 (Structured) - 80-120 hours:**
```
Week 3-6:
□ Implement behavioral baseline monitoring
□ Add pre-action verification for high-risk operations
□ Create red team test suite (50+ test cases)
□ Deploy anomaly detection on agent behavior
□ Establish human-in-the-loop for flagged actions
```

**Level 3 (Optimized) - 120-200 hours:**
```
Week 7-12:
□ Implement ML-based goal deviation detection
□ Automate response to detected hijack attempts
□ Integrate with threat intelligence feeds
□ Achieve <5 min MTTD target
□ Publish internal metrics dashboard
```

### Common Pitfalls

1. **Pattern Matching Only:** Relying solely on known patterns misses novel attacks
2. **Objective Drift:** Not updating objective definitions as agent capabilities change
3. **Alert Fatigue:** Too many false positives cause real alerts to be ignored
4. **Incomplete Coverage:** Only checking user inputs, not documents or web content

### Tools & Resources

**Open Source:**
- [Rebuff](https://github.com/protectai/rebuff) - Prompt injection detection
- [LLM Guard](https://github.com/protectai/llm-guard) - Input/output validation
- [Garak](https://github.com/leondz/garak) - LLM vulnerability scanner

**Commercial:**
- Protect AI Guardian
- Robust Intelligence
- HiddenLayer AISec

**References:**
- OWASP Agentic Security Guidelines
- MITRE ATLAS - AI Threat Matrix
- NIST AI RMF - Govern function

---

## ASI02: Tool Misuse & Exploitation

### Risk Description

Agents misuse legitimate tools due to ambiguous prompts, manipulated inputs, or inadequate access controls. Attackers exploit tool interfaces to perform unauthorized operations through the agent.

**Attack Vectors:**
- Ambiguous tool descriptions leading to misuse
- Parameter injection through user inputs
- Tool chaining to bypass individual tool restrictions
- Exploiting tool error handling for information disclosure

**Real-World Impact:**
- Unauthorized file system modifications
- Data exfiltration through legitimate APIs
- Privilege escalation via tool chaining
- Denial of service through resource exhaustion

### HAIAMM Practice Mapping

| Practice | Role | Domain |
|----------|------|--------|
| **SA** (Secure Architecture) | Design tool access architecture | Software |
| **PC** (Policy & Compliance) | Define tool usage policies | Processes |
| **ML** (Monitoring & Logging) | Monitor tool invocations | Software |
| **SR** (Security Requirements) | Specify tool constraints | Software |

### Measurable Outcomes

#### Outcome 1: Tool Permission Enforcement

**Target:** 100% of tool invocations validated against permission policy

**Measurement Formula:**
```
Enforcement Rate = (Validated Invocations / Total Invocations) × 100
```

**Data Sources:**
- Tool gateway logs
- Permission check audit trail
- Policy engine metrics

**Measurement Methodology:**
1. Implement centralized tool gateway with policy enforcement
2. Log all invocations with permission check results
3. Track policy violations and enforcement actions
4. Monitor for bypass attempts (direct tool access)

**Validation:**
- Test with unauthorized tool calls quarterly
- Verify no direct tool access paths exist
- Audit policy completeness monthly

**Frequency:** Continuous monitoring, Weekly reporting

---

#### Outcome 2: Tool Abuse Detection Rate

**Target:** >85% of tool abuse patterns detected within 1 minute

**Measurement Formula:**
```
Detection Rate = (Detected Abuse / Total Abuse Instances) × 100
Time to Detect = Alert Timestamp - First Abuse Indicator
```

**Data Sources:**
- Tool usage anomaly detection system
- Security incident reports
- Behavioral analysis logs

**Measurement Methodology:**
1. Define abuse patterns (unusual frequency, parameter patterns, sequences)
2. Implement real-time abuse detection
3. Track true positives, false positives, and missed detections
4. Measure time from first indicator to alert

**Validation:**
- Monthly abuse simulation exercises
- Quarterly red team testing of detection
- Compare detection with post-hoc forensics

**Frequency:** Continuous detection, Monthly metrics

---

#### Outcome 3: Least Privilege Compliance

**Target:** >95% of agents operate with minimum required permissions

**Measurement Formula:**
```
Compliance Rate = (Compliant Agents / Total Agents) × 100
Permission Ratio = Granted Permissions / Required Permissions
```

**Data Sources:**
- Agent configuration registry
- Permission audit reports
- Tool access logs

**Measurement Methodology:**
1. Define required permissions per agent type based on function
2. Audit granted vs. required permissions monthly
3. Track permission creep over time
4. Flag agents with unused permissions >30 days

**Validation:**
- Quarterly permission recertification
- Automated compliance checking
- Annual third-party audit

**Frequency:** Monthly audit, Quarterly recertification

---

#### Outcome 4: Tool Chain Risk Score

**Target:** All tool chains risk-scored, no high-risk chains without approval

**Measurement Formula:**
```
Risk Score = Σ(Tool Risk × Chain Position Weight × Data Sensitivity)
Coverage = (Scored Chains / Total Chains) × 100
```

**Data Sources:**
- Tool chain definitions
- Risk assessment database
- Approval workflow records

**Measurement Methodology:**
1. Enumerate all possible tool chains (automated discovery)
2. Assign risk scores based on tool combination
3. Require approval for chains exceeding threshold
4. Track chain execution against approved patterns

**Validation:**
- Test with novel chain combinations
- Review scoring algorithm quarterly
- Validate approvals are enforced

**Frequency:** Continuous scoring, Monthly review

---

### Implementation Guidance

**Level 1 (Foundation) - 30-50 hours:**
```
Week 1-2:
□ Inventory all agent tools and their capabilities
□ Document tool permissions per agent
□ Implement basic tool invocation logging
□ Define sensitive operations requiring approval
```

**Level 2 (Structured) - 60-100 hours:**
```
Week 3-5:
□ Deploy centralized tool gateway
□ Implement permission policy enforcement
□ Add tool usage anomaly detection
□ Create tool chain risk scoring
□ Establish approval workflow for high-risk operations
```

**Level 3 (Optimized) - 100-150 hours:**
```
Week 6-10:
□ Implement ML-based abuse detection
□ Automate permission right-sizing
□ Add predictive risk scoring for new chains
□ Achieve real-time enforcement with <100ms latency
□ Integrate with SIEM for correlation
```

### Common Pitfalls

1. **Overly Permissive Defaults:** Starting with broad access and never tightening
2. **Tool Description Vulnerabilities:** Ambiguous descriptions that can be exploited
3. **Chain Blindness:** Only securing individual tools, not combinations
4. **Enforcement Gaps:** Having policies but not enforcing them technically

### Tools & Resources

**Open Source:**
- [OPA (Open Policy Agent)](https://www.openpolicyagent.org/) - Policy enforcement
- [Falco](https://falco.org/) - Runtime security monitoring
- Tool permission frameworks (per platform)

**Commercial:**
- Anthropic Claude tool use controls
- OpenAI function calling guardrails
- LangChain security extensions

---

## ASI03: Identity & Privilege Abuse

### Risk Description

High-privilege credentials are unintentionally reused or escalated across agents without proper scoping. Agents accumulate permissions beyond what's needed, creating excessive blast radius.

**Attack Vectors:**
- Shared service account across multiple agents
- Credential inheritance in agent spawning
- Permission accumulation over time
- Impersonation of higher-privilege agents

**Real-World Impact:**
- Single compromised agent exposes all shared resources
- Lateral movement through agent infrastructure
- Privilege escalation to administrative access
- Audit trail confusion with shared identities

### HAIAMM Practice Mapping

| Practice | Role | Domain |
|----------|------|--------|
| **SR** (Security Requirements) | Define identity requirements | Infrastructure |
| **EH** (Environment Hardening) | Implement identity controls | Infrastructure |
| **ML** (Monitoring & Logging) | Monitor identity usage | Software |
| **SA** (Secure Architecture) | Design identity architecture | Infrastructure |

### Measurable Outcomes

#### Outcome 1: Unique Agent Identity Rate

**Target:** 100% of production agents have unique, non-shared identities

**Measurement Formula:**
```
Uniqueness Rate = (Agents with Unique ID / Total Agents) × 100
Shared Credential Count = Count of credentials used by >1 agent
```

**Data Sources:**
- Identity management system
- Agent configuration database
- Credential vault audit

**Measurement Methodology:**
1. Enumerate all agent identities in production
2. Map identities to credentials/service accounts
3. Identify shared credentials
4. Track remediation of shared identities

**Validation:**
- Monthly credential audit
- Automated shared credential detection
- Cross-reference with deployment records

**Frequency:** Weekly scanning, Monthly reporting

---

#### Outcome 2: Privilege Scope Compliance

**Target:** >95% of agents scoped to minimum required resources

**Measurement Formula:**
```
Scope Compliance = (Properly Scoped Agents / Total Agents) × 100
Over-Privilege Score = (Granted Access - Required Access) / Required Access
```

**Data Sources:**
- IAM policy analysis
- Resource access logs
- Agent function specifications

**Measurement Methodology:**
1. Define required resource access per agent function
2. Analyze actual IAM policies/permissions
3. Calculate over-privilege score per agent
4. Track scope reduction over time

**Validation:**
- Unused permission detection (>30 days)
- Quarterly access certification
- Red team privilege escalation testing

**Frequency:** Monthly analysis, Quarterly certification

---

#### Outcome 3: Credential Rotation Compliance

**Target:** 100% of agent credentials rotated within policy period

**Measurement Formula:**
```
Rotation Compliance = (Rotated On Time / Total Credentials) × 100
Days Since Rotation = Current Date - Last Rotation Date
```

**Data Sources:**
- Credential vault rotation logs
- Secret management system
- Compliance reporting

**Measurement Methodology:**
1. Define rotation policy (e.g., 90 days max)
2. Track credential age for all agents
3. Automate rotation where possible
4. Alert on approaching expiration

**Validation:**
- Test rotated credentials still function
- Verify old credentials are invalidated
- Audit rotation logs for anomalies

**Frequency:** Daily monitoring, Weekly compliance check

---

#### Outcome 4: Identity Anomaly Detection

**Target:** >80% of identity abuse patterns detected within 5 minutes

**Measurement Formula:**
```
Detection Rate = (Detected Anomalies / Total Anomalies) × 100
MTTD = Average(Alert Time - Anomaly Start Time)
```

**Data Sources:**
- Authentication logs
- Identity analytics platform
- SIEM alerts

**Measurement Methodology:**
1. Define identity anomaly indicators:
   - Impossible travel
   - Unusual access times
   - New resource access patterns
   - Failed authentication spikes
2. Implement real-time detection
3. Track detection accuracy and latency

**Validation:**
- Monthly simulated anomaly injection
- Correlation with incident forensics
- Tune detection thresholds quarterly

**Frequency:** Continuous monitoring, Monthly metrics

---

### Implementation Guidance

**Level 1 (Foundation) - 40-60 hours:**
```
Week 1-2:
□ Audit current agent identities and credentials
□ Eliminate shared credentials (create unique per agent)
□ Document required permissions per agent
□ Enable basic authentication logging
```

**Level 2 (Structured) - 80-120 hours:**
```
Week 3-6:
□ Implement workload identity (no static secrets)
□ Deploy automated credential rotation
□ Add privilege scope analysis
□ Implement identity anomaly detection
□ Create credential usage dashboard
```

**Level 3 (Optimized) - 120-180 hours:**
```
Week 7-12:
□ Implement just-in-time privilege elevation
□ Deploy ML-based identity analytics
□ Automate over-privilege remediation
□ Achieve zero standing privileges for high-risk agents
□ Integrate with zero trust architecture
```

### Common Pitfalls

1. **Shared Service Accounts:** Convenient but creates massive blast radius
2. **Static Long-Lived Credentials:** Never rotating API keys or tokens
3. **Over-Provisioning:** Granting broad access "just in case"
4. **Audit Trail Gaps:** Unable to attribute actions to specific agents

### Tools & Resources

**Open Source:**
- [SPIFFE/SPIRE](https://spiffe.io/) - Workload identity
- [Vault](https://www.vaultproject.io/) - Secret management
- [AWS IAM Access Analyzer](https://aws.amazon.com/iam/features/analyze-access/)

**Commercial:**
- CyberArk Privileged Access
- HashiCorp Vault Enterprise
- Azure Managed Identity

---

## ASI04: Agentic Supply Chain Vulnerabilities

### Risk Description

Compromised tools, plugins, templates, and MCP servers fetched at runtime introduce malicious code or behavior into agent systems. The dynamic nature of agent tool loading expands the attack surface.

**Attack Vectors:**
- Compromised tool packages in public registries
- Malicious MCP server implementations
- Typosquatting on popular tool names
- Compromised dependencies in tool chains

**Real-World Impact:**
- Backdoor installation through legitimate-looking tools
- Data exfiltration via compromised dependencies
- Credential theft through malicious plugins
- Supply chain attacks affecting multiple organizations

### HAIAMM Practice Mapping

| Practice | Role | Domain |
|----------|------|--------|
| **TA** (Threat Assessment) | Assess supply chain risks | Vendors |
| **SA** (Secure Architecture) | Design secure tool loading | Software |
| **IM** (Issue Management) | Track supply chain vulnerabilities | Vendors |
| **SR** (Security Requirements) | Define supply chain requirements | Vendors |

### Measurable Outcomes

#### Outcome 1: Tool Provenance Verification

**Target:** 100% of production tools have verified provenance

**Measurement Formula:**
```
Verification Rate = (Verified Tools / Total Tools) × 100
Provenance Coverage = (Tools with Known Origin / Total Tools) × 100
```

**Data Sources:**
- Tool registry with signatures
- SBOM (Software Bill of Materials)
- Verification logs

**Measurement Methodology:**
1. Maintain inventory of all agent tools
2. Require cryptographic signatures for tools
3. Verify signatures before loading
4. Track verification failures and blocks

**Validation:**
- Test with unsigned tools (must be blocked)
- Verify signature chain to trusted root
- Audit provenance claims quarterly

**Frequency:** Per-load verification, Weekly reporting

---

#### Outcome 2: Dependency Vulnerability Coverage

**Target:** >95% of tool dependencies scanned, <24hr remediation for critical

**Measurement Formula:**
```
Scan Coverage = (Scanned Dependencies / Total Dependencies) × 100
MTTR (Critical) = Average(Remediation Time for Critical Vulnerabilities)
```

**Data Sources:**
- Dependency scanning tools
- Vulnerability database
- Remediation tracking system

**Measurement Methodology:**
1. Implement automated dependency scanning in CI/CD
2. Scan runtime-loaded tools before deployment
3. Track time from detection to remediation
4. Categorize by severity (critical, high, medium, low)

**Validation:**
- Test scanner detection with known vulnerabilities
- Verify remediation actually removes vulnerability
- Audit false negative rate quarterly

**Frequency:** Daily scanning, Per-vulnerability tracking

---

#### Outcome 3: Supply Chain Incident Response Time

**Target:** <4 hours from supply chain advisory to assessment complete

**Measurement Formula:**
```
Response Time = Assessment Complete Timestamp - Advisory Published Timestamp
```

**Data Sources:**
- Security advisory feeds
- Assessment records
- Incident timeline

**Measurement Methodology:**
1. Subscribe to relevant security advisories (NVD, GitHub, vendor)
2. Implement automated matching to your tool inventory
3. Track time to complete impact assessment
4. Measure time to implement mitigations

**Validation:**
- Drill with simulated advisories quarterly
- Compare actual response times to targets
- Review assessment completeness

**Frequency:** Per-incident, Monthly aggregation

---

#### Outcome 4: Approved Tool Registry Compliance

**Target:** 100% of production agent tools from approved registry

**Measurement Formula:**
```
Compliance Rate = (Tools from Approved Registry / Total Tools) × 100
Shadow Tool Count = Tools loaded from unapproved sources
```

**Data Sources:**
- Approved tool registry
- Runtime tool loading logs
- Network egress monitoring

**Measurement Methodology:**
1. Establish approved tool registry with security review process
2. Enforce registry-only loading in production
3. Monitor for shadow tool loading attempts
4. Track approval queue and times

**Validation:**
- Attempt to load unapproved tool (must fail)
- Audit registry contents quarterly
- Review approval decisions for consistency

**Frequency:** Continuous enforcement, Weekly reporting

---

### Implementation Guidance

**Level 1 (Foundation) - 30-50 hours:**
```
Week 1-2:
□ Inventory all agent tools and dependencies
□ Create approved tool registry
□ Implement basic signature verification
□ Subscribe to security advisory feeds
```

**Level 2 (Structured) - 60-100 hours:**
```
Week 3-5:
□ Generate SBOM for all tools
□ Implement automated vulnerability scanning
□ Deploy registry-only enforcement
□ Create supply chain incident response playbook
□ Establish vendor security assessment process
```

**Level 3 (Optimized) - 100-150 hours:**
```
Week 6-10:
□ Implement real-time supply chain monitoring
□ Deploy behavioral analysis for loaded tools
□ Automate vulnerability remediation where safe
□ Achieve <4hr response target
□ Integrate with industry threat intelligence
```

### Common Pitfalls

1. **Trust by Default:** Loading tools without verification
2. **Stale SBOM:** Not updating dependency inventory
3. **Slow Response:** Taking days to assess supply chain alerts
4. **Incomplete Coverage:** Only scanning some tools or dependencies

### Tools & Resources

**Open Source:**
- [Syft](https://github.com/anchore/syft) - SBOM generation
- [Grype](https://github.com/anchore/grype) - Vulnerability scanning
- [Sigstore](https://www.sigstore.dev/) - Code signing

**Commercial:**
- Snyk
- Socket.dev
- Sonatype Nexus

---

## ASI05: Unexpected Code Execution (RCE)

### Risk Description

Agents generate or execute code unsafely without proper validation, leading to remote code execution vulnerabilities. This is especially dangerous when agents have code generation capabilities.

**Attack Vectors:**
- Prompt injection leading to malicious code generation
- Unsafe execution of agent-generated code
- Code injection through data sources
- Exploitation of code execution sandbox escapes

**Real-World Impact:**
- Full system compromise through code execution
- Data exfiltration via generated scripts
- Persistence mechanisms installed by agent
- Lateral movement through agent infrastructure

### HAIAMM Practice Mapping

| Practice | Role | Domain |
|----------|------|--------|
| **SR** (Security Requirements) | Define execution boundaries | Software |
| **ST** (Security Testing) | Test for RCE vulnerabilities | Software |
| **EH** (Environment Hardening) | Secure execution environment | Infrastructure |
| **IR** (Implementation Review) | Review generated code | Software |

### Measurable Outcomes

#### Outcome 1: Sandbox Escape Prevention

**Target:** 0 successful sandbox escapes in production

**Measurement Formula:**
```
Escape Rate = (Successful Escapes / Total Escape Attempts) × 100
Escape Attempt Count = Detected attempts to break sandbox
```

**Data Sources:**
- Sandbox monitoring logs
- Security incident reports
- Red team results

**Measurement Methodology:**
1. Deploy code execution sandboxes for all agent code execution
2. Monitor for sandbox escape indicators:
   - File system access outside allowed paths
   - Network connections to unauthorized hosts
   - Process spawning outside allowed list
   - Resource limit violations
3. Track all escape attempts and outcomes

**Validation:**
- Quarterly sandbox penetration testing
- Test with known escape techniques
- Verify sandbox configuration drift detection

**Frequency:** Continuous monitoring, Monthly reporting

---

#### Outcome 2: Code Validation Coverage

**Target:** 100% of agent-generated code validated before execution

**Measurement Formula:**
```
Validation Rate = (Validated Executions / Total Executions) × 100
```

**Data Sources:**
- Code validation gateway logs
- Execution audit trail
- Validation failure logs

**Measurement Methodology:**
1. Implement mandatory code validation pipeline
2. Define validation rules:
   - Static analysis (syntax, security patterns)
   - Allowlisted operations only
   - Resource limit verification
   - Dangerous function detection
3. Track validation results and execution decisions

**Validation:**
- Test with malicious code samples
- Verify bypass attempts are blocked
- Audit validation rule effectiveness

**Frequency:** Per-execution, Daily aggregation

---

#### Outcome 3: Execution Blast Radius Containment

**Target:** All code execution confined to dedicated, ephemeral environments

**Measurement Formula:**
```
Containment Rate = (Contained Executions / Total Executions) × 100
Shared Environment Count = Executions in non-isolated environments
```

**Data Sources:**
- Container/VM provisioning logs
- Execution environment inventory
- Network segmentation logs

**Measurement Methodology:**
1. Define execution environment requirements:
   - Ephemeral (destroyed after use)
   - Isolated (no shared resources)
   - Limited (restricted capabilities)
2. Track execution environment allocation
3. Monitor for container/VM reuse violations

**Validation:**
- Verify environment destruction after execution
- Test cross-execution data leakage
- Audit network isolation quarterly

**Frequency:** Continuous monitoring, Weekly reporting

---

#### Outcome 4: Dangerous Operation Detection

**Target:** >95% of dangerous operations detected and blocked

**Measurement Formula:**
```
Detection Rate = (Blocked Dangerous Ops / Total Dangerous Op Attempts) × 100
```

**Data Sources:**
- Code analysis results
- Execution monitoring
- Blocked operation logs

**Measurement Methodology:**
1. Define dangerous operations:
   - System calls (exec, fork, network bind)
   - File operations (write to system paths)
   - Resource operations (memory allocation, process creation)
2. Implement detection in validation and runtime
3. Track detection accuracy and bypass attempts

**Validation:**
- Test with known dangerous patterns
- Red team with novel techniques quarterly
- Tune detection based on false positive/negative rates

**Frequency:** Per-operation, Daily reporting

---

### Implementation Guidance

**Level 1 (Foundation) - 50-70 hours:**
```
Week 1-3:
□ Inventory all agent code execution capabilities
□ Implement basic sandboxing (Docker, gVisor)
□ Add static analysis for generated code
□ Block known dangerous functions
```

**Level 2 (Structured) - 100-150 hours:**
```
Week 4-8:
□ Deploy hardened sandbox (Firecracker, seccomp)
□ Implement comprehensive code validation pipeline
□ Add runtime monitoring for anomalies
□ Create ephemeral execution environments
□ Establish code execution approval workflow
```

**Level 3 (Optimized) - 150-220 hours:**
```
Week 9-16:
□ Implement ML-based code behavior prediction
□ Deploy formal verification for critical paths
□ Achieve zero escape rate target
□ Automate sandbox hardening updates
□ Integrate with vulnerability management
```

### Common Pitfalls

1. **Weak Sandboxes:** Using containers without additional hardening
2. **Validation Gaps:** Static analysis only, no runtime protection
3. **Persistent Environments:** Reusing execution environments
4. **Escape Complacency:** Assuming sandboxes are unbreakable

### Tools & Resources

**Open Source:**
- [gVisor](https://gvisor.dev/) - Application kernel sandboxing
- [Firecracker](https://firecracker-microvm.github.io/) - MicroVM isolation
- [Semgrep](https://semgrep.dev/) - Static analysis

**Commercial:**
- E2B Sandbox
- Modal
- AWS Lambda with security controls

---

## ASI06: Memory & Context Poisoning

### Risk Description

Attackers poison memory systems and RAG databases to influence future agent decisions. Persistent context creates an attack surface that affects all future interactions.

**Attack Vectors:**
- Injecting malicious content into vector stores
- Poisoning conversation history databases
- Manipulating agent memory through crafted interactions
- Corrupting RAG retrieval results

**Real-World Impact:**
- Agent provides incorrect information persistently
- Backdoor activation through poisoned context
- Data exfiltration through manipulated memory
- Trust erosion through unreliable agent behavior

### HAIAMM Practice Mapping

| Practice | Role | Domain |
|----------|------|--------|
| **DR** (Design Review) | Review memory architecture | Data |
| **ST** (Security Testing) | Test memory integrity | Software |
| **EH** (Environment Hardening) | Secure memory systems | Data |
| **ML** (Monitoring & Logging) | Monitor memory changes | Data |

### Measurable Outcomes

#### Outcome 1: Memory Integrity Verification

**Target:** 100% of memory retrievals verified for integrity

**Measurement Formula:**
```
Verification Rate = (Verified Retrievals / Total Retrievals) × 100
Integrity Failure Rate = (Failed Verifications / Total Verifications) × 100
```

**Data Sources:**
- Memory system access logs
- Integrity check results
- Retrieval audit trail

**Measurement Methodology:**
1. Implement cryptographic integrity for stored memories
2. Verify integrity on retrieval
3. Track verification failures and sources
4. Investigate and remediate integrity issues

**Validation:**
- Inject tampered memory entries (must be detected)
- Test with various tampering methods
- Verify restoration from backups

**Frequency:** Per-retrieval, Daily aggregation

---

#### Outcome 2: Memory Source Attribution

**Target:** >95% of memory entries have verified source attribution

**Measurement Formula:**
```
Attribution Rate = (Attributed Entries / Total Entries) × 100
```

**Data Sources:**
- Memory provenance logs
- Source verification records
- Attribution audit trail

**Measurement Methodology:**
1. Record source for all memory entries (user, system, agent, external)
2. Verify source authenticity (signatures, timestamps)
3. Track unattributed or questionable entries
4. Apply trust scores based on source

**Validation:**
- Test source spoofing attempts
- Audit attribution accuracy
- Verify trust scores affect retrieval priority

**Frequency:** Per-entry, Weekly reporting

---

#### Outcome 3: Context Poisoning Detection

**Target:** >80% of poisoning attempts detected within 24 hours

**Measurement Formula:**
```
Detection Rate = (Detected Attempts / Total Attempts) × 100
Time to Detect = Alert Timestamp - Poisoning Timestamp
```

**Data Sources:**
- Memory analysis logs
- Anomaly detection alerts
- Incident reports

**Measurement Methodology:**
1. Define poisoning indicators:
   - Sudden content pattern changes
   - Unusual source patterns
   - Embedding space anomalies
   - Contradictory information injection
2. Implement detection mechanisms
3. Track detection accuracy and timing

**Validation:**
- Monthly poisoning simulation exercises
- Compare automated detection with manual review
- Test novel poisoning techniques

**Frequency:** Continuous monitoring, Weekly metrics

---

#### Outcome 4: Memory Hygiene Compliance

**Target:** 100% of memory systems meet hygiene standards

**Measurement Formula:**
```
Hygiene Score = (Met Standards / Total Standards) × 100
```

**Data Sources:**
- Memory system configuration
- Retention policy compliance
- Access control audit

**Measurement Methodology:**
1. Define hygiene standards:
   - Retention limits (max age)
   - Access controls (who can write)
   - Validation requirements (what can be stored)
   - Backup and recovery (data protection)
2. Audit compliance monthly
3. Track remediation of gaps

**Validation:**
- Test retention enforcement
- Verify access controls
- Test backup and recovery

**Frequency:** Monthly audit, Quarterly review

---

### Implementation Guidance

**Level 1 (Foundation) - 30-50 hours:**
```
Week 1-2:
□ Inventory all agent memory and context systems
□ Implement basic access controls on memory stores
□ Add source attribution for new entries
□ Enable memory change logging
```

**Level 2 (Structured) - 60-100 hours:**
```
Week 3-5:
□ Implement cryptographic integrity verification
□ Deploy memory content validation
□ Add poisoning detection (anomaly-based)
□ Create memory backup and recovery procedures
□ Establish memory retention policies
```

**Level 3 (Optimized) - 100-150 hours:**
```
Week 6-10:
□ Implement ML-based poisoning detection
□ Deploy real-time memory health monitoring
□ Automate memory hygiene enforcement
□ Achieve >80% detection rate target
□ Integrate with incident response
```

### Common Pitfalls

1. **Trust All Content:** Treating all retrieved content as trustworthy
2. **No Attribution:** Unable to determine where memory entries came from
3. **Permanent Memory:** Never expiring or validating old entries
4. **Detection Gaps:** Only monitoring writes, not detecting subtle poisoning

### Tools & Resources

**Open Source:**
- Vector databases with integrity features (Pinecone, Weaviate)
- Data validation frameworks
- Anomaly detection libraries

**Commercial:**
- Memory management platforms with security
- RAG security solutions

---

## ASI07: Insecure Inter-Agent Communication

### Risk Description

Multi-agent message exchanges lack authentication, encryption, or semantic validation. Attackers can intercept, modify, or inject messages between agents.

**Attack Vectors:**
- Man-in-the-middle on agent communications
- Message spoofing between agents
- Replay attacks using captured messages
- Semantic injection through message manipulation

**Real-World Impact:**
- Agents acting on forged instructions
- Sensitive data exposed in transit
- Coordinated agent behavior disrupted
- Trust relationships between agents compromised

### HAIAMM Practice Mapping

| Practice | Role | Domain |
|----------|------|--------|
| **SA** (Secure Architecture) | Design secure communication | Software |
| **SR** (Security Requirements) | Define communication requirements | Infrastructure |
| **ML** (Monitoring & Logging) | Monitor inter-agent traffic | Software |
| **EH** (Environment Hardening) | Secure communication channels | Infrastructure |

### Measurable Outcomes

#### Outcome 1: Communication Encryption Coverage

**Target:** 100% of inter-agent communications encrypted in transit

**Measurement Formula:**
```
Encryption Rate = (Encrypted Communications / Total Communications) × 100
```

**Data Sources:**
- Network monitoring logs
- TLS/mTLS certificate inventory
- Communication protocol audit

**Measurement Methodology:**
1. Inventory all inter-agent communication channels
2. Verify encryption (TLS 1.3+, mTLS preferred)
3. Monitor for unencrypted traffic
4. Track encryption version and cipher strength

**Validation:**
- Network scanning for unencrypted traffic
- Certificate validity monitoring
- Quarterly cipher strength review

**Frequency:** Continuous monitoring, Weekly reporting

---

#### Outcome 2: Message Authentication Rate

**Target:** 100% of inter-agent messages authenticated

**Measurement Formula:**
```
Authentication Rate = (Authenticated Messages / Total Messages) × 100
Spoofing Attempt Count = Detected unauthenticated message attempts
```

**Data Sources:**
- Message authentication logs
- Signature verification results
- Spoofing detection alerts

**Measurement Methodology:**
1. Implement message signing for all agent communications
2. Verify signatures on receipt
3. Reject unauthenticated messages
4. Track authentication failures and spoofing attempts

**Validation:**
- Test with spoofed messages (must be rejected)
- Verify key management processes
- Audit signature verification implementation

**Frequency:** Per-message, Daily aggregation

---

#### Outcome 3: Communication Anomaly Detection

**Target:** >85% of communication anomalies detected within 5 minutes

**Measurement Formula:**
```
Detection Rate = (Detected Anomalies / Total Anomalies) × 100
MTTD = Average(Detection Time - Anomaly Start)
```

**Data Sources:**
- Communication monitoring platform
- Anomaly detection alerts
- Incident reports

**Measurement Methodology:**
1. Baseline normal inter-agent communication patterns
2. Define anomalies (unusual volume, new recipients, pattern changes)
3. Implement real-time detection
4. Track detection accuracy and timing

**Validation:**
- Monthly simulated anomaly injection
- Compare with forensic analysis
- Tune detection thresholds

**Frequency:** Continuous monitoring, Weekly metrics

---

### Implementation Guidance

**Level 1 (Foundation) - 30-40 hours:**
```
Week 1-2:
□ Inventory all inter-agent communication channels
□ Implement TLS for all agent communications
□ Add basic message logging
□ Document communication architecture
```

**Level 2 (Structured) - 60-80 hours:**
```
Week 3-4:
□ Deploy mTLS with certificate management
□ Implement message signing and verification
□ Add replay attack prevention (nonces, timestamps)
□ Create communication monitoring dashboard
```

**Level 3 (Optimized) - 80-120 hours:**
```
Week 5-8:
□ Implement semantic validation for messages
□ Deploy ML-based anomaly detection
□ Automate certificate rotation
□ Achieve real-time detection target
```

### Common Pitfalls

1. **Plain Text Protocols:** Using unencrypted communication channels
2. **Trust by Channel:** Assuming all messages on a channel are legitimate
3. **Missing Replay Protection:** No nonces or timestamp validation
4. **Semantic Blindness:** Verifying signatures but not message content sense

---

## ASI08: Cascading Failures

### Risk Description

Small errors propagate across planning, execution, and downstream systems. Agent architectures create complex dependencies where failures amplify.

**Attack Vectors:**
- Triggering initial errors that cascade
- Exploiting retry logic to amplify impact
- Resource exhaustion through cascading requests
- Data corruption propagating through pipelines

### HAIAMM Practice Mapping

| Practice | Role | Domain |
|----------|------|--------|
| **SA** (Secure Architecture) | Design resilient architecture | Processes |
| **IM** (Issue Management) | Manage cascading incidents | Infrastructure |
| **ML** (Monitoring & Logging) | Detect cascade initiation | Processes |
| **EH** (Environment Hardening) | Implement circuit breakers | Infrastructure |

### Measurable Outcomes

#### Outcome 1: Circuit Breaker Coverage

**Target:** 100% of agent dependencies protected by circuit breakers

**Measurement Formula:**
```
Coverage = (Protected Dependencies / Total Dependencies) × 100
Trip Rate = (Circuit Trips / Total Calls) × 100
```

**Measurement Methodology:**
1. Inventory all agent dependencies (APIs, services, data stores)
2. Implement circuit breakers for each
3. Configure appropriate thresholds
4. Track trips and recovery

---

#### Outcome 2: Cascade Detection Time

**Target:** Cascade initiation detected within 2 minutes

**Measurement Formula:**
```
MTTD = Alert Timestamp - First Failure Timestamp
```

---

### Implementation Guidance

**Level 1:** Implement basic circuit breakers and failure logging
**Level 2:** Deploy distributed tracing and cascade detection
**Level 3:** Implement predictive failure detection and auto-remediation

---

## ASI09: Human-Agent Trust Exploitation

### Risk Description

Users over-trust agent recommendations, allowing influence or data extraction. Agents manipulate human decision-making through social engineering patterns.

### HAIAMM Practice Mapping

| Practice | Role | Domain |
|----------|------|--------|
| **EG** (Education & Guidance) | Train users on AI limitations | Processes |
| **PC** (Policy & Compliance) | Define trust boundaries | Processes |
| **ML** (Monitoring & Logging) | Monitor high-impact decisions | Endpoints |

### Measurable Outcomes

#### Outcome 1: High-Impact Decision Review Rate

**Target:** 100% of agent-influenced high-impact decisions reviewed by human

**Measurement Formula:**
```
Review Rate = (Reviewed Decisions / Total High-Impact Decisions) × 100
```

---

#### Outcome 2: User AI Literacy Score

**Target:** >80% of users pass AI limitation awareness assessment

---

### Implementation Guidance

**Level 1:** Define high-impact decisions, implement review workflows
**Level 2:** Deploy user training program, add friction for risky decisions
**Level 3:** Implement adaptive trust calibration, measure decision quality

---

## ASI10: Rogue Agents

### Risk Description

Compromised or misaligned agents act harmfully while appearing legitimate. Detection is difficult because behavior appears normal to existing controls.

### HAIAMM Practice Mapping

| Practice | Role | Domain |
|----------|------|--------|
| **TA** (Threat Assessment) | Model rogue agent threats | Software |
| **ML** (Monitoring & Logging) | Detect behavioral anomalies | Processes |
| **IM** (Issue Management) | Respond to rogue agent incidents | Software |

### Measurable Outcomes

#### Outcome 1: Behavioral Baseline Coverage

**Target:** 100% of agents have established behavioral baselines

---

#### Outcome 2: Rogue Detection Time

**Target:** Rogue behavior detected within 1 hour of onset

---

#### Outcome 3: Containment Time

**Target:** <15 minutes from detection to agent isolation

---

### Implementation Guidance

**Level 1:** Establish behavioral baselines, implement isolation procedures
**Level 2:** Deploy anomaly detection, create response playbooks
**Level 3:** Implement ML-based detection, automate containment

---

## Document Information

| Field | Value |
|-------|-------|
| Document | OWASP Top 10 for Agentic Applications - HAIAMM Mapping |
| HAIAMM Version | 2.2 |
| OWASP Agentic Version | 2026 |
| Last Updated | January 2026 |

---

**Related Documents:**
- [Quick Start Guide](01-QUICK-START.md)
- [Top 10 LLM Risks](03-TOP10-LLM-RISKS.md)
- [Risk-Practice Matrix](05-RISK-PRACTICE-MATRIX.md)
- [Tools & Resources](08-TOOLS-RESOURCES.md)

[Back to Index](00-INDEX.md)
