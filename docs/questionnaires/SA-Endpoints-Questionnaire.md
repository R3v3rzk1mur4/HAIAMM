# Secure Architecture (SA) - Endpoints Domain
## HAIAMM Assessment Questionnaire v3.0

**Practice:** Secure Architecture (SA)
**Domain:** Endpoints
**Purpose:** Assess organizational maturity in architectural design for AI-powered endpoint security systems including EDR/XDR, behavioral analytics, ransomware detection, and automated response
**Scoring Model:** Evidence + Outcome Metrics

---

## Instructions

- Answer each question honestly based on **current, implemented practices** (not plans or aspirations)
- **Evidence and metrics both required** - Document proof and collect metric data for each question
- **Answer progressively** - Complete all Level 1 questions before Level 2
- **Level progression** - Achieve ALL questions at lower level before advancing
- **Partial implementation = "Partial" or below** - Practice must be complete and systematic for "Implemented" or higher

---

## Level 1: Foundational
**Objective:** Establish foundational architecture for AI-powered endpoint security with hybrid detection models, lightweight endpoint agents, privacy-preserving telemetry, centralized analysis, safe automated response, and cross-platform support

### Question 1: AI Model Architecture and Hybrid Detection Design

**Q1.1:** Have you designed and deployed AI model architecture for endpoint threat detection using a hybrid approach (signature-based, heuristic, and machine learning detection with ensemble combination), with on-device lightweight models for real-time detection (≤1 second) and cloud-based deep learning models for high-accuracy analysis, including model specialization for ransomware, fileless attacks, and lateral movement?

**Evidence Required:**
- [ ] Hybrid Detection Architecture designed and implemented:
  - Signature-Based Detection: Traditional antivirus signatures for known malware (fast, low resource)
  - Heuristic Detection: Behavior-based rules for suspicious activities
  - Machine Learning Detection: Random Forest for file classification (PE headers, API calls, strings), neural networks for behavioral analysis (process trees, network connections)
  - Ensemble Combination: All methods combined for comprehensive coverage with weighted voting
- [ ] On-Device vs Cloud Analysis Architecture:
  - On-Device (Lightweight Models): Simple ML models running on endpoint, ≤1 second detection, works offline
  - Cloud (Heavy Models): Deep learning models in cloud backend, higher accuracy, network required
  - Decision Logic: When to escalate from on-device to cloud analysis (confidence threshold-based)
- [ ] Model Specialization:
  - Ransomware-Specific Models: Detect rapid file encryption patterns, canary file monitoring
  - Fileless Attack Models: Detect PowerShell/WMI abuse, memory-only malware, script-based attacks
  - Lateral Movement Models: Detect unusual network behavior indicating attacker pivoting
  - Insider Threat Models: Detect unusual data access patterns, privilege escalation attempts
- [ ] Model Versioning & Management:
  - Model registry with versions, metadata, performance metrics per endpoint platform
  - A/B testing architecture for model updates before full deployment
  - Rollback capability if model performance degrades ≥5%
- [ ] Explainability: Detection decisions include reasoning (features triggered, confidence factors, kill chain stage)
- [ ] Architecture documentation (diagrams, design decisions, technology choices)
- [ ] Architecture reviewed by security engineering and SOC leadership

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Overall endpoint malware detection rate (red team validated) | ___ | ___ | ≥95% | ☐ | |
| On-device detection latency | ___ | ___ | ≤1 second | ☐ | |
| False positive rate across all detection methods | ___ | ___ | ≤5% | ☐ | |
| Model rollback trigger threshold compliance | ___ | ___ | Automated rollback within 1 hr of ≥5% degradation | ☐ | |

**Metric Collection Guidance:**
- **Overall endpoint malware detection rate (red team validated)**: Red team exercise reports and EDR detection dashboard; formula = (threat scenarios detected by hybrid detection system / total threat scenarios executed in red team exercise) × 100; conduct at least semi-annually, covering all specialization categories (ransomware, fileless, lateral movement)
- **On-device detection latency**: EDR agent telemetry timing logs; formula = median time in milliseconds from event generation on endpoint to local classification decision; sample 1,000 detection events per month from agent performance telemetry, report as median and 95th percentile
- **False positive rate across all detection methods**: EDR alert disposition log; formula = (endpoint alerts confirmed false positive by analyst or automated validation / total endpoint alerts generated) × 100; collect monthly from analyst case closure data and automated resolution tags
- **Model rollback trigger threshold compliance**: Model registry event log; formula = (rollback events where automated rollback was initiated within 60 minutes of ≥5% degradation detection / total rollback trigger events) × 100; review each rollback event post-occurrence

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________
**Metric Validation Date:** _________________________________
**Notes:** ___________________________________________

---

### Question 2: Endpoint Agent Architecture and Privacy-Preserving Telemetry

**Q1.2:** Have you implemented lightweight endpoint agent architecture (sensor, local AI engine, response module, communication module) meeting performance requirements (≤5% CPU, ≤200 MB memory, ≤3% battery impact), with privacy-preserving telemetry architecture (data minimization, BYOD work/personal separation, GDPR compliance with ≤90 day retention) and secure agent update mechanisms (staged rollout with automated rollback)?

**Evidence Required:**
- [ ] Endpoint Agent Architecture:
  - Sensor Component: Collect endpoint telemetry (process events, file events, network events, registry events)
  - Local AI Engine: Lightweight ML models for real-time detection on-device
  - Response Module: Execute containment actions (isolate, kill process, quarantine file)
  - Communication Module: Secure encrypted communication with backend (TLS 1.3, certificate pinning)
- [ ] Performance Requirements Met:
  - CPU Usage: ≤5% average (measured at 95th percentile across fleet)
  - Memory: ≤200 MB resident memory
  - Disk I/O: Minimized to avoid performance degradation
  - Battery Impact: ≤3% battery drain on laptops/mobile devices
  - Performance testing results documented per platform
- [ ] Privacy-Preserving Telemetry:
  - Data Minimization: Collect only security-relevant data (e.g., "Word.exe launched Calculator.exe" not document contents)
  - Differential Privacy: Noise added to aggregate telemetry to prevent individual identification
  - BYOD Privacy Architecture: Work/personal separation, user consent for monitoring scope, data isolation
  - GDPR Compliance: Telemetry retained ≤90 days, right to access, right to deletion (except during investigations)
- [ ] Secure Agent Update Architecture:
  - Over-the-Air Updates: Secure automatic agent updates with code signing verification
  - Staged Rollout: 10% → 50% → 100% deployment with health monitoring at each stage
  - Automated Rollback: Automatic rollback if update causes agent health degradation or performance regression
  - Update authentication: Cryptographic signing prevents malicious agent updates
- [ ] Agent architecture supports ≥95% endpoint deployment coverage

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Agent CPU usage (95th percentile across fleet) | ___ | ___ | ≤5% | ☐ | |
| Endpoint fleet agent deployment coverage | ___ | ___ | ≥95% of managed endpoints | ☐ | |
| Telemetry data retention compliance rate | ___ | ___ | 100% deleted within 90 days (non-investigation data) | ☐ | |
| Agent update staged rollout success rate | ___ | ___ | ≥99% successful updates without manual rollback | ☐ | |

**Metric Collection Guidance:**
- **Agent CPU usage (95th percentile across fleet)**: Endpoint performance monitoring (EDR agent telemetry or endpoint management platform); formula = 95th percentile of per-endpoint average CPU usage attributed to agent processes across fleet; sample daily, report monthly fleet-wide 95th percentile
- **Endpoint fleet agent deployment coverage**: Endpoint management platform (MDM, SCCM, or EDR console); formula = (endpoints with active healthy agent / total managed endpoints in CMDB) × 100; collect weekly from asset management console
- **Telemetry data retention compliance rate**: Data management platform + retention policy audit; formula = (telemetry data records deleted within 90 days of collection date / total telemetry data records eligible for deletion in audit period) × 100; audit monthly using automated data age analysis query
- **Agent update staged rollout success rate**: Agent update management system; formula = (endpoints successfully updated to target version without requiring manual rollback intervention / total endpoints targeted for update) × 100; measure per update campaign, track within staged deployment windows

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________
**Metric Validation Date:** _________________________________
**Notes:** ___________________________________________

---

### Question 3: Centralized Analysis, Automated Response, and Cross-Platform Architecture

**Q1.3:** Have you implemented centralized analysis architecture (stream processing for real-time telemetry from thousands of endpoints, cross-endpoint correlation for outbreak and lateral movement detection, threat intelligence integration), safe automated response architecture (tiered response levels with blast radius limits preventing mass disruption), and cross-platform support architecture (Windows, macOS, Linux, mobile) with platform-agnostic detection logic?

**Evidence Required:**
- [ ] Centralized Analysis Architecture:
  - Stream Processing: Kafka/Kinesis for real-time telemetry streams from ≥1,000 endpoints
  - Data Lake: Raw telemetry storage for forensic analysis (S3, Azure Data Lake)
  - SIEM Integration: Forward endpoint events to organizational SIEM
  - Cross-Endpoint Correlation: Detect same malware on multiple endpoints (outbreak), unusual cross-endpoint network connections (lateral movement), simultaneous suspicious activity (coordinated attacks)
  - Threat Intelligence Integration: IOC matching against threat intel feeds, file hash/domain/IP reputation services
- [ ] Safe Automated Response Architecture:
  - Tiered Response Levels:
    - Level 1 - Alert: Notify SOC, no automated action
    - Level 2 - Isolate: Disconnect endpoint from network (prevent spread)
    - Level 3 - Remediate: Kill malicious process, delete malware, restore files
    - Level 4 - Reimage: Wipe and rebuild endpoint (requires human approval)
  - Safety Guardrails: User notification before disruptive actions, override capability, quarantine (not delete) suspicious files
  - Blast Radius Limits: AI cannot isolate >50 endpoints in 10-minute window without approval; AI cannot automatically reimage any endpoint
  - Escalation: Automated escalation to SOC when AI confidence is below threshold
- [ ] Cross-Platform Support Architecture:
  - Multi-Platform Agent: Windows (C++/Rust), macOS (respecting Apple privacy frameworks), Linux (multi-distro), Mobile (iOS/Android with OS restrictions)
  - Platform-Specific Challenges Addressed: macOS Endpoint Security Framework, Linux kernel diversity, mobile app sandboxing
  - Unified Detection Logic: Platform-agnostic rules (YARA, Sigma) with platform-specific implementations (Windows hooks, macOS ESF, Linux eBPF)
- [ ] Architecture documentation and approval by security and IT operations leadership

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Cross-platform agent coverage (Windows, macOS, Linux, mobile) | ___ | ___ | All 4 platform families covered with active agents | ☐ | |
| Outbreak detection time (same malware across multiple endpoints) | ___ | ___ | ≤5 minutes from first detection to outbreak alert | ☐ | |
| Automated response blast radius compliance rate | ___ | ___ | Zero violations of isolation limits without approval | ☐ | |
| Telemetry reporting completeness (endpoints actively reporting) | ___ | ___ | ≥90% of managed endpoints reporting telemetry | ☐ | |

**Metric Collection Guidance:**
- **Cross-platform agent coverage**: EDR console + endpoint inventory; formula = count of distinct OS platform families (Windows, macOS, Linux, mobile) with ≥95% of that platform's managed endpoints running a healthy agent; audit monthly from asset management platform broken down by OS family
- **Outbreak detection time**: EDR correlation engine logs; formula = median time in minutes from first individual endpoint detection event to cross-endpoint outbreak alert generation; measure for each outbreak or simulated outbreak event, target median ≤5 minutes
- **Automated response blast radius compliance rate**: SOAR/EDR automated response audit log; formula = (automated isolation actions that stayed within configured blast radius limits / total automated isolation actions) × 100; review monthly from response action audit trail; any violation requires immediate investigation
- **Telemetry reporting completeness**: EDR management console health dashboard; formula = (endpoints reporting at least one telemetry event in the past 24 hours / total managed endpoints) × 100; collect daily, report weekly average

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________
**Metric Validation Date:** _________________________________
**Notes:** ___________________________________________

---

**Level 1 Score:** _____ / 3 questions answered "Implemented" or above

**Level 1 Achieved:** ☐ Yes (3/3 at Implemented or above) ☐ No (< 3/3)

---

## Level 2: Comprehensive
**Objective:** Implement behavioral analytics (UEBA) for advanced threat detection, memory forensics for fileless malware, automated threat hunting, predictive endpoint security, and advanced privacy-preserving techniques

**Prerequisites:** ALL Level 1 questions must be "Implemented" or above to proceed to Level 2

### Question 4: Behavioral Analytics (UEBA) and Memory Forensics Architecture

**Q2.1:** Have you implemented behavioral analytics (UEBA) architecture including per-endpoint user behavior baselining, anomaly detection models (Isolation Forest, Autoencoders) for detecting deviations from normal patterns, and memory forensics architecture for in-memory threat detection (rootkits, fileless malware, DLL injection) and Living-off-the-Land attack detection using ML-based command-line analysis?

**Evidence Required:**
- [ ] Behavioral Analytics (UEBA) Architecture:
  - User Behavior Baselining: ML models learn normal user behavior per endpoint (login times, applications used, data access patterns)
  - Anomaly Detection Models: Isolation Forest, Autoencoders, or equivalent for outlier detection
  - Context-Aware Scoring: Anomaly scores adjusted for context (time of day, user role, device type)
  - Example Coverage: Unusual login times, unusual applications, unusual data access, privilege escalation patterns
  - Accuracy Target: ≥85% detection rate for insider threat scenarios with ≤10% false positive rate
- [ ] Memory Forensics Architecture:
  - In-Memory Threat Detection: Scan process memory for malicious code injection, rootkits, fileless malware
  - Techniques: YARA scanning of memory, API hooking detection, DLL injection detection, reflective loading detection
  - Performance: Memory scanning ≤5% additional CPU during scan windows
- [ ] Living-off-the-Land (LOTL) Detection:
  - Legitimate Tool Abuse Detection: PowerShell, WMI, PsExec, certutil, mshta, regsvr32
  - ML Command-Line Analysis: Models trained on benign vs malicious command patterns
  - Behavioral Context: Same command benign from admin, suspicious from regular user
  - MITRE ATT&CK Mapping: LOTL detections mapped to ATT&CK techniques
- [ ] UEBA and memory forensics integrated with centralized analysis for cross-endpoint correlation
- [ ] Detection models validated via purple team exercises

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| UEBA detection rate for insider threat scenarios (purple team validated) | ___ | ___ | ≥85% detection rate | ☐ | |
| UEBA false positive rate | ___ | ___ | ≤10% | ☐ | |
| Memory scan CPU overhead during scan windows | ___ | ___ | ≤5% additional CPU | ☐ | |
| LOTL technique detection coverage (MITRE ATT&CK mapped) | ___ | ___ | ≥80% of common LOTL techniques detected | ☐ | |

**Metric Collection Guidance:**
- **UEBA detection rate for insider threat scenarios (purple team validated)**: Purple team exercise reports + UEBA platform; formula = (insider threat simulation scenarios generating UEBA alert / total insider threat scenarios executed) × 100; conduct at least annually using documented insider threat scenario library covering data exfiltration, privilege escalation, account misuse
- **UEBA false positive rate**: UEBA platform + analyst disposition log; formula = (UEBA alerts confirmed false positive by analyst / total UEBA alerts generated in period) × 100; collect monthly from analyst case closure data tagged by alert source
- **Memory scan CPU overhead during scan windows**: Endpoint performance telemetry; formula = median CPU usage difference on endpoints during active memory scan windows vs baseline CPU usage at same time of day; sample across 100+ endpoints per platform, measure monthly
- **LOTL technique detection coverage**: Detection rule registry mapped to MITRE ATT&CK; formula = (count of MITRE ATT&CK LOTL sub-techniques with at least one active detection rule or ML model / total MITRE ATT&CK LOTL sub-techniques in scope) × 100; audit quarterly against current ATT&CK version

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________
**Metric Validation Date:** _________________________________
**Notes:** ___________________________________________

---

### Question 5: Automated Threat Hunting and Predictive Endpoint Security

**Q2.2:** Have you implemented automated threat hunting architecture (AI-generated hypothesis-driven hunting, continuous hunting queries, retrospective analysis) and predictive endpoint security models that identify endpoints at highest risk of compromise based on risk factors (patch status, configuration drift, user behavior, exposure) for proactive hardening?

**Evidence Required:**
- [ ] Automated Threat Hunting Architecture:
  - Hypothesis-Driven Hunting: AI generates threat hunting hypotheses based on threat intelligence
    - Example: "New APT campaign uses LOLBin X" → AI hunts for LOLBin X usage across all endpoints
  - Continuous Hunting Queries: Automated queries run continuously to discover hidden threats missed by real-time detection
  - Retrospective Analysis: When new IOCs or attack patterns identified, automatically search historical telemetry
  - Threat Intelligence Integration: Hunting hypotheses informed by MITRE ATT&CK, vendor advisories, industry threat reports
  - Hunting Effectiveness: Track discovery rate (threats found per hunting cycle)
- [ ] Predictive Endpoint Security:
  - Risk Factor Analysis: ML models predict endpoint compromise probability based on:
    - Patch status (missing critical patches)
    - Configuration drift (deviations from security baseline)
    - User behavior risk score (phishing susceptibility, policy violations)
    - Network exposure (internet-facing services, VPN usage patterns)
    - Historical incidents (previous malware infections, policy violations)
  - Proactive Hardening: High-risk endpoints receive enhanced monitoring, forced patching, restricted access
  - Prediction Validation: Back-testing against historical endpoint incidents
  - Risk Dashboard: Endpoint fleet risk visualization for security and IT operations
- [ ] Hunting and prediction models integrated with response architecture (automated or recommended actions)
- [ ] Quarterly review of hunting effectiveness and prediction accuracy

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Endpoint compromise prediction model accuracy (back-tested) | ___ | ___ | ≥70% precision in identifying high-risk endpoints | ☐ | |
| Additional threats discovered via automated hunting (not caught by real-time detection) | ___ | ___ | ≥5% of total incidents discovered via hunting | ☐ | |
| Patch compliance rate on endpoints flagged as high-risk | ___ | ___ | ≥95% of critical patches applied within 48 hrs on high-risk endpoints | ☐ | |
| Retrospective hunt coverage on new IOC publication | ___ | ___ | 100% of newly published IOCs hunted within 24 hours | ☐ | |

**Metric Collection Guidance:**
- **Endpoint compromise prediction model accuracy (back-tested)**: ML model evaluation pipeline against historical incident data; formula = (endpoints flagged as high-risk by model that subsequently experienced a confirmed security incident within 30 days / total endpoints flagged as high-risk by model) × 100; calculate quarterly using 6-month rolling historical dataset
- **Additional threats discovered via automated hunting**: Incident management system with detection source tagging; formula = (confirmed incidents first discovered by automated hunting query / total confirmed incidents in period) × 100; collect monthly; exclude incidents also detected simultaneously by real-time detection
- **Patch compliance rate on endpoints flagged as high-risk**: Patch management system + endpoint risk scoring system; formula = (high-risk endpoints with critical patches applied within 48 hours of patch release / total high-risk endpoints eligible for patch) × 100; measure per patch release cycle
- **Retrospective hunt coverage on new IOC publication**: Threat hunting management system; formula = (newly published IOCs (from threat intel feeds) that triggered automated retrospective hunt within 24 hours / total newly published IOCs received) × 100; measure weekly from IOC ingestion log vs hunt execution log

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________
**Metric Validation Date:** _________________________________
**Notes:** ___________________________________________

---

### Question 6: Advanced Privacy-Preserving Techniques and Federated Learning

**Q2.3:** Have you implemented advanced privacy-preserving endpoint security architecture including federated learning (train models across endpoints without centralizing raw data), on-device model personalization, privacy-preserving threat intelligence sharing, and BYOD-specific privacy controls that meet GDPR and regional privacy requirements while maintaining detection effectiveness?

**Evidence Required:**
- [ ] Federated Learning Architecture:
  - Distributed Training: Train ML models across endpoints without sending raw telemetry to central server
  - Model Aggregation: Secure aggregation of model updates from endpoints (federated averaging)
  - Privacy Guarantees: Differential privacy applied to model updates (prevent data reconstruction)
  - Performance: Federated models achieve ≥90% of centrally-trained model accuracy
- [ ] On-Device Model Personalization:
  - Per-Endpoint Adaptation: Base model fine-tuned on each endpoint's specific patterns
  - Transfer Learning: Global model provides baseline, endpoint-specific layer adapts to local behavior
  - Privacy Preservation: Personalized model never leaves endpoint
- [ ] Privacy-Preserving Threat Intelligence Sharing:
  - IOC Sharing: Share threat indicators without revealing endpoint identity or user data
  - Techniques: Secure multi-party computation, homomorphic encryption, or privacy-preserving protocols
  - Compliance: Sharing mechanisms validated against GDPR, CCPA, and organizational privacy policies
- [ ] BYOD-Specific Privacy Controls:
  - Containerization: Work data and monitoring fully isolated from personal applications
  - User Transparency: Clear dashboard showing exactly what is monitored and what is not
  - Consent Management: Granular consent controls with opt-out options for non-essential monitoring
  - Data Minimization Audit: Regular audit confirming only security-relevant data collected
- [ ] Privacy architecture validated by legal/compliance team and DPO (if applicable)
- [ ] Privacy impact assessment completed for endpoint monitoring architecture

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Federated model accuracy vs centrally-trained model accuracy | ___ | ___ | ≥90% of centralized model accuracy | ☐ | |
| BYOD user consent coverage rate | ___ | ___ | 100% of BYOD users with documented consent | ☐ | |
| Privacy violations from endpoint monitoring | ___ | ___ | Zero GDPR/privacy regulatory findings | ☐ | |
| Data minimization audit compliance | ___ | ___ | 100% of telemetry categories confirmed security-relevant each quarter | ☐ | |

**Metric Collection Guidance:**
- **Federated model accuracy vs centrally-trained model accuracy**: ML evaluation pipeline; formula = (federated model F1 score on held-out test set / centrally-trained model F1 score on same test set) × 100; evaluate quarterly using identical evaluation dataset and detection categories; report as percentage of centralized accuracy achieved
- **BYOD user consent coverage rate**: BYOD enrollment system + consent management platform; formula = (BYOD devices with valid current consent record on file / total BYOD devices enrolled) × 100; audit monthly; flag any enrolled device without documented consent for immediate remediation
- **Privacy violations from endpoint monitoring**: Legal/compliance incident register + DPO records; formula = count of confirmed GDPR, CCPA, or other privacy regulatory findings related to endpoint monitoring in the assessment period; collect quarterly from compliance incident register; target is zero findings
- **Data minimization audit compliance**: Data governance platform + telemetry category registry; formula = (telemetry data categories with documented security justification reviewed in current quarter / total active telemetry data categories) × 100; conduct quarterly audit where each category must have updated justification signed off by DPO or security lead

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________
**Metric Validation Date:** _________________________________
**Notes:** ___________________________________________

---

**Level 2 Score:** _____ / 3 questions answered "Implemented" or above

**Level 2 Achieved:** ☐ Yes (3/3 at Implemented or above) ☐ No (< 3/3)

---

## Level 3: Industry-Leading
**Objective:** Implement autonomous endpoint security operations, zero-trust endpoint architecture, predictive compromise detection, and contribute to open-source EDR tools

**Prerequisites:** ALL Level 2 questions must be "Implemented" or above to proceed to Level 3

### Question 7: Autonomous Endpoint Security and Self-Healing Architecture

**Q3.1:** Have you implemented autonomous endpoint security operations where AI detects and remediates endpoint issues autonomously (configuration drift auto-remediation, malware containment and cleanup, patch deployment for critical vulnerabilities) with self-healing capabilities that maintain security baselines without human intervention for ≥80% of routine security events?

**Evidence Required:**
- [ ] Autonomous Detection and Remediation:
  - AI autonomously handles ≥80% of routine endpoint security events without SOC intervention
  - Autonomous Actions: Malware quarantine, process termination, network isolation, configuration restoration
  - Confidence-Based Automation: High-confidence detections (≥95%) handled autonomously; lower confidence escalated to SOC
  - Mean Time to Remediate: ≤5 minutes for autonomous actions (vs ≤4 hours for human-handled)
- [ ] Self-Healing Endpoints:
  - Configuration Drift Detection: Continuous monitoring of endpoint security configuration against baseline
  - Auto-Remediation: Automatically restore configuration to approved baseline when drift detected
  - Patch Deployment: Autonomous deployment of critical security patches within defined SLA
  - Health Monitoring: Agent self-diagnostics with auto-recovery from common failure modes
  - Resilience: Agent survives reboot, service restart, and common tampering attempts
- [ ] Safety Controls for Autonomous Operations:
  - Blast radius limits maintained (cannot autonomously remediate >100 endpoints in 1 hour)
  - Override capability: SOC can halt autonomous actions at any time
  - Audit trail: Every autonomous action logged with full reasoning and evidence
  - Escalation: Automatic escalation for novel threats, repeated failures, or high-value endpoints
- [ ] Autonomous operation metrics tracked: Actions taken, success rate, false positive rate, escalation rate
- [ ] Monthly review of autonomous decision quality

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Autonomous endpoint security event handling rate | ___ | ___ | ≥80% of routine events handled without SOC intervention | ☐ | |
| Autonomous remediation MTTR | ___ | ___ | ≤5 minutes median | ☐ | |
| Configuration drift auto-remediation success rate | ___ | ___ | ≥95% of drift events auto-remediated successfully | ☐ | |
| Autonomous action false positive rate (requiring rollback) | ___ | ___ | ≤2% of autonomous actions reversed | ☐ | |

**Metric Collection Guidance:**
- **Autonomous endpoint security event handling rate**: EDR/SOAR incident database; formula = (endpoint security events fully resolved without SOC analyst ticket or approval / total endpoint security events in period) × 100; collect monthly; tag each event with resolution mode (autonomous, escalated, human-handled)
- **Autonomous remediation MTTR**: Autonomous action log; formula = median time in minutes from detection event to remediation confirmation for autonomously-handled endpoint events; collect monthly from EDR action timeline data
- **Configuration drift auto-remediation success rate**: Endpoint configuration management platform; formula = (configuration drift events where auto-remediation restored baseline successfully within 30 minutes / total configuration drift events detected) × 100; collect weekly from configuration compliance dashboard
- **Autonomous action false positive rate (requiring rollback)**: Autonomous action audit log + rollback event log; formula = (autonomous endpoint actions reversed due to false positive confirmation / total autonomous endpoint actions taken) × 100; collect monthly; each rollback event reviewed in monthly autonomous decision quality review

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________
**Metric Validation Date:** _________________________________
**Notes:** ___________________________________________

---

### Question 8: Zero-Trust Endpoint Architecture

**Q3.2:** Have you implemented zero-trust endpoint architecture where device posture is continuously assessed (patched, correctly configured, malware-free) before granting access, with micro-segmentation isolating each endpoint in its own network segment to prevent lateral movement, continuous device identity verification, and dynamic access policies based on real-time risk scoring?

**Evidence Required:**
- [ ] Continuous Device Posture Assessment:
  - Device Health Checks: Patch status, security configuration compliance, antimalware status, encryption status
  - Assessment Frequency: Continuous (not just at login/VPN connection)
  - Access Decisions: Only verified-healthy devices granted access to organizational resources
  - Remediation Guidance: Unhealthy devices receive automated remediation instructions or forced compliance actions
- [ ] Micro-Segmentation Architecture:
  - Each endpoint in isolated network segment (prevent lateral movement)
  - Application-Level Segmentation: Access granted per-application, not per-network
  - Dynamic Segmentation: Segment isolation level adjusted based on endpoint risk score
  - Lateral Movement Prevention: Even compromised endpoints cannot reach other endpoints directly
- [ ] Continuous Device Identity Verification:
  - Device certificates with hardware-bound keys (TPM-based attestation)
  - Multi-factor device authentication (device certificate + user authentication + posture check)
  - Device identity lifecycle management (enrollment, renewal, revocation)
- [ ] Dynamic Access Policies:
  - Real-Time Risk Scoring: Access policies adjust based on current endpoint risk score
  - Context-Aware Access: Location, network, time, user behavior influence access decisions
  - Step-Up Authentication: Higher-risk access requests require additional verification
  - Continuous Evaluation: Access can be revoked mid-session if endpoint posture degrades
- [ ] Zero-trust architecture integrated with identity provider (IdP) and SASE/SSE platforms
- [ ] Access decision latency ≤200ms (no noticeable user impact)

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Device posture assessment coverage (continuous vs point-in-time) | ___ | ___ | 100% of managed endpoints on continuous assessment | ☐ | |
| Access decision latency | ___ | ___ | ≤200ms (95th percentile) | ☐ | |
| Lateral movement success rate in adversarial testing (micro-segmentation efficacy) | ___ | ___ | 0% successful lateral movement between segmented endpoints | ☐ | |
| Device trust score compliance rate (only healthy devices granted access) | ___ | ___ | ≥99.5% of access grants to posture-verified devices only | ☐ | |

**Metric Collection Guidance:**
- **Device posture assessment coverage**: Zero-trust policy engine + endpoint management platform; formula = (managed endpoints enrolled in continuous posture assessment policy / total managed endpoints) × 100; audit monthly from zero-trust platform reporting console
- **Access decision latency**: Zero-trust policy engine performance logs; formula = 95th percentile time in milliseconds from access request received to access grant/deny decision returned; sample from policy engine telemetry, report monthly fleet-wide 95th percentile across all access decision types
- **Lateral movement success rate in adversarial testing**: Red team/penetration test reports; formula = (red team lateral movement attempts that successfully reached a second segmented endpoint / total lateral movement attempts executed) × 100; conduct at least annually; target is 0% (zero successful lateral movements)
- **Device trust score compliance rate**: Zero-trust access log; formula = (access grants where device posture score met minimum threshold at time of grant / total access grants in period) × 100; collect monthly from access decision audit log; any out-of-compliance grant is a finding requiring investigation

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________
**Metric Validation Date:** _________________________________
**Notes:** ___________________________________________

---

### Question 9: Open-Source Contribution and Continuous Architecture Evolution

**Q3.3:** Do you contribute to open-source EDR/endpoint security tools or research, participate in endpoint security community standards development, and maintain a continuous architecture improvement program incorporating lessons learned from adversarial testing, real-world endpoint incidents, and emerging research, with evidence of architecture evolution over time?

**Evidence Required:**
- [ ] Open-Source and Industry Contributions:
  - At least 2 contributions per year: open-source EDR detection rules, endpoint security tools, behavioral analytics libraries
  - Industry standards participation: MITRE ATT&CK endpoint contributions, detection engineering community, Sigma rule contributions
  - Published research: Blog posts, conference talks (Black Hat, DEF CON, BSides), or papers on AI endpoint security
  - Community engagement: Shared detection engineering methodologies, purple team frameworks, EDR tuning guides
- [ ] Continuous Architecture Evolution:
  - Documented process for updating endpoint security architecture based on:
    - Adversarial testing results (red team findings, EDR evasion testing, purple team exercises)
    - Real-world incidents (ransomware outbreaks, undetected APTs, false positive business disruptions)
    - Emerging research (adversarial ML techniques, new malware families, EDR bypass methods)
    - Vendor intelligence (EDR platform updates, newly identified detection gaps)
    - Technology evolution (new OS security features, new hardware security capabilities)
  - Historical record showing architecture evolution (12+ months)
  - Examples of architecture improvements triggered by operational experience:
    - Enhanced LOTL detection after behavioral bypass testing
    - Multi-layered defense improvements after ransomware simulation
    - Privacy architecture updates after regulatory changes
    - Agent performance optimization after fleet-wide analysis
- [ ] Feedback Loop: Threat intelligence → Architecture update → Testing → Deployment → Monitoring → Re-assess
- [ ] Metrics tracked: detection accuracy (precision, recall, F1), false positive/negative rates, performance impact, endpoint coverage, autonomous operation percentage, time-to-detection per attack phase

**Outcome Metrics:**
| Metric | Baseline | Current | Target | Met? | Notes |
|--------|----------|---------|--------|------|-------|
| Open-source or community contributions per year | ___ | ___ | ≥2 substantive contributions/year | ☐ | |
| Architecture improvement cycle time (red team finding to deployed fix) | ___ | ___ | ≤90 days from finding to verified deployment | ☐ | |
| Detection accuracy trend (F1 score, 12-month rolling) | ___ | ___ | Improving or stable (no decline >5% over 12 months) | ☐ | |
| Architecture evolution documentation completeness | ___ | ___ | 12+ months of documented architecture decisions with rationale | ☐ | |

**Metric Collection Guidance:**
- **Open-source or community contributions per year**: Contribution tracking log; formula = count of distinct substantive contributions (Sigma rules submitted, GitHub PRs merged to external EDR projects, ATT&CK technique submissions, conference presentations, published research) per calendar year; audit annually; each contribution must be externally verifiable (public URL or documented reference)
- **Architecture improvement cycle time**: Architecture change log + red team/purple team finding tracker; formula = median days from red team or purple team finding documented to architecture fix deployed and verified in production; track per finding from adversarial testing reports, calculate median quarterly
- **Detection accuracy trend (F1 score, 12-month rolling)**: Model evaluation pipeline; formula = monthly F1 score computed on consistent held-out test set for each detection category (malware, ransomware, fileless, LOTL, lateral movement); plot 12-month trend; flag any month with >5% decline for investigation; report quarterly
- **Architecture evolution documentation completeness**: Architecture decision record (ADR) system; formula = count of months in past 12 months with at least one documented architecture decision record (new decision, update, or deprecation) with business/security rationale; audit annually from ADR log; target is 12 of 12 months documented

**Answer:**
- ☐ **Fully Mature** (Evidence complete + ≥75% of metrics meet targets = ≥3 metrics met)
- ☐ **Implemented** (Evidence complete + 50-74% of metrics meet targets = 2 metrics met)
- ☐ **Partial** (Evidence complete + <50% metrics meet targets OR incomplete evidence)
- ☐ **Not Implemented** (No evidence)

**Evidence Location:** _________________________________
**Metric Validation Date:** _________________________________
**Notes:** ___________________________________________

---

**Level 3 Score:** _____ / 3 questions answered "Implemented" or above

**Level 3 Achieved:** ☐ Yes (3/3 at Implemented or above) ☐ No (< 3/3)

---

## Practice Score Calculation

### Question Scoring

```
Fully Mature    = 1.00 points
Implemented     = 0.67 points
Partial         = 0.33 points
Not Implemented = 0.00 points
```

### Level Scoring with Progression Rule

```
Level 1 Raw Score  = sum of Q1.1 + Q1.2 + Q1.3 scores (max 3.0)
Level 1 Normalized = Level 1 Raw Score / 3.0

Level 2 Raw Score  = sum of Q2.1 + Q2.2 + Q2.3 scores (max 3.0)
Level 2 Normalized = (Level 2 Raw Score / 3.0) × Level 1 Normalized

Level 3 Raw Score  = sum of Q3.1 + Q3.2 + Q3.3 scores (max 3.0)
Level 3 Normalized = (Level 3 Raw Score / 3.0) × Level 2 Normalized

Practice Score = Level 1 Normalized + Level 2 Normalized + Level 3 Normalized
```

### Practice Score Interpretation (max 3.0)

```
Level 0 (Score < 1.0):  Ad-hoc, no formal endpoint security architecture
Level 1 (Score 1.0–1.9): Foundational detection, agent, and response architecture
Level 2 (Score 2.0–2.9): Comprehensive behavioral analytics, hunting, and privacy architecture
Level 3 (Score 3.0):     Industry-leading autonomous operations and zero-trust endpoint architecture
```

### Simplified Scoring (Recommended for Internal Use)

```
Level 1 Achieved (all 3 at "Implemented" or above): 1.0 point
Level 2 Achieved (all 3 at "Implemented" or above): +1.0 point (total 2.0)
Level 3 Achieved (all 3 at "Implemented" or above): +1.0 point (total 3.0)
```

**SA-Endpoints Practice Score:** _______ / 3.0

---

## Assessment Summary

**Assessment Date:** _________________________________

**Assessor(s):** _____________________________________

**HAI System(s) Assessed:** __________________________

**Overall Maturity Level:**
- ☐ Level 0 (Score < 1.0): Ad-hoc, no formal endpoint security architecture
- ☐ Level 1 (Score 1.0 - 1.9): Foundational detection, agent, and response architecture
- ☐ Level 2 (Score 2.0 - 2.9): Comprehensive behavioral analytics, hunting, and privacy architecture
- ☐ Level 3 (Score 3.0): Industry-leading autonomous operations and zero-trust endpoint architecture

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

## Secure Architecture Endpoint-Specific Notes

**Architecture Components Covered:**
- [ ] Hybrid detection architecture (signature + heuristic + ML + ensemble)
- [ ] On-device vs cloud analysis decision architecture
- [ ] Model specialization (ransomware, fileless, lateral movement, insider threat)
- [ ] Lightweight endpoint agent (sensor, local AI, response, communication)
- [ ] Privacy-preserving telemetry (data minimization, differential privacy, BYOD separation)
- [ ] Centralized analysis (stream processing, cross-endpoint correlation, threat intelligence)
- [ ] Safe automated response (tiered levels, blast radius limits, safety guardrails)
- [ ] Cross-platform support (Windows, macOS, Linux, mobile with unified detection logic)
- [ ] Behavioral analytics / UEBA (baselining, anomaly detection, context-aware scoring)
- [ ] Memory forensics (in-memory threats, rootkits, DLL injection, reflective loading)
- [ ] Living-off-the-Land detection (legitimate tool abuse, ML command-line analysis)
- [ ] Automated threat hunting (hypothesis-driven, continuous queries, retrospective analysis)
- [ ] Predictive endpoint security (risk factor analysis, proactive hardening)
- [ ] Federated learning (distributed training, secure aggregation, privacy guarantees)
- [ ] Autonomous operations (self-healing, auto-remediation, confidence-based automation)
- [ ] Zero-trust endpoint (continuous posture, micro-segmentation, dynamic access policies)

**Endpoint Performance Requirements:**
- [ ] Agent CPU: ≤5% average (95th percentile)
- [ ] Agent Memory: ≤200 MB resident
- [ ] Agent Battery Impact: ≤3% on laptops/mobile
- [ ] On-Device Detection: ≤1 second latency
- [ ] Cloud Detection: Higher accuracy with network dependency
- [ ] Ransomware Response: Detect and isolate ≤60 seconds
- [ ] Zero-Trust Access Decision: ≤200ms latency
- [ ] Autonomous Remediation: ≤5 minutes MTTR

**Platform Coverage:**
- [ ] Windows (C++/Rust agent, Windows hooks, ETW)
- [ ] macOS (Endpoint Security Framework, System Integrity Protection compliance)
- [ ] Linux (multi-distro support, eBPF-based monitoring)
- [ ] Mobile iOS (MDM integration, app sandboxing constraints)
- [ ] Mobile Android (device admin, Work Profile support)
- [ ] IoT/resource-constrained endpoints (lightweight monitoring)
- [ ] Unified detection logic: YARA, Sigma rules with platform-specific implementations

**Privacy Architecture:**
- [ ] GDPR compliance (≤90 day retention, right to access, right to deletion)
- [ ] BYOD work/personal separation with user consent
- [ ] Federated learning for privacy-preserving model training
- [ ] Differential privacy for aggregate telemetry
- [ ] Privacy impact assessment completed
- [ ] DPO review (if applicable)

---

**Document Version:** 3.0
**Last Updated:** 2026-02-19
**Next Review:** Quarterly or after significant HAI endpoint security changes
