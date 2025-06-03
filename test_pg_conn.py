import psycopg2

try:
    conn = psycopg2.connect(
        dbname='edunova',
        user='mumbi',
        password='mumbi@123',
        host='localhost',
        port='5433'
    )
    print("✅ Connected to PostgreSQL!")
    conn.close()
except Exception as e:
    print("❌ Connection failed:", e)
