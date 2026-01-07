# HAIAMM Jira Templates Import Guide

This guide explains how to import HAIAMM templates into Jira for tracking AI security implementation.

## Template Overview

### Epics (4 templates)

| Epic | File | Practices |
|------|------|-----------|
| Governance Function | `epics/governance-epic.json` | SM, PC, EG |
| Building Function | `epics/building-epic.json` | TA, SR, SA |
| Verification Function | `epics/verification-epic.json` | DR, IR, ST |
| Operations Function | `epics/operations-epic.json` | IM, EH, ML |

### Stories (12 templates)

| Practice | File | Story Points |
|----------|------|--------------|
| SM - Strategy & Metrics | `stories/SM-strategy-metrics.json` | 8 |
| PC - Policy & Compliance | `stories/PC-policy-compliance.json` | 8 |
| EG - Education & Guidance | `stories/EG-education-guidance.json` | 5 |
| TA - Threat Assessment | `stories/TA-threat-assessment.json` | 8 |
| SR - Security Requirements | `stories/SR-security-requirements.json` | 8 |
| SA - Secure Architecture | `stories/SA-secure-architecture.json` | 13 |
| DR - Design Review | `stories/DR-design-review.json` | 5 |
| IR - Implementation Review | `stories/IR-implementation-review.json` | 8 |
| ST - Security Testing | `stories/ST-security-testing.json` | 13 |
| IM - Issue Management | `stories/IM-issue-management.json` | 5 |
| EH - Environment Hardening | `stories/EH-environment-hardening.json` | 13 |
| ML - Monitoring & Logging | `stories/ML-monitoring-logging.json` | 8 |

**Total Story Points:** 102 points for Level 1 implementation

---

## Import Methods

### Method 1: Manual Creation (Recommended for Small Teams)

1. **Create Project**
   - Create a Jira project for AI security (or use existing)
   - Add component: "AI Security"
   - Add labels: `haiamm`, `ai-security`

2. **Create Custom Fields** (optional but recommended)
   - HAIAMM Practice (dropdown)
   - HAIAMM Function (dropdown)
   - Target Maturity Level (dropdown)
   - OWASP Risks Addressed (text)

3. **Create Epics**
   - Copy summary and description from JSON files
   - Assign labels and components
   - Link to parent initiative if applicable

4. **Create Stories**
   - Copy acceptance criteria from JSON
   - Assign to epics
   - Create subtasks from JSON subtasks array
   - Set story points

---

### Method 2: CSV Import (Bulk Import)

Use the CSV file at `haiamm-jira-import.csv` for bulk import.

**Steps:**

1. Go to **Project Settings** → **External System Import** → **CSV**
2. Upload `haiamm-jira-import.csv`
3. Map fields:
   - `Summary` → Summary
   - `Description` → Description
   - `Issue Type` → Issue Type
   - `Priority` → Priority
   - `Labels` → Labels (comma-separated)
   - `Story Points` → Story Points
   - `Epic Link` → Epic Link

4. Run import
5. Verify and adjust as needed

---

### Method 3: Jira REST API (Automation)

For automated import, use the Jira REST API:

```python
import json
import requests
from pathlib import Path

JIRA_URL = "https://your-domain.atlassian.net"
JIRA_EMAIL = "your-email@example.com"
JIRA_API_TOKEN = "your-api-token"
PROJECT_KEY = "HAIAMM"

def create_issue(issue_data):
    url = f"{JIRA_URL}/rest/api/3/issue"
    auth = (JIRA_EMAIL, JIRA_API_TOKEN)
    headers = {"Content-Type": "application/json"}

    payload = {
        "fields": {
            "project": {"key": PROJECT_KEY},
            "summary": issue_data["summary"],
            "description": {
                "type": "doc",
                "version": 1,
                "content": [
                    {
                        "type": "paragraph",
                        "content": [
                            {"type": "text", "text": issue_data["description"]}
                        ]
                    }
                ]
            },
            "issuetype": {"name": issue_data["issueType"]},
            "priority": {"name": issue_data["priority"]},
            "labels": issue_data["labels"]
        }
    }

    response = requests.post(url, auth=auth, headers=headers, json=payload)
    return response.json()

# Load and create epics
for epic_file in Path("epics").glob("*.json"):
    with open(epic_file) as f:
        data = json.load(f)
        result = create_issue(data["epic"])
        print(f"Created: {result.get('key')}")
```

---

### Method 4: Jira Automation Rules

Create automation rules to generate issues from templates:

1. **Trigger:** Manual trigger or scheduled
2. **Action:** Create issue with template values
3. **Branch:** Create child issues (subtasks)

---

## Recommended Setup

### Project Configuration

```
Project: AI Security Implementation
Type: Scrum or Kanban
Components:
  - AI Security
  - Governance
  - Building
  - Verification
  - Operations

Labels:
  - haiamm
  - ai-security
  - level-1, level-2, level-3
  - governance, building, verification, operations
  - [practice codes]: sm, pc, eg, ta, sr, sa, dr, ir, st, im, eh, ml
```

### Board Setup

**Columns:**
1. Backlog
2. Ready for Work
3. In Progress
4. In Review
5. Done

**Swimlanes:** By Epic (function)

**Quick Filters:**
- Level 1 items
- By function (Governance, Building, etc.)
- By practice

---

## Implementation Roadmap

### Phase 1: Foundation (Weeks 1-4)
Create and prioritize:
- [ ] All 4 Epic issues
- [ ] High-priority Level 1 stories (EH, ST, SR, TA)

### Phase 2: Core Implementation (Weeks 5-12)
- [ ] Complete remaining Level 1 stories
- [ ] Begin Level 2 planning for critical practices

### Phase 3: Maturity (Ongoing)
- [ ] Level 2 stories (duplicate templates, update for Level 2)
- [ ] Level 3 stories (advanced optimization)

---

## Story Point Reference

| Points | Effort | Example |
|--------|--------|---------|
| 3 | 1-2 days | Single document, simple config |
| 5 | 3-5 days | Process definition, basic tooling |
| 8 | 1-2 weeks | Multi-step implementation |
| 13 | 2-3 weeks | Complex implementation, integration |
| 21 | 3-4 weeks | Major initiative, multiple teams |

---

## Customization

### Adding Level 2/3 Stories

1. Duplicate Level 1 story JSON
2. Update summary: `[XX] Practice Name - Level 2 Implementation`
3. Update acceptance criteria from Level 2/3 checklist
4. Increase story points (typically +50-100% per level)
5. Update labels to include `level-2` or `level-3`

### Adding Custom Practices

1. Create new story JSON following template structure
2. Include:
   - Summary with practice code
   - Description with overview
   - Acceptance criteria
   - Definition of done
   - OWASP risks addressed
   - Subtasks
3. Add to appropriate epic

---

## Integration with Verifhai

When using Verifhai skills, reference Jira issues:

```
After completing /verifhai-practice SR, create:
- Jira Story: [SR] Security Requirements - Level 1
- Link findings to issue comments
- Track progress via subtasks
```

Verifhai can suggest issues to create based on assessment findings.

---

## Support

- [HAIAMM Handbook](../handbook/00-INDEX.md)
- [GitHub Issue Templates](../../.github/ISSUE_TEMPLATE/)
- [Checklists](../checklists/)

---

## Document Information

| Field | Value |
|-------|-------|
| Version | 1.0 |
| Last Updated | January 2026 |
