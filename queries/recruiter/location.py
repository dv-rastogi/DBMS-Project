from . import conn, cursor
from prettytable import PrettyTable

def analyse():

    print("ENTER 1 FOR LOCATION WISE AVERAGE RATING")
    print("ENTER 2 FOR LOCATION WISE AGE")
    print("ENTER 3 FOR LOCATION WISE USER DENSITY")
    cho = int(input("INPUT: "))

    if cho not in [1, 2, 3]:
        print("BRUH")
        return

    if cho == 2:
        print("-- Location wise average age of users --")
        q1 = """SELECT u.Location_Country, u.Location_City, avg(timestampdiff(YEAR, DateOfBirth, NOW())) as Average_Age FROM
        users u Group by u.Location_City;
        """
        cursor.execute(q1)

    elif cho == 1:
        print("-- Location wise average rating of users --")
        q2 = """SELECT u.Location_Country, u.Location_City, avg(r.Rating) as Average_Rating FROM 
        users u, registered r WHERE u.ID = r.User_ID
        Group by u.Location_City; 
        """
        cursor.execute(q2)

    elif cho == 3:
        print("-- Location wise user density --")
        q3 = """SELECT Location_Country, Location_City, COUNT(*) as no_of_users 
        from users group by Location_Country, Location_City WITH ROLLUP; """
        cursor.execute(q3)

    t = PrettyTable(list(cursor.column_names))
    ans = cursor.fetchall()
    for x in ans:
        t.add_row(list(x))
    print(t)
    print()