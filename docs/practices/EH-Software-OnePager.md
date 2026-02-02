# Environment Hardening Practice – Software Domain
## HAIAMM v2.0 One-Pager

### Practice Overview

Environment Hardening for Software ensures AI code security systems are deployed with secure configurations, minimal attack surface, least privilege access, defense-in-depth controls, and resilient architecture to withstand attacks.

**Scope**: Hardening for:
- Application runtime environments (containers, VMs, serverless)
- AI model serving infrastructure (inference servers, model registries)
- Development environments (IDE plugins, CI/CD pipelines)
- Data storage (databases, object storage, caches)
- Network architecture (segmentation, encryption, access controls)

**Why This Matters**: Secure-by-default configuration and defense-in-depth reduce attack surface and limit blast radius of successful attacks. Hardening ensures that even if vulnerabilities exist, they're difficult to exploit and limited in impact.

---

### Level 1: Foundational Environment Hardening

### Core Objectives
1. Establish secure baseline configurations for all AI system components
2. Implement least privilege access controls (principle of least privilege)
3. Reduce attack surface through service minimization and network segmentation
4. Deploy defense-in-depth controls (multiple layers of security)
5. Harden development and deployment pipelines
6. Maintain hardening standards and continuous validation

### Key Activities

#### 1. Secure Baseline Configuration

**Operating System Hardening**:
- [ ] **OS Hardening Standards**: Apply security benchmarks
  - Benchmarks: CIS Benchmarks for Linux, Windows, macOS
  - Coverage: Disable unnecessary services, secure boot, disk encryption, firewall configuration
  - Validation: Automated compliance scanning (OpenSCAP, InSpec)
- [ ] **Minimal OS Installation**: Install only required packages
  - Approach: Use minimal base images (Alpine Linux, distroless containers)
  - Rationale: Fewer packages = smaller attack surface
- [ ] **Patch Management**: Keep OS fully patched
  - Automation: Automated patch deployment (unattended-upgrades, yum-cron)
  - SLA: Critical OS patches ≤24 hours, High ≤7 days

**Container Hardening**:
- [ ] **Minimal Container Images**: Use distroless or minimal base images
  - Images: Google Distroless, Alpine, scratch (for static binaries)
  - Size Reduction: Smaller images = fewer vulnerabilities, faster deployment
- [ ] **Container Security Scanning**: Scan images for vulnerabilities
  - Tools: Trivy, Grype, Clair, Anchore
  - Policy: Block deployment of images with critical CVEs
  - Integration: Scan in CI/CD pipeline, registry scanning
- [ ] **Container Hardening Practices**:
  - [ ] Run containers as non-root user (USER directive in Dockerfile)
  - [ ] Read-only root filesystem (--read-only flag)
  - [ ] Drop unnecessary Linux capabilities (--cap-drop ALL)
  - [ ] Use seccomp and AppArmor/SELinux profiles
  - [ ] Set resource limits (CPU, memory, file descriptors)
- [ ] **Image Signing and Verification**: Ensure image integrity
  - Tools: Docker Content Trust, Cosign, Notary
  - Process: Sign images at build time, verify signatures before deployment

**Kubernetes Hardening**:
- [ ] **Pod Security Standards**: Enforce pod security policies
  - Levels: Baseline (deny known privilege escalations), Restricted (heavily restricted)
  - Implementation: Pod Security Admission, OPA/Gatekeeper policies
- [ ] **Network Policies**: Implement network segmentation
  - Default Deny: Deny all traffic by default, explicitly allow required traffic
  - Segmentation: Isolate namespaces, limit inter-pod communication
- [ ] **RBAC**: Implement role-based access control
  - Principle: Least privilege for service accounts, users
  - Validation: Audit RBAC permissions, remove excessive permissions
- [ ] **Secrets Management**: Secure Kubernetes secrets
  - Encryption: Encrypt secrets at rest (encryption provider)
  - External: Use external secrets manager (Vault, AWS Secrets Manager)
  - Access Control: Limit secret access to required pods only
- [ ] **Admission Controllers**: Enforce security policies at admission
  - Controllers: PodSecurityPolicy, ImagePolicyWebhook, ResourceQuota
  - Custom: Use OPA/Gatekeeper for custom policies

#### 2. Application Hardening

**Secure Application Configuration**:
- [ ] **Disable Debug Features**: Disable debug modes, verbose logging in production
  - Risk: Debug features leak sensitive information, enable exploitation
  - Examples: Disable Flask debug mode, Django DEBUG=False
- [ ] **Remove Default Credentials**: Change or remove default passwords, API keys
  - Scope: Admin accounts, database users, service accounts, API tokens
  - Validation: Scan for default credentials, enforce credential rotation
- [ ] **Minimize Exposed Services**: Disable unnecessary endpoints, features
  - Examples: Disable admin UI in production, remove unused API endpoints
  - Validation: Inventory exposed services, disable unnecessary ones

**Input Validation and Output Encoding**:
- [ ] **Input Validation**: Validate all external input
  - Coverage: API requests, file uploads, user input, external data sources
  - Approach: Whitelist validation (allow known-good), reject known-bad
  - Libraries: Use validation libraries (Joi, Pydantic, Marshmallow)
- [ ] **Output Encoding**: Encode output to prevent injection
  - Coverage: HTML output (prevent XSS), SQL queries (prevent SQLi), shell commands
  - Libraries: Use templating engines with auto-escaping, parameterized queries, ORMs

**Authentication and Session Management**:
- [ ] **Strong Authentication**: Enforce strong authentication mechanisms
  - Password Policy: Minimum length ≥12 chars, complexity requirements, no common passwords
  - MFA: Enforce multi-factor authentication for privileged accounts
  - SSO: Integrate with enterprise SSO (OAuth, SAML)
- [ ] **Secure Session Management**:
  - [ ] Use cryptographically random session tokens
  - [ ] Set secure cookie flags (HttpOnly, Secure, SameSite)
  - [ ] Implement session timeout (idle timeout ≤30 minutes, absolute timeout ≤12 hours)
  - [ ] Invalidate sessions on logout, password change

**API Security**:
- [ ] **API Authentication**: Require authentication for all API endpoints
  - Methods: API keys, OAuth tokens, JWT
  - Enforcement: No unauthenticated endpoints except public-facing health checks
- [ ] **API Authorization**: Enforce authorization on all operations
  - Model: RBAC (role-based), ABAC (attribute-based)
  - Validation: Verify user permissions before every operation
- [ ] **Rate Limiting**: Prevent API abuse
  - Limits: Per-user rate limits (100 requests/minute), global rate limits
  - Response: Return 429 Too Many Requests with Retry-After header
- [ ] **API Versioning**: Maintain API backward compatibility
  - Approach: URL versioning (/v1/, /v2/), header versioning
  - Deprecation: Provide migration path, deprecation warnings

#### 3. Data Security Hardening

**Encryption at Rest**:
- [ ] **Database Encryption**: Encrypt sensitive data in databases
  - Approach: Transparent Data Encryption (TDE), column-level encryption
  - Key Management: Use external key management (AWS KMS, Azure Key Vault)
  - Scope: Model files, training data, findings, user data
- [ ] **Object Storage Encryption**: Encrypt S3, Blob Storage, GCS
  - Method: Server-side encryption (SSE-S3, SSE-KMS)
  - Policy: Enforce encryption (reject unencrypted uploads)
- [ ] **Disk Encryption**: Encrypt disks and volumes
  - Methods: LUKS (Linux), BitLocker (Windows), FileVault (macOS)
  - Scope: All disks containing sensitive data

**Encryption in Transit**:
- [ ] **TLS Enforcement**: Require TLS for all network communication
  - Version: TLS 1.3 (or TLS 1.2 minimum)
  - Cipher Suites: Strong cipher suites only (disable weak ciphers)
  - Certificate Validation: Enforce certificate validation, no self-signed certs in production
- [ ] **Certificate Management**: Manage TLS certificates securely
  - Approach: Automated certificate management (Let's Encrypt, cert-manager)
  - Rotation: Rotate certificates before expiration, monitor expiration
- [ ] **mTLS for Service-to-Service**: Mutual TLS for internal services
  - Implementation: Service mesh (Istio, Linkerd), manual mTLS
  - Benefit: Authenticate both client and server, encrypt traffic

**Key Management**:
- [ ] **Secrets Manager**: Store secrets in dedicated secrets manager
  - Tools: HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, GCP Secret Manager
  - Scope: Database credentials, API keys, encryption keys, TLS certificates
- [ ] **Key Rotation**: Rotate encryption keys and credentials regularly
  - Frequency: Encryption keys annually, credentials quarterly, compromised keys immediately
  - Automation: Automated key rotation where possible
- [ ] **Access Control**: Restrict access to secrets
  - Principle: Least privilege, grant access only to services that need it
  - Auditing: Log all secret access, alert on anomalies

#### 4. Network Hardening

**Network Segmentation**:
- [ ] **Multi-Tier Architecture**: Separate tiers by sensitivity
  - Tiers: Public (web servers), Application (app servers), Data (databases)
  - Isolation: Firewalls, network policies between tiers
- [ ] **Zero Trust Network**: Assume breach, verify every connection
  - Approach: No implicit trust, authenticate and authorize every request
  - Implementation: Service mesh, micro-segmentation, mTLS
- [ ] **Private Networks**: Use private networks for internal communication
  - Clouds: VPC (AWS), VNet (Azure), VPC (GCP)
  - Access: No public IPs for internal services, use VPN/bastion for access

**Firewall Configuration**:
- [ ] **Default Deny**: Block all traffic by default, explicitly allow required traffic
  - Ingress: Allow only required inbound ports (443 for HTTPS, etc.)
  - Egress: Restrict outbound traffic, allow only required destinations
- [ ] **Least Privilege Network Access**: Minimize exposed services
  - Public: Only public-facing services (web UI, API) have public IPs
  - Internal: All other services internal-only, accessed via VPN or bastion
- [ ] **Web Application Firewall (WAF)**: Protect public-facing applications
  - Coverage: OWASP Top 10 attacks (SQLi, XSS, etc.), custom rules
  - Providers: Cloudflare, AWS WAF, Azure WAF, ModSecurity

**DDoS Protection**:
- [ ] **DDoS Mitigation**: Protect against denial-of-service attacks
  - Services: Cloudflare, AWS Shield, Azure DDoS Protection
  - Methods: Rate limiting, traffic scrubbing, geo-blocking

#### 5. Access Control Hardening

**Principle of Least Privilege**:
- [ ] **IAM Policies**: Grant minimal required permissions
  - Approach: Start with no permissions, add only required permissions
  - Review: Quarterly access reviews, remove unused permissions
- [ ] **Service Accounts**: Use dedicated service accounts per service
  - Isolation: Each service has dedicated account, no shared credentials
  - Permissions: Minimal permissions for service account
- [ ] **Just-In-Time Access**: Temporary privileged access
  - Approach: Require approval for privileged access, auto-expire after time limit
  - Tools: AWS IAM Access Analyzer, Azure PIM, Google Cloud IAM recommender

**Multi-Factor Authentication (MFA)**:
- [ ] **Enforce MFA**: Require MFA for all user accounts
  - Scope: All users, especially privileged accounts (admins, developers)
  - Methods: TOTP (Google Authenticator), WebAuthn (hardware keys), SMS (last resort)
- [ ] **Conditional Access**: Risk-based access control
  - Factors: Location, device compliance, user risk score
  - Action: Require MFA for risky sign-ins, block high-risk access

**Privileged Access Management (PAM)**:
- [ ] **Bastion Hosts**: Centralize privileged access
  - Approach: All privileged access via bastion/jump host
  - Logging: Log all sessions, enable session recording
- [ ] **Credential Rotation**: Rotate privileged credentials regularly
  - Frequency: Quarterly rotation, immediate rotation on personnel change
  - Automation: Automated credential rotation where possible

#### 6. Logging and Monitoring Hardening

**Security Logging**:
- [ ] **Comprehensive Logging**: Log all security-relevant events
  - Events: Authentication, authorization, configuration changes, errors, security alerts
  - Format: Structured logging (JSON), include context (user, timestamp, IP, action)
- [ ] **Centralized Log Aggregation**: Send logs to SIEM
  - Tools: Splunk, ELK Stack, Datadog, Sumo Logic
  - Retention: ≥90 days hot storage, ≥1 year cold storage
- [ ] **Log Integrity**: Protect logs from tampering
  - Methods: Write-once storage, log signing, separate log infrastructure
  - Access Control: Restrict log access, audit log access

**Security Monitoring**:
- [ ] **Intrusion Detection**: Monitor for attacks
  - Tools: IDS/IPS (Snort, Suricata), EDR, SIEM correlation rules
  - Coverage: Network traffic, system calls, application logs
- [ ] **Anomaly Detection**: Detect unusual behavior
  - AI-Based: ML models detect deviations from baseline
  - Alerts: Alert on anomalies (unusual API calls, data access patterns)

#### 7. Development Pipeline Hardening

**Secure CI/CD**:
- [ ] **Pipeline Access Control**: Restrict who can modify pipelines
  - RBAC: Role-based access to CI/CD (developers, security, ops)
  - MFA: Require MFA for pipeline access
- [ ] **Secret Management in CI/CD**: Secure secrets in pipelines
  - Approach: Use CI/CD secret management (GitHub Secrets, GitLab CI/CD variables)
  - Never: Hardcode secrets in pipeline configs, commit secrets to repo
- [ ] **Build Isolation**: Isolate build environments
  - Approach: Ephemeral build agents, containers for builds
  - Benefit: Prevent contamination between builds

**Code Repository Hardening**:
- [ ] **Branch Protection**: Protect main branches
  - Rules: Require PR reviews, status checks before merge
  - Enforcement: Block direct commits to main/master
- [ ] **Signed Commits**: Verify commit authenticity
  - Method: GPG signed commits
  - Verification: Require signed commits for sensitive repos

**Artifact Hardening**:
- [ ] **Artifact Signing**: Sign build artifacts (container images, binaries)
  - Tools: Cosign, GPG
  - Verification: Verify signatures before deployment
- [ ] **Artifact Scanning**: Scan artifacts for vulnerabilities
  - Scope: Container images, dependencies, binaries
  - Policy: Block deployment of vulnerable artifacts

#### 8. Resilience and High Availability

**High Availability Architecture**:
- [ ] **Redundancy**: Eliminate single points of failure
  - Deployment: Multi-AZ (availability zones), multi-region for critical services
  - Load Balancing: Distribute traffic across multiple instances
- [ ] **Auto-Scaling**: Scale to handle load
  - Horizontal: Scale out (add instances) under load
  - Vertical: Scale up (larger instances) if needed
- [ ] **Health Checks**: Monitor service health
  - Liveness: Is service running? (restart if not)
  - Readiness: Is service ready to accept traffic? (remove from load balancer if not)

**Backup and Recovery**:
- [ ] **Automated Backups**: Regular backups of critical data
  - Frequency: Databases (daily), files (weekly), code (continuous via Git)
  - Retention: 30 days hot storage, 1 year cold storage
- [ ] **Backup Testing**: Validate backups are restorable
  - Frequency: Quarterly restore tests
  - Scope: Test full restore, measure RTO (Recovery Time Objective)
- [ ] **Disaster Recovery Plan**: Plan for catastrophic failure
  - RTO: Recovery Time Objective (≤4 hours for critical services)
  - RPO: Recovery Point Objective (≤1 hour data loss maximum)

---

### Key Success Indicators

**Configuration Compliance**:
1. **Baseline Compliance**: ≥95% systems comply with security baselines (CIS Benchmarks)
2. **Vulnerability Density**: ≤5 vulnerabilities per system (container, VM, service)
3. **Patch Compliance**: ≥95% systems patched within SLA

**Access Control**:
1. **Least Privilege**: ≥90% accounts/services have minimal required permissions
2. **MFA Adoption**: 100% privileged accounts use MFA, ≥95% all accounts use MFA
3. **Unused Credentials**: Zero unused credentials >90 days old

**Encryption**:
1. **Encryption at Rest**: 100% sensitive data encrypted at rest
2. **Encryption in Transit**: 100% network traffic encrypted (TLS 1.2+)
3. **Certificate Validity**: 100% certificates valid, ≥30 days before expiration

**Network Security**:
1. **Segmentation**: 100% of tiers isolated with firewalls/network policies
2. **Unnecessary Services**: Zero unnecessary exposed services
3. **DDoS Protection**: 100% public-facing services behind DDoS protection

---

## Level 2: Comprehensive Environment Hardening

**Enhanced Practices**:
- Immutable infrastructure (no runtime changes, redeploy for updates)
- Security chaos engineering (test hardening under attack)
- Automated hardening validation (continuous compliance checking)
- Advanced threat modeling (attack path analysis, blast radius mapping)

---

## Level 3: Industry-Leading Environment Hardening

**Advanced Practices**:
- Formal verification of security properties
- Confidential computing (encrypted in-use data, TEEs)
- Supply chain hardening (software bill of materials, provenance tracking)
- Public hardening guides and benchmarks

---

## Practice Integration

**Issue Management (IM)**: EH reduces vulnerabilities; IM identifies hardening gaps
**Security Architecture (SA)**: EH implements architectural security controls
**Security Testing (ST)**: ST validates hardening effectiveness
**Monitoring & Logging (ML)**: ML monitors hardening compliance, detects deviations

---

## Conclusion

Environment Hardening for Software ensures AI code security systems are deployed with secure configurations, minimal attack surface, and defense-in-depth controls. Level 1 establishes secure baselines, least privilege, encryption, network segmentation, and resilient architecture. Level 2 adds immutable infrastructure and automated validation. Level 3 achieves formal verification and confidential computing.

---

**Document Information**:
- **Practice**: Environment Hardening (EH)
- **Domain**: Software
- **HAIAMM Version**: 2.0
- **Maturity Levels**: 3 (Foundational, Comprehensive, Industry-Leading)
- **Last Updated**: 2025-12-25
