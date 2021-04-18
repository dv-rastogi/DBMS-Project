from . import conn, cursor
# sizes are automatically updated via triggers
def add_user():
    u = input("Enter USER_ID: ")
    g = input("Enter GROUP_ID: ")
    q = f"""
    INSERT INTO member_of (Id, Group_ID, DateOfJoining) VALUES ({u}, {g}, now())
    """
    try:
        cursor.execute(q)
        conn.commit()
        print("Added user!")
    except Exception as e:
        print("Exception", e)
        return

def remove_user():
    u = input("Enter USER_ID: ")
    g = input("Enter GROUP_ID: ")
    q = f"""
    delete from member_of where group_id={g} and id={u}
    """
    try:
        cursor.execute(q)
        conn.commit()
        print("Removed user!")
    except Exception as e:
        print("Exception", e)
        return