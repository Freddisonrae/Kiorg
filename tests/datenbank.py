from src.models.datenbank import create_connection, create_table

def test_create_connection():
    conn = create_connection(":memory:")
    assert conn is not None
    conn.close()

def test_create_table():
    conn = create_connection(":memory:")
    create_table(conn, "TestTable", "id", "name", "genre", "konstellation")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='TestTable';")
    table = cursor.fetchone()
    assert table is not None
    conn.close()


if __name__ == "__main__":
    test_create_connection()
    test_create_table()
    print("Alle Tests bestanden.")