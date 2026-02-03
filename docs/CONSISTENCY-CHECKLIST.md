# HAIAMM Documentation Consistency Checklist
## Reference Guide for Maintaining Canonical Structure

**Version:** 1.0
**Last Updated:** 2025-12-29
**Purpose:** Ensure all HAIAMM documentation aligns with the canonical structure defined in HAIAMM-Framework-Structure.md

---

## Quick Reference

**Canonical Source:** [`docs/HAIAMM-Framework-Structure.md`](HAIAMM-Framework-Structure.md)

**Before making ANY documentation changes, verify against this checklist.**

---

## 1. Terminology Checks

### ✅ Correct Terminology

| Term | Correct Usage | Common Error |
|------|---------------|--------------|
| Framework Name | "Human Assisted Intelligence" | ~~"Human-Assisted Intelligence"~~ (no hyphen) |
| Abbreviation | "HAI" or "HAIAMM" | ~~"HAI-AMM"~~ |
| Practice IR | "Implementation Review" | ~~"Code Review"~~ |
| Focus Areas | "trust, safety, and security" | ~~"security"~~ alone |

### ❌ Common Errors to Avoid

- [ ] Remove ALL hyphens from "Human Assisted Intelligence"
- [ ] Never use "HAI security programs"
- [ ] Never use "AI security agents" or "AI security tools"
- [ ] Avoid "Code Review" (correct term: "Implementation Review")

---

## 2. Domain Order (CRITICAL)

**Canonical Order:** Software, Data, Infrastructure, Vendors, Processes, Endpoints

### ✅ Correct Examples

```markdown
1. **Software** - HAI applications, models, code
2. **Data** - Training/operational data, privacy, quality
3. **Infrastructure** - Cloud/on-premise platforms, deployment
4. **Vendors** - Third-party HAI services, supply chain
5. **Processes** - Business workflows, governance, compliance
6. **Processes** - User interfaces, APIs, integration points
```

### ❌ Common Errors

- [ ] ~~Software, Infrastructure, Endpoints, Data, Processes, Vendors~~ (WRONG ORDER)
- [ ] ~~Infrastructure before Data~~ (WRONG)
- [ ] ~~Endpoints before Vendors~~ (WRONG)

### Verification Steps

1. When listing domains, ALWAYS follow canonical order
2. Visual representations (charts, tables) must follow canonical order
3. Code examples referencing domains must use canonical order

---

## 3. Business Functions & Practices

### Business Functions Order

**Canonical:** Governance → Building → Verification → Operations

### 12 Security Practices (Canonical List)

| Code | Practice Name | Business Function |
|------|--------------|-------------------|
| **SM** | Strategy & Metrics | Governance |
| **PC** | Policy & Compliance | Governance |
| **EG** | Education & Guidance | Governance |
| **TA** | Threat Assessment | Building |
| **SR** | Security Requirements | Building |
| **SA** | Secure Architecture | Building |
| **DR** | Design Review | Verification |
| **IR** | Implementation Review | Verification |
| **ST** | Security Testing | Verification |
| **EH** | Environment Hardening | Operations |
| **IM** | Issue Management | Operations |
| **ML** | Monitoring & Logging | Operations |

### ✅ Verification Checklist

- [ ] Total practice count = 12 (not 13)
- [ ] IR = "Implementation Review" (never "Code Review" or "CR")
- [ ] All 3 Governance practices listed: SM, PC, EG
- [ ] All 3 Building practices listed: TA, SR, SA
- [ ] All 3 Verification practices listed: DR, IR, ST
- [ ] All 3 Operations practices listed: EH, IM, ML

---

## 4. Statistics & Numbers (v2.0)

### ✅ Correct v2.0 Statistics

| Metric | Correct Value | Common Error |
|--------|---------------|--------------|
| Domains | 6 | ✓ |
| Business Functions | 24 (4 per domain) | ✓ |
| **Security Practices** | **12 practices** | ~~13 practices~~ |
| **Practice Instances** | **72 (12 × 6 domains)** | ~~78~~ |
| **Maturity Levels** | **216 (72 × 3 levels)** | ~~234~~ |
| **Assessment Criteria** | **432 (v2.0)** | ~~702 (v1.0)~~ |

### Tiered Assessment (v2.0)

| Tier | Time | Questions | Domains |
|------|------|-----------|---------|
| **Tier 1 (Foundation)** | 20-30 min | 24 | Software, Data |
| **Tier 2 (Standard)** | 3-4 hours | 192 | +Infrastructure, Endpoints |
| **Tier 3 (Comprehensive)** | 12-16 hours | 432 | All 6 domains |

### ❌ Outdated v1.0 Statistics to Replace

- [ ] ~~78 security practices~~ → Use "72 practice instances"
- [ ] ~~234 maturity levels~~ → Use "216 maturity levels"
- [ ] ~~702 assessment criteria~~ → Use "432 assessment criteria (v2.0)"
- [ ] ~~13 practices~~ → Use "12 practices"

---

## 5. Core Messaging

### Framework Purpose

**Correct:**
> HAIAMM assesses the maturity of organizations designing and implementing Human Assisted Intelligence (HAI) solutions - providing foundational practices to ensure **trust, safety, and security**.

**Incorrect:**
> ~~HAIAMM is for HAI security programs~~ ❌
> ~~HAIAMM focuses only on security~~ ❌

### Use Cases (MUST Include)

✅ **Required use case mentions:**
- Automation workflows / business process automation
- Security testing & code analysis (SAST/DAST tools)
- Customer service chatbots with human escalation
- Decision support systems with human approval
- AI-assisted development (code generation, review)

### Core Principles

- [ ] ✅ Human oversight is REQUIRED (not optional)
- [ ] ✅ Focus on trust, safety, AND security (all three)
- [ ] ✅ HAI systems ASSIST humans (humans maintain authority)
- [ ] ✅ Progressive maturity (Level 0 → 3)
- [ ] ✅ Based on OpenSAMM v1.0 + Pravir Chandra's multi-domain concept

---

## 6. Foundation & Attribution

### ✅ Correct Attribution

```markdown
**Based on:** OWASP OpenSAMM v1.0 with extensions from Pravir Chandra's
"Future Directions" (3/27/2015)

**Key Innovations:**
1. Multi-Domain Architecture (6 domains)
2. HAI-Specific Practices (adapted for AI/ML systems)
3. Human oversight requirements integrated throughout
```

### Reference Format

```markdown
## References

- [OWASP SAMM Official Site](https://www.opensamm.org/)
- [OpenSAMM v1.0 Documentation](https://opensamm.org/downloads/SAMM-1.0.pdf)
- HAIAMM extends OpenSAMM v1.0 with multi-domain architecture for
  comprehensive assessment of Human Assisted Intelligence governance,
  building, verification, and operations with appropriate human oversight
```

---

## 7. File-Specific Checks

### README.md

- [ ] Title uses "Human Assisted Intelligence" (no hyphen)
- [ ] Domains listed in canonical order
- [ ] Statistics reflect v2.0 (72 instances, 432 questions)
- [ ] IR = Implementation Review (not Code Review)
- [ ] Emphasizes trust, safety, and security
- [ ] Includes HAI use cases (automation, chatbots, security testing)

### Quick Start Guide

- [ ] Domain order: Software, Data, Infrastructure, Vendors, Processes, Endpoints
- [ ] Practice names match canonical list
- [ ] Statistics are v2.0 compliant
- [ ] Assessment methodology included
- [ ] Plain English, accessible to practitioners

### Pitch Decks

- [ ] No hyphens in "Human Assisted Intelligence"
- [ ] Domain visualizations follow canonical order
- [ ] Statistics updated to v2.0
- [ ] Code examples reference 72 instances, 432 questions
- [ ] Performance benchmarks reference v2.0 numbers

### Handbook

- [ ] All 12 practices documented with correct names
- [ ] IR = Implementation Review throughout
- [ ] Domain order consistent
- [ ] Statistics match v2.0
- [ ] Emphasizes HAI governance, building, verification, operations

---

## 8. Before Publishing Checklist

### Pre-Publication Review

Run these checks before committing documentation changes:

**Automated Checks (grep/search):**
```bash
# Check for hyphens in "Human Assisted Intelligence"
grep -r "Human-Assisted Intelligence" docs/
# Should return NO results

# Check for outdated statistics
grep -r "78 practices\|702 questions\|234 maturity" docs/
# Should return NO results

# Check for "Code Review" instead of "Implementation Review"
grep -r "CR - Code Review\|Code Review (CR)" docs/
# Should return NO results
```

**Manual Checks:**
- [ ] All domain lists follow canonical order
- [ ] All practice lists include all 12 practices with correct codes
- [ ] Statistics match v2.0 (72, 216, 432)
- [ ] Use cases include automation, chatbots, security testing
- [ ] Framework described as for HAI governance/building/verification/operations
- [ ] Attribution to OpenSAMM v1.0 + Pravir Chandra included

---

## 9. Document Update Workflow

### When Updating ANY Documentation:

1. **Read** `docs/HAIAMM-Framework-Structure.md` (canonical source)
2. **Check** this consistency checklist
3. **Update** your document
4. **Verify** against checklist before committing
5. **Test** automated checks (grep commands above)
6. **Commit** with clear message describing alignment changes

### Propagation Priority

If canonical structure changes:

**Priority 1 (Update Immediately):**
- README.md
- HAIAMM-Framework-Structure.md
- HAIAMM-Quick-Start-Guide.md

**Priority 2 (Update Within 24h):**
- HAIAMM-Handbook.md
- Pitch decks (all 3)
- CONTRIBUTING.md

**Priority 3 (Update Within 1 week):**
- Individual practice one-pagers (72 files)
- Code examples and tutorials
- Video scripts

---

## 10. Common Mistakes & How to Fix

### Mistake 1: Wrong Domain Order

❌ **Wrong:**
```markdown
1. Software
2. Infrastructure  ← ERROR
3. Endpoints       ← ERROR
4. Data            ← ERROR
5. Processes
6. Vendors         ← ERROR
```

✅ **Correct:**
```markdown
1. Software
2. Data
3. Infrastructure
4. Vendors
5. Processes
6. Endpoints
```

### Mistake 2: Outdated Statistics

❌ **Wrong:**
```markdown
- 78 Security Practices
- 234 Maturity Levels
- 702 Assessment Criteria
```

✅ **Correct:**
```markdown
- 72 Security Practice Instances (12 practices × 6 domains)
- 216 Maturity Levels (3 per practice instance)
- 432 Assessment Criteria (v2.0)
```

### Mistake 3: Wrong Practice Names

❌ **Wrong:**
```markdown
**CR - Code Review**
```

✅ **Correct:**
```markdown
**IR - Implementation Review**
```

### Mistake 4: Incomplete Core Messaging

❌ **Wrong:**
```markdown
HAIAMM focuses on AI security.
```

✅ **Correct:**
```markdown
HAIAMM provides foundational practices to ensure trust, safety, and
security of Human Assisted Intelligence solutions across governance,
building, verification, and operations.
```

---

## 11. Quick Validation Script

### Bash Script for Automated Checks

```bash
#!/bin/bash
# validate-haiamm-docs.sh

echo "=== HAIAMM Documentation Consistency Check ==="

# Check 1: Hyphens in HAI
echo "Checking for hyphens in 'Human Assisted Intelligence'..."
if grep -r "Human-Assisted Intelligence" docs/ pitch-decks/ README.md 2>/dev/null; then
    echo "❌ FAIL: Found hyphens in 'Human Assisted Intelligence'"
else
    echo "✅ PASS: No hyphens found"
fi

# Check 2: Outdated statistics
echo "Checking for outdated v1.0 statistics..."
if grep -r "78 practices\|702 questions\|234 maturity" docs/ pitch-decks/ README.md 2>/dev/null; then
    echo "❌ FAIL: Found outdated v1.0 statistics"
else
    echo "✅ PASS: No outdated statistics found"
fi

# Check 3: Wrong practice names
echo "Checking for 'Code Review' instead of 'Implementation Review'..."
if grep -r "CR - Code Review\|Code Review (CR)" docs/ pitch-decks/ README.md 2>/dev/null; then
    echo "❌ FAIL: Found 'Code Review' instead of 'Implementation Review'"
else
    echo "✅ PASS: Correct practice names used"
fi

echo "=== Check Complete ==="
```

**Usage:**
```bash
chmod +x validate-haiamm-docs.sh
./validate-haiamm-docs.sh
```

---

## 12. Emergency Fix Guide

### If You Find Inconsistencies

**Step 1:** Identify scope
- Single file? Fix immediately
- Multiple files? Create todo list

**Step 2:** Reference canonical
- Open `docs/HAIAMM-Framework-Structure.md`
- Verify correct terminology/structure

**Step 3:** Fix systematically
- Use search/replace for terminology fixes
- Manually verify domain orders
- Check statistics against v2.0 table

**Step 4:** Validate
- Run automated checks
- Manual review against checklist
- Test if documentation code examples

**Step 5:** Commit with context
```bash
git add <files>
git commit -m "docs: align with canonical HAIAMM structure

- Remove hyphens from 'Human Assisted Intelligence'
- Update domain order to canonical sequence
- Fix statistics to v2.0 (72 instances, 432 questions)
- Change CR to IR (Implementation Review)

Ref: docs/HAIAMM-Framework-Structure.md"
```

---

## Summary: The Golden Rules

1. **Canonical Source:** `docs/HAIAMM-Framework-Structure.md` is THE authority
2. **No Hyphens:** "Human Assisted Intelligence" (never "Human-Assisted")
3. **Domain Order:** Software, Data, Infrastructure, Vendors, Processes, Endpoints
4. **12 Practices:** Including IR (Implementation Review), not CR
5. **v2.0 Stats:** 72 instances, 216 levels, 432 questions
6. **Core Focus:** Trust, safety, and security (all three)
7. **Use Cases:** Must include automation, chatbots, security testing
8. **Human Oversight:** Required, not optional - HAI assists humans

---

**This checklist is the second-most important document after HAIAMM-Framework-Structure.md**

**Last Updated:** 2025-12-29
**Maintainer:** Reference HAIAMM-Framework-Structure.md for any conflicts
