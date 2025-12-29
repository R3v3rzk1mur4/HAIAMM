# Environment Hardening Practice – Vendors Domain
## HAIAMM v2.1 One-Pager

### Practice Overview

Environment Hardening for Vendors ensures AI vendor risk management systems are deployed with secure configurations, hardened integrations, protected vendor data, and defense-in-depth controls to prevent vendor-related security incidents.

---

### Level 1: Key Hardening Activities

**Vendor Risk Platform Hardening**:
- [ ] **Platform Configuration Hardening**: Secure vendor risk platform
  - Authentication: Strong authentication, MFA for all accounts
  - Network: Restrict network access (private IPs, VPN/bastion access)
  - Encryption: TLS for all connections, encrypt vendor data at rest
  - Patching: Apply platform patches within SLA (Critical ≤24h, High ≤7d)
  - Access Control: RBAC for users (viewer, analyst, admin)
- [ ] **API Security**: Secure vendor platform APIs
  - Authentication: API key or OAuth required for all API calls
  - Rate Limiting: Prevent API abuse, enforce rate limits
  - Logging: Log all API calls, audit for anomalies
  - IP Restrictions: Restrict API access to known IPs

**Vendor Data Protection**:
- [ ] **Vendor Data Encryption**: Encrypt all vendor information
  - At Rest: Encrypt vendor database, documents, SBOMs, assessments
  - In Transit: TLS 1.3 for all data transmission
  - Key Management: Use customer-managed keys, rotate annually
- [ ] **Data Classification**: Classify vendor data by sensitivity
  - Critical: Vendor SBOMs, security assessments, breach data, contracts
  - Confidential: Vendor contact info, questionnaire responses, risk scores
  - Access Control: Restrict access based on classification
- [ ] **Data Retention**: Enforce vendor data retention policies
  - Retention: Vendor data retained per contractual/regulatory requirements
  - Deletion: Secure deletion after retention period, vendor contract termination

**Vendor Integration Hardening**:
- [ ] **Third-Party Integration Security**: Secure integrations with vendor data sources
  - Sources: BitSight, SecurityScorecard, breach databases, SBOM repositories
  - Authentication: Secure credential storage (secrets manager), rotate quarterly
  - API Security: Validate TLS certificates, enforce API authentication
  - Error Handling: Graceful handling of API failures, circuit breaker pattern
- [ ] **Vendor Portal Hardening**: Secure vendor self-service portal
  - Authentication: MFA required for vendor access
  - Authorization: Vendors see only their own data, not other vendors
  - Input Validation: Validate all vendor inputs (prevent injection attacks)
  - Rate Limiting: Prevent portal abuse, DoS attacks

**Vendor Access Control**:
- [ ] **Least Privilege Access**: Minimal access to vendor data
  - Principle: Grant access only to vendor data required for job function
  - RBAC: Roles for vendor managers, analysts, executives (different permissions)
  - Review: Quarterly access reviews, remove unused accounts
- [ ] **Vendor Segmentation**: Isolate vendor systems from production
  - Network: Separate network segment for vendor risk platform
  - Access: No direct access from vendor platform to production systems
  - Benefit: Limit blast radius if vendor platform compromised

**SBOM Security**:
- [ ] **SBOM Storage Hardening**: Secure SBOM storage
  - Encryption: Encrypt SBOMs at rest and in transit
  - Access Control: Restrict SBOM access (contains sensitive component info)
  - Integrity: Verify SBOM integrity (signatures, checksums)
- [ ] **SBOM Processing Hardening**: Secure SBOM analysis pipeline
  - Validation: Validate SBOM format, reject malformed SBOMs
  - Sandboxing: Process SBOMs in isolated environment (prevent exploits)
  - Monitoring: Monitor SBOM processing for anomalies, errors

**Vendor Communication Security**:
- [ ] **Secure Communication Channels**: Encrypt vendor communications
  - Email: Use encrypted email (S/MIME, PGP) for sensitive communications
  - File Sharing: Use secure file sharing (encrypted, access-controlled)
  - Meetings: Use secure video conferencing, record security discussions
- [ ] **Vendor Portal**: Centralized vendor communication platform
  - Features: Secure messaging, file upload, questionnaire submission
  - Security: MFA, encryption, audit logging, access control

**Vendor Contract Hardening**:
- [ ] **Security Requirements in Contracts**: Mandate vendor security requirements
  - Requirements: Encryption, MFA, incident notification, audit rights, SBOM provision
  - SLAs: Vulnerability remediation SLAs, incident response timelines
  - Termination: Right to terminate for security violations
- [ ] **Data Processing Agreements (DPA)**: GDPR/CCPA compliance
  - Requirements: Data protection, subprocessor disclosure, data deletion
  - Review: Annual DPA reviews, updates per regulatory changes

**Vendor Incident Response**:
- [ ] **Vendor Breach Response Plan**: Define response to vendor breaches
  - Detection: Monitor for vendor breaches (≤24 hours detection)
  - Assessment: Assess impact on organization (≤24 hours)
  - Response: Contain, remediate, notify stakeholders
  - Termination: Consider vendor termination for severe breaches
- [ ] **Vendor Monitoring**: Continuous vendor security monitoring
  - Coverage: Security ratings, breaches, vulnerabilities, compliance
  - Frequency: Critical vendors daily, high-risk weekly, others monthly
  - Alerts: Real-time alerts on critical vendor incidents

**Subprocessor Hardening**:
- [ ] **Subprocessor Inventory**: Track vendor subprocessors
  - Depth: ≥3 levels (vendor → subprocessor → sub-subprocessor)
  - Requirements: Vendors must disclose all subprocessors
  - Approval: Require approval for new subprocessors, security review
- [ ] **Subprocessor Security**: Extend security requirements to subprocessors
  - Flow-Down: Vendor contracts require subprocessors meet same security requirements
  - Validation: Audit subprocessor security (via vendor or directly)

**Vendor Offboarding**:
- [ ] **Secure Vendor Termination**: Securely offboard vendors
  - Data Deletion: Require vendor delete all organizational data
  - Verification: Verify data deletion (certificates of destruction)
  - Access Revocation: Revoke all vendor access (credentials, VPN, systems)
  - Documentation: Document termination, retain for compliance

**Compliance and Audit**:
- [ ] **Vendor Audit Rights**: Contractual audit rights
  - Rights: Right to audit vendor security, SOC 2 reports, penetration tests
  - Frequency: Annual audits for critical vendors
  - Scope: Security controls, data handling, compliance
- [ ] **Regulatory Compliance**: Ensure vendor compliance
  - Requirements: GDPR, CCPA, HIPAA, PCI-DSS per applicable regulations
  - Validation: Request compliance certifications, audit reports
  - Enforcement: Suspend vendors for non-compliance

**Success Indicators**:
- Platform security: ≥95% patched within SLA, 100% MFA enforcement
- Data protection: 100% vendor data encrypted, zero unauthorized access incidents
- Integration security: ≥95% integrations secure, zero credential compromises
- Contract compliance: 100% vendors have security requirements in contracts
- Incident response: All vendor breaches assessed within ≤24 hours

---

**Document Information**: Practice: Environment Hardening (EH) | Domain: Vendors | HAIAMM v2.1 | Last Updated: 2025-12-25
