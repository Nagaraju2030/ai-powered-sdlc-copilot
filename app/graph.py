from langgraph.graph import END, START, StateGraph
from .state import SDLCState
from .nodes import (
    requirement_agent, architecture_agent, user_story_agent, test_design_agent,
    security_agent, risk_agent, approval_agent, release_notes_agent, jira_payload_agent
)

def route_after_risk(state):
    return "approval" if state.get("risk_level") == "HIGH" else "release"

def route_after_approval(state):
    return "release" if state.get("approval_status") == "approved" else "stop"

def build_graph():
    g = StateGraph(SDLCState)
    for name, node in [
        ("requirements", requirement_agent), ("architecture", architecture_agent),
        ("stories", user_story_agent), ("tests", test_design_agent),
        ("security", security_agent), ("risk", risk_agent),
        ("approval", approval_agent), ("release", release_notes_agent),
        ("jira_payload", jira_payload_agent)
    ]:
        g.add_node(name, node)

    g.add_edge(START, "requirements")
    g.add_edge("requirements", "architecture")
    g.add_edge("architecture", "stories")
    g.add_edge("stories", "tests")
    g.add_edge("tests", "security")
    g.add_edge("security", "risk")
    g.add_conditional_edges("risk", route_after_risk, {"approval":"approval","release":"release"})
    g.add_conditional_edges("approval", route_after_approval, {"release":"release","stop":END})
    g.add_edge("release", "jira_payload")
    g.add_edge("jira_payload", END)
    return g.compile()

sdlc_graph = build_graph()
