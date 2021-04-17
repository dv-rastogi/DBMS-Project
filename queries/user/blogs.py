from . import conn, cursor
from datetime import date

def add_blog():
    u = input("Enter USER_ID: ")
    n = input("Enter Name of the Blog: ")
    c = input("Enter Content for the Blog: ")
    t = input("Enter tag of the Blog: ")

    d = str(date.today())
    q1 = """INSERT INTO Blogs (ID, Name, Date, Content, Likes) VALUES (%s, %s, %s, %s, %s) """
    r1 = (u, n,d, c, 0)

    q2 = """INSERT INTO Blogs_Tags (ID, Name, Date, Tag) VALUES (%s, %s, %s, %s) """
    r2 = (u, n, d, t)

    try:
        cursor.execute(q1, r1)
        conn.commit()
        print("Blog inserted!")

        cursor.execute(q2, r2)
        conn.commit()
        print("Blogs tag registered!")
        
    except Exception as e:
        print(e)


    
    