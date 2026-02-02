![HAIAMM Logo](../images/HAIAMM_logo.png)

# HAIAMM Tools & Resources

**Recommended tools organized by practice**

[Back to Index](00-INDEX.md) | [First 30 Days](02-FIRST-30-DAYS.md) | [Assessment Checklist](07-ASSESSMENT-CHECKLIST.md)

---

## Overview

This guide provides tool recommendations for implementing HAIAMM practices. Tools are categorized as:

- **Open Source** - Free, community-supported
- **Commercial** - Paid products with enterprise support
- **Frameworks** - Standards and methodologies
- **References** - Documentation and research

---

## Governance Practices

### SM - Strategy & Metrics

**Dashboards & Visualization**
| Tool | Type | Purpose |
|------|------|---------|
| [Grafana](https://grafana.com/) | Open Source | Metrics visualization |
| [Metabase](https://www.metabase.com/) | Open Source | Business analytics |
| [Tableau](https://www.tableau.com/) | Commercial | Enterprise dashboards |
| [Power BI](https://powerbi.microsoft.com/) | Commercial | Microsoft ecosystem |

**Metrics Collection**
| Tool | Type | Purpose |
|------|------|---------|
| [Prometheus](https://prometheus.io/) | Open Source | Time-series metrics |
| [OpenTelemetry](https://opentelemetry.io/) | Open Source | Observability framework |
| [Datadog](https://www.datadoghq.com/) | Commercial | Full-stack monitoring |

**Frameworks**
- NIST AI Risk Management Framework (AI RMF)
- ISO/IEC 42001 AI Management System
- IEEE AI Ethics Guidelines

---

### PC - Policy & Compliance

**Policy Management**
| Tool | Type | Purpose |
|------|------|---------|
| [Open Policy Agent (OPA)](https://www.openpolicyagent.org/) | Open Source | Policy as code |
| [Kyverno](https://kyverno.io/) | Open Source | Kubernetes policies |
| [Vanta](https://www.vanta.com/) | Commercial | Compliance automation |
| [Drata](https://drata.com/) | Commercial | Compliance platform |

**Compliance Frameworks**
- EU AI Act compliance checklists
- NIST AI RMF Govern function
- ISO 42001 controls
- GDPR for AI systems

**References**
- [NIST AI RMF Playbook](https://airc.nist.gov/AI_RMF_Knowledge_Base/Playbook)
- [EU AI Act Official Text](https://artificialintelligenceact.eu/)

---

### EG - Education & Guidance

**Training Platforms**
| Tool | Type | Purpose |
|------|------|---------|
| [SANS Security Awareness](https://www.sans.org/security-awareness-training/) | Commercial | Security training |
| [KnowBe4](https://www.knowbe4.com/) | Commercial | Awareness training |
| [Coursera](https://www.coursera.org/) | Mixed | AI security courses |

**AI Security Training Resources**
- [OWASP AI Security Training](https://owasp.org/www-project-ai-security/)
- [Google AI Security Course](https://developers.google.com/machine-learning/crash-course)
- [Microsoft AI Security Guidelines](https://www.microsoft.com/en-us/security/blog/topic/ai-security/)
- [Anthropic AI Safety Resources](https://www.anthropic.com/research)

---

## Building Practices

### TA - Threat Assessment

**Threat Modeling Tools**
| Tool | Type | Purpose |
|------|------|---------|
| [OWASP Threat Dragon](https://owasp.org/www-project-threat-dragon/) | Open Source | Visual threat modeling |
| [Microsoft Threat Modeling Tool](https://www.microsoft.com/en-us/securityengineering/sdl/threatmodeling) | Free | STRIDE methodology |
| [IriusRisk](https://www.iriusrisk.com/) | Commercial | Automated threat modeling |
| [ThreatModeler](https://threatmodeler.com/) | Commercial | Enterprise threat modeling |

**AI-Specific Threat Frameworks**
- [MITRE ATLAS](https://atlas.mitre.org/) - Adversarial Threat Landscape for AI Systems
- [OWASP AI Security Matrix](https://owaspai.org/)
- [NIST AI Adversarial ML](https://csrc.nist.gov/publications/detail/white-paper/2024/adversarial-ml-taxonomy)

**Threat Intelligence**
| Tool | Type | Purpose |
|------|------|---------|
| [MITRE ATT&CK](https://attack.mitre.org/) | Free | Threat knowledge base |
| [AlienVault OTX](https://otx.alienvault.com/) | Free | Threat intelligence sharing |
| [Recorded Future](https://www.recordedfuture.com/) | Commercial | Threat intelligence |

---

### SR - Security Requirements

**Requirements Management**
| Tool | Type | Purpose |
|------|------|---------|
| [Jira](https://www.atlassian.com/software/jira) | Commercial | Requirements tracking |
| [Linear](https://linear.app/) | Commercial | Modern issue tracking |
| [Azure DevOps](https://azure.microsoft.com/en-us/products/devops/) | Commercial | Microsoft ALM |

**Security Requirements Frameworks**
- [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) - Application Security Verification
- [NIST 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final) - Security Controls
- [CIS Controls](https://www.cisecurity.org/controls) - Critical Security Controls

**AI-Specific Requirements**
- OWASP Top 10 for LLMs requirements
- OWASP Agentic Top 10 requirements
- ISO 42001 control requirements

---

### SA - Secure Architecture

**Architecture Tools**
| Tool | Type | Purpose |
|------|------|---------|
| [Draw.io](https://app.diagrams.net/) | Free | Diagramming |
| [Lucidchart](https://www.lucidchart.com/) | Commercial | Architecture diagrams |
| [C4 Model](https://c4model.com/) | Free | Architecture documentation |
| [Structurizr](https://structurizr.com/) | Mixed | Architecture as code |

**Cloud Security Architecture**
| Tool | Type | Purpose |
|------|------|---------|
| [AWS Well-Architected Tool](https://aws.amazon.com/architecture/well-architected/) | Free | AWS architecture review |
| [Azure Architecture Center](https://docs.microsoft.com/en-us/azure/architecture/) | Free | Azure patterns |
| [GCP Architecture Framework](https://cloud.google.com/architecture/framework) | Free | GCP patterns |

**AI Architecture Patterns**
- RAG security architecture patterns
- Agent orchestration patterns
- Model serving security patterns

---

## Verification Practices

### DR - Design Review

**Design Review Tools**
| Tool | Type | Purpose |
|------|------|---------|
| [Figma](https://www.figma.com/) | Commercial | Design collaboration |
| [Miro](https://miro.com/) | Commercial | Visual collaboration |
| GitHub PR Reviews | Mixed | Code/design review |

**Design Review Checklists**
- OWASP Security Design Review Checklist
- STRIDE threat analysis checklist
- AI-specific design review (see handbook one-pagers)

---

### IR - Implementation Review

**Static Analysis - General**
| Tool | Type | Purpose |
|------|------|---------|
| [Semgrep](https://semgrep.dev/) | Open Source | Custom rules SAST |
| [SonarQube](https://www.sonarsource.com/products/sonarqube/) | Mixed | Code quality/security |
| [CodeQL](https://codeql.github.com/) | Free | GitHub security scanning |
| [Snyk Code](https://snyk.io/product/snyk-code/) | Commercial | AI-powered SAST |

**Static Analysis - Python/ML**
| Tool | Type | Purpose |
|------|------|---------|
| [Bandit](https://bandit.readthedocs.io/) | Open Source | Python security |
| [Safety](https://safetycli.com/) | Open Source | Python dependency check |
| [PyRight](https://github.com/microsoft/pyright) | Open Source | Type checking |

**AI-Specific Implementation Review**
- LangChain security patterns
- Prompt handling review
- RAG implementation review

---

### ST - Security Testing

**LLM Security Testing**
| Tool | Type | Purpose |
|------|------|---------|
| [Garak](https://github.com/leondz/garak) | Open Source | LLM vulnerability scanner |
| [PyRIT](https://github.com/Azure/PyRIT) | Open Source | Microsoft red team tool |
| [Rebuff](https://github.com/protectai/rebuff) | Open Source | Prompt injection detection |
| [LLM Guard](https://github.com/protectai/llm-guard) | Open Source | Input/output validation |
| [Vigil](https://github.com/deadbits/vigil-llm) | Open Source | LLM security scanner |

**AI Security Platforms**
| Tool | Type | Purpose |
|------|------|---------|
| [HiddenLayer](https://hiddenlayer.com/) | Commercial | AI security platform |
| [Robust Intelligence](https://www.robustintelligence.com/) | Commercial | AI validation |
| [Protect AI](https://protectai.com/) | Commercial | ML security |
| [Calypso AI](https://calypsoai.com/) | Commercial | AI security testing |

**General Security Testing**
| Tool | Type | Purpose |
|------|------|---------|
| [OWASP ZAP](https://www.zaproxy.org/) | Open Source | Web app testing |
| [Burp Suite](https://portswigger.net/burp) | Commercial | Web security testing |
| [Nuclei](https://nuclei.projectdiscovery.io/) | Open Source | Vulnerability scanner |

**Red Team Frameworks**
- [MITRE ATLAS Navigator](https://atlas.mitre.org/)
- OWASP LLM Testing Guide
- AI Red Team Playbook (Microsoft)

---

## Operations Practices

### IM - Issue Management

**Issue Tracking**
| Tool | Type | Purpose |
|------|------|---------|
| [Jira](https://www.atlassian.com/software/jira) | Commercial | Issue tracking |
| [Linear](https://linear.app/) | Commercial | Modern tracking |
| [GitHub Issues](https://github.com/features/issues) | Mixed | Developer-focused |
| [ServiceNow](https://www.servicenow.com/) | Commercial | Enterprise ITSM |

**Vulnerability Management**
| Tool | Type | Purpose |
|------|------|---------|
| [DefectDojo](https://defectdojo.github.io/django-DefectDojo/) | Open Source | Vuln management |
| [Tenable.io](https://www.tenable.com/) | Commercial | Vulnerability platform |
| [Qualys](https://www.qualys.com/) | Commercial | Vuln management |

**Incident Response**
| Tool | Type | Purpose |
|------|------|---------|
| [PagerDuty](https://www.pagerduty.com/) | Commercial | Incident management |
| [Opsgenie](https://www.atlassian.com/software/opsgenie) | Commercial | Alerting |
| [TheHive](https://thehive-project.org/) | Open Source | Security IR platform |

---

### EH - Environment Hardening

**Container Security**
| Tool | Type | Purpose |
|------|------|---------|
| [gVisor](https://gvisor.dev/) | Open Source | Container sandboxing |
| [Firecracker](https://firecracker-microvm.github.io/) | Open Source | MicroVM isolation |
| [Falco](https://falco.org/) | Open Source | Runtime security |
| [Trivy](https://aquasecurity.github.io/trivy/) | Open Source | Container scanning |

**Infrastructure Security**
| Tool | Type | Purpose |
|------|------|---------|
| [Checkov](https://www.checkov.io/) | Open Source | IaC scanning |
| [Terraform Sentinel](https://www.hashicorp.com/sentinel) | Commercial | Policy as code |
| [AWS Config](https://aws.amazon.com/config/) | Commercial | Configuration compliance |
| [Azure Policy](https://azure.microsoft.com/en-us/products/azure-policy/) | Commercial | Azure compliance |

**Secret Management**
| Tool | Type | Purpose |
|------|------|---------|
| [HashiCorp Vault](https://www.vaultproject.io/) | Mixed | Secret management |
| [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) | Commercial | AWS secrets |
| [Azure Key Vault](https://azure.microsoft.com/en-us/products/key-vault/) | Commercial | Azure secrets |

**AI Execution Sandboxes**
| Tool | Type | Purpose |
|------|------|---------|
| [E2B](https://e2b.dev/) | Commercial | Code execution sandbox |
| [Modal](https://modal.com/) | Commercial | Serverless AI |
| [Fly.io](https://fly.io/) | Commercial | App sandboxing |

---

### ML - Monitoring & Logging

**Logging & SIEM**
| Tool | Type | Purpose |
|------|------|---------|
| [Elasticsearch/ELK](https://www.elastic.co/) | Mixed | Log management |
| [Splunk](https://www.splunk.com/) | Commercial | Enterprise SIEM |
| [Datadog](https://www.datadoghq.com/) | Commercial | Observability |
| [Grafana Loki](https://grafana.com/oss/loki/) | Open Source | Log aggregation |

**AI-Specific Monitoring**
| Tool | Type | Purpose |
|------|------|---------|
| [Weights & Biases](https://wandb.ai/) | Mixed | ML experiment tracking |
| [MLflow](https://mlflow.org/) | Open Source | ML lifecycle |
| [Arize](https://arize.com/) | Commercial | ML observability |
| [WhyLabs](https://whylabs.ai/) | Commercial | AI observability |

**Anomaly Detection**
| Tool | Type | Purpose |
|------|------|---------|
| [Apache Spark MLlib](https://spark.apache.org/mllib/) | Open Source | ML for anomaly detection |
| [Amazon SageMaker](https://aws.amazon.com/sagemaker/) | Commercial | ML platform |
| [Azure Anomaly Detector](https://azure.microsoft.com/en-us/products/cognitive-services/anomaly-detector/) | Commercial | Anomaly API |

---

## Supply Chain Security

**Dependency Scanning**
| Tool | Type | Purpose |
|------|------|---------|
| [Syft](https://github.com/anchore/syft) | Open Source | SBOM generation |
| [Grype](https://github.com/anchore/grype) | Open Source | Vulnerability scanning |
| [Snyk](https://snyk.io/) | Commercial | Dependency security |
| [Socket.dev](https://socket.dev/) | Commercial | Supply chain security |

**Code Signing**
| Tool | Type | Purpose |
|------|------|---------|
| [Sigstore](https://www.sigstore.dev/) | Open Source | Keyless signing |
| [Cosign](https://github.com/sigstore/cosign) | Open Source | Container signing |
| [In-toto](https://in-toto.io/) | Open Source | Supply chain integrity |

**Model Registries**
| Tool | Type | Purpose |
|------|------|---------|
| [MLflow Model Registry](https://mlflow.org/) | Open Source | Model versioning |
| [AWS SageMaker Registry](https://aws.amazon.com/sagemaker/) | Commercial | AWS model registry |
| [Azure ML Registry](https://azure.microsoft.com/en-us/products/machine-learning/) | Commercial | Azure model registry |
| [Hugging Face](https://huggingface.co/) | Mixed | Model hub |

---

## Key References

### OWASP Resources
- [OWASP AI Exchange](https://owaspai.org/)
- [OWASP Top 10 for LLMs](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [OWASP Top 10 for Agentic Applications](https://genai.owasp.org/)
- [OWASP ML Security Top 10](https://owasp.org/www-project-machine-learning-security-top-10/)

### Industry Frameworks
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [MITRE ATLAS](https://atlas.mitre.org/)
- [ISO/IEC 42001](https://www.iso.org/standard/81230.html) - AI Management Systems
- [IEEE AI Ethics](https://ethicsinaction.ieee.org/)

### Research & Publications
- [Anthropic AI Safety Research](https://www.anthropic.com/research)
- [OpenAI Safety Research](https://openai.com/safety)
- [Google AI Safety](https://ai.google/responsibility/responsible-ai-practices/)
- [Microsoft Responsible AI](https://www.microsoft.com/en-us/ai/responsible-ai)

---

## Tool Selection Guide

### By Organization Size

**Startups (< 50 employees)**
- Focus: Open source tools, cloud-native
- Recommended: Garak, Semgrep, Grafana, GitHub Security

**Mid-Size (50-500 employees)**
- Focus: Balance of open source and commercial
- Recommended: Snyk, Datadog, HiddenLayer, PagerDuty

**Enterprise (500+ employees)**
- Focus: Enterprise-grade with support
- Recommended: Splunk, ServiceNow, Robust Intelligence, CrowdStrike

### By Budget

**Low Budget (< $10K/year)**
- All open source stack
- Garak, Semgrep, DefectDojo, ELK, Prometheus

**Medium Budget ($10K-$100K/year)**
- Mixed open source + commercial
- Snyk, Datadog, one AI security platform

**High Budget (> $100K/year)**
- Enterprise stack
- Full commercial suite with enterprise support

---

## Document Information

| Field | Value |
|-------|-------|
| Document | Tools & Resources |
| HAIAMM Version | 2.0 |
| Last Updated | January 2026 |

---

**Related Documents:**
- [First 30 Days](02-FIRST-30-DAYS.md) - Implementation guide
- [Assessment Checklist](07-ASSESSMENT-CHECKLIST.md) - Self-assessment
- [Maturity Roadmap](06-MATURITY-ROADMAP.md) - Level progression

[Back to Index](00-INDEX.md)
