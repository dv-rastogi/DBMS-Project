import pandas as pd
import random
from datetime import timedelta
from datetime import datetime


def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + timedelta(seconds=random_second)


def form_block():
    res = {"User_ID": [], "Admin_Role": [], "Date_Unblock": []}

    users_read = pd.read_csv('../../tables/users.csv')
    blocked_users = users_read.sample(n=20, replace=False)
    l = ["Technical", "General", "Financial", "Support", "Senior", "Domain", "Signatory", "Advertisement", "HR",
         "Global", "User"]
    for idx in blocked_users.index:
        res["User_ID"].append(users_read["ID"][idx])
        res["Admin_Role"].append(l[random.randint(0,10)])
        dLow = datetime.strptime('2021-2-1 1:30 PM', '%Y-%m-%d %I:%M %p')
        dHigh = datetime.strptime('1/2/2022 4:50 AM', '%m/%d/%Y %I:%M %p')
        res["Date_Unblock"].append(random_date(dLow,dHigh).date().strftime("%Y-%m-%d"))
    df = pd.DataFrame.from_dict(res)
    print(df.head())
    df.to_csv('../../tables/blocks.csv', index=False)
if __name__ == "__main__":
    form_block()
