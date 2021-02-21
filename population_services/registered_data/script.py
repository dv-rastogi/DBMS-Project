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


def form_registered():
    res = {"User_ID": [], "Programming_Organisation_ID": [], "DateOfJoining": [],
           "Rating": [], "Handle": []}
    users_read = pd.read_csv('../../tables/users.csv')

    for idx in users_read.index:
        id = users_read["ID"][idx]
        djoin = users_read["DateOfJoining"][idx]
        dLow = datetime.strptime(djoin + ' 1:30 PM', '%Y-%m-%d %I:%M %p')
        dHigh = datetime.strptime('2/1/2021 4:50 AM', '%m/%d/%Y %I:%M %p')
        # print(dLow.date().__str__() +dHigh.date().__str__())
        djoinonorgansation = random_date(dLow, dHigh)
        handle = users_read["User_Name"][idx]
        res["User_ID"].append(id)
        res["DateOfJoining"].append(djoinonorgansation.date().strftime("%Y-%m-%d"))
        res["Handle"].append(handle)
        i=random.randint(0,1)
        if(i):
            res["Programming_Organisation_ID"].append("P-1")
        else:
            res["Programming_Organisation_ID"].append("P-2")
        res["Rating"].append(random.randint(1000,3500))
    # print(res)
    df = pd.DataFrame.from_dict(res)
    print(df.head())
    df.to_csv('../../tables/registered.csv', index=False)

if __name__ == "__main__":
    form_registered()
