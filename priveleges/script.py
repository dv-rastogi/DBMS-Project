### Assumptions 
#       1. mysql and mysql connector for python are installed on the system
#       2. conf stores correct usernames and password

from mysql.connector import connect
from time import sleep
from dotenv import load_dotenv
import random, os

load_dotenv()

conf = {
    'host': os.getenv('MYSQL_HOST') or 'localhost',
    'user': os.getenv('MYSQL_USER') or '',
    'password': os.getenv('MYSQL_PASSWORD') or 'password'
}
db_name = 'cp-stats'

users = {

    'user_codebook': {

    },
    
    'admin_codebook': {
        "SELECT": ["*"],
        "INSERT": [],
        "UPDATE": [],
        "DELETE": []
    },

    'recruiter_codebook': {

    },
    
    'organisation_codebook': {

    },
    
    'group_leader_codebook': {

    }
}

def setup(cu, db):
    
    # Dropping users
    for user in users:
        q = f"DROP USER IF EXISTS '{user}'@'localhost';"        
        try: 
            print(f"Done deletion with {user}")
            cu.execute(q)
            db.commit()
            
        except Exception:
            print(f'Continuing...')
            break


db = connect(**conf)
cu = db.cursor()

setup(cu, db)

def flush_pri():
    print("\n>> 🏃‍♀️ Flushing Privileges\n")
    try:
        cu.execute('FLUSH PRIVILEGES;')
        db.commit()
    except:
        print("Could not flush pri")


# MySQL Users
print("\n>> 🏃‍♀️ Creating MySQL Users\n")
for user in users:    
    q = f"""
        CREATE USER '{user}'@'localhost' IDENTIFIED BY '{user}';
    """
    # print(q)
    try:
        cu.execute(q)
        db.commit()
    except Exception as e:
        print(f'Continuing...')
        break
    print(f"Done creation with {user}")       

# MySQL Permissions
flush_pri()
print("\n>> 🏃‍♀️ Granting Permissions to MySQL Users\n")
for user in users:    
    for grant in users[user]:
        for table in users[user][grant]:        
            q = f"""
                GRANT {grant} ON {db_name}.{table} TO '{user}'@'localhost';
            """
            # print(q)
            try:
                cu.execute(q)
                db.commit()
            except Exception as e:
                print(f'Continuing...')
                break
            
            print(f"Done {grant} with {table} for {user}")       

flush_pri()

cu.close()