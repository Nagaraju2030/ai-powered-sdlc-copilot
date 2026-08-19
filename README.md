# AI-Powered SDLC Copilot

Agentic AI workflow that turns a business requirement into a structured SDLC package.

## GitHub description
Agentic AI SDLC workflow using LangGraph to generate requirements, architecture, user stories, tests, security review, release notes and Jira-ready artifacts.

## Workflow

```text
Requirement
 -> Requirement Agent
 -> Architecture Agent
 -> User Story Agent
 -> Test Design Agent
 -> Security Agent
 -> Risk Agent
 -> Human Approval Gate (high risk)
 -> Release Notes
 -> Jira-ready Payload
```

## Outputs

- BRD/refined requirement
- solution architecture
- user stories and acceptance criteria
- test scenarios
- security review
- delivery-risk assessment
- human approval status
- release notes
- Jira-ready JSON

## Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export OPENAI_API_KEY=...
export OPENAI_MODEL=...
uvicorn app.api:app --reload
```

Example:

```json
{
  "requirement": "Build an employee travel approval portal with manager approval, policy checks, audit history and notifications.",
  "approved": false
}
```

## Production extensions

Jira API, GitHub PR review, SonarQube, test execution agents, CI/CD generation,
persistent LangGraph checkpoints, audit logs, tracing and evaluation.
