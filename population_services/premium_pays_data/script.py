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

def form_premium_pays():
    res={"Premium_User_ID":[],"Admin_Role":[],"DateOfPayment":[],"AmountPaid":[]}
    premium_users_read = pd.read_csv('../../tables/premium_users.csv')
    l=["Technical", "General", "Financial", "Support", "Senior", "Domain", "Premium", "Advertisement", "HR",
                 "Global", "User","Organisation"]
    for idx in premium_users_read.index:
        res["Premium_User_ID"].append(premium_users_read["ID"][idx])
        res["Admin_Role"].append(l[random.randint(0, len(l)-1)])
        dLow = datetime.strptime('2020-2-1 1:30 PM', '%Y-%m-%d %I:%M %p')
        dHigh = datetime.strptime('1/2/2021 4:50 AM', '%m/%d/%Y %I:%M %p')
        res["DateOfPayment"].append(random_date(dLow,dHigh).date().strftime("%Y-%m-%d"))
        res["AmountPaid"].append(random.randint(1000,2500))
    df = pd.DataFrame.from_dict(res)
    print(df.head())
    df.to_csv('../../tables/premium_users_paysto.csv', index=False)









if __name__ == "__main__":
    form_premium_pays()