# Environment Hardening Practice – Endpoints Domain
## HAIAMM v2.0 One-Pager

### Practice Overview

Environment Hardening for Endpoints ensures endpoint devices running AI security agents are configured securely, have minimal attack surface, enforce least privilege, and maintain defense-in-depth controls across Windows, macOS, Linux, and mobile platforms.

---

### Level 1: Key Hardening Activities

**Operating System Hardening**:
- [ ] **OS Security Baselines**: Apply security benchmarks
  - Benchmarks: CIS Benchmarks for Windows, macOS, Linux
  - Tools: Group Policy (Windows), MDM profiles (macOS/mobile), Ansible/Puppet (Linux)
  - Coverage: Disable unnecessary services, secure boot, firewall, password policy
- [ ] **Patch Management**: Keep OS fully patched
  - Automation: WSUS (Windows), Software Update (macOS), unattended-upgrades (Linux)
  - SLA: Critical OS patches ≤24 hours, High ≤7 days
  - Coverage: ≥95% endpoints patched within SLA
- [ ] **Disk Encryption**: Encrypt all endpoint disks
  - Windows: BitLocker (TPM + PIN/password)
  - macOS: FileVault
  - Linux: LUKS
  - Mobile: Native encryption (iOS, Android)
  - Coverage: 100% of corporate endpoints encrypted

**Endpoint Agent Hardening**:
- [ ] **Agent Protection**: Protect AI security agent from tampering
  - Anti-Tamper: Prevent agent process termination, file deletion, configuration changes
  - Kernel-Level Protection: Driver-level protection (Windows), kext (macOS), eBPF (Linux)
  - Self-Healing: Agent auto-restarts if terminated, auto-repairs if modified
- [ ] **Agent Resource Limits**: Prevent agent resource exhaustion
  - Limits: CPU ≤5%, Memory ≤200MB, Disk I/O minimal
  - Monitoring: Alert if agent exceeds resource limits (possible malfunction)
- [ ] **Agent Updates**: Secure agent update mechanism
  - Signing: Code-signed updates (verify signature before install)
  - Rollout: Staged rollout (canary → 10% → 100%)
  - Rollback: Automated rollback on update failure

**Application Hardening**:
- [ ] **Application Whitelisting**: Allow only approved applications
  - Windows: AppLocker, WDAC (Windows Defender Application Control)
  - macOS: Gatekeeper, notarization
  - Benefit: Block unapproved/malicious software execution
- [ ] **Browser Hardening**: Secure web browsers
  - Settings: Disable auto-run, block pop-ups, enable safe browsing
  - Extensions: Whitelist approved extensions, block unapproved
  - Updates: Auto-update browsers to latest version
- [ ] **Disable Unnecessary Software**: Remove unused applications
  - Examples: Disable Adobe Flash, Java applets, unnecessary services
  - Rationale: Reduce attack surface

**Privilege Hardening**:
- [ ] **Standard User Accounts**: Users operate as standard (non-admin)
  - Approach: Separate admin accounts for privileged tasks
  - Benefit: Prevents malware from gaining admin privileges easily
- [ ] **Admin Account Protection**: Secure privileged accounts
  - MFA: Require MFA for admin account access
  - Separation: Dedicated admin accounts, no daily use
  - Monitoring: Alert on admin account usage, require justification
- [ ] **UAC/Sudo Hardening**: Enforce privilege escalation prompts
  - Windows: User Account Control (UAC) set to always notify
  - macOS/Linux: Require password for sudo, log all sudo usage

**Network Hardening**:
- [ ] **Host Firewall**: Enable and configure host-based firewall
  - Windows: Windows Firewall enabled, block inbound by default
  - macOS: Firewall enabled, stealth mode
  - Linux: iptables/nftables, default deny inbound
- [ ] **Network Access Control**: Limit network connectivity
  - Corporate Network: NAC (Network Access Control) validates endpoint compliance before network access
  - Segmentation: Isolate endpoints by role (guest, employee, privileged)
- [ ] **VPN for Remote Access**: Require VPN for remote access
  - Coverage: All remote access via VPN (zero direct internet exposure of internal resources)
  - MFA: Require MFA for VPN access

**BYOD Hardening**:
- [ ] **MDM/MAM**: Manage BYOD devices
  - MDM: Mobile Device Management (Intune, Jamf, VMware Workspace ONE)
  - MAM: Mobile Application Management (manage corporate apps only)
  - Policies: Enforce encryption, password, remote wipe, app whitelisting
- [ ] **Work/Personal Separation**: Isolate corporate and personal data
  - Containers: Work profile (Android), managed apps (iOS)
  - Scope: AI agent monitors work apps/data only, not personal
- [ ] **Device Compliance**: Enforce minimum security requirements
  - Requirements: OS version, encryption, password, MDM enrollment
  - Enforcement: Block non-compliant devices from corporate resources

**Mobile Device Hardening**:
- [ ] **OS Version Enforcement**: Require recent OS versions
  - iOS: Require iOS version released ≤1 year ago
  - Android: Require Android version released ≤1 year ago
  - Rationale: Old OS versions lack security patches
- [ ] **Jailbreak/Root Detection**: Detect compromised devices
  - Detection: AI agent detects jailbreak/root
  - Response: Alert, block corporate access, or quarantine
- [ ] **App Store Restriction**: Limit app installation sources
  - iOS: Require apps from Apple App Store only
  - Android: Disable "Unknown Sources", require Google Play only
  - Enterprise: Use enterprise app stores for corporate apps

**Physical Security**:
- [ ] **Lock Screen**: Enforce screen lock
  - Timeout: Auto-lock after ≤5 minutes inactivity
  - Authentication: PIN/password/biometric required
  - Complexity: Minimum 6-digit PIN, complex password
- [ ] **Remote Wipe**: Enable remote device wipe
  - Capability: MDM can remotely wipe lost/stolen devices
  - Coverage: 100% corporate endpoints, BYOD work containers
- [ ] **Theft Protection**: Enable device tracking and theft mode
  - Tools: Find My (Apple), Find My Device (Android)
  - Activation Lock: Prevent device reuse after wipe (requires owner credentials)

**Configuration Management**:
- [ ] **Automated Configuration**: Deploy hardening via automation
  - Tools: Group Policy (Windows), Configuration Profiles (macOS), Ansible/Puppet (Linux)
  - Coverage: 100% of corporate endpoints, periodic re-application
- [ ] **Configuration Drift Detection**: Detect unauthorized changes
  - Monitoring: Monitor endpoint configurations, alert on drift from baseline
  - Remediation: Auto-remediate drift, or alert for manual review

**Success Indicators**:
- OS hardening: ≥95% endpoints compliant with CIS Benchmarks
- Encryption: 100% endpoints with disk encryption enabled
- Privilege: ≥90% users operate as standard (non-admin) accounts
- Patch compliance: ≥95% endpoints patched within SLA
- BYOD compliance: 100% BYOD devices enrolled in MDM, work/personal separation enforced

---

**Document Information**: Practice: Environment Hardening (EH) | Domain: Endpoints | HAIAMM v2.0 | Last Updated: 2025-12-25
