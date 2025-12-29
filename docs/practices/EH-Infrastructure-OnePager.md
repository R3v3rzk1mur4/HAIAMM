# Environment Hardening Practice – Infrastructure Domain
## HAIAMM v2.1 One-Pager

### Practice Overview

Environment Hardening for Infrastructure ensures AI cloud and network security systems are deployed with secure cloud configurations, hardened network architecture, least privilege IAM, and defense-in-depth controls across multi-cloud environments.

---

### Level 1: Key Hardening Activities

**Cloud Account Hardening**:
- [ ] **Root Account Protection**: Secure cloud root/admin accounts
  - MFA: Enable MFA on all root accounts (AWS root, Azure Global Admin, GCP Owner)
  - Access: Minimize root account usage, use IAM roles instead
  - Monitoring: Alert on root account usage
- [ ] **Account Structure**: Organize accounts for isolation
  - AWS: Multi-account strategy (AWS Organizations, separate accounts per environment)
  - Azure: Management groups, subscriptions per environment
  - GCP: Organization, folders, projects per environment
- [ ] **Service Control Policies**: Enforce guardrails across accounts
  - Restrictions: Disable unused regions, enforce encryption, block public access
  - Coverage: Apply to all accounts in organization

**IAM Hardening**:
- [ ] **Least Privilege IAM**: Minimal permissions for users, services
  - Approach: Start with no permissions, grant only required permissions
  - Tools: AWS IAM Access Analyzer, Azure AD PIM, GCP IAM Recommender
  - Review: Quarterly access reviews, remove unused permissions
- [ ] **MFA Enforcement**: Require MFA for all user accounts
  - Scope: 100% of privileged accounts, ≥95% of all accounts
  - Methods: TOTP, WebAuthn, hardware keys
- [ ] **IAM Policies**: Use restrictive IAM policies
  - Best Practices: Explicit deny, condition-based access, time-based access
  - Validation: Test policies, use policy simulators
- [ ] **Service Accounts**: Dedicated service accounts per service
  - Rotation: Rotate service account keys quarterly
  - Permissions: Minimal required permissions

**Network Hardening**:
- [ ] **VPC/VNet Segmentation**: Isolate resources by sensitivity
  - Structure: Separate VPCs/VNets for production, staging, dev
  - Isolation: Private subnets for databases, public subnets for load balancers only
- [ ] **Security Groups/NSGs**: Restrictive network access control
  - Default Deny: Block all traffic by default, explicitly allow required traffic
  - Least Privilege: Minimal port exposure, source IP restrictions
- [ ] **Network ACLs**: Subnet-level network filtering
  - Defense in Depth: Additional layer beyond security groups
  - Rules: Deny known-bad IPs, restrict inter-subnet traffic
- [ ] **Private Endpoints**: Eliminate public internet exposure
  - Services: Use VPC endpoints (AWS), Private Link (Azure), Private Service Connect (GCP)
  - Benefit: Access cloud services without public internet

**Data Protection Hardening**:
- [ ] **Encryption at Rest**: Encrypt all storage
  - S3/Blob/GCS: Server-side encryption (SSE-KMS, customer-managed keys)
  - EBS/Disks: Encrypt volumes, use customer-managed keys
  - Databases: Transparent data encryption (TDE)
  - Policy: Enforce encryption (block unencrypted resources)
- [ ] **Encryption in Transit**: TLS for all network communication
  - Load Balancers: TLS termination at load balancer, TLS 1.2+ only
  - Inter-Service: mTLS for service-to-service communication
- [ ] **S3/Blob Storage Hardening**:
  - [ ] Block public access (S3 Block Public Access, Azure Blob private containers)
  - [ ] Enable versioning (protect against accidental deletion)
  - [ ] Enable logging (CloudTrail, Azure Storage Analytics)
  - [ ] Enforce encryption

**Logging and Monitoring Hardening**:
- [ ] **Cloud Audit Logging**: Enable comprehensive logging
  - AWS: CloudTrail (all regions), VPC Flow Logs, S3 access logs
  - Azure: Activity Log, NSG Flow Logs, Storage Analytics
  - GCP: Cloud Audit Logs, VPC Flow Logs
  - Retention: ≥90 days in SIEM, ≥1 year in cold storage
- [ ] **Log Protection**: Secure logs from tampering
  - Approach: Separate log account, read-only access for operators
  - Integrity: Log file validation, object lock for S3 logs
- [ ] **Security Monitoring**: Real-time threat detection
  - Tools: AWS GuardDuty, Azure Defender, GCP Security Command Center
  - Alerts: Real-time alerts on suspicious activity, automated response

**Compliance and Governance**:
- [ ] **Config Management**: Track resource configuration changes
  - Tools: AWS Config, Azure Policy, GCP Config Connector
  - Rules: Detect non-compliant resources, auto-remediate or alert
- [ ] **Compliance Frameworks**: Apply security benchmarks
  - Benchmarks: CIS Benchmarks for AWS, Azure, GCP
  - Validation: Automated compliance scanning, remediation tracking
- [ ] **Tag Enforcement**: Enforce resource tagging for governance
  - Tags: Environment, Owner, CostCenter, DataClassification
  - Enforcement: Block resource creation without required tags

**Remediation Safety**:
- [ ] **Blast Radius Limits**: Hard-code maximum automated changes
  - Limits: ≤50 resources per remediation action
  - Validation: Test limits, ensure enforcement
- [ ] **Pre-Change Validation**: Assess impact before remediation
  - Simulation: Test changes in sandbox, predict impact
  - Approval: Require approval for high-risk changes
- [ ] **Rollback Capability**: Automated rollback on failure
  - Implementation: Snapshot before change, rollback on error
  - Testing: Test rollback mechanisms quarterly

**Success Indicators**:
- IAM compliance: ≥90% accounts follow least privilege, 100% privileged accounts use MFA
- Encryption: 100% data encrypted at rest and in transit
- Network security: Zero unnecessary public exposure, 100% resources in private subnets (except load balancers)
- Logging: 100% audit logging enabled, logs retained ≥90 days
- Compliance: ≥95% resources compliant with CIS Benchmarks

---

**Document Information**: Practice: Environment Hardening (EH) | Domain: Infrastructure | HAIAMM v2.1 | Last Updated: 2025-12-25
