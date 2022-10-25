import psycopg2
import json

with open("./secret.json","r",encoding="utf-8") as f:
    secret_data = json.loads(f.read()) # 리스트는 힙 영역에 저장됨 

conn = None
cursor = None

def connect():    
    global conn, cursor
    dbname = secret_data.get("dbname")
    user = secret_data.get("user")
    password = secret_data.get("password")
    host = secret_data.get("host")
    port = secret_data.get("port")

    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
    cursor = conn.cursor() 

def close():
    conn.commit()
    cursor.close()
    conn.close()

def is_login(user_id, user_pwd):
    connect()
    cursor.execute(f"""
        SELECT *
        FROM Users
        WHERE email = '{user_id}' and password='{user_pwd}'
    """)
    data = cursor.fetchone()
    close() 
    return data

def likes(user_id):
    connect()
    cursor.execute(f"""
        SELECT user_id
        FROM Likes
        WHERE user_id = '{user_id}';
    """)

    is_like = cursor.fetchone()
    
    if is_like:
        # 좋아요를 눌렀다면 -> DELETE
        cursor.execute(f"""
            DELETE FROM Likes
            WHERE user_id = '{user_id}';
        """)
    else:
        # 안눌렀다면 -> INSERT
        cursor.execute(f"""
            INSERT INTO Likes
            VALUES('{user_id}')
        """)

    close()
    return is_like

def counting_likes():
    connect()
    cursor.execute(f"""
        SELECT COUNT(user_id)
        FROM Likes;
    """)
    data = cursor.fetchone()
    close()
    return data

# cursor.execute("SELECT * FROM Users;")
# data = cursor.fetchone()
# print(data)