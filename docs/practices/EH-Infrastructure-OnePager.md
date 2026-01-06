# Environment Hardening Practice – Infrastructure Domain
## HAIAMM v2.1 One-Pager

### Practice Overview

Environment Hardening for Infrastructure ensures AI cloud and network security systems are deployed with secure cloud configurations, hardened network architecture, least privilege IAM, and defense-in-depth controls across multi-cloud environments.

---

### Level 1: Comprehensive Environment Hardening

#### 1.1 Cloud Account Hardening

**AWS Account Hardening**:
- [ ] **Root Account Protection**:
  - [ ] Enable MFA on root account (hardware MFA recommended, YubiKey or Titan)
  - [ ] Delete root access keys (use IAM roles instead)
  - [ ] Set strong root password (≥20 characters, random)
  - [ ] Configure root account contact email (monitored security inbox)
  - [ ] Enable CloudTrail alerts on root account usage (immediate page on-call)
  - [ ] Store root credentials in secure vault (offline, encrypted)
- [ ] **AWS Organizations Setup**:
  - [ ] Create multi-account structure (separate accounts: production, staging, development, security/logging, shared services)
  - [ ] Enable consolidated billing, cost allocation tags
  - [ ] Create OUs (Organizational Units) for account grouping (by environment, business unit)
- [ ] **Service Control Policies (SCPs)**:
  - [ ] Deny public S3 buckets organization-wide (enforce S3 Block Public Access)
  - [ ] Deny disabling CloudTrail, GuardDuty, Config
  - [ ] Deny creating resources in unapproved regions (e.g., only us-east-1, eu-west-1)
  - [ ] Deny privilege escalation (block iam:PutUserPolicy for * resource)
  - [ ] Require encryption for S3, EBS (deny unencrypted resources)
- [ ] **AWS Account Settings**:
  - [ ] Set account alias (human-readable account identifier)
  - [ ] Configure IAM password policy (≥14 chars, complexity, expiration 90 days)
  - [ ] Enable EBS encryption by default (all regions)
  - [ ] Enable S3 Block Public Access (account-level, all regions)

**Azure Tenant Hardening**:
- [ ] **Global Administrator Protection**:
  - [ ] Enable MFA for all Global Admins (conditional access policy)
  - [ ] Limit number of Global Admins (≤5 emergency break-glass accounts)
  - [ ] Use Azure AD Privileged Identity Management (PIM) for just-in-time Global Admin access
  - [ ] Enable Azure AD Identity Protection (risk-based policies)
- [ ] **Management Group Structure**:
  - [ ] Create management group hierarchy (tenant root → business units → environments)
  - [ ] Assign subscriptions to appropriate management groups
  - [ ] Apply Azure policies at management group level (inherit to subscriptions)
- [ ] **Azure Policy Assignments**:
  - [ ] Deny public IP addresses (except approved resources)
  - [ ] Require encryption for storage accounts, disks
  - [ ] Require diagnostic logs forwarded to Log Analytics
  - [ ] Require resource tags (Environment, Owner, CostCenter)
  - [ ] Deny creation of resources in unapproved regions
- [ ] **Azure AD Configuration**:
  - [ ] Disable legacy authentication protocols (block Basic Auth, allow Modern Auth only)
  - [ ] Enable conditional access policies (require MFA, compliant devices, approved locations)
  - [ ] Configure password protection (banned password list, lockout threshold)

**GCP Organization Hardening**:
- [ ] **Organization Owner Protection**:
  - [ ] Enable MFA for Organization Owner accounts (2FA with hardware keys)
  - [ ] Limit Organization Owner role (≤3 accounts)
  - [ ] Use IAM conditions for time-based access (emergency access only)
  - [ ] Monitor Organization Owner usage (alert on any usage)
- [ ] **Organization Resource Hierarchy**:
  - [ ] Create folder structure (organization → business units → environments)
  - [ ] Create projects per application/environment (e.g., app-prod, app-staging)
  - [ ] Apply organization policies at folder/org level (inherited by projects)
- [ ] **Organization Policies**:
  - [ ] Require OS Login for VMs (enforce SSH key management)
  - [ ] Disable service account key creation (use workload identity instead)
  - [ ] Require shielded VMs (secure boot, vTPM, integrity monitoring)
  - [ ] Restrict resource locations (allowed GCP regions)
  - [ ] Require uniform bucket-level access (disable ACLs)
- [ ] **GCP IAM Configuration**:
  - [ ] Remove primitive roles (Owner, Editor, Viewer → Use granular predefined roles)
  - [ ] Enable Cloud Identity (centralized identity management)
  - [ ] Configure context-aware access (device policy, location restrictions)

#### 1.2 IAM Hardening

**Least Privilege Implementation**:
- [ ] **Access Analysis and Right-Sizing**:
  - [ ] Run IAM access analyzers (AWS IAM Access Analyzer, Azure Access Reviews, GCP IAM Recommender)
  - [ ] Identify unused permissions (last accessed data, activity logs)
  - [ ] Remove unused permissions quarterly (automate removal of permissions unused ≥90 days)
  - [ ] Right-size IAM policies (grant only permissions actually used)
  - [ ] Success Criteria: ≥90% of users/roles have only required permissions
- [ ] **Principle of Least Privilege**:
  - [ ] Start with zero permissions, grant incrementally (not "allow all, then restrict")
  - [ ] Use managed policies (AWS managed, Azure built-in, GCP predefined) where possible
  - [ ] Custom policies: Specific resources (not *), specific actions (not *), conditions (IP, MFA, time)
  - [ ] Separate read vs. write permissions (analysts get read-only, operators get read-write)

**MFA Enforcement**:
- [ ] **Multi-Factor Authentication Requirements**:
  - [ ] Enforce MFA for 100% of privileged accounts (admins, security, finance)
  - [ ] Enforce MFA for ≥95% of all human user accounts
  - [ ] Methods: Hardware MFA (YubiKey, Titan) for privileged, TOTP (Google Authenticator) for standard users
  - [ ] Block console access without MFA (IAM policy condition: `aws:MultiFactorAuthPresent: false` → Deny)
- [ ] **Conditional Access Policies**:
  - [ ] Azure: Require MFA for all users, require compliant device, block legacy auth
  - [ ] GCP: Context-aware access based on device policy, IP location
  - [ ] AWS: IAM policy conditions (require MFA, source IP restrictions)

**IAM Policy Best Practices**:
- [ ] **Policy Structure**:
  - [ ] Use explicit Deny for sensitive actions (deny iam:*, s3:DeleteBucket)
  - [ ] Use conditions for context-based access (IP whitelist, time-based, MFA-required)
  - [ ] Use NotAction sparingly (can lead to unintended permissions)
  - [ ] Use resource ARNs (not *) wherever possible
  - [ ] Example: Allow S3 read only from specific bucket: `arn:aws:s3:::my-app-data/*`
- [ ] **Policy Validation**:
  - [ ] Test policies before deployment (AWS IAM Policy Simulator, Azure What-If)
  - [ ] Use policy linting tools (cfn-lint for CloudFormation IAM, IAM Policy Validator)
  - [ ] Peer review all custom IAM policies
  - [ ] Version control IAM policies (Git, track changes)

**Service Account Hardening**:
- [ ] **Service Account Management**:
  - [ ] Dedicated service account per service/application (not shared)
  - [ ] Descriptive naming (app-name-environment-purpose, e.g., cspm-prod-remediation)
  - [ ] Rotate service account keys quarterly (automated rotation, alert if not rotated)
  - [ ] Prefer instance profiles/managed identities over static keys (AWS instance profile, Azure managed identity, GCP workload identity)
- [ ] **Service Account Permissions**:
  - [ ] Minimal required permissions (least privilege)
  - [ ] No wildcard permissions (* resources or * actions)
  - [ ] Use conditions (restrict by IP, resource tags)
  - [ ] Review service account permissions quarterly

**Identity Federation**:
- [ ] **Single Sign-On (SSO)**:
  - [ ] Centralized identity provider (Okta, Azure AD, Google Workspace)
  - [ ] SAML/OIDC federation to cloud providers (AWS SSO, Azure AD, Google Workspace federation)
  - [ ] Disable direct cloud user creation (all users via SSO)
  - [ ] Benefits: Centralized MFA, centralized access reviews, automatic deprovisioning
- [ ] **Break-Glass Accounts**:
  - [ ] Maintain 2-3 emergency local accounts (in case SSO fails)
  - [ ] Strong unique passwords (stored in secure vault, offline)
  - [ ] Alert on any break-glass account usage (immediate incident investigation)

#### 1.3 Network Hardening

**VPC/VNet Segmentation**:
- [ ] **Multi-Tier Architecture**:
  - [ ] Public subnet: Load balancers, NAT gateways (internet-facing resources only)
  - [ ] Private subnet: Application servers, CSPM detection/remediation engines (no direct internet)
  - [ ] Database subnet: Databases, caches (most restricted, no internet access)
  - [ ] Management subnet: Bastion hosts, admin tools (tightly controlled access)
- [ ] **Network Isolation by Environment**:
  - [ ] Separate VPC/VNet per environment (production, staging, development)
  - [ ] VPC peering or Transit Gateway for cross-VPC communication (controlled routes)
  - [ ] No production-to-development connectivity (prevent lateral movement)
- [ ] **Subnet CIDR Planning**:
  - [ ] Non-overlapping CIDR blocks (enable VPC peering, hybrid cloud)
  - [ ] Sufficient IP space for scaling (e.g., /24 for small apps, /20 for large)
  - [ ] Reserve CIDR ranges for future expansion

**Security Group and NSG Hardening**:
- [ ] **Default Deny Stance**:
  - [ ] Start with deny-all, explicitly allow required traffic
  - [ ] Remove default allow-all rules
  - [ ] Review all 0.0.0.0/0 rules (should be rare, only load balancers)
- [ ] **Least Privilege Network Access**:
  - [ ] Restrict source IPs (specific CIDR blocks, not 0.0.0.0/0)
  - [ ] Restrict destination ports (specific ports, not port ranges)
  - [ ] Restrict protocols (TCP/UDP specific, not "all protocols")
  - [ ] Example: Allow HTTPS from load balancer subnet only → `Source: 10.0.1.0/24, Port: 443, Protocol: TCP`
- [ ] **Security Group Naming and Tagging**:
  - [ ] Descriptive names (app-name-tier-purpose, e.g., cspm-app-web-sg)
  - [ ] Tags: Environment, Owner, Purpose
  - [ ] Documentation: Comments in IaC describing purpose of each rule
- [ ] **Security Group Auditing**:
  - [ ] Quarterly review of all security group rules
  - [ ] Automated detection of risky rules (0.0.0.0/0 on risky ports: 22, 3389, 3306, 5432)
  - [ ] Alert on security group changes (forward to SIEM)

**Network ACLs**:
- [ ] **Subnet-Level Filtering**:
  - [ ] Network ACLs as additional layer (defense in depth beyond security groups)
  - [ ] Deny known-bad IPs (threat intelligence, previous attackers)
  - [ ] Deny inter-subnet traffic (where not required, e.g., web subnet → database subnet blocked unless required)
- [ ] **Stateless Filtering**:
  - [ ] Remember NACLs are stateless (must allow both inbound and outbound)
  - [ ] Ephemeral port ranges (allow outbound 1024-65535 for response traffic)

**Private Endpoints and Service Endpoints**:
- [ ] **Eliminate Public Internet for Cloud Services**:
  - [ ] AWS: VPC Endpoints for S3, DynamoDB, SQS, etc. (traffic stays in AWS network)
  - [ ] Azure: Private Link for Storage, SQL, Key Vault (traffic stays in Azure network)
  - [ ] GCP: Private Service Connect for Cloud Storage, BigQuery (traffic stays in GCP network)
  - [ ] Benefits: No public internet exposure, lower latency, better security
- [ ] **PrivateLink/Private Service Connect for Third-Party Services**:
  - [ ] Use PrivateLink for SaaS vendors (Datadog, Snowflake, etc.)
  - [ ] Avoid NAT gateway for large data transfers (use private endpoints)

**Bastion Host and VPN Hardening**:
- [ ] **Bastion Host (Jump Box)**:
  - [ ] Minimal software (SSH/RDP only, no unnecessary packages)
  - [ ] MFA enforcement for bastion access
  - [ ] Session recording (log all SSH/RDP sessions)
  - [ ] IP whitelisting (only allow from corporate VPN/office IPs)
  - [ ] Automatic shutdown of idle sessions (≤15 minutes idle)
- [ ] **VPN Hardening**:
  - [ ] Use site-to-site VPN for corporate network connectivity (not individual user VPN)
  - [ ] Enforce strong VPN encryption (AES-256, IKEv2)
  - [ ] MFA for VPN access (all users)
  - [ ] Monitor VPN access (alert on unusual VPN usage)

#### 1.4 Data Protection Hardening

**Encryption at Rest**:
- [ ] **Object Storage Encryption**:
  - [ ] S3: SSE-KMS (customer-managed keys, not AWS-managed keys) for sensitive data
  - [ ] Azure Blob: Customer-managed keys in Azure Key Vault
  - [ ] GCS: Customer-managed encryption keys (CMEK)
  - [ ] Enforce encryption: Deny PUT requests without server-side encryption header
- [ ] **Block Storage Encryption**:
  - [ ] EBS volumes: Enable EBS encryption by default (account-level setting)
  - [ ] Azure Disks: Azure Disk Encryption (customer-managed keys)
  - [ ] GCE Persistent Disks: Encrypted by default (CMEK for sensitive data)
- [ ] **Database Encryption**:
  - [ ] RDS/Azure SQL/Cloud SQL: Enable TDE (Transparent Data Encryption)
  - [ ] DynamoDB/Cosmos DB/Firestore: Encryption at rest enabled (default)
  - [ ] Backups: Encrypt database backups (same key as database or separate backup key)
- [ ] **Encryption Policy Enforcement**:
  - [ ] Service Control Policies: Deny creation of unencrypted resources
  - [ ] Azure Policy: Audit/deny unencrypted storage accounts, disks
  - [ ] GCP Organization Policy: Require CMEK for sensitive projects

**Encryption in Transit**:
- [ ] **TLS for All External Traffic**:
  - [ ] Load balancers: TLS 1.2+ only (disable TLS 1.0, 1.1)
  - [ ] Strong cipher suites (ECDHE, AES-GCM, no RC4, no 3DES)
  - [ ] HSTS (HTTP Strict Transport Security) headers
  - [ ] Certificate management: Auto-renewal (AWS ACM, Let's Encrypt), monitor expiration
- [ ] **mTLS for Internal Service-to-Service**:
  - [ ] Mutual TLS between microservices (both client and server verify certificates)
  - [ ] Tools: Service mesh (Istio, Linkerd), AWS App Mesh, Azure Service Fabric
  - [ ] Certificate rotation: Automated short-lived certificates (≤7 days)
- [ ] **Database Connection Encryption**:
  - [ ] Enforce SSL/TLS for database connections (RDS force SSL, Azure SQL require encryption)
  - [ ] Reject unencrypted connections

**S3/Blob Storage Hardening**:
- [ ] **Block Public Access**:
  - [ ] S3: Enable S3 Block Public Access (account-level and bucket-level)
  - [ ] Azure: Disable public blob access (private containers only)
  - [ ] GCS: Uniform bucket-level access (disable ACLs, use IAM only)
  - [ ] Success Criteria: Zero public buckets (except explicitly approved, e.g., static website hosting)
- [ ] **Versioning and Lifecycle**:
  - [ ] Enable versioning (protect against accidental deletion, ransomware)
  - [ ] MFA Delete for S3 (require MFA to delete versions)
  - [ ] Lifecycle policies: Transition old versions to Glacier (cost optimization), expire after retention period
- [ ] **Access Logging and Monitoring**:
  - [ ] S3 access logs: Log all access (who, when, what, source IP)
  - [ ] CloudTrail S3 data events: Log API calls (GetObject, PutObject, DeleteObject)
  - [ ] Alerts: Alert on unusual access patterns (large downloads, access from unusual IPs)
- [ ] **Bucket Policies**:
  - [ ] Deny insecure transport (enforce TLS: `"Condition": {"Bool": {"aws:SecureTransport": false}}`)
  - [ ] Deny unencrypted uploads (enforce SSE-KMS)
  - [ ] IP restrictions (if applicable, e.g., only from corporate network)

#### 1.5 Logging and Monitoring Hardening

**Comprehensive Audit Logging**:
- [ ] **Enable All Cloud Audit Logs**:
  - [ ] AWS: CloudTrail (all regions, management + data events), VPC Flow Logs, S3 access logs, RDS logs
  - [ ] Azure: Activity Log, Resource Logs, NSG Flow Logs, Storage Analytics
  - [ ] GCP: Admin Activity, Data Access, System Event, Policy Denied logs
  - [ ] Retention: ≥90 days in SIEM, ≥1 year in cold storage (S3 Glacier, Azure Archive)
- [ ] **Log Forwarding to SIEM**:
  - [ ] Forward all logs to centralized SIEM (Splunk, Elastic, Azure Sentinel)
  - [ ] Real-time streaming (CloudWatch Logs → Kinesis → SIEM, Activity Log → Event Hub → SIEM)
  - [ ] Log normalization (map cloud-specific fields to common schema)

**Log Protection**:
- [ ] **Separate Log Storage Account**:
  - [ ] AWS: Dedicated S3 bucket in separate account (prevent tampering by attackers in main account)
  - [ ] Azure: Separate subscription for log storage
  - [ ] GCP: Separate project for log sinks
  - [ ] Cross-account access: Read-only access from main account to log account
- [ ] **Log Integrity**:
  - [ ] CloudTrail log file validation (SHA-256 digest files, verify integrity)
  - [ ] S3 Object Lock (WORM - write once read many, prevent log deletion)
  - [ ] Immutable storage (Azure immutable blob storage)
- [ ] **Log Access Controls**:
  - [ ] IAM: Read-only access for security analysts, no write/delete access
  - [ ] Log all access to logs (meta-logging, audit who accessed logs)
  - [ ] Alert on log access from unusual accounts/IPs

**Security Monitoring Services**:
- [ ] **Enable Cloud-Native Threat Detection**:
  - [ ] AWS GuardDuty: Enable in all regions, all accounts (detect malicious activity, compromised instances)
  - [ ] Azure Defender for Cloud: Enable for VMs, storage, SQL, Kubernetes, App Service
  - [ ] GCP Security Command Center: Premium tier (vulnerability scanning, threat detection, compliance monitoring)
  - [ ] Forward findings to SIEM: Integrate with SIEM for centralized alerting
- [ ] **Automated Response**:
  - [ ] High-severity findings: Page on-call, auto-isolate compromised instances (security group change)
  - [ ] Medium-severity: Create ticket, investigate within 24 hours
  - [ ] Low-severity: Weekly digest, review for trends

#### 1.6 Compliance and Governance

**Configuration Management and Drift Detection**:
- [ ] **Enable Configuration Tracking**:
  - [ ] AWS Config: Enable in all regions, record all resource types, track configuration history
  - [ ] Azure Policy: Track policy compliance, configuration changes
  - [ ] GCP Config Connector: Track resource configurations, export to Git
- [ ] **Configuration Rules**:
  - [ ] CIS Benchmark rules: Automated checks for CIS compliance (CloudTrail enabled, S3 encryption, etc.)
  - [ ] Custom rules: Organization-specific policies (required tags, approved AMIs, etc.)
  - [ ] Remediation: Auto-remediate non-compliant resources (or alert for manual remediation)
- [ ] **Drift Detection**:
  - [ ] Detect changes outside IaC (manual changes via console → Alert security team)
  - [ ] Quarantine drifted resources (tag for review, optionally revert to IaC state)

**Compliance Framework Implementation**:
- [ ] **CIS Benchmarks**:
  - [ ] CIS AWS Foundations Benchmark (identity, logging, monitoring, networking)
  - [ ] CIS Azure Foundations Benchmark (identity, defender, logging, networking)
  - [ ] CIS GCP Foundations Benchmark (IAM, logging, networking, VM)
  - [ ] Automated scanning: Daily compliance scans, trend compliance score over time
  - [ ] Success Criteria: ≥95% compliance with CIS Benchmarks
- [ ] **Industry-Specific Compliance**:
  - [ ] PCI-DSS: Network segmentation, encryption, access controls, logging
  - [ ] HIPAA: PHI encryption, access logging, audit trails
  - [ ] SOC 2: Security controls, availability, confidentiality
  - [ ] Tools: AWS Security Hub, Azure Compliance Manager, GCP Compliance Reports Manager

**Tag Enforcement and Governance**:
- [ ] **Required Resource Tags**:
  - [ ] Environment (production, staging, development)
  - [ ] Owner (team email, individual email)
  - [ ] CostCenter (for chargeback, budget tracking)
  - [ ] DataClassification (public, internal, confidential, restricted)
  - [ ] Application (app name, for asset inventory)
- [ ] **Tag Enforcement**:
  - [ ] Service Control Policies: Deny resource creation without required tags (AWS)
  - [ ] Azure Policy: Audit/deny resources missing required tags
  - [ ] GCP: Use labels (equivalent to tags), enforce via organization policies
  - [ ] Automated tagging: Tag EC2 instances from AMI tags, tag volumes from instance tags
- [ ] **Tag Compliance Monitoring**:
  - [ ] Weekly reports: Resources missing tags, tag compliance by account/project
  - [ ] Auto-remediate: Tag resources with default values, alert owner to correct tags

#### 1.7 Remediation Safety Hardening

**Blast Radius Limits**:
- [ ] **Hard-Coded Limits in Remediation Engine**:
  - [ ] Maximum resources per single remediation: ≤10 (conservative, prevent mass changes)
  - [ ] Maximum remediations per hour: ≤100 (rate limiting, prevent runaway automation)
  - [ ] Maximum remediations per day: ≤1000 (daily cap)
  - [ ] Implementation: Code constants, enforced programmatically, tested in CI/CD
- [ ] **Graduated Automation Levels**:
  - [ ] Alert-Only: High-risk changes → Alert security team, no automation (e.g., IAM policy changes)
  - [ ] Auto-Remediate Low-Risk: Well-understood issues → Automatic remediation (e.g., public S3 bucket → Make private)
  - [ ] Manual Approval for High-Risk: Changes affecting many resources → Require human approval before remediation
- [ ] **Blast Radius Monitoring**:
  - [ ] Real-time dashboard: Current blast radius usage (resources changed today, this hour)
  - [ ] Alerts: Alert when approaching limits (e.g., 80% of daily limit)
  - [ ] Audit: Log all blast radius limit violations, investigate why limit approached

**Pre-Change Validation**:
- [ ] **Impact Assessment**:
  - [ ] Dependency analysis: Identify resources affected by change (e.g., security group change affects 50 EC2 instances)
  - [ ] Risk scoring: Calculate risk score (low/medium/high based on blast radius, resource criticality)
  - [ ] Approval routing: High-risk changes → Require security lead approval
- [ ] **Sandbox Testing**:
  - [ ] Test changes in non-production first (staging environment)
  - [ ] Canary deployments: Apply change to 1-2 resources, monitor, then roll out to others
  - [ ] Validation: Verify change achieves desired outcome without breaking functionality

**Rollback Capability**:
- [ ] **Automated State Backup**:
  - [ ] Before remediation: Snapshot current state (resource configuration, dependencies)
  - [ ] Storage: Store state in S3/Blob/GCS with versioning
  - [ ] Retention: Retain state backups for ≥30 days
  - [ ] Success Criteria: 100% of remediations have state backup
- [ ] **Rollback Mechanisms**:
  - [ ] Automated rollback: On remediation failure, automatically restore previous state
  - [ ] Manual rollback: Operator can trigger rollback of any recent remediation
  - [ ] Rollback validation: Verify state restored to pre-remediation configuration
- [ ] **Rollback Testing**:
  - [ ] Quarterly rollback drills: Intentionally fail remediation, verify rollback works
  - [ ] Test rollback on different resource types (security groups, IAM policies, S3 bucket policies)
  - [ ] Success Criteria: 100% successful rollback in drills

#### 1.8 Container and Serverless Hardening

**Kubernetes/Container Hardening**:
- [ ] **Pod Security Standards**:
  - [ ] Enforce Restricted Pod Security Standard (no privileged containers, non-root user, read-only root filesystem)
  - [ ] Use admission controllers (Pod Security Admission, OPA Gatekeeper) to enforce policies
  - [ ] Disable privileged containers (`privileged: false` in pod spec)
- [ ] **Network Policies**:
  - [ ] Default deny all traffic, explicitly allow required traffic
  - [ ] Isolate namespaces (prevent cross-namespace traffic unless required)
  - [ ] Example: Allow traffic to database pods only from app pods
- [ ] **RBAC Hardening**:
  - [ ] Least privilege RBAC roles (no cluster-admin unless absolutely necessary)
  - [ ] Service accounts per application (not default service account)
  - [ ] Audit RBAC permissions quarterly (remove unused)
- [ ] **Image Security**:
  - [ ] Scan images for vulnerabilities (Trivy, Clair, Snyk)
  - [ ] Use minimal base images (distroless, Alpine)
  - [ ] Signed images (Docker Content Trust, Notary v2)
  - [ ] Private container registry (ECR, ACR, Artifact Registry)

**Serverless Function Hardening**:
- [ ] **Lambda/Azure Functions/Cloud Functions**:
  - [ ] Minimal IAM permissions (function-specific IAM role, no wildcards)
  - [ ] VPC integration (run functions in private subnet, use VPC endpoints)
  - [ ] Environment variable encryption (KMS-encrypted environment variables)
  - [ ] Timeouts and concurrency limits (prevent runaway functions, DoS protection)
- [ ] **Function Dependencies**:
  - [ ] Dependency scanning (scan Python/Node.js dependencies for vulnerabilities)
  - [ ] Minimal dependencies (reduce attack surface)
  - [ ] Pin dependency versions (avoid supply chain attacks)

#### 1.9 Database Hardening

**Database Access Controls**:
- [ ] **Network Isolation**:
  - [ ] Databases in private subnets (no public IPs)
  - [ ] Security groups: Allow only from application tier (not 0.0.0.0/0)
  - [ ] Bastion/VPN for admin access (no direct internet access for DBAs)
- [ ] **Authentication and Authorization**:
  - [ ] IAM database authentication (RDS IAM auth, Azure AD auth, Cloud SQL IAM auth)
  - [ ] Disable default database users (postgres, sa, root)
  - [ ] Strong passwords for database users (≥20 characters, random)
  - [ ] Least privilege database roles (application gets read/write on specific tables, not superuser)

**Database Encryption**:
- [ ] **Encryption at Rest**:
  - [ ] Enable TDE (Transparent Data Encryption) for all databases
  - [ ] Customer-managed keys (KMS, Key Vault, Cloud KMS)
  - [ ] Encrypted backups (same key as database or separate backup key)
- [ ] **Encryption in Transit**:
  - [ ] Force SSL/TLS for all database connections
  - [ ] Reject unencrypted connections (RDS parameter: `rds.force_ssl=1`)

**Database Auditing**:
- [ ] **Enable Database Audit Logs**:
  - [ ] Log all connections, authentication attempts, query execution
  - [ ] Forward to SIEM for centralized monitoring
  - [ ] Alerts: Failed login attempts, unusual query patterns, data exfiltration (large SELECT)

#### 1.10 Secret Management

**Centralized Secret Storage**:
- [ ] **Secrets Manager**:
  - [ ] AWS Secrets Manager, Azure Key Vault, GCP Secret Manager for all secrets (passwords, API keys, certificates)
  - [ ] Never hardcode secrets in code, environment variables, or config files
  - [ ] Rotate secrets automatically (90-day rotation for database passwords, API keys)
- [ ] **Secret Access Policies**:
  - [ ] IAM policies restrict secret access to specific services/users
  - [ ] Audit secret access (log all secret retrievals, alert on unusual access)

**Application Secret Injection**:
- [ ] **Runtime Secret Injection**:
  - [ ] ECS/Kubernetes: Inject secrets as environment variables from Secrets Manager
  - [ ] Lambda: Retrieve secrets at runtime (not in environment variables)
  - [ ] Never log secrets (redact secrets from application logs)

#### 1.11 Infrastructure as Code (IaC) Hardening

**IaC Security Scanning**:
- [ ] **Pre-Deployment Scanning**:
  - [ ] Scan Terraform/CloudFormation for security issues (Checkov, tfsec, Terrascan, cfn-lint, cfn_nag)
  - [ ] CI/CD integration: Block deployment if security issues detected
  - [ ] Example issues: Unencrypted S3 buckets, public security groups, missing logging
- [ ] **Policy as Code**:
  - [ ] Enforce security policies in IaC (OPA/Rego, Sentinel for Terraform)
  - [ ] Example policies: All S3 buckets must have encryption, all EC2 instances must be in private subnet

**IaC State File Security**:
- [ ] **Terraform State Security**:
  - [ ] Store state in S3 with encryption and versioning (not locally)
  - [ ] Enable state locking (DynamoDB) to prevent concurrent modifications
  - [ ] Restrict state file access (IAM policies, only CI/CD pipeline can access)
- [ ] **State File Encryption**:
  - [ ] Encrypt Terraform state with KMS (state may contain sensitive data: passwords, keys)

#### 1.12 Success Indicators

**IAM Security Metrics**:
- [ ] ≥90% of accounts follow least privilege (no wildcard permissions)
- [ ] 100% of privileged accounts use MFA
- [ ] ≥95% of all user accounts use MFA
- [ ] Zero root account usage (except emergency break-glass scenarios)

**Encryption Metrics**:
- [ ] 100% of data encrypted at rest (storage, databases, backups)
- [ ] 100% of data encrypted in transit (TLS 1.2+, no unencrypted protocols)
- [ ] Zero unencrypted S3 buckets, EBS volumes, databases

**Network Security Metrics**:
- [ ] Zero unnecessary public exposure (only load balancers, approved resources have public IPs)
- [ ] 100% of compute resources in private subnets (no direct internet access)
- [ ] ≥95% of security group rules follow least privilege (specific sources, ports)

**Logging and Monitoring Metrics**:
- [ ] 100% of cloud accounts have audit logging enabled (CloudTrail, Activity Log, Cloud Audit Logs)
- [ ] Logs retained ≥90 days in SIEM, ≥1 year in cold storage
- [ ] 100% of high-severity GuardDuty/Defender/SCC findings investigated within ≤24 hours

**Compliance Metrics**:
- [ ] ≥95% resources compliant with CIS Benchmarks
- [ ] 100% of resources have required tags (Environment, Owner, DataClassification)
- [ ] Zero configuration drift unresolved ≥7 days

**Remediation Safety Metrics**:
- [ ] Zero blast radius limit violations
- [ ] 100% of remediations have state backups (enable rollback)
- [ ] 100% rollback success rate in quarterly drills

---

### Level 2: Advanced Environment Hardening

#### 2.1 Automated Hardening Validation

**Continuous Compliance Scanning**:
- [ ] **Real-Time Compliance Monitoring**:
  - [ ] Event-driven compliance checks (trigger on CloudTrail/Activity Log events)
  - [ ] Example: S3 bucket created → Immediately check encryption, public access, logging → Remediate within ≤5 minutes
  - [ ] Tools: AWS Config Rules (automated remediation), Azure Policy (auto-remediate), GCP Config Connector
- [ ] **Compliance as Code**:
  - [ ] Define compliance policies as code (OPA/Rego, Sentinel, Cloud Custodian)
  - [ ] Version control policies (Git, track changes, peer review)
  - [ ] Automated enforcement (block non-compliant resources in CI/CD, auto-remediate in production)

**Infrastructure Testing**:
- [ ] **Automated Security Testing**:
  - [ ] InSpec for infrastructure compliance testing (test SSH hardening, firewall rules, encryption)
  - [ ] Serverspec for automated testing of server configurations
  - [ ] Example test: "Verify all EC2 instances are in private subnets" → Automated test runs daily
- [ ] **Chaos Engineering for Security**:
  - [ ] Intentionally introduce security issues (disable encryption, open firewall) → Verify CSPM detects and remediates
  - [ ] Test blast radius limits (attempt to remediate 101 resources) → Verify blocked
  - [ ] Test rollback mechanisms (inject remediation failures) → Verify rollback works

#### 2.2 AI-Powered Configuration Drift Detection

**ML-Based Drift Detection**:
- [ ] **Anomaly Detection for Configuration Changes**:
  - [ ] Train ML models on normal configuration change patterns
  - [ ] Detect anomalous changes (sudden spike in security group rules, unusual IAM policy changes)
  - [ ] Alert on drift that deviates from learned patterns
  - [ ] Benefit: Detect sophisticated attacks (slow, subtle config changes over weeks)
- [ ] **Behavioral Analysis**:
  - [ ] Learn typical change velocity (e.g., 10 security group changes per week)
  - [ ] Alert on unusual velocity (100 changes in one day → Investigate)

**Predictive Drift Prevention**:
- [ ] **Predict Likely Drift**:
  - [ ] Analyze historical drift patterns → Predict which resources likely to drift
  - [ ] Proactive monitoring of drift-prone resources (increase monitoring frequency)
  - [ ] Example: "Resource X drifts every 2 weeks → Proactively check daily"

#### 2.3 Advanced Threat Protection

**Automated Vulnerability Patching**:
- [ ] **Patch Management Automation**:
  - [ ] AWS Systems Manager Patch Manager: Automated OS patching (Windows, Linux)
  - [ ] Azure Update Management: Automated VM patching
  - [ ] GCP OS Patch Management: Automated patching for Compute Engine
  - [ ] Patch cadence: Critical patches within ≤7 days, high within ≤30 days
- [ ] **Container Image Patching**:
  - [ ] Automated base image updates (rebuild images monthly with latest base)
  - [ ] Dependency updates (Dependabot, Renovate for automated dependency PRs)
  - [ ] Automated redeployment after patching (CI/CD pipeline redeploys with patched images)

**Endpoint Detection and Response (EDR/XDR)**:
- [ ] **Cloud Workload Protection**:
  - [ ] AWS: GuardDuty Malware Protection (scan EBS volumes for malware)
  - [ ] Azure: Microsoft Defender for Servers (EDR for VMs)
  - [ ] GCP: Chronicle endpoint agents (SIEM-integrated EDR)
  - [ ] Automated response: Isolate compromised instances, snapshot for forensics
- [ ] **Runtime Protection**:
  - [ ] Falco for Kubernetes runtime security (detect abnormal container behavior)
  - [ ] Aqua Security, Sysdig for container runtime protection
  - [ ] Alerts: Process spawning suspicious binaries, unauthorized network connections

#### 2.4 Zero Trust Architecture

**Identity-Based Access (Not Network-Based)**:
- [ ] **Zero Trust Network Access (ZTNA)**:
  - [ ] Replace VPN with identity-based access (BeyondCorp, Zscaler Private Access)
  - [ ] Every request authenticated and authorized (no "trusted network")
  - [ ] Device posture checks (require compliant devices, up-to-date OS)
- [ ] **Micro-Segmentation**:
  - [ ] Segment networks to individual workloads (not just VPC/subnet level)
  - [ ] Enforce least privilege at workload level (app A can talk to database B, but not database C)
  - [ ] Tools: AWS Security Groups (instance-level), Kubernetes Network Policies (pod-level)

**Continuous Verification**:
- [ ] **Session Verification**:
  - [ ] Re-verify user identity periodically (not just at login)
  - [ ] Step-up authentication for sensitive actions (require MFA to delete resources, even if already logged in)
  - [ ] Short-lived tokens (access tokens expire after 1 hour, require re-auth)

#### 2.5 Advanced Encryption

**Bring Your Own Key (BYOK)**:
- [ ] **Customer-Managed Key Management**:
  - [ ] Generate keys on-premises in HSM (Hardware Security Module)
  - [ ] Import keys to cloud KMS (AWS KMS BYOK, Azure Key Vault BYOK, GCP Cloud HSM)
  - [ ] Benefit: Customer controls key lifecycle (cloud provider never sees plaintext key)
- [ ] **Key Rotation**:
  - [ ] Automated key rotation (AWS KMS auto-rotation annually, manual for imported keys)
  - [ ] Re-encrypt data with new keys (automated re-encryption for S3, RDS)

**Hardware Security Modules (HSM)**:
- [ ] **Dedicated HSM**:
  - [ ] AWS CloudHSM, Azure Dedicated HSM, GCP Cloud HSM for cryptographic operations
  - [ ] Use Cases: Signing certificates, encrypting highly sensitive data, regulatory requirements (FIPS 140-2 Level 3)
  - [ ] Key storage: Private keys never leave HSM (tamper-resistant hardware)

#### 2.6 Automated Compliance Enforcement

**Policy as Code Frameworks**:
- [ ] **Open Policy Agent (OPA)**:
  - [ ] Define compliance policies in Rego language
  - [ ] Integrate with CI/CD (deny Terraform apply if violates policies)
  - [ ] Integrate with Kubernetes (deny pod creation if violates policies via Gatekeeper)
- [ ] **Cloud Custodian**:
  - [ ] Define policies in YAML (e.g., "Delete untagged resources after 7 days")
  - [ ] Automated enforcement (real-time or scheduled)
  - [ ] Multi-cloud support (AWS, Azure, GCP policies in one tool)

**Automated Remediation Frameworks**:
- [ ] **AWS Config Remediation**:
  - [ ] Config Rules trigger SSM Automation Documents (auto-remediate non-compliance)
  - [ ] Example: Unencrypted S3 bucket detected → Run SSM doc to enable encryption
- [ ] **Azure Policy Remediation**:
  - [ ] Deploy remediation tasks (automatically fix non-compliant resources)
  - [ ] Example: VM without disk encryption → Deploy policy to enable encryption
- [ ] **GCP Cloud Asset Inventory + Cloud Functions**:
  - [ ] Cloud Asset Inventory feeds → Cloud Functions → Auto-remediate non-compliance
  - [ ] Example: Public IP on VM → Cloud Function removes public IP

#### 2.7 Success Indicators for Level 2

**Automation Metrics**:
- [ ] ≥80% of compliance violations auto-remediated within ≤5 minutes
- [ ] ≥90% of infrastructure changes deployed via IaC (not manual console changes)
- [ ] Zero manual configuration changes (all via IaC, enforced via alerts on drift)

**Advanced Security Metrics**:
- [ ] Patch compliance: ≥95% of systems patched within SLA (critical ≤7 days, high ≤30 days)
- [ ] Vulnerability density: ≤5 high/critical vulnerabilities per 100 cloud resources
- [ ] EDR/XDR coverage: 100% of compute workloads protected

**Zero Trust Metrics**:
- [ ] 100% of access decisions based on identity (not network location)
- [ ] ≥90% of services use micro-segmentation (workload-level network policies)
- [ ] Average session duration ≤4 hours (short-lived tokens, continuous verification)

**Encryption Metrics**:
- [ ] 100% of sensitive data encrypted with customer-managed keys (BYOK)
- [ ] Key rotation: 100% of keys rotated annually (automated)
- [ ] HSM usage: 100% of cryptographic signing operations via HSM (for regulated data)

**Compliance Automation Metrics**:
- [ ] 100% of compliance policies defined as code (version controlled)
- [ ] Compliance drift: ≤1 hour from detection to remediation (real-time enforcement)
- [ ] Policy violations: ≤5 violations per week (measure policy effectiveness)

---

### Level 3: Research-Grade Environment Hardening

#### 3.1 Formal Verification of Hardening Policies

**Mathematical Proofs of Security Policies**:
- [ ] **Formal Verification of IAM Policies**:
  - [ ] Model IAM policies in formal logic (TLA+, Alloy)
  - [ ] Prove policies enforce least privilege (no unintended permissions)
  - [ ] Example proof: "No path exists for non-admin user to gain admin permissions"
  - [ ] Benefit: Mathematical guarantee of security properties
  - [ ] Publication: Publish formal verification methodology in academic venues
- [ ] **Network Security Formal Verification**:
  - [ ] Model network topology and security group rules in formal methods
  - [ ] Prove network isolation properties (e.g., "Production VPC cannot communicate with development VPC")
  - [ ] Automated verification: Re-verify on every security group change
  - [ ] Tools: Network policy verification tools, formal verification frameworks

**Provable Security Properties**:
- [ ] **Zero Trust Formal Verification**:
  - [ ] Prove every access decision requires authentication and authorization
  - [ ] Prove no "trusted network" bypasses (all access identity-based)
  - [ ] Result: Mathematical guarantee of Zero Trust architecture

#### 3.2 AI-Powered Auto-Remediation of Drift

**Autonomous Drift Remediation**:
- [ ] **Self-Healing Infrastructure**:
  - [ ] AI detects drift → Analyzes root cause → Auto-generates remediation → Executes remediation (autonomously)
  - [ ] Example: Security group rule changed manually → AI detects → Reverts to IaC state → Notifies operator
  - [ ] Safeguards: Blast radius limits, rollback on error, human override capability
  - [ ] Success Criteria: ≥90% of drift auto-remediated without human intervention
- [ ] **AI-Powered Remediation Optimization**:
  - [ ] AI learns from remediation outcomes → Improves remediation strategies
  - [ ] Reinforcement learning: AI tries remediation approaches → Learns which most effective
  - [ ] Result: Continuously improving remediation success rate

**Predictive Hardening**:
- [ ] **Predict and Prevent Misconfigurations**:
  - [ ] AI predicts likely misconfigurations based on historical patterns
  - [ ] Proactive hardening: Apply preventive controls before misconfiguration occurs
  - [ ] Example: "Resource type X often misconfigured → Apply extra validation before deployment"

#### 3.3 Research-Grade Security Controls

**Advanced Cryptography**:
- [ ] **Post-Quantum Cryptography**:
  - [ ] Implement post-quantum algorithms (NIST PQC standards)
  - [ ] Hybrid approach: Classical + post-quantum (transition period)
  - [ ] Use Cases: Long-term data encryption (data that must remain confidential for 10+ years)
- [ ] **Homomorphic Encryption for Cloud Data**:
  - [ ] Encrypt data, perform computations on encrypted data (never decrypt)
  - [ ] Use Cases: Privacy-preserving analytics, confidential computing
  - [ ] Research: Contribute to practical homomorphic encryption implementations

**Confidential Computing**:
- [ ] **Trusted Execution Environments (TEE)**:
  - [ ] AWS Nitro Enclaves, Azure Confidential Computing, GCP Confidential VMs
  - [ ] Encrypt data in use (not just at rest and in transit)
  - [ ] Use Cases: Process sensitive data in memory (encrypted even from cloud provider)
- [ ] **Secure Multi-Party Computation (SMPC)**:
  - [ ] Multiple parties compute on data without revealing inputs
  - [ ] Use Cases: Cross-organization analytics without sharing raw data

#### 3.4 Published Hardening Frameworks

**Open-Source Security Frameworks**:
- [ ] **Cloud Hardening Reference Architecture**:
  - [ ] Publish comprehensive hardening guide for multi-cloud environments
  - [ ] Content: IaC templates (Terraform modules), compliance policies (OPA/Rego), automation scripts
  - [ ] License: Open-source (Apache 2.0, MIT)
  - [ ] Community: Active community, regular updates, conference presentations
  - [ ] Success Criteria: ≥10,000 GitHub stars, adopted by ≥100 organizations
- [ ] **Automated Hardening Toolkit**:
  - [ ] CLI tool for automated cloud hardening (scan → detect issues → Auto-remediate)
  - [ ] Multi-cloud support (AWS, Azure, GCP)
  - [ ] Publication: Open-source tool, conference demos (Black Hat, DEF CON)

**Academic Research**:
- [ ] **Research Publications**:
  - [ ] Topics: Formal verification of cloud security, AI-powered auto-remediation, post-quantum cloud encryption
  - [ ] Venues: IEEE S&P, USENIX Security, ACM CCS, NDSS
  - [ ] Collaboration: Partner with universities for joint research
  - [ ] Impact: Advance state-of-the-art in cloud security hardening
  - [ ] Success Criteria: ≥2 peer-reviewed papers per year in top venues

**Industry Standards Contribution**:
- [ ] **Contribute to Security Standards**:
  - [ ] CIS Benchmarks: Propose new hardening controls, review existing controls
  - [ ] NIST Cybersecurity Framework: Contribute cloud security guidance
  - [ ] CSA (Cloud Security Alliance): Participate in working groups, contribute to CCM (Cloud Controls Matrix)
  - [ ] Impact: Shape industry standards, broad adoption of best practices

#### 3.5 Industry-Leading Hardening Metrics

**Comprehensive Hardening Coverage**:
- [ ] **100% Automated Hardening**: All hardening controls deployed via IaC, no manual configuration
- [ ] **Zero Trust Compliance**: 100% of access decisions identity-based (no network-based trust)
- [ ] **Encryption Everywhere**: 100% of data encrypted at rest, in transit, and in use (confidential computing)
- [ ] **Real-Time Compliance**: ≥99% of compliance violations remediated within ≤5 minutes (automated enforcement)

**Advanced Security Metrics**:
- [ ] Formal verification coverage: ≥50% of critical security policies formally verified
- [ ] AI-powered remediation: ≥90% of drift auto-remediated autonomously (no human intervention)
- [ ] Post-quantum cryptography: ≥50% of long-term data encrypted with post-quantum algorithms
- [ ] Confidential computing: ≥30% of sensitive workloads use TEEs (data encrypted in use)

**Research and Publication Metrics**:
- [ ] Academic publications: ≥2 peer-reviewed papers per year in top security venues
- [ ] Open-source impact: Published hardening framework with ≥10,000 GitHub stars, adopted by ≥100 organizations
- [ ] Standards contribution: Active participation in ≥3 industry standards bodies (CIS, NIST, CSA)
- [ ] Conference presentations: ≥3 presentations per year at major conferences (Black Hat, DEF CON, RSA)

**Industry Leadership Metrics**:
- [ ] Thought leadership: Recognized as industry leader in cloud security hardening
- [ ] Community impact: Open-source framework widely adopted, shaping industry practices
- [ ] Innovation: Novel techniques (formal verification, AI remediation, post-quantum crypto) published and adopted

#### 3.6 Success Indicators for Level 3

**Formal Verification Metrics**:
- [ ] Security policies formally verified: ≥50% of critical IAM policies, network policies have formal proofs
- [ ] Zero Trust formally verified: Mathematical proof of Zero Trust architecture compliance
- [ ] Network isolation formally verified: Proof of network segmentation properties

**AI and Automation Metrics**:
- [ ] Autonomous drift remediation: ≥90% of configuration drift auto-remediated without human intervention
- [ ] AI remediation accuracy: ≥95% of AI-generated remediations successful (no rollbacks required)
- [ ] Predictive hardening: ≥30% of misconfigurations prevented via predictive controls

**Advanced Cryptography Metrics**:
- [ ] Post-quantum cryptography: ≥50% of long-term encrypted data uses post-quantum algorithms
- [ ] Confidential computing: ≥30% of sensitive workloads use TEEs (encrypted in use)
- [ ] Homomorphic encryption: ≥5 use cases of privacy-preserving computation in production

**Research and Publication Metrics**:
- [ ] Academic publications: ≥2 peer-reviewed papers per year in top security venues
- [ ] Open-source impact: Published framework with ≥10,000 GitHub stars, ≥100 organizational adoptions
- [ ] Standards contribution: Contributed to ≥3 industry standards (CIS, NIST, CSA)
- [ ] Conference presentations: ≥3 presentations per year at Black Hat, DEF CON, RSA, USENIX Security

**Industry Leadership Metrics**:
- [ ] Thought leadership: Top 10 most influential voices in cloud security hardening
- [ ] Community impact: Framework cited in ≥50 academic papers, industry publications
- [ ] Innovation: Novel hardening techniques adopted by ≥20 peer organizations
- [ ] Industry recognition: Awards for security innovation, invited keynote speaking

---

**Document Information**: Practice: Environment Hardening (EH) | Domain: Infrastructure | HAIAMM v2.1 | Last Updated: 2025-12-30
