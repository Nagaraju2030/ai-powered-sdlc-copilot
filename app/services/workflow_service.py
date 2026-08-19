"""Workflow execution service."""
import uuid
from datetime import datetime
from typing import Optional, Dict, Any
from app.workflow.graph import create_sdlc_workflow
from app.core.logger import logger
from app.models.schemas import WorkflowRequest, WorkflowResponse


class WorkflowService:
    """Service for executing SDLC workflows."""
    
    def __init__(self):
        self.workflow = create_sdlc_workflow()
        self.execution_history: Dict[str, WorkflowResponse] = {}
    
    async def execute_workflow(self, request: WorkflowRequest) -> WorkflowResponse:
        """Execute the complete SDLC workflow."""
        workflow_id = str(uuid.uuid4())
        logger.info(f"Starting workflow {workflow_id}")
        
        try:
            initial_state = {
                "requirement": request.requirement,
                "context": request.context or "",
                "priority": request.priority,
                "refined_requirement": {},
                "architecture": {},
                "user_stories": {},
                "test_design": {},
                "security_review": {},
                "risk_assessment": {},
                "approval_status": False,
                "release_notes": {},
                "jira_payload": {},
                "errors": []
            }
            
            result = await self.workflow.ainvoke(initial_state)
            
            response = WorkflowResponse(
                workflow_id=workflow_id,
                status="completed",
                created_at=datetime.now(),
                completed_at=datetime.now(),
                errors=result.get("errors", [])
            )
            
            self.execution_history[workflow_id] = response
            logger.info(f"Workflow {workflow_id} completed successfully")
            
            return response
            
        except Exception as e:
            logger.error(f"Workflow {workflow_id} failed: {str(e)}")
            response = WorkflowResponse(
                workflow_id=workflow_id,
                status="failed",
                created_at=datetime.now(),
                errors=[str(e)]
            )
            self.execution_history[workflow_id] = response
            return response
    
    def get_workflow_status(self, workflow_id: str) -> Optional[WorkflowResponse]:
        """Get workflow execution status."""
        return self.execution_history.get(workflow_id)
    
    def get_execution_history(self, limit: int = 10) -> list:
        """Get recent workflow executions."""
        return list(self.execution_history.values())[-limit:]
