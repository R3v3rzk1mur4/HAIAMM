# Arcanum Prompt Injection Taxonomy Integration Proposal
## HAIAMM v2.1 Enhancement

**Date**: 2025-12-26
**Status**: PROPOSAL - Awaiting User Approval
**Source**: [Arcanum Prompt Injection Taxonomy](https://github.com/Arcanum-Sec/arc_pi_taxonomy) by Jason Haddix

---

## Executive Summary

The Arcanum Prompt Injection Taxonomy provides a comprehensive classification of prompt injection attacks, techniques, and evasions highly relevant to AI-operated security systems. This proposal outlines how to safely integrate this knowledge into HAIAMM to strengthen guidance for securing AI systems against prompt injection attacks.

**Key Benefit**: AI security systems (SAST, DAST, CSPM, EDR, DLP, SOAR) use LLMs and are vulnerable to prompt injection. This taxonomy provides foundational security guidance.

---

## Taxonomy Overview

### Structure
The Arcanum taxonomy organizes prompt injection knowledge into:

1. **Attack Intents** (13 categories) - Goals attackers aim to achieve
2. **Attack Techniques** (18 categories) - Methods to execute attacks
3. **Attack Evasions** (20 categories) - Ways to hide/obfuscate attacks
4. **Utilities** - Supporting resources

### Additional Resources
- **32 Threat Modeling Questions** - Organized by category (inputs, ecosystem, model, prompts, data, app, pivoting, monitoring)
- **5-Layer Defense Checklist** - Ecosystem, Model, Prompt, Data, Application
- **Probe Library** - For identifying AI-enabled endpoints

---

## Attack Intents (13 Categories)

1. **API Enumeration** - Discovering API endpoints
2. **Attack Users** - Targeting end users
3. **Business Integrity** - Compromising business operations
4. **Data Poisoning** - Corrupting training/operational data
5. **Denial of Service** - Rendering services unavailable
6. **Discuss Harm** - Requesting harmful information
7. **Generate Image** - Misusing image generation
8. **Get Prompt Secret** - Extracting hidden configurations
9. **Jailbreak** - Circumventing safety constraints
10. **Multi-Chain Attacks** - Combined multi-step exploits
11. **System Prompt Leak** - Revealing system instructions
12. **Test Bias** - Identifying model bias
13. **Tool Enumeration** - Discovering available tools

---

## Attack Techniques (18 Categories)

1. **Act as Interpreter** - Role-playing/assuming identities
2. **Anti-Harm Coercion** - Bypassing safety via persuasion
3. **ASCII** - ASCII character encoding attacks
4. **Binary Streams** - Binary data exploitation
5. **Cognitive Overload** - Overwhelming with complexity
6. **Contradiction** - Logical inconsistencies
7. **End Sequences** - Manipulating termination patterns
8. **Framing** - Recontextualizing requests
9. **Inversion** - Reversing instructions
10. **Link Injection** - Malicious references/redirects
11. **Memory Exploitation** - Context window vulnerabilities
12. **Meta Prompting** - Prompts about prompting
13. **Narrative Smuggling** - Harmful instructions in stories
14. **Puzzling** - Riddles/obfuscated logic
15. **Rule Addition** - New constraints mid-conversation
16. **Russian Doll** - Nested prompt injection
17. **Spatial Byte Arrays** - Spatial formatting with encoded data
18. **Variable Expansion** - Variable substitution exploitation

---

## Attack Evasions (20 Categories)

1. **Alt Language** - Alternative languages
2. **Base64** - Base64 encoding
3. **Case Changing** - Case manipulation
4. **Cipher** - Cipher-based obfuscation
5. **Emoji** - Emoji-based evasion
6. **Fictional Language** - Fictional language encoding
7. **Graph Nodes** - Graph node evasion
8. **Hex** - Hexadecimal encoding
9. **JSON** - JSON-based evasion
10. **Link Smuggling** - URL/link smuggling
11. **Markdown** - Markdown formatting evasion
12. **Metacharacter Confusion** - Metacharacter exploitation
13. **Morse** - Morse code encoding
14. **Phoenetic Substitution** - Phonetic substitution
15. **Reverse** - Text reversal
16. **Spaces** - Whitespace manipulation
17. **Splats** - Splat operator evasion
18. **Stego** - Steganography
19. **Waveforms** - Waveform-based encoding
20. **XML** - XML-based evasion

---

## 32 Threat Modeling Questions (by Category)

### 1. System Inputs & Entry Points (4 questions)
- User prompt submission interfaces
- Indirect input vectors (file uploads, document processing)
- Authentication mechanisms across channels
- Input validation at each entry point

### 2. Ecosystem Vulnerabilities (4 questions)
- Third-party components and dependencies
- Security updates and library maintenance
- Infrastructure hosting vulnerabilities
- Network attack surfaces

### 3. Model Security (4 questions)
- Model type and origin classification
- Known model weaknesses
- Susceptibility to adversarial/jailbreak attacks
- Inference manipulation protections

### 4. Prompt Engineering Security (4 questions)
- System prompt and instruction security
- Prompt injection attack prevention
- Malicious instruction filtering
- Exposure risks from prompt leakage

### 5. Data Security (4 questions)
- Sensitive data processing scope
- Training/fine-tuning and user data protections
- Vector database and embedding safeguards
- Data retention and deletion protocols

### 6. Application Security (4 questions)
- Frontend and API layer security
- Authentication and authorization controls
- Rate limiting and abuse prevention
- Behavioral monitoring systems

### 7. Pivoting Potential (4 questions)
- Cross-system pivot risks
- Lateral movement pathways
- Access to sensitive internal systems
- Compromise blast radius assessment

### 8. Monitoring & Response (4 questions)
- Attack detection and alerting mechanisms
- Incident response procedures
- Security log collection and analysis
- Emerging threat adaptation processes

---

## 5-Layer Defense Checklist

### Layer 1: Ecosystem Security
- Maintain current OSS with security patches
- Eliminate latent vulnerabilities
- Enable MFA for admin access
- Configure IAM appropriately
- Monitor suspicious access patterns
- Protect logging systems

### Layer 2: Model Protection
- Select models with robust safety mechanisms
- Fine-tune to minimize harmful outputs
- Deploy external prompt injection protections
- Include legal disclaimers
- Conduct regular security assessments

### Layer 3: Prompt Defense
- Apply system-level prompt safeguards
- Exclude sensitive data from system prompts
- Implement request throttling
- Limit context window scope

### Layer 4: Data Safeguarding
- Remove PII before RAG ingestion
- Restrict API-connected tools to minimal permissions
- Limit data access to operational requirements
- Prefer read-only API interactions

### Layer 5: Application Hardening
- Validate inputs and encode outputs
- Restrict diagnostic logging visibility
- Sandbox AI components from critical infrastructure

---

## Proposed HAIAMM Integration

### Practice 1: Threat Assessment (TA)

**Add Prompt Injection Threat Category**

**For All Domains** (Software, Infrastructure, Endpoints, Data, Processes, Vendors):
- Add "Prompt Injection Attacks" as a primary threat category
- Include 13 attack intents as specific threat scenarios
- Map to MITRE ATLAS framework where applicable

**Specific Additions**:

**TA-Software**:
- Add prompt injection threats to AI model threat modeling
- Include system prompt leakage, jailbreak, multi-chain attacks
- Add threat: "Adversary extracts system prompts revealing security logic"

**TA-Data**:
- Add prompt injection for data exfiltration
- Data poisoning via prompt injection
- Privacy violations through prompt manipulation

**TA-Processes** (SOAR):
- Add prompt injection to abuse automated workflows
- Alert triage manipulation via prompt injection
- Playbook execution hijacking

**TA-Vendors**:
- Vendor AI system prompt injection risks
- SBOM manipulation via prompt injection to vendor systems

---

### Practice 2: Security Requirements (SR)

**Add Prompt Injection Prevention Requirements**

**For All Domains**:
- **SR-PROMPT-001**: System prompts must not contain sensitive data (credentials, API keys, PII)
- **SR-PROMPT-002**: Input validation must sanitize prompt injection patterns
- **SR-PROMPT-003**: Context window must be scoped to prevent memory exploitation
- **SR-PROMPT-004**: Rate limiting must prevent prompt enumeration attacks
- **SR-PROMPT-005**: Model outputs must be validated/sanitized before execution

**Domain-Specific Requirements**:

**SR-Software**:
- Code generation models must not execute arbitrary code from prompts
- SAST/DAST systems must validate LLM outputs before applying fixes
- API responses must be sanitized to prevent injection in downstream prompts

**SR-Data**:
- DLP classification models must resist prompt injection to misclassify data
- RAG systems must sanitize retrieved documents before LLM ingestion
- PII must be removed before inclusion in prompts

**SR-Processes** (SOAR):
- Alert triage models must validate prompts before decision-making
- Playbook parameters must be validated to prevent injection
- Action outputs must be sanitized before inclusion in subsequent prompts

---

### Practice 3: Security Architecture (SA)

**Add Prompt Injection Defense Architecture**

**Defense-in-Depth Layers** (from Arcanum 5-Layer Model):

1. **Ecosystem Layer**:
   - Dependency management for LLM libraries
   - MFA for LLM API access
   - Network segmentation for AI components

2. **Model Layer**:
   - Select models with built-in safety mechanisms
   - External prompt injection detection layer (e.g., Lakera Guard, Azure AI Content Safety)
   - Model output validation before execution

3. **Prompt Layer**:
   - Separate user prompts from system prompts
   - Prompt templates with parameter validation
   - Context window scoping
   - Sensitive data exclusion from prompts

4. **Data Layer**:
   - PII removal before RAG ingestion
   - Read-only API permissions for LLM-connected tools
   - Data access logging

5. **Application Layer**:
   - Input validation and output encoding
   - Sandboxed LLM execution environment
   - Least privilege for LLM service accounts

**Architecture Patterns**:
- **Transformation Intermediaries**: Validate/sanitize between user input and LLM
- **Prompt Firewall**: Dedicated component to detect/block injection attempts
- **Output Validation**: Validate LLM outputs before taking actions

---

### Practice 4: Security Testing (ST)

**Add Prompt Injection Testing Methodology**

**Testing Categories**:

1. **Attack Intent Testing**:
   - Test all 13 attack intents against AI systems
   - System prompt leak attempts
   - Jailbreak attempts (safety constraint bypass)
   - Tool enumeration via prompts
   - Data poisoning through prompt manipulation
   - DoS via resource-intensive prompts

2. **Attack Technique Testing**:
   - Test 18 attack techniques
   - Role-playing attacks (act as interpreter)
   - Cognitive overload attacks
   - Nested prompt injection (Russian doll)
   - Narrative smuggling
   - Memory exploitation (context window abuse)

3. **Evasion Testing**:
   - Test 20 evasion techniques
   - Base64/hex encoding evasion
   - Alternative language evasion
   - JSON/XML/Markdown injection
   - Emoji-based evasion
   - Steganography

4. **Adversarial Prompt Testing**:
   - Use Arcanum probe library for discovery
   - Automated prompt fuzzing
   - Red team exercises with prompt injection

**Test Coverage Requirements**:
- [ ] Test all user-controlled prompt inputs
- [ ] Test indirect prompt injection vectors (file uploads, RAG documents)
- [ ] Test prompt injection in multi-turn conversations
- [ ] Test prompt injection with tool calling/function execution
- [ ] Test cross-prompt contamination (conversation history)

**Success Criteria**:
- ≥95% of prompt injection attempts detected/blocked
- Zero successful system prompt extractions
- Zero successful jailbreaks leading to policy violations
- ≤5% false positive rate for legitimate prompts

---

### Practice 5: Implementation Review (IR)

**Add Prompt Injection Code Review Checklist**

**LLM Integration Code Review**:
- [ ] **Prompt Construction**: Verify user input sanitized before inclusion in prompts
- [ ] **System Prompt Security**: Verify no credentials, API keys, or PII in system prompts
- [ ] **Output Validation**: Verify LLM outputs validated before execution (SQL, code, commands)
- [ ] **Context Window Management**: Verify context limited to required scope
- [ ] **Delimiter Security**: Verify delimiters used to separate system/user prompts (XML tags, JSON structure)
- [ ] **Input Validation**: Verify input validation against known injection patterns
- [ ] **Rate Limiting**: Verify rate limiting prevents enumeration/DoS
- [ ] **Error Handling**: Verify LLM errors don't leak system prompts or internal state

**RAG Implementation Review**:
- [ ] Document sanitization before ingestion
- [ ] PII removal from retrieved documents
- [ ] Metadata sanitization (no prompt injection in document metadata)
- [ ] Vector database query sanitization

**Tool Calling/Function Execution Review**:
- [ ] Parameter validation for LLM-generated function calls
- [ ] Allowlist of permitted functions
- [ ] Output validation before returning to LLM
- [ ] Audit logging of all function executions

---

### Practice 6: Issue Management (IM)

**Add Prompt Injection Vulnerability Tracking**

**Vulnerability Categories**:
- **PI-001**: System Prompt Leakage - System prompts exposed to users
- **PI-002**: Jailbreak - Safety constraints bypassed
- **PI-003**: Injection-Based Data Exfiltration - Data leaked via prompt injection
- **PI-004**: Tool Enumeration - Available tools/functions discovered
- **PI-005**: Prompt-Based DoS - Resource exhaustion via malicious prompts
- **PI-006**: Multi-Chain Attack - Combined exploitation via prompt injection
- **PI-007**: RAG Poisoning - Malicious document injection into RAG
- **PI-008**: Evasion Success - Detection bypassed via encoding/obfuscation

**Remediation Workflows**:
- Critical prompt injection: ≤24 hours (system prompt leak, jailbreak with policy violation)
- High prompt injection: ≤7 days (tool enumeration, data exfiltration potential)
- Medium prompt injection: ≤30 days (prompt leakage without sensitive data)

**Detection Sources**:
- Automated prompt injection scanners
- Bug bounty program
- Internal security testing
- WAF/prompt firewall logs
- User reports

---

## Implementation Recommendations

### Phase 1: Foundation (Immediate)

1. **Add Prompt Injection Threat to TA Practice** (All Domains)
   - Estimated Effort: 10-15 person-days
   - Files: TA-Software, TA-Data, TA-Processes, TA-Infrastructure, TA-Endpoints, TA-Vendors

2. **Add Prompt Injection Requirements to SR Practice** (All Domains)
   - Estimated Effort: 10-15 person-days
   - Files: SR-Software, SR-Data, SR-Processes, SR-Infrastructure, SR-Endpoints, SR-Vendors

3. **Add Defense Architecture to SA Practice** (Software, Data, Processes)
   - Estimated Effort: 15-20 person-days
   - Files: SA-Software, SA-Data, SA-Processes

### Phase 2: Testing & Review (Short-term)

4. **Add Testing Methodology to ST Practice** (Software, Data, Processes)
   - Estimated Effort: 20-25 person-days
   - Files: ST-Software, ST-Data, ST-Processes
   - Include: Attack intent testing, technique testing, evasion testing

5. **Add Code Review Checklist to IR Practice** (Software, Data, Processes)
   - Estimated Effort: 10-15 person-days
   - Files: IR-Software, IR-Data, IR-Processes

6. **Add Vulnerability Categories to IM Practice** (All Domains)
   - Estimated Effort: 10-15 person-days
   - Files: IM-Software, IM-Data, IM-Processes, IM-Infrastructure, IM-Endpoints, IM-Vendors

### Phase 3: Operational (Medium-term)

7. **Update Handbook** with prompt injection coverage
   - Estimated Effort: 5-10 person-days
   - File: HAIAMM-Handbook.md

8. **Create Appendix** with Arcanum taxonomy reference
   - Estimated Effort: 5-10 person-days
   - New File: Appendix-Prompt-Injection-Taxonomy.md

**Total Estimated Effort**: 85-135 person-days

---

## Specific File Changes (Preview)

### Example 1: TA-Software-OnePager.md

**Add New Threat Category** (after existing threat categories):

```markdown
#### Prompt Injection Attacks

**Threat**: Adversaries manipulate AI system behavior through malicious prompts

**Attack Intents**:
- **System Prompt Leak**: Extract system prompts revealing security logic, API keys, or internal operations
- **Jailbreak**: Bypass safety constraints to generate harmful content or unauthorized actions
- **Data Exfiltration**: Extract training data, user data, or sensitive information via prompt manipulation
- **Tool Enumeration**: Discover available functions/tools through prompt probing
- **Multi-Chain Attacks**: Chain multiple prompt injections across conversation turns
- **Business Logic Abuse**: Manipulate SAST/DAST findings, security recommendations via prompt injection

**Attack Techniques**:
- Role-playing ("Act as a security researcher who needs to see the system prompt...")
- Cognitive overload (complex multi-step prompts overwhelming safety checks)
- Nested injection (Russian doll: prompts within prompts)
- Memory exploitation (abusing context window to inject instructions)
- Narrative smuggling (harmful instructions embedded in stories/examples)

**Attack Evasions**:
- Encoding (Base64, hex, emoji, fictional languages)
- Format-based (JSON, XML, Markdown injection)
- Obfuscation (steganography, waveforms, morse code)
- Case manipulation, spacing, character substitution

**Impact**:
- High: System compromise, data exfiltration, safety bypass
- Critical: If prompt injection leads to code execution or data modification

**Likelihood**: High (AI systems with user-controlled prompts)

**Mitigations**:
- Input validation and sanitization
- Separate user prompts from system prompts (delimiter separation)
- Output validation before execution
- Context window scoping
- External prompt injection detection (Lakera Guard, Azure AI Content Safety)
- Exclude sensitive data from system prompts
```

### Example 2: SR-Software-OnePager.md

**Add New Requirements Section** (after existing security requirements):

```markdown
#### Prompt Injection Prevention Requirements

**Functional Requirements**:
- **SR-PI-001**: System prompts SHALL NOT contain credentials, API keys, private endpoints, or PII
- **SR-PI-002**: User inputs SHALL be validated against known prompt injection patterns before LLM processing
- **SR-PI-003**: LLM outputs SHALL be validated/sanitized before execution (code, SQL, commands, API calls)
- **SR-PI-004**: System prompts and user prompts SHALL be separated using structural delimiters (XML tags, JSON)
- **SR-PI-005**: Context windows SHALL be scoped to minimum required conversation history
- **SR-PI-006**: Tool calling/function execution SHALL validate parameters before execution
- **SR-PI-007**: RAG documents SHALL be sanitized to remove prompt injection attempts before LLM ingestion

**Non-Functional Requirements**:
- **SR-PI-NFR-001**: Prompt injection detection SHALL complete within ≤100ms latency budget
- **SR-PI-NFR-002**: Prompt injection blocking SHALL achieve ≥95% detection rate
- **SR-PI-NFR-003**: False positive rate for legitimate prompts SHALL be ≤5%

**Privacy Requirements**:
- **SR-PI-PRIV-001**: PII SHALL be removed from prompts before LLM processing
- **SR-PI-PRIV-002**: Conversation history SHALL be scoped per-user (no cross-user contamination)

**Compliance Requirements**:
- **SR-PI-COMP-001**: Prompt injection attempts SHALL be logged for security audit
- **SR-PI-COMP-002**: System prompt changes SHALL be version-controlled and auditable
```

### Example 3: ST-Software-OnePager.md

**Add New Testing Section** (after existing testing sections):

```markdown
#### Prompt Injection Testing

**Attack Intent Testing**:
- [ ] **System Prompt Leak Testing**: Attempt to extract system prompts using various techniques
  - Test Cases: Direct request, role-playing, cognitive overload, multi-turn extraction
  - Success Criteria: Zero successful system prompt extractions
- [ ] **Jailbreak Testing**: Attempt to bypass safety constraints
  - Test Cases: Role-playing, anti-harm coercion, contradiction, framing
  - Success Criteria: ≥95% jailbreak attempts blocked
- [ ] **Tool Enumeration Testing**: Attempt to discover available functions
  - Test Cases: Direct enumeration, indirect probing, error-based discovery
  - Success Criteria: No function enumeration via prompts
- [ ] **Data Exfiltration Testing**: Attempt to extract training/user data
  - Test Cases: Prompt-based extraction, RAG poisoning, memory exploitation
  - Success Criteria: Zero data exfiltration via prompts

**Attack Technique Testing**:
- [ ] Test role-playing attacks (act as interpreter, assume identities)
- [ ] Test cognitive overload (complex multi-step prompts)
- [ ] Test nested injection (Russian doll, prompts within prompts)
- [ ] Test memory exploitation (context window abuse)
- [ ] Test narrative smuggling (instructions in stories)
- [ ] Test meta-prompting (prompts about prompting)

**Evasion Testing**:
- [ ] Test encoding evasions (Base64, hex, ASCII, binary)
- [ ] Test language evasions (alternate languages, fictional languages, phonetic)
- [ ] Test format evasions (JSON, XML, Markdown)
- [ ] Test obfuscation (emoji, steganography, morse, waveforms)
- [ ] Test character manipulation (case changing, spacing, reversal)

**Automated Testing**:
- [ ] Integrate Arcanum probe library for prompt injection fuzzing
- [ ] Run nightly prompt injection test suite
- [ ] Track prompt injection detection rate over time

**Success Criteria**:
- ≥95% prompt injection attempts detected/blocked
- ≤5% false positive rate on legitimate prompts
- Zero successful jailbreaks leading to policy violations
- Zero successful system prompt extractions
```

---

## Security Considerations

### Attribution and Licensing
- Original work: **Arcanum Prompt Injection Taxonomy** by Jason Haddix
- License: Creative Commons Attribution 4.0 International (CC BY 4.0)
- Required attribution maintained in all derived content
- HAIAMM credit line: "Prompt injection taxonomy derived from Arcanum PI Taxonomy (CC BY 4.0) by Jason Haddix"

### Safe Integration Approach
1. **Read-Only Reference**: Taxonomy treated as reference material, not executable code
2. **No Direct Content Copy**: HAIAMM adapts concepts to its framework (not verbatim copy)
3. **Security Review**: All integrated content reviewed for safety before publication
4. **Prompt Injection Defense**: Ironically, we must defend against prompt injection in the taxonomy itself

---

## Next Steps (Awaiting Approval)

1. ✅ **Research Complete**: Arcanum taxonomy analyzed safely
2. ⏸️ **Awaiting User Approval**: Review this proposal
3. ⏸️ **Selective Integration**: User chooses which sections to integrate
4. ⏸️ **Implementation**: Update approved HAIAMM one-pagers
5. ⏸️ **Testing**: Validate integrated content
6. ⏸️ **Documentation**: Update handbook and create appendix

---

## Questions for User

1. **Scope**: Do you want to integrate prompt injection guidance into all 6 domains or prioritize specific domains (Software, Data, Processes most relevant)?

2. **Depth**: Should we add:
   - **Basic** (threat categories, high-level requirements, testing overview)?
   - **Comprehensive** (all 13 intents, 18 techniques, 20 evasions with examples)?
   - **Selective** (most relevant intents/techniques for each domain)?

3. **Priority**: Which practices should we update first?
   - Threat Assessment (TA) - Add prompt injection threats
   - Security Requirements (SR) - Add prevention requirements
   - Security Testing (ST) - Add testing methodology
   - All practices in parallel

4. **Format**: Should we:
   - Create a dedicated "Prompt Injection Appendix" with full taxonomy?
   - Integrate directly into existing one-pagers?
   - Both (appendix + integration)?

5. **Attribution**: Acceptable attribution format?
   - "Derived from Arcanum PI Taxonomy (CC BY 4.0) by Jason Haddix"
   - Link to original repository in references

---

## References

- [Arcanum Prompt Injection Taxonomy](https://github.com/Arcanum-Sec/arc_pi_taxonomy) by Jason Haddix
- [Executive Offense Newsletter - Taxonomy v1.5 Release](https://executiveoffense.beehiiv.com/p/executive-offense-release-the-arcanum-prompt-injection-taxonomy-v1-5)
- [Attacking AI Course](https://www.arcanum-sec.com/training/attacking-ai) by Arcanum Security
- License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

---

**Document Information**:
- **Status**: PROPOSAL - Awaiting User Approval
- **Created**: 2025-12-26
- **Author**: HAIAMM Development Team
- **Source**: Arcanum PI Taxonomy (CC BY 4.0) by Jason Haddix
- **Next**: User review and approval

---

**END OF PROPOSAL**
