import sqlite3


def create_connection(db_name):
    try:
        conn = sqlite3.connect(db_name)
        print(f"Verbindung zur Datenbank '{db_name}' erfolgreich hergestellt.")
        return conn
    except sqlite3.Error as e:
        print(f"Fehler beim Verbinden zur Datenbank: {e}")
        return None

# Tabelle erstellen
def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Noten (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                Genre TEXT NOT NULL,
                Konstellation TEXT NOT NULL
            );
        """)
        print("Tabelle 'Noten' erfolgreich erstellt.")
    except sqlite3.Error as e:
        print(f"Fehler beim Erstellen der Tabelle: {e}")

# Einfügen der Daten
def insert_data(conn, name, genre, konstellation):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Noten (name, Genre, Konstellation)
            VALUES (?, ?, ?);
        """, (name, genre, konstellation))
        conn.commit()
        print(f"Datensatz für '{name}' erfolgreich eingefügt.")
    except sqlite3.IntegrityError as e:
        print(f"Fehler beim Einfügen der Daten: {e}")

# Abrufen der Daten
def fetch_data(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Noten;")
        rows = cursor.fetchall()
        print("Daten aus der Tabelle 'Noten':")
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(f"Fehler beim Abrufen der Daten: {e}")


if __name__ == "__main__":
    database_name = "notenbank.db"
    connection = create_connection(database_name)

    if connection:
        create_table(connection)
        insert_data(connection, "Max Mustermann", "Pop", "Solo")
        insert_data(connection, "Anna Müller", "Rock", "Duett")
        fetch_data(connection)
        connection.close()
