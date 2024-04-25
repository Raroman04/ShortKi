import sqlite3

def create_database():
    conn = sqlite3.connect('shortki.db')
    cursor = conn.cursor()

    # Create the 'users' table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, hashed_password TEXT)''') 

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

def insert_user(username, password):
    conn = sqlite3.connect('shortki.db')
    cursor = conn.cursor()

    # Insert a new user into the 'users' table
    cursor.execute("INSERT INTO users (username, hashed_password) VALUES (?, ?)", (username, password))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

def fetch_user_from_database(username):
    try:
        conn = sqlite3.connect('shortki.db')
        cursor = conn.cursor()

        cursor.execute("SELECT id, username, hashed_password FROM users WHERE username = ?", (username,))
        user_data = cursor.fetchone()  # Fetches one row (the matching user)

        conn.close()
        return user_data  # Return a tuple: (id, username, hashed_password)

    except sqlite3.Error as error:
        print("Failed to fetch user data:", error)
        return None  # Return None on database error