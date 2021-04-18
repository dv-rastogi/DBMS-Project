### Assumptions 
#       1. mysql and mysql connector for python are installed on the system
#       2. conf stores correct usernames and password

from mysql.connector import connect
from time import sleep
from dotenv import load_dotenv
import random, os

load_dotenv()

db_name = 'cp-stats'
conf = {
    'host': os.getenv('MYSQL_HOST') or 'localhost',
    'user': os.getenv('MYSQL_USER') or '',
    'password': os.getenv('MYSQL_PASSWORD') or 'password',
    'database': db_name
}


# NEED TO ADD VIEWS BEFORE THE SCRIPT (views.sql)

users = {

    'user_codebook': {
        "SELECT": ["users", "problems", "problems_tags", "solved", "repository", "repo_templates", "repository", "repo_tags", "blogs", "blogs_tags", "contests", "contest_tags", "member_of", "`groups`", "recruited", "recruiters", "registered", "todolist", "user_languages", "favourites", "admin"],
        "INSERT": ["solved", "repository", "repo_templates", "repo_tags", "blogs", "blogs_tags", "`groups`", "registered", "todolist", "user_languages", "favourites"],
        "UPDATE": ["users", "repository", "repo_templates", "repo_tags", "blogs", "blogs_tags", "registered", "user_languages"],
        "DELETE": ["repository", "repo_templates", "repo_tags", "blogs", "blogs_tags", "member_of", "registered", "todolist", "user_languages", "favourites"]
    },

    'premium_user_codebook': {
        "SELECT": ["premium_users", "premium_users_paysto", "preferred"],
        "INSERT": ["premium_users", "premium_users_paysto"],
        "UPDATE": ["premium_users"],
        "DELETE": ["premium_users", "premium_users_paysto"]
    },
    
    'admin_codebook': {
        "SELECT": ["*"],
        "INSERT": ["*"],
        "UPDATE": ["*"],
        "DELETE": ["*"],
        "CREATE VIEW": ["*"],
        "SHOW VIEW": ["*"]
    },

    'recruiter_codebook': {
        "SELECT": ["recruiters", "users", "user_languages", "preferred", "recruited", "problems", "solved", "problems_tags", "repository", "repo_templates", "repository", "repo_tags", "blogs", "blogs_tags", "member_of", "`groups`", "admin", "registered"],
        "INSERT": ["recruited", "preferred"],
        "UPDATE": ["recruited", "preferred", "recruiters"],
        "DELETE": ["recruited", "preferred"]
    },
    
    'organisation_codebook': {
        "SELECT": ["users", "contests", "contest_tags", "registered", "organisation_paysto", "admin", "problems", "problems_tags"],
        "INSERT": ["contests", "contest_tags", "registered", "organisation_paysto", "problems", "problems_tags"],
        "UPDATE": ["contests", "contest_tags", "registered", "problems", "problems_tags"],
        "DELETE": ["contests", "contest_tags", "registered", "problems", "problems_tags"]
    },
    
    'group_leader_codebook': {
        "SELECT": [],
        "INSERT": ["member_of"],
        "UPDATE": ["`groups`"],
        "DELETE": ["`groups`"]
    }
}

## Add extra users priveleges
for privelege in users['user_codebook']:
    users['premium_user_codebook'][privelege] += users['user_codebook'][privelege] 
    users['group_leader_codebook'][privelege] += users['user_codebook'][privelege] 


## Views priveleges
views = {
    'user_codebook': ["USER_STRENGTH", "FOLLOWERS", "PROBLEM_SOLVED_COUNT", "UPCOMING_CONTESTS"],
    'premium_user_codebook': ["NUM_FOLLOWERS", "PREMIUM_AMOUNT_PAID"],
    'group_leader_codebook': [],
    'admin_codebook': ["*"],
    'organisation_codebook': ["INCREASE_IN_REGISTERED"],
    'recruiter_codebook': ["USER_STRENGTH", "FOLLOWERS"]
}

views['premium_user_codebook'] += views['user_codebook']
views['group_leader_codebook'] += views['user_codebook']

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
                GRANT {grant} ON `{db_name}`.{table} TO '{user}'@'localhost';
            """
            # print(q)
            try:
                cu.execute(q)
                db.commit()
            except Exception as e:
                print(q)
                print("Exception", e)
                print(f'Continuing...')
                break
            
            print(f"Done {grant} with {table} for {user}")       

    for view in views:
        q = f"""
            GRANT SELECT ON `{db_name}`.{table} TO '{user}'@'localhost';
        """
        # print(q)
        try:
            cu.execute(q)
            db.commit()
        except Exception as e:
            print(q)
            print("Exception", e)
            print(f'Continuing...')
            break
        
        print(f"Done SELECT with view {table} for {user}")


flush_pri()

cu.close()
print("SEE YA!")