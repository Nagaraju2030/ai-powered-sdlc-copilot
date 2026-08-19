"""Test SDLC agents."""
import pytest
from app.agents.requirement_agent import RequirementAgent
from app.agents.architecture_agent import ArchitectureAgent
from app.agents.user_story_agent import UserStoryAgent


def test_requirement_agent_initialization():
    """Test RequirementAgent initialization."""
    agent = RequirementAgent()
    assert agent.name == "RequirementAgent"
    assert agent.description == "Refines business requirements into structured BRD format"


def test_architecture_agent_initialization():
    """Test ArchitectureAgent initialization."""
    agent = ArchitectureAgent()
    assert agent.name == "ArchitectureAgent"
    assert agent.description == "Designs solution architecture and technical approach"


def test_user_story_agent_initialization():
    """Test UserStoryAgent initialization."""
    agent = UserStoryAgent()
    assert agent.name == "UserStoryAgent"
    assert agent.description == "Generates user stories with acceptance criteria"
