import psycopg2

try:
    conn = psycopg2.connect(
        host="127.0.0.1",
        port=5000,
        user="postgres",
        password="Divinity:100",
        dbname="postgres"
    )
    print("Connection Successful")
    conn.close()
except psycopg2.Error as e:
    print(f"Connection Error: {e}")