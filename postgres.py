import psycopg2


def insert_func(parent, child):
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="postgres",
        user="postgres",
        password="paria"
    )
    cursor = conn.cursor()
    insert_query = """ INSERT INTO edges (ParentURL, ChildURL) VALUES (%s,%s)"""
    record = (parent, child)
    cursor.execute(insert_query, record)
    conn.commit()
    conn.close()
