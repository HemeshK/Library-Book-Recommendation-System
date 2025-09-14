# 📚 Mini Library Recommendation System

A simple **book recommendation system** built with **Python, MySQL, Flask, and scikit-learn**.  
This project demonstrates how to combine **SQL database management** with **machine learning** for practical applications.

---

## 🚀 Features
- **Database Design (ERD)** with 3 tables:
  - `Users(user_id, name, email)`
  - `Books(book_id, title, author, genre)`
  - `BorrowHistory(borrow_id, user_id, book_id, borrow_date)`
- Add new users and books.
- Record borrow events.
- Query borrowed books for a given user.
- **Recommendation Logic**:
  - For a given user, find other users who borrowed the same books.
  - Recommend books those similar users borrowed, which the current user hasn’t read yet.
- Implemented using **SQL JOINs + Python (pandas + scikit-learn)**.
- Flask web app frontend for interaction.

---

## 🛠️ Tech Stack
- **Backend**: Python (Flask)
- **Database**: MySQL
- **ML Library**: scikit-learn (Nearest Neighbors)
- **Frontend**: HTML (Jinja2 Templates)

---

## 📂 Project Structure

LibraryBook/
├── app.py             # Flask app (runs the web server)
├── recommend.py       # Recommendation model logic
├── schema.sql         # Database schema (Users, Books, BorrowHistory)
├── sample_data.sql    # Example dataset for testing
├── requirements.txt   # Dependencies
├── .gitignore         # Git ignore file
└── templates/
    └── index.html     # Frontend template

---


---

## ⚡ Setup Instructions

### 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/LibraryBook-Recommender.git
cd LibraryBook-Recommender


### 2. Install dependencies
pip install -r requirements.txt

### 3. Set up MySQL
mysql -u root -p
CREATE DATABASE LibraryDB;
USE LibraryDB;
SOURCE schema.sql;
SOURCE sample_data.sql;

### 4. Run the Flask app
python3 app.py

### Open your browser → http://127.0.0.1:5000

## 🎯 Example Output

### For Alice (User 1), sample result:
Users similar to 1: [3, 2]

📚 Recommended Books for User 1:
- The Great Gatsby
- To Kill a Mockingbird

## 💡 Future Improvements

# Potential next steps:
- Add user login & authentication
- Improve frontend (React or Figma design integration)
- Deploy on cloud (Heroku / Render / AWS)
- Add content-based filtering (recommend by author/genre)
