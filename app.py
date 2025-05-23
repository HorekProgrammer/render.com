from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Пример "базы данных" с ключами
KEYS = {
    "ABC123": "2025-07-01",
    "DEF456": "2025-08-15",
}

@app.route("/validate_key", methods=["POST"])
def validate():
    data = request.get_json()
    key = data.get("key")
    if key not in KEYS:
        return jsonify({"valid": False, "reason": "not_found"}), 404

    expiry = datetime.strptime(KEYS[key], "%Y-%m-%d")
    if datetime.now() > expiry:
        return jsonify({"valid": False, "reason": "expired"}), 403

    return jsonify({"valid": True})
