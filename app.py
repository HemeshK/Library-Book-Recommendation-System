import mysql.connector
from flask import Flask, request, render_template
from recommend import recommend_books

app = Flask(__name__)

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="pyuser",         # 🔑 your MySQL username
        password="your_password_here", # 🔑 your MySQL password
        database="LibraryDB"
    )

def get_users():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT user_id, name FROM Users;")
    users = cursor.fetchall()
    conn.close()
    return users

@app.route("/", methods=["GET", "POST"])
def home():
    recs = []
    users = get_users()
    selected_user = None

    if request.method == "POST":
        user_id = int(request.form["user_id"])
        selected_user = user_id
        recs = recommend_books(user_id)  # returns list of book titles

    return render_template("index.html", recs=recs, users=users, selected_user=selected_user)

if __name__ == "__main__":
    app.run(debug=True)
