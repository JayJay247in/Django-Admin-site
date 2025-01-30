import psycopg # type: ignore

try:
    conn = psycopg.connect(
        host="127.0.0.1",
        port=5000,
        user="postgres",
        password="Divinity:100",
        dbname="postgres"
    )
    print("Connection Successful")
    conn.close()
except psycopg.Error as e:
    print(f"Connection Error: {e}")