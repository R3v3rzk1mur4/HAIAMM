# Monitoring & Logging (ML) - Software Domain
## HAIAMM Assessment Questionnaire v2.0

**Practice:** Monitoring & Logging (ML)
**Domain:** Software
**Purpose:** Assess organizational maturity in monitoring and logging for Human Assisted Intelligence software security systems

---

## Instructions

- Answer each question honestly based on **current, implemented practices** (not plans or aspirations)
- **"Yes" requires evidence** - Document proof for each affirmative answer
- **Answer progressively** - Complete all Level 1 questions before Level 2
- **Level progression** - Achieve ALL questions at lower level before advancing
- **Partial implementation = "No"** - Practice must be complete and systematic

---

## Level 1: Foundational
**Objective:** Establish comprehensive logging and monitoring across all HAI system components

### Question 1: Comprehensive Security and AI Model Logging

**Q1.1:** Do you implement comprehensive security event logging (authentication, authorization, API security, attack detection) and AI model logging (inference requests, performance metrics, model drift detection) with structured log formats?

**Evidence Required:**
- [ ] Security event logging implemented:
  - Authentication events (login success/failure, session management, privilege escalation)
  - Authorization events (access allowed/denied with context)
  - API security events (input validation failures, rate limiting, suspicious requests)
  - Attack detection (injection attempts, brute force, vulnerability exploitation)
- [ ] AI model logging implemented:
  - Inference requests logged (privacy-preserving, no sensitive data)
  - Model performance metrics tracked (precision ≥90%, recall ≥85%, false positive rate ≤5%)
  - Model drift detection enabled (data drift, concept drift, accuracy degradation alerts)
  - Model training and deployment logged (versions, parameters, validation results)
- [ ] Structured logging format used (JSON or equivalent) for ≥90% of logs
- [ ] Logging coverage: 100% of services/components emit logs

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

### Question 2: Centralized Log Aggregation and SIEM Integration

**Q1.2:** Do you aggregate all logs to a centralized SIEM platform with real-time security monitoring, correlation rules, and alerting capabilities that detect security incidents within 5 minutes?

**Evidence Required:**
- [ ] Centralized SIEM platform deployed (Splunk, ELK Stack, Sumo Logic, Azure Sentinel, or equivalent)
- [ ] Log collection agents deployed on ≥95% of infrastructure (servers, containers, applications)
- [ ] Log delivery metrics:
  - ≥99% log completeness (logs successfully delivered to SIEM)
  - ≥95% logs ingested within ≤60 seconds
- [ ] Security monitoring and alerting implemented:
  - Real-time correlation rules for multi-stage attacks
  - Alert triage by severity (Critical/High/Medium/Low)
  - Alert routing to appropriate teams (on-call paging for Critical/High)
  - ≥90% of attacks detected within ≤5 minutes
  - ≤5% false positive rate for security alerts
- [ ] Threat intelligence integration (IOC monitoring, IP blacklists, CVE matching)

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

### Question 3: Compliance Audit Logging and Retention

**Q1.3:** Do you maintain comprehensive audit logs for compliance requirements (data access, configuration changes, administrative actions) with appropriate retention policies and log integrity protection?

**Evidence Required:**
- [ ] Compliance audit logging implemented:
  - Data access logging (all access to PII, PHI, financial data with user/timestamp/action)
  - Configuration change logging (security settings, access policies, encryption keys)
  - Administrative action logging (user management, role assignment, policy changes)
- [ ] Regulatory compliance coverage (if applicable):
  - GDPR: Consent, SARs, data deletion, cross-border transfers (≥3 year retention)
  - HIPAA: PHI access, modifications, security incidents (≥6 year retention)
  - PCI-DSS: Cardholder data access, authentication, admin actions (≥1 year retention)
- [ ] Log retention policies documented and enforced:
  - Security logs: ≥90 days hot (SIEM), ≥1 year cold (archive)
  - Compliance logs: Per regulatory requirements
- [ ] Log integrity protection implemented:
  - Write-once storage, log signing, or immutable storage
  - Restricted log deletion access
  - Periodic integrity validation
- [ ] 100% compliance coverage for required events

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

**Level 1 Score:** _____ / 3 questions answered "Yes"

**Level 1 Achieved:** ☐ Yes (3/3) ☐ No (< 3/3)

---

## Level 2: Comprehensive
**Objective:** Implement advanced observability with distributed tracing, user behavior analytics, and predictive monitoring

**Prerequisites:** ALL Level 1 questions must be "Yes" to proceed to Level 2

### Question 4: Distributed Tracing and User Behavior Analytics

**Q2.1:** Do you implement distributed tracing across microservices using correlation IDs to trace requests end-to-end, and deploy user behavior analytics to detect insider threats and account compromise?

**Evidence Required:**
- [ ] Distributed tracing implemented:
  - Correlation IDs (request IDs) generated at entry point and propagated through all services
  - Trace visualization showing request path across services
  - Latency breakdown per service/component
  - Coverage: ≥90% of microservices instrumented
  - Tools: OpenTelemetry, Jaeger, Zipkin, AWS X-Ray, or equivalent
- [ ] User behavior analytics (UBA) deployed:
  - Behavioral baselines established for normal user activity
  - Anomaly detection for unusual patterns (login locations, data access, API usage)
  - Insider threat detection (excessive data access, privilege abuse, off-hours activity)
  - Account compromise detection (credential stuffing, session hijacking indicators)
  - Integration with SIEM for automated alerting
- [ ] Mean time to investigate (MTTI) ≤30 minutes for critical alerts
- [ ] Evidence of UBA detecting real security incidents

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

### Question 5: Advanced Anomaly Detection and Synthetic Monitoring

**Q2.2:** Do you deploy ML-based anomaly detection with behavioral baselines for security and performance, and implement synthetic monitoring with proactive health checks to detect issues before user impact?

**Evidence Required:**
- [ ] ML-based anomaly detection implemented:
  - Statistical or ML models for behavioral baselines
  - Anomaly detection for: API usage patterns, resource consumption, security events, model performance
  - Automated alerts on significant deviations (configurable thresholds)
  - Evidence of detecting previously unknown issues
  - Integration with incident response workflows
- [ ] Synthetic monitoring program:
  - Proactive health checks for critical user journeys
  - Simulated transactions testing end-to-end functionality
  - Monitoring frequency: ≤5 minute intervals for critical paths
  - Coverage: All critical user workflows monitored
  - Alerts on synthetic test failures before user reports
- [ ] Anomaly detection accuracy: ≥80% true positive rate
- [ ] Synthetic monitoring detects ≥70% of issues before user impact

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

### Question 6: Predictive Analytics and Proactive Capacity Planning

**Q2.3:** Do you use predictive analytics to forecast system failures, capacity constraints, and performance degradation before they occur, with documented evidence of proactive issue prevention?

**Evidence Required:**
- [ ] Predictive analytics capabilities implemented:
  - Time-series forecasting for resource utilization (CPU, memory, disk, network)
  - Capacity planning models (predict when resources will be exhausted)
  - Performance degradation prediction (latency trends, error rate trends)
  - Model drift prediction (forecast when AI model retraining needed)
- [ ] Predictive alerts configured:
  - Alert on predicted resource exhaustion (e.g., "disk full in 7 days")
  - Alert on predicted performance degradation
  - Alert on predicted model accuracy drop
- [ ] Proactive actions documented:
  - Evidence of capacity additions before exhaustion
  - Evidence of performance optimizations before user impact
  - Evidence of model retraining before accuracy drops
- [ ] Historical tracking (≥6 months) showing prediction accuracy
- [ ] ≥60% of capacity/performance issues prevented proactively

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

**Level 2 Score:** _____ / 3 questions answered "Yes"

**Level 2 Achieved:** ☐ Yes (3/3) ☐ No (< 3/3)

---

## Level 3: Industry-Leading
**Objective:** Achieve AI-powered observability, continuous compliance validation, and public transparency

**Prerequisites:** ALL Level 2 questions must be "Yes" to proceed to Level 3

### Question 7: AI-Powered Incident Detection and Triage

**Q3.1:** Do you deploy AI systems that automatically analyze logs, detect security incidents, perform root cause analysis, and auto-triage incidents with severity classification, demonstrably reducing mean time to detect (MTTD) and mean time to investigate (MTTI)?

**Evidence Required:**
- [ ] AI-powered incident detection system deployed:
  - AI analyzes logs in real-time for security incidents
  - Automated pattern recognition for attack techniques
  - Automated correlation of multi-stage attacks
  - Root cause analysis automation (identifies initial attack vector, blast radius)
- [ ] AI-powered auto-triage capabilities:
  - Automated severity classification (Critical/High/Medium/Low)
  - Automated incident categorization (type of attack, affected systems)
  - Automated incident enrichment (threat intel, asset context, user risk)
  - Recommended response actions provided
- [ ] Measurable improvements documented:
  - MTTD reduction ≥50% compared to manual detection
  - MTTI reduction ≥40% compared to manual investigation
  - ≥80% of incidents correctly triaged by AI
  - Evidence of AI catching incidents missed by rule-based detection
- [ ] Human oversight maintained for high-severity incidents

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

### Question 8: Continuous Compliance Validation and Open Telemetry Contribution

**Q3.2:** Do you implement continuous, real-time compliance monitoring that validates regulatory requirements automatically, and contribute to open-source observability standards (OpenTelemetry, observability frameworks) with documented industry impact?

**Evidence Required:**
- [ ] Continuous compliance validation system:
  - Real-time monitoring of compliance controls (GDPR, HIPAA, PCI-DSS, SOC 2)
  - Automated validation of compliance requirements (data retention, access controls, encryption)
  - Automated compliance reporting (live compliance dashboards)
  - Automated alerts on compliance violations
  - Evidence of compliance drift detection and remediation
- [ ] Open telemetry contributions (at least 2 per year):
  - Contributions to OpenTelemetry project (code, documentation, standards)
  - Open-source observability tools or frameworks published
  - Public talks/blog posts on observability best practices
  - Participation in observability standards bodies (CNCF, W3C Distributed Tracing)
- [ ] Public evidence (GitHub repositories, conference presentations, published articles)
- [ ] Documented industry adoption or impact (downloads, citations, implementations)

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

### Question 9: Public Transparency Reports and Chaos Engineering Observability

**Q3.3:** Do you publish annual public transparency reports with security and incident metrics, and conduct chaos engineering experiments with observability validation to ensure monitoring catches injected failures?

**Evidence Required:**
- [ ] Public transparency reports published (at least annually):
  - Security incident statistics (types, frequency, MTTD/MTTR)
  - Availability metrics (uptime, performance, SLA adherence)
  - Compliance posture (audit results, certifications)
  - AI model performance metrics (accuracy, drift, retraining frequency)
  - Demonstrates commitment to transparency and accountability
- [ ] Chaos engineering program with observability validation:
  - Scheduled chaos experiments (service failures, network issues, resource exhaustion)
  - Validation that monitoring detects injected failures
  - Validation that alerts fire correctly
  - Validation that runbooks and incident response work
  - Experiments run at least quarterly
- [ ] Chaos engineering results documented:
  - ≥95% of injected failures detected by monitoring
  - ≥90% of failures trigger appropriate alerts
  - Mean detection time for chaos failures ≤5 minutes
- [ ] Public evidence (transparency report URL, chaos engineering blog posts)

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

**ML-Software Practice Score:** _______ / 3.0

### Precise Scoring (For Formal Audits)

```
L1_score = (L1 "Yes" answers) / 3
L2_score = (L2 "Yes" answers) / 3 × L1_score
L3_score = (L3 "Yes" answers) / 3 × L2_score

Practice Score = L1_score + L2_score + L3_score
```

**ML-Software Practice Score (Precise):** _______ / 3.0

---

## Assessment Summary

**Assessment Date:** _________________________________

**Assessor(s):** _____________________________________

**HAI System(s) Assessed:** __________________________

**Overall Maturity Level:**
- ☐ Level 0 (Score < 1.0): Ad-hoc, minimal logging and monitoring
- ☐ Level 1 (Score 1.0 - 1.9): Comprehensive logging, SIEM integration, compliance
- ☐ Level 2 (Score 2.0 - 2.9): Advanced observability with distributed tracing and predictive analytics
- ☐ Level 3 (Score 3.0): AI-powered observability and public transparency

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

## Monitoring & Logging Specific Notes

**Logging Categories Covered:**
- [ ] Security event logging (authentication, authorization, attacks)
- [ ] AI model logging (inference, performance, drift)
- [ ] System performance monitoring (latency, throughput, errors)
- [ ] Compliance audit logging (data access, configuration changes, admin actions)
- [ ] Application performance monitoring (APM)

**SIEM and Observability Tools:**
- [ ] SIEM platform deployed (Splunk, ELK, Sumo Logic, Azure Sentinel)
- [ ] APM tools deployed (Datadog, New Relic, Dynatrace, Prometheus+Grafana)
- [ ] Distributed tracing (OpenTelemetry, Jaeger, Zipkin, AWS X-Ray)
- [ ] Log aggregation (Fluentd, Filebeat, Logstash, CloudWatch)

**Key Metrics Tracked:**
- [ ] Logging coverage (100% of services)
- [ ] Log completeness (≥99% delivery to SIEM)
- [ ] Log latency (≥95% within ≤60 seconds)
- [ ] Alert quality (≤5% false positive rate)
- [ ] Detection time (≥90% attacks within ≤5 minutes)
- [ ] Investigation time (MTTI ≤30 minutes for critical)

---

**Document Version:** 2.0
**Last Updated:** 2025-12-29
**Next Review:** Quarterly or after significant HAI system changes
