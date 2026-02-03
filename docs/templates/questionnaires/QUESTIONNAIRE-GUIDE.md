# HAIAMM Questionnaires Guide

This guide explains how to use HAIAMM assessment questionnaires for evaluating AI security maturity, vendors, deployments, and incidents.

## Questionnaire Overview

| Questionnaire | Purpose | Time | When to Use |
|--------------|---------|------|-------------|
| [Full Maturity Assessment](full-maturity-assessment.md) | Complete HAIAMM evaluation | 2-4 hours | Annual assessment, major initiatives |
| [Vendor AI Assessment](vendor-ai-assessment.md) | Third-party AI evaluation | 1-2 hours | New vendors, renewals, integrations |
| [Pre-Deployment Review](pre-deployment-review.md) | Production readiness | 30-60 min | Before go-live, major updates |
| [Incident Post-Mortem](incident-post-mortem.md) | Incident analysis | 1-2 hours | After security incidents |

---

## Quick Selection Guide

```
What do you need to assess?
│
├─► Organization's HAI security program
│   └─► Full Maturity Assessment
│
├─► Third-party AI service or vendor
│   └─► Vendor AI Assessment
│
├─► AI system before deployment
│   └─► Pre-Deployment Review
│
└─► Security incident that occurred
    └─► Incident Post-Mortem
```

---

## Questionnaire Details

### 1. Full Maturity Assessment

**File:** `full-maturity-assessment.md`

**Scope:** 180 questions covering all 12 HAIAMM practices across 3 maturity levels

**Structure:**
- 4 Functions × 3 Practices each = 12 practice sections
- Each practice: 15 questions (5 per maturity level)
- Scoring: Yes (2), Partial (1), No (0), N/A (skip)

**When to Use:**
- Annual security program assessment
- Starting a new AI security initiative
- Measuring progress over time
- Reporting to leadership/board

**Scoring:**

| Level | Questions | Max Score |
|-------|-----------|-----------|
| Level 1 (Foundation) | 60 | 120 |
| Level 2 (Structured) | 60 | 120 |
| Level 3 (Optimized) | 60 | 120 |
| **Total** | **180** | **360** |

**Maturity Calculation:**
- Level 1 achieved: ≥80% of Level 1 questions = Yes/Partial
- Level 2 achieved: Level 1 complete + ≥80% of Level 2 = Yes/Partial
- Level 3 achieved: Levels 1-2 complete + ≥80% of Level 3 = Yes/Partial

---

### 2. Vendor AI Assessment

**File:** `vendor-ai-assessment.md`

**Scope:** 7 sections evaluating third-party AI security

**Sections:**
1. Company & Compliance (16 points)
2. Data Handling (16 points)
3. Model Security (16 points)
4. API & Integration (22 points)
5. Operational Security (18 points)
6. Agent & Tool Security (16 points, if applicable)
7. Contractual & Legal (16 points)

**When to Use:**
- Evaluating new AI vendors/services
- Annual vendor security review
- Before integrating third-party AI/ML models
- Assessing AI API providers

**Risk Rating:**

| Score Range | Risk Level | Recommendation |
|-------------|------------|----------------|
| 90-100% | Low | Approve with standard monitoring |
| 70-89% | Medium | Approve with additional controls |
| 50-69% | High | Approve with risk acceptance only |
| <50% | Critical | Do not approve without remediation |

---

### 3. Pre-Deployment Review

**File:** `pre-deployment-review.md`

**Scope:** 9 sections for production security readiness

**Sections:**
1. Design & Architecture (14 points)
2. Input Security (16 points)
3. Output Security (16 points)
4. Authentication & Authorization (14 points)
5. Data Protection (14 points)
6. Agent/Tool Security (16 points, if applicable)
7. Monitoring & Logging (14 points)
8. Testing & Validation (16 points)
9. Operational Readiness (14 points)

**When to Use:**
- Before first production deployment
- Major version updates
- Significant architecture changes
- New integrations or data sources

**Pass Criteria:**
- Each section must score ≥70%
- No critical findings unresolved
- All "must have" items complete

---

### 4. Incident Post-Mortem

**File:** `incident-post-mortem.md`

**Scope:** 10 sections for AI security incident analysis

**Sections:**
1. Incident Summary
2. Timeline & Detection
3. AI-Specific Analysis (prompt injection, data, agents, model)
4. Root Cause Analysis (Five Whys)
5. Response Evaluation
6. Impact Assessment
7. Remediation Actions
8. Prevention Measures
9. Lessons Learned
10. Follow-Up

**When to Use:**
- After any AI security incident
- Security near-misses
- Discovered vulnerabilities
- Failed attacks that revealed weaknesses

**AI-Specific Sections:**
- Prompt injection analysis (direct/indirect, encoding, multi-turn)
- Data security (training data, PII, RAG, conversation history)
- Agent/tool security (goal hijack, privilege abuse, cascading failures)
- Model integrity (poisoning, extraction, supply chain)

---

## Scoring Methodology

### Standard Scoring (Most Questionnaires)

| Response | Points | Criteria |
|----------|--------|----------|
| Yes | 2 | Fully implemented and documented |
| Partial | 1 | Partially implemented or undocumented |
| No | 0 | Not implemented |
| N/A | Skip | Not applicable to this system |

### Calculating Percentages

```
Score % = (Points Earned / Max Possible Points) × 100

Example:
- Questions answered: 50
- N/A responses: 5 (excluded)
- Applicable questions: 45
- Max points: 45 × 2 = 90
- Points earned: 72
- Score: 72/90 = 80%
```

---

## Integration with Verifhai

Verifhai skills can suggest and guide questionnaire completion:

| Verifhai Skill | Questionnaire Integration |
|----------------|---------------------------|
| `/verifhai-assess` | Recommends Full Maturity Assessment |
| `/verifhai-measure` | Uses Full Maturity Assessment methodology |
| `/verifhai-practice` | References relevant questionnaire sections |
| `/verifhai-review` | Suggests Pre-Deployment Review |
| `/verifhai-start` | Guides questionnaire selection |

### Workflow Example

```
1. User runs /verifhai-assess
2. Verifhai identifies gaps
3. Recommends specific questionnaire
4. Guides through relevant sections
5. Tracks findings in GitHub issues
```

---

## Best Practices

### Before Starting

1. **Gather documentation** - Architecture diagrams, policies, configs
2. **Identify stakeholders** - Who needs to answer which sections
3. **Schedule time** - Block uninterrupted time for assessment
4. **Prepare evidence** - Screenshots, logs, configs as proof

### During Assessment

1. **Be honest** - Aspirational answers help no one
2. **Document gaps** - Notes are as valuable as scores
3. **Capture evidence** - Link to supporting documentation
4. **Mark unknowns** - Flag questions needing follow-up

### After Assessment

1. **Calculate scores** - Use formulas provided
2. **Prioritize findings** - Critical → High → Medium → Low
3. **Create action items** - Use GitHub issue templates
4. **Schedule follow-up** - Reassess in 30/60/90 days

---

## Customization

### Adding Organization-Specific Questions

1. Copy the questionnaire to your organization's docs
2. Add questions to relevant sections
3. Update max score calculations
4. Maintain HAIAMM practice mapping

### Creating Abbreviated Versions

For quick checks, create abbreviated versions:
- Select 3-5 critical questions per section
- Focus on Level 1 requirements
- Use for regular spot-checks between full assessments

### Automating Scoring

```python
# Example scoring calculator
def calculate_score(responses):
    points = {"yes": 2, "partial": 1, "no": 0}
    total = sum(points.get(r, 0) for r in responses if r != "na")
    max_possible = len([r for r in responses if r != "na"]) * 2
    return (total / max_possible * 100) if max_possible > 0 else 0
```

---

## Related Resources

### Templates
- [GitHub Issue Templates](../../.github/ISSUE_TEMPLATE/) - Track findings
- [Jira Templates](../jira/) - Enterprise tracking
- [Checklists](../checklists/) - Quick implementation checks

### Handbook
- [Assessment Checklist](../../handbook/07-ASSESSMENT-CHECKLIST.md) - Quick 30-min assessment
- [OWASP Risk Mappings](../../handbook/03-TOP10-LLM-RISKS.md) - Risk context
- [First 30 Days](../../handbook/02-FIRST-30-DAYS.md) - Implementation roadmap

### HAIAMM Framework
- [Practice One-Pagers](../../practices/) - Detailed practice guidance
- [Maturity Roadmap](../../handbook/06-MATURITY-ROADMAP.md) - Level progression

---

## Questionnaire Lifecycle

```
┌─────────────────────────────────────────────────────────────┐
│                    Assessment Cycle                          │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐              │
│  │  Annual  │───►│ Vendor   │───►│ Deploy   │              │
│  │  Maturity│    │ Review   │    │ Review   │              │
│  └──────────┘    └──────────┘    └──────────┘              │
│       │                               │                      │
│       │         ┌──────────┐          │                      │
│       └────────►│ Incident │◄─────────┘                      │
│                 │Post-Mortem│                                │
│                 └──────────┘                                 │
│                      │                                       │
│                      ▼                                       │
│              ┌──────────────┐                                │
│              │ Update       │                                │
│              │ Controls     │                                │
│              └──────────────┘                                │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## Document Information

| Field | Value |
|-------|-------|
| HAIAMM Version | 2.0 |
| Guide Version | 1.0 |
| Last Updated | January 2026 |
