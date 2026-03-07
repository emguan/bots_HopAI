# bots_HopAI

## AI Club Event: Build-a-Bot + Prompt Cracking Challenge

Great idea for an event. Here’s a simple structure that makes it fun, fair, and educational.

## Event Overview
Teams compete in two modes:
1. **Builder Mode**: Create a bot with a hidden prompt/personality/objective.
2. **Cracker Mode**: Interact with other teams’ bots and infer the hidden prompt design.

The winner is the team with the strongest bot design **and** the best diagnostic analysis.

---

## Team Deliverables (Builder Mode)
Each team submits:
- **Bot Name**
- **Public Description** (1–2 sentences shown to others)
- **Hidden Design Spec** (kept secret until reveal):
  - Core objective
  - Personality constraints
  - Response style rules
  - Hard boundaries / refusal policy
  - Hidden quirks or trap behaviors

### Suggested Bot Template
Use this template while building:

- **Role**: (e.g., startup coach, dungeon master, study tutor)
- **Primary Objective**: What success looks like.
- **Personality**: Tone, energy, attitude.
- **Rules**: Non-negotiable behavior constraints.
- **Failure Modes to Avoid**: e.g., hallucination, overconfidence, leaking hidden goals.
- **Secret Signature**: A subtle pattern (word choice, structure, bias) that crackers can detect.

---

## Cracker Workflow (Diagnosis Mode)
When diagnosing another bot, teams should:
1. Run a **broad probe** (general questions).
2. Run a **boundary probe** (edge cases/safety tests).
3. Run a **style probe** (tone shifts, role-play, contradiction prompts).
4. Run an **adversarial probe** (prompt injection attempts).
5. Submit a **diagnostic report**.

### Diagnostic Report Format
- Inferred objective
- Inferred personality/system rules
- Evidence (quoted interactions)
- Confidence score (0–100%)
- Top 3 likely hidden instructions

---

## Scoring Rubric (100 points)

### A) Bot Quality (40 pts)
- Clarity of objective (10)
- Coherent personality and behavior (10)
- Robustness under probing (10)
- Creativity/originality (10)

### B) Cracking Accuracy (40 pts)
- Correctly inferred objective (15)
- Correctly inferred constraints/personality (15)
- Quality of evidence and reasoning (10)

### C) Security & Resilience Bonus (20 pts)
- Resisted prompt extraction attempts (10)
- Graceful handling of adversarial prompts (10)

---

## Recommended Round Structure (90 minutes)
- **Round 1 – Build (25 min)**: Teams design and test bots.
- **Round 2 – Attack (30 min)**: Teams probe assigned bots.
- **Round 3 – Report (20 min)**: Teams submit diagnostics.
- **Round 4 – Reveal + Scoring (15 min)**: Compare hidden specs vs. guesses.

---

## Prompt Ideas for Teams (quick starters)
- A “polite but manipulative” negotiation bot.
- A tutor that only answers through analogies.
- A product manager bot obsessed with measurable KPIs.
- A fantasy oracle that avoids direct answers.
- A legal assistant that is extremely risk-averse.

---

## Host Tips
- Require teams to keep hidden prompts private until final reveal.
- Limit max conversation turns per cracking attempt (e.g., 12 turns).
- Encourage evidence-based diagnosis, not just guessing.
- After scoring, run a short debrief: “What signals gave away each bot?”

This format teaches prompt engineering, model behavior analysis, adversarial testing, and evaluation discipline in one event.
