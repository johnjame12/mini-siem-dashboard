# app/modules/siem.py

def analyze_logs(filepath):
    """
    Simple SIEM log analyzer.
    Looks for 'FAILED' or 'ERROR' in logs and returns alerts.
    """
    alerts = []

    try:
        with open(filepath, "r") as f:
            for line in f:
                line = line.strip()
                if "FAILED" in line or "ERROR" in line:
                    alerts.append({
                        "type": "SIEM Alert",
                        "message": line
                    })
    except FileNotFoundError:
        pass  # No logs yet, ignore

    return alerts
