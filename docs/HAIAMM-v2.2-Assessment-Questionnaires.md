# HAIAMM v2.2 Assessment Questionnaires
## Critical Human Assisted Intelligence Assurance Risks

**Version:** 1.0
**Date:** 2026-01-02
**Purpose:** Assessment questions for 4 critical HAI assurance gaps

---

## Overview

This document provides assessment questionnaires for:

1. **Excessive Agency (EA)** - Questions for Processes domain
2. **Agent Goal Hijack (AGH)** - Questions for Processes/Software domains
3. **Tool Misuse (TM)** - Questions for Processes/Software domains
4. **Rogue Agents (RA)** - Questions for Processes domain

Each questionnaire follows HAIAMM's assessment format:
- **Question**: Measurable, verifiable criteria
- **Verification**: How to verify the answer
- **Evidence**: Documentation required for "Yes"
- **Scoring**: Yes/Partial/No criteria

---

# 1. EXCESSIVE AGENCY (EA) - Processes Domain

## Level 1 Foundational Questions

### EA-PROC-L1-Q1: Least Agency Principle
**Question:** Do you apply the "Least Agency Principle" by granting agents only the minimum autonomy required for their tasks?

**Verification:**
- Review agent permission configurations and scopes
- Examine agent role definitions and access control lists
- Interview team leads on agent permission scoping process
- Audit agent actions to verify they stay within assigned scope

**Evidence:**
- Agent permission documentation showing scoped access (not blanket admin)
- Role-based access control (RBAC) policies for agents
- Examples of agents denied actions outside their scope
- Permission review process (quarterly scope audits)

**Scoring:**
- **Yes if**: All agents have documented permission scopes; permissions limited to minimum required; agents cannot exceed scope; quarterly reviews conducted
- **Partial if**: Most agents scoped but some have overly broad permissions; reviews conducted but less frequently than quarterly
- **No if**: Agents have blanket permissions (admin access, unrestricted); no documented scopes; no permission reviews

---

### EA-PROC-L1-Q2: Action Classification Framework
**Question:** Do you classify agent actions into Autonomous (Green), Human-Validated (Yellow), and Human-Only (Red) categories?

**Verification:**
- Review action classification documentation for each agent
- Examine approval workflows for Human-Validated actions
- Test that Human-Only actions are blocked when attempted by agents
- Verify Autonomous actions proceed without approval

**Evidence:**
- Action classification matrix (which actions are Green/Yellow/Red per agent)
- Approval workflow documentation and logs
- Examples of Human-Validated actions requiring approval
- Examples of Human-Only actions blocked when agent attempts

**Scoring:**
- **Yes if**: All agent action types classified; Human-Validated actions require approval; Human-Only actions blocked; Autonomous actions proceed independently
- **Partial if**: Classification exists but incomplete; some high-risk actions lack approval gates; inconsistent enforcement
- **No if**: No action classification; agents can perform any action without approval; no distinction between autonomous and high-risk actions

---

### EA-PROC-L1-Q3: High-Risk Action Approval Gates
**Question:** Do high-risk agent actions (data deletion, production deployment, financial transactions, external communications) require explicit human approval before execution?

**Verification:**
- Test destructive actions (attempt agent data deletion without approval)
- Review production deployment logs for approval records
- Examine external communication logs for approval gates
- Verify approval workflow provides sufficient context for decision

**Evidence:**
- Approval workflow implementation (tickets, dashboards showing pending approvals)
- Approval logs showing human decisions for high-risk actions
- Examples of high-risk actions blocked pending approval
- Approval context documentation (what/why/impact shown to approver)

**Scoring:**
- **Yes if**: ≥95% of high-risk actions require approval; approval workflows provide context; blocked actions logged; no unapproved high-risk actions executed
- **Partial if**: Approval gates exist but <95% coverage; some high-risk actions slip through; approval context insufficient for informed decision
- **No if**: No approval gates; agents can execute high-risk actions autonomously; no approval logs

---

### EA-PROC-L1-Q4: Agent Privilege Inheritance
**Question:** Do agents inherit their operator's privileges (or subset), never exceeding the operator's authorization level?

**Verification:**
- Test confused deputy scenarios (junior developer using agent to perform senior-only action)
- Review agent permission configuration vs. operator permissions
- Examine audit logs for privilege escalation attempts via agents
- Verify agents cannot grant themselves additional privileges

**Evidence:**
- Agent privilege inheritance policy documentation
- Examples of agents denied actions operator cannot perform
- Audit logs showing privilege escalation attempts blocked
- Configuration showing agent permissions ≤ operator permissions

**Scoring:**
- **Yes if**: Agent permissions always ≤ operator permissions; junior operator's agent cannot perform senior actions; privilege escalation attempts blocked and logged
- **Partial if**: Inheritance generally enforced but exceptions exist; some agents have elevated privileges; escalation detection incomplete
- **No if**: Agents have higher privileges than operators; junior operators can use agents to bypass approval requirements; no privilege inheritance controls

---

### EA-PROC-L1-Q5: Autonomy Level Documentation
**Question:** Are agent autonomy levels explicitly documented, including which actions are Autonomous/Validated/Prohibited, and reviewed at least quarterly?

**Verification:**
- Review autonomy level documentation for each agent
- Check documentation date and review schedule (quarterly)
- Interview operators on awareness of autonomy levels
- Verify documentation matches actual agent behavior

**Evidence:**
- Agent autonomy documentation (per-agent action classifications)
- Quarterly review schedule and records
- Updated documentation after each review
- Operator training materials on agent autonomy levels

**Scoring:**
- **Yes if**: All agents have documented autonomy levels; documentation up-to-date; quarterly reviews conducted; operators aware of boundaries
- **Partial if**: Documentation exists but outdated; reviews conducted but less than quarterly; incomplete agent coverage
- **No if**: No autonomy documentation; operators unaware of agent boundaries; no reviews conducted

---

### EA-PROC-L1-Q6: Approval Workflow Performance
**Question:** Do approval workflows for Human-Validated actions complete within acceptable latency (≤2 minutes for 90% of approvals)?

**Verification:**
- Measure approval latency from agent proposal to human decision
- Review approval timeout handling (auto-reject after 30 minutes)
- Examine approval interface usability and context provision
- Check approval metrics dashboard

**Evidence:**
- Approval latency metrics (median, 90th percentile, 99th percentile)
- Approval timeout logs and auto-reject records
- Screenshots of approval interface showing context provided
- User feedback on approval process

**Scoring:**
- **Yes if**: 90% of approvals complete ≤2 minutes; 99% ≤10 minutes; timeouts configured (30 min auto-reject); approval interface provides sufficient context
- **Partial if**: Latency higher (>2 min median); timeouts missing or too long; approval context incomplete; user complaints about approval process
- **No if**: No latency tracking; approvals take hours/days; no timeouts (indefinite pending); approval interface lacks context

---

### EA-PROC-L1-Q7: Excessive Agency Monitoring
**Question:** Do you monitor agent permission usage, approval gate compliance, and privilege escalation attempts?

**Verification:**
- Review monitoring dashboards for agent permissions
- Examine logs of privilege escalation attempts
- Check approval bypass detection alerts
- Verify autonomy drift monitoring (agents expanding scope over time)

**Evidence:**
- Permission usage monitoring dashboards
- Privilege escalation attempt logs (denied actions outside scope)
- Approval bypass alerts (Human-Validated action executed without approval)
- Autonomy drift reports (% autonomous actions over time)

**Scoring:**
- **Yes if**: Real-time monitoring of permissions, approvals, escalations; alerts configured for violations; dashboards available; baseline tracking for autonomy drift
- **Partial if**: Monitoring exists but not real-time; alerts incomplete; no autonomy drift tracking; manual reviews only
- **No if**: No monitoring; privilege escalation attempts not logged; approval bypasses undetected; no visibility into agent autonomy

---

### EA-PROC-L1-Q8: Regulated Decision Human Control
**Question:** Are regulated decisions (GDPR, HIPAA, SOX, compliance decisions) classified as Human-Only (Red), with agents prohibited from making final decisions?

**Verification:**
- Review compliance decision workflows (GDPR DSARs, HIPAA access requests, SOX financial approvals)
- Test that agents cannot complete regulated decisions autonomously
- Examine audit logs for human approval of all regulated decisions
- Verify compliance team awareness of human-only requirements

**Evidence:**
- Regulated decision classification (list of Human-Only compliance decisions)
- Audit logs showing human approval for all regulated decisions
- Examples of agents blocked from completing regulated decisions
- Compliance team training on AI assistant limitations

**Scoring:**
- **Yes if**: All regulated decisions classified Human-Only; 100% require human final approval; agents can assist (research, draft) but not decide; audit trail clear
- **Partial if**: Most regulated decisions require approval but exceptions exist; some agents can complete low-risk compliance decisions; audit trail incomplete
- **No if**: Agents can make regulated decisions autonomously; no differentiation for compliance; no audit trail of human approval

---

## Level 2 Comprehensive Questions

### EA-PROC-L2-Q1: Dynamic Permission Adjustment
**Question:** Do you automatically adjust agent permissions based on observed behavior, risk level, and changing business context?

**Verification:**
- Review dynamic permission adjustment algorithms
- Examine examples of permissions downgraded due to risky behavior
- Verify permissions escalate/de-escalate based on business context (e.g., higher permissions during business hours, lower after-hours)
- Check permission adjustment audit logs

**Evidence:**
- Dynamic permission policy documentation
- Examples of automatic permission downgrades (e.g., agent flagged for anomaly, permissions reduced)
- Context-based permission rules (time-of-day, data sensitivity, operator role)
- Audit logs of permission adjustments with justifications

**Scoring:**
- **Yes if**: Permissions adjust dynamically; risky behavior triggers automatic downgrade; context-aware rules active; all adjustments logged and auditable
- **Partial if**: Some dynamic adjustments but limited scope; manual permission changes only; context rules incomplete
- **No if**: Static permissions only; no automatic adjustments; risky behavior doesn't affect permissions

---

### EA-PROC-L2-Q2: Approval Gate Effectiveness Metrics
**Question:** Do you track approval gate effectiveness metrics (approval rate, rejection reasons, timeout rate) and optimize gates based on data?

**Verification:**
- Review approval metrics dashboard (approval rate, average latency, timeout rate, rejection reasons)
- Examine analysis of rejection patterns (why are actions rejected?)
- Verify gate optimization based on metrics (e.g., reduce approvals for consistently-approved low-risk actions)
- Check quarterly approval gate reviews

**Evidence:**
- Approval metrics dashboard (real-time visibility into approval performance)
- Approval rate analysis (% approved vs. rejected, by action type)
- Rejection reason categorization (security concern, business policy, insufficient context)
- Gate optimization examples (rules adjusted based on approval patterns)

**Scoring:**
- **Yes if**: Comprehensive metrics tracked; data analyzed quarterly; gates optimized based on patterns; rejection reasons categorized and actionable
- **Partial if**: Basic metrics (approval count) but limited analysis; infrequent optimization; rejection reasons not categorized
- **No if**: No approval metrics; gates never reviewed or optimized; approval process static

---

# 2. AGENT GOAL HIJACK (AGH) - Processes/Software Domains

## Level 1 Foundational Questions

### AGH-PROC-L1-Q1: Goal Validation Before Execution
**Question:** Do agents validate their current goal against the intended objective before executing actions?

**Verification:**
- Review agent code/configuration for pre-execution goal validation
- Test that agents with modified goals (via prompt injection) fail validation
- Examine validation logs showing goal checks before each action
- Verify validation latency ≤100ms (doesn't impact performance)

**Evidence:**
- Goal validation implementation (code, configuration showing validation logic)
- Validation logs (pre-action goal checks with pass/fail results)
- Test results showing modified goals rejected
- Performance metrics (validation latency)

**Scoring:**
- **Yes if**: 100% of actions validated against intended goal before execution; validation latency ≤100ms; modified goals rejected and logged
- **Partial if**: Validation exists but incomplete coverage (<100% actions); latency >100ms; some modified goals slip through
- **No if**: No pre-execution goal validation; agents can act on hijacked goals; no validation logs

---

### AGH-PROC-L1-Q2: Goal State Change Logging
**Question:** Do you log all agent goal state changes with immutable audit trails, and alert on any unauthorized modifications?

**Verification:**
- Review goal state audit logs (initialization, modifications, validation results)
- Verify log immutability (append-only, tamper-evident)
- Test that goal modifications trigger CRITICAL alerts
- Check logs include goal change trigger (prompt, memory, configuration update)

**Evidence:**
- Immutable goal state audit logs
- Goal modification alerts (CRITICAL severity for any goal change)
- Log entries showing goal initialization, changes, validation events
- Alert configurations for goal modifications

**Scoring:**
- **Yes if**: All goal changes logged immutably; CRITICAL alerts on modifications; logs include trigger/justification; append-only storage prevents tampering
- **Partial if**: Goal logging exists but not immutable; alerts incomplete; some goal changes not logged; manual review required
- **No if**: No goal state logging; modifications not alerted; logs can be modified; no audit trail

---

### AGH-PROC-L1-Q3: Multi-Turn Goal Consistency
**Question:** Do you validate goal consistency across multi-turn agent conversations, detecting drift between conversation start and current turn?

**Verification:**
- Review conversation goal tracking implementation
- Test multi-turn prompt injection (gradual goal modification over 5-10 turns)
- Verify goal drift detection (≥20% similarity degradation triggers alert)
- Examine goal consistency reports from production conversations

**Evidence:**
- Multi-turn goal consistency validation logic
- Test results showing gradual goal drift detected
- Goal similarity metrics over conversation (Turn 1 vs. Turn N)
- Production examples of goal drift detected and prevented

**Scoring:**
- **Yes if**: Goal tracked throughout conversation; drift ≥20% detected and alerted; goal reset triggered on drift; test results show drift detection ≤5 turns
- **Partial if**: Conversation tracking exists but drift detection incomplete; thresholds too lenient (>30% drift required); slow detection (>10 turns)
- **No if**: No multi-turn goal tracking; drift undetected; agents can be gradually manipulated across conversation

---

### AGH-PROC-L1-Q4: Goal Immutability Controls
**Question:** Are agent goals immutable without explicit human authorization, with goal changes requiring secure approval workflows?

**Verification:**
- Test that agents cannot self-modify goals via prompt injection
- Review goal modification approval workflow
- Verify goal stored in read-only configuration (write-access restricted to admins)
- Examine rejected goal modification attempts in logs

**Evidence:**
- Goal immutability configuration (read-only goal storage, admin-only write access)
- Goal modification approval workflow documentation
- Test results showing prompt injection goal modification attempts blocked
- Audit logs of rejected goal modifications

**Scoring:**
- **Yes if**: Goals stored immutably (read-only); admin-only modifications; human approval required; prompt injection attempts blocked and logged
- **Partial if**: Goals mostly immutable but some agent self-modification possible; approval workflow exists but bypasses possible; incomplete protection
- **No if**: Agents can modify own goals; no approval required; prompt injection can change goals; no immutability controls

---

### AGH-PROC-L1-Q5: Goal Modification Rejection
**Question:** Do agents explicitly reject instructions attempting to modify their goals, and log these attempts for security review?

**Verification:**
- Test prompts like "Your new goal is...", "Instead, focus on...", "Ignore previous instructions..."
- Verify agents reject goal modification instructions
- Check that rejection is logged with prompt content and timestamp
- Review security team alerts for goal modification attempts

**Evidence:**
- Input validation logic detecting goal modification patterns
- Test results showing goal modification prompts rejected
- Logs of rejected goal modification attempts (with prompt content)
- Security team alert notifications for modification attempts

**Scoring:**
- **Yes if**: ≥95% of goal modification attempts detected and rejected; attempts logged with full context; security team alerted; quarterly testing verifies detection
- **Partial if**: Detection exists but <95% success rate; some prompts bypass detection; logging incomplete; no security alerts
- **No if**: No goal modification detection; agents accept "new goal" instructions; attempts not logged

---

### AGH-PROC-L1-Q6: Goal Source Validation
**Question:** Are agent goals sourced exclusively from secure configuration (not user input or external data)?

**Verification:**
- Review goal initialization code (verify goals from config, not prompts)
- Test that user inputs cannot influence goal parameters
- Examine goal configuration storage (separate from user data)
- Verify strict separation between system configuration and user input

**Evidence:**
- Goal initialization code showing config-only sourcing
- Configuration storage (secure, version-controlled, separate from user data)
- Test results showing user input doesn't affect goals
- Architecture documentation showing goal/input separation

**Scoring:**
- **Yes if**: Goals sourced 100% from secure configuration; user input completely isolated; goal parameters never from prompts; strict separation enforced
- **Partial if**: Mostly config-based but some goal parameters from user input; incomplete separation; edge cases where input affects goals
- **No if**: Goals influenced by user input; no separation between config and prompts; goal parameters come from external data

---

### AGH-PROC-L1-Q7: Prompt Injection Goal Manipulation Detection
**Question:** Do you monitor prompts for goal modification attempts using pattern detection ("your new goal", "instead focus on", "ignore previous instructions")?

**Verification:**
- Review prompt monitoring configuration (patterns detected)
- Test known goal manipulation prompts against detection
- Verify detection triggers alerts and blocks prompt
- Examine false positive rate (legitimate prompts flagged incorrectly)

**Evidence:**
- Prompt monitoring pattern library (regex, ML-based detection)
- Test results showing manipulation prompts detected
- Detection alerts and blocked prompt logs
- False positive analysis (≤1% target)

**Scoring:**
- **Yes if**: ≥95% of goal manipulation prompts detected; real-time blocking; alerts generated; ≤1% false positive rate
- **Partial if**: Detection exists but <95% success rate; delayed detection (not real-time); high false positives (>5%); incomplete pattern coverage
- **No if**: No prompt monitoring for goal manipulation; attempts go undetected; no blocking or alerts

---

### AGH-PROC-L1-Q8: Memory-Based Goal Persistence Validation
**Question:** If agents use persistent memory, do you validate goals stored in memory against authorized configuration with daily integrity checks?

**Verification:**
- Review persistent memory architecture (where goals stored)
- Examine integrity check implementation (checksums, digital signatures)
- Verify daily validation schedule and alerts on integrity failures
- Test that corrupted memory goals are detected and rejected

**Evidence:**
- Memory integrity validation implementation (daily scheduled checks)
- Integrity check logs (pass/fail results, checksums)
- Examples of corrupted memory detected and rejected
- Memory restore procedures (fallback to authorized configuration)

**Scoring:**
- **Yes if**: Daily integrity checks on memory-stored goals; checksums/signatures validated; corrupted goals detected and rejected; automatic restore from config
- **Partial if**: Integrity checks exist but less frequent than daily; validation incomplete; manual remediation required; no automatic restore
- **No if**: No memory integrity validation; corrupted goals persist undetected; no checksums or validation

---

## Level 2 Comprehensive Questions

### AGH-PROC-L2-Q1: AI-Powered Goal Drift Detection
**Question:** Do you use machine learning to detect subtle goal drift patterns that static rules might miss?

**Verification:**
- Review ML-based goal drift detection model
- Examine training data (normal vs. drifted goal examples)
- Test model against subtle drift scenarios (small incremental changes)
- Verify model accuracy metrics (≥90% detection, ≤5% false positives)

**Evidence:**
- Goal drift detection model documentation (architecture, training)
- Model performance metrics (precision, recall, F1-score)
- Test results on subtle drift scenarios
- Production deployment and monitoring

**Scoring:**
- **Yes if**: ML model deployed; ≥90% detection accuracy; ≤5% false positives; detects subtle drift static rules miss; quarterly model retraining
- **Partial if**: ML model exists but lower accuracy (<85%); high false positives (>10%); infrequent retraining; limited subtle drift detection
- **No if**: No ML-based detection; static rules only; subtle drift goes undetected

---

# 3. TOOL MISUSE (TM) - Processes/Software Domains

## Level 1 Foundational Questions

### TM-PROC-L1-Q1: Tool Intent Validation
**Question:** Do you validate that agent tool calls align with legitimate business purpose (not just parameter validation)?

**Verification:**
- Review intent validation logic (checks tool call against agent goal and context)
- Test suspicious tool calls (e.g., code reviewer calling delete_database)
- Verify intent mismatches are blocked and logged
- Examine intent validation performance (≤200ms latency)

**Evidence:**
- Intent validation implementation (goal/context/tool alignment checks)
- Test results showing inappropriate tool calls blocked
- Intent validation logs (approved/rejected with reasons)
- Performance metrics (validation latency)

**Scoring:**
- **Yes if**: 100% of tool calls validated for intent; inappropriate uses blocked; validation latency ≤200ms; validation logs include reasoning
- **Partial if**: Intent validation exists but incomplete coverage; high latency (>500ms); some inappropriate uses slip through; limited logging
- **No if**: No intent validation; only parameter validation; agents can use any authorized tool regardless of appropriateness

---

### TM-PROC-L1-Q2: Destructive Tool Approval Gates
**Question:** Do destructive tool calls (delete, drop, remove, terminate) require explicit human approval before execution?

**Verification:**
- Test destructive operations without approval (should be blocked)
- Review approval workflow for destructive tools
- Verify approval interface shows what/why/impact/reversibility
- Examine logs for unapproved destructive operations (should be zero)

**Evidence:**
- Destructive tool list and approval requirements
- Approval workflow implementation (pre-execution gates)
- Approval interface screenshots (context provided to human)
- Audit logs showing 100% approval compliance for destructive operations

**Scoring:**
- **Yes if**: 100% of destructive operations require approval; approval workflow provides context; zero unapproved destructive operations; reversibility/backup status shown
- **Partial if**: Most destructive operations require approval but gaps exist; approval context insufficient; occasional unapproved operations
- **No if**: No approval gates for destructive operations; agents can delete/destroy autonomously; no approval logs

---

### TM-PROC-L1-Q3: Tool Usage Anomaly Monitoring
**Question:** Do you monitor agent tool usage patterns for anomalies (frequency spikes, new tools, unusual combinations)?

**Verification:**
- Review tool usage baseline per agent (normal patterns)
- Examine anomaly detection configuration (thresholds, alerting)
- Test anomaly scenarios (10x tool usage spike, never-before-used tool)
- Verify anomaly detection latency (≤5 minutes from anomaly to alert)

**Evidence:**
- Tool usage baselines (per agent, 30-day history)
- Anomaly detection configuration (thresholds: ≥2 SD triggers investigation)
- Anomaly alert logs (examples of detected anomalies)
- Detection performance metrics (MTTD ≤5 minutes)

**Scoring:**
- **Yes if**: Baselines established for all agents; real-time anomaly detection; alerts on ≥2 SD deviations; MTTD ≤5 minutes; ≤10% false positives
- **Partial if**: Baselines exist but incomplete; delayed detection (>15 min); high false positives (>20%); manual monitoring required
- **No if**: No tool usage monitoring; no baselines; anomalies go undetected; no alerting

---

### TM-PROC-L1-Q4: Scoped Tool Authorization
**Question:** Are agent tool authorizations scoped to specific use cases with parameter constraints (not blanket access)?

**Verification:**
- Review tool authorization policies (per-agent, per-tool constraints)
- Examine parameter restriction implementation (e.g., send_email restricted to internal domains)
- Test that agents cannot bypass parameter constraints
- Verify authorization scope documented and reviewed quarterly

**Evidence:**
- Tool authorization policy documentation (per-agent scopes and constraints)
- Parameter constraint examples (send_email → internal domains only)
- Test results showing constraint enforcement
- Quarterly authorization review records

**Scoring:**
- **Yes if**: All tool authorizations scoped; parameter constraints enforced; agents cannot bypass constraints; quarterly reviews conducted
- **Partial if**: Some tools scoped but others have blanket access; constraint enforcement incomplete; infrequent reviews (<quarterly)
- **No if**: Blanket tool access; no parameter constraints; agents can use tools without restrictions; no reviews

---

### TM-PROC-L1-Q5: External Communication Validation
**Question:** Do external communication tools (send_email, upload_file, api_call to external domains) validate recipients against allowlists?

**Verification:**
- Test external emails/uploads to non-allowlisted addresses (should be blocked)
- Review allowlist configuration (approved external domains/recipients)
- Verify blocked external communications logged and alerted
- Examine approval workflow for external communications requiring exceptions

**Evidence:**
- External communication allowlist (approved domains, partners, APIs)
- Blocked communication logs (rejected external recipients)
- Alerts for external communication attempts to non-allowlisted destinations
- Approval workflow for allowlist exceptions

**Scoring:**
- **Yes if**: All external communications validated; allowlist enforced; blocked attempts logged and alerted; exception approval workflow exists
- **Partial if**: Validation exists but incomplete; allowlist bypasses possible; some external communications go unmonitored
- **No if**: No allowlist validation; agents can send to any external address; no monitoring of external communications

---

### TM-PROC-L1-Q6: Tool Call Logging
**Question:** Do you log all tool calls with full context (agent, tool, parameters, goal, timestamp, result) in tamper-evident storage?

**Verification:**
- Review tool call logs (verify comprehensive context captured)
- Test log immutability (append-only, cannot be modified)
- Verify minimum 90-day retention
- Examine log analysis capabilities (forensics after incidents)

**Evidence:**
- Tool call audit logs (comprehensive fields: agent, tool, params, goal, timestamp, result)
- Log storage configuration (append-only, tamper-evident, encrypted)
- Retention policy (≥90 days)
- Forensic analysis examples (investigation of tool misuse incidents)

**Scoring:**
- **Yes if**: 100% of tool calls logged; immutable storage; ≥90 days retention; full context captured; forensic analysis capabilities proven
- **Partial if**: Logging exists but incomplete (missing fields); storage not tamper-evident; shorter retention (<90 days); limited forensics
- **No if**: No tool call logging; logs can be modified; insufficient retention; no forensic capabilities

---

### TM-PROC-L1-Q7: Destructive Action Reversibility
**Question:** Before approving destructive operations, do you verify reversibility (backups exist, restore procedures tested)?

**Verification:**
- Review approval workflow for reversibility checks
- Examine backup validation before destructive operations
- Test restore procedures (verify backups can be restored successfully)
- Verify approval interface shows backup status and restore time

**Evidence:**
- Approval workflow reversibility checks (backup validation, restore procedure confirmation)
- Backup testing records (restore procedures tested quarterly)
- Approval interface showing backup status (last backup timestamp, estimated restore time)
- Examples of destructive operations safely reversed (restore from backup)

**Scoring:**
- **Yes if**: Reversibility checked for 100% of destructive operations; backups validated; restore procedures tested quarterly; approval shows backup status
- **Partial if**: Reversibility considered but not always validated; backups exist but restore not tested; approval doesn't show backup status
- **No if**: No reversibility checks; backups not validated; restore procedures untested; approval doesn't consider reversibility

---

### TM-PROC-L1-Q8: Cross-Context Tool Usage Validation
**Question:** Do you validate tools are used in appropriate contexts (e.g., test environment tools not used in production)?

**Verification:**
- Review context validation logic (environment, data classification, time-of-day)
- Test cross-context violations (test environment tool used in production)
- Verify context mismatches blocked and alerted
- Examine context-aware authorization policies

**Evidence:**
- Context validation implementation (environment checks, data classification validation)
- Test results showing cross-context tool usage blocked
- Context violation alerts
- Context-aware authorization policies (tools authorized per context)

**Scoring:**
- **Yes if**: Context validated for all tool calls; cross-context violations blocked; alerts generated; authorization policies context-aware
- **Partial if**: Context validation exists but incomplete; some cross-context uses allowed; limited alerting
- **No if**: No context validation; tools can be used in any context; no environment/classification checks

---

## Level 2 Comprehensive Questions

### TM-PROC-L2-Q1: Predictive Tool Misuse Detection
**Question:** Do you use machine learning to predict tool misuse before it occurs based on behavioral patterns?

**Verification:**
- Review predictive model architecture and training data
- Examine model performance (precision, recall, false positive rate)
- Test predictive alerts (early warning before misuse)
- Verify model identifies suspicious patterns missed by rules

**Evidence:**
- Predictive misuse detection model documentation
- Model performance metrics (≥80% precision, ≥70% recall, ≤15% FP rate)
- Predictive alert examples (misuse predicted and prevented)
- Quarterly model retraining records

**Scoring:**
- **Yes if**: ML model deployed; ≥80% precision, ≥70% recall; ≤15% FP rate; early warning prevents misuse; quarterly retraining
- **Partial if**: Model exists but lower performance; delayed predictions; high FP rate (>25%); infrequent retraining
- **No if**: No predictive detection; reactive only (detect after misuse); no ML-based early warning

---

# 4. ROGUE AGENTS (RA) - Processes Domain

## Level 1 Foundational Questions

### RA-PROC-L1-Q1: Behavioral Baseline Establishment
**Question:** Do you establish behavioral baselines for each agent (tool usage, API calls, resource consumption, active hours, output characteristics) over a 30-day period?

**Verification:**
- Review baseline establishment process (30-day observation period)
- Examine baseline metrics (tools, APIs, resources, timing, outputs)
- Verify baselines stored in tamper-evident storage (agent cannot modify own baseline)
- Test that new agents complete baselining before full operational deployment

**Evidence:**
- Behavioral baseline documentation (per-agent profiles)
- Baseline metrics (tool frequency, API patterns, resource usage, active hours, output stats)
- Tamper-evident baseline storage (append-only, integrity-protected)
- Examples of baselines established for new agents

**Scoring:**
- **Yes if**: All agents have 30-day baselines; comprehensive metrics captured; tamper-evident storage; new agents baseline before full deployment
- **Partial if**: Some agents baselined but coverage incomplete; shorter baseline period (<30 days); storage not tamper-evident; metrics limited
- **No if**: No baseline establishment; agents operate without behavioral profiles; no storage protection

---

### RA-PROC-L1-Q2: Real-Time Behavioral Anomaly Detection
**Question:** Do you detect behavioral anomalies in real-time (≤1 second latency) by comparing current behavior against baselines?

**Verification:**
- Review anomaly detection implementation (streaming analysis, real-time comparison)
- Test detection latency (time from anomalous action to alert)
- Examine anomaly thresholds (≥2 SD investigation, ≥3 SD alert, ≥4 SD auto-contain)
- Verify anomaly types detected (tool, API, resource, timing, output)

**Evidence:**
- Anomaly detection system documentation (architecture, thresholds, latency)
- Detection latency metrics (95th percentile ≤1 second)
- Anomaly alert examples (tool spikes, unusual APIs, resource anomalies, off-hours activity)
- Threshold configuration (2 SD, 3 SD, 4 SD actions)

**Scoring:**
- **Yes if**: Real-time detection (≤1 sec latency); comprehensive anomaly types covered; thresholds configured (2/3/4 SD); alerts generated appropriately
- **Partial if**: Detection exists but delayed (>5 sec); limited anomaly types; static thresholds; manual review required
- **No if**: No real-time anomaly detection; agents monitored manually; behavioral changes go undetected

---

### RA-PROC-L1-Q3: Automatic Containment
**Question:** Do severe behavioral anomalies (≥4 SD or Critical type like exfiltration) trigger automatic containment within 30 seconds?

**Verification:**
- Test containment execution (trigger severe anomaly, measure time to containment)
- Verify containment actions (suspend permissions, isolate agent, preserve forensics, alert humans)
- Examine containment logs (what was contained, when, why)
- Review restoration process (human approval required to restore agent)

**Evidence:**
- Containment system implementation (automated actions, triggers)
- Containment execution time metrics (90% ≤30 seconds)
- Containment logs (agent suspended, isolated, forensics preserved)
- Restoration approval workflow (human must approve before agent restored)

**Scoring:**
- **Yes if**: Automatic containment on severe anomalies; execution ≤30 sec; permissions suspended, agent isolated, forensics preserved; human approval for restore
- **Partial if**: Containment exists but slower (>60 sec); partial containment (permissions not fully suspended); manual restoration
- **No if**: No automatic containment; severe anomalies require manual response; no isolation capabilities

---

### RA-PROC-L1-Q4: Ephemeral Goal State
**Question:** Do agents use ephemeral goal state (cleared on session end, re-initialized from config on session start) to prevent persistent compromise?

**Verification:**
- Review goal state lifecycle (ephemeral vs. persistent)
- Test that compromised goals don't survive restarts
- Verify goal initialization from secure configuration (not from memory)
- Examine exceptions for long-running agents (if goals persist, integrity checks required)

**Evidence:**
- Goal state lifecycle documentation (ephemeral design, initialization process)
- Test results showing compromised goals cleared on restart
- Configuration-based goal initialization (secure, version-controlled)
- Exception handling for long-running agents (integrity checks if goals persist)

**Scoring:**
- **Yes if**: Goals ephemeral by default; cleared on session end; re-initialized from config; compromised goals cannot persist; long-running agent exceptions have integrity checks
- **Partial if**: Some goals ephemeral but exceptions common; goals sometimes persist without validation; unclear initialization process
- **No if**: Goals always persistent; compromised goals survive restarts; no initialization from config; no integrity checks

---

### RA-PROC-L1-Q5: Agent Identity Verification
**Question:** Do agents cryptographically verify identity before inter-agent communication using certificates and signed messages?

**Verification:**
- Review inter-agent identity verification implementation (certificates, signatures, mutual TLS)
- Test impersonation attempts (rogue agent claiming to be high-privilege agent)
- Verify identity verification failures logged and alerted
- Examine certificate management (issuance, rotation, revocation)

**Evidence:**
- Identity verification implementation (mTLS, certificate-based authentication, message signing)
- Impersonation test results (verification failures detected)
- Identity verification logs (successful/failed verifications)
- Certificate management documentation (lifecycle, rotation schedule)

**Scoring:**
- **Yes if**: Cryptographic identity verification for all inter-agent comms; impersonation attempts detected 100%; certificates managed (rotation, revocation); verification failures logged
- **Partial if**: Identity verification exists but incomplete coverage; some agents don't verify identity; certificate management ad-hoc
- **No if**: No identity verification; agents trust each other without validation; impersonation possible

---

### RA-PROC-L1-Q6: Inter-Agent Message Scanning
**Question:** Do you scan inter-agent communications for malicious content (prompt injection, goal modification attempts, privilege escalation)?

**Verification:**
- Review message scanning implementation (pattern detection, content analysis)
- Test malicious inter-agent messages (prompt injection payloads)
- Verify malicious messages blocked and logged
- Examine false positive rate (legitimate messages flagged incorrectly)

**Evidence:**
- Inter-agent message scanning configuration (patterns, ML models)
- Test results showing malicious messages detected and blocked
- Message scanning logs (blocked messages, detected patterns)
- False positive analysis (≤5% target)

**Scoring:**
- **Yes if**: All inter-agent messages scanned; ≥95% malicious content detected; messages blocked before delivery; ≤5% false positives
- **Partial if**: Scanning exists but incomplete coverage; detection <90%; high false positives (>10%); delayed scanning (not real-time)
- **No if**: No inter-agent message scanning; malicious content not detected; propagation prevention absent

---

### RA-PROC-L1-Q7: Exfiltration Detection
**Question:** Do you monitor agent outbound data transfers for potential exfiltration (non-allowlisted destinations, large volumes, sensitive data)?

**Verification:**
- Review outbound monitoring configuration (destination allowlists, volume thresholds, data classification)
- Test exfiltration scenarios (large data transfer to external IP, sensitive data outbound)
- Verify exfiltration alerts trigger CRITICAL severity and automatic containment
- Examine false positive rate for outbound monitoring

**Evidence:**
- Outbound monitoring implementation (network traffic analysis, data classification detection)
- Exfiltration test results (transfers to non-allowlisted destinations detected)
- Exfiltration alerts (CRITICAL severity, containment triggered)
- False positive analysis (≤5% target for legitimate external communications)

**Scoring:**
- **Yes if**: All outbound transfers monitored; non-allowlisted destinations detected; large volumes and sensitive data flagged; CRITICAL alerts + auto-containment; ≤5% FP rate
- **Partial if**: Monitoring exists but incomplete; some exfiltration types missed; manual containment; high FP rate (>10%)
- **No if**: No outbound monitoring; exfiltration goes undetected; no destination validation; no volume or classification checks

---

### RA-PROC-L1-Q8: Rogue Agent Detection Metrics
**Question:** Do you track rogue agent detection metrics (detection rate, MTTD, false positive rate, containment success rate)?

**Verification:**
- Review metrics dashboard (detection rate, MTTD, FP rate, containment success)
- Examine detection performance (≥90% detection rate, MTTD ≤5 minutes, FP ≤10%)
- Verify metrics used to optimize detection (adjust thresholds, improve models)
- Check quarterly metrics reviews and optimizations

**Evidence:**
- Rogue agent detection dashboard (real-time metrics)
- Performance metrics (detection rate ≥90%, MTTD ≤5 min, FP ≤10%, containment success ≥95%)
- Optimization examples (thresholds adjusted, models improved based on metrics)
- Quarterly review records (metrics analyzed, improvements implemented)

**Scoring:**
- **Yes if**: Comprehensive metrics tracked; ≥90% detection, ≤5 min MTTD, ≤10% FP, ≥95% containment success; quarterly optimization; dashboard available
- **Partial if**: Basic metrics tracked but incomplete; lower performance (detection <85%, MTTD >10 min, FP >15%); infrequent optimization
- **No if**: No metrics tracking; detection performance unknown; no optimization based on data

---

## Level 2 Comprehensive Questions

### RA-PROC-L2-Q1: Multi-Agent Compromise Propagation Prevention
**Question:** Do you prevent rogue agent compromise from propagating through multi-agent systems using isolation, message scanning, and containment?

**Verification:**
- Review multi-agent architecture (isolation mechanisms, communication controls)
- Test propagation scenarios (one compromised agent attempts to infect peers)
- Verify containment prevents spread (≤10% of agents compromised in tests)
- Examine propagation detection (simultaneous anomalies across multiple agents)

**Evidence:**
- Multi-agent isolation architecture documentation
- Propagation test results (containment limits spread to initial victim)
- Propagation detection alerts (multiple agents showing similar anomalies)
- Containment effectiveness metrics (≤10% agents compromised in tests)

**Scoring:**
- **Yes if**: Isolation mechanisms prevent propagation; message scanning blocks malicious inter-agent comms; containment limits spread to ≤10% agents; propagation detected and alerted
- **Partial if**: Some isolation but gaps exist; propagation possible to ≤30% agents; delayed detection (>10 minutes)
- **No if**: No propagation prevention; compromise spreads freely across multi-agent system; no containment mechanisms

---

### RA-PROC-L2-Q2: Dormant Compromise Detection
**Question:** Do you detect time-delayed or trigger-based dormant compromises using long-term goal consistency monitoring?

**Verification:**
- Review long-term goal tracking (goal consistency over days/weeks)
- Test dormant activation scenarios (goal changes after 30-day dormancy)
- Verify sudden goal shifts detected (after extended normal period)
- Examine baseline stability metrics (detect deviation after stability)

**Evidence:**
- Long-term goal consistency monitoring implementation
- Dormant activation test results (delayed goal changes detected)
- Goal shift detection after stable period (alerts on sudden behavior change)
- Baseline stability analysis (normal period → sudden change detected)

**Scoring:**
- **Yes if**: Long-term goal tracking active; dormant activations detected within ≤1 hour; sudden shifts after stable period alerted; quarterly dormancy testing
- **Partial if**: Some long-term tracking but incomplete; delayed dormant detection (>24 hours); manual analysis required
- **No if**: No long-term tracking; dormant compromises go undetected until damage occurs; no baseline stability monitoring

---

## Document Summary

**Total Questions:** 47 assessment questions across 4 critical risks
- **Excessive Agency (EA)**: 10 questions (8 Level 1, 2 Level 2)
- **Agent Goal Hijack (AGH)**: 9 questions (8 Level 1, 1 Level 2)
- **Tool Misuse (TM)**: 9 questions (8 Level 1, 1 Level 2)
- **Rogue Agents (RA)**: 10 questions (8 Level 1, 2 Level 2)

**Next Steps:**
1. Integrate questions into HAIAMM v2.2 assessment questionnaires
2. Generate JSON questionnaire files for assessment tool integration
3. Create scoring calculator for new questions
4. Pilot test questions with organizations

---

**End of Assessment Questionnaires Document**
