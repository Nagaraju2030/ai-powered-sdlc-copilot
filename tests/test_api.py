"""Test API endpoints."""
import pytest
from httpx import AsyncClient
from app.api import app


@pytest.mark.asyncio
async def test_health_check():
    """Test health check endpoint."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/health")
        assert response.status_code == 200
        assert response.json()["status"] == "healthy"


@pytest.mark.asyncio
async def test_root_endpoint():
    """Test root endpoint."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert "version" in data
        assert "endpoints" in data


@pytest.mark.asyncio
async def test_agents_endpoint():
    """Test agents info endpoint."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/api/v1/agents")
        assert response.status_code == 200
        data = response.json()
        assert "agents" in data
        assert data["total_agents"] == 8


@pytest.mark.asyncio
async def test_workflow_documentation():
    """Test workflow documentation endpoint."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/api/v1/docs/workflow")
        assert response.status_code == 200
        data = response.json()
        assert "workflow_name" in data
        assert "workflow_stages" in data
        assert "outputs" in data
