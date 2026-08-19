from app.graph import route_after_risk, route_after_approval

def test_high_risk_requires_approval():
    assert route_after_risk({"risk_level":"HIGH"}) == "approval"

def test_low_risk_releases():
    assert route_after_risk({"risk_level":"LOW"}) == "release"

def test_unapproved_stops():
    assert route_after_approval({"approval_status":"awaiting_approval"}) == "stop"
