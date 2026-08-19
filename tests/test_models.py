"""Test data models and schemas."""
import pytest
from datetime import datetime
from app.models.schemas import (
    WorkflowRequest, WorkflowResponse, RequirementInput, UserStory
)


def test_workflow_request_validation():
    """Test WorkflowRequest validation."""
    request = WorkflowRequest(
        requirement="Build a travel portal",
        context="HR integration",
        priority="HIGH"
    )
    
    assert request.requirement == "Build a travel portal"
    assert request.context == "HR integration"
    assert request.priority == "HIGH"


def test_workflow_request_default_priority():
    """Test WorkflowRequest default priority."""
    request = WorkflowRequest(requirement="Build a portal")
    assert request.priority == "MEDIUM"


def test_workflow_response_validation():
    """Test WorkflowResponse validation."""
    response = WorkflowResponse(
        workflow_id="test-123",
        status="completed",
        created_at=datetime.now()
    )
    
    assert response.workflow_id == "test-123"
    assert response.status == "completed"
    assert response.errors == []
