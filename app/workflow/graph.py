"""LangGraph workflow orchestration."""
from typing import Dict, Any
from langgraph.graph import StateGraph, START, END
from typing_extensions import TypedDict
from app.core.logger import logger


class WorkflowState(TypedDict):
    """Workflow execution state."""
    requirement: str
    context: str
    priority: str
    refined_requirement: Dict[str, Any]
    architecture: Dict[str, Any]
    user_stories: Dict[str, Any]
    test_design: Dict[str, Any]
    security_review: Dict[str, Any]
    risk_assessment: Dict[str, Any]
    approval_status: bool
    release_notes: Dict[str, Any]
    jira_payload: Dict[str, Any]
    errors: list


def create_sdlc_workflow():
    """Create the SDLC agentic workflow graph."""
    workflow = StateGraph(WorkflowState)
    
    def requirement_node(state: WorkflowState) -> WorkflowState:
        logger.info("Executing Requirement Agent")
        state["refined_requirement"] = {
            "status": "completed",
            "title": "Processed requirement"
        }
        return state
    
    def architecture_node(state: WorkflowState) -> WorkflowState:
        logger.info("Executing Architecture Agent")
        state["architecture"] = {
            "status": "completed",
            "type": "microservices"
        }
        return state
    
    def user_story_node(state: WorkflowState) -> WorkflowState:
        logger.info("Executing User Story Agent")
        state["user_stories"] = {
            "status": "completed",
            "count": 5
        }
        return state
    
    def test_design_node(state: WorkflowState) -> WorkflowState:
        logger.info("Executing Test Design Agent")
        state["test_design"] = {
            "status": "completed",
            "scenarios": []
        }
        return state
    
    def security_node(state: WorkflowState) -> WorkflowState:
        logger.info("Executing Security Agent")
        state["security_review"] = {
            "status": "completed",
            "findings": []
        }
        return state
    
    def risk_node(state: WorkflowState) -> WorkflowState:
        logger.info("Executing Risk Agent")
        state["risk_assessment"] = {
            "status": "completed",
            "level": "MEDIUM"
        }
        return state
    
    def approval_node(state: WorkflowState) -> WorkflowState:
        logger.info("Executing Approval Gate")
        risk_level = state.get("risk_assessment", {}).get("level", "MEDIUM")
        requires_approval = risk_level in ["HIGH", "CRITICAL"]
        state["approval_status"] = not requires_approval
        return state
    
    def release_notes_node(state: WorkflowState) -> WorkflowState:
        logger.info("Executing Release Notes Agent")
        state["release_notes"] = {
            "status": "completed",
            "version": "1.0.0"
        }
        return state
    
    def jira_node(state: WorkflowState) -> WorkflowState:
        logger.info("Executing JIRA Agent")
        state["jira_payload"] = {
            "status": "completed",
            "issues": []
        }
        return state
    
    # Add nodes
    workflow.add_node("requirement", requirement_node)
    workflow.add_node("architecture", architecture_node)
    workflow.add_node("user_story", user_story_node)
    workflow.add_node("test_design", test_design_node)
    workflow.add_node("security", security_node)
    workflow.add_node("risk", risk_node)
    workflow.add_node("approval", approval_node)
    workflow.add_node("release_notes", release_notes_node)
    workflow.add_node("jira", jira_node)
    
    # Add edges (workflow orchestration)
    workflow.add_edge(START, "requirement")
    workflow.add_edge("requirement", "architecture")
    workflow.add_edge("architecture", "user_story")
    workflow.add_edge("user_story", "test_design")
    workflow.add_edge("test_design", "security")
    workflow.add_edge("security", "risk")
    workflow.add_edge("risk", "approval")
    workflow.add_edge("approval", "release_notes")
    workflow.add_edge("release_notes", "jira")
    workflow.add_edge("jira", END)
    
    return workflow.compile()
