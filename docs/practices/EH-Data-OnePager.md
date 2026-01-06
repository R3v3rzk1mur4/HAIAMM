# Environment Hardening Practice – Data Domain
## HAIAMM v2.1 One-Pager

### Practice Overview

Environment Hardening for Data ensures AI data security systems are deployed with secure data storage configurations, minimal data exposure, strong encryption, least privilege data access, defense-in-depth data protection controls, and resilient data infrastructure to protect sensitive information and maintain privacy.

**Scope**: Hardening for:
- Data storage (databases, object storage, data warehouses, file systems)
- Data classification and labeling infrastructure
- Data Loss Prevention (DLP) systems and policies
- Privacy-preserving technologies (differential privacy, federated learning, homomorphic encryption)
- Data access control systems (IAM, RBAC, ABAC)
- Data encryption infrastructure (key management, TLS, at-rest encryption)
- Data retention and disposal systems
- Compliance automation (GDPR, CCPA, HIPAA, PCI-DSS)

**Why This Matters**: Data is the organization's most valuable asset and largest attack surface. Secure-by-default data infrastructure, encryption, least-privilege access, and defense-in-depth reduce the risk of data breaches, ensure compliance, protect user privacy, and limit blast radius of successful attacks.

---

### Level 1: Foundational Environment Hardening

### Core Objectives
1. Establish secure baseline configurations for all data storage systems
2. Implement encryption at rest and in transit for all sensitive data
3. Enforce least privilege data access controls
4. Harden Data Loss Prevention (DLP) systems
5. Secure privacy-preserving AI infrastructure
6. Automate compliance enforcement (GDPR, CCPA, HIPAA, PCI-DSS)
7. Maintain data security hardening standards and continuous validation

### Key Activities

#### 1. Data Storage Hardening

**Database Hardening**:
- [ ] **Authentication Hardening**: Secure database authentication
  - Remove Default Credentials: Change/remove default passwords (postgres, root, admin)
  - Strong Passwords: Enforce strong password policy (≥16 chars, complexity, no dictionary words)
  - Key-Based Authentication: Prefer certificate/key-based auth over passwords
  - MFA: Require MFA for administrative database access
  - No Anonymous Access: Disable anonymous/guest accounts
- [ ] **Network Hardening**: Restrict database network access
  - Bind to Private IPs: Never bind to 0.0.0.0 (all interfaces), use private IPs only
  - Firewall Rules: Allow only required sources (application servers), deny all else
  - No Public Access: Never expose databases to public internet
  - VPN/Bastion Access: Require VPN or bastion host for administrative access
- [ ] **Encryption Hardening**:
  - [ ] **Encryption at Rest**: Enable Transparent Data Encryption (TDE)
    - Databases: PostgreSQL (pgcrypto), MySQL (InnoDB encryption), SQL Server (TDE), MongoDB (encryption at rest)
    - Algorithm: AES-256
    - Key Management: Use external KMS (AWS KMS, Azure Key Vault), rotate keys annually
  - [ ] **Encryption in Transit**: Require TLS for all database connections
    - Version: TLS 1.3 (or TLS 1.2 minimum)
    - Certificate Validation: Enforce certificate validation, reject self-signed certs
    - Cipher Suites: Use strong cipher suites only
- [ ] **Authorization Hardening**: Least privilege database permissions
  - Application Accounts: Grant only required permissions (SELECT, INSERT, UPDATE on specific tables)
  - Read-Only Accounts: Create separate read-only accounts for analytics, reporting
  - No SUPERUSER: Avoid SUPERUSER/root for application accounts
  - Row-Level Security: Implement row-level security (RLS) for multi-tenant databases
  - Column-Level Security: Encrypt or restrict access to sensitive columns (PII, PHI, PCI)
- [ ] **Configuration Hardening**:
  - [ ] Disable unnecessary features (remote file access, external scripts, xp_cmdshell)
  - [ ] Enable query logging for sensitive tables
  - [ ] Set connection limits (prevent resource exhaustion)
  - [ ] Configure timeouts (idle connection timeout, query timeout)
  - [ ] Apply CIS Benchmarks (CIS PostgreSQL, MySQL, MongoDB, SQL Server)
- [ ] **Patching**: Keep databases fully patched
  - SLA: Critical patches ≤48 hours, High ≤7 days, Medium ≤30 days
  - Testing: Test patches in staging before production
  - Automation: Automated patching where possible (managed databases)

**Object Storage Hardening (S3, Azure Blob, GCS)**:
- [ ] **Public Access Blocking**: Prevent public data exposure
  - AWS S3: Enable S3 Block Public Access (account-level, bucket-level)
  - Azure Blob: Set containers to private (no anonymous access)
  - GCS: Set buckets to private, use IAM for access control
  - Validation: Scan for publicly accessible buckets/objects (tools: ScoutSuite, Prowler)
- [ ] **Encryption Hardening**:
  - [ ] **Encryption at Rest**: Enforce server-side encryption
    - AWS S3: Use SSE-KMS (customer-managed keys), not SSE-S3
    - Azure Blob: Use customer-managed keys in Key Vault
    - GCS: Use CMEK (Customer-Managed Encryption Keys)
    - Policy: Bucket policies require encryption (reject unencrypted uploads)
  - [ ] **Encryption in Transit**: Require HTTPS for all access
    - Policy: Deny HTTP requests, allow only HTTPS
    - TLS Version: TLS 1.2+ required
- [ ] **Access Control Hardening**:
  - [ ] Least Privilege IAM: Grant minimal required permissions (read-only vs write)
  - [ ] Bucket Policies: Use bucket policies to enforce access restrictions
  - [ ] Pre-Signed URLs: Use time-limited pre-signed URLs for temporary access
  - [ ] No Wildcard Permissions: Avoid `s3:*` or `storage.*`, specify actions explicitly
- [ ] **Versioning and Lifecycle**:
  - [ ] Enable Versioning: Protect against accidental deletion, ransomware
  - [ ] Lifecycle Policies: Auto-delete old versions after retention period
  - [ ] Object Lock: Enable WORM (Write Once Read Many) for compliance (S3 Object Lock, Azure Blob immutability)
- [ ] **Access Logging**: Enable and monitor access logs
  - AWS S3: Enable S3 Server Access Logging or CloudTrail Data Events
  - Azure Blob: Enable Storage Analytics logging
  - GCS: Enable Access Logs and Data Access Audit Logs
  - SIEM: Send logs to SIEM for analysis
- [ ] **Cross-Region Replication**: Replicate sensitive data for DR
  - Method: S3 Cross-Region Replication, Azure Blob Replication, GCS Multi-Region
  - Encryption: Replicate encrypted data with KMS key replication

**Data Lake/Warehouse Hardening**:
- [ ] **Big Data Platform Hardening** (Hadoop, Spark, Databricks, Snowflake, BigQuery, Redshift):
  - [ ] **Authentication**: Strong authentication mechanisms
    - Hadoop: Kerberos for authentication, no simple auth in production
    - Cloud Warehouses: SSO integration (SAML, OAuth), MFA for admin accounts
  - [ ] **Encryption**:
    - At Rest: Enable encryption for HDFS, S3, warehouse storage
    - In Transit: TLS for all client-server, server-server communication
  - [ ] **Access Control**:
    - Fine-Grained: Column-level, row-level security (Snowflake RLS, BigQuery column-level security, Redshift column-level encryption)
    - Least Privilege: Grant access only to required tables/columns/rows
    - Dynamic Masking: Mask sensitive data for unauthorized users
  - [ ] **Network Isolation**: Private networks for data platforms
    - No Public Access: Use private endpoints, VPC peering
    - Network Segmentation: Isolate data platform from general network

**File System and File Share Hardening**:
- [ ] **Network File Share Hardening** (NFS, SMB, CIFS):
  - [ ] Restrict Access: Limit access to specific IPs/hosts (NFS exports, SMB ACLs)
  - [ ] Encryption: Use encrypted protocols (NFSv4 with Kerberos, SMB3 encryption)
  - [ ] Authentication: Require authentication (no anonymous shares)
  - [ ] Permissions: Least privilege file permissions (read-only where possible)
- [ ] **Distributed File System Hardening** (HDFS, GlusterFS):
  - [ ] Authentication: Kerberos for HDFS, strong authentication for GlusterFS
  - [ ] Encryption: HDFS encryption zones, GlusterFS client-server encryption
  - [ ] Permissions: HDFS permissions, ACLs for fine-grained control

#### 2. Encryption Infrastructure Hardening

**Encryption at Rest Hardening**:
- [ ] **Full-Disk Encryption**: Encrypt all storage volumes
  - Methods: LUKS (Linux), BitLocker (Windows), FileVault (macOS)
  - Cloud: Enable encrypted EBS volumes (AWS), encrypted disks (Azure/GCP)
  - Purpose: Protect data if physical media stolen/lost
- [ ] **Application-Level Encryption**: Encrypt sensitive data at application layer
  - Use Cases: Sensitive columns (credit card, SSN), PII fields
  - Libraries: Use encryption libraries (NaCl, libsodium, AWS Encryption SDK)
  - Key Management: Store encryption keys in KMS, not in database
- [ ] **Algorithm Selection**: Use strong encryption algorithms
  - Symmetric: AES-256-GCM (authenticated encryption), ChaCha20-Poly1305
  - Asymmetric: RSA-4096, Ed25519, ECDSA (P-256 or higher)
  - Avoid: DES, 3DES, RC4, MD5, SHA-1 (deprecated/broken algorithms)

**Encryption in Transit Hardening**:
- [ ] **TLS Configuration Hardening**:
  - [ ] **TLS Version**: TLS 1.3 preferred, TLS 1.2 minimum (disable TLS 1.0, 1.1, SSLv3)
  - [ ] **Cipher Suites**: Use strong cipher suites only
    - Prefer: ECDHE-RSA-AES256-GCM-SHA384, ECDHE-RSA-CHACHA20-POLY1305
    - Disable: Weak ciphers (RC4, DES, 3DES, export ciphers), null ciphers
    - Forward Secrecy: Require ECDHE or DHE (perfect forward secrecy)
  - [ ] **Certificate Validation**: Enforce strict certificate validation
    - No Self-Signed: Reject self-signed certificates in production
    - Certificate Pinning: Pin certificates for critical services
    - Revocation Checking: Check certificate revocation (OCSP, CRL)
- [ ] **Certificate Management**:
  - [ ] **Automated Issuance**: Use automated certificate management
    - Tools: Let's Encrypt, cert-manager (Kubernetes), AWS ACM
    - Benefit: Prevents expired certificates, reduces manual effort
  - [ ] **Certificate Rotation**: Rotate certificates before expiration
    - Monitoring: Alert when certificates ≤30 days from expiration
    - Automation: Automated rotation where possible
  - [ ] **Private Key Protection**: Secure private keys
    - Storage: Store in HSM (Hardware Security Module) or KMS
    - Permissions: Restrict key file permissions (chmod 600)
    - No Sharing: Never share private keys across systems
- [ ] **mTLS for Service-to-Service**: Mutual TLS for internal services
  - Implementation: Service mesh (Istio, Linkerd, Consul Connect), manual mTLS
  - Benefit: Authenticate both client and server, encrypt all internal traffic
  - Scope: Data classification service ↔ database, DLP ↔ data stores

**Key Management Hardening**:
- [ ] **Key Management Service (KMS) Usage**: Centralize key management
  - Tools: AWS KMS, Azure Key Vault, GCP Cloud KMS, HashiCorp Vault
  - Scope: All encryption keys (data encryption keys, TLS keys, API keys)
  - Benefit: Centralized key lifecycle management, audit logging, access control
- [ ] **Key Hierarchy**: Implement key hierarchy (KEK and DEK)
  - KEK: Key Encryption Key (master key, stored in KMS/HSM)
  - DEK: Data Encryption Key (encrypts actual data, encrypted by KEK)
  - Benefit: Rotate DEKs without re-encrypting data, KEK in hardware
- [ ] **Key Rotation**: Rotate encryption keys regularly
  - Frequency: Data encryption keys annually, master keys every 2-3 years
  - Compromised Keys: Immediate rotation if compromise suspected
  - Automation: Automated rotation with zero downtime
- [ ] **Key Access Control**: Least privilege key access
  - Principle: Only services that encrypt/decrypt data can access keys
  - IAM: Use IAM policies to restrict key usage (kms:Encrypt, kms:Decrypt)
  - Auditing: Log all key usage (who accessed which key, when, for what purpose)
- [ ] **Key Backup and Recovery**: Secure key backups
  - Backup: Encrypted backups of keys (protect with separate KEK)
  - Storage: Store backups in separate region/account
  - Recovery: Documented key recovery procedures, tested annually
- [ ] **Hardware Security Modules (HSM)**: Use HSMs for critical keys
  - Purpose: Store master keys in tamper-resistant hardware
  - Options: AWS CloudHSM, Azure Dedicated HSM, on-premise HSMs
  - Use Cases: Root keys, payment processing keys, high-value secrets

#### 3. Data Access Control Hardening

**Identity and Access Management (IAM) Hardening**:
- [ ] **Least Privilege Principle**: Grant minimal required data access
  - Approach: Start with zero access, add only required permissions
  - Granularity: Database-level, table-level, column-level, row-level, object-level
  - Review: Quarterly access reviews, remove unused permissions
  - Tools: AWS IAM Access Analyzer, Azure Access Reviews, GCP IAM Recommender
- [ ] **Role-Based Access Control (RBAC)**: Assign roles, not individual permissions
  - Roles: Define roles by job function (analyst, engineer, admin)
  - Assignment: Assign users to roles, not direct permissions
  - Benefit: Easier management, consistent permissions, audit trail
- [ ] **Attribute-Based Access Control (ABAC)**: Dynamic access based on attributes
  - Attributes: Department, clearance level, data classification, location
  - Policy: Access granted if attributes match (e.g., HR dept can access HR data)
  - Implementation: OPA (Open Policy Agent), cloud IAM conditions
- [ ] **Service Accounts**: Dedicated accounts per service
  - Isolation: Each service has dedicated account, no shared credentials
  - Permissions: Minimal permissions for each service account
  - Rotation: Rotate service account credentials regularly (quarterly)
- [ ] **Break-Glass Accounts**: Emergency access accounts
  - Purpose: Access when primary authentication unavailable (MFA device lost)
  - Security: Highly monitored, MFA required, auto-alert on use
  - Review: Monthly review of break-glass account usage

**Authentication Hardening**:
- [ ] **Strong Password Policies**: Enforce strong passwords
  - Length: Minimum 12 characters (16+ for privileged accounts)
  - Complexity: Mix of uppercase, lowercase, numbers, symbols
  - No Common Passwords: Block common passwords (Have I Been Pwned API)
  - Expiration: Consider passwordless or long expiration (90+ days) with breach monitoring
- [ ] **Multi-Factor Authentication (MFA)**: Require MFA for data access
  - Scope: All users, especially privileged accounts (admins, DBAs, analysts)
  - Methods: Hardware keys (WebAuthn, FIDO2), TOTP (Google Authenticator), biometrics
  - Avoid: SMS (SIM swapping risk), use as last resort only
  - Conditional MFA: Require MFA for sensitive data access, high-risk locations
- [ ] **Passwordless Authentication**: Eliminate password risks
  - Methods: WebAuthn/FIDO2 (hardware keys), certificate-based auth
  - Benefit: No password to steal, phishing-resistant
- [ ] **SSO Integration**: Centralize authentication
  - Protocols: SAML, OAuth 2.0, OpenID Connect
  - Providers: Okta, Azure AD, Google Workspace, Auth0
  - Benefit: Single point of authentication, easier MFA enforcement

**Authorization Hardening**:
- [ ] **Database-Level Access Control**: Control database access
  - Grants: GRANT/REVOKE permissions on databases, tables, columns
  - Least Privilege: Application users have minimal required permissions (no DROP, TRUNCATE)
  - No Wildcards: Avoid GRANT ALL, specify exact permissions
- [ ] **Row-Level Security (RLS)**: Filter rows based on user
  - Use Cases: Multi-tenant databases (users see only their tenant's data), role-based filtering
  - Implementation: PostgreSQL RLS, Oracle VPD, SQL Server RLS
  - Example: Sales rep sees only their region's data
- [ ] **Column-Level Security**: Restrict access to sensitive columns
  - Methods: Column-level permissions (GRANT SELECT on specific columns), dynamic data masking
  - Use Cases: Hide SSN, credit card from unauthorized users
  - Implementation: PostgreSQL column-level GRANT, SQL Server column-level permissions
- [ ] **Dynamic Data Masking**: Mask sensitive data for unauthorized users
  - Method: Return masked version of data (XXX-XX-1234 instead of full SSN)
  - Scope: PII, PHI, PCI data
  - Implementation: SQL Server Dynamic Data Masking, Azure SQL Data Masking, custom views
- [ ] **Policy-Based Access Control**: Centralized policy enforcement
  - Tools: Open Policy Agent (OPA), AWS IAM Policies, Azure Policy
  - Policies: Define access rules centrally, enforce consistently
  - Benefits: Audit trail, version control for policies, separation of policy from code

**Privileged Access Management (PAM)**:
- [ ] **Just-In-Time (JIT) Access**: Temporary elevated access
  - Approach: Request elevated access, auto-expire after time limit (e.g., 2 hours)
  - Approval: Require manager/security approval for JIT access
  - Tools: AWS IAM Access Analyzer, Azure PIM, Google Cloud IAM
- [ ] **Bastion/Jump Host**: Centralize privileged data access
  - Approach: All database admin access via bastion host
  - Logging: Session recording, keystroke logging for audit
  - MFA: Require MFA for bastion access
- [ ] **Credential Vaulting**: Secure privileged credentials
  - Tools: CyberArk, HashiCorp Vault, AWS Secrets Manager
  - Rotation: Automated credential rotation (daily or weekly)
  - Checkout/Checkin: Credentials checked out for use, checked in after, rotated

#### 4. Data Classification Infrastructure Hardening

**Classification Model Hardening**:
- [ ] **Model Security**: Secure AI classification models
  - Access Control: Restrict access to model files, weights
  - Encryption: Encrypt model files at rest
  - Integrity: Sign models, verify signatures before loading
  - Versioning: Track model versions, roll back if compromised
- [ ] **Training Data Protection**: Secure classification training data
  - Sensitivity: Training data contains sensitive examples (PII, PHI)
  - Access Control: Restrict access to training data
  - Encryption: Encrypt training data at rest and in transit
  - Privacy: Use differential privacy in training to prevent data leakage

**Classification Enforcement Hardening**:
- [ ] **Automated Classification**: Classify data at creation
  - Trigger: Auto-classify when data created, uploaded, modified
  - Tagging: Apply classification labels (metadata tags, database columns)
  - Validation: Validate classification accuracy, human review for low confidence
- [ ] **Classification-Based Controls**: Enforce security per classification
  - Restricted Data:
    - Encryption: AES-256 at rest, TLS 1.3 in transit
    - Access: MFA required, least privilege, audit all access
    - DLP: Block external sharing, allow only to authorized users
    - Retention: Minimum retention per regulation (GDPR, HIPAA)
  - Confidential Data:
    - Encryption: AES-256 at rest, TLS 1.2+ in transit
    - Access: Least privilege, audit access
    - DLP: Alert on external sharing, block to public
  - Internal Data:
    - Encryption: Recommended
    - Access: Standard access controls
  - Public Data:
    - Minimal controls
- [ ] **Classification Validation**: Verify classification accuracy
  - Sampling: Sample classified data, manual review (≥100 samples/month)
  - Accuracy Target: ≥90% classification accuracy
  - Reclassification: Reclas sify if accuracy drops or policy changes

#### 5. DLP System Hardening

**DLP Policy Hardening**:
- [ ] **Policy Configuration**: Secure DLP policy settings
  - Default Action: Block by default for Restricted data to external destinations
  - Justification Required: Require business justification for policy overrides
  - Approval Workflow: Manager approval required for Restricted data sharing
  - Audit Logging: Log all DLP events (blocks, alerts, overrides)
- [ ] **DLP Channel Coverage**: Enable DLP on all exfiltration channels
  - Email: SMTP, webmail (Gmail, Outlook.com)
  - Chat: Slack, Teams, Discord, internal chat
  - File Upload: Web uploads, cloud storage (personal Dropbox, Drive)
  - Clipboard: Copy/paste monitoring
  - Cloud Sync: OneDrive, iCloud, Google Drive sync clients
  - Removable Media: USB drives, external disks
  - Print: Print job inspection
  - Screen Capture: Screenshot/screen recording detection (if feasible)
  - Coverage Target: 100% of defined channels
- [ ] **DLP Evasion Prevention**: Harden against DLP bypasses
  - Encoding Detection: Detect base64, hex, URL encoding
  - Obfuscation Detection: Detect typos, spacing, leetspeak
  - Channel Hopping Detection: Correlate user behavior across channels
  - Fragmentation Detection: Detect PII sent in pieces

**DLP Infrastructure Hardening**:
- [ ] **DLP Agent Security**: Secure endpoint DLP agents
  - Tamper Protection: Prevent agent uninstall/disable by users
  - Updates: Automated agent updates, vulnerability patching
  - Monitoring: Alert if agent stops reporting, disabled, or crashes
- [ ] **DLP Gateway Security**: Secure network DLP gateways
  - High Availability: Redundant DLP gateways (no single point of failure)
  - Performance: Ensure DLP doesn't bottleneck network (≤100ms latency)
  - Failover: Fail-safe mode (block/alert-only if DLP unavailable, per policy)

#### 6. Privacy-Preserving Technology Hardening

**Differential Privacy Hardening**:
- [ ] **Privacy Budget Enforcement**: Strictly enforce epsilon budget
  - Configuration: Set epsilon budget (ε ≤ 8 for Level 1)
  - Tracking: Track budget consumption per query, per user, per dataset
  - Blocking: Automatically block queries when budget exhausted (100% consumed)
  - Alerts: Alert at 80%, 95%, 100% budget consumption
- [ ] **Noise Implementation Security**: Validate noise addition
  - Correctness: Verify noise magnitude matches epsilon/delta parameters
  - Source: Use cryptographically secure random number generator (CSPRNG) for noise
  - Testing: Periodic testing to ensure noise correctly applied (see ST-Data)
- [ ] **Query Validation**: Validate queries against privacy attacks
  - Detection: Detect membership inference, model inversion attempts (see ST-Data)
  - Throttling: Rate limit queries to prevent privacy attacks
  - Auditing: Log all queries, anomaly detection for suspicious patterns

**Federated Learning Hardening**:
- [ ] **Client Authentication**: Authenticate all federated learning participants
  - Method: Client certificates, OAuth tokens
  - Validation: Verify client identity before accepting model updates
- [ ] **Model Update Validation**: Validate model updates for attacks
  - Byzantine Detection: Detect poisoned gradients, reject malicious updates
  - Differential Privacy: Add noise to gradients for privacy
  - Secure Aggregation: Use secure multi-party computation for aggregation
- [ ] **Communication Security**: Encrypt federated learning communication
  - Encryption: TLS 1.3 for all client-server communication
  - Payload: Encrypt model updates, validate integrity (HMAC)

**Homomorphic Encryption Hardening**:
- [ ] **HE Library Security**: Use secure homomorphic encryption libraries
  - Libraries: Microsoft SEAL, PALISADE, HElib (peer-reviewed, maintained)
  - Configuration: Use secure parameters (prevent attacks)
  - Updates: Keep libraries updated (patch vulnerabilities)
- [ ] **Key Management**: Secure homomorphic encryption keys
  - Storage: Store HE keys in KMS
  - Access Control: Least privilege access to HE keys
  - Rotation: Rotate HE keys per policy (annually)

#### 7. Data Retention and Disposal Hardening

**Retention Policy Enforcement**:
- [ ] **Automated Retention Policies**: Define and enforce retention periods
  - By Classification:
    - Restricted: Minimum retention per regulation (GDPR variable, HIPAA 6 years, PCI-DSS 1 year)
    - Confidential: 3-7 years (business requirement)
    - Internal: 1-3 years
    - Public: No retention limit
  - By Data Type:
    - Logs: 90 days hot, 1 year cold (security logs), 3+ years (compliance logs)
    - Backups: 30 days (operational), 1+ years (compliance)
    - User Data: Per privacy policy and regulation
- [ ] **Automated Data Deletion**: Auto-delete data after retention period
  - Frequency: Daily automated deletion job
  - Scope: Production databases, backups, logs, caches, archives (delete everywhere)
  - Verification: Verify deletion successful, data irrecoverable
- [ ] **Retention Holds**: Support legal holds, litigation holds
  - Mechanism: Flag data for hold (prevent auto-deletion)
  - Approval: Require legal approval for holds
  - Removal: Auto-remove hold when legal matter resolved

**Secure Data Disposal**:
- [ ] **Crypto-Shredding**: Delete encryption keys to render data unreadable
  - Method: Delete DEK (Data Encryption Key), data becomes gibberish
  - Benefit: Fast, effective for encrypted data
  - Validation: Verify keys deleted, data undecryptable
- [ ] **Data Overwriting**: Overwrite data multiple times
  - Method: DoD 5220.22-M (7-pass overwrite), NIST 800-88
  - Use Cases: Unencrypted data, physical media disposal
  - Validation: Verify data overwritten (cannot be recovered)
- [ ] **Physical Media Destruction**: Destroy physical storage media
  - Methods: Shredding, degaussing, incineration
  - Use Cases: Decommissioned disks, retired hardware
  - Certification: Certificate of destruction for compliance
- [ ] **Deletion Verification**: Verify complete data removal
  - Scope: Production, backups, replicas, caches, logs, archives
  - Method: Query for deleted data, verify zero results
  - Audit: Log deletion verification results

#### 8. Compliance Automation Hardening

**GDPR Compliance Hardening**:
- [ ] **Data Subject Rights Automation**: Automate GDPR rights
  - Right of Access (Article 15): Auto-export user data within 30 days
  - Right to Erasure (Article 17): Auto-delete user data within 30 days (see secure disposal above)
  - Right to Portability (Article 20): Export in machine-readable format (JSON, CSV)
  - Right to Rectification (Article 16): Provide data correction interface
- [ ] **Consent Management**: Track and enforce consent
  - Collection: Log consent (purpose, timestamp, user)
  - Storage: Store consent records for 3+ years
  - Withdrawal: Honor consent withdrawal within 30 days
  - Granular: Separate consent for different purposes (marketing, analytics, AI training)
- [ ] **Privacy by Design (Article 25)**: Build privacy into data systems
  - Encryption: Encrypt all PII by default
  - Data Minimization: Collect only necessary data
  - Anonymization: Anonymize data for analytics, testing
- [ ] **Data Protection Impact Assessment (DPIA) (Article 35)**: Assess high-risk processing
  - Trigger: Automated DPIA for high-risk processing (large-scale PII, automated decision-making)
  - Review: DPO review and approval required
  - Documentation: Maintain DPIA records for audits

**CCPA Compliance Hardening**:
- [ ] **Consumer Rights Automation**: Automate CCPA rights
  - Right to Know: Auto-provide data disclosure within 45 days
  - Right to Delete: Auto-delete consumer data within 45 days
  - Right to Opt-Out: Honor do-not-sell within 15 days, display opt-out link
  - Non-Discrimination: Ensure equal service for opted-out consumers
- [ ] **Do Not Sell Enforcement**: Implement do-not-sell mechanism
  - Opt-Out Link: Prominent "Do Not Sell My Personal Information" link
  - Enforcement: Verify data not sold/shared after opt-out
  - Validation: Audit third-party data sharing compliance

**HIPAA Compliance Hardening** (for healthcare PHI):
- [ ] **PHI Encryption**: Encrypt all Protected Health Information
  - At Rest: AES-256 encryption for all PHI storage
  - In Transit: TLS 1.2+ for all PHI transmission
  - Compliance: HIPAA Security Rule requires encryption as "addressable"
- [ ] **Minimum Necessary**: Enforce minimum necessary PHI access
  - Access Control: Users access only minimum PHI for job function
  - Monitoring: Alert on excessive PHI access (>100 patient records/day without justification)
- [ ] **Business Associate Agreements (BAA)**: Manage BAAs
  - Requirement: Signed BAA before sharing PHI with vendors
  - Tracking: Track BAA status for all vendors
  - Alerts: Alert on PHI sharing without BAA (HIPAA violation)
- [ ] **Breach Notification**: Automate breach detection and notification
  - Detection: Automated detection of PHI breaches (unauthorized access, exfiltration)
  - Timeline: Notify individuals within 60 days of discovery
  - Reporting: Report breaches affecting >500 individuals to HHS

**PCI-DSS Compliance Hardening** (for payment card data):
- [ ] **Cardholder Data Environment (CDE) Segmentation**: Isolate CDE
  - Network: Separate CDE from general network (VLAN, firewall)
  - Access: Restrict access to CDE (least privilege, MFA)
  - Scope: Minimize CDE scope (reduce systems storing cardholder data)
- [ ] **Card Data Encryption**: Encrypt all cardholder data
  - Storage: AES-256 encryption for stored card data
  - Transmission: TLS 1.2+ for card data transmission
  - Truncation: Store only last 4 digits when possible (truncate rest)
- [ ] **Card Data Retention Limits**: Enforce 90-day retention limit
  - Auto-Deletion: Delete card data >90 days old
  - Justification: Require business justification to extend retention
  - Audit: Verify no card data >90 days old

#### 9. Backup Security Hardening

**Backup Encryption**:
- [ ] **Encrypt All Backups**: Encrypt backups before storage
  - Method: Client-side encryption (encrypt before sending to backup storage)
  - Key Management: Use separate encryption keys for backups (not production keys)
  - Algorithm: AES-256-GCM
- [ ] **Backup Key Security**: Secure backup encryption keys
  - Storage: Store backup keys in KMS, separate from production keys
  - Access: Least privilege access to backup keys
  - Rotation: Rotate backup keys annually

**Backup Access Control**:
- [ ] **Separate Backup Access**: Isolate backup access from production
  - Principle: Production admin ≠ backup admin (prevent insider attack)
  - Accounts: Separate accounts for backup access
  - MFA: Require MFA for backup access and restoration
- [ ] **Immutable Backups**: Prevent backup deletion/modification
  - Methods: S3 Object Lock (retention mode), Azure Blob immutability policies
  - Benefit: Ransomware protection (backups can't be encrypted/deleted)
  - Duration: Immutability period matches retention requirement

**Backup Testing**:
- [ ] **Restore Testing**: Validate backups are recoverable
  - Frequency: Quarterly full restore tests
  - Scope: Test restore to separate environment, validate data integrity
  - Metrics: Measure RTO (Recovery Time Objective), RPO (Recovery Point Objective)
  - Documentation: Document restore procedures, update runbooks
- [ ] **Backup Monitoring**: Monitor backup success
  - Metrics: Backup success rate (target: ≥99.9%), backup age, backup size
  - Alerts: Alert on backup failures, missing backups (>24 hours)

**Backup Storage Security**:
- [ ] **Geo-Redundancy**: Store backups in separate geographic region
  - Method: Cross-region replication (AWS, Azure, GCP)
  - Benefit: Disaster recovery (region failure doesn't affect backups)
- [ ] **Air-Gapped Backups**: Offline backups for critical data
  - Method: Periodic backups to disconnected storage (tape, offline disks)
  - Frequency: Monthly or quarterly
  - Benefit: Protection against ransomware, network-based attacks

#### 10. Data Lineage and Provenance Hardening

**Lineage Infrastructure Security**:
- [ ] **Lineage Metadata Protection**: Secure data lineage metadata
  - Encryption: Encrypt lineage graphs, metadata
  - Access Control: Restrict access to lineage data (reveals data flows)
  - Integrity: Tamper-proof lineage (cryptographic signatures)
- [ ] **Lineage Validation**: Verify lineage accuracy
  - Auditing: Periodic audits of lineage data
  - Alerts: Alert on lineage gaps (untracked data flows)

---

### Key Success Indicators

**Configuration Compliance**:
1. **Database Hardening**: ≥95% databases comply with CIS Benchmarks
2. **Object Storage Security**: Zero publicly accessible buckets/objects
3. **Encryption Coverage**: 100% sensitive data encrypted at rest and in transit

**Access Control**:
1. **Least Privilege**: ≥90% data access follows least privilege
2. **MFA Adoption**: 100% privileged data access uses MFA
3. **Unused Credentials**: Zero unused credentials >90 days old

**Encryption**:
1. **Encryption at Rest**: 100% sensitive data encrypted at rest (AES-256)
2. **Encryption in Transit**: 100% data connections use TLS 1.2+ (prefer TLS 1.3)
3. **Key Rotation**: ≥95% keys rotated per policy

**Data Classification**:
1. **Classification Coverage**: 100% data classified
2. **Classification Accuracy**: ≥90% automatic classification accuracy
3. **Enforcement**: 100% classification-based controls enforced

**DLP Effectiveness**:
1. **Exfiltration Prevention**: ≥85% exfiltration attempts blocked
2. **False Positive Rate**: ≤5% false positive rate
3. **Channel Coverage**: 100% defined DLP channels active

**Compliance**:
1. **Retention Enforcement**: 100% data retention policies automated
2. **GDPR Compliance**: 100% data subject requests completed within 30 days
3. **Privacy Violations**: Zero privacy budget exhaustion events

---

## Level 2: Comprehensive Environment Hardening

### Enhanced Practices

**Immutable Data Infrastructure**:
- [ ] **Immutable Storage**: No runtime modifications, versioned data
  - Approach: Write-once storage, versioning for all changes
  - Benefit: Audit trail, ransomware protection, rollback capability
- [ ] **Infrastructure as Code (IaC)**: Data infrastructure defined as code
  - Tools: Terraform, CloudFormation, ARM templates
  - Version Control: Git for all infrastructure changes
  - Validation: Automated security scanning of IaC (Checkov, tfsec)

**Automated Hardening Validation**:
- [ ] **Continuous Compliance Scanning**: Automated hardening validation
  - Tools: AWS Config, Azure Policy, GCP Security Command Center
  - Frequency: Real-time monitoring, hourly compliance checks
  - Remediation: Automated remediation for common violations
- [ ] **Configuration Drift Detection**: Detect unauthorized config changes
  - Baseline: Approved baseline configuration
  - Detection: Alert on deviations from baseline
  - Response: Auto-revert to baseline or flag for review

**Advanced Threat Modeling**:
- [ ] **Attack Path Analysis**: Map attack paths to sensitive data
  - Method: Graph analysis of permissions, network paths
  - Purpose: Identify lateral movement paths, privilege escalation paths
  - Response: Close high-risk attack paths
- [ ] **Blast Radius Mapping**: Quantify breach impact
  - Analysis: If account X compromised, what data accessible?
  - Purpose: Identify high-value accounts, reduce blast radius
  - Response: Segment high-value accounts, add MFA, monitoring

**Data Masking and Tokenization**:
- [ ] **Dynamic Data Masking**: Real-time data masking for non-production
  - Use Cases: Development, testing, analytics (mask PII/PHI/PCI)
  - Implementation: Database dynamic masking, proxy-based masking
- [ ] **Tokenization**: Replace sensitive data with tokens
  - Use Cases: Payment processing, PII in analytics
  - Benefit: Reduce PCI-DSS scope, protect data while preserving utility
  - Implementation: Tokenization service, token vault

**Zero Trust Data Access**:
- [ ] **Continuous Verification**: Verify every data access request
  - Principle: Never trust, always verify
  - Factors: User identity, device compliance, location, data sensitivity
  - Implementation: Context-aware access policies, continuous authentication
- [ ] **Micro-Segmentation**: Fine-grained network segmentation
  - Scope: Isolate data stores, restrict lateral movement
  - Implementation: Network policies, service mesh, cloud security groups

**Security Chaos Engineering for Data**:
- [ ] **Data Security Resilience Testing**: Test hardening under attack
  - Scenarios:
    - Simulate credential theft → validate MFA prevents access
    - Simulate DLP bypass attempts → validate detection
    - Simulate ransomware attack → validate immutable backups
    - Simulate data exfiltration → validate DLP blocks
  - Frequency: Quarterly chaos engineering exercises
  - Result: ≥90% of attacks detected/blocked by hardening

---

### Enhanced Success Indicators

**Advanced Hardening**:
1. **Infrastructure as Code**: 100% data infrastructure defined as code
2. **Configuration Drift**: ≤1% configuration drift detected
3. **Attack Path Mitigation**: ≥80% high-risk attack paths closed

**Advanced Compliance**:
1. **Real-Time Compliance**: Continuous compliance monitoring (100% coverage)
2. **Automated Remediation**: ≥70% compliance violations auto-remediated

**Zero Trust**:
1. **Continuous Verification**: 100% data access requests verified
2. **Micro-Segmentation**: ≥90% data stores micro-segmented

---

## Level 3: Industry-Leading Environment Hardening

### Advanced Practices

**Formal Verification of Data Security Properties**:
- [ ] **Mathematical Proofs of Security Guarantees**: Formal verification
  - Properties: Prove encryption enforced (no plaintext leakage), least privilege (no unauthorized access), data deletion (data irrecoverable)
  - Tools: TLA+, Alloy, Coq for security property verification
  - Result: Machine-checked proofs of data security properties
- [ ] **Privacy Property Verification**: Prove privacy guarantees
  - Properties: Differential privacy (ε bounds), k-anonymity (no individual identifiable), secure deletion (data unrecoverable)
  - Result: Formal proofs published, peer-reviewed

**Confidential Computing**:
- [ ] **Encrypted In-Use Data**: Encrypt data during processing
  - Technologies: Intel SGX, AMD SEV, AWS Nitro Enclaves, Azure Confidential Computing
  - Use Cases: Process sensitive data in untrusted environments, cloud
  - Benefit: Data encrypted at rest, in transit, AND in use (full lifecycle encryption)
- [ ] **Secure Enclaves**: Isolated execution environments
  - Purpose: Run sensitive data processing in hardware-isolated enclave
  - Verification: Remote attestation (verify code running in enclave)

**Supply Chain Hardening for Data Systems**:
- [ ] **Software Bill of Materials (SBOM)**: Track all software components
  - Content: List all dependencies, libraries, versions
  - Purpose: Identify vulnerable components, license compliance
  - Tools: Syft, CycloneDX
- [ ] **Provenance Tracking**: Verify software origin
  - Method: Signed commits, signed container images, signed artifacts
  - Verification: Verify signatures before deployment
  - Tools: Sigstore, in-toto, SLSA

**Public Hardening Guides and Benchmarks**:
- [ ] **Publish Data Security Hardening Guides**: Share best practices
  - Content: Database hardening guides, encryption standards, DLP configuration templates
  - Publication: Blog posts, GitHub repos, conference talks
  - Purpose: Industry leadership, community contribution
- [ ] **Contribute to Data Security Standards**: Participate in standards development
  - Organizations: NIST, ISO, OWASP, Cloud Security Alliance
  - Contribution: Data security benchmarks, encryption guidelines, privacy standards
  - Goal: Recognized industry leader in data security

**Quantified ROI and Business Value**:
- [ ] **Measure Hardening ROI**: Quantify business value
  - Metrics:
    - Cost of hardening program: $X
    - Cost of breaches prevented: $Y (Y >> X, average breach cost $4.45M per IBM)
    - Customer trust increase: Measured via NPS, retention
  - Result: Hardening ROI ≥30:1 (every $1 spent prevents $30 in breach costs)
- [ ] **Compliance Cost Savings**: Calculate compliance automation value
  - Calculation: Manual compliance effort (hours) × hourly cost vs automated compliance cost
  - Result: ≥90% reduction in compliance effort costs

---

### Industry Leadership Indicators

**Formal Verification**:
1. Machine-checked proofs of data security properties published
2. Formal verification results accepted by academic community

**Confidential Computing**:
1. ≥50% of sensitive data processing in secure enclaves
2. Remote attestation for all enclave workloads

**Supply Chain Security**:
1. 100% of data systems have SBOM
2. 100% of deployments verify signatures (provenance)

**Public Leadership**:
1. ≥3 data security hardening guides published annually
2. Active participation in data security standards bodies
3. Open-source data security tools adopted by ≥10 organizations

**Business Impact**:
1. Hardening ROI ≥30:1 (quantified business value)
2. Zero data breaches due to hardening gaps
3. ≥90% reduction in compliance costs via automation

---

## Practice Integration

**Threat Assessment (TA-Data)**: EH mitigates threats identified in TA (data breaches, exfiltration, insider threats)
**Security Requirements (SR-Data)**: EH implements security requirements (encryption, access control, DLP)
**Secure Architecture (SA-Data)**: EH implements architectural security controls (segmentation, encryption, least privilege)
**Design Review (DR-Data)**: DR validates hardening design (encryption strategy, access model)
**Implementation Review (IR-Data)**: IR validates hardening implementation (config review, code review)
**Security Testing (ST-Data)**: ST validates hardening effectiveness (penetration testing, compliance testing)
**Monitoring & Logging (ML-Data)**: ML monitors hardening compliance (config drift, access anomalies)
**Issue Management (IM-Data)**: IM tracks hardening gaps, vulnerabilities

---

## Conclusion

Environment Hardening for Data ensures AI data security systems are deployed with secure storage configurations, strong encryption, least privilege access, defense-in-depth controls, and resilient architecture to protect sensitive data and maintain privacy. Level 1 establishes secure baselines, encryption at rest and in transit, least privilege access, DLP hardening, privacy-preserving technology security, and compliance automation. Level 2 adds immutable infrastructure, automated validation, zero trust, and security chaos engineering. Level 3 achieves formal verification, confidential computing, supply chain hardening, and public leadership.

---

**Document Information**:
- **Practice**: Environment Hardening (EH)
- **Domain**: Data
- **HAIAMM Version**: 2.1
- **Maturity Levels**: 3 (Foundational, Comprehensive, Industry-Leading)
- **Last Updated**: 2025-12-29
