# Contributing to HAIAMM

Thank you for your interest in contributing to HAIAMM (Human-Assisted Intelligence Assurance Maturity Model)! We welcome contributions from the security community to improve and evolve this framework.

---

## 🎯 How to Contribute

### 1. Framework Improvements

**What You Can Contribute:**
- ✅ New assessment questions for existing practices
- ✅ Improved question clarity or wording
- ✅ Additional maturity level criteria
- ✅ Domain-specific guidance and examples
- ✅ Real-world case studies and scenarios
- ✅ Translations to other languages

**Process:**
1. Fork the repository
2. Create a feature branch (`git checkout -b improve-security-testing-practice`)
3. Make your changes to `config/haiamm_multi_domain_data_v2.json` or docs
4. Submit a pull request with detailed explanation
5. Community review and discussion
6. Merge upon approval

### 2. Documentation Contributions

**What We Need:**
- Implementation guides for specific industries (finance, healthcare, etc.)
- Tool integration examples (SIEM, SOAR, GRC platforms)
- Assessment best practices and lessons learned
- Industry benchmarking data
- FAQ additions

**Process:**
1. Create new `.md` file in `docs/` directory
2. Follow existing documentation style
3. Submit PR with clear description

### 3. Software & Tool Improvements

**What You Can Build:**
- UI/UX enhancements
- New visualization types
- Export formats (PDF, PowerPoint, etc.)
- API integrations
- Automated assessment tools
- Mobile app versions

**Process:**
1. Open an issue describing your proposal
2. Get feedback from maintainers
3. Implement following coding standards (see below)
4. Submit PR with tests

### 4. Bug Reports

**How to Report:**
1. Check existing issues first
2. Open new issue with:
   - Clear description of bug
   - Steps to reproduce
   - Expected vs actual behavior
   - Environment details (OS, Python version)
   - Screenshots if applicable

### 5. Feature Requests

**How to Propose:**
1. Open issue with `[Feature Request]` tag
2. Describe the problem you're solving
3. Propose solution approach
4. Community discussion
5. Approval from maintainers before implementation

---

## 📋 Contribution Guidelines

### Framework Changes (Questions, Practices, Maturity Levels)

**Review Criteria:**
- ✅ Aligns with HAIAMM philosophy (AI implementation maturity assessment)
- ✅ Doesn't duplicate existing questions
- ✅ Clear, unambiguous wording
- ✅ Applicable across multiple industries
- ✅ Measurable/verifiable criteria
- ✅ Appropriate maturity level placement

**Required Information:**
- Rationale for change
- Industry/domain applicability
- Impact on existing assessments
- Backward compatibility considerations

### Code Contributions

**Coding Standards:**
- Python 3.10+ compatibility
- PEP 8 style guide
- Type hints where applicable
- Docstrings for all public methods
- Unit tests for new features (>80% coverage)

**Before Submitting:**
```bash
# Run linter
ruff check .

# Run tests
pytest

# Check type hints
mypy .
```

### Documentation Standards

**Style Guide:**
- Markdown format (GitHub-flavored)
- Clear headings and structure
- Code examples where applicable
- Links to related docs
- Spell-check before submitting

---

## 🏛️ Governance Model

### Maintainers

**Core Maintainer:**
- Kuai Hinojosa (Project Creator)
- Final approval on framework changes
- Strategic direction

**Community Maintainers:**
- Experienced contributors with commit access
- Review and approve PRs
- Moderate discussions
- Appointed by core maintainer

### Decision Making

**Minor Changes** (typos, clarifications, bug fixes):
- Single maintainer approval
- Fast-track merge

**Major Changes** (new practices, structural changes):
- Community discussion (minimum 2 weeks)
- Multiple maintainer approval
- Core maintainer final decision

**Framework Evolution:**
- Annual review cycle
- Community input via surveys/discussions
- Major version releases (v3.0, v4.0) with RFC process

---

## 🎓 Becoming an Official HAIAMM Service Provider

While the HAIAMM framework is open source, offering **Official HAIAMM Certification** or **HAIAMM Certified Assessor** credentials requires authorization.

### Free Use (No Authorization Required):
- ✅ Use HAIAMM for internal assessments
- ✅ Build tools and software using HAIAMM
- ✅ Teach and train using HAIAMM materials (with attribution)
- ✅ Offer consulting using HAIAMM framework

### Official Services (Authorization Required):
- ✗ "Official HAIAMM Certification"
- ✗ "HAIAMM Certified Assessor" credentials
- ✗ Using HAIAMM trademark for commercial assessment services

**Why Authorization?**
- Quality control for official certifications
- Consistency in assessment methodology
- Protection of HAIAMM brand reputation
- Support for framework maintenance

**How to Become Authorized:**
1. Demonstrate expertise (contributions, case studies)
2. Complete HAIAMM Assessor Training (when available)
3. Pass certification exam
4. Sign service provider agreement
5. Maintain quality standards

**Contact:** [your-email] for authorization inquiries

---

## 🤝 Community Guidelines

### Code of Conduct

**We Are Committed To:**
- Inclusive, welcoming environment
- Respectful discourse
- Constructive feedback
- Collaborative problem-solving

**Not Tolerated:**
- Harassment or discrimination
- Personal attacks
- Spam or promotional content
- Violation of intellectual property rights

**Enforcement:**
- First violation: Warning
- Second violation: Temporary ban
- Serious/repeated violations: Permanent ban

### Communication Channels

**GitHub Issues:** Bug reports, feature requests
**GitHub Discussions:** Community Q&A, brainstorming
**Pull Requests:** Code/content contributions
**Email:** [your-email] for sensitive matters

---

## 📊 Contribution Recognition

### Contributors List

All contributors will be recognized in:
- `CONTRIBUTORS.md` file
- Annual project report
- Release notes for their contributions

### Levels of Recognition:

**🌟 Framework Contributor:** Improved questions, practices, maturity levels
**💻 Code Contributor:** Software features, bug fixes, tools
**📚 Documentation Contributor:** Guides, examples, translations
**🔍 Issue Reporter:** High-quality bug reports and feature requests
**🎓 Community Leader:** Maintainer, educator, advocate

---

## 🚀 Getting Started

### First-Time Contributors

**Easy First Issues:**
- Look for `good-first-issue` tag
- Documentation improvements
- Typo fixes
- Adding examples or case studies

**Suggested Flow:**
1. ⭐ Star the repository
2. 📖 Read through documentation
3. 🐛 Try the tool yourself
4. 💡 Identify improvement area
5. 💬 Open issue to discuss
6. 🔨 Submit PR

### Development Setup

```bash
# Clone repository
git clone https://github.com/[your-repo]/HAIAMM.git
cd HAIAMM

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install dev dependencies
pip install -r requirements-dev.txt

# Run tests
pytest

# Run application
python main.py
```

---

## 📜 Contributor License Agreement (CLA)

**By contributing to HAIAMM, you agree:**

1. You have the right to contribute the content
2. Your contribution is licensed under the same license as HAIAMM:
   - Framework content: CC BY-SA 4.0
   - Software: MIT License
3. You grant the project maintainers right to use your contribution
4. You waive any moral rights that may interfere with project use

**No Separate CLA Required:**
- Opening a PR constitutes agreement
- We follow GitHub's standard contribution terms

---

## 🙏 Thank You!

Your contributions help make HAIAMM the standard framework for HAI security assessment. Together, we're building a safer AI security future.

**Questions?**
- Open a GitHub Discussion
- Email: [your-email]
- Check the FAQ: docs/FAQ.md

---

**Version:** 1.0
**Last Updated:** December 14, 2025
**Maintainer:** Kuai Hinojosa
