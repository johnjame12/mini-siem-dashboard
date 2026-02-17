
from app.modules.siem import analyze_logs
from app.modules.casb import monitor_cloud
from app.modules.mdr import respond
from app.models.threat import Threat
from ..core.extensions import db

def run_security_engine():
    """
    Run SIEM + CASB + MDR, store all alerts in database.
    """
    siem_alerts = analyze_logs("data/logs.txt")
    casb_risks = monitor_cloud("data/cloud_activity.txt")
    combined_alerts = siem_alerts + casb_risks

    # Generate MDR actions
    mdr_actions = respond(combined_alerts)

    # Clear old entries (optional)
    Threat.query.delete()

    # Save all alerts and actions to DB
    for threat in combined_alerts:
        # Find MDR action
        action = next((a["action"] for a in mdr_actions if a["detail"] == threat["message"]), "")
        db.session.add(Threat(
            type=threat["type"],
            source=threat["type"],
            detail=threat["message"],
            action=action
        ))

    db.session.commit()

    return {
        "siem": siem_alerts,
        "casb": casb_risks,
        "mdr": mdr_actions
    }
