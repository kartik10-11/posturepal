"""
AI Posture Correction System - Flask Backend
============================================
This is the backend (server) of the project.
It receives posture data from the frontend and stores it.
"""

from flask import Flask, render_template, request, jsonify
from datetime import datetime
import json
import os

# Create the Flask app
app = Flask(__name__)

# This file stores all posture logs (acts as our simple database)
LOG_FILE = "posture_logs.json"

# ─── Helper: load logs from file ─────────────────────────
def load_logs():
    if not os.path.exists(LOG_FILE):
        return []
    with open(LOG_FILE, "r") as f:
        try:
            return json.load(f)
        except:
            return []

# ─── Helper: save logs to file ───────────────────────────
def save_logs(logs):
    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)

# ════════════════════════════════════════════════════════
#  ROUTES
# ════════════════════════════════════════════════════════

# Route 1: Main page - serves the frontend HTML
@app.route("/")
def index():
    return render_template("index.html")


# Route 2: API to receive posture data from frontend
# Frontend calls this every time posture changes
@app.route("/api/log-posture", methods=["POST"])
def log_posture():
    try:
        data = request.get_json()

        # Create a log entry
        log_entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "posture":   data.get("posture", "unknown"),    # correct / bad / worst
            "neck_angle":    data.get("neck_angle", 0),
            "spine_angle":   data.get("spine_angle", 0),
            "shoulder_diff": data.get("shoulder_diff", 0),
            "hip_diff":      data.get("hip_diff", 0),
            "streak_seconds": data.get("streak_seconds", 0)
        }

        # Load existing logs, add new entry, save back
        logs = load_logs()
        logs.append(log_entry)

        # Keep only last 500 entries (prevents file getting too big)
        if len(logs) > 500:
            logs = logs[-500:]

        save_logs(logs)

        return jsonify({"status": "success", "message": "Posture logged!"}), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


# Route 3: API to get all posture logs (for dashboard/history)
@app.route("/api/get-logs", methods=["GET"])
def get_logs():
    logs = load_logs()
    return jsonify({
        "status": "success",
        "total": len(logs),
        "logs": logs[-50:]  # Return last 50 entries
    }), 200


# Route 4: API to get posture summary/stats
@app.route("/api/summary", methods=["GET"])
def get_summary():
    logs = load_logs()

    if not logs:
        return jsonify({
            "status": "success",
            "summary": {
                "total_sessions": 0,
                "correct_count": 0,
                "bad_count": 0,
                "worst_count": 0,
                "correct_percent": 0
            }
        })

    correct = sum(1 for l in logs if l["posture"] == "correct")
    bad     = sum(1 for l in logs if l["posture"] == "bad")
    worst   = sum(1 for l in logs if l["posture"] == "worst")
    total   = len(logs)

    return jsonify({
        "status": "success",
        "summary": {
            "total_sessions":   total,
            "correct_count":    correct,
            "bad_count":        bad,
            "worst_count":      worst,
            "correct_percent":  round((correct / total) * 100, 1) if total else 0
        }
    }), 200


# Route 5: Clear all logs
@app.route("/api/clear-logs", methods=["POST"])
def clear_logs():
    save_logs([])
    return jsonify({"status": "success", "message": "Logs cleared!"}), 200


# ════════════════════════════════════════════════════════
#  START THE SERVER
# ════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("=" * 50)
    print("  AI Posture Correction System - Backend")
    print("  Open browser at: http://localhost:5000")
    print("=" * 50)
    app.run(debug=True, port=5000)
