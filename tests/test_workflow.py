"""Test SDLC workflow."""
import pytest
from app.models.schemas import WorkflowRequest, WorkflowResponse
from app.services.workflow_service import WorkflowService


@pytest.mark.asyncio
async def test_workflow_execution():
    """Test workflow execution."""
    service = WorkflowService()
    request = WorkflowRequest(
        requirement="Build a travel approval portal",
        context="HR system integration",
        priority="HIGH"
    )
    
    response = await service.execute_workflow(request)
    
    assert response.workflow_id is not None
    assert response.status == "completed"
    assert response.created_at is not None


def test_workflow_history():
    """Test workflow history."""
    service = WorkflowService()
    history = service.get_execution_history(limit=5)
    
    assert isinstance(history, list)
    assert len(history) <= 5
