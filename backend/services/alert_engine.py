def generate_threat_alert(record):
    """
    Generate a defensive alert for high-risk synthetic threat intelligence.

    CSV values are strings when read using csv.DictReader, so risk_score
    and confidence_score are explicitly converted to integers here.
    """

    try:
        risk_score = int(record.get("risk_score", 0))
        confidence_score = int(record.get("confidence_score", 0))
    except (TypeError, ValueError):
        # Invalid numeric values should not crash database seeding.
        return None

    if risk_score >= 75 or (
        confidence_score >= 85 and risk_score >= 60
    ):
        return {
            "alert_id": "ALT-" + record["threat_id"],
            "threat_id": record["threat_id"],
            "timestamp": record["last_seen"],
            "alert_type": "HIGH_RISK_SYNTHETIC_INDICATOR",
            "severity": record["severity"],
            "risk_score": risk_score,
            "confidence_score": confidence_score,
            "description": (
                "Synthetic intelligence crossed the demo alert threshold."
            ),
            "status": "NEW",
        }

    return None