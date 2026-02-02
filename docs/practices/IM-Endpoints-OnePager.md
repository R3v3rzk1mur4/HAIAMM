# Issue Management Practice – Endpoints Domain
## HAIAMM v2.0 One-Pager

### Practice Overview

Issue Management for Endpoints ensures AI endpoint security systems systematically identify, assess, prioritize, and remediate vulnerabilities in endpoint agents, operating systems, applications, and endpoint configurations across all platforms.

---

### Level 1: Key Issue Management Activities

**Endpoint Agent Issue Management**:
- [ ] **Agent Code Scanning**: Scan endpoint agent code for vulnerabilities
  - Scope: Agent binaries, dependencies, libraries
  - Tools: SAST, dependency scanners, binary analysis
  - Frequency: Daily scans, pre-release validation
- [ ] **Agent Update Management**: Patch agent vulnerabilities promptly
  - Deployment: Staged rollout (canary → 10% → 50% → 100%)
  - Rollback: Automated rollback on errors or performance degradation
  - SLA: Critical agent vulnerabilities ≤24 hours, High ≤7 days

**OS and Application Vulnerability Scanning**:
- [ ] **OS Vulnerability Scanning**: Scan endpoint operating systems
  - Platforms: Windows, macOS, Linux, iOS, Android
  - Tools: Qualys, Rapid7, Tenable, Microsoft Defender
  - Coverage: Missing patches, CVEs, OS misconfigurations
  - Frequency: Daily scans
- [ ] **Application Vulnerability Scanning**: Scan installed applications
  - Scope: Browsers, productivity apps, development tools, third-party software
  - Detection: Outdated versions, known vulnerabilities, unsafe configurations
- [ ] **Mobile Device Scanning**: Scan mobile endpoints (BYOD, corporate)
  - Tools: Mobile Device Management (MDM), Mobile Threat Defense (MTD)
  - Coverage: OS version, app vulnerabilities, jailbreak/root detection

**Configuration Vulnerability Assessment**:
- [ ] **Endpoint Configuration Scanning**: Detect insecure configurations
  - Coverage: Firewall disabled, encryption disabled, weak passwords, unnecessary services
  - Benchmarks: CIS Benchmarks for Windows, macOS, Linux
  - Frequency: Daily configuration scans
- [ ] **Privilege Escalation Checks**: Detect local privilege escalation vulnerabilities
  - Tools: BeRoot, LinPEAS, WinPEAS
  - Frequency: Weekly scans on high-value endpoints

**Cross-Platform Vulnerability Coverage**:
- [ ] **Windows Issue Management**: Track Windows CVEs, patches
  - Sources: Microsoft Security Response Center (MSRC), Windows Update
  - Coverage: Windows 10, 11, Server 2016, 2019, 2022
- [ ] **macOS Issue Management**: Track macOS CVEs, patches
  - Sources: Apple Security Updates
  - Coverage: Recent macOS versions (Ventura, Sonoma)
- [ ] **Linux Issue Management**: Track Linux CVEs, patches
  - Sources: Distribution security advisories (Ubuntu, RHEL, Debian)
  - Package Managers: apt, yum, dnf vulnerability tracking
- [ ] **Mobile Issue Management**: Track iOS/Android CVEs
  - Sources: Apple/Google security bulletins
  - Policy: Enforce minimum OS version, block outdated devices

**Remediation Workflows**:
- [ ] **Automated Patch Deployment**: Deploy OS/app patches automatically
  - Tools: WSUS, SCCM, Jamf, Intune
  - Policy: Auto-deploy critical patches within SLA, staged rollout for major updates
  - Testing: Test patches in staging before production deployment
- [ ] **Endpoint Isolation**: Isolate vulnerable endpoints until patched
  - Triggers: Critical unpatched vulnerability + network-facing
  - Method: Network isolation, prevent lateral movement
  - Override: Allow manual override with approval for business-critical systems
- [ ] **Compensating Controls**: Implement temporary mitigations
  - Examples: Enable enhanced monitoring, restrict network access, disable vulnerable features
  - Documentation: Track compensating controls until permanent remediation

**Prioritization and SLAs**:
- [ ] **Risk-Based Prioritization**: Prioritize by exploitability × asset criticality
  - Critical: Actively exploited vulnerabilities in internet-facing or sensitive endpoints
  - High: High CVSS score, public exploits available, privileged user endpoints
  - Medium: Moderate risk, internal endpoints, compensating controls exist
  - Low: Minimal risk, difficult to exploit
- [ ] **Remediation SLAs by Severity**:
  - Critical: ≤24 hours
  - High: ≤7 days
  - Medium: ≤30 days
  - Low: ≤90 days

**Vulnerability Metrics**:
- [ ] **Patch Compliance**: % endpoints fully patched
  - Target: ≥95% endpoints patched within SLA
- [ ] **Vulnerable Endpoint Count**: Track endpoints with unpatched critical/high vulnerabilities
  - Target: ≤5% endpoints with critical vulnerabilities
- [ ] **Mean Time to Patch**: Average time from vulnerability disclosure to patch deployment
  - Target: Critical ≤24h, High ≤7d
- [ ] **Patch Failure Rate**: % patches that fail to deploy or cause issues
  - Target: ≤2% patch failure rate

**Success Indicators**:
- Patch compliance: ≥95% endpoints patched within SLA
- Vulnerability coverage: 100% of endpoints scanned daily
- MTTR: Critical ≤24h, High ≤7d
- Vulnerable endpoints: ≤5% with critical/high vulnerabilities

---

**Document Information**: Practice: Issue Management (IM) | Domain: Endpoints | HAIAMM v2.0 | Last Updated: 2025-12-25
