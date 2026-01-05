# HAIAMM Maturity Roadmap

**Level 1 → 2 → 3 progression guide**

[Back to Index](00-INDEX.md) | [Assessment Checklist](07-ASSESSMENT-CHECKLIST.md) | [First 30 Days](02-FIRST-30-DAYS.md)

---

## Overview

This roadmap provides guidance for progressing through HAIAMM maturity levels. Each level builds on the previous, creating a sustainable security improvement path.

---

## Maturity Level Characteristics

### Level 1: Foundation

**Characteristics:**
- Basic awareness of AI security issues
- Ad-hoc security activities
- Individual efforts, not organizational
- Reactive security posture

**Typical State:**
- AI systems exist but security is inconsistent
- Some controls implemented, mostly basic
- Limited visibility into AI security posture
- No formal metrics or tracking

**Effort to Achieve:** 1-3 months
**Typical Investment:** 40-80 hours per practice

---

### Level 2: Structured

**Characteristics:**
- Documented security requirements
- Consistent processes across projects
- Defined roles and responsibilities
- Proactive security activities

**Typical State:**
- Security requirements defined and tracked
- Processes documented and followed
- Regular testing and monitoring
- Metrics collected (but may not drive decisions)

**Effort to Achieve:** 3-6 months (from Level 1)
**Typical Investment:** 80-160 hours per practice

---

### Level 3: Optimized

**Characteristics:**
- Quantitative management
- Continuous improvement
- Automated controls where possible
- Industry leadership

**Typical State:**
- Metrics drive security decisions
- Automation reduces manual effort
- Benchmarked against industry
- Proactive threat anticipation

**Effort to Achieve:** 6-12 months (from Level 2)
**Typical Investment:** 160-240 hours per practice

---

## Level 1 → Level 2 Transition

### Transition Criteria

You're ready for Level 2 when:
- [ ] All AI systems inventoried and documented
- [ ] Basic security controls in place (validation, logging)
- [ ] Ownership assigned for all AI systems
- [ ] At least one security test completed per system
- [ ] Incident response procedure exists

### Key Activities by Practice

| Practice | Level 1 State | Level 2 Target | Key Activities |
|----------|---------------|----------------|----------------|
| **SM** | Ad-hoc strategy | Documented strategy with KPIs | Define metrics, create dashboard |
| **PC** | Basic policies | Enforced policies | Implement technical enforcement |
| **EG** | Informal training | Structured program | Create role-based training |
| **TA** | Basic threat awareness | Formal threat models | Adopt structured methodology |
| **SR** | Informal requirements | Documented, testable | Create requirements spec |
| **SA** | Basic architecture | Security patterns | Document and review architecture |
| **DR** | Ad-hoc reviews | Checklist-based | Create review process |
| **IR** | Basic implementation review | Security-focused | Add security linting |
| **ST** | Manual testing | Test suite (50+ cases) | Build automated tests |
| **IM** | Reactive response | SLA-tracked | Implement ticketing, SLAs |
| **EH** | Basic hardening | Standards-based | Document hardening standards |
| **ML** | Basic logging | Alerting & correlation | Deploy SIEM integration |

### Recommended Transition Order

**Phase 1: Visibility (Month 1-2)**
1. SM - Establish metrics framework
2. ML - Implement comprehensive logging
3. IM - Set up issue tracking

**Phase 2: Controls (Month 2-4)**
4. ST - Build security test suite
5. EH - Document and apply hardening
6. SR - Formalize security requirements

**Phase 3: Process (Month 4-6)**
7. TA - Adopt threat modeling methodology
8. DR - Implement design review process
9. SA - Document architecture patterns

**Phase 4: Culture (Month 5-6)**
10. PC - Enforce policies technically
11. EG - Launch training program
12. IR - Add security-focused implementation review

### Level 1→2 Investment Estimate

| Category | Hours | Cost (Internal) | Cost (External) |
|----------|-------|-----------------|-----------------|
| Process Documentation | 80-120 | $16K-$24K | $30K-$50K |
| Technical Implementation | 120-200 | $24K-$40K | $50K-$80K |
| Training Development | 40-60 | $8K-$12K | $20K-$30K |
| Tool Deployment | 60-100 | $12K-$20K | $25K-$40K |
| **Total** | **300-480** | **$60K-$96K** | **$125K-$200K** |

*Based on $200/hr loaded internal cost, consultant rates vary*

---

## Level 2 → Level 3 Transition

### Transition Criteria

You're ready for Level 3 when:
- [ ] All Level 2 practices consistently executed
- [ ] Metrics collected for at least 6 months
- [ ] No critical vulnerabilities open >30 days
- [ ] Security testing automated in CI/CD
- [ ] Incident response tested via tabletop

### Key Activities by Practice

| Practice | Level 2 State | Level 3 Target | Key Activities |
|----------|---------------|----------------|----------------|
| **SM** | KPIs tracked | ROI demonstrated | Implement benchmarking |
| **PC** | Policies enforced | Automated compliance | Deploy continuous compliance |
| **EG** | Structured training | Champions program | Create career path |
| **TA** | Formal threat models | Threat intelligence | Integrate threat feeds |
| **SR** | Documented reqs | Auto-verified | CI/CD integration |
| **SA** | Patterns documented | Continuously validated | Architecture scanning |
| **DR** | Checklist reviews | Automated checks | Deploy design scanning |
| **IR** | Security linting | ML-based analysis | Advanced SAST |
| **ST** | Automated suite | Red team + ML testing | Continuous testing |
| **IM** | SLA-tracked | Root cause analysis | Trend analysis |
| **EH** | Standards-based | Drift detection | Auto-remediation |
| **ML** | Alerting active | ML anomaly detection | Predictive monitoring |

### Recommended Transition Order

**Phase 1: Automation (Month 1-3)**
1. ST - Implement continuous security testing
2. EH - Deploy drift detection and auto-remediation
3. SR - Integrate requirements verification in CI/CD

**Phase 2: Intelligence (Month 3-6)**
4. ML - Deploy ML-based anomaly detection
5. TA - Integrate threat intelligence feeds
6. IM - Implement trend analysis and prediction

**Phase 3: Optimization (Month 6-9)**
7. SM - Achieve ROI demonstration capability
8. PC - Deploy continuous compliance monitoring
9. SA - Implement architecture drift detection

**Phase 4: Leadership (Month 9-12)**
10. DR - Automate design security verification
11. IR - Deploy advanced static analysis
12. EG - Launch security champions program

### Level 2→3 Investment Estimate

| Category | Hours | Cost (Internal) | Cost (External) |
|----------|-------|-----------------|-----------------|
| Automation Development | 200-300 | $40K-$60K | $80K-$120K |
| ML/Analytics Setup | 100-150 | $20K-$30K | $50K-$75K |
| Tool Integration | 150-200 | $30K-$40K | $60K-$80K |
| Process Optimization | 80-120 | $16K-$24K | $30K-$50K |
| **Total** | **530-770** | **$106K-$154K** | **$220K-$325K** |

---

## Practice Dependencies

Some practices should be prioritized before others:

```
                    ┌─────────────────┐
                    │    SM (Strategy) │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
       ┌──────────┐   ┌──────────┐   ┌──────────┐
       │   TA     │   │   PC     │   │   EG     │
       │ (Threat) │   │ (Policy) │   │(Training)│
       └────┬─────┘   └────┬─────┘   └──────────┘
            │              │
            ▼              ▼
       ┌──────────┐   ┌──────────┐
       │   SR     │   │   SA     │
       │  (Reqs)  │   │ (Arch)   │
       └────┬─────┘   └────┬─────┘
            │              │
            └──────┬───────┘
                   ▼
            ┌──────────┐
            │   DR     │
            │ (Design) │
            └────┬─────┘
                 │
       ┌─────────┼─────────┐
       ▼         ▼         ▼
  ┌────────┐ ┌────────┐ ┌────────┐
  │   IR   │ │   ST   │ │   EH   │
  │(Impl)  │ │ (Test) │ │(Harden)│
  └────────┘ └────┬───┘ └────────┘
                  │
                  ▼
            ┌──────────┐
            │   IM     │
            │ (Issues) │
            └────┬─────┘
                 │
                 ▼
            ┌──────────┐
            │   ML     │
            │(Monitor) │
            └──────────┘
```

**Critical Path:** SM → TA → SR → DR → ST → IM → ML

---

## Sample 12-Month Roadmap

### Quarter 1: Establish Foundation (Level 1)

| Month | Focus | Practices | Deliverables |
|-------|-------|-----------|--------------|
| M1 | Discovery | SM, ML | AI inventory, basic logging |
| M2 | Assessment | TA, ST | Threat models, initial tests |
| M3 | Controls | SR, EH | Requirements, hardening |

### Quarter 2: Build Structure (Level 2 Start)

| Month | Focus | Practices | Deliverables |
|-------|-------|-----------|--------------|
| M4 | Process | DR, IR | Review processes |
| M5 | Policy | PC, EG | Policies, training |
| M6 | Architecture | SA, IM | Architecture review, issue tracking |

### Quarter 3: Mature (Level 2 Complete)

| Month | Focus | Practices | Deliverables |
|-------|-------|-----------|--------------|
| M7 | Automation | ST, EH | CI/CD testing, auto-hardening |
| M8 | Metrics | SM, ML | Dashboard, alerts |
| M9 | Validation | All | Level 2 assessment |

### Quarter 4: Optimize (Level 3 Start)

| Month | Focus | Practices | Deliverables |
|-------|-------|-----------|--------------|
| M10 | Intelligence | TA, ML | Threat intel, anomaly detection |
| M11 | Advanced | ST, IR | Red team, advanced analysis |
| M12 | Leadership | SM, EG | ROI, champions program |

---

## Common Roadblocks

### Roadblock 1: Lack of Executive Support
**Symptom:** Budget constraints, competing priorities
**Solution:** Start with [Risk Matrix](05-RISK-PRACTICE-MATRIX.md) to show risk coverage

### Roadblock 2: Skill Gaps
**Symptom:** Team lacks AI security expertise
**Solution:** Focus on EG practice, leverage [Tools](08-TOOLS-RESOURCES.md)

### Roadblock 3: Technical Debt
**Symptom:** Legacy systems resist security controls
**Solution:** Prioritize ML (monitoring) to create visibility

### Roadblock 4: Scope Creep
**Symptom:** Trying to do too much at once
**Solution:** Follow phased roadmap, complete one level before advancing

### Roadblock 5: Measurement Paralysis
**Symptom:** Can't prove progress
**Solution:** Establish basic SM metrics early, track consistently

---

## Maturity Assessment Schedule

| Maturity Level | Assessment Frequency | Duration |
|----------------|---------------------|----------|
| Level 0-1 | Quarterly | 2-4 hours |
| Level 2 | Semi-annually | 4-8 hours |
| Level 3 | Annually | 8-16 hours |

---

## Document Information

| Field | Value |
|-------|-------|
| Document | Maturity Roadmap |
| HAIAMM Version | 2.2 |
| Last Updated | January 2026 |

---

**Related Documents:**
- [Assessment Checklist](07-ASSESSMENT-CHECKLIST.md) - Assess current state
- [First 30 Days](02-FIRST-30-DAYS.md) - Start Level 1
- [Tools & Resources](08-TOOLS-RESOURCES.md) - Implementation support

[Back to Index](00-INDEX.md)
