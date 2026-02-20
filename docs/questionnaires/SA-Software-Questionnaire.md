# Secure Architecture (SA) - Software Domain
## HAIAMM Assessment Questionnaire v3.0

**Practice:** Secure Architecture (SA)
**Domain:** Software
**Version:** v3.0
**Purpose:** Assess organizational maturity in architectural design for Human Assisted Intelligence systems
**Scoring Model:** Evidence + Outcome Metrics (see Scoring Methodology below)

---

## Instructions

- Answer each question honestly based on **current, implemented practices** (not plans or aspirations)
- **"Yes" requires evidence** - Document proof for each affirmative answer
- **Answer progressively** - Complete all Level 1 questions before Level 2
- **Level progression** - Achieve ALL questions at lower level before advancing
- **Partial implementation = "Partial"** - Practice must be complete and systematic for full credit
- Each question has two components: **Evidence** (what you did) and **Outcome Metrics** (how well it worked)
- **Scoring uses 4 tiers:** Fully Mature (1.0), Implemented (0.67), Partial (0.33), Not Implemented (0.0)
- **Baseline first** - Record current metric values before setting targets

---

## Level 1: Foundational
**Objective:** Establish foundational architecture for AI code security systems with model design, data management, developer workflow integration, and operational infrastructure

### Question 1: AI Model and Data Architecture Foundations

**Q1.1:** Have you designed and deployed AI model architecture (hybrid approach combining rule-based, ML, and deep learning models with explainability) and data architecture for training data management, code repository integration, vulnerability knowledge bases, and feedback loops?

**Evidence Required:**
- [ ] AI Model Architecture designed and implemented:
  - Hybrid Architecture: Rule-Based Static Analysis + Machine Learning + Deep Learning (if applicable)
  - Multi-Stage Pipeline (Fast Filtering → ML Classification → Deep Analysis for complex findings)
  - Model Specialization (language-specific or vulnerability-specific models)
  - Explainability Architecture (LIME, SHAP, or code-specific explanations highlighting vulnerable lines)
  - Model Versioning & Management (model registry with versions, metadata, deployment support)
- [ ] Data Architecture implemented:
  - Training Data: Curated vulnerability dataset (≥10,000 labeled examples per major vulnerability class)
  - Code Repository Integration: Connector to ≥95% of organization's code repositories (GitHub, GitLab, Bitbucket, etc.)
  - Incremental Analysis (analyze only changed code, ≥10x faster than full scans)
  - Vulnerability Knowledge Base (structured database of vulnerability patterns, remediation guidance)
  - Feedback Data Collection (capture developer feedback from IDE, code review, CI/CD, dashboard)
  - Data Privacy & Security (code encrypted at rest/in transit, strict access controls, RBAC)
- [ ] Architecture documentation (architectural diagrams, design decisions, technology choices)
- [ ] Architecture reviewed and approved by security and engineering leadership

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Model precision (% of flagged findings that are true positives) | ___ | ___ | ≥85% | ☐ | |
| Model recall (% of actual vulnerabilities detected) | ___ | ___ | ≥95% | ☐ | |
| Code repository integration coverage (% of repos connected) | ___ | ___ | ≥95% | ☐ | |
| Training dataset size per major vulnerability class (labeled examples) | ___ | ___ | ≥10,000 | ☐ | |

**Metric Collection Guidance:**
- **Model precision**: Collect from security dashboard; formula = True Positives / (True Positives + False Positives) computed monthly from validated developer feedback and expert review
- **Model recall**: Collect from security audits and production incident retrospectives; formula = True Positives / (True Positives + False Negatives); validate via quarterly red-team exercises
- **Repository integration coverage**: Pull from repository connector admin dashboard; formula = Connected Repos / Total Known Repos; report monthly
- **Training dataset size**: Export count from model registry or training data catalog; count labeled examples per vulnerability class (SQL injection, XSS, auth flaws, crypto, etc.)

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### Question 2: Developer Workflow Integration and Infrastructure Deployment

**Q1.2:** Have you implemented integration architecture that embeds AI security seamlessly into developer workflows (IDE, CI/CD, code review platforms with ≤3 second latency for IDE, <10% build time impact for CI/CD), and deployed scalable infrastructure architecture (cloud-native or on-premise with ≥99.5% uptime, horizontal scaling, high availability)?

**Evidence Required:**
- [ ] Developer Workflow Integration implemented:
  - IDE Integration: Real-time analysis with results displayed within ≤3 seconds
  - Supported IDEs covering ≥70% of developers (VS Code, IntelliJ IDEA, PyCharm, etc.)
  - CI/CD Pipeline Integration: PR analysis, build-time analysis with <10% build time impact
  - Code Review Platform Integration: AI posts findings as PR comments (GitHub, GitLab, Bitbucket)
  - API Architecture: RESTful API for custom integrations (authentication, rate limiting)
- [ ] Infrastructure Architecture deployed:
  - Deployment Model: Cloud-Native (Kubernetes) or On-Premise (Docker Swarm/VMware)
  - Scalability: Horizontal scaling with auto-scaling (support ≥1,000 concurrent analysis requests)
  - Analysis Queue Architecture (message queue: RabbitMQ, SQS, Kafka for decoupling)
  - High Availability: Multi-instance deployment with ≥99.5% uptime target
  - Load Balancing: Application load balancer distributing requests across instances
  - Disaster Recovery: Backup strategy with RTO ≤4 hours, RPO ≤24 hours
- [ ] Performance Architecture:
  - Caching Strategy (result caching for unchanged code, ≥60% cache hit rate target)
  - Database Architecture (findings database: PostgreSQL/MongoDB, time-series DB for metrics)
  - Model Serving Architecture (model server or embedded models)
- [ ] Infrastructure monitoring and alerting configured

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| IDE analysis latency p95 (seconds from code change to result display) | ___ | ___ | ≤3 seconds | ☐ | |
| CI/CD build time overhead added by security scan (%) | ___ | ___ | <10% | ☐ | |
| System uptime (monthly availability %) | ___ | ___ | ≥99.5% | ☐ | |
| Result cache hit rate (% of analysis requests served from cache) | ___ | ___ | ≥60% | ☐ | |

**Metric Collection Guidance:**
- **IDE latency p95**: Instrument IDE plugin with telemetry; collect timestamps from code change event to result display; compute 95th percentile monthly from plugin analytics or APM tool (Datadog, New Relic)
- **CI/CD build time overhead**: Compare average build time with and without security scan step; formula = (Build Time With Scan - Build Time Without Scan) / Build Time Without Scan x 100; pull from CI/CD pipeline analytics (GitHub Actions, Jenkins) monthly
- **System uptime**: Calculate from monitoring tool (Prometheus, Datadog); formula = (Total Minutes - Downtime Minutes) / Total Minutes x 100; report monthly from SLO dashboard
- **Cache hit rate**: Pull from Redis/Memcached metrics dashboard; formula = Cache Hits / (Cache Hits + Cache Misses) x 100; report daily, average monthly

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### Question 3: Security Architecture and Feedback Loop Implementation

**Q1.3:** Have you implemented security architecture protecting AI systems from adversarial attacks (model protection, training data security, credential management, API security, network segmentation, audit logging), and established feedback loop architecture enabling continuous AI improvement from developer input and production validation?

**Evidence Required:**
- [ ] Security Architecture for AI Systems implemented:
  - Model Security: Models encrypted at rest/in transit, strict access controls, versioning with cryptographic signatures
  - Adversarial Attack Defense: Input validation, anomaly detection, rate limiting
  - Training Data Security: Data provenance tracking, integrity (cryptographic hashing), poisoning attack prevention
  - Credential & Secrets Management: Secrets manager (Vault, AWS Secrets Manager), no hardcoded credentials, automated rotation (≥every 90 days)
  - API Security: Authentication (OAuth 2.0, API keys), authorization (RBAC), input validation, rate limiting
  - Network Security: AI services in dedicated VPC/subnet, firewall rules, TLS 1.3 for all communications
  - Audit & Logging: All API requests, analysis executions, model predictions, feedback logged with ≥1 year retention
- [ ] Feedback Loop & Continuous Improvement Architecture:
  - Multi-Channel Feedback Collection (IDE plugin, code review, security dashboard, API)
  - Feedback Validation: Tiered validation (developer feedback + security expert review + production incidents)
  - Automated Retraining Pipeline: Triggered monthly or when ≥1,000 validated feedback samples accumulated
  - A/B Testing Architecture: Deploy new model alongside old, traffic splitting, performance comparison, gradual rollout
  - Performance Tracking Dashboard: Metrics (precision, recall, F1 score, false positive rate, developer satisfaction)
- [ ] Monitoring & Observability Architecture:
  - System Health Monitoring (infrastructure metrics, application metrics, SLOs)
  - AI Model Performance Monitoring (accuracy metrics, prediction distribution, model drift detection)
  - Security Outcome Monitoring (vulnerability detection metrics, remediation tracking)
- [ ] Evidence of operational security (logs, monitoring dashboards, security reviews)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Developer feedback volume (validated feedback submissions per month) | ___ | ___ | ≥100/month | ☐ | |
| False positive rate (% of findings marked as false positive by developers) | ___ | ___ | ≤20% | ☐ | |
| Credential rotation compliance (% of AI service credentials rotated on schedule) | ___ | ___ | 100% | ☐ | |
| Security incidents involving AI system compromise (count in trailing 12 months) | ___ | ___ | 0 | ☐ | |

**Metric Collection Guidance:**
- **Developer feedback volume**: Count from feedback database or ticketing system; formula = COUNT(feedback records) per calendar month where feedback_type IN ('false_positive', 'confirmed', 'severity_adjustment'); report monthly
- **False positive rate**: Pull from security dashboard findings data; formula = Findings marked 'false_positive' / Total Findings Reviewed x 100; compute monthly from triaged findings
- **Credential rotation compliance**: Query secrets manager audit log or credential rotation scheduler; formula = Credentials Rotated On Time / Total Credentials x 100; report monthly
- **AI security incidents**: Count from incident management system (PagerDuty, Jira) tagged with AI system component; report quarterly with trailing 12-month count

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

**Level 1 Score:** _____ / 3.0 (sum of question scores)

**Level 1 Achieved:** [ ] Yes (all questions ≥0.67) [ ] No

---

## Level 2: Comprehensive
**Objective:** Implement comprehensive architecture with ensemble learning, real-time adaptation, distributed processing at enterprise scale, and advanced developer experience

**Prerequisites:** ALL Level 1 questions must score ≥0.67 to proceed to Level 2

### Question 4: Ensemble Learning and Real-Time Model Adaptation

**Q2.1:** Have you implemented ensemble learning architecture combining multiple specialist models (language-specific or vulnerability-specific with meta-model orchestration) and real-time learning architecture enabling continuous model improvement without full retraining, achieving ≥92% precision and ≥97% recall?

**Evidence Required:**
- [ ] Ensemble Learning Architecture implemented:
  - Multiple specialist models deployed (5-10 models)
  - Specialization strategy (language-specific: Java/Python/JavaScript, OR vulnerability-specific: injection/auth/crypto)
  - Meta-model or orchestration layer (combines specialist outputs, confidence weighting)
  - Ensemble performance: Achieves ≥10% higher accuracy than any single specialist model
  - Accuracy metrics: ≥92% precision, ≥97% recall (improvement from Level 1: ≥85%/≥95%)
- [ ] Real-Time Learning Architecture:
  - Continuous Learning: Model adapts incrementally from feedback without full retraining
  - Active Learning: Intelligently selects most informative samples for human labeling (achieves ≥3x faster improvement vs random sampling)
  - Automated Model Updates: New feedback incorporated into training, model updated, validated, deployed
  - Performance Improvement: Model accuracy improves ≥2% per month through continuous learning
- [ ] Model Quality Assurance:
  - Automated validation against validation set before deployment
  - Rollback capability if new model performs worse
  - Historical tracking showing sustained accuracy improvement (≥6 months)
- [ ] Evidence of ensemble and real-time learning effectiveness (metrics dashboards, performance reports)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Ensemble model precision (% true positives among all flagged findings) | ___ | ___ | ≥92% | ☐ | |
| Ensemble lift over best single model (% accuracy improvement) | ___ | ___ | ≥10% | ☐ | |
| Monthly model accuracy improvement via continuous learning (%) | ___ | ___ | ≥2%/month | ☐ | |
| Active learning efficiency vs random sampling (multiplier) | ___ | ___ | ≥3x | ☐ | |

**Metric Collection Guidance:**
- **Ensemble precision**: Pull from model monitoring dashboard; compute monthly from validated ground truth labels; formula = True Positives / (True Positives + False Positives); compare ensemble to each specialist individually
- **Ensemble lift**: Compare ensemble accuracy score to best-performing individual specialist model in A/B test; formula = (Ensemble Accuracy - Best Specialist Accuracy) / Best Specialist Accuracy x 100; evaluate quarterly
- **Monthly accuracy improvement**: Track precision/recall on held-out validation set month-over-month; formula = (Current Month Accuracy - Prior Month Accuracy); chart in model performance dashboard
- **Active learning efficiency**: Run controlled experiment comparing active-selected vs randomly-selected labeling batches; formula = Accuracy Gain Per Label (Active) / Accuracy Gain Per Label (Random); evaluate semi-annually

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### Question 5: Distributed Architecture at Enterprise Scale

**Q2.2:** Have you implemented distributed analysis architecture at enterprise scale supporting ≥10 million lines of code with ≤5 second average latency, using worker pools, model replication, distributed caching (≥70% hit rate), and database sharding?

**Evidence Required:**
- [ ] Distributed Analysis Architecture deployed:
  - Worker Pool Architecture: Horizontal scaling with ≥10-100 worker instances
  - Load balancing across workers (queue-based or load balancer)
  - Parallel analysis (multiple files analyzed simultaneously)
  - Scale Achievement: Successfully analyzes ≥10 million lines of code
  - Latency Performance: ≤5 second average latency for analysis requests
  - Parallel Efficiency: ≥80% (near-linear scaling with worker count)
- [ ] Model Replication & Sharding:
  - Model Replication: Each worker has model replica (avoids contention)
  - Model Sharding (if very large models): Split models across multiple servers
- [ ] Distributed Caching Architecture:
  - Distributed Cache: Redis Cluster or Memcached for shared caching
  - Hierarchical Caching: L1 (local worker memory) + L2 (distributed cache) + L3 (database)
  - Cache Hit Rate: ≥70% achieved
  - Cache invalidation on file changes or model updates
- [ ] Database Sharding Architecture:
  - Horizontal sharding by repository or organization
  - Distributes load across multiple database instances
- [ ] Service Mesh (optional): Istio or Linkerd for microservice communication management
- [ ] Performance metrics demonstrating scale achievement (load testing reports, production metrics)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Maximum lines of code analyzed in a single day (millions of LOC) | ___ | ___ | ≥10M LOC | ☐ | |
| Average analysis request latency at peak load (seconds) | ___ | ___ | ≤5 seconds | ☐ | |
| Distributed cache hit rate (%) | ___ | ___ | ≥70% | ☐ | |
| Parallel processing efficiency (% of linear scaling achieved) | ___ | ___ | ≥80% | ☐ | |

**Metric Collection Guidance:**
- **Max daily LOC analyzed**: Aggregate from analysis job logs or metrics pipeline; formula = SUM(lines_analyzed) per calendar day; pull from findings database or telemetry; report peak day per month
- **Average latency at peak load**: Capture from APM tool or distributed tracing (Jaeger, Zipkin) during peak hours; formula = mean(request_duration_ms) during top-10% traffic periods; report monthly
- **Distributed cache hit rate**: Pull from Redis Cluster metrics (redis-cli INFO stats: keyspace_hits, keyspace_misses); formula = hits / (hits + misses) x 100; report daily average monthly
- **Parallel efficiency**: Load test with N workers vs 2N workers; formula = (Throughput_2N / Throughput_N) / 2 x 100; run quarterly load tests and document

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### Question 6: Advanced Developer Experience and Automated Remediation

**Q2.3:** Have you implemented advanced developer experience features including automated code remediation (AI generates and validates fixes with ≥60% developer adoption), contextual security guidance reducing false positives by ≥30%, and proactive security assistance, achieving ≥85% developer satisfaction?

**Evidence Required:**
- [ ] Automated Code Remediation Architecture:
  - Fix Generation Pipeline: Vulnerability detection → Fix generation → Fix validation → Fix presentation
  - Fix Generation Techniques: Template-based, example-based, or generative AI (Codex, CodeT5)
  - Automated testing validates generated fixes don't break functionality
  - Multiple candidate fixes presented with confidence scores
  - Developer Adoption: ≥60% of vulnerabilities fixed using AI-suggested remediation
- [ ] Contextual Security Guidance:
  - Context-Aware Analysis: Tailored based on application type, framework, risk profile
  - Application Type Detection: Automatically detects web app, API, mobile app, library, CLI
  - Framework Detection: Detects frameworks in use (Spring, Django, React, etc.)
  - Smart Suppression: Context-based false positive reduction (e.g., suppress hardcoded credentials in test files)
  - False Positive Reduction: Contextual analysis reduces false positive rate by ≥30% vs context-free analysis
- [ ] Proactive Security Assistance:
  - Security Co-Pilot: AI provides proactive security guidance during development
  - Real-time suggestions as developers write security-sensitive code (authentication, crypto, input handling)
  - Security best practice knowledge base integrated
- [ ] Automated PR Security Reports:
  - AI generates comprehensive security report for each pull request
  - Markdown report posted as PR comment with vulnerability summary, risk assessment, recommended actions
- [ ] Developer Satisfaction:
  - Quarterly developer surveys showing ≥85% satisfaction score
  - Developers rate AI tools as helpful (not hindering productivity)
- [ ] Evidence of advanced features in use (metrics, developer feedback, adoption rates)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| AI-suggested remediation adoption rate (% of vulnerabilities fixed using AI fix) | ___ | ___ | ≥60% | ☐ | |
| False positive rate reduction from contextual analysis (% improvement vs context-free) | ___ | ___ | ≥30% reduction | ☐ | |
| Developer satisfaction score (quarterly survey, 0-100 scale) | ___ | ___ | ≥85 | ☐ | |
| IDE coverage (% of developers with AI security plugin actively installed and used) | ___ | ___ | ≥70% | ☐ | |

**Metric Collection Guidance:**
- **Remediation adoption rate**: Track in findings management system; formula = Findings fixed using AI-suggested fix / Total Findings Fixed x 100; pull from remediation workflow audit log monthly
- **False positive reduction**: A/B test context-aware vs context-free analysis on same codebase; formula = (FP Rate Context-Free - FP Rate Context-Aware) / FP Rate Context-Free x 100; evaluate quarterly
- **Developer satisfaction score**: Run quarterly survey (SurveyMonkey, Google Forms, or internal tool); ask "How satisfied are you with the AI security tools?" on 0-100 scale; compute mean score; report quarterly
- **IDE coverage**: Pull from IDE plugin telemetry or developer tooling management (Toolbox, MDM); formula = Active Plugin Users (activity in last 30 days) / Total Developers x 100; report monthly

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

**Level 2 Score:** _____ / 3.0 (sum of question scores)

**Level 2 Achieved:** [ ] Yes (all questions ≥0.67) [ ] No

---

## Level 3: Industry-Leading
**Objective:** Achieve industry-leading architecture with self-healing systems, zero-trust security, multi-cloud resilience, AIOps, and open-source contributions

**Prerequisites:** ALL Level 2 questions must score ≥0.67 to proceed to Level 3

### Question 7: Self-Healing Architecture and AIOps Integration

**Q3.1:** Have you implemented self-healing architecture that automatically maintains optimal performance (auto-scaling based on ML predictions, automatic model rollback on performance degradation, self-optimizing resource allocation) and integrated AI-powered operations (AIOps) for anomaly detection, predictive incident prevention, and automated root cause analysis?

**Evidence Required:**
- [ ] Self-Healing Architecture implemented:
  - Automated Detection & Remediation of architecture issues
  - Auto-Scaling based on ML predictions (predictive scaling before load increases)
  - Automatic Model Rollback: Continuous accuracy monitoring, automatic rollback on performance degradation ≥5%
  - Self-Optimizing Resource Allocation: AI adjusts resource allocation based on workload patterns
  - Automated recovery from common failures (service restarts, replica scaling, cache warming)
  - Evidence of self-healing actions (incident logs showing automatic remediation)
- [ ] AIOps Integration:
  - AI Monitoring AI: Anomaly detection on AI system metrics (latency, accuracy, error rates)
  - Predictive Incident Prevention: ML models predict potential incidents before they occur
  - Automated Root Cause Analysis: AI analyzes incidents and identifies root causes automatically
  - Intelligent Alerting: ML-based alert prioritization and noise reduction
  - Automated Remediation Recommendations: AIOps suggests or applies remediation actions
- [ ] Observability Platform:
  - Comprehensive observability (distributed tracing, centralized logging, metrics, dashboards)
  - AI-powered insights into system behavior
  - Real-time anomaly detection and alerting
- [ ] Historical tracking showing self-healing effectiveness (≥12 months of incident data, resolution times, automation rates)
- [ ] Documented reduction in manual interventions (≥50% reduction in manual incident response)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Reduction in manual incident response actions (% vs 12-month prior baseline) | ___ | ___ | ≥50% reduction | ☐ | |
| Predictive scaling accuracy (% of load spikes handled proactively before capacity breach) | ___ | ___ | ≥80% | ☐ | |
| Mean time to self-heal (minutes from anomaly detection to automated resolution) | ___ | ___ | ≤10 minutes | ☐ | |
| AIOps alert noise reduction (% reduction in actionable alert volume vs pre-AIOps baseline) | ___ | ___ | ≥50% reduction | ☐ | |

**Metric Collection Guidance:**
- **Manual incident response reduction**: Compare incident tickets requiring human action this year vs same period prior year; formula = (Prior Year Manual Incidents - Current Year Manual Incidents) / Prior Year Manual Incidents x 100; pull from PagerDuty or incident management system; report annually
- **Predictive scaling accuracy**: Track from Kubernetes HPA or auto-scaling logs; formula = Load Spikes With Proactive Scale-Out / Total Load Spikes x 100; a spike is "proactively handled" if capacity was available before queue depth exceeded threshold; report monthly
- **Mean time to self-heal**: Measure from anomaly detection timestamp to remediation verified timestamp in incident logs; formula = MEAN(remediation_time - detection_time) for auto-resolved incidents; report monthly from AIOps platform
- **Alert noise reduction**: Compare alert volume pre-AIOps vs current; formula = (Baseline Alert Volume - Current Alert Volume) / Baseline Alert Volume x 100; pull from alerting platform (PagerDuty, OpsGenie) monthly; establish 6-month pre-AIOps baseline

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### Question 8: Zero-Trust Security and Multi-Cloud Resilience

**Q3.2:** Have you implemented zero-trust security architecture for AI systems (continuous verification, least-privilege access, encrypted communication, runtime attestation) and established multi-cloud resilience (active-active deployment across cloud providers, automated failover, cloud-agnostic abstractions)?

**Evidence Required:**
- [ ] Zero-Trust AI Architecture implemented:
  - Continuous Verification: Every component continuously verified (not "trust once, access always")
  - Least-Privilege Access: Every service/user has minimum required permissions, regularly audited
  - Encrypted Communication: All service-to-service communication encrypted (mTLS)
  - Runtime Attestation: Services verify identity and integrity at runtime
  - Micro-Segmentation: Network segmentation isolating AI components
  - Adaptive Authentication: Risk-based authentication (e.g., elevated access requires MFA)
  - Security monitoring: Continuous monitoring for anomalous access patterns
- [ ] Multi-Cloud Resilience Architecture:
  - Active-Active Deployment: AI system deployed across ≥2 cloud providers simultaneously
  - Automated Failover: Automatic failover to backup cloud provider on primary cloud failure
  - Cloud-Agnostic Abstractions: Infrastructure-as-Code using cloud-agnostic tools (Terraform, Pulumi)
  - Data Replication: Real-time data replication across cloud providers
  - Multi-cloud orchestration tested (failover drills conducted at least annually)
  - Evidence of surviving cloud provider outage or degradation
- [ ] Hybrid Deployment support (cloud + on-premise coordination)
- [ ] Compliance considerations addressed (data residency, regulatory requirements)
- [ ] Evidence of zero-trust implementation (security audits, penetration tests, compliance certifications)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Zero-trust policy coverage (% of service-to-service paths enforcing mTLS and RBAC) | ___ | ___ | 100% | ☐ | |
| Multi-cloud failover RTO achieved in drills (minutes to full service restoration) | ___ | ___ | ≤30 minutes | ☐ | |
| Least-privilege audit pass rate (% of service accounts with no excess permissions) | ___ | ___ | ≥95% | ☐ | |
| Cross-cloud replication lag (seconds of data lag between primary and replica cloud) | ___ | ___ | ≤60 seconds | ☐ | |

**Metric Collection Guidance:**
- **Zero-trust policy coverage**: Audit service mesh configuration (Istio, Linkerd) and IAM policies; formula = Service Paths With mTLS + RBAC Enforced / Total Service Paths x 100; run automated compliance scan quarterly
- **Failover RTO in drills**: Time annual or semi-annual failover drill from trigger to service health check passing on secondary cloud; formula = time(service_healthy_secondary) - time(primary_failure_simulated); document each drill result
- **Least-privilege audit pass rate**: Run IAM analyzer or cloud security posture tool (AWS Access Analyzer, Azure Permissions Management); formula = Service Accounts With Minimum Required Permissions Only / Total Service Accounts x 100; report quarterly
- **Cross-cloud replication lag**: Monitor replication metrics from data replication tool (AWS DMS, custom sync); formula = MEAN(replication_lag_seconds) sampled every 5 minutes; alert if lag > 60 seconds; report monthly P95

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### Question 9: Open-Source Contributions and Measurable Business Impact

**Q3.3:** Does your organization contribute architecture patterns, reference implementations, and benchmarks to open-source and industry standards (at least 2 contributions per year), and demonstrate measurable business impact and ROI from architecture investments (quantified vulnerability reduction, cost savings, developer productivity improvements)?

**Evidence Required:**
- [ ] Open-Source Contributions (at least 2 per year):
  - Architecture Patterns: Published architecture patterns for AI code security (blog posts, white papers, conference talks)
  - Reference Implementations: Open-source reference architectures or tools (GitHub repositories)
  - Benchmarks: Contributed benchmarks or datasets for AI security tool evaluation
  - Standards Development: Participation in industry standards bodies (OWASP, NIST, ISO)
  - Documentation: Comprehensive documentation of architecture decisions, lessons learned
- [ ] Public Evidence:
  - Conference presentations on architecture (OWASP, security conferences, engineering conferences)
  - Blog posts or white papers published
  - GitHub repositories with open-source architecture components
  - Standards contributions documented
- [ ] Industry Impact:
  - Documented adoption by other organizations (downloads, citations, forks)
  - Influence on vendor products or industry practices
  - Recognition as thought leader in AI security architecture
- [ ] Measurable Business Impact demonstrated:
  - Vulnerability Reduction: Quantified reduction in vulnerabilities (≥50% reduction year-over-year)
  - Cost Savings: Calculated cost savings from AI architecture (reduced manual security review, faster remediation)
  - Developer Productivity: Measured productivity improvements (time savings, faster development cycles)
  - ROI Calculation: Documented ROI ≥3:1 (benefits exceed architecture investment costs)
  - Shift-Left Effectiveness: ≥80% of vulnerabilities caught in development (by AI) vs. QA or production
- [ ] Green Architecture considerations:
  - Energy-efficient AI (model compression, quantization for reduced compute)
  - Sustainable infrastructure practices documented
- [ ] Executive-level reporting on architecture business value

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Year-over-year vulnerability reduction in production (%) | ___ | ___ | ≥50% YoY | ☐ | |
| Shift-left ratio (% of vulnerabilities caught in development vs QA/production) | ___ | ___ | ≥80% in development | ☐ | |
| Architecture ROI (ratio of benefits to investment costs, trailing 12 months) | ___ | ___ | ≥3:1 | ☐ | |
| Open-source contributions per year (count of qualifying contributions) | ___ | ___ | ≥2/year | ☐ | |

**Metric Collection Guidance:**
- **YoY vulnerability reduction**: Compare production security incidents and post-release CVEs year vs prior year; formula = (Prior Year Production Vulns - Current Year Production Vulns) / Prior Year Production Vulns x 100; pull from bug tracker and security incident system; report annually
- **Shift-left ratio**: Tag all vulnerabilities in findings system by detection phase (development/IDE/CI, QA/staging, production); formula = Vulnerabilities Found in Development / Total Vulnerabilities Found x 100; report quarterly
- **Architecture ROI**: Benefits = cost of manual security reviews avoided + breach prevention value + developer time savings; Costs = infrastructure + tooling + engineering; formula = Total Benefits / Total Costs; document methodology and compute annually with finance team
- **Open-source contributions**: Maintain contribution log (GitHub repos, conference talks, published papers, standards working groups); count qualifying contributions per calendar year; qualifying = publicly accessible and substantive (>500 words or functional code)

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

**Level 3 Score:** _____ / 3.0 (sum of question scores)

**Level 3 Achieved:** [ ] Yes (all questions ≥0.67) [ ] No

---

## Practice Score Calculation

**SA-Software Practice Score:** _______ / 3.0

---

## Assessment Summary

**Assessment Date:** _________________________________

**Assessor(s):** _____________________________________

**HAI System(s) Assessed:** __________________________

**Overall Maturity Level:**
- [ ] Level 0 (Score < 0.5): Ad-hoc, no formal architecture for AI code security
- [ ] Level 1 (Score 0.5 - 1.49): Foundational architecture with model design, data management, workflow integration
- [ ] Level 2 (Score 1.5 - 2.49): Comprehensive architecture with ensemble learning, distributed processing, advanced UX
- [ ] Level 3 (Score 2.5 - 3.0): Industry-leading with self-healing, zero-trust, multi-cloud, AIOps, open-source contributions

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

## Secure Architecture Specific Notes

**AI Model Architecture Components:**
- [ ] Hybrid Architecture (Rule-Based + ML + Deep Learning)
- [ ] Multi-Stage Pipeline (Fast Filtering → ML Classification → Deep Analysis)
- [ ] Model Specialization (language-specific or vulnerability-specific)
- [ ] Explainability Architecture (LIME, SHAP, code-specific explanations)
- [ ] Model Versioning & Management (model registry)

**Data Architecture Components:**
- [ ] Training Data (curated vulnerability dataset: ≥10,000 labeled examples per vulnerability class)
- [ ] Code Repository Integration (≥95% of repositories, incremental analysis)
- [ ] Vulnerability Knowledge Base (structured database of patterns, remediation)
- [ ] Feedback Data Collection (IDE, code review, CI/CD, dashboard)
- [ ] Data Privacy & Security (encryption at rest/in transit, RBAC)

**Integration Architecture:**
- [ ] IDE Integration (real-time analysis, ≤3 second latency, ≥70% IDE coverage)
- [ ] CI/CD Pipeline Integration (<10% build time impact, PR analysis, build-time analysis)
- [ ] Code Review Platform Integration (AI PR comments on GitHub/GitLab/Bitbucket)
- [ ] API Architecture (RESTful API, authentication, rate limiting)

**Infrastructure Architecture:**
- [ ] Deployment Model (Cloud-Native Kubernetes or On-Premise Docker Swarm/VMware)
- [ ] Scalability (horizontal scaling, auto-scaling, ≥1,000 concurrent requests)
- [ ] High Availability (multi-instance, ≥99.5% uptime, load balancing)
- [ ] Disaster Recovery (RTO ≤4 hours, RPO ≤24 hours)
- [ ] Caching Strategy (≥60% cache hit rate at Level 1, ≥70% at Level 2)
- [ ] Database Architecture (findings DB, time-series DB for metrics)

**Security Architecture for AI:**
- [ ] Model Security (encryption, access controls, versioning with crypto signatures)
- [ ] Adversarial Attack Defense (input validation, anomaly detection, rate limiting)
- [ ] Training Data Security (provenance tracking, integrity, poisoning prevention)
- [ ] Credential & Secrets Management (secrets manager, no hardcoded credentials, rotation ≥90 days)
- [ ] API Security (OAuth 2.0, RBAC, input validation, rate limiting)
- [ ] Network Security (dedicated VPC/subnet, firewall rules, TLS 1.3)
- [ ] Audit & Logging (≥1 year retention)

**Feedback & Continuous Improvement:**
- [ ] Multi-channel feedback collection
- [ ] Tiered validation (developer + security expert + production incidents)
- [ ] Automated retraining pipeline (monthly or ≥1,000 samples)
- [ ] A/B testing architecture (traffic splitting, gradual rollout)
- [ ] Performance tracking dashboard

**Level 2 Advanced Architecture:**
- [ ] Ensemble Learning (5-10 specialist models, meta-model, ≥10% accuracy improvement)
- [ ] Real-Time Learning (continuous learning, active learning, ≥2% monthly improvement)
- [ ] Distributed Architecture (worker pools, ≥10M LOC, ≤5s latency, ≥80% parallel efficiency)
- [ ] Distributed Caching (≥70% cache hit rate, hierarchical caching)
- [ ] Database Sharding (horizontal sharding by repository/organization)
- [ ] Automated Remediation (fix generation, validation, ≥60% adoption)
- [ ] Contextual Security Guidance (≥30% false positive reduction)
- [ ] Developer Satisfaction ≥85%

**Level 3 Industry-Leading:**
- [ ] Self-Healing Architecture (auto-scaling, automatic rollback, self-optimizing)
- [ ] AIOps Integration (anomaly detection, predictive incident prevention, automated RCA)
- [ ] Zero-Trust Architecture (continuous verification, least-privilege, mTLS, runtime attestation)
- [ ] Multi-Cloud Resilience (active-active deployment, automated failover, cloud-agnostic)
- [ ] Open-Source Contributions (≥2 per year: architecture patterns, reference implementations, benchmarks)
- [ ] Measurable Business Impact (≥50% vulnerability reduction, ROI ≥3:1, ≥80% shift-left)
- [ ] Green Architecture (energy-efficient AI, model compression, sustainable infrastructure)

---

## Updated Scoring Methodology

### Question-Level Scoring

Each question receives a score based on evidence + outcome metrics:

| Answer Category | Score | Criteria |
|----------------|-------|----------|
| **Fully Mature** | 1.0 | Evidence complete + ≥75% of metrics meet targets (≥3 of 4 metrics) |
| **Implemented** | 0.67 | Evidence complete + 50-74% of metrics meet targets (2 of 4 metrics) |
| **Partial** | 0.33 | Evidence complete + <50% metrics meet targets OR incomplete evidence |
| **Not Implemented** | 0.0 | No evidence |

### Level Scoring

Level Score = Sum of question scores in that level / Number of questions

```
L1_score = (Q1.1_score + Q1.2_score + Q1.3_score) / 3
L2_score = (Q2.1_score + Q2.2_score + Q2.3_score) / 3 × (L1_score if L1_score ≥ 1.0, else 0)
L3_score = (Q3.1_score + Q3.2_score + Q3.3_score) / 3 × (L2_score if L2_score ≥ 1.0, else 0)
```

### Practice Score

Practice Score = L1_score + L2_score + L3_score (Maximum = 3.0)

### Maturity Interpretation

| Score Range | Maturity Level | Interpretation |
|-------------|---------------|----------------|
| 2.5 - 3.0 | Level 3: Industry-Leading | Comprehensive evidence + strong outcome metrics |
| 1.5 - 2.49 | Level 2: Comprehensive | Strong evidence + metrics at L1-L2 |
| 0.5 - 1.49 | Level 1: Foundational | Basic evidence + some outcome metrics at L1 |
| < 0.5 | Level 0: Ad-hoc | Minimal evidence or metrics |

---

**Document Version:** 3.0
**Last Updated:** 2026-02-18
**Next Review:** Quarterly or after significant HAI system changes
