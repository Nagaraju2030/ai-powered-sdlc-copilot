from typing import TypedDict

class SDLCState(TypedDict, total=False):
    requirement: str
    approved: bool
    brd: str
    architecture: str
    user_stories: str
    test_plan: str
    security_review: str
    risk_level: str
    risk_reason: str
    approval_status: str
    release_notes: str
    jira_payload: dict
