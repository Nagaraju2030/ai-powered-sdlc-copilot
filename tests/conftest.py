"""Test configuration and fixtures."""
import pytest
from httpx import AsyncClient
from app.api import app


@pytest.fixture
async def client():
    """Async test client."""
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac


@pytest.fixture
def sample_requirement():
    """Sample requirement for testing."""
    return {
        "requirement": "Build an employee travel approval portal with manager approval, policy checks, audit history and notifications.",
        "context": "Must integrate with existing HR system",
        "priority": "HIGH"
    }
