# Environment Hardening (EH) - Software Domain
## HAIAMM Assessment Questionnaire v2.0

**Practice:** Environment Hardening (EH)
**Domain:** Software
**Purpose:** Assess organizational maturity in environment hardening for Human Assisted Intelligence code security system deployments

---

## Instructions

- Answer each question honestly based on **current, implemented practices** (not plans or aspirations)
- **"Yes" requires evidence** - Document proof for each affirmative answer
- **Answer progressively** - Complete all Level 1 questions before Level 2
- **Level progression** - Achieve ALL questions at lower level before advancing
- **Partial implementation = "No"** - Practice must be complete and systematic

---

## Level 1: Foundational
**Objective:** Establish secure baseline configurations, least privilege access, encryption, network segmentation, and resilient architecture

### Question 1: Secure Baseline Configuration and Hardening Standards

**Q1.1:** Have you established and enforced secure baseline configurations for all AI system components (OS, containers, Kubernetes) achieving ≥95% compliance with security benchmarks (CIS Benchmarks), ≤5 vulnerabilities per system, and ≥95% patch compliance within SLA (critical patches ≤24 hours, high ≤7 days)?

**Evidence Required:**
- [ ] Secure Baseline Configuration implemented:
  - OS Hardening Standards: CIS Benchmarks applied for Linux, Windows, macOS
  - Coverage: Unnecessary services disabled, secure boot, disk encryption, firewall configuration
  - Validation: Automated compliance scanning (OpenSCAP, InSpec)
  - Minimal OS Installation: Only required packages installed (Alpine Linux, distroless containers)
  - Patch Management: Automated patch deployment (unattended-upgrades, yum-cron)
- [ ] Container Hardening:
  - Minimal Container Images: Distroless or minimal base images (Google Distroless, Alpine, scratch)
  - Container Security Scanning: Trivy, Grype, Clair, Anchore scanning in CI/CD and registry
  - Policy: Block deployment of images with critical CVEs
  - Container Hardening Practices:
    - Run containers as non-root user
    - Read-only root filesystem
    - Drop unnecessary Linux capabilities (--cap-drop ALL)
    - Use seccomp and AppArmor/SELinux profiles
    - Set resource limits (CPU, memory, file descriptors)
  - Image Signing and Verification: Docker Content Trust, Cosign, or Notary
- [ ] Kubernetes Hardening (if applicable):
  - Pod Security Standards: Baseline or Restricted levels enforced (Pod Security Admission, OPA/Gatekeeper)
  - Network Policies: Default deny, explicit allow for required traffic
  - RBAC: Least privilege for service accounts and users
  - Secrets Encryption: Secrets encrypted at rest, external secrets manager (Vault, AWS Secrets Manager)
  - Admission Controllers: Security policies enforced at admission
- [ ] Compliance Metrics:
  - Baseline Compliance: ≥95% systems comply with security baselines
  - Vulnerability Density: ≤5 vulnerabilities per system
  - Patch Compliance: ≥95% systems patched within SLA (critical ≤24 hours, high ≤7 days)
- [ ] Evidence of automated compliance scanning and patch management

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

### Question 2: Application and Data Security Hardening

**Q1.2:** Have you implemented comprehensive application hardening (secure configuration, input validation, strong authentication with MFA, API security with rate limiting) and data security hardening (encryption at rest for 100% sensitive data, TLS 1.2+ for 100% network traffic, secure key management with quarterly rotation)?

**Evidence Required:**
- [ ] Application Hardening:
  - Secure Application Configuration:
    - Debug features disabled in production
    - Default credentials removed/changed
    - Unnecessary services/endpoints disabled
  - Input Validation and Output Encoding:
    - All external input validated (API requests, file uploads, user input)
    - Whitelist validation approach
    - Output encoding to prevent injection (HTML escaping, parameterized queries)
  - Authentication and Session Management:
    - Strong password policy (≥12 chars, complexity, no common passwords)
    - MFA enforced for privileged accounts (100%), recommended for all accounts (≥95%)
    - SSO integration (OAuth, SAML)
    - Secure session management (random tokens, secure cookies: HttpOnly/Secure/SameSite, timeout ≤30 min idle/≤12 hr absolute)
  - API Security:
    - API authentication required (API keys, OAuth, JWT)
    - API authorization enforced (RBAC/ABAC)
    - Rate limiting implemented (per-user and global limits)
    - API versioning maintained
- [ ] Data Security Hardening:
  - Encryption at Rest:
    - 100% of sensitive data encrypted (model files, training data, findings, user data)
    - Database encryption (TDE, column-level encryption)
    - Object storage encryption (SSE-S3, SSE-KMS)
    - Disk encryption (LUKS, BitLocker, FileVault)
  - Encryption in Transit:
    - TLS enforcement: 100% network traffic encrypted (TLS 1.3 or TLS 1.2 minimum)
    - Strong cipher suites only
    - Certificate validation enforced
    - mTLS for service-to-service communication (optional but recommended)
  - Key Management:
    - Secrets Manager: HashiCorp Vault, AWS Secrets Manager, Azure Key Vault, GCP Secret Manager
    - Key Rotation: Encryption keys annually, credentials quarterly, compromised keys immediately
    - Access Control: Least privilege for secret access, audit logging of all secret access
- [ ] Metrics tracked:
  - Encryption at Rest: 100% sensitive data encrypted
  - Encryption in Transit: 100% network traffic encrypted (TLS 1.2+)
  - Certificate Validity: 100% certificates valid, ≥30 days before expiration
  - MFA Adoption: 100% privileged accounts, ≥95% all accounts
- [ ] Evidence of encryption, authentication, and key management implementation

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

### Question 3: Network Hardening, Access Control, and Resilience

**Q1.3:** Have you implemented network hardening (multi-tier segmentation with 100% tier isolation, default deny firewalls, DDoS protection for 100% public services), access control hardening (least privilege for ≥90% accounts, zero unused credentials >90 days), and high availability with tested disaster recovery (RTO ≤4 hours, RPO ≤1 hour)?

**Evidence Required:**
- [ ] Network Hardening:
  - Network Segmentation:
    - Multi-tier architecture (Public/Web, Application, Data tiers)
    - 100% of tiers isolated with firewalls/network policies
    - Zero Trust Network principles (assume breach, verify every connection)
    - Private networks for internal communication (VPC, VNet)
  - Firewall Configuration:
    - Default deny (block all traffic by default, explicitly allow required)
    - Least privilege network access
    - Public IPs only for public-facing services
  - Web Application Firewall (WAF) for public-facing applications:
    - OWASP Top 10 coverage
    - Cloudflare, AWS WAF, Azure WAF, ModSecurity, or equivalent
  - DDoS Protection:
    - 100% public-facing services behind DDoS protection
    - Cloudflare, AWS Shield, Azure DDoS Protection, or equivalent
  - Zero unnecessary exposed services
- [ ] Access Control Hardening:
  - Principle of Least Privilege:
    - ≥90% accounts/services have minimal required permissions
    - IAM policies grant minimal permissions
    - Quarterly access reviews, unused permissions removed
  - Service Accounts:
    - Dedicated service account per service
    - No shared credentials
  - Just-In-Time Access (optional): Temporary privileged access with approval
  - Multi-Factor Authentication (MFA):
    - 100% privileged accounts use MFA
    - ≥95% all accounts use MFA
  - Privileged Access Management (PAM):
    - Bastion hosts for centralized privileged access
    - Session logging and recording
    - Credential rotation (quarterly, immediate on personnel change)
  - Zero unused credentials >90 days old
- [ ] Resilience and High Availability:
  - High Availability Architecture:
    - Multi-AZ or multi-region deployment
    - Load balancing across multiple instances
    - Auto-scaling (horizontal scaling under load)
    - Health checks (liveness and readiness probes)
  - Backup and Recovery:
    - Automated backups (databases daily, files weekly, code via Git)
    - Retention: 30 days hot, 1 year cold
    - Quarterly backup restore testing
    - Disaster Recovery Plan documented:
      - RTO (Recovery Time Objective) ≤4 hours for critical services
      - RPO (Recovery Point Objective) ≤1 hour data loss maximum
- [ ] Logging and Monitoring:
  - Comprehensive logging of security events (authentication, authorization, config changes, errors)
  - Centralized log aggregation (SIEM: Splunk, ELK, Datadog, Sumo Logic)
  - Log retention: ≥90 days hot, ≥1 year cold
  - Log integrity protection (write-once storage, log signing)
  - Intrusion detection (IDS/IPS: Snort, Suricata, EDR)
- [ ] Development Pipeline Hardening:
  - Secure CI/CD: Pipeline access control, secrets management, build isolation
  - Code Repository: Branch protection, signed commits (optional)
  - Artifact Hardening: Artifact signing and scanning
- [ ] Evidence of network segmentation, access controls, resilience architecture, and disaster recovery testing

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

**Level 1 Score:** _____ / 3 questions answered "Yes"

**Level 1 Achieved:** ☐ Yes (3/3) ☐ No (< 3/3)

---

## Level 2: Comprehensive
**Objective:** Implement immutable infrastructure, security chaos engineering, automated hardening validation, and advanced threat modeling

**Prerequisites:** ALL Level 1 questions must be "Yes" to proceed to Level 2

### Question 4: Immutable Infrastructure and Security Chaos Engineering

**Q2.1:** Have you implemented immutable infrastructure (no runtime changes, redeploy for all updates, automated deployment pipelines) and conduct security chaos engineering (test hardening under attack, quarterly attack simulations, validate defenses work under adversarial conditions)?

**Evidence Required:**
- [ ] Immutable Infrastructure:
  - Infrastructure as Code (IaC): All infrastructure defined in code (Terraform, CloudFormation, Pulumi)
  - No Runtime Changes: Configuration changes prohibited in production (redeploy instead)
  - Automated Deployment: CI/CD pipelines deploy infrastructure changes
  - Versioned Infrastructure: All infrastructure changes version-controlled
  - Rollback Capability: Quick rollback to previous infrastructure version
  - Benefits demonstrated: Consistency, auditability, security (no configuration drift)
- [ ] Container Immutability:
  - Containers never modified after build
  - All changes require rebuilding container image
  - Container images tagged with versions/hashes
  - Read-only root filesystem enforced
- [ ] Configuration Management:
  - Configuration externalized (environment variables, config maps, secrets)
  - No manual configuration changes in production
  - Configuration changes via automated deployment
- [ ] Security Chaos Engineering program:
  - Quarterly Attack Simulations:
    - Red team exercises against AI system
    - Penetration testing of hardened infrastructure
    - Social engineering tests (phishing simulations)
    - Denial-of-service simulations
  - Adversarial Testing:
    - Test if hardening withstands real attacks
    - Validate defense-in-depth layers work
    - Test incident response under attack
  - Chaos Experiments:
    - Inject failures to test resilience (kill services, network partitions, resource exhaustion)
    - Validate auto-healing and recovery
    - Test backup and disaster recovery procedures
  - Results Documented:
    - Attack success/failure rates
    - Defense effectiveness measured
    - Gaps identified and remediated
    - Improvements implemented based on findings
- [ ] Evidence of immutable infrastructure reducing configuration drift and security chaos engineering improving defenses

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

### Question 5: Automated Hardening Validation and Continuous Compliance

**Q2.2:** Have you implemented automated hardening validation with continuous compliance checking (real-time monitoring of configuration drift, automated remediation of non-compliance, continuous security scanning) achieving ≥98% compliance with security baselines?

**Evidence Required:**
- [ ] Automated Hardening Validation:
  - Continuous Compliance Checking:
    - Real-time monitoring of security baselines (CIS Benchmarks, custom policies)
    - Automated compliance scanning (continuous, not just periodic)
    - Tools: Chef InSpec, AWS Config, Azure Policy, Google Cloud Security Command Center, Terraform Sentinel
  - Configuration Drift Detection:
    - Detect when configurations deviate from baseline
    - Alert on drift immediately
    - Track drift metrics over time
  - Automated Remediation:
    - Auto-remediate common non-compliance issues (restart service, apply patch, revert config)
    - Manual remediation for complex issues with automated ticket creation
    - Remediation SLA: Critical within 24 hours, High within 7 days
  - Continuous Security Scanning:
    - Container image scanning (on build, on push to registry, runtime scanning)
    - Infrastructure scanning (IaC scanning before deployment)
    - Application scanning (SAST/DAST in CI/CD)
    - Dependency scanning (continuous monitoring for new vulnerabilities)
- [ ] Compliance Dashboards:
  - Real-time compliance status visible to all stakeholders
  - Compliance trends over time
  - Non-compliance alerts and tracking
  - Compliance reporting for audits
- [ ] Metrics:
  - Baseline Compliance: ≥98% systems comply (improved from ≥95% at Level 1)
  - Mean Time to Remediation (MTTR): ≤24 hours for critical issues
  - Configuration Drift: ≤2% of systems with drift
  - False Positive Rate: <5% for automated compliance checks
- [ ] Historical tracking showing sustained high compliance (≥12 months data)
- [ ] Evidence of automated validation preventing security incidents

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

### Question 6: Advanced Threat Modeling and Attack Path Analysis

**Q2.3:** Do you conduct advanced threat modeling including attack path analysis (map all potential attack paths, identify critical choke points), blast radius mapping (limit impact of successful attacks through segmentation), and threat modeling-driven hardening (prioritize hardening based on threat model findings)?

**Evidence Required:**
- [ ] Advanced Threat Modeling:
  - Attack Path Analysis:
    - Map all potential attack paths to critical assets (data, models, credentials)
    - Identify attack vectors (network, application, supply chain, insider)
    - Document attack prerequisites and kill chain stages
    - Identify critical choke points where attacks can be blocked
  - Blast Radius Mapping:
    - Define blast radius for each component (what can attacker access if component compromised?)
    - Minimize blast radius through micro-segmentation
    - Isolate high-value targets (model files, training data, production secrets)
    - Implement containment controls (network policies, RBAC, data isolation)
  - Threat Modeling-Driven Hardening:
    - Prioritize hardening efforts based on threat model (focus on high-risk attack paths)
    - Validate hardening effectiveness against threat model
    - Update threat model as hardening is implemented
    - Continuous threat modeling (quarterly reviews, updates on architecture changes)
- [ ] Threat Modeling Integration:
  - Threat models from TA practice used to inform EH hardening decisions
  - Design Review (DR) validates designs address threat model
  - Security Testing (ST) validates hardening against threat model
- [ ] Attack Surface Reduction:
  - Minimize exposed services (close unnecessary ports, disable unnecessary features)
  - Reduce privilege (least privilege for all accounts and services)
  - Harden attack vectors (WAF for web, API security, secure authentication)
  - Metrics: Attack surface quantified and reducing over time
- [ ] Evidence of advanced threat modeling improving security outcomes:
  - Attack paths identified and mitigated
  - Blast radius reduced through segmentation
  - Successful attack simulations showing limited impact
- [ ] Historical tracking showing threat modeling driving hardening improvements

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

**Level 2 Score:** _____ / 3 questions answered "Yes"

**Level 2 Achieved:** ☐ Yes (3/3) ☐ No (< 3/3)

---

## Level 3: Industry-Leading
**Objective:** Achieve formal verification, confidential computing, supply chain hardening, and public contribution of hardening standards

**Prerequisites:** ALL Level 2 questions must be "Yes" to proceed to Level 3

### Question 7: Formal Verification and Confidential Computing

**Q3.1:** Have you implemented formal verification of critical security properties (≥5 properties formally verified) and confidential computing for sensitive data processing (encrypted in-use data using TEEs: Trusted Execution Environments, secure enclaves)?

**Evidence Required:**
- [ ] Formal Verification of Security Properties:
  - Formal Methods applied to critical security components:
    - Authentication mechanisms
    - Authorization logic
    - Encryption implementations
    - Key management
    - Access control enforcement
  - Verification Techniques:
    - Formal proof systems (TLA+, Coq, Isabelle/HOL, Z3)
    - Model checking for state machines
    - Symbolic execution for path analysis
    - Abstract interpretation for invariant verification
  - Verified Properties (≥5 properties):
    - "No unauthenticated access to sensitive data"
    - "All encryption keys properly rotated within SLA"
    - "No privilege escalation without authorization"
    - "All sensitive data encrypted at rest and in transit"
    - "Audit logging cannot be tampered or deleted"
  - Verification Proofs:
    - Proofs completed and peer-reviewed
    - Proofs maintained as code evolves
    - Continuous verification in CI/CD
  - Evidence of formal verification preventing critical security vulnerabilities
- [ ] Confidential Computing:
  - Trusted Execution Environments (TEEs) deployed for sensitive operations:
    - Intel SGX enclaves, AMD SEV, ARM TrustZone, AWS Nitro Enclaves
    - Sensitive workloads: Model training, inference on sensitive data, key management
  - Encrypted In-Use Data:
    - Data encrypted even while being processed (memory encryption)
    - Protection from compromised OS, hypervisor, or cloud provider
  - Remote Attestation:
    - Verify TEE integrity before processing sensitive data
    - Cryptographic proof that code running in enclave hasn't been tampered
  - Use Cases:
    - Processing PII/PHI without exposing to application layer
    - Secure multi-party computation
    - Confidential model training (training on encrypted data)
  - Documented confidential computing deployment (architecture, use cases, threat model)
- [ ] Historical tracking showing formal verification and confidential computing effectiveness (≥12 months)

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

### Question 8: Supply Chain Hardening and Provenance Tracking

**Q3.2:** Have you implemented comprehensive supply chain hardening including Software Bill of Materials (SBOM) for all components, provenance tracking with signed attestations, and continuous supply chain risk monitoring with ≥99% component provenance verified?

**Evidence Required:**
- [ ] Software Bill of Materials (SBOM):
  - SBOM generated for all software components:
    - Container images, libraries, frameworks, tools, infrastructure components
    - Format: SPDX, CycloneDX, or equivalent standard
  - SBOM Contents:
    - Component name, version, supplier, license, known vulnerabilities
    - Dependency tree (direct and transitive dependencies)
  - SBOM Generation:
    - Automated SBOM generation in CI/CD pipeline
    - SBOMs signed and versioned
    - SBOMs published and accessible for audits
- [ ] Provenance Tracking:
  - Build Provenance:
    - Track full build process (source commit, build environment, build tools, build timestamp)
    - Signed build attestations (SLSA: Supply-chain Levels for Software Artifacts)
    - Reproducible builds (same source → same binary)
  - Artifact Provenance:
    - Track origin of all artifacts (who built, when, from what source)
    - Cryptographic signatures on all artifacts
    - Verification before deployment (verify signatures and provenance)
  - Dependency Provenance:
    - Track origin of all dependencies
    - Verify checksums/hashes of dependencies
    - Pin dependency versions (no floating versions like "latest")
- [ ] Supply Chain Risk Monitoring:
  - Continuous Vulnerability Scanning:
    - Monitor dependencies for newly disclosed vulnerabilities
    - Automated alerts on new CVEs affecting components
    - Automated patch/update recommendations
  - Supply Chain Attack Detection:
    - Monitor for typosquatting, dependency confusion
    - Verify package integrity (checksums, signatures)
    - Detect malicious code injection in dependencies
  - Supplier Risk Assessment:
    - Assess trustworthiness of component suppliers
    - Prefer well-maintained, reputable sources
    - Document supply chain risk decisions
- [ ] Metrics:
  - Component Provenance: ≥99% of components have verified provenance
  - SBOM Coverage: 100% of deployments have SBOM
  - Supply Chain Vulnerabilities: Mean time to patch ≤7 days
  - Zero unverified third-party components in production
- [ ] Evidence of supply chain hardening preventing supply chain attacks

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

### Question 9: Public Hardening Guides and Industry Contribution

**Q3.3:** Does your organization publish public hardening guides and benchmarks (at least 2 contributions per year) and achieve peer recognition for hardening excellence (industry awards, case studies, speaking invitations, contributions to CIS Benchmarks or similar standards)?

**Evidence Required:**
- [ ] Public Hardening Guides and Benchmarks (at least 2 per year):
  - Published Hardening Guides:
    - AI system hardening best practices
    - Container security hardening guides
    - Kubernetes security hardening guides
    - Cloud infrastructure hardening guides
  - Security Benchmarks:
    - Organization-specific security baselines published
    - Contributions to CIS Benchmarks, NIST guidelines, or OWASP standards
    - Benchmarks adopted by peer organizations
  - Hardening Tools:
    - Open-source hardening tools or scripts shared
    - Automated compliance checking tools published
    - Configuration templates shared
  - Case Studies:
    - Published case studies on hardening effectiveness
    - Lessons learned from security incidents
    - ROI demonstrations for hardening investments
- [ ] Public Evidence:
  - Conference presentations on hardening (Black Hat, DEF CON, OWASP, KubeCon)
  - Blog posts, white papers, or research papers
  - Open-source repositories with hardening tools/guides
  - Webinars or workshops teaching hardening practices
- [ ] Industry Standards Contribution:
  - Participation in CIS Benchmark development
  - Contributions to NIST SP 800 series, OWASP guides, CNCF security standards
  - Influence on industry hardening practices
- [ ] Peer Recognition:
  - Industry awards for security excellence or hardening innovation
  - Case study publications by analysts or vendors
  - Speaking invitations at major security conferences
  - Peer citations (other organizations adopting your hardening practices)
  - Customer/partner recognition for security hardening
- [ ] Documented Industry Impact:
  - Hardening guides adopted by ≥5 other organizations
  - Industry standards incorporating your contributions
  - Measurable improvement in industry hardening practices
- [ ] Internal excellence program:
  - Hardening champions program
  - Recognition for hardening excellence
  - Continuous improvement culture

**Answer:** ☐ Yes  ☐ No

**Evidence Location:** _________________________________

**Notes:** ___________________________________________

---

**Level 3 Score:** _____ / 3 questions answered "Yes"

**Level 3 Achieved:** ☐ Yes (3/3) ☐ No (< 3/3)

---

## Practice Score Calculation

### Simplified Scoring (Recommended)

```
Level 1 Achieved (all 3 "Yes"): 1.0 point
Level 2 Achieved (all 3 "Yes"): +1.0 point (total 2.0)
Level 3 Achieved (all 3 "Yes"): +1.0 point (total 3.0)
```

**EH-Software Practice Score:** _______ / 3.0

### Precise Scoring (For Formal Audits)

```
L1_score = (L1 "Yes" answers) / 3
L2_score = (L2 "Yes" answers) / 3 × L1_score
L3_score = (L3 "Yes" answers) / 3 × L2_score

Practice Score = L1_score + L2_score + L3_score
```

**EH-Software Practice Score (Precise):** _______ / 3.0

---

## Assessment Summary

**Assessment Date:** _________________________________

**Assessor(s):** _____________________________________

**HAI System(s) Assessed:** __________________________

**Overall Maturity Level:**
- ☐ Level 0 (Score < 1.0): Ad-hoc, no formal environment hardening for AI systems
- ☐ Level 1 (Score 1.0 - 1.9): Foundational hardening with secure baselines, encryption, access controls
- ☐ Level 2 (Score 2.0 - 2.9): Comprehensive hardening with immutable infrastructure, chaos engineering, automated validation
- ☐ Level 3 (Score 3.0): Industry-leading with formal verification, confidential computing, supply chain hardening

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

## Environment Hardening Specific Notes

**Secure Baseline Configuration:**
- [ ] OS Hardening (CIS Benchmarks, minimal installation, patch management)
- [ ] Container Hardening (minimal images, security scanning, non-root, read-only, capabilities drop, seccomp/AppArmor, image signing)
- [ ] Kubernetes Hardening (Pod Security Standards, network policies, RBAC, secrets encryption, admission controllers)

**Application Hardening:**
- [ ] Secure configuration (debug disabled, default credentials removed, minimal exposed services)
- [ ] Input validation and output encoding
- [ ] Strong authentication (password policy, MFA, SSO, secure sessions)
- [ ] API security (authentication, authorization, rate limiting, versioning)

**Data Security:**
- [ ] Encryption at Rest (100% sensitive data: databases, object storage, disk encryption)
- [ ] Encryption in Transit (100% network traffic: TLS 1.2+, certificate management, mTLS)
- [ ] Key Management (secrets manager, key rotation: encryption annually/credentials quarterly, access control)

**Network Hardening:**
- [ ] Network Segmentation (multi-tier, 100% tier isolation, zero trust, private networks)
- [ ] Firewall Configuration (default deny, least privilege, public IPs minimized)
- [ ] WAF for public-facing applications
- [ ] DDoS Protection (100% public services)

**Access Control:**
- [ ] Least Privilege (≥90% accounts/services with minimal permissions, quarterly reviews)
- [ ] MFA (100% privileged, ≥95% all accounts)
- [ ] Privileged Access Management (bastion hosts, session logging, credential rotation)
- [ ] Zero unused credentials >90 days

**Resilience:**
- [ ] High Availability (multi-AZ, load balancing, auto-scaling, health checks)
- [ ] Backup and Recovery (automated backups, retention, quarterly restore testing, DR plan: RTO ≤4h, RPO ≤1h)

**Logging and Monitoring:**
- [ ] Comprehensive logging (security events, centralized aggregation, retention ≥90d/≥1yr, log integrity)
- [ ] Intrusion detection (IDS/IPS, anomaly detection)

**Development Pipeline:**
- [ ] Secure CI/CD (access control, secrets management, build isolation)
- [ ] Code repository (branch protection, signed commits)
- [ ] Artifact hardening (signing, scanning)

**Compliance Metrics (Level 1):**
- [ ] Baseline Compliance ≥95%
- [ ] Vulnerability Density ≤5 per system
- [ ] Patch Compliance ≥95% within SLA
- [ ] Encryption at Rest: 100% sensitive data
- [ ] Encryption in Transit: 100% network traffic
- [ ] MFA: 100% privileged, ≥95% all accounts

**Level 2 Advanced Practices:**
- [ ] Immutable Infrastructure (IaC, no runtime changes, automated deployment)
- [ ] Security Chaos Engineering (quarterly attack simulations, adversarial testing, chaos experiments)
- [ ] Automated Hardening Validation (continuous compliance ≥98%, config drift detection ≤2%, automated remediation MTTR ≤24h)
- [ ] Advanced Threat Modeling (attack path analysis, blast radius mapping, threat-driven hardening)

**Level 3 Industry-Leading:**
- [ ] Formal Verification (≥5 security properties verified using TLA+, Coq, etc.)
- [ ] Confidential Computing (TEEs: Intel SGX, AMD SEV, AWS Nitro Enclaves; encrypted in-use data)
- [ ] Supply Chain Hardening (SBOM for 100%, provenance tracking ≥99%, continuous risk monitoring, SLSA compliance)
- [ ] Public Contributions (≥2 per year: hardening guides, benchmarks, tools, CIS Benchmark contributions)
- [ ] Peer Recognition (awards, case studies, speaking invitations)

---

**Document Version:** 2.0
**Last Updated:** 2025-12-29
**Next Review:** Quarterly or after significant HAI system changes
