# Marsha AI – Sponsorship Coordinator

> **Version:** v0.1.0 – Workflow Engine Complete

The Sponsorship Coordinator is the first AI employee being developed as part of the Marsha AI platform.

Its purpose is to help nonprofit organizations identify sponsors, manage outreach, coordinate follow-up, and build long-term sponsorship relationships through an AI-powered workflow system.

This project is not intended to be a chatbot.

It is a workflow engine that guides an organization from sponsorship planning through prospect research, outreach, follow-up, and opportunity management.

---

# Current Status

**Current Release**

- v0.1.0 – Workflow Engine Complete

Phase 1 has been completed and validated.

The complete sponsorship workflow has been tested through runtime validation and automated regression testing.

---

# Major Features

## Research

- Contact Research Worker
- Decision-maker identification
- Email support
- Phone support
- Contact-form support

## Outreach

- AI-generated outreach
- Message Quality Review Worker
- Subject generation
- TEST email delivery
- LIVE email delivery

## Follow-Up

- Follow-up generation
- Follow-up regeneration
- AI Quality Review
- TEST follow-up delivery
- LIVE follow-up delivery
- Automatic scheduling
- Manual completion option

## Pipeline

- Opportunity records
- Opportunity stages
- Follow-up scheduling
- Notes
- Prospect management

---

# Technology Stack

- Python
- Flask
- SQLAlchemy
- SQLite (development)
- Bootstrap
- OpenAI API
- Gmail SMTP
- GitHub Actions
- Pytest

---

# Installation

Clone the repository.

```bash
git clone https://github.com/MarshaKDesigns-Dev/sponsorship-coordinator-mvp.git

cd sponsorship-coordinator-mvp
```

Create a virtual environment.

```bash
python -m venv venv
```

Activate it.

Windows

```bash
venv\Scripts\activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Copy

```text
.env.example
```

to

```text
.env
```

Configure:

- OpenAI API Key
- Gmail SMTP credentials
- TEST_MODE
- TEST_EMAIL

---

# Run the Application

```bash
python app.py
```

Default URL

```
http://127.0.0.1:5000
```

---

# Run Tests

```bash
pytest -q
```

Current regression suite:

**13 automated tests**

---

# Development Workflow

Development follows a feature branch workflow.

Every feature is developed using:

1. Feature Branch
2. Local Testing
3. Regression Testing
4. Pull Request
5. GitHub Actions Validation
6. Merge to Main
7. Runtime Validation
8. GitHub Release

---

# Documentation

Additional documentation is located in:

```
docs/
```

Including:

- ROADMAP.md
- CHANGELOG.md
- MILESTONES.md

---

# Roadmap

Phase 2 will focus on onboarding.

Upcoming work includes:

- Organization Profile
- Sponsorship Questionnaire
- Sponsorship Initiative Builder
- Sponsorship Asset Builder
- Sponsor Category Recommendation Engine
- Automatic Prospect Generation

---

# Vision

The Sponsorship Coordinator is the first AI employee within the larger Marsha AI platform.

The long-term objective is to build specialized AI employees that execute complete business workflows rather than simply answering questions.

Each AI employee will become a reusable component within the Marsha AI ecosystem.

---

# License

Copyright © Marsha K Designs.

All rights reserved.