# Verifhai GitHub Issue Template Guide

This guide explains how Verifhai Claude skills should suggest and help create GitHub issues using the HAIAMM issue templates.

## Template Overview

| Template | Purpose | Verifhai Skills |
|----------|---------|-----------------|
| `verifhai-recommendation.yml` | AI-generated security recommendations | All skills |
| `practice-implementation.yml` | Track HAIAMM practice implementation | `/verifhai-practice`, `/verifhai-start` |
| `security-control.yml` | Track individual security controls | `/verifhai-practice`, `/verifhai-review` |
| `risk-finding.yml` | Document identified risks | `/verifhai-assess`, `/verifhai-review` |
| `maturity-assessment.yml` | Track assessment results | `/verifhai-assess`, `/verifhai-measure` |

---

## Skill-to-Template Mapping

### `/verifhai-start` - Initial HAI Security Journey

**Suggested templates after session:**
1. `maturity-assessment.yml` - Capture baseline assessment
2. `practice-implementation.yml` - First practice to implement

**Example suggestion:**
```
Based on your initial assessment, I recommend creating these GitHub issues:

1. **[ASSESSMENT] Baseline HAIAMM Assessment Q1 2026**
   - Document your current maturity scores
   - Template: maturity-assessment

2. **[PRACTICE] TA - Threat Assessment Level 1**
   - Start with foundational threat assessment
   - Template: practice-implementation
```

---

### `/verifhai-assess` - Quick Maturity Assessment

**Suggested templates after session:**
1. `maturity-assessment.yml` - Record assessment results
2. `verifhai-recommendation.yml` - Quick wins identified
3. `risk-finding.yml` - Any risks discovered

**Example suggestion:**
```
Assessment complete. Create these issues to track findings:

1. **[ASSESSMENT] Quick Assessment - January 2026**
   - Overall maturity: 1.2 (Foundation)
   - Critical gaps: TA (0), ST (1)

2. **[VERIFHAI] Implement basic threat modeling**
   - Quick win: Use STRIDE for AI threat assessment
   - Effort: S (1-4 hours)

3. **[RISK] No input validation on chatbot endpoint**
   - Risk: LLM01 - Prompt Injection
   - Priority: High
```

---

### `/verifhai-practice` - Practice Building Session

**Suggested templates after session:**
1. `practice-implementation.yml` - Track the practice being built
2. `security-control.yml` - Individual controls to implement
3. `verifhai-recommendation.yml` - Specific action items

**Example CAN/CANNOT/MUST to Issue mapping:**

```
## Practice: SR - Security Requirements (Level 1)

Based on our session, create these issues:

### CAN (Capabilities to Build)
**[PRACTICE] SR - Security Requirements Level 1**
- Objective: Establish security requirements for AI systems
- Activities from CAN list

### CANNOT (Gaps to Address)
**[CONTROL] Input validation for LLM endpoints**
- Addresses: Cannot currently validate prompts
- Risk: LLM01 - Prompt Injection

### MUST (Critical Requirements)
**[VERIFHAI] Define security requirements template**
- Priority: Critical
- Must complete before any new AI deployment
```

---

### `/verifhai-measure` - Full HAIAMM Measurement

**Suggested templates after session:**
1. `maturity-assessment.yml` - Comprehensive assessment record
2. Multiple `practice-implementation.yml` - Roadmap items
3. Multiple `verifhai-recommendation.yml` - Prioritized actions

**Example output structure:**
```
## Full HAIAMM Measurement Complete

### Assessment Summary
Create: **[ASSESSMENT] Full HAIAMM Measurement - Q1 2026**
- Function scores: Governance (1.3), Building (0.7), Verification (1.0), Operations (1.7)
- Recommended focus: Building function

### Implementation Roadmap (6 issues)
1. [PRACTICE] TA - Threat Assessment → Level 1
2. [PRACTICE] SR - Security Requirements → Level 1
3. [PRACTICE] SA - Secure Architecture → Level 1
4. [PRACTICE] ST - Security Testing → Level 2
5. [PRACTICE] DR - Design Review → Level 1
6. [PRACTICE] IR - Implementation Review → Level 1

### Quick Wins (3 issues)
1. [VERIFHAI] Create AI system inventory
2. [VERIFHAI] Enable LLM interaction logging
3. [VERIFHAI] Document emergency shutdown procedure
```

---

### `/verifhai-review` - Security Code Review

**Suggested templates after session:**
1. `risk-finding.yml` - Vulnerabilities discovered
2. `security-control.yml` - Recommended controls
3. `verifhai-recommendation.yml` - Code-specific recommendations

**Example output:**
```
## Code Review Findings

### Risks Identified
1. **[RISK] Hardcoded API key in llm_client.py**
   - Risk: LLM02 - Sensitive Information Disclosure
   - Line: 47

2. **[RISK] No output sanitization in response handler**
   - Risk: LLM05 - Improper Output Handling
   - Line: 112-118

### Recommended Controls
1. **[CONTROL] Environment variable for API credentials**
2. **[CONTROL] Output validation middleware**

### Quick Fixes
1. **[VERIFHAI] Move API key to environment variable**
   - Effort: XS (<1 hour)
   - Priority: Critical
```

---

## Issue Creation Best Practices

### For Verifhai Skills

When suggesting issues, always include:

1. **Clear title with prefix**: `[PRACTICE]`, `[CONTROL]`, `[RISK]`, `[ASSESSMENT]`, or `[VERIFHAI]`
2. **Template reference**: Which template to use
3. **Pre-filled values**: Suggest values for key fields
4. **Verifhai session reference**: Date/ID for traceability
5. **Priority and effort**: Help users prioritize

### Example Verifhai Output Format

```markdown
## Recommended GitHub Issues

Based on this session, I recommend creating the following issues:

### Issue 1: [VERIFHAI] Implement prompt injection detection
**Template:** verifhai-recommendation
**Priority:** High
**Effort:** M (1-3 days)
**Practice:** EH - Environment Hardening
**Risks Addressed:** LLM01, ASI01

**Pre-filled values:**
- Source Skill: /verifhai-practice
- Recommendation Type: Control Implementation
- Maturity Impact: Level 1 - Foundation

**Acceptance Criteria:**
- [ ] Input validation on all LLM endpoints
- [ ] Known injection patterns blocked
- [ ] Logging enabled for blocked attempts

---

Would you like me to help you create these issues now?
```

---

## Verifhai Integration Fields

All templates include optional Verifhai integration fields:

| Field | Purpose |
|-------|---------|
| `verifhai_generated` / `verifhai_assisted` | Indicates AI involvement |
| `verifhai_session` | Session reference for traceability |
| `verifhai_recommendations` | Links to related issues (assessment template) |

### Why Track Verifhai-Generated Issues?

1. **Traceability**: Link recommendations back to assessment sessions
2. **Metrics**: Measure Verifhai effectiveness over time
3. **Audit**: Document AI-assisted security decisions
4. **Continuity**: Resume work across sessions

---

## Template Field Mapping

### From Verifhai Assessment to Templates

| Verifhai Output | Template Field |
|-----------------|----------------|
| Practice scores | `*_score` dropdowns in maturity-assessment |
| Identified gaps | `gaps` textarea in maturity-assessment |
| Risk findings | `risk_category`, `likelihood`, `impact` in risk-finding |
| CAN items | `activities` in practice-implementation |
| CANNOT items | `gaps` → create control issues |
| MUST items | `acceptance_criteria` in verifhai-recommendation |
| Quick wins | `recommendation_type: Quick Win` in verifhai-recommendation |

---

## Integration with Verifhai Skill Code

### Suggesting Templates Programmatically

When implementing Verifhai skills, use this pattern:

```markdown
## GitHub Issue Suggestions

After completing [skill action], Verifhai should output:

1. **Summary of findings**
2. **Recommended issues with:**
   - Template name
   - Pre-filled field values
   - Direct link to create issue (if repo known)

### Link Format
https://github.com/{owner}/{repo}/issues/new?template={template_name}.yml&title={encoded_title}&labels={labels}
```

### Example URL Generation

```
https://github.com/R3v3rzk1mur4/HAIAMM/issues/new?template=verifhai-recommendation.yml&title=[VERIFHAI]%20Implement%20input%20validation&labels=haiamm,verifhai,ai-recommended
```

---

## Next Steps

After creating issues from Verifhai recommendations:

1. **Run `/verifhai-status`** to update progress tracking
2. **Link related issues** using GitHub's linking syntax (#123)
3. **Update labels** as work progresses
4. **Close with reference** to Verifhai session when complete

---

## Document Information

| Field | Value |
|-------|-------|
| Version | 1.0 |
| Last Updated | January 2026 |
| Related Skills | /verifhai-* |
