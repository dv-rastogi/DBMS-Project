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

def form_premium():
    users_read = pd.read_csv('../../tables/users.csv')
    premium_users=users_read.sample(n=50,replace=False)
    res={"ID":[],"Profile_Visits":[],"Subscription_Time_Start":[],"Subscription_Time_End":[]}
    for idx in premium_users.index:
        # print(premium_users["DateOfJoining"][idx])
        djoin=premium_users["DateOfJoining"][idx]
        dLow = datetime.strptime(djoin+' 1:30 PM', '%d-%m-%Y %I:%M %p')
        dHigh = datetime.strptime('2/18/2022 4:50 AM', '%m/%d/%Y %I:%M %p')
        sub_start_date=random_date(dLow,dHigh)
        sub_end_date=random_date(sub_start_date,dHigh)
        res["ID"].append(premium_users["ID"][idx])
        res["Profile_Visits"].append(random.randint(0,300))
        res["Subscription_Time_Start"].append(sub_start_date.date().strftime("%d-%m-%Y"))
        res["Subscription_Time_End"].append(sub_end_date.date().strftime("%d-%m-%Y"))
    df = pd.DataFrame.from_dict(res)
    print(df.head())
    df.to_csv('../../tables/premium_users.csv', index=False)

if __name__ == "__main__":
    form_premium()