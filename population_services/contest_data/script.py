import pandas as pd
import requests
from random_word import RandomWords
import random
import datetime
UNIV_TAGS = ["graphs", "dp", "binary search", "greedy", "implementation", "data structures", "brute force", "math","strings", "number theory"]

def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + datetime.timedelta(seconds=random_second)

def form_contest_tags():
    readcontest = pd.read_csv('../../tables/contests.csv')

    res = {
        "ID": [],
        "Name": [],
        "Tag": [],
        "Date":[]
    }
    done = {}
    for i in readcontest.index:
        numofTags = random.randint(0, 5)
        if(numofTags==0):
            continue
        for j in range(0, numofTags):
            id = random.randint(0, len(UNIV_TAGS) - 1)
            x = readcontest["ID"][i]
            y = readcontest["Name"][i]
            z = UNIV_TAGS[id]
            k=readcontest["Date"][i]
            if (x, y, z, k) in done:
                continue

            res["ID"].append(x)
            res["Name"].append(y)
            res["Tag"].append(z)
            res["Date"].append(k)
            done[(x, y, z, k)] = True
    # print(res)
    df = pd.DataFrame.from_dict(res)
    print(df.head())
    df.to_csv('../../tables/contest_tags.csv', index=False)

def form_contests():
    rand = RandomWords()
    res = {
        "ID": [],
        "Name": [],
        "Date": [],
        "Content": [],
        "Likes": [], "DateOfContest": []
    }
    l = ["Codeforces Round ", "Leetcode Weekly Contest ", "Leetcode Biweekly Contest "]
    for i in range(20):
        j = random.randint(0, 2)
        if j:
            res["ID"].append("P-2")
        else:
            res["ID"].append("P-1")
        res["Name"].append(l[j] + str(random.randint(400, 700)))
        dLow = datetime.datetime.strptime('2016-12-01 1:30 PM', '%Y-%m-%d %I:%M %p')
        dHigh = datetime.datetime.strptime('1/1/2021 1:30 PM', '%m/%d/%Y %I:%M %p')
        date = random_date(dLow, dHigh)
        res["Date"].append(date.date().strftime("%Y-%m-%d"))
        dHigh = datetime.datetime.strptime('1/2/2021 1:30 PM', '%m/%d/%Y %I:%M %p')
        dc = random_date(date, dHigh)
        res["DateOfContest"].append(dc.date().strftime("%Y-%m-%d"))
        x = None
        while x is None:
            x = rand.get_random_words(hasDictionaryDef="true", minLength=5, maxLength=10)
        content = ' '.join(x)
        res["Content"].append(content)
        res["Likes"].append(random.randint(0, 100))
    print(res)
    df = pd.DataFrame.from_dict(res)
    # print(df.head())
    # df.to_csv('../../tables/contests.csv', index=False)




if __name__ == "__main__":
    form_contest_tags()
