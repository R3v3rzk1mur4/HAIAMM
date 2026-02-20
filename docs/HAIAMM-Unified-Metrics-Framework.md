# HAIAMM Unified Metrics Framework
## Security Architecture (SA) & Threat Assessment (TA) Practices

**Version:** 2.0  
**Last Updated:** 2026-02-11  
**Purpose:** Provide a unified, measurable framework for tracking security outcomes, process health, and business value across SA and TA practices for all 6 HAIAMM domains

---

## Table of Contents

1. [Metrics Taxonomy](#1-metrics-taxonomy)
2. [SA Practice Metrics Summary](#2-sa-practice-metrics-summary)
3. [TA Practice Metrics Summary](#3-ta-practice-metrics-summary)
4. [Measurement Methodology](#4-measurement-methodology)
5. [Maturity Scoring Integration](#5-maturity-scoring-integration)
6. [Dashboard Templates](#6-dashboard-templates)
7. [Metrics Lifecycle](#7-metrics-lifecycle)
8. [Appendix A: Data Source Catalog](#appendix-a-data-source-catalog)
9. [Appendix B: Metric Calculation Examples](#appendix-b-metric-calculation-examples)

---

## 1. Metrics Taxonomy

### 1.1 Metric Categories

HAIAMM uses three complementary metric categories to provide comprehensive visibility into HAI security system performance:

#### **Outcome Metrics (Lagging Indicators)**
**Purpose:** Measure whether security objectives were achieved  
**Timeframe:** Historical (weekly, monthly, quarterly)  
**Question Answered:** "Did we achieve the desired security outcome?"

**Characteristics:**
- Direct measurement of security results (vulnerabilities prevented, incidents avoided, compliance achieved)
- Quantifiable business impact (risk reduction, cost avoidance, regulatory compliance)
- Actionable for strategic decisions (resource allocation, tool selection, program investment)
- Typically measured post-deployment or post-incident

**Examples:**
- SA Outcome: System uptime ≥99.5%, API latency p95 ≤3s, model accuracy ≥85% precision/≥95% recall
- TA Outcome: Zero critical vulnerabilities deployed to production, ≥95% threat scenarios with documented mitigations

#### **Process Metrics (Leading Indicators)**
**Purpose:** Predict whether outcomes will be achieved  
**Timeframe:** Real-time or near-real-time (daily, weekly)  
**Question Answered:** "Are we on track to achieve security outcomes?"

**Characteristics:**
- Early warning signals before incidents occur (drift detection, coverage gaps, adoption trends)
- Operational health indicators (analysis throughput, feedback velocity, integration status)
- Actionable for tactical decisions (process adjustments, resource reallocation, escalation)
- Measured during development and operations

**Examples:**
- SA Process: ≥95% code coverage, cache hit rate ≥60%, feedback volume ≥100/week
- TA Process: Threat model review quarterly, threat intelligence reviewed weekly, adversarial testing conducted quarterly

#### **Effectiveness Metrics (Business Value)**
**Purpose:** Measure return on investment and business impact  
**Timeframe:** Quarterly, annually  
**Question Answered:** "Is this practice delivering measurable business value?"

**Characteristics:**
- Financial impact (cost savings, risk reduction ROI, efficiency gains)
- Strategic alignment (regulatory compliance, competitive advantage, innovation enablement)
- Stakeholder satisfaction (developer NPS, security team confidence, executive trust)
- Comparative value (vs. manual processes, vs. industry benchmarks)

**Examples:**
- SA Effectiveness: ≥50% manual intervention reduction (self-healing), ROI ≥3:1, ≥50% vulnerability reduction YoY
- TA Effectiveness: Time to mitigate high-priority threats ≤30 days, cost of threat response reduced ≥40%, zero incidents from identified-but-unmitigated threats

### 1.2 Metric Relationship Model

```
┌─────────────────────────────────────────────────────────────────┐
│                    METRICS RELATIONSHIP FLOW                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  PROCESS METRICS          OUTCOME METRICS       EFFECTIVENESS    │
│  (Leading)          →     (Lagging)        →    METRICS          │
│                                                                  │
│  Example Flow:                                                   │
│                                                                  │
│  Code coverage 95%  →  Zero critical    →  $2M breach avoided   │
│  Analysis latency   →  vulnerabilities  →  Developer NPS +40    │
│  <3s                    deployed        →  ROI 3:1              │
│  Feedback 100/wk    →  Model accuracy   →  50% faster releases  │
│                        maintains 95%                             │
│                                                                  │
│  Feedback Loop:                                                  │
│  Effectiveness metrics inform strategic investment decisions  →  │
│  → Outcome metrics validate approach → Process metrics guide    │
│  tactical execution → Loop continues                             │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### 1.3 Measurement Principles

**SMART Metrics:**
- **Specific:** Precisely defined with clear measurement criteria
- **Measurable:** Quantifiable with objective data sources
- **Achievable:** Targets based on realistic progression (L1→L2→L3)
- **Relevant:** Directly tied to security outcomes and business value
- **Time-bound:** Measured at defined intervals with clear timeframes

**Outcome-Focused:**
- Prioritize results over outputs (vulnerabilities prevented > reports generated)
- Focus on security impact over activity volume (threats mitigated > threat models created)
- Measure business value over technical activity (ROI > features deployed)

**Data-Driven:**
- All metrics automated where possible (minimize manual reporting)
- Single source of truth per metric (no conflicting data sources)
- Audit trail for metric calculations (reproducible, verifiable)

---

## 2. SA Practice Metrics Summary

### 2.1 SA-Software Metrics (All 3 Levels)

| **Maturity Level** | **Outcome Metrics** | **Process Metrics** | **Effectiveness Metrics** | **Measurement Frequency** |
|-------------------|-------------------|-------------------|-------------------------|--------------------------|
| **L1: Foundational** | • System uptime ≥99.5%<br>• API latency p95 ≤3s<br>• Concurrent requests ≥1,000<br>• Model accuracy: ≥85% precision, ≥95% recall<br>• Developer adoption ≥80% | • Code coverage ≥95%<br>• Analysis coverage ≥95% within 24h<br>• Feedback volume ≥100/week<br>• Cache hit rate ≥60%<br>• Integration coverage ≥90% repos | • Zero security incidents (AI system compromise)<br>• Training data quality ≥85% inter-rater reliability<br>• Deployment velocity ≤1 week (model training→production)<br>• DR recovery ≤4 hours (tested quarterly) | • Uptime: Real-time<br>• Latency: Real-time<br>• Accuracy: Weekly<br>• Coverage: Daily<br>• Adoption: Monthly |
| **L2: Comprehensive** | • Accuracy: ≥92% precision, ≥97% recall<br>• Scale: ≥10M LOC at ≤5s latency<br>• Developer satisfaction ≥85%<br>• Auto-remediation adoption ≥60%<br>• Real-time adaptation: ≥2% accuracy improvement/month | • Ensemble performance: ≥10% higher than single model<br>• Distributed efficiency ≥80% parallel efficiency<br>• Cache hit rate ≥70%<br>• Active learning efficiency: ≥3x vs random sampling<br>• Context-aware FP reduction ≥30% | • Feedback incorporation ≤1 hour (validated feedback→model update)<br>• False positive rate reduced ≥30% vs L1<br>• Developer time saved ≥40% (via auto-remediation)<br>• Model improvement velocity ≥2%/month | • Accuracy: Daily<br>• Efficiency: Weekly<br>• Satisfaction: Quarterly<br>• Adaptation: Monthly<br>• FP rate: Weekly |
| **L3: Industry-Leading** | • Self-healing: ≥50% manual intervention reduction<br>• Zero-trust architecture deployed<br>• Multi-cloud active-active deployment<br>• Vulnerability reduction ≥50% YoY<br>• Business ROI ≥3:1 | • Auto-scaling prediction accuracy ≥90%<br>• Model rollback triggers <5% false positives<br>• Multi-cloud failover time ≤60s<br>• Energy efficiency improvement ≥30% vs L2<br>• Open-source contributions ≥4/year | • Incident MTTR ≤15 minutes (self-healing)<br>• Predictive incident prevention ≥80%<br>• Sustainability: Carbon footprint reduced ≥30%<br>• Industry recognition (published research, awards)<br>• Vendor partnership revenue ≥$500K/year | • Self-healing: Real-time<br>• Failover: Simulated monthly<br>• ROI: Quarterly<br>• YoY metrics: Annually<br>• Contributions: Ongoing |

### 2.2 SA-Data Metrics

| **Maturity Level** | **Outcome Metrics** | **Process Metrics** | **Effectiveness Metrics** |
|-------------------|-------------------|-------------------|-------------------------|
| **L1: Foundational** | • Data classification coverage ≥95%<br>• Encryption at rest/transit 100%<br>• DLP detection accuracy ≥90%<br>• Access control coverage 100% (RBAC)<br>• Privacy compliance 100% (GDPR, CCPA) | • Training data quality ≥85% labeling accuracy<br>• Data pipeline SLA ≥99% uptime<br>• Sensitive data discovery ≥95% coverage<br>• Anonymization validation 100%<br>• Data lineage tracking 100% | • Zero data breaches from AI systems<br>• Privacy violation incidents = 0<br>• Data retention compliance 100%<br>• Audit readiness ≤24 hours<br>• Data quality cost savings ≥$200K/year |
| **L2: Comprehensive** | • Real-time DLP detection ≤1s latency<br>• Synthetic data quality ≥95% fidelity<br>• Federated learning accuracy ≥90% of centralized<br>• Differential privacy ε≤1.0 (strong privacy)<br>• Data drift detection accuracy ≥95% | • Automated data discovery ≥98% coverage<br>• Data catalog completeness ≥95%<br>• Lineage tracking real-time<br>• Privacy budget management automated 100%<br>• Cross-border compliance 100% | • Privacy-preserving ROI ≥2:1<br>• Synthetic data cost reduction ≥60%<br>• Data breach risk reduced ≥70%<br>• Compliance audit findings reduced ≥80%<br>• Data scientist productivity +40% |
| **L3: Industry-Leading** | • Homomorphic encryption in production<br>• Zero-knowledge ML deployed<br>• Quantum-resistant encryption ready<br>• Global privacy compliance 100%<br>• Self-sovereign data controls | • Automated privacy engineering 100%<br>• Real-time consent management<br>• Privacy-by-design coverage 100%<br>• Continuous compliance monitoring<br>• Privacy tech research contributions ≥3/year | • Privacy innovation revenue ≥$1M/year<br>• Regulatory leadership (standards participation)<br>• Competitive advantage from privacy<br>• Customer trust score ≥90%<br>• Industry privacy awards |

### 2.3 SA-Infrastructure Metrics

| **Maturity Level** | **Outcome Metrics** | **Process Metrics** | **Effectiveness Metrics** |
|-------------------|-------------------|-------------------|-------------------------|
| **L1: Foundational** | • Cloud security posture ≥90% compliant<br>• Container vulnerability scan coverage 100%<br>• Network segmentation 100% (AI services isolated)<br>• IaC security scan coverage ≥95%<br>• Secrets management 100% (no hardcoded) | • CSPM scan frequency: Continuous<br>• IaC policy enforcement ≥95%<br>• Vulnerability remediation MTTR ≤7 days<br>• Auto-scaling effectiveness ≥90%<br>• Infrastructure drift detection ≤24 hours | • Cloud misconfiguration incidents = 0<br>• Infrastructure cost optimization ≥20%<br>• Deployment failure rate ≤5%<br>• Compliance audit findings ≤3/year<br>• Infrastructure automation ≥80% |
| **L2: Comprehensive** | • Multi-region HA ≥99.95% uptime<br>• Auto-remediation coverage ≥70%<br>• Chaos engineering resilience ≥99%<br>• Zero-downtime deployments 100%<br>• Infrastructure security score ≥95% | • Policy-as-code coverage 100%<br>• Automated remediation MTTR ≤1 hour<br>• Chaos test frequency: Monthly<br>• Service mesh security 100%<br>• Observability coverage ≥98% | • Infrastructure MTTR reduced ≥60%<br>• Deployment velocity +100%<br>• Security incidents from infra = 0<br>• Cloud spend optimization ≥40%<br>• SRE team efficiency +50% |
| **L3: Industry-Leading** | • AI-driven auto-healing ≥90%<br>• Predictive capacity planning ≥95% accuracy<br>• Self-optimizing infrastructure<br>• Quantum-ready cryptography<br>• Multi-cloud orchestration seamless | • AIOps incident prediction ≥85%<br>• Infrastructure-as-data analytics<br>• Automated cost optimization continuous<br>• Zero-trust micro-segmentation 100%<br>• Green infrastructure ≥50% carbon reduction | • Infrastructure incidents ≤1/year<br>• Capacity planning cost savings ≥$2M/year<br>• Sustainability leadership<br>• Industry infrastructure research ≥2/year<br>• Platform revenue ≥$5M/year |

### 2.4 SA-Vendors Metrics

| **Maturity Level** | **Outcome Metrics** | **Process Metrics** | **Effectiveness Metrics** |
|-------------------|-------------------|-------------------|-------------------------|
| **L1: Foundational** | • Vendor security assessment coverage 100%<br>• Third-party risk scoring ≥80% accuracy<br>• SLA compliance monitoring ≥95%<br>• Vendor incident response ≤4 hours<br>• Contract security terms 100% | • Vendor onboarding security checks 100%<br>• Continuous vendor monitoring<br>• SBOM coverage ≥95%<br>• Vendor access reviews quarterly<br>• Vendor risk reassessment annually | • Vendor-related incidents ≤2/year<br>• Vendor consolidation savings ≥15%<br>• Contract negotiation time reduced ≥30%<br>• Vendor compliance validated 100%<br>• Supply chain visibility ≥90% |
| **L2: Comprehensive** | • Real-time vendor risk scoring<br>• Automated vendor compliance verification<br>• Vendor security posture ≥90%<br>• Fourth-party risk visibility ≥80%<br>• Vendor breach notification ≤2 hours | • Vendor security dashboard real-time<br>• Automated vendor offboarding<br>• API security monitoring continuous<br>• License compliance automated 100%<br>• Vendor concentration risk ≤20% any single vendor | • Vendor incident MTTR ≤2 hours<br>• Third-party risk reduced ≥50%<br>• Vendor switching time reduced ≥60%<br>• Procurement efficiency +40%<br>• Vendor ecosystem trust score ≥85% |
| **L3: Industry-Leading** | • Predictive vendor risk modeling<br>• AI-driven vendor security benchmarking<br>• Supply chain attack prevention ≥99%<br>• Vendor ecosystem orchestration<br>• Regulatory leadership in vendor management | • Vendor security intelligence sharing<br>• Industry vendor risk standards contribution<br>• Automated vendor breach response<br>• Vendor security co-development<br>• Vendor community engagement ≥10 events/year | • Supply chain resilience ≥99.9%<br>• Vendor ecosystem revenue ≥$3M/year<br>• Industry vendor security leadership<br>• Zero critical vendor incidents<br>• Vendor partnership innovation ≥5/year |

### 2.5 SA-Processes Metrics

| **Maturity Level** | **Outcome Metrics** | **Process Metrics** | **Effectiveness Metrics** |
|-------------------|-------------------|-------------------|-------------------------|
| **L1: Foundational** | • SOAR automation coverage ≥60%<br>• Playbook execution success ≥95%<br>• Incident response MTTR ≤4 hours<br>• False positive rate ≤20%<br>• Workflow SLA compliance ≥95% | • Playbook coverage ≥80% incident types<br>• Automation testing frequency: Monthly<br>• Workflow documentation 100%<br>• Integration health monitoring continuous<br>• Alert triage time ≤15 minutes | • SOC efficiency +40%<br>• Analyst burnout reduced ≥30%<br>• Incident cost reduced ≥50%<br>• Compliance reporting automated 80%<br>• Audit preparation time ≤2 days |
| **L2: Comprehensive** | • AI-driven triage accuracy ≥90%<br>• Autonomous response coverage ≥40%<br>• Alert fatigue reduction ≥60%<br>• Cross-domain orchestration ≥80%<br>• Adaptive playbooks deployed | • Playbook optimization continuous<br>• AI decision explainability 100%<br>• Workflow A/B testing monthly<br>• Integration redundancy ≥2 paths<br>• Chaos testing quarterly | • Tier 1 SOC workload reduced ≥70%<br>• MTTR improvement ≥60%<br>• False positive reduction ≥50%<br>• Analyst satisfaction +50 NPS<br>• Incident prevention ≥30% |
| **L3: Industry-Leading** | • Self-healing security operations ≥70%<br>• Predictive incident prevention ≥80%<br>• Zero-touch incident response ≥50%<br>• AI-human collaboration seamless<br>• Industry SOAR leadership | • AIOps maturity ≥Level 4<br>• Process innovation deployment continuous<br>• Industry research contributions ≥3/year<br>• Vendor partnerships ≥5<br>• Open-source SOAR contributions ≥6/year | • SOC cost per incident reduced ≥80%<br>• Security operations ROI ≥5:1<br>• Industry recognition (awards, research)<br>• SOAR platform revenue ≥$2M/year<br>• Zero critical incidents from automation failure |

### 2.6 SA-Endpoints Metrics

| **Maturity Level** | **Outcome Metrics** | **Process Metrics** | **Effectiveness Metrics** |
|-------------------|-------------------|-------------------|-------------------------|
| **L1: Foundational** | • EDR deployment coverage ≥95%<br>• Malware detection accuracy ≥98%<br>• Endpoint vulnerability remediation ≤7 days<br>• Device compliance ≥90%<br>• Endpoint incidents ≤5/quarter | • Endpoint agent health ≥98%<br>• Policy enforcement 100%<br>• Threat hunting frequency: Weekly<br>• Endpoint baseline drift detection ≤24h<br>• Patch deployment ≤72 hours | • Endpoint breach prevention ≥99%<br>• Ransomware incidents = 0<br>• Help desk tickets reduced ≥25%<br>• Compliance audit findings ≤2/year<br>• Endpoint management cost reduced ≥20% |
| **L2: Comprehensive** | • AI-driven threat detection ≥95% accuracy<br>• Autonomous isolation ≥80% incidents<br>• Behavioral anomaly detection ≥90%<br>• Zero-trust endpoint coverage 100%<br>• Endpoint MTTR ≤30 minutes | • ML model accuracy monitoring daily<br>• Automated remediation ≥60%<br>• Threat intelligence integration real-time<br>• User behavior analytics coverage ≥95%<br>• Endpoint forensics automated 100% | • Endpoint incident MTTR reduced ≥70%<br>• False positive rate ≤5%<br>• User productivity impact ≤2%<br>• Analyst workload reduced ≥50%<br>• Endpoint security ROI ≥3:1 |
| **L3: Industry-Leading** | • Predictive threat prevention ≥85%<br>• Self-healing endpoints ≥70%<br>• AI-driven user behavior trust scoring<br>• Quantum-resistant endpoint encryption<br>• Zero critical endpoint incidents | • AIOps endpoint management<br>• Continuous adaptive trust<br>• Industry threat research ≥4/year<br>• Endpoint innovation patents ≥2/year<br>• Vendor collaboration ≥6 partnerships | • Endpoint security incidents = 0<br>• Productivity improvement +30%<br>• Industry endpoint security leadership<br>• Platform licensing revenue ≥$1M/year<br>• User trust score ≥95% |

---

## 3. TA Practice Metrics Summary

### 3.1 TA-Software Metrics (All 3 Levels)

| **Maturity Level** | **Outcome Metrics** | **Process Metrics** | **Effectiveness Metrics** |
|-------------------|-------------------|-------------------|-------------------------|
| **L1: Foundational** | • Threat scenarios documented ≥10 (AI-specific)<br>• Training completion ≥80% (developers, security, leadership)<br>• AI agent threat mapping 100%<br>• Executive threat briefing completed | • Threat scenario review frequency: Annually<br>• Training delivery timeline ≤90 days post-deployment<br>• Threat awareness assessment ≥75% pass rate<br>• Threat inventory updates quarterly | • Zero incidents from undocumented threats<br>• Stakeholder threat awareness ≥80%<br>• Training ROI: ≥30% incident reduction<br>• Compliance: Threat documentation 100%<br>• Time to threat identification ≤30 days |
| **L2: Comprehensive** | • Abuse cases per AI agent ≥3<br>• Risk matrix coverage 100% threats<br>• High-priority threat mitigations ≥90% implemented<br>• Quarterly threat model updates | • Likelihood × impact scoring consistent<br>• Mitigation tracking ≥95% high-priority threats<br>• Threat reassessment quarterly<br>• Attack tree coverage ≥80% critical agents<br>• Evidence of mitigation deployment | • Time to mitigate high-priority threats ≤30 days<br>• Threat-driven security investment ≥$500K/year<br>• Incident reduction from prioritized threats ≥60%<br>• Risk-based roadmap adoption 100%<br>• Threat model ROI ≥2:1 |
| **L3: Industry-Leading** | • Threat intelligence monitoring continuous<br>• Adversarial testing quarterly<br>• Red team exercise annually<br>• Model drift monitoring automated<br>• Industry threat intelligence contributions ≥2/year | • CVE monitoring weekly<br>• Academic research review monthly<br>• Evasion testing ≥95% detection maintained<br>• Prompt injection testing semi-annually<br>• Vendor responsible disclosure ≥3/year | • Zero incidents from emerging threats<br>• Adversarial testing ROI: ≥$1M breach prevention<br>• Threat detection improvement ≥5% quarterly<br>• Industry collaboration value ≥$200K/year<br>• Proactive threat mitigation ≥80% |

### 3.2 TA-Data Metrics

| **Maturity Level** | **Outcome Metrics** | **Process Metrics** | **Effectiveness Metrics** |
|-------------------|-------------------|-------------------|-------------------------|
| **L1: Foundational** | • Data poisoning scenarios documented ≥8<br>• Training data threats identified 100%<br>• Privacy threat assessment complete<br>• Data breach threat scenarios ≥5 | • Threat scenario updates annually<br>• Data security training ≥80% completion<br>• Sensitive data threat mapping 100%<br>• ML pipeline threat coverage 100% | • Zero data poisoning incidents<br>• Privacy violation prevention 100%<br>• Training data integrity maintained<br>• Threat awareness cost avoidance ≥$300K/year<br>• Compliance violations = 0 |
| **L2: Comprehensive** | • Data attack trees ≥3 per pipeline<br>• Privacy risk scoring automated<br>• Cross-border threat assessment complete<br>• Data exfiltration scenarios ≥5 | • Risk matrix updates quarterly<br>• Privacy threat prioritization documented<br>• Mitigation evidence ≥90%<br>• Data lineage threat coverage 100%<br>• Federated learning threat assessment complete | • Data breach risk reduced ≥70%<br>• Privacy threat mitigation ≤60 days<br>• Model poisoning prevention 100%<br>• Regulatory compliance maintained<br>• Data security ROI ≥3:1 |
| **L3: Industry-Leading** | • Adversarial data testing quarterly<br>• Privacy red teaming annually<br>• Model inversion testing continuous<br>• Membership inference prevention ≥99%<br>• Industry privacy threat research ≥2/year | • Privacy threat intelligence weekly<br>• Data security CVE monitoring continuous<br>• Synthetic data attack testing monthly<br>• Differential privacy audit automated<br>• Academic collaboration ≥3/year | • Zero advanced persistent threats (data)<br>• Privacy attack prevention ≥99.9%<br>• Threat research revenue ≥$500K/year<br>• Industry privacy leadership recognized<br>• Proactive defense effectiveness ≥90% |

### 3.3 TA-Infrastructure Metrics

| **Maturity Level** | **Outcome Metrics** | **Process Metrics** | **Effectiveness Metrics** |
|-------------------|-------------------|-------------------|-------------------------|
| **L1: Foundational** | • Cloud threat scenarios ≥10<br>• Container security threats documented ≥8<br>• Network attack scenarios ≥6<br>• Infrastructure training ≥80% completion | • Threat updates annually<br>• Cloud threat awareness ≥75%<br>• Kubernetes threat mapping 100%<br>• IaC threat coverage 100% | • Cloud misconfiguration incidents = 0<br>• Container breach prevention 100%<br>• Infrastructure threat awareness ROI ≥$400K/year<br>• Compliance: Infrastructure threats documented<br>• Incident prevention ≥40% |
| **L2: Comprehensive** | • Cloud abuse cases ≥3 per service<br>• Attack surface mapping automated<br>• Lateral movement scenarios ≥5<br>• Supply chain threat assessment complete | • Infrastructure risk scoring quarterly<br>• Threat prioritization evidence ≥90%<br>• Mitigation tracking continuous<br>• Multi-cloud threat coverage 100%<br>• Zero-trust threat modeling complete | • Infrastructure attack prevention ≥95%<br>• Lateral movement blocked 100%<br>• Threat-driven hardening ≥85%<br>• Infrastructure MTTR ≤2 hours<br>• Security posture improvement ≥50% |
| **L3: Industry-Leading** | • Infrastructure red teaming quarterly<br>• Cloud breach simulation annually<br>• Chaos engineering security testing monthly<br>• Supply chain attack testing continuous<br>• Industry infrastructure research ≥2/year | • Threat intelligence integration real-time<br>• Automated threat modeling<br>• Kubernetes CVE monitoring daily<br>• Cloud threat hunting weekly<br>• Academic partnerships ≥2 | • Zero critical infrastructure incidents<br>• Advanced threat prevention ≥99%<br>• Research revenue ≥$300K/year<br>• Industry leadership recognized<br>• Proactive security effectiveness ≥85% |

### 3.4 TA-Vendors Metrics

| **Maturity Level** | **Outcome Metrics** | **Process Metrics** | **Effectiveness Metrics** |
|-------------------|-------------------|-------------------|-------------------------|
| **L1: Foundational** | • Vendor threat scenarios ≥8<br>• Supply chain threat documentation complete<br>• Third-party risk scenarios ≥6<br>• Vendor security training ≥80% completion | • Vendor threat updates annually<br>• Supply chain awareness ≥75%<br>• Vendor threat mapping 100%<br>• SaaS threat coverage 100% | • Vendor-sourced incidents = 0<br>• Supply chain breach prevention 100%<br>• Vendor threat awareness ROI ≥$250K/year<br>• Compliance maintained<br>• Vendor risk visibility ≥90% |
| **L2: Comprehensive** | • Vendor abuse cases ≥3 per critical vendor<br>• Fourth-party threat assessment complete<br>• API security threat scenarios ≥5<br>• Vendor concentration risk documented | • Vendor risk reassessment quarterly<br>• Supply chain threat prioritization<br>• Mitigation evidence ≥90%<br>• Vendor threat intelligence monitoring<br>• Incident simulation annually | • Vendor incident prevention ≥90%<br>• Supply chain risk reduced ≥60%<br>• Vendor MTTR ≤4 hours<br>• Procurement security improvement +50%<br>• Vendor security ROI ≥2:1 |
| **L3: Industry-Leading** | • Vendor red teaming annually<br>• Supply chain adversarial testing quarterly<br>• API security testing continuous<br>• Vendor breach simulation bi-annually<br>• Industry vendor threat research ≥2/year | • Vendor threat intelligence daily<br>• Automated vendor threat modeling<br>• SBOM vulnerability monitoring real-time<br>• Vendor threat hunting monthly<br>• Industry collaboration ≥4/year | • Zero critical vendor incidents<br>• Supply chain attack prevention ≥99.9%<br>• Research contributions recognized<br>• Vendor ecosystem trust ≥95%<br>• Proactive vendor security ≥90% |

### 3.5 TA-Processes Metrics

| **Maturity Level** | **Outcome Metrics** | **Process Metrics** | **Effectiveness Metrics** |
|-------------------|-------------------|-------------------|-------------------------|
| **L1: Foundational** | • SOAR threat scenarios ≥10<br>• Automation abuse threats documented ≥6<br>• Workflow manipulation scenarios ≥5<br>• Process security training ≥80% completion | • Threat updates annually<br>• SOAR threat awareness ≥75%<br>• Playbook threat mapping 100%<br>• Automation threat coverage 100% | • SOAR compromise incidents = 0<br>• Automation abuse prevention 100%<br>• Workflow integrity maintained<br>• Threat awareness ROI ≥$200K/year<br>• Process security incidents ≤2/year |
| **L2: Comprehensive** | • SOAR abuse cases ≥3 per workflow<br>• AI decision manipulation scenarios ≥5<br>• Alert suppression threat assessment complete<br>• Cross-process threat coverage 100% | • Process risk scoring quarterly<br>• Threat prioritization evidence ≥90%<br>• Mitigation tracking continuous<br>• Workflow security testing monthly<br>• Playbook validation automated | • Process manipulation prevention ≥95%<br>• SOAR security MTTR ≤1 hour<br>• Workflow integrity ≥99.9%<br>• Automation trust score ≥90%<br>• Process security ROI ≥3:1 |
| **L3: Industry-Leading** | • SOAR red teaming quarterly<br>• Automation adversarial testing continuous<br>• AI decision manipulation testing monthly<br>• Process chaos engineering quarterly<br>• Industry SOAR threat research ≥2/year | • SOAR threat intelligence weekly<br>• Automated threat modeling<br>• Playbook vulnerability scanning continuous<br>• Workflow threat hunting monthly<br>• Academic collaboration ≥2/year | • Zero critical process security incidents<br>• Advanced automation threats prevented ≥99%<br>• Research recognized industry-wide<br>• SOAR security leadership<br>• Proactive process security ≥85% |

### 3.6 TA-Endpoints Metrics

| **Maturity Level** | **Outcome Metrics** | **Process Metrics** | **Effectiveness Metrics** |
|-------------------|-------------------|-------------------|-------------------------|
| **L1: Foundational** | • Endpoint AI threat scenarios ≥10<br>• EDR manipulation threats documented ≥6<br>• Device compromise scenarios ≥8<br>• Endpoint security training ≥80% completion | • Threat updates annually<br>• EDR threat awareness ≥75%<br>• Endpoint threat mapping 100%<br>• AI agent threat coverage 100% | • EDR compromise incidents = 0<br>• Endpoint threat prevention ≥98%<br>• Device security maintained<br>• Threat awareness ROI ≥$300K/year<br>• Ransomware incidents = 0 |
| **L2: Comprehensive** | • EDR abuse cases ≥3 per agent type<br>• AI evasion scenarios ≥5<br>• User behavior manipulation threats ≥4<br>• BYOD threat assessment complete | • Endpoint risk scoring quarterly<br>• Threat prioritization evidence ≥90%<br>• Mitigation tracking continuous<br>• Endpoint testing monthly<br>• Behavioral anomaly threat coverage 100% | • AI evasion prevention ≥95%<br>• Endpoint MTTR ≤30 minutes<br>• User trust maintained ≥90%<br>• Endpoint security improvement +60%<br>• Endpoint threat ROI ≥3:1 |
| **L3: Industry-Leading** | • Endpoint red teaming quarterly<br>• AI adversarial testing continuous<br>• Behavioral analysis evasion testing monthly<br>• Zero-trust endpoint simulation quarterly<br>• Industry endpoint threat research ≥2/year | • Endpoint threat intelligence daily<br>• Automated threat modeling<br>• EDR vulnerability monitoring real-time<br>• Endpoint threat hunting weekly<br>• Vendor collaboration ≥4/year | • Zero critical endpoint incidents<br>• Advanced endpoint threats prevented ≥99.5%<br>• Research contributions recognized<br>• Industry endpoint security leadership<br>• Proactive endpoint defense ≥90% |

---

## 4. Measurement Methodology

### 4.1 Baseline Establishment

**Purpose:** Establish current state before improvement initiatives

**Process:**
1. **Data Collection Period:** Minimum 30 days of operational data for statistical significance
2. **Metric Calculation:** Use methodology from Appendix B for each metric
3. **Variance Analysis:** Calculate standard deviation to understand stability
4. **Baseline Documentation:** Record baseline value, collection period, data sources, calculation method
5. **Validation:** Review baseline with stakeholders for reasonableness

**Example Baseline (SA-Software L1):**
```
Metric: Model Accuracy (Precision)
Baseline Period: 2026-01-01 to 2026-01-31
Data Source: AI security tool analytics dashboard
Calculation Method: TP / (TP + FP) where TP = True Positives, FP = False Positives
Baseline Value: 78.3% precision (σ = 4.2%)
Sampling: 2,847 vulnerability findings, 487 developer feedback validations
Validation: Reviewed by Security Engineering Lead on 2026-02-05
```

### 4.2 Target Setting

**Realistic Progression Framework:**

| **Metric Type** | **L1 Target Setting** | **L1→L2 Improvement** | **L2→L3 Improvement** |
|----------------|----------------------|----------------------|----------------------|
| **Accuracy Metrics** | Baseline + 5-10% or industry standard (whichever higher) | +5-8% improvement | +3-5% improvement (diminishing returns) |
| **Performance Metrics** | 90% of theoretical maximum | +5-10% optimization | +2-5% optimization |
| **Coverage Metrics** | ≥90% coverage | ≥95% coverage | ≥98% coverage |
| **Adoption Metrics** | ≥75% adoption | ≥85% adoption | ≥95% adoption |
| **Financial Metrics** | Positive ROI (≥1:1) | ROI ≥2:1 | ROI ≥3:1 |

**Target Setting Process:**
1. **Reference Baseline:** Start with current performance
2. **Industry Benchmarking:** Compare to industry standards (NIST, OWASP, vendor benchmarks)
3. **Effort Assessment:** Estimate effort required to achieve target (use OpenSAMM effort model)
4. **Stakeholder Alignment:** Validate targets with engineering leadership and business owners
5. **Phased Approach:** Set quarterly milestones toward annual target
6. **Document Rationale:** Record why target is achievable and valuable

**Example Target (SA-Software L1 → L2):**
```
Metric: Model Accuracy (Precision)
Current State (L1 Achieved): 87.2% precision
Target (L2): 92% precision (+4.8% improvement)
Rationale: 
  - Industry benchmark (Snyk, GitHub Advanced Security): 90-93% precision
  - Ensemble model architecture (L2 activity) expected to yield +5-7% improvement
  - Phased rollout: Q1: 89%, Q2: 90%, Q3: 91%, Q4: 92%
Effort: 18 weeks (per SA-Software L2 ensemble architecture implementation)
Owner: ML Engineering Team Lead
Review Frequency: Monthly progress reviews, quarterly target adjustment
```

### 4.3 Measurement Frequency

| **Metric Category** | **Recommended Frequency** | **Rationale** | **Data Retention** |
|--------------------|--------------------------|--------------|-------------------|
| **System Health (uptime, latency)** | Real-time monitoring, aggregated hourly | Critical for operational response | 13 months (rolling) |
| **Accuracy Metrics (precision, recall)** | Daily calculation, weekly review | Detect drift early, balance noise vs signal | 24 months |
| **Coverage Metrics (code analysis %)** | Daily calculation, monthly trend analysis | Leading indicator for exposure | 12 months |
| **Adoption Metrics (tool usage %)** | Weekly calculation, monthly review | Inform training and communication needs | 12 months |
| **Process Metrics (feedback volume)** | Daily tracking, weekly review | Operational health indicator | 12 months |
| **Effectiveness Metrics (ROI, cost savings)** | Quarterly calculation | Strategic decision-making cycle | 36 months |
| **Maturity Assessment** | Semi-annually or annually | Comprehensive evaluation requires time | Permanent (historical record) |

### 4.4 Data Sources

See **Appendix A: Data Source Catalog** for comprehensive mapping of metrics to data sources.

**Data Quality Requirements:**
- **Accuracy:** Data must be factually correct (validated against source systems)
- **Completeness:** ≥95% data coverage (minimal missing values)
- **Timeliness:** Data fresher than measurement frequency (real-time metrics ≤5 min lag)
- **Consistency:** Single source of truth per metric (no conflicting sources)
- **Auditability:** Data lineage documented (source → transformation → metric)

### 4.5 Ownership Model

| **Role** | **Responsibilities** | **Metrics Owned** |
|----------|---------------------|------------------|
| **Security Engineering Lead** | Overall metrics program, target setting, stakeholder reporting | All outcome metrics, effectiveness metrics |
| **ML Engineering Team** | Model performance metrics, accuracy tracking, drift detection | SA/TA model accuracy, performance, drift metrics |
| **DevOps/SRE Team** | Infrastructure metrics, system health, uptime, performance | SA infrastructure, latency, uptime, scalability metrics |
| **Security Operations Team** | Process metrics, incident metrics, threat metrics | TA threat coverage, incident prevention, SOAR metrics |
| **Product/Engineering Manager** | Adoption metrics, developer satisfaction, business value | Adoption rates, developer NPS, productivity impact |
| **Finance/Business Analyst** | ROI calculations, cost metrics, business effectiveness | ROI, cost savings, efficiency gains, revenue metrics |
| **Compliance/Risk Team** | Compliance metrics, audit readiness, regulatory alignment | Compliance coverage, audit findings, regulatory violations |

**Escalation Path:**
1. Metric Owner → Team Lead (operational issues, data quality)
2. Team Lead → Security Engineering Lead (target misses, trend concerns)
3. Security Engineering Lead → CISO (strategic program issues, investment decisions)

---

## 5. Maturity Scoring Integration

### 5.1 Metrics-Based Maturity Determination

**Principle:** Maturity levels require BOTH activity completion AND metric achievement

**Scoring Model:**

```
Maturity Level Achievement = Activities Completed (60%) + Metrics Achieved (40%)

Where:
- Activities Completed = % of Level activities implemented (from questionnaire)
- Metrics Achieved = % of Level metrics meeting target thresholds
```

**Rationale:**
- Activities demonstrate **capability** (we can do the work)
- Metrics demonstrate **effectiveness** (the work delivers results)
- 60/40 weighting prevents "checklist compliance" without outcomes

### 5.2 Minimum Metric Thresholds

**Level 1 Achievement Requirements:**

| **Domain** | **SA Minimum Thresholds** | **TA Minimum Thresholds** |
|-----------|-------------------------|-------------------------|
| **Software** | • Uptime ≥99.5%<br>• Latency p95 ≤3s<br>• Model accuracy ≥85% precision, ≥95% recall<br>• Developer adoption ≥75% | • Threat scenarios ≥10<br>• Training completion ≥75%<br>• Threat mapping 100%<br>• Executive briefing completed |
| **Data** | • Data classification ≥90%<br>• Encryption 100%<br>• DLP accuracy ≥85%<br>• Access control 100% | • Poisoning scenarios ≥8<br>• Training threats identified 100%<br>• Privacy assessment complete |
| **Infrastructure** | • Cloud posture ≥85%<br>• Container scan 100%<br>• Network segmentation 100%<br>• IaC scan ≥90% | • Cloud threats ≥10<br>• Container threats ≥8<br>• Network attacks ≥6<br>• Training ≥75% |
| **Vendors** | • Vendor assessment 100%<br>• Risk scoring ≥75% accuracy<br>• SLA monitoring ≥90%<br>• Security terms 100% | • Vendor threats ≥8<br>• Supply chain docs complete<br>• Third-party scenarios ≥6<br>• Training ≥75% |
| **Processes** | • SOAR automation ≥50%<br>• Playbook success ≥90%<br>• MTTR ≤6 hours<br>• False positive ≤25% | • SOAR threats ≥10<br>• Automation abuse ≥6<br>• Workflow manipulation ≥5<br>• Training ≥75% |
| **Endpoints** | • EDR coverage ≥90%<br>• Malware detection ≥95%<br>• Remediation ≤10 days<br>• Compliance ≥85% | • Endpoint threats ≥10<br>• EDR manipulation ≥6<br>• Device compromise ≥8<br>• Training ≥75% |

**Level 2 Achievement Requirements:**

Must achieve ALL L1 thresholds PLUS L2-specific metrics (see domain tables in Section 2 and 3).

**Level 3 Achievement Requirements:**

Must achieve ALL L1 and L2 thresholds PLUS L3-specific metrics.

### 5.3 Assessment Integration

**Questionnaire + Metrics Assessment Process:**

```
┌────────────────────────────────────────────────────────────────┐
│            HAIAMM MATURITY ASSESSMENT PROCESS                  │
├────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Phase 1: Questionnaire Assessment                             │
│  ├─ Answer practice questions (243 total, ~3 per domain-level) │
│  ├─ Collect evidence (documents, configs, dashboards)          │
│  └─ Calculate activity score: % implemented                    │
│                                                                 │
│  Phase 2: Metrics Validation                                   │
│  ├─ Collect metric data (30-90 days)                          │
│  ├─ Calculate metric achievement: % thresholds met            │
│  └─ Document metric evidence (dashboards, reports)             │
│                                                                 │
│  Phase 3: Combined Scoring                                     │
│  ├─ Maturity Score = (Activity % × 0.6) + (Metric % × 0.4)    │
│  ├─ Apply minimum thresholds (must meet ALL for level)        │
│  └─ Determine maturity level per practice-domain              │
│                                                                 │
│  Phase 4: Gap Analysis                                         │
│  ├─ Identify missing activities (from questionnaire)           │
│  ├─ Identify metric gaps (from threshold comparison)           │
│  └─ Prioritize by impact and effort                           │
│                                                                 │
│  Phase 5: Roadmap Creation                                    │
│  ├─ Sequence improvements (dependencies, quick wins)           │
│  ├─ Estimate effort (OpenSAMM methodology)                     │
│  └─ Assign owners and timelines                               │
│                                                                 │
└────────────────────────────────────────────────────────────────┘
```

**Example Assessment (SA-Software L1):**

```
Practice: Security Architecture (SA)
Domain: Software
Target Level: L1

Activity Assessment (Questionnaire):
  Q1: Model architecture designed? YES (hybrid models, multi-stage pipeline)
  Q2: Data architecture established? YES (training data, repository integration)
  Q3: Integration architecture deployed? YES (IDE, CI/CD, code review)
  Q4: Infrastructure architecture implemented? PARTIAL (cloud-native, but uptime <99.5%)
  Q5: Security architecture complete? YES (model security, credentials, network)
  Q6: Feedback loops operational? YES (multi-channel, retraining pipeline)
  Q7: Monitoring architecture deployed? YES (infrastructure, model, security outcomes)
  
  Activity Score: 6.5 / 7 = 93%

Metric Validation:
  • Uptime: 99.2% (BELOW threshold 99.5%) ❌
  • Latency p95: 2.8s (MEETS threshold ≤3s) ✅
  • Concurrent requests: 1,200 (MEETS threshold ≥1,000) ✅
  • Precision: 87.1% (MEETS threshold ≥85%) ✅
  • Recall: 96.3% (MEETS threshold ≥95%) ✅
  • Developer adoption: 82% (MEETS threshold ≥80%) ✅
  
  Metrics Achieved: 5 / 6 = 83%

Combined Maturity Score:
  Score = (93% × 0.6) + (83% × 0.4) = 55.8% + 33.2% = 89%

Minimum Threshold Check:
  ❌ FAIL: Uptime 99.2% below required 99.5%
  
Assessment Result: NOT YET L1
  Reason: Uptime threshold not met (critical outcome metric)
  Gap: Infrastructure resilience needs improvement (+0.3% uptime)
  Recommendation: Implement multi-zone deployment, load balancer HA

Time to Remediation: 4-6 weeks (infrastructure hardening)
Re-assessment: After uptime ≥99.5% sustained for 30 days
```

### 5.4 Metric Weighting by Criticality

**Not all metrics are equal.** Some are **critical** (must meet threshold) vs **important** (contribute to overall score).

**Critical Metrics (Must Meet Threshold):**
- SA: Uptime, accuracy (precision/recall), security incidents = 0
- TA: Threat coverage, training completion, zero incidents from undocumented threats

**Important Metrics (Contribute to Score):**
- SA: Latency, cache hit rate, feedback volume, efficiency
- TA: Testing frequency, intelligence monitoring cadence, research contributions

**Scoring Adjustment:**
```
IF any Critical Metric below threshold:
  Maturity Level = NOT ACHIEVED (regardless of overall score)
ELSE:
  Maturity Level = Based on combined score + important metrics
```

---

## 6. Dashboard Templates

### 6.1 Executive Summary Dashboard

**Purpose:** Board/C-suite visibility into HAI security program health  
**Audience:** CISO, CTO, CEO, Board  
**Update Frequency:** Monthly  
**Format:** Single-page executive summary

**Dashboard Sections:**

```
┌─────────────────────────────────────────────────────────────────┐
│         HAIAMM EXECUTIVE SECURITY DASHBOARD                     │
│                  Month: January 2026                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│ OVERALL MATURITY                                                │
│ ├─ Current Maturity: Level 1.7 (↑0.2 from Dec 2025)           │
│ ├─ Target Maturity: Level 2.0 by Q4 2026                       │
│ ├─ Progress: 85% toward L2 (on track)                          │
│ └─ RAG Status: 🟢 GREEN                                        │
│                                                                  │
│ SECURITY OUTCOMES (This Month)                                  │
│ ├─ Critical Vulnerabilities Prevented: 47 (↑12 from Dec)       │
│ ├─ Security Incidents: 0 (🟢 Target: 0)                        │
│ ├─ System Uptime: 99.7% (🟢 Target: ≥99.5%)                    │
│ ├─ Model Accuracy: 89.3% precision (🟢 Target: ≥85%)           │
│ └─ Developer Adoption: 84% (🟢 Target: ≥80%)                   │
│                                                                  │
│ BUSINESS VALUE (YTD)                                            │
│ ├─ ROI: 2.3:1 ($1.2M value / $520K investment)                │
│ ├─ Breach Risk Reduction: $3.4M (estimated)                   │
│ ├─ Developer Productivity Gain: +38% (security tasks)          │
│ ├─ Compliance: 100% (zero audit findings)                      │
│ └─ Competitive Advantage: Industry recognition (OWASP talk)     │
│                                                                  │
│ RISKS & CONCERNS                                                │
│ ├─ 🟡 AMBER: False positive rate 18% (target ≤15% by Q2)       │
│ ├─ 🟡 AMBER: Vendor threat coverage 78% (target ≥90% by Q3)    │
│ └─ 🟢 GREEN: All other metrics within acceptable range         │
│                                                                  │
│ KEY INITIATIVES (This Quarter)                                  │
│ ├─ Ensemble Model Deployment (L2) - 60% complete               │
│ ├─ Distributed Architecture Rollout - 40% complete              │
│ ├─ Automated Remediation Launch - In progress                  │
│ └─ Vendor Threat Assessment Program - Scoping                   │
│                                                                  │
│ NEXT BOARD UPDATE: February 2026                                │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**RAG Status Definitions:**

| **Status** | **Criteria** | **Action Required** |
|-----------|-------------|-------------------|
| 🟢 **GREEN** | ≥90% metrics meeting targets, no critical risks, on track for maturity goals | Continue monitoring, celebrate wins |
| 🟡 **AMBER** | 70-89% metrics meeting targets, OR 1-2 important metrics below target, OR moderate risk identified | Tactical adjustments, resource reallocation, monthly review |
| 🔴 **RED** | <70% metrics meeting targets, OR any critical metric failing, OR high/critical risk identified | Executive intervention, escalation, strategy review, remediation plan required |

### 6.2 Operational Metrics Dashboard

**Purpose:** Day-to-day operational health and performance tracking  
**Audience:** Security Engineering, ML Engineering, DevOps, SOC teams  
**Update Frequency:** Real-time (refreshed every 5-15 minutes)  
**Format:** Multi-panel dashboard (Grafana, Datadog, Splunk)

**Dashboard Panels:**

**Panel 1: System Health (Real-Time)**
```
┌─────────────────────────────────────────────┐
│ SYSTEM HEALTH - LIVE                         │
├─────────────────────────────────────────────┤
│ Uptime: 99.82% (Last 30 days)               │
│   └─ Current Status: 🟢 OPERATIONAL          │
│ API Latency (p95): 2.4s                     │
│   └─ Trend: ↓ (3.1s → 2.4s last 7 days)     │
│ Concurrent Requests: 1,340 / 2,000          │
│   └─ Utilization: 67% (🟢 HEALTHY)          │
│ Error Rate: 0.3%                            │
│   └─ Threshold: <1% (🟢 PASS)               │
└─────────────────────────────────────────────┘
```

**Panel 2: Model Performance (Daily)**
```
┌─────────────────────────────────────────────┐
│ MODEL ACCURACY - DAILY TREND                 │
├─────────────────────────────────────────────┤
│ Precision: 88.7% (↑0.4% from yesterday)     │
│   └─ Target: ≥85% (🟢 EXCEEDS)              │
│ Recall: 96.1% (↔ stable)                    │
│   └─ Target: ≥95% (🟢 EXCEEDS)              │
│ F1 Score: 92.2%                             │
│ False Positive Rate: 16.8%                  │
│   └─ Trend: ↓ (19.2% → 16.8% last 30 days)  │
│ Model Drift: 2.3% (🟢 ACCEPTABLE <5%)       │
└─────────────────────────────────────────────┘
```

**Panel 3: Coverage & Adoption (Daily)**
```
┌─────────────────────────────────────────────┐
│ COVERAGE & ADOPTION                          │
├─────────────────────────────────────────────┤
│ Code Analysis Coverage: 96.4%               │
│   └─ Repositories: 287 / 294 (97.6%)        │
│ Developer Adoption: 85.2%                   │
│   └─ Active Users: 523 / 614 developers     │
│ IDE Plugin Install: 88.1%                   │
│   └─ Daily Active: 71.3%                    │
│ CI/CD Integration: 93.5%                    │
│   └─ Pipelines Enabled: 1,847 / 1,975       │
└─────────────────────────────────────────────┘
```

**Panel 4: Security Outcomes (Weekly)**
```
┌─────────────────────────────────────────────┐
│ SECURITY OUTCOMES - LAST 7 DAYS              │
├─────────────────────────────────────────────┤
│ Vulnerabilities Detected: 142               │
│   └─ Critical: 3, High: 18, Medium: 58, Low: 63 │
│ Vulnerabilities Prevented: 3 (critical)     │
│   └─ Blocked Deployments: 3 PRs             │
│ False Positives (Dev Feedback): 24          │
│   └─ FP Rate: 16.9% (improving)             │
│ True Positives Validated: 41                │
│   └─ Validation Rate: 28.9%                 │
│ Security Incidents: 0 (🟢 TARGET MET)       │
└─────────────────────────────────────────────┘
```

**Panel 5: Threat Assessment Activity (Weekly)**
```
┌─────────────────────────────────────────────┐
│ THREAT ASSESSMENT ACTIVITY                   │
├─────────────────────────────────────────────┤
│ Threat Intelligence Reviewed: 14 sources    │
│   └─ CVEs: 8, Research: 4, Vendor: 2        │
│ Threat Scenarios Updated: 3                 │
│   └─ New Scenarios: 1, Modified: 2          │
│ Adversarial Testing: Scheduled for Feb 15   │
│   └─ Last Test: Jan 10 (95.3% detection)    │
│ High-Priority Threats: 2 open               │
│   └─ Mitigation Timeline: ≤30 days          │
└─────────────────────────────────────────────┘
```

**Panel 6: Effectiveness & ROI (Monthly)**
```
┌─────────────────────────────────────────────┐
│ EFFECTIVENESS & BUSINESS VALUE (MTD)         │
├─────────────────────────────────────────────┤
│ Vulnerabilities Fixed (via auto-remediation): 28 │
│   └─ Developer Time Saved: 112 hours        │
│ Estimated Breach Prevention Value: $380K    │
│   └─ Based on: 3 critical vulns prevented   │
│ Developer Productivity Impact: +41%         │
│   └─ Security Tasks: 2.3h → 1.4h avg        │
│ ROI (YTD): 2.4:1                            │
│   └─ Value: $1.25M / Investment: $520K      │
└─────────────────────────────────────────────┘
```

### 6.3 Practice-Specific Dashboards

**SA Practice Dashboard Focus:**
- System performance (uptime, latency, throughput)
- Model accuracy (precision, recall, F1)
- Architecture health (scalability, efficiency, resilience)
- Developer experience (adoption, satisfaction, productivity)

**TA Practice Dashboard Focus:**
- Threat coverage (scenarios documented, gaps identified)
- Threat intelligence activity (sources monitored, scenarios updated)
- Testing results (adversarial testing, red team, drift detection)
- Incident prevention (threats mitigated, zero-day response time)

---

## 7. Metrics Lifecycle

### 7.1 Baseline → Target → Measure → Improve

```
┌──────────────────────────────────────────────────────────────────┐
│                    METRICS LIFECYCLE                              │
├──────────────────────────────────────────────────────────────────┤
│                                                                   │
│  PHASE 1: BASELINE (Weeks 1-4)                                   │
│  ├─ Collect 30 days operational data                             │
│  ├─ Calculate baseline for all metrics                           │
│  ├─ Document data sources and methodology                        │
│  ├─ Validate baseline with stakeholders                          │
│  └─ Establish measurement infrastructure                         │
│                                                                   │
│  PHASE 2: TARGET SETTING (Week 5-6)                              │
│  ├─ Review industry benchmarks                                   │
│  ├─ Assess organizational capacity                               │
│  ├─ Set SMART targets (L1, L2, L3)                              │
│  ├─ Define quarterly milestones                                  │
│  └─ Gain executive approval                                      │
│                                                                   │
│  PHASE 3: MEASUREMENT (Ongoing)                                  │
│  ├─ Automated data collection (real-time, daily, weekly)         │
│  ├─ Dashboard updates (operational, executive)                   │
│  ├─ Weekly metric reviews (teams)                                │
│  ├─ Monthly metric reviews (leadership)                          │
│  └─ Quarterly maturity assessments                               │
│                                                                   │
│  PHASE 4: IMPROVEMENT (Continuous)                               │
│  ├─ Identify gaps (metrics below target)                         │
│  ├─ Root cause analysis (why metric failing)                     │
│  ├─ Implement improvements (activities, architecture, process)   │
│  ├─ Measure impact (did improvement work?)                       │
│  └─ Iterate (adjust targets, refine methodology)                 │
│                                                                   │
│  PHASE 5: GOVERNANCE (Quarterly)                                 │
│  ├─ Maturity assessment (questionnaire + metrics)                │
│  ├─ Executive reporting (business value, ROI)                    │
│  ├─ Strategy adjustment (investment, priorities)                 │
│  ├─ Benchmark comparison (industry, competitors)                 │
│  └─ Celebrate wins (team recognition, communication)             │
│                                                                   │
└──────────────────────────────────────────────────────────────────┘
```

### 7.2 Continuous Improvement Process

**Weekly Metrics Review (Operational Teams):**
1. Review operational dashboard (system health, model performance)
2. Identify any metrics trending negative (↓ arrows)
3. Triage issues (critical = immediate action, important = backlog)
4. Document actions taken and impact
5. Update stakeholders if critical metrics affected

**Monthly Metrics Review (Leadership):**
1. Review executive dashboard (outcomes, effectiveness, ROI)
2. Compare to targets (on track / at risk / off track)
3. Assess maturity progress (% toward next level)
4. Approve resource allocation adjustments
5. Communicate status to broader organization

**Quarterly Maturity Assessment:**
1. Conduct full questionnaire assessment (243 questions)
2. Validate metrics against thresholds (30-90 day data)
3. Calculate combined maturity score (60% activities + 40% metrics)
4. Identify gaps and prioritize remediation
5. Update roadmap for next quarter
6. Report to executive leadership and board

**Annual Strategic Review:**
1. Year-over-year metric comparison (progress, trends)
2. ROI validation (business value delivered)
3. Benchmark against industry (are we competitive?)
4. Strategy adjustment (new threats, technologies, priorities)
5. Investment planning (budget, headcount, tools for next year)

### 7.3 Metric Refinement

**When to Refine Metrics:**
- **Target Too Easy:** Consistently exceeding target by >20% → Raise target
- **Target Unrealistic:** Consistently missing target despite effort → Lower target or extend timeline
- **Metric No Longer Relevant:** Business context changed, metric doesn't drive value → Replace metric
- **Data Quality Issues:** Source unreliable, calculation flawed → Fix methodology or change source
- **New Technology/Threat:** Framework evolved, new capabilities available → Add new metrics

**Refinement Process:**
1. Propose metric change (document reason, impact)
2. Stakeholder review (affected teams, leadership)
3. Pilot new metric (collect 30 days data)
4. Validate new metric (does it drive desired behavior?)
5. Formally adopt (update dashboards, documentation)
6. Communicate change (teams, executives, historical data handling)

---

## Appendix A: Data Source Catalog

### SA Practice Data Sources

| **Metric** | **Primary Data Source** | **Backup Data Source** | **Collection Method** | **Update Frequency** |
|-----------|------------------------|----------------------|---------------------|-------------------|
| **System Uptime** | APM tool (Datadog, New Relic) | Cloud provider metrics (AWS CloudWatch) | Automated monitoring agent | Real-time (5 min intervals) |
| **API Latency (p95)** | API gateway logs (Kong, Nginx) | APM distributed tracing | Log aggregation + percentile calculation | Real-time (aggregated hourly) |
| **Model Accuracy (Precision/Recall)** | AI security tool analytics dashboard | Developer feedback database + ground truth validation | Automated calculation from TP/FP/TN/FN | Daily (refreshed nightly) |
| **Developer Adoption (%)** | IDE plugin telemetry + CI/CD logs | User access logs (authentication system) | Active user count / total developer count | Weekly (calculated Monday) |
| **Code Analysis Coverage (%)** | CI/CD pipeline logs + code repository metadata | Security tool reports (SonarQube, Snyk) | Analyzed files / total files in production | Daily (post-deployment) |
| **False Positive Rate** | Developer feedback system (JIRA, GitHub Issues) | Security team triage database | FP count / total findings | Weekly (human validation required) |
| **Cache Hit Rate** | Cache system metrics (Redis, Memcached) | Application logs (cache access patterns) | Cache hits / total cache requests | Real-time (aggregated hourly) |
| **Vulnerability Remediation MTTR** | Issue tracking system (JIRA, ServiceNow) | Security dashboard (vulnerability lifecycle) | Time from detection to fix deployed | Weekly (calculated per finding) |
| **ROI Calculation** | Financial system (costs) + Security dashboard (value) | Manual calculation (quarterly review) | (Breach prevention value + productivity gains) / (tool cost + labor) | Quarterly |

### TA Practice Data Sources

| **Metric** | **Primary Data Source** | **Backup Data Source** | **Collection Method** | **Update Frequency** |
|-----------|------------------------|----------------------|---------------------|-------------------|
| **Threat Scenarios Documented** | Threat model repository (Confluence, SharePoint) | Security documentation system | Count of threat scenarios per domain | Monthly (manual review) |
| **Training Completion Rate (%)** | Learning Management System (LMS) | HR training records | Completed users / assigned users | Weekly |
| **Threat Intelligence Sources Monitored** | Threat intelligence platform (TIP) | Security team tracking spreadsheet | Count of active sources | Weekly |
| **Adversarial Testing Frequency** | Security testing calendar + test reports | JIRA security testing tickets | Count of tests per quarter | Quarterly |
| **Threat Mitigation MTTR** | Risk management system + JIRA | Security dashboard (risk register) | Time from threat identification to mitigation deployed | Monthly |
| **Model Drift Detection Events** | ML monitoring platform (Evidently AI, Fiddler) | Model performance dashboard | Count of drift alerts exceeding threshold | Daily |
| **Evasion Test Success Rate** | Security testing reports | Adversarial testing database | Successful detections / total adversarial samples | Quarterly (post-testing) |
| **Incident Prevention Count** | Incident management system (ServiceNow, PagerDuty) | Correlation: Threats documented → Incidents = 0 | Count of zero incidents from documented threats | Quarterly (requires analysis) |

### Cross-Domain Data Sources

| **Data Type** | **Tool/System** | **Domains Using** | **Access Method** |
|--------------|----------------|------------------|------------------|
| **System Logs** | ELK Stack (Elasticsearch, Logstash, Kibana) | All domains | API query, dashboard |
| **Metrics & Monitoring** | Prometheus + Grafana | All domains (infrastructure, software) | PromQL queries, Grafana API |
| **Security Events** | SIEM (Splunk, Sentinel, Chronicle) | All domains | SPL queries, API |
| **Cloud Metrics** | AWS CloudWatch, Azure Monitor, GCP Cloud Monitoring | Infrastructure, Data, Software | Cloud provider API |
| **Developer Activity** | GitHub/GitLab Analytics, JIRA | Software, Processes | API, webhooks |
| **Model Performance** | MLflow, Weights & Biases | Software, Data | API, SDK |
| **Compliance Data** | GRC platform (Compliance.ai, AuditBoard) | All domains (compliance metrics) | API, reports |

---

## Appendix B: Metric Calculation Examples

### B.1 Model Accuracy (Precision & Recall)

**Definitions:**
- **Precision:** Of all vulnerabilities AI flagged, what % were actually vulnerable?
  - Formula: `Precision = TP / (TP + FP)`
  - Interpretation: Low precision = many false positives (developer frustration)
  
- **Recall:** Of all actual vulnerabilities, what % did AI detect?
  - Formula: `Recall = TP / (TP + FN)`
  - Interpretation: Low recall = missing vulnerabilities (security risk)

**Where:**
- TP (True Positive) = AI correctly identified vulnerability (validated by security team or developer)
- FP (False Positive) = AI incorrectly flagged secure code as vulnerable (developer rejected)
- TN (True Negative) = AI correctly identified secure code (no flag, code is safe)
- FN (False Negative) = AI missed actual vulnerability (discovered in production, pentesting, or incident)

**Data Collection:**
1. **Developer Feedback:** Developers mark AI findings as "True Positive" or "False Positive"
2. **Security Expert Validation:** Security team samples findings (≥100/month) for ground truth
3. **Production Incidents:** Vulnerabilities discovered post-deployment = False Negatives
4. **Penetration Testing:** External pentests find vulnerabilities AI missed = False Negatives

**Calculation Example:**

```
Month: January 2026
Total AI Findings: 450
Developer Feedback:
  - Confirmed Vulnerable (TP): 367
  - Marked False Positive (FP): 83
  - No Feedback: 0 (assumed validated via auto-merge)

Security Team Validation (Ground Truth):
  - Reviewed: 120 findings
  - Confirmed TP: 102 (85%)
  - Confirmed FP: 18 (15%)

Production Incidents (False Negatives):
  - Vulnerabilities found in production: 2 (SQL injection, XSS)
  - Root cause: New attack pattern not in training data

Calculation:
  TP = 367
  FP = 83
  FN = 2 (from production incidents)

Precision = 367 / (367 + 83) = 367 / 450 = 81.6%
Recall = 367 / (367 + 2) = 367 / 369 = 99.5%

Interpretation:
  - Precision 81.6%: BELOW L1 target (≥85%) → Too many false positives
  - Recall 99.5%: EXCEEDS L1 target (≥95%) → Good vulnerability detection
  - Action: Reduce false positives (context-aware analysis, model fine-tuning)
```

**Improving Precision (Reduce False Positives):**
- Implement contextual analysis (test files, internal APIs excluded)
- Developer feedback loop (retrain model on validated FPs)
- Severity filtering (show only Critical/High to developers)

**Improving Recall (Reduce False Negatives):**
- Expand training data (new vulnerability patterns)
- Increase model complexity (GNN, transformers for complex patterns)
- Threat intelligence integration (zero-day patterns)

### B.2 System Uptime Calculation

**Formula:**
```
Uptime % = (Total Time - Downtime) / Total Time × 100
```

**Measurement Period:** Rolling 30 days (720 hours)

**Data Source:** APM tool (Datadog, New Relic) or cloud provider health checks

**Example:**

```
Period: January 1-30, 2026 (720 hours)

Downtime Events:
  - Jan 5: 2:14 AM - 2:47 AM (33 minutes) - Database connection pool exhaustion
  - Jan 12: 11:23 PM - 11:58 PM (35 minutes) - API gateway memory leak
  - Jan 22: 3:05 PM - 3:18 PM (13 minutes) - Kubernetes node failure (auto-recovered)

Total Downtime: 33 + 35 + 13 = 81 minutes = 1.35 hours

Uptime Calculation:
  Uptime % = (720 - 1.35) / 720 × 100
  Uptime % = 718.65 / 720 × 100
  Uptime % = 99.81%

Comparison to Target:
  L1 Target: ≥99.5% uptime
  Result: 99.81% ✅ EXCEEDS target

Interpretation:
  - Uptime exceeds L1 requirement
  - Room for improvement toward L2 (≥99.95%)
  - Focus: Eliminate single points of failure (database, API gateway)
```

**Improving Uptime:**
- Multi-zone deployment (eliminate single datacenter failure)
- Database connection pool monitoring and auto-scaling
- API gateway HA configuration (≥3 replicas)
- Chaos engineering testing (proactive failure detection)

### B.3 ROI Calculation

**Formula:**
```
ROI = (Total Value Delivered - Total Investment) / Total Investment × 100%

Where:
  Total Value = Breach Prevention Value + Productivity Gains + Cost Savings
  Total Investment = Tool Costs + Labor Costs + Infrastructure Costs
```

**Example Calculation (Annual):**

```
Investment (2025):
  - AI Security Tool Licensing: $180K
  - Infrastructure (AWS, compute): $120K
  - Labor (2 ML engineers, 1 security engineer): $450K
  - Training & Onboarding: $25K
  Total Investment: $775K

Value Delivered (2025):
  
  1. Breach Prevention Value:
     - Critical vulnerabilities prevented: 18
     - Estimated breach cost per critical vuln: $500K (industry average)
     - Breach Prevention Value: 18 × $500K × 0.15 (probability) = $1.35M
  
  2. Productivity Gains:
     - Developers: 500
     - Time saved per developer per month: 4 hours (security tasks automated)
     - Hours saved per year: 500 × 4 × 12 = 24,000 hours
     - Hourly rate: $75 (average developer)
     - Productivity Value: 24,000 × $75 = $1.8M
  
  3. Cost Savings:
     - Manual security review reduction: $150K/year (security analyst time)
     - Compliance automation: $80K/year (audit preparation)
     - Cost Savings: $230K
  
  Total Value: $1.35M + $1.8M + $230K = $3.38M

ROI Calculation:
  ROI = ($3.38M - $775K) / $775K × 100%
  ROI = $2.605M / $775K × 100%
  ROI = 336% or 4.36:1

Interpretation:
  - For every $1 invested, return $4.36 in value
  - Significantly exceeds L3 target (ROI ≥3:1) ✅
  - Strong business case for continued investment
```

**ROI Improvement Strategies:**
- Increase value: Detect more vulnerabilities, expand to more teams
- Reduce cost: Infrastructure optimization, open-source alternatives
- Improve productivity: Auto-remediation (reduce developer time further)

### B.4 False Positive Rate

**Formula:**
```
False Positive Rate = FP / (FP + TP) × 100%

Where:
  FP = Findings marked as false positive by developers
  TP = Findings confirmed as true vulnerabilities
```

**Example:**

```
Month: January 2026
Total AI Findings: 450

Developer Feedback:
  - Confirmed Vulnerable (TP): 367
  - Marked False Positive (FP): 83

False Positive Rate Calculation:
  FP Rate = 83 / (83 + 367) × 100%
  FP Rate = 83 / 450 × 100%
  FP Rate = 18.4%

Comparison to Target:
  L1 Target: ≤20% FP Rate
  Result: 18.4% ✅ MEETS target (but close to threshold)

Trend Analysis (Last 3 Months):
  - November: 24.1% (ABOVE target)
  - December: 21.3% (ABOVE target)
  - January: 18.4% (MEETS target) ↓ Improving trend

Interpretation:
  - Currently meeting L1 target
  - Positive trend (↓ FP rate over time)
  - Goal: Reduce to ≤15% for improved developer experience
  - L2 Target: Context-aware reduction ≥30% → 18.4% × 0.7 = 12.9% target
```

**Reducing False Positives:**
- Context exclusions (test files, example code, documentation)
- Framework-aware analysis (understand common secure patterns in Django, React)
- Developer feedback loop (retrain model on FPs)
- Confidence thresholds (only show high-confidence findings)

---

## Conclusion

The HAIAMM Unified Metrics Framework provides a comprehensive, outcome-focused measurement system for Security Architecture (SA) and Threat Assessment (TA) practices across all 6 domains (Software, Data, Infrastructure, Vendors, Processes, Endpoints) and 3 maturity levels.

**Key Principles:**
1. **Outcome Over Output:** Focus on security results, not just activities
2. **Leading + Lagging:** Balance predictive (process) and retrospective (outcome) metrics
3. **Business Value:** Demonstrate ROI and effectiveness, not just technical achievement
4. **Data-Driven:** Automated, objective, auditable measurement
5. **Continuous Improvement:** Baseline → Target → Measure → Improve lifecycle

**Usage:**
- **Practitioners:** Use metric tables (Section 2-3) for target setting and dashboards (Section 6)
- **Assessors:** Integrate metrics validation (Section 5) with questionnaire assessments
- **Leadership:** Review executive dashboards (Section 6.1) for strategic decision-making
- **Auditors:** Reference data sources (Appendix A) and calculations (Appendix B) for verification

**Next Steps:**
1. Establish baselines for your organization (Section 4.1)
2. Set realistic targets based on maturity progression (Section 4.2)
3. Implement dashboards (Section 6) for visibility
4. Conduct quarterly maturity assessments (Section 5)
5. Iterate and improve continuously (Section 7)

This framework evolves with the HAIAMM model. Feedback and contributions welcome via HAIAMM project repository.

---

**Document Version:** 2.0  
**Publication Date:** 2026-02-11  
**License:** CC BY 4.0  
**Contact:** HAIAMM Project Team

---