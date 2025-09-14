import mysql.connector
import pandas as pd
from sklearn.neighbors import NearestNeighbors

def get_connection():
    """Direct MySQL connection (no dotenv)."""
    return mysql.connector.connect(
        host="localhost",
        user="pyuser",          # 🔑 your MySQL username
        password="py_password", # 🔑 your MySQL password
        database="LibraryDB"
    )

def recommend_books(user_id):
    """Return recommended book titles for a given user_id."""
    conn = get_connection()

    # Load data from MySQL
    df = pd.read_sql("SELECT user_id, book_id FROM BorrowHistory;", conn)
    books = pd.read_sql("SELECT * FROM Books;", conn)
    conn.close()

    if user_id not in df["user_id"].unique():
        return []  # No history for this user → no recommendations

    # Step 1: Build User-Item Matrix
    user_item_matrix = pd.crosstab(df['user_id'], df['book_id'])

    # Step 2: Train NearestNeighbors model
    model = NearestNeighbors(metric="cosine", algorithm="brute")
    model.fit(user_item_matrix)

    # Step 3: Get vector for target user
    user_vector = user_item_matrix.loc[user_id].values.reshape(1, -1)

    # Find similar users
    distances, indices = model.kneighbors(user_vector, n_neighbors=3)
    similar_users = user_item_matrix.index[indices.flatten()].tolist()
    similar_users.remove(user_id)  # exclude same user

    # Step 4: Find books borrowed by similar users but not current user
    user_books = set(df[df["user_id"] == user_id]["book_id"])
    recommendations = set()

    for sim_user in similar_users:
        sim_books = set(df[df["user_id"] == sim_user]["book_id"])
        recommendations |= (sim_books - user_books)

    # Step 5: Convert book_ids → titles
    rec_titles = []
    for book_id in recommendations:
        title = books.loc[books["book_id"] == book_id, "title"].values
        if len(title) > 0:
            rec_titles.append(title[0])

    return rec_titles
