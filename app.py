# Imports.
from flask import Flask, render_template, request, jsonify
from db import Database

# Initialization.
app = Flask(__name__)
db = Database()


# Route - Landing Page
@app.route("/")
def landing_page():
    platform = request.user_agent.platform

    if platform == "linux":
        os_name = "LINUX"
        file_name = "linux_runner.zip"
    elif platform == "macos":
        os_name = "MACOS"
        file_name = "macos_runner.dmg"
    else:
        os_name = "WINDOWS"
        file_name = "windows_runner.exe"

    return render_template("index.html", os=os_name, file_name=file_name)


# Route - Leaderboard Page
@app.route("/leaderboard")
def leaderboard_page():
    records = db.get_top_scores()

    return render_template("leaderboard.html", players=records)


# Endpoint - User score update
@app.route("/api/add-score", methods=["POST"])
def update_score():
    data = request.json
    username = data.get("username")
    score = data.get("score")

    if not username or not score:
        return jsonify({"error": "Username and Score required"}), 400

    db.update_score(username, score)

    return jsonify({"message": "Score Updated"}), 201
