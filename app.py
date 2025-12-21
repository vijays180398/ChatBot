from flask import Flask, render_template, request, jsonify
import sqlite3
from chatbot import get_response
from datetime import datetime

app = Flask(__name__)

# ---------- DATABASE SETUP ----------
def get_db_connection():
    conn = sqlite3.connect("chat.db")
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS chats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_message TEXT,
            bot_reply TEXT,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

create_table()
# -----------------------------------

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    bot_reply = get_response(user_message)
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Save to database
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO chats (user_message, bot_reply, timestamp) VALUES (?, ?, ?)",
        (user_message, bot_reply, time)
    )
    conn.commit()
    conn.close()

    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
