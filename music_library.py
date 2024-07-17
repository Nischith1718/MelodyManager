import mysql.connector


def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="your_mysql_username",
        password="your_mysql_password",
        database="music_library"
    )


def add_song(title, artist, album, genre, year):
    conn = create_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO songs (title, artist, album, genre, year) VALUES (%s, %s, %s, %s, %s)"
    values = (title, artist, album, genre, year)
    cursor.execute(sql, values)
    conn.commit()
    conn.close()
    print("Song added successfully!")

def view_songs():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM songs")
    result = cursor.fetchall()
    for row in result:
        print(row)
    conn.close()

def update_song(song_id, title, artist, album, genre, year):
    conn = create_connection()
    cursor = conn.cursor()
    sql = "UPDATE songs SET title = %s, artist = %s, album = %s, genre = %s, year = %s WHERE id = %s"
    values = (title, artist, album, genre, year, song_id)
    cursor.execute(sql, values)
    conn.commit()
    conn.close()
    print("Song updated successfully!")

def delete_song(song_id):
    conn = create_connection()
    cursor = conn.cursor()
    sql = "DELETE FROM songs WHERE id = %s"
    values = (song_id,)
    cursor.execute(sql, values)
    conn.commit()
    conn.close()
    print("Song deleted successfully!")

def search_song_by_title(title):
    conn = create_connection()
    cursor = conn.cursor()
    sql = "SELECT * FROM songs WHERE title LIKE %s"
    values = ('%' + title + '%',)
    cursor.execute(sql, values)
    result = cursor.fetchall()
    for row in result:
        print(row)
    conn.close()

def search_song_by_artist(artist):
    conn = create_connection()
    cursor = conn.cursor()
    sql = "SELECT * FROM songs WHERE artist LIKE %s"
    values = ('%' + artist + '%',)
    cursor.execute(sql, values)
    result = cursor.fetchall()
    for row in result:
        print(row)
    conn.close()

def search_song_by_genre(genre):
    conn = create_connection()
    cursor = conn.cursor()
    sql = "SELECT * FROM songs WHERE genre LIKE %s"
    values = ('%' + genre + '%',)
    cursor.execute(sql, values)
    result = cursor.fetchall()
    for row in result:
        print(row)
    conn.close()

def search_song_by_year(year):
    conn = create_connection()
    cursor = conn.cursor()
    sql = "SELECT * FROM songs WHERE year = %s"
    values = (year,)
    cursor.execute(sql, values)
    result = cursor.fetchall()
    for row in result:
        print(row)
    conn.close()

def menu():
    while True:
        print("\n--- Music Library Management System ---")
        print("1. Add a song")
        print("2. View all songs")
        print("3. Update a song")
        print("4. Delete a song")
        print("5. Search songs by title")
        print("6. Search songs by artist")
        print("7. Search songs by genre")
        print("8. Search songs by year")
        print("9. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter song title: ")
            artist = input("Enter artist name: ")
            album = input("Enter album name: ")
            genre = input("Enter genre: ")
            year = input("Enter release year: ")
            add_song(title, artist, album, genre, year)
        elif choice == "2":
            view_songs()
        elif choice == "3":
            song_id = input("Enter song ID to update: ")
            title = input("Enter new title: ")
            artist = input("Enter new artist name: ")
            album = input("Enter new album name: ")
            genre = input("Enter new genre: ")
            year = input("Enter new release year: ")
            update_song(song_id, title, artist, album, genre, year)
        elif choice == "4":
            song_id = input("Enter song ID to delete: ")
            delete_song(song_id)
        elif choice == "5":
            title = input("Enter title to search: ")
            search_song_by_title(title)
        elif choice == "6":
            artist = input("Enter artist name to search: ")
            search_song_by_artist(artist)
        elif choice == "7":
            genre = input("Enter genre to search: ")
            search_song_by_genre(genre)
        elif choice == "8":
            year = input("Enter year to search: ")
            search_song_by_year(year)
        elif choice == "9":
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    menu()
