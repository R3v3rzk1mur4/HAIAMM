# HAIAMM Pitch Decks

This directory contains three comprehensive pitch decks for the HAIAMM (Human-Assisted Intelligence Assurance Maturity Model) framework.

## Available Decks

### 1. Executive Pitch Deck (`01-executive-pitch-deck.md`)
**Audience:** C-suite, investors, business stakeholders, non-technical decision makers

**Duration:** 15-20 minutes

**Content:**
- Problem statement and market opportunity
- Solution overview and value proposition
- Business model and revenue streams
- Use cases and competitive advantages
- Call to action

**Best For:**
- Board presentations
- Investor pitches
- Executive briefings
- Sales presentations

---

### 2. Technical Deep Dive (`02-technical-deep-dive.md`)
**Audience:** Software architects, security engineers, developers, technical teams

**Duration:** 30-45 minutes

**Content:**
- System architecture and design patterns
- Data model and database schema
- Scoring algorithms and calculations
- Technology stack and dependencies
- Security considerations and performance optimization
- Extensibility and deployment architecture

**Best For:**
- Technical evaluations
- Architecture reviews
- Developer onboarding
- Integration planning

---

### 3. Quick Overview (`03-quick-overview.md`)
**Audience:** General audience, quick introductions, demos

**Duration:** 5-10 minutes

**Content:**
- What is HAIAMM (one-line summary)
- How it works (3-step process)
- Six security domains
- Key features and benefits
- Sample results
- Getting started

**Best For:**
- Conference presentations
- Demo sessions
- Quick introductions
- Networking events

---

## Converting Markdown to Presentation Formats

These markdown files can be converted to various presentation formats using the tools below:

### Option 1: Marp (Recommended)

**Install:**
```bash
npm install -g @marp-team/marp-cli
```

**Convert to PDF:**
```bash
marp 01-executive-pitch-deck.md -o executive-pitch.pdf
marp 02-technical-deep-dive.md -o technical-deep-dive.pdf
marp 03-quick-overview.md -o quick-overview.pdf
```

**Convert to PowerPoint:**
```bash
marp 01-executive-pitch-deck.md -o executive-pitch.pptx
marp 02-technical-deep-dive.md -o technical-deep-dive.pptx
marp 03-quick-overview.md -o quick-overview.pptx
```

**Convert to HTML:**
```bash
marp 01-executive-pitch-deck.md -o executive-pitch.html
marp 02-technical-deep-dive.md -o technical-deep-dive.html
marp 03-quick-overview.md -o quick-overview.html
```

**With Custom Theme:**
```bash
marp --theme custom-theme.css 01-executive-pitch-deck.md -o executive-pitch.pdf
```

---

### Option 2: Pandoc

**Install:**
```bash
# macOS
brew install pandoc

# Ubuntu/Debian
sudo apt-get install pandoc

# Windows
choco install pandoc
```

**Convert to PowerPoint:**
```bash
pandoc 01-executive-pitch-deck.md -o executive-pitch.pptx
pandoc 02-technical-deep-dive.md -o technical-deep-dive.pptx
pandoc 03-quick-overview.md -o quick-overview.pptx
```

**Convert to PDF (requires LaTeX):**
```bash
pandoc 01-executive-pitch-deck.md -o executive-pitch.pdf
pandoc 02-technical-deep-dive.md -o technical-deep-dive.pdf
pandoc 03-quick-overview.md -o quick-overview.pdf
```

**Convert to Beamer (LaTeX presentation):**
```bash
pandoc 01-executive-pitch-deck.md -t beamer -o executive-pitch-beamer.pdf
```

---

### Option 3: Slidev (Interactive HTML Presentations)

**Install:**
```bash
npm init slidev@latest
```

**Convert:**
1. Copy markdown content into a Slidev project
2. Add front matter:
```yaml
---
theme: default
background: https://source.unsplash.com/collection/94734566/1920x1080
class: text-center
highlighter: shiki
lineNumbers: false
drawings:
  persist: false
---
```
3. Run `npm run dev` to preview
4. Run `npm run build` to export HTML
5. Run `npm run export` to export PDF

---

### Option 4: Reveal.js

**Using reveal-md:**
```bash
npm install -g reveal-md
```

**Present:**
```bash
reveal-md 01-executive-pitch-deck.md
reveal-md 02-technical-deep-dive.md
reveal-md 03-quick-overview.md
```

**Export to PDF:**
```bash
reveal-md 01-executive-pitch-deck.md --print executive-pitch.pdf
reveal-md 02-technical-deep-dive.md --print technical-deep-dive.pdf
reveal-md 03-quick-overview.md --print quick-overview.pdf
```

**Export to HTML:**
```bash
reveal-md 01-executive-pitch-deck.md --static executive-pitch
reveal-md 02-technical-deep-dive.md --static technical-deep-dive
reveal-md 03-quick-overview.md --static quick-overview
```

---

## Customization Guide

### Adding Your Branding

1. **Replace Placeholder Content:**
   - `[Your website]` → Your actual website URL
   - `[Your email]` → Your contact email
   - `[Your GitHub repo]` → Your repository URL
   - `[Calendar link]` → Your scheduling link

2. **Add Logos:**
   - Add logo images to an `assets/` directory
   - Reference in markdown: `![HAIAMM Logo](assets/logo.png)`

3. **Customize Colors:**
   - For Marp: Create a custom CSS theme file
   - For PowerPoint: Apply your corporate template after conversion

### Tailoring Content

**For Different Industries:**
- **Financial Services:** Emphasize compliance, audit trails, regulatory requirements
- **Healthcare:** Focus on data privacy, HIPAA compliance, patient data security
- **Technology:** Highlight extensibility, API integrations, developer experience
- **Government:** Stress national security, sovereignty, offline capabilities

**For Different Audience Levels:**
- **C-Suite:** Focus on ROI, risk reduction, competitive advantage (use Executive deck)
- **Technical:** Emphasize architecture, performance, security (use Technical deck)
- **Mixed:** Start with Quick Overview, then dive deeper based on questions

---

## Presentation Tips

### Executive Pitch Deck
1. **Start Strong:** Open with the problem statement (Slide 1)
2. **Visual Focus:** Use the radar chart and heatmap visuals prominently
3. **Business Value:** Emphasize ROI and risk reduction
4. **Time Management:** 12 slides in 15 minutes = ~75 seconds per slide
5. **Call to Action:** End with clear next steps

### Technical Deep Dive
1. **Know Your Audience:** Gauge technical depth early
2. **Live Demo:** Consider running HAIAMM during the presentation
3. **Code Examples:** Be prepared to show actual code if asked
4. **Architecture First:** Start with the high-level architecture diagram
5. **Q&A Time:** Budget 10-15 minutes for technical questions

### Quick Overview
1. **Pace:** Fast-paced, high-energy delivery
2. **Visuals:** Lead with the radar chart on Slide 6
3. **Hook:** Open with "How secure are your AI systems?" question
4. **Demo:** 2-minute live demo of creating an assessment
5. **Close:** Strong CTA with next steps

---

## File Structure

```
pitch-decks/
├── README.md                      # This file
├── 01-executive-pitch-deck.md     # Business-focused pitch (12 slides)
├── 02-technical-deep-dive.md      # Technical architecture (18 slides)
├── 03-quick-overview.md           # Quick intro (10 slides)
├── assets/                        # Images, logos, diagrams (create this)
│   ├── logo.png
│   ├── radar-chart-example.png
│   └── architecture-diagram.png
└── exports/                       # Generated presentation files (create this)
    ├── executive-pitch.pdf
    ├── executive-pitch.pptx
    ├── technical-deep-dive.pdf
    ├── technical-deep-dive.pptx
    ├── quick-overview.pdf
    └── quick-overview.pptx
```

---

## Quick Start Commands

**Generate all presentations at once (Marp):**
```bash
# Create exports directory
mkdir -p exports

# Generate PDFs
marp 01-executive-pitch-deck.md -o exports/executive-pitch.pdf
marp 02-technical-deep-dive.md -o exports/technical-deep-dive.pdf
marp 03-quick-overview.md -o exports/quick-overview.pdf

# Generate PowerPoint
marp 01-executive-pitch-deck.md -o exports/executive-pitch.pptx
marp 02-technical-deep-dive.md -o exports/technical-deep-dive.pptx
marp 03-quick-overview.md -o exports/quick-overview.pptx
```

**Generate all presentations at once (Pandoc):**
```bash
# Create exports directory
mkdir -p exports

# Generate PowerPoint
for file in *.md; do
    pandoc "$file" -o "exports/${file%.md}.pptx"
done
```

---

## Recommended Presentation Setup

**For In-Person:**
- Print handouts of executive deck for stakeholders
- Bring laptop with HAIAMM installed for live demo
- Have backup PDF versions in case of technical issues

**For Virtual:**
- Share screen with presentation mode
- Use Zoom/Teams annotations for emphasis
- Record session for those who can't attend
- Share PDF follow-up via email

**For Conferences:**
- Use Quick Overview deck (10 minutes)
- Prepare 2-minute "elevator pitch" version
- Bring business cards with demo scheduling link
- Have QR code linking to GitHub repo

---

## Updates and Maintenance

**When to Update These Decks:**
- Product version changes (update roadmap slide)
- New features released (update features slide)
- Market data changes (update market opportunity slide)
- Pricing changes (update business model slide)
- Technical stack changes (update architecture slide)

**Version Control:**
- These files are tracked in the HAIAMM git repository
- Tag deck versions with product releases
- Keep changelog of major deck updates

---

## License

These pitch decks are part of the HAIAMM project and follow the same license as the main repository.

For questions or suggestions about these pitch decks, please open an issue on the GitHub repository.
