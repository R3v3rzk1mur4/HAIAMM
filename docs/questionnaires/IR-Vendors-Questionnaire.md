# Implementation Review (IR) - Vendors Domain
## HAIAMM Assessment Questionnaire v3.0

**Practice:** Implementation Review (IR)
**Domain:** Vendors
**Purpose:** Assess organizational maturity in reviewing AI vendor risk management implementations for correctness, reliability, security, and performance
**Scoring Model:** Evidence + Outcome Metrics (see Scoring Methodology below)

---

## Instructions

- Answer each question honestly based on **current, implemented practices** (not plans or aspirations)
- Each question has two components: **Evidence** (what you did) and **Outcome Metrics** (how well it worked)
- **Scoring uses 4 tiers:** Fully Mature (1.0), Implemented (0.67), Partial (0.33), Not Implemented (0.0)
- **Answer progressively** - Complete all Level 1 questions before Level 2
- **Level progression** - Achieve ALL questions at lower level before advancing
- **Baseline first** - Record current metric values before setting targets

---

## Level 1: Comprehensive Implementation Review
**Objective:** Verify that AI vendor risk management implementations are correct, tested, secure, and performant

### **Question 1: Risk Scoring Algorithm Review**

**Q1.1:** Do you review risk scoring algorithm implementation with weighted scoring (data handling 30%, security 25%, compliance 20%, operational 15%, financial 10%), normalization to 0-100 scale, and edge case handling (missing data, extreme values, NaN)?

**Evidence Required:**
- [ ] Weighted scoring implementation reviewed (verify weight constants match design spec)
- [ ] Normalization logic verified (each dimension converted to 0-100 scale)
- [ ] Aggregation formula validated (weighted sum calculated correctly)
- [ ] Edge case handling tested (missing data, extreme values, NaN, zero scores, overflow)
- [ ] Data quality checks reviewed (input validation, outlier detection, rejection of invalid scores/dates/categories)
- [ ] Unit tests cover all scoring paths with known inputs/outputs

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Risk score accuracy vs. human expert labels | ___% | ___% | >=85% | ☐ | |
| Edge case test coverage (categories with passing tests) | ___/5 | ___/5 | 5/5 | ☐ | |
| Weight calibration error vs. actual risk outcomes | ___% | ___% | <=10% | ☐ | |
| Risk score calculation latency per vendor | ___ms | ___ms | <=1,000ms | ☐ | |

**Metric Collection Guidance:**
- **Risk score accuracy**: Compare ML risk predictions to human expert labels on a quarterly test set of >=100 vendors. Formula: `correct_predictions / total_predictions × 100`
- **Edge case coverage**: Count categories with passing unit tests out of 5: missing data, extreme values, NaN handling, zero scores, overflow/underflow. Source: test suite reports
- **Weight calibration error**: Correlate predicted risk tiers to actual vendor incidents over 12 months. Formula: `avg(abs(predicted_tier - actual_tier)) / max_tier × 100`
- **Calculation latency**: P95 latency for risk score API calls from APM monitoring (Datadog, New Relic). Measured continuously

**Answer:**
- ☐ **Fully Mature** (Evidence complete + >=3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of risk scoring review)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### **Question 2: ML Classification Model Review**

**Q1.2:** Do you review ML classification model implementation including training code (feature engineering, model selection, hyperparameter tuning, cross-validation), evaluation (>=85% accuracy target, confusion matrix), serving code (model loading, prediction API, confidence scores, versioning), and retraining pipeline with drift monitoring?

**Evidence Required:**
- [ ] Training code reviewed (data loading, feature engineering, model selection Random Forest/Gradient Boosting, hyperparameter tuning GridSearchCV/RandomizedSearchCV, cross-validation k-fold/stratified)
- [ ] Model evaluation verified (accuracy/precision/recall/F1, confusion matrix, >=85% agreement with human experts, class imbalance handling SMOTE/class weights)
- [ ] Serving code reviewed (model loading pickle/joblib/ONNX, prediction API inputs/outputs/latency, confidence scores with probability distributions, model versioning)
- [ ] Retraining pipeline reviewed (trigger on monthly schedule or accuracy <80%, model comparison deploy if >=5% improvement, rollback capability)
- [ ] Model monitoring reviewed (performance tracking over time, drift detection, alert on degradation >=5%)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| ML classification F1-score on quarterly test set | ___ | ___ | >=0.85 | ☐ | |
| Model drift detection latency (time to detect >=5% degradation) | ___ days | ___ days | <=7 days | ☐ | |
| Retraining pipeline success rate | ___% | ___% | >=95% | ☐ | |
| Model serving inference latency (P95) | ___ms | ___ms | <=200ms | ☐ | |

**Metric Collection Guidance:**
- **F1-score**: Evaluate model quarterly on held-out test set of >=200 labeled vendor assessments. Formula: `2 × (precision × recall) / (precision + recall)`. Source: model evaluation pipeline
- **Drift detection latency**: Track days between model accuracy dropping below threshold and automated alert firing. Source: model monitoring dashboard (MLflow, Weights & Biases)
- **Retraining success rate**: `successful_retraining_runs / total_triggered_runs × 100` over trailing 12 months. Source: CI/CD pipeline logs
- **Inference latency**: P95 of prediction API response times. Source: APM monitoring. Measured continuously

**Answer:**
- ☐ **Fully Mature** (Evidence complete + >=3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of ML model review)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### **Question 3: API Integration Review**

**Q1.3:** Do you review API integration implementation for vendor risk data sources (BitSight, SecurityScorecard, HaveIBeenPwned) including authentication, response parsing with rating normalization, rate limiting, timeout handling, retry logic with exponential backoff, circuit breaker pattern, and caching?

**Evidence Required:**
- [ ] BitSight API integration reviewed (API key auth, endpoint URLs, request parameters, response parsing, rating normalization 300-900 → 0-100)
- [ ] SecurityScorecard API integration reviewed (token auth, response parsing letter grades A-F → numerical, factor scores extraction)
- [ ] Breach database APIs reviewed (HaveIBeenPwned domain/email checks, response parsing, severity classification)
- [ ] General API resilience reviewed (rate limiting 100-1000 req/hr with backoff, timeout 30-60s, retry with exponential backoff, circuit breaker, response caching)
- [ ] API integration tests reviewed (mock responses, error handling, rate limit simulation)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| API call success rate across all vendor data sources | ___% | ___% | >=99% | ☐ | |
| API response time (P95) | ___ms | ___ms | <=2,000ms | ☐ | |
| Rate limit violation incidents per month | ___ | ___ | 0 | ☐ | |
| API response cache hit rate | ___% | ___% | >=60% | ☐ | |

**Metric Collection Guidance:**
- **API success rate**: `successful_api_calls / total_api_calls × 100` across BitSight, SecurityScorecard, HaveIBeenPwned. Source: API gateway logs, application logs. Measured daily
- **API response time**: P95 latency from request initiation to parsed response. Source: APM traces. Measured continuously
- **Rate limit violations**: Count of HTTP 429 responses received from vendor APIs per month. Source: API error logs. Reviewed weekly
- **Cache hit rate**: `cache_hits / (cache_hits + cache_misses) × 100`. Source: caching layer metrics (Redis, Memcached). Measured daily

**Answer:**
- ☐ **Fully Mature** (Evidence complete + >=3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of API integration review)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### **Question 4: Entity Resolution Review**

**Q1.4:** Do you review entity resolution implementation with fuzzy matching (Levenshtein distance, domain name matching, DUNS matching, >=80% similarity threshold), deduplication logic (primary key hierarchy DUNS > domain > name, merge strategy, conflict resolution for human review), and accuracy validation?

**Evidence Required:**
- [ ] Fuzzy matching implementation reviewed (Levenshtein distance calculation, domain name extraction/comparison, DUNS exact matching, threshold >=80% for medium confidence)
- [ ] Deduplication logic reviewed (primary key selection DUNS > domain > name, merge strategy latest data per field with lineage, conflict resolution flags for human review)
- [ ] Confidence scoring reviewed (high = exact DUNS, medium = domain + name >=80%, low = name similarity only, human review trigger on low confidence)
- [ ] Test coverage reviewed (known duplicates correctly identified, similar-but-different vendors not merged, edge cases empty strings/special characters)
- [ ] Accuracy validation on labeled test set (>=95% correct matching target)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Entity resolution accuracy on labeled test set | ___% | ___% | >=95% | ☐ | |
| False merge rate (incorrectly merged distinct vendors) | ___% | ___% | <=1% | ☐ | |
| Deduplication processing time per vendor pair | ___ms | ___ms | <=500ms | ☐ | |
| Human review queue volume (low-confidence matches awaiting review) | ___ | ___ | <=50/week | ☐ | |

**Metric Collection Guidance:**
- **Resolution accuracy**: Test on labeled set of >=200 vendor pairs (100 known duplicates + 100 known distinct). Formula: `(true_matches + true_non_matches) / total_pairs × 100`. Quarterly
- **False merge rate**: `incorrectly_merged_pairs / total_merge_decisions × 100`. Source: quarterly manual audit of 100 random merge decisions
- **Processing time**: P95 latency per vendor pair comparison. Source: application performance logs. Measured per batch run
- **Human review queue**: Count of low-confidence matches awaiting manual resolution per week. Source: review queue dashboard. Reviewed weekly

**Answer:**
- ☐ **Fully Mature** (Evidence complete + >=3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of entity resolution review)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### **Question 5: Continuous Monitoring Review**

**Q1.5:** Do you review continuous monitoring implementation with event-driven architecture (webhook subscriptions, event stream processing via Kafka/Kinesis, idempotency handling) and polling architecture (tiered schedule Critical daily / High weekly / Medium monthly / Low quarterly, change detection, state management)?

**Evidence Required:**
- [ ] Event-driven architecture reviewed (webhook subscriptions for BitSight/SecurityScorecard, event parsing, schema validation, Kafka/Kinesis consumer code, idempotent event processing)
- [ ] Polling architecture reviewed (tiered schedule enforcement Critical daily / High weekly / Medium monthly / Low quarterly, polling logic fetch/compare, change detection for rating changes/breaches/expiring certs, state management for previous vendor state)
- [ ] Monitoring coverage verified (100% of critical vendors monitored daily, all vendors at appropriate frequency)
- [ ] Monitoring tests reviewed (webhook processing tests, polling scheduler tests, change detection tests, state comparison tests)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Critical vendor daily monitoring coverage | ___% | ___% | 100% | ☐ | |
| Event processing latency (webhook to alert) | ___min | ___min | <=5 min | ☐ | |
| Monitoring system uptime | ___% | ___% | >=99.9% | ☐ | |
| Duplicate event processing rate | ___% | ___% | 0% | ☐ | |

**Metric Collection Guidance:**
- **Critical vendor coverage**: `critical_vendors_with_daily_monitoring / total_critical_vendors × 100`. Source: monitoring configuration database. Verified daily via automated check
- **Event processing latency**: Median and P95 time from webhook receipt to processed alert. Source: event pipeline timestamps. Measured per event
- **Monitoring uptime**: `(total_minutes - downtime_minutes) / total_minutes × 100` over trailing 30 days. Source: health check monitoring (Pingdom, UptimeRobot)
- **Duplicate event rate**: `duplicate_events_processed / total_events × 100`. Source: event deduplication logs. Should be 0% if idempotency works correctly. Measured daily

**Answer:**
- ☐ **Fully Mature** (Evidence complete + >=3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of monitoring review)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### **Question 6: Change Detection & Alert Generation Review**

**Q1.6:** Do you review change detection and alert generation implementation with rating change thresholds (>=10 points or grade drop), breach detection (<=24 hours from disclosure), certification expiration warnings (90/30/7 days), severity assignment (Critical/High/Medium/Low), alert deduplication (1-hour window), and routing (Critical → page, High → ticket, Medium/Low → digest)?

**Evidence Required:**
- [ ] Rating change detection reviewed (threshold >=10 points or letter grade drop, trend analysis for consistent downward trend, alert generation with severity/details/vendor)
- [ ] Breach detection reviewed (new breach identification vs. known breaches, severity classification customer data = Critical, detection within <=24 hours of public disclosure)
- [ ] Certification expiration reviewed (days-to-expiry calculation, tiered alerts at 90/30/7 days, escalating severity)
- [ ] Severity assignment reviewed (Critical: breach w/ customer data, rating failing, bankruptcy; High: >=20 point drop, cert <30 days; Medium: 10-20 point drop; Low: minor changes)
- [ ] Alert deduplication reviewed (suppress duplicate alerts within 1-hour window for same issue)
- [ ] Alert routing reviewed (Critical → PagerDuty/Opsgenie page, High → Jira/ServiceNow ticket, Medium/Low → email digest)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Breach detection latency (disclosure to internal alert) | ___ hrs | ___ hrs | <=24 hrs | ☐ | |
| Critical alert delivery latency | ___ min | ___ min | <=5 min | ☐ | |
| False alert rate (alerts not requiring action) | ___% | ___% | <=5% | ☐ | |
| Alert deduplication effectiveness | ___% | ___% | >=95% | ☐ | |

**Metric Collection Guidance:**
- **Breach detection latency**: Compare internal alert timestamp to public disclosure timestamp (HaveIBeenPwned, vendor disclosure, news). Formula: `alert_timestamp - disclosure_timestamp` in hours. Measured per breach event
- **Critical alert delivery**: Time from alert generation in system to delivery confirmation (PagerDuty acknowledgment). Source: alerting platform logs. Measured per critical alert
- **False alert rate**: `alerts_closed_as_false_positive / total_alerts × 100` over trailing 30 days. Source: alert resolution data in ticketing system. Reviewed monthly
- **Deduplication effectiveness**: `1 - (duplicate_alerts_delivered / total_duplicate_events) × 100`. Source: alert dedup logs. Reviewed weekly

**Answer:**
- ☐ **Fully Mature** (Evidence complete + >=3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of change detection review)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### **Question 7: SBOM Parsing Review**

**Q1.7:** Do you review SBOM parsing implementation with multi-format support (SPDX JSON/XML/YAML/tag-value, CycloneDX JSON/XML), parser library usage (spdx-tools, cyclonedx-python-lib), schema validation against official specs, and complete data extraction (component names, versions, licenses, dependency relationships)?

**Evidence Required:**
- [ ] Format support reviewed (SPDX parser for JSON, XML, YAML, tag-value; CycloneDX parser for JSON, XML)
- [ ] Parser library usage reviewed (spdx-tools, cyclonedx-python-lib correctly integrated)
- [ ] Schema validation reviewed (validates against official SPDX/CycloneDX schemas, rejects malformed SBOMs)
- [ ] Data extraction reviewed (component names/versions/vendors, license information SPDX IDs, dependency relationships parent-child links)
- [ ] Error handling reviewed (invalid format rejection, missing field handling, malformed SBOM graceful degradation)
- [ ] Performance tested (parsing <=30 seconds for 10,000-component SBOM, streaming for large files)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| SBOM format support coverage | ___/6 | ___/6 | 6/6 formats | ☐ | |
| Parsing time for 10K-component SBOM | ___sec | ___sec | <=30 sec | ☐ | |
| Schema validation pass rate (valid SBOMs accepted) | ___% | ___% | >=99% | ☐ | |
| Data extraction completeness (fields correctly extracted) | ___% | ___% | >=99% | ☐ | |

**Metric Collection Guidance:**
- **Format support**: Count supported formats out of 6: SPDX JSON, SPDX XML, SPDX YAML, SPDX tag-value, CycloneDX JSON, CycloneDX XML. Source: parser configuration. Verified per release
- **Parsing time**: Wall-clock time from SBOM upload to parsing complete for a standard 10K-component test SBOM. Source: performance test suite. Run weekly
- **Schema validation rate**: `valid_SBOMs_correctly_accepted / total_valid_SBOMs_submitted × 100`. Source: validation logs. Verified with standard test corpus
- **Extraction completeness**: `fields_correctly_extracted / total_expected_fields × 100` on a labeled test SBOM with known components. Source: extraction accuracy test suite. Run per release

**Answer:**
- ☐ **Fully Mature** (Evidence complete + >=3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of SBOM parsing review)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### **Question 8: Vulnerability Scanning Review**

**Q1.8:** Do you review vulnerability scanning implementation with CVE database integration (NVD API, GitHub Advisory Database), CVE/CPE matching logic (component name + version → CVEs, version range handling), transitive dependency analysis (>=5 levels deep, recursive propagation, DFS/BFS graph traversal), and CVSS v3.1 severity scoring with exploitability and reachability analysis?

**Evidence Required:**
- [ ] CVE database integration reviewed (NVD API fetch, GitHub Advisory Database integration, CVE matching component name + version, version range handling >=1.0 / <2.0)
- [ ] CPE matching reviewed (CPE string construction cpe:2.3:a:vendor:product:version, CPE dictionary search, precision/recall tuning)
- [ ] Transitive dependency analysis reviewed (dependency graph >=5 levels deep, recursive vulnerability propagation, graph traversal DFS/BFS)
- [ ] Severity scoring reviewed (CVSS v3.1 extraction from NVD, exploitability check Exploit-DB/Metasploit, reachability analysis, priority = CVSS + exploitability + reachability)
- [ ] Accuracy validated (precision >=90% on known vulnerable components, recall >=85% on patched components with no false positives)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| CVE matching precision (minimize false positives) | ___% | ___% | >=90% | ☐ | |
| CVE matching recall (minimize false negatives) | ___% | ___% | >=85% | ☐ | |
| Transitive dependency analysis depth achieved | ___ levels | ___ levels | >=5 levels | ☐ | |
| Vulnerability scan time per SBOM | ___sec | ___sec | <=60 sec | ☐ | |

**Metric Collection Guidance:**
- **CVE precision**: `true_positive_CVEs / (true_positive_CVEs + false_positive_CVEs) × 100` on test set of known vulnerable components. Source: quarterly manual validation of 100 random findings
- **CVE recall**: `true_positive_CVEs / (true_positive_CVEs + false_negative_CVEs) × 100` on NIST's known vulnerable software dataset. Source: quarterly regression testing
- **Transitive depth**: Maximum dependency depth traversed in production SBOM scans. Source: dependency graph analysis logs. Verified per SBOM
- **Scan time**: Wall-clock time from SBOM input to complete vulnerability report. Source: scanning pipeline performance logs. Measured per scan

**Answer:**
- ☐ **Fully Mature** (Evidence complete + >=3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of vulnerability scanning review)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### **Question 9: Supply Chain Attack Detection Review**

**Q1.9:** Do you review supply chain attack detection implementation for typosquatting (Levenshtein distance <=2 to popular packages, homoglyph detection), suspicious packages (newly created <30 days with low downloads, abandoned >=2 years, excessive permissions), and anomalous updates (major version jumps, maintainer changes, sudden activity spikes)?

**Evidence Required:**
- [ ] Typosquatting detection reviewed (Levenshtein distance <=2 to popular package names, homoglyph/Unicode detection Cyrillic vs. Latin, suspicious name patterns)
- [ ] Suspicious package detection reviewed (age <30 days with low downloads flagged, abandoned packages >=2 years no updates, excessive permissions filesystem/network)
- [ ] Anomalous update detection reviewed (major version jumps 1.0→2.0 flagged, maintainer/ownership changes detected, sudden activity spikes unusual update frequency)
- [ ] Detection tuning reviewed (false positive vs. false negative balance, whitelist for known-good packages, configurable thresholds)
- [ ] Alert workflow reviewed (severity classification, routing to security team, vendor notification, remediation tracking)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Typosquatting detection rate (known examples) | ___% | ___% | >=95% | ☐ | |
| Supply chain detection false positive rate | ___% | ___% | <=10% | ☐ | |
| Detection of known supply chain attacks (historical replay) | ___% | ___% | >=90% | ☐ | |
| Time from suspicious package detection to analyst notification | ___min | ___min | <=30 min | ☐ | |

**Metric Collection Guidance:**
- **Typosquatting detection rate**: Test with corpus of known typosquatting examples (>=50). Formula: `detected_typosquats / total_known_typosquats × 100`. Source: detection test suite. Run monthly
- **False positive rate**: `false_positive_alerts / total_supply_chain_alerts × 100` over trailing 30 days. Source: alert resolution data. Reviewed monthly
- **Known attack detection**: Replay historical supply chain attacks (event-stream, ua-parser-js, colors.js, etc.) through detection system. Formula: `detected / total_replayed × 100`. Quarterly
- **Notification latency**: Time from detection engine flag to analyst notification delivery. Source: alerting pipeline timestamps. Measured per detection event

**Answer:**
- ☐ **Fully Mature** (Evidence complete + >=3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of supply chain detection review)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

## Level 2: Advanced Implementation Review
**Objective:** Verify advanced AI techniques, data pipelines, and testing methodologies for vendor risk management

### **Question 10: ML Model Explainability & Fairness Review**

**Q2.1:** Do you review ML model advanced capabilities including explainability (SHAP values for individual predictions, feature importance analysis, counterfactual explanations), fairness testing (bias detection across vendor size/industry/geography, statistical parity within ±5%, bias mitigation), and AutoML integration (automated hyperparameter tuning, neural architecture search, automated feature engineering)?

**Evidence Required:**
- [ ] SHAP explainability reviewed (SHAP values generated for each prediction, feature importance analysis identifies key risk factors, counterfactual explanations "what would reduce this score?", explainability API provides explanations to stakeholders)
- [ ] Fairness testing reviewed (bias testing across vendor size, industry, geography; fairness metrics calculated statistical parity/equal opportunity; bias mitigation techniques re-weighting/fairness constraints)
- [ ] AutoML integration reviewed (automated hyperparameter tuning Optuna/Ray Tune, neural architecture search AutoKeras/NAS, automated feature engineering Featuretools)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Predictions with SHAP explanations available | ___% | ___% | 100% | ☐ | |
| Bias detection: statistical parity across vendor segments | ___% deviation | ___% deviation | <=5% deviation | ☐ | |
| AutoML retraining automation rate (zero manual tuning) | ___% | ___% | 100% automated | ☐ | |
| Stakeholder satisfaction with model explanations | ___% | ___% | >=80% | ☐ | |

**Metric Collection Guidance:**
- **SHAP coverage**: `predictions_with_SHAP / total_predictions × 100`. Source: model serving logs. Measured continuously
- **Statistical parity**: Max deviation in positive prediction rates across vendor segments (small/medium/large, by industry, by geography). Formula: `max(segment_rate) - min(segment_rate)`. Source: fairness audit pipeline. Quarterly
- **AutoML automation**: `automated_retraining_cycles / total_retraining_cycles × 100`. Source: MLOps pipeline logs. Measured per retraining event
- **Stakeholder satisfaction**: Survey analysts and procurement teams on explanation quality. Source: quarterly stakeholder survey (Likert scale → percentage). Quarterly

**Answer:**
- ☐ **Fully Mature** (Evidence complete + >=3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of advanced ML review)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### **Question 11: Advanced Data Pipeline Review**

**Q2.2:** Do you review advanced data pipeline implementation including stream processing (Kafka Streams/Apache Flink, event time processing, windowing operations, exactly-once semantics) and data quality monitoring (Great Expectations/Deequ automated checks, anomaly detection for schema drift/volume changes, data lineage tracking)?

**Evidence Required:**
- [ ] Stream processing reviewed (Kafka Streams or Apache Flink implementation, event time processing with late-event handling, windowing operations tumbling/sliding/session, exactly-once delivery semantics verified)
- [ ] Data quality monitoring reviewed (Great Expectations or Deequ automated checks, anomaly detection for data volume changes and schema drift, data lineage tracking provenance from source to normalized)
- [ ] Data validation pipelines reviewed (validate data before processing, reject invalid records, alert on quality degradation)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Stream processing latency (P99) | ___sec | ___sec | <=10 sec | ☐ | |
| Data quality check pass rate | ___% | ___% | >=99% | ☐ | |
| Duplicate event processing rate | ___% | ___% | 0% (exactly-once) | ☐ | |
| Data lineage coverage (sources with tracked provenance) | ___% | ___% | >=95% | ☐ | |

**Metric Collection Guidance:**
- **Stream latency**: P99 latency from event ingestion to processing complete. Source: stream processing framework metrics (Kafka Streams state store, Flink metrics). Measured continuously
- **Data quality pass rate**: `records_passing_all_checks / total_records_validated × 100`. Source: Great Expectations/Deequ validation reports. Measured per batch/stream window
- **Duplicate event rate**: `duplicate_events_processed / total_events × 100`. Source: event deduplication tracking. Should be 0% with exactly-once. Measured daily
- **Lineage coverage**: `data_sources_with_lineage / total_data_sources × 100`. Source: lineage tracking system (Apache Atlas, DataHub). Reviewed monthly

**Answer:**
- ☐ **Fully Mature** (Evidence complete + >=3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of advanced pipeline review)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### **Question 12: Advanced Testing Review**

**Q2.3:** Do you review advanced testing implementation including property-based testing (Hypothesis library for random input generation, invariants for risk scoring and entity resolution), mutation testing (mutmut with >=80% mutation kill rate), and chaos engineering (fault injection simulating API failures/database outages, resilience verification, recovery testing)?

**Evidence Required:**
- [ ] Property-based testing reviewed (Hypothesis framework generates random inputs, properties/invariants defined: risk scores always 0-100, entity matching is symmetric/transitive, >=10,000 random inputs tested)
- [ ] Mutation testing reviewed (mutmut configured, mutation score >=80% overall, >=90% on safety-critical code, surviving mutants investigated)
- [ ] Chaos engineering reviewed (fault injection simulates API failures/database outages/network partitions, resilience verified system continues in degraded mode, recovery verified system resumes after fault resolves)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Core functions with property-based tests | ___% | ___% | >=50% | ☐ | |
| Mutation testing kill rate (overall) | ___% | ___% | >=80% | ☐ | |
| Chaos test scenario survival rate | ___% | ___% | >=90% | ☐ | |
| Property test input volume per function | ___ | ___ | >=10,000 | ☐ | |

**Metric Collection Guidance:**
- **Property test coverage**: `functions_with_property_tests / total_core_functions × 100`. Core functions = risk scoring, entity resolution, alert generation, severity assignment. Source: test suite inventory. Reviewed per release
- **Mutation kill rate**: `killed_mutants / total_mutants × 100` from mutmut report. Source: mutation testing CI pipeline. Run monthly
- **Chaos survival rate**: `fault_scenarios_survived / total_fault_scenarios × 100`. Scenarios: API timeout, API 500, DB down, Kafka partition, network latency spike. Source: chaos test results. Run monthly in staging
- **Property test inputs**: Count of random inputs generated per Hypothesis test function. Source: Hypothesis statistics output. Verified per test run

**Answer:**
- ☐ **Fully Mature** (Evidence complete + >=3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of advanced testing review)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

## Level 3: Industry-Leading Implementation
**Objective:** Verify research-grade techniques including formal verification, federated learning, and quantum-safe cryptography

### **Question 13: Formal Verification Review**

**Q3.1:** Do you review formal verification of vendor risk implementations including TLA+ specifications of critical algorithms (risk scoring correctness, concurrency model checking), and smart contract verification for blockchain-based vendor registries (Solidity verification, immutable vendor records)?

**Evidence Required:**
- [ ] TLA+ specification reviewed (risk scoring algorithm specified, algorithm correctness proven scores always in range/monotonic, concurrency properties model-checked no deadlocks/race conditions)
- [ ] Model checking results reviewed (TLC model checker output, all safety properties hold, all liveness properties satisfied)
- [ ] Implementation-to-specification mapping reviewed (code matches TLA+ specification, manual review or automated verification)
- [ ] Smart contract verification reviewed (blockchain vendor registry if applicable, Solidity formal verification, immutable record integrity)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Critical algorithms with formal TLA+ specifications | ___% | ___% | >=50% | ☐ | |
| Concurrency bugs found in production (formally verified components) | ___ | ___ | 0 | ☐ | |
| Specification-to-code alignment verification coverage | ___% | ___% | >=90% | ☐ | |
| Model checking property violations in production | ___ | ___ | 0 | ☐ | |

**Metric Collection Guidance:**
- **Formal specification coverage**: `algorithms_with_TLA+_specs / total_critical_algorithms × 100`. Critical algorithms = risk scoring, event processing, state management, deduplication. Source: TLA+ spec inventory. Reviewed semi-annually
- **Concurrency bugs**: Count of concurrency-related bugs (race conditions, deadlocks, data corruption) in formally verified components. Source: bug tracker filtered by component + root cause. Measured continuously
- **Spec-code alignment**: `verified_code_paths / total_specified_code_paths × 100`. Source: formal verification tool output or manual alignment review. Reviewed quarterly
- **Property violations**: Count of safety/liveness property violations detected in production for model-checked components. Source: runtime property monitors. Measured continuously

**Answer:**
- ☐ **Fully Mature** (Evidence complete + >=3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of formal verification review)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### **Question 14: Advanced AI Techniques Review**

**Q3.2:** Do you review advanced AI technique implementations including federated learning (cross-organization vendor risk model training without sharing raw data, privacy-preserving aggregation, differential privacy guarantees with ε <=1.0) and neural architecture search (automated model discovery, multi-objective optimization for accuracy + latency + interpretability)?

**Evidence Required:**
- [ ] Federated learning reviewed (model trained across >=5 organizations without sharing raw vendor data, secure aggregation using secure multi-party computation, differential privacy enforced ε <=1.0)
- [ ] Privacy guarantees verified (no data leakage proven, gradient inspection attacks mitigated, federated vs. single-org accuracy compared)
- [ ] Neural architecture search reviewed (automated model discovery finds optimal architecture, multi-objective optimization balances accuracy + latency + interpretability)
- [ ] Accuracy improvement validated (federated model >=10% accuracy improvement vs. single-organization model)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Organizations participating in federated learning | ___ | ___ | >=5 | ☐ | |
| Accuracy improvement vs. single-org model | ___% | ___% | >=10% | ☐ | |
| Differential privacy guarantee (epsilon) | ___ | ___ | <=1.0 | ☐ | |
| NAS model discovery automation (zero manual architecture design) | ___% | ___% | 100% | ☐ | |

**Metric Collection Guidance:**
- **Federated participants**: Count of organizations contributing to federated model training. Source: federated learning platform dashboard. Reviewed quarterly
- **Accuracy improvement**: `(federated_accuracy - single_org_accuracy) / single_org_accuracy × 100` on common evaluation set. Source: model evaluation pipeline. Measured per federated training round
- **Differential privacy**: Epsilon value from privacy accounting (Rényi differential privacy or moments accountant). Source: federated learning framework privacy budget tracking. Verified per training round
- **NAS automation**: `NAS_discovered_architectures / total_new_model_architectures × 100`. Source: NAS experiment logs. Reviewed quarterly

**Answer:**
- ☐ **Fully Mature** (Evidence complete + >=3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of advanced AI techniques review)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

### **Question 15: Quantum-Safe Implementation Review**

**Q3.3:** Do you review quantum-safe cryptography implementation for vendor data protection including post-quantum algorithms (ML-KEM for key encapsulation, ML-DSA for digital signatures, SLH-DSA for stateless hash-based signatures), hybrid cryptography (classical + PQC during transition period), and migration of all quantum-vulnerable algorithms?

**Evidence Required:**
- [ ] Post-quantum algorithm implementation reviewed (ML-KEM key encapsulation for vendor data encryption, ML-DSA digital signatures for vendor attestations, SLH-DSA hash-based signatures where applicable)
- [ ] Hybrid cryptography reviewed (classical + PQC algorithms run in parallel during transition, fallback to classical if PQC implementation issues)
- [ ] Quantum-vulnerable algorithm inventory reviewed (identify all RSA, ECDSA, ECDH usage in vendor data handling, migration plan to PQC equivalents)
- [ ] Performance impact assessed (PQC algorithm latency vs. classical, key size impact on storage/bandwidth, acceptable performance thresholds defined)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Sensitive vendor data protected with PQC encryption | ___% | ___% | 100% | ☐ | |
| Quantum-vulnerable algorithms remaining in vendor systems | ___ | ___ | 0 | ☐ | |
| Hybrid mode operational (classical + PQC fallback working) | ☐ Yes / ☐ No | ☐ Yes / ☐ No | Yes | ☐ | |
| PQC performance overhead vs. classical | ___% | ___% | <=50% latency increase | ☐ | |

**Metric Collection Guidance:**
- **PQC encryption coverage**: `vendor_data_fields_with_PQC_encryption / total_sensitive_vendor_data_fields × 100`. Source: encryption configuration audit. Reviewed quarterly
- **Quantum-vulnerable algorithms**: Count of RSA/ECDSA/ECDH instances in vendor data handling code and infrastructure. Source: cryptographic algorithm inventory scan (automated). Reviewed monthly
- **Hybrid mode status**: Binary - is hybrid mode (classical + PQC with automatic fallback) operational in production? Source: cryptography configuration, integration test results. Verified monthly
- **PQC performance overhead**: `(PQC_operation_latency - classical_operation_latency) / classical_operation_latency × 100` for key operations (encrypt, decrypt, sign, verify). Source: performance benchmark suite. Run quarterly

**Answer:**
- ☐ **Fully Mature** (Evidence complete + >=3 metrics meet targets)
- ☐ **Implemented** (Evidence complete + 2 metrics meet targets)
- ☐ **Partial** (Evidence partially complete + <2 metrics meet targets)
- ☐ **Not Implemented** (No evidence of quantum-safe review)

**Evidence Location:** _________________________________

**Metric Validation Date:** _________________________________

**Notes:** ___________________________________________

---

## Scoring Methodology

### Per-Question Scoring

| Answer | Score | Criteria |
|--------|-------|----------|
| Fully Mature | 1.0 | Evidence complete + >=75% of outcome metrics meet targets (>=3 of 4 metrics) |
| Implemented | 0.67 | Evidence complete + 50-74% of outcome metrics meet targets (2 of 4 metrics) |
| Partial | 0.33 | Evidence partially complete + <50% of metrics meet targets (<2 metrics) |
| Not Implemented | 0.0 | No evidence of implementation review |

### Level Scoring

- **L1 Score** = Average of all L1 question scores (Q1.1 through Q1.9)
- **L2 Score** = Average of all L2 question scores (Q2.1 through Q2.3) × (1 if L1 >= 1.0, else 0)
- **L3 Score** = Average of all L3 question scores (Q3.1 through Q3.3) × (1 if L2 >= 1.0, else 0)

### Practice Score

**IR-Vendors Practice Score = L1 + L2 + L3** (Maximum: 3.0)

| Score Range | Interpretation |
|-------------|---------------|
| 0.0 - 0.5 | Initial - No systematic implementation review for vendor risk code |
| 0.5 - 1.0 | Developing - Basic code reviews established but metrics not tracked |
| 1.0 - 1.5 | Defined - Comprehensive L1 reviews with measurable accuracy targets |
| 1.5 - 2.0 | Managed - Advanced reviews with explainability, fairness, and chaos testing |
| 2.0 - 2.5 | Optimizing - Research-grade formal verification and federated learning adopted |
| 2.5 - 3.0 | Industry-Leading - Full formal verification, federated AI, and quantum-safe cryptography |

### Score Calculation Example

```
Example Organization:
  Q1.1 = 0.67 (Implemented)    Q1.6 = 1.0  (Fully Mature)
  Q1.2 = 0.67 (Implemented)    Q1.7 = 0.67 (Implemented)
  Q1.3 = 1.0  (Fully Mature)   Q1.8 = 0.67 (Implemented)
  Q1.4 = 0.67 (Implemented)    Q1.9 = 0.33 (Partial)
  Q1.5 = 1.0  (Fully Mature)

  L1 Score = (0.67+0.67+1.0+0.67+1.0+1.0+0.67+0.67+0.33) / 9 = 0.74

  Since L1 (0.74) < 1.0, L2 is gated:
  L2 Score = 0 (must achieve L1 >= 1.0 first)
  L3 Score = 0 (gated by L2)

  Practice Score = 0.74 + 0 + 0 = 0.74 (Developing)

  Action: Improve Q1.9 supply chain detection and raise Q1.2/Q1.4/Q1.7/Q1.8
  from Implemented to Fully Mature to unlock Level 2.
```

---

**Document Information:** Practice: Implementation Review (IR) | Domain: Vendors | HAIAMM v3.0 | Last Updated: 2026-02-10
