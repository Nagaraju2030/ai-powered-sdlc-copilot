import json
from .llm import ask

def requirement_agent(state):
    return {"brd": ask(
        "Act as a senior business analyst. Produce objective, scope, actors, functional and "
        "non-functional requirements, assumptions and out-of-scope items.", state["requirement"])}

def architecture_agent(state):
    return {"architecture": ask(
        "Act as a solution architect. Cover services, APIs, data, auth, deployment, observability "
        "and scalability. Do not invent requirements.", state["brd"])}

def user_story_agent(state):
    return {"user_stories": ask(
        "Generate prioritized Agile user stories with acceptance criteria and story points.",
        state["brd"])}

def test_design_agent(state):
    return {"test_plan": ask(
        "Create functional, negative, integration, security and performance test scenarios.",
        f"BRD:\n{state['brd']}\nArchitecture:\n{state['architecture']}")}

def security_agent(state):
    return {"security_review": ask(
        "Review authentication, authorization, data protection, secrets, injection, logging "
        "and abuse risks. Provide mitigations.",
        f"BRD:\n{state['brd']}\nArchitecture:\n{state['architecture']}")}

def risk_agent(state):
    text = ask(
        "Return exactly two lines: risk=<LOW|MEDIUM|HIGH> and reason=<one sentence>. "
        "Use HIGH for unresolved critical security/compliance/destructive migration risk.",
        f"Architecture:\n{state['architecture']}\nSecurity:\n{state['security_review']}")
    level, reason = "HIGH", "Ambiguous risk classification."
    for line in text.splitlines():
        if line.lower().startswith("risk="):
            value = line.split("=",1)[1].strip().upper()
            if value in {"LOW","MEDIUM","HIGH"}:
                level = value
        elif line.lower().startswith("reason="):
            reason = line.split("=",1)[1].strip()
    return {"risk_level": level, "risk_reason": reason}

def approval_agent(state):
    return {"approval_status": "approved" if state.get("approved") else "awaiting_approval"}

def release_notes_agent(state):
    return {"release_notes": ask(
        "Produce concise release notes with purpose, user impact, prerequisites, validation "
        "and rollback considerations.", json.dumps(state, indent=2))}

def jira_payload_agent(state):
    return {"jira_payload": {
        "project": "AIP",
        "epic": {"summary": state["requirement"][:120], "description": state.get("brd","")},
        "artifacts": {
            "architecture": state.get("architecture",""),
            "user_stories": state.get("user_stories",""),
            "test_plan": state.get("test_plan",""),
            "security_review": state.get("security_review",""),
            "release_notes": state.get("release_notes",""),
        },
        "risk": {"level": state.get("risk_level"), "reason": state.get("risk_reason")},
    }}
