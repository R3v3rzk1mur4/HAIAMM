# Issue Management Practice – Infrastructure Domain
## HAIAMM v2.1 One-Pager

### Practice Overview

Issue Management for Infrastructure ensures AI cloud and network security systems systematically identify, assess, prioritize, and remediate vulnerabilities in multi-cloud infrastructure, network devices, and security configurations.

---

### Level 1: Key Issue Management Activities

**Cloud Infrastructure Vulnerability Scanning**:
- [ ] **CSPM Scanning**: Continuous cloud security posture assessment
  - Providers: AWS, Azure, GCP
  - Tools: Prisma Cloud, Wiz, Orca, AWS Security Hub, Azure Security Center
  - Coverage: IAM misconfigurations, network exposure, storage security, encryption gaps
  - Frequency: Continuous scanning, real-time alerts on critical misconfigurations
- [ ] **IaC Vulnerability Scanning**: Scan Terraform, CloudFormation before deployment
  - Tools: Checkov, tfsec, Terrascan
  - Policy: Block deployments with critical misconfigurations
- [ ] **Container Orchestration Scanning**: Scan Kubernetes configurations
  - Tools: kube-bench, kube-hunter, Polaris
  - Coverage: Pod security, RBAC, network policies, secrets management

**Network Vulnerability Scanning**:
- [ ] **Network Device Scanning**: Scan firewalls, load balancers, routers
  - Tools: Nessus, Qualys, Rapid7
  - Frequency: Weekly scans, on-demand after configuration changes
- [ ] **Network Segmentation Validation**: Verify network isolation
  - Tests: Attempt cross-zone communication, validate firewall rules
  - Frequency: Quarterly validation, after network changes

**Multi-Cloud Vulnerability Assessment**:
- [ ] **Cross-Cloud Configuration Drift**: Detect configuration inconsistencies across clouds
  - Detection: Compare security baselines across AWS, Azure, GCP
  - Risk: Inconsistent security posture creates gaps
- [ ] **Cloud Service Vulnerabilities**: Monitor cloud provider security bulletins
  - Sources: AWS Security Bulletins, Azure Security Updates, GCP Security Advisories
  - Process: Assess impact, apply patches/mitigations within SLA

**Remediation Prioritization**:
- [ ] **Risk-Based Prioritization**: Prioritize by risk × business impact
  - Critical: Internet-facing misconfigurations, credential exposure, data exposure
  - High: Internal misconfigurations, excessive permissions, missing encryption
  - Medium: Compliance gaps, logging deficiencies
  - Low: Cosmetic issues, best practice deviations
- [ ] **Remediation SLAs**: Define time-to-remediate by severity
  - Critical: ≤24 hours
  - High: ≤7 days
  - Medium: ≤30 days
  - Low: ≤90 days

**Automated Remediation**:
- [ ] **Auto-Remediation for Low-Risk Issues**: Automatically fix common misconfigurations
  - Examples: Enable encryption at rest, enforce MFA, close unnecessary ports
  - Safeguards: Blast radius limits, rollback capability, approval for high-risk changes
- [ ] **Remediation Workflows**: Automated ticket creation and assignment
  - Integration: ServiceNow, Jira, PagerDuty
  - SLA Tracking: Alert when approaching remediation deadline

**Vulnerability Metrics**:
- [ ] Track MTTR by severity and cloud provider
- [ ] Monitor open vulnerability backlog (target: ≤10 critical, ≤50 high)
- [ ] SLA compliance (≥95% remediated within SLA)
- [ ] Vulnerability density per cloud account

**Success Indicators**:
- Scanning coverage: 100% of cloud accounts, network devices scanned
- MTTR: Critical ≤24h, High ≤7d, Medium ≤30d
- SLA compliance: ≥95%
- Vulnerability reduction: ≥70% year-over-year reduction in critical/high vulnerabilities

---

**Document Information**: Practice: Issue Management (IM) | Domain: Infrastructure | HAIAMM v2.1 | Last Updated: 2025-12-25
