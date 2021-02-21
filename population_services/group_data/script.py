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
        name = rand.get_random_word(hasDictionaryDef="true", minLength=5, maxLength=15)
        while name is None:
            name = rand.get_random_word(hasDictionaryDef="true", minLength=5, maxLength=15)
        res["Name"].append(name)
        dLow = datetime.datetime.strptime(dfu['DateOfJoining'][admin] + ' 1:30 PM', '%Y-%m-%d %I:%M %p')
        dHigh = datetime.datetime.strptime('1/1/2021 1:30 PM', '%m/%d/%Y %I:%M %p')
        res["DateOfFormation"].append(random_date(dLow, dHigh).date().strftime("%Y-%m-%d"))
        res["Size"].append(random.randint(1, 20))

    df = pd.DataFrame.from_dict(res)
    print(df.head())
    df.to_csv('../../tables/groups.csv', index=False)


# Needs groups to be formed
def form_member_of():
    res = {"ID": [], "Group_ID": [], "DateOfJoining": []}
    readgroup = pd.read_csv('../../tables/groups.csv')
    readuser = pd.read_csv('../../tables/users.csv')
    noOfUsers = len((readuser.to_dict())["ID"])

    # To avoid duplicacy
    done = {}
    dHigh = datetime.datetime.strptime('1/1/2021 1:30 PM', '%m/%d/%Y %I:%M %p')
    for i in readgroup.index:
        groupssize = readgroup["Size"][i]

        #admin
        res["ID"].append(readgroup["ID"][i])
        res["Group_ID"].append(readgroup["Group_ID"][i])
        res["DateOfJoining"].append(readgroup["DateOfFormation"][i])
        dateOfCreation = datetime.datetime.strptime(readgroup["DateOfFormation"][i] + ' 1:30 PM', '%Y-%m-%d %I:%M %p')

        for j in range(0, groupssize-1):
            id = random.randint(0, noOfUsers-1)
            x = readuser["ID"][id]          #random user
            y = readgroup["Group_ID"][i]
            z = random_date((dateOfCreation), dHigh).date().strftime("%Y-%m-%d")
            if (x, y) in done:
                continue

            res["ID"].append(x)
            res["Group_ID"].append(y)
            res["DateOfJoining"].append(z)
            done[(x, y)] = True

    df = pd.DataFrame.from_dict(res)
    print(df.head())
    df.to_csv('../../tables/member_of.csv', index=False)


if __name__ == "__main__":
    # form_group()
    form_member_of()