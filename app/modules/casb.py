def monitor_cloud(filepath):
    """
    Simple CASB module.
    Looks for 'UNAUTHORIZED' or 'RISK' events in cloud logs and returns alerts.
    """
    risks = []

    try:
        with open(filepath, "r") as f:
            for line in f:
                line = line.strip()
                if "UNAUTHORIZED" in line or "RISK" in line:
                    risks.append({
                        "type": "CASB Risk",
                        "message": line
                    })
    except FileNotFoundError:
        pass

    return risks
