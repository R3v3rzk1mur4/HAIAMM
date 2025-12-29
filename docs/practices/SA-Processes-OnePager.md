# Security Architecture Practice – Processes Domain
## HAIAMM v2.1 One-Pager

### Practice Overview

The Security Architecture (SA) practice for the Processes domain defines the architectural design for AI-powered security orchestration, automation, and response (SOAR) systems. This practice establishes how AI security process automation should be architected to achieve security requirements while maintaining safety, reliability, and human oversight.

**Scope**: Architecture for:
- **AI Model Architecture**: Models for alert triage, incident analysis, and response recommendation
- **Orchestration Architecture**: Multi-tool workflow orchestration and automation
- **Incident Response Architecture**: Automated investigation and containment workflows
- **Integration Architecture**: Integration with security tools (SIEM, EDR, firewall, cloud, etc.)
- **Safety Architecture**: Blast radius limits, rollback capabilities, and human oversight
- **Scalability Architecture**: Handle thousands of alerts/incidents per day
- **Resilience Architecture**: Graceful degradation when AI or tools fail

**Why This Matters**: Process automation AI operates in high-stakes, time-sensitive environments where errors can cause business disruption (e.g., AI blocks wrong network segment, disables wrong accounts). Architecture must balance automation speed (rapid response) with safety (prevent AI-caused outages), autonomy (minimal human intervention) with oversight (human final authority), and efficiency (handle high volumes) with reliability (no missed critical incidents).

---

### Practice Maturity Levels

## Level 1: Foundational Architecture

### Core Objectives
1. Design AI models for alert triage and incident classification
2. Implement orchestration engine architecture for automated workflows
3. Establish safety architecture with blast radius limits
4. Deploy integration architecture for security tool ecosystem
5. Implement human oversight architecture for high-risk actions
6. Design monitoring architecture for SOAR health and performance

### Key Activities

#### 1. AI Model Architecture for Security Operations

**Alert Triage Models**:
- **Classification**: ML models classify alerts as true positive, false positive, or requires investigation
  - Input: Alert metadata (source, severity, affected assets, indicators)
  - Output: Classification + confidence score + priority
  - Accuracy Target: ≥95% true positive detection, ≥70% precision

- **Severity Scoring**: AI adjusts alert severity based on context
  - Example: Port scan from internal IP = Low; Port scan from known attacker IP = Critical

**Incident Analysis Models**:
- **Root Cause Analysis**: NLP models analyze logs, events to identify incident root cause
- **Scope Assessment**: Graph models trace incident impact across systems
- **Attack Chain Reconstruction**: Sequence models reconstruct multi-stage attacks

**Response Recommendation Models**:
- **Action Selection**: Reinforcement learning recommends optimal response actions
  - Trained on historical incidents: What actions led to fastest containment?
- **Risk Assessment**: Predict business impact of proposed response actions

#### 2. Orchestration Engine Architecture

**Workflow Engine**:
- **Playbook Execution**: Execute automated incident response playbooks
  - Playbooks defined as DAGs (Directed Acyclic Graphs): Step 1 → Step 2 → Step 3
  - Conditional logic: If malware detected, goto remediation; else goto false positive handling

- **Multi-Tool Orchestration**: Coordinate actions across security tools
  - Example Playbook: (1) Query SIEM for related alerts, (2) Pull endpoint telemetry from EDR, (3) Block malicious IP at firewall, (4) Isolate endpoint, (5) Create ticket

**Execution Architecture**:
- **Asynchronous Execution**: Non-blocking task execution (don't wait for slow tools)
- **Parallel Execution**: Execute independent tasks in parallel (query SIEM and EDR simultaneously)
- **Timeout Handling**: Fail gracefully if tool takes too long (don't hang indefinitely)
- **Retry Logic**: Retry failed actions with exponential backoff

**State Management**:
- **Workflow State**: Track workflow progress (which steps completed, which failed)
- **Incident State**: Track incident lifecycle (new → investigating → contained → resolved)
- **Persistence**: State persisted to database (survive service restarts)

#### 3. Safety Architecture

**Graduated Automation Levels**:
- **Level 0 - Alert Only**: AI detects issue, alerts human, human acts
- **Level 1 - Recommend**: AI recommends actions, human approves and executes
- **Level 2 - Auto-Execute (Reversible)**: AI executes reversible actions (disable account, quarantine email)
- **Level 3 - Auto-Execute (Irreversible)**: AI executes irreversible actions (delete malware, wipe device)

**Blast Radius Limits**:
- **Network Changes**: AI cannot block >50 IPs or >5 subnets in single action
- **Account Changes**: AI cannot disable >20 accounts in single action
- **System Changes**: AI cannot isolate >5 production servers in single action

**Change Validation & Rollback**:
- **Pre-Change Validation**: Simulate change impact before execution
  - Example: "Blocking this IP will affect 0 legitimate users, 1 suspected attacker"
- **Post-Change Validation**: Verify change successful
- **Automated Rollback**: If change causes issues, auto-rollback
  - Example: Account disable → User complains → SOC reviews → Rollback (re-enable account)

**Human Approval Workflow**:
- **High-Risk Actions**: Require human approval
  - Actions affecting >10 systems, irreversible actions, production network changes
- **Approval SLA**: Approvals answered within ≤30 minutes (on-call escalation if no response)

#### 4. Integration Architecture

**Security Tool Integration**:
- **API Integration**: REST APIs for programmatic tool control
  - Covered Tools: SIEM (Splunk, QRadar), EDR (CrowdStrike, SentinelOne), Firewall (Palo Alto, Fortinet), Cloud (AWS, Azure, GCP), Ticketing (Jira, ServiceNow)

- **Integration Patterns**:
  - **Query Pattern**: Fetch data from tool (logs, alerts, configurations)
  - **Action Pattern**: Execute action via tool (block IP, disable account, isolate endpoint)
  - **Webhook Pattern**: Tool pushes events to SOAR (real-time alerts)

**Integration Reliability**:
- **Error Handling**: Graceful handling of API failures (tool down, rate limiting, timeout)
- **Retry Strategy**: Exponential backoff with jitter
- **Circuit Breaker**: If tool consistently fails, stop attempting (prevent cascading failures)

**Data Normalization**:
- **Common Schema**: Normalize data from diverse tools into common schema (OCSF, ECS)
  - Challenge: Each tool uses different field names (source_ip vs src_ip vs sourceIP)
  - Solution: Mapping layer converts tool-specific formats to common schema

#### 5. Human Oversight Architecture

**Human-in-the-Loop Workflows**:
- **Approval Checkpoints**: Workflows pause at critical steps for human approval
  - Example: AI investigates incident, gathers evidence → Human reviews → Approves containment → AI executes

- **Spot-Check Auditing**: Random sampling of AI autonomous actions for quality validation
  - Sample: ≥10% of autonomous actions reviewed by humans within 24 hours

**Escalation Architecture**:
- **Tiered Escalation**: Incident severity determines escalation path
  - Low: Tier 1 analyst handles autonomously
  - Medium: Escalate to Tier 2 analyst for approval
  - High: Escalate to SOC manager + on-call engineer
  - Critical: Escalate to CISO + incident commander

- **Escalation Timeout**: If human doesn't respond within SLA, escalate to next tier or take conservative action

**Override Mechanism**:
- **Analyst Override**: Security analysts can override AI decisions at any time
  - Override triggers: Review AI decision, provide justification, execute alternative action
  - Logging: All overrides logged for AI training

#### 6. Monitoring & Observability Architecture

**SOAR Health Monitoring**:
- **Infrastructure**: Service availability, API latency, queue depth, error rates
- **AI Model Performance**: Triage accuracy, false positive rate, confidence distribution
- **Integration Health**: Tool API success rates, response times

**Incident Metrics Dashboard**:
- **Volume**: Incidents handled, alerts processed
- **Performance**: Mean time to detect (MTTD), mean time to respond (MTTR)
- **Accuracy**: False positive rate, true positive rate (validated via human review)

**Alerting**:
- **P0 (Critical)**: SOAR down, incident spike >5x normal, model accuracy drops >20%
- **P1 (High)**: Integration failure, queue backlog >100 incidents, model accuracy drops >10%

---

### Key Success Indicators

**Outcome Metrics**:
1. **Incident Response Speed**: MTTR ≤10 hours (≥60% improvement vs manual)
2. **Automation Rate**: ≥70% of incidents handled autonomously or semi-autonomously
3. **Safety**: Zero production outages caused by AI automation
4. **Accuracy**: ≥95% true positive detection, ≥70% precision in alert triage
5. **Reliability**: ≥99% SOAR platform uptime

**Process Metrics**:
1. **Alert Reduction**: ≥70% reduction in alerts requiring human investigation (via de-duplication, auto-resolution)
2. **Playbook Coverage**: ≥80% of common incident types covered by automated playbooks
3. **Integration Coverage**: Integrated with ≥80% of organization's security tools

---

## Level 2: Comprehensive Architecture

### Core Objectives
1. Implement adaptive playbooks that learn and evolve
2. Design cross-domain orchestration architecture
3. Establish advanced behavioral analytics for incident detection
4. Implement real-time feedback loop architecture
5. Design multi-stage attack detection architecture

### Key Activities

#### 1. Adaptive Playbook Architecture

**Playbook Learning**:
- Analyze incident outcomes: Which playbooks led to fastest resolution?
- A/B testing: Test playbook variations, adopt best-performing
- Automatic optimization: AI adjusts playbook parameters based on outcomes

#### 2. Cross-Domain Orchestration

**Coordinated Response**:
- Orchestrate actions across domains (endpoint + network + identity + cloud)
- Example: Ransomware response → Isolate endpoints (EDR) + Block C2 (firewall) + Disable accounts (AD) + Snapshot cloud VMs (AWS)

---

## Level 3: Industry-Leading Architecture

### Core Objectives
1. Implement autonomous security operations (≥80% automation)
2. Design self-healing SOAR architecture
3. Establish predictive incident prevention
4. Contribute to open-source SOAR platforms
5. Achieve zero-trust SOAR architecture

### Key Activities

#### 1. Autonomous Security Operations

**Full Lifecycle Automation**:
- AI handles detection → triage → investigation → containment → eradication → recovery autonomously for routine incidents

#### 2. Predictive Incident Prevention

**Incident Forecasting**:
- Predict which incident types likely in next 30 days
- Proactive hardening before incidents occur

---

## Practice Integration

**Threat Assessment (TA)**: TA identifies process automation threats → SA designs resilient architecture
**Security Requirements (SR)**: SR defines automation accuracy → SA implements models to achieve
**Incident Response (IR)**: IR defines processes → SA implements automated workflows

---

## Conclusion

Processes SA practice provides architectural guidance for AI-powered security orchestration and automation. Level 1 establishes foundational triage, orchestration, safety, and integration. Level 2 adds adaptive playbooks and cross-domain orchestration. Level 3 achieves autonomous operations and predictive prevention.

---

**Document Information**:
- **Practice**: Security Architecture (SA)
- **Domain**: Processes
- **HAIAMM Version**: 2.1
- **Maturity Levels**: 3 (Foundational, Comprehensive, Industry-Leading)
- **Last Updated**: 2025-12-25
