import mysql.connector
from prettytable import PrettyTable

conn = mysql.connector.connect(
    user='user_codebook',
    password='user_codebook',
    host='localhost',
    database='cp-stats'
)

cursor = conn.cursor()
print("user cursor initiated!")

def query():
    print("QUERYING AS USER")
    q = input("ENTER YOUR QUERY: ")
    try:
        cursor.execute(q)
    except Exception as e:
        print("Exception occured", e)
        return
    
    try:
        t = PrettyTable(list(cursor.column_names))
        res = cursor.fetchall()
        for r in res:
            t.add_row(list(r))
        print(t)
    except Exception as e:
        pass

    conn.commit()