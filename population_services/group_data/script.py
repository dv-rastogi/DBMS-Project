import pandas as pd
import random
from random_word import RandomWords
import datetime


def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + datetime.timedelta(seconds=random_second)


# Needs users to be formed
def form_group():

    dfu = pd.read_csv('../../tables/users.csv')
    
    # random select some group admins
    ids = dict(dfu["ID"])
    admins = random.sample(list(ids.keys()), 50)

    res = {
        "ID": [],
        "Group_ID": [],
        "Name": [],
        "DateOfFormation": [],
        "Size": []
    }

    rand = RandomWords()
    gid = 1

    for admin in admins:
        res["ID"].append(dfu["ID"][admin])
        res["Group_ID"].append(gid)
        gid += 1
        res["Name"].append(rand.get_random_word(hasDictionaryDef="true", minLength=5, maxLength=15))
        dLow = datetime.datetime.strptime(dfu['DateOfJoining'][admin] + ' 1:30 PM', '%Y-%m-%d %I:%M %p')
        dHigh = datetime.datetime.strptime('1/1/2021 1:30 PM', '%m/%d/%Y %I:%M %p')
        res["DateOfFormation"].append(random_date(dLow, dHigh).date().strftime("%Y-%m-%d"))
        res["Size"].append(random.randint(1, 20))

    df = pd.DataFrame.from_dict(res)
    print(df.head())
    df.to_csv('../../tables/groups.csv', index=False)

if __name__ == "__main__":
    form_group()