# Environment Hardening Practice – Data Domain
## HAIAMM v2.1 One-Pager

### Practice Overview

Environment Hardening for Data ensures AI data security systems are deployed with secure data storage, minimal data exposure, strong encryption, least privilege data access, and defense-in-depth data protection controls.

---

### Level 1: Key Hardening Activities

**Data Storage Hardening**:
- [ ] **Database Hardening**: Secure database configurations
  - Authentication: Strong authentication (no default passwords), MFA for admin accounts
  - Network: Restrict network access (bind to private IPs, firewall rules)
  - Encryption: Enable encryption at rest (TDE), encryption in transit (TLS)
  - Patching: Apply database security patches within SLA (Critical ≤48h, High ≤7d)
  - Benchmarks: Apply CIS Benchmarks for PostgreSQL, MySQL, MongoDB, etc.
- [ ] **Object Storage Hardening**: Secure S3, Blob Storage, GCS
  - Public Access: Block public access (S3 Block Public Access, private containers)
  - Encryption: Enforce server-side encryption (SSE-KMS, customer-managed keys)
  - Versioning: Enable versioning (protect against accidental deletion)
  - Access Logging: Enable access logs, send to SIEM
  - Lifecycle Policies: Auto-delete old data per retention policy
- [ ] **Data Lake/Warehouse Hardening**: Secure big data infrastructure
  - Authentication: Kerberos for Hadoop, IAM for cloud data warehouses
  - Encryption: Encrypt data at rest and in transit
  - Access Control: Column-level, row-level security (least privilege)

**Encryption Hardening**:
- [ ] **Encryption at Rest**: Encrypt all sensitive data storage
  - Coverage: Databases, object storage, file systems, backups
  - Key Management: Use customer-managed keys (AWS KMS, Azure Key Vault, GCP KMS)
  - Algorithm: AES-256 or ChaCha20-Poly1305
  - Policy: Enforce encryption (block unencrypted data creation)
- [ ] **Encryption in Transit**: TLS for all data transmission
  - Coverage: Database connections, API calls, file transfers, backups
  - Version: TLS 1.3 (or TLS 1.2 minimum)
  - Certificate Validation: Enforce certificate validation, no self-signed certs in production
- [ ] **Key Management Hardening**:
  - [ ] Store keys in dedicated key management service (KMS, Vault)
  - [ ] Rotate encryption keys annually, compromised keys immediately
  - [ ] Separate key management from data storage (different accounts/services)
  - [ ] Audit key usage (log all key access, alert on anomalies)
  - [ ] Least privilege key access (only required services can access keys)

**Data Access Control Hardening**:
- [ ] **Least Privilege Access**: Minimal data access permissions
  - Principle: Grant access only to data required for job function
  - Granularity: Database-level, table-level, column-level, row-level security
  - Review: Quarterly access reviews, remove unused permissions
- [ ] **Authentication**: Strong authentication for data access
  - Database: No default credentials, enforce strong passwords or key-based auth
  - API: Require API authentication (tokens, OAuth), no anonymous access
  - MFA: Require MFA for privileged data access (admin, analyst accounts)
- [ ] **Authorization**: Enforce data access policies
  - RBAC: Role-based access control (assign roles, not individual permissions)
  - ABAC: Attribute-based access control (access based on attributes: department, clearance)
  - Policy Enforcement: Centralized policy enforcement (OPA, cloud IAM)

**Data Classification Hardening**:
- [ ] **Automated Classification**: Classify data at creation
  - Coverage: All data classified (Public, Internal, Confidential, Restricted)
  - Automation: AI classification at ingestion, tagging, labeling
  - Enforcement: Enforce security controls based on classification
- [ ] **Data Labeling**: Label sensitive data
  - Methods: Metadata tags, database columns, file attributes
  - Purpose: Drive access control, DLP, retention, encryption policies
- [ ] **Sensitivity Handling**: Enforce controls per sensitivity
  - Restricted: Strongest encryption, MFA required, audit logging, no public access
  - Confidential: Encryption, access logging, restricted sharing
  - Internal: Encryption, standard access controls
  - Public: Minimal controls

**DLP Hardening**:
- [ ] **DLP Policy Enforcement**: Block/alert on data exfiltration
  - Channels: Email, chat, file upload, clipboard, cloud sync, removable media
  - Actions: Block (sensitive data to external), Alert (to internal), Log (all)
  - Exceptions: Allow legitimate business use with approval and logging
- [ ] **Exfiltration Prevention**: Prevent unauthorized data transfer
  - Network: Block unauthorized outbound connections, data transfer protocols
  - Endpoint: Restrict USB, removable media, cloud sync to approved services
  - Monitoring: Monitor data transfers, alert on anomalies (large downloads, unusual destinations)

**Data Retention and Disposal**:
- [ ] **Retention Policies**: Define data retention periods
  - By Classification: Restricted (7 years), Confidential (3 years), Internal (1 year)
  - By Regulation: GDPR (variable), HIPAA (6 years), PCI-DSS (1 year)
  - Enforcement: Auto-delete data after retention period
- [ ] **Secure Deletion**: Ensure complete data removal
  - Methods: Crypto-shredding (delete encryption keys), overwrite (multiple passes), physical destruction
  - Validation: Verify data irrecoverable after deletion
  - Scope: Backups, replicas, caches (delete everywhere)

**Data Residency and Compliance**:
- [ ] **Geographic Controls**: Enforce data residency requirements
  - Regulation: GDPR (EU data in EU), CCPA (California), local data laws
  - Enforcement: Store data in required regions, block transfers to prohibited regions
  - Validation: Audit data location, verify compliance
- [ ] **Compliance Automation**: Automate compliance enforcement
  - GDPR: Auto-delete data after retention, process deletion requests within 30 days
  - CCPA: Honor opt-outs, provide data portability
  - HIPAA: Encrypt PHI, audit access, business associate agreements

**Backup Hardening**:
- [ ] **Backup Encryption**: Encrypt all backups
  - Method: Encrypt before backup, use separate encryption keys
  - Storage: Store backups in separate account/region, immutable storage
- [ ] **Backup Access Control**: Restrict backup access
  - Principle: Least privilege, separate backup access from production access
  - MFA: Require MFA for backup access and restoration
- [ ] **Backup Testing**: Validate backup recoverability
  - Frequency: Quarterly restore tests
  - Scope: Test full restore, validate data integrity, measure RTO/RPO
- [ ] **Immutable Backups**: Prevent backup tampering/deletion
  - Methods: Object lock (S3), immutable snapshots, write-once storage
  - Benefit: Protect against ransomware (backups can't be encrypted/deleted)

**Privacy-Preserving Hardening**:
- [ ] **Differential Privacy**: Add noise to protect individual privacy
  - Implementation: Validate epsilon/delta parameters, enforce query limits
  - Monitoring: Track privacy budget consumption, prevent budget exhaustion
- [ ] **Data Minimization**: Collect and retain only necessary data
  - Principle: Don't collect data you don't need
  - Application: User content not captured in telemetry, PII minimized
- [ ] **Anonymization/Pseudonymization**: Protect identities
  - Methods: Hash identifiers, tokenization, aggregation
  - Use Cases: Analytics, testing, research (use anonymized data)

**Success Indicators**:
- Encryption: 100% sensitive data encrypted at rest and in transit
- Access control: ≥90% data access follows least privilege
- Classification: 100% data classified, ≥90% automated classification accuracy
- DLP: ≥85% exfiltration attempts blocked
- Compliance: 100% data retention policies enforced, zero GDPR/CCPA violations

---

**Document Information**: Practice: Environment Hardening (EH) | Domain: Data | HAIAMM v2.1 | Last Updated: 2025-12-25
