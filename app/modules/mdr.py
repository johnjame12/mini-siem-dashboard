def respond(threats):
    """
    Simple MDR module.
    Takes a list of alerts (from SIEM + CASB) and generates response actions.
    """
    actions = []

    for threat in threats:
        action = {
            "source": threat["type"],
            "detail": threat["message"],
            "action": ""
        }

        # Example response rules
        if threat["type"] == "SIEM Alert":
            action["action"] = "Notify SOC team and lock user account"
        elif threat["type"] == "CASB Risk":
            action["action"] = "Block cloud access and alert admin"

        actions.append(action)

    return actions
