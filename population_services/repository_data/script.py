import os
from functools import reduce
from random_word import RandomWords
import pandas as pd
import datetime
import random

UNIV_LANG = ["C++", "C#", "C", "Python", "Java", "JavaScript", "Kotlin"]
UNIV_MAP = {"cpp": "C++", "cs": "C", "c": "C", "py": "Python", "java": "Java", "js": "JavaScript", "kt": "Kotlin"}
UNIV_TAGS = ["graphs", "dp", "binary search", "greedy", "implementation", "data structures", "brute force", "math",
             "strings", "number theory"]


def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + datetime.timedelta(seconds=random_second)


def get_directory_structure(rootdir: str):
    """
    Creates a nested dictionary that represents the folder structure of rootdir
    """
    dir = {}
    rootdir = rootdir.rstrip(os.sep)
    start = rootdir.rfind(os.sep) + 1
    for path, dirs, files in os.walk(rootdir):
        folders = path[start:].split(os.sep)
        subdir = dict.fromkeys(files)
        parent = reduce(dict.get, folders[:-1], dir)
        parent[folders[-1]] = subdir
    return dir


def getLang(lang: str):
    idx = lang.rfind('.')
    if idx == -1:
        return None
    ext = lang[idx + 1:]
    if ext not in UNIV_MAP:
        return None
    return UNIV_MAP[ext]


res = {
    "Name": [],
    "Language": [],
    "Content": []
}


# Forms templates.csv, Generate Template table (Need to add user PK)
def form_template_data():
    req = dict(get_directory_structure(os.getcwd()))  # get current working directory
    req = req[list(req.keys())[0]]["CSES-Solutions"]
    for tag in req.keys():
        for problem in req[tag].keys():
            for solution in req[tag][problem].keys():
                path = "CSES-Solutions/" + tag + "/" + problem + "/" + solution

                # get Name
                problem_name = problem
                if problem_name.find('(') != -1:
                    problem_name = problem[:problem.find('(') - 1]

                # get Lang
                problem_lang = getLang(solution)

                # get Content
                f = open(path, "r")
                problem_content = f.read()

                if problem_lang is None:
                    continue

                res["Name"].append(problem_name)
                res["Language"].append(problem_lang)
                res["Content"].append(problem_content)
    df = pd.DataFrame.from_dict(res)
    print(df.head())
    df.to_csv("templates.csv", index=False)


# Forms repository.csv needs users.csv
def form_repository():
    rand = RandomWords()
    dfu = pd.read_csv('../../tables/users.csv')

    dHigh = datetime.datetime.strptime('1/1/2021 1:30 PM', '%m/%d/%Y %I:%M %p')

    res = {
        "ID": [],
        "Name": [],
        "Date": []
    }
    for idx in dfu.index:
        print("Forming", dfu["ID"][idx])
        titles = rand.get_random_words(hasDictionaryDef="true", minLength=5, maxLength=10)
        if titles is None:
            continue
        for name in titles[:random.randint(1, 4)]:
            res["ID"].append(dfu["ID"][idx])
            res["Name"].append(name)
            dLow = datetime.datetime.strptime(dfu['DateOfJoining'][idx] + ' 1:30 PM', '%Y-%m-%d %I:%M %p')
            res["Date"].append(random_date(dLow, dHigh).date().strftime("%Y-%m-%d"))

    df = pd.DataFrame.from_dict(res)
    print(df.head())
    df.to_csv("../../tables/repository.csv", index=False)


# Needs repository.csv to exist
def form_repo_templates():
    rand = RandomWords()
    dfr = pd.read_csv('../../tables/repository.csv')
    dft = pd.read_csv('templates.csv')
    left = list(range(0, len(dft.index)))

    res = {
        "ID": [],
        "Name": [],
        "Template_Name": [],
        "Template_Language": [],
        "Template_Content": []
    }

    # to avoid duplicacy
    done = {}
    for idx in dfr.index:
        print("Formed", idx)
        if len(left) == 0:
            break
        here = random.sample(left, random.randint(1, min(len(left), 5)))
        left = [x for x in left if x not in here]  # remove elements
        for selected in here:
            w = dfr["ID"][idx]
            x = dfr["Name"][idx]
            y = dft["Name"][selected]
            z = dft["Language"][selected]
            if (w, x, y, z) in done:
                continue
            res["ID"].append(w)
            res["Name"].append(x)
            res["Template_Name"].append(y)
            res["Template_Language"].append(z)
            done[(w, x, y, z)] = True
            a = None
            while a is None:
                a = rand.get_random_words(hasDictionaryDef="true", minLength=5, maxLength=10)
            content = ' '.join(a)
            res["Template_Content"].append(content)

    df = pd.DataFrame.from_dict(res)
    print(df.head())
    df.to_csv('../../tables/repo_templates.csv', index=False)


# Form favourites needs repository.csv & problems.csv
def form_favourites():
    readrep = pd.read_csv('../../tables/repository.csv')
    readprob = pd.read_csv('../../tables/problems.csv')
    length = len((readprob.to_dict())["Problem_ID"])

    res = {
        "Users_ID": [],
        "Name": [],
        "Problem_ID": []
    }

    # To avoid duplicacy
    done = {}

    for i in readrep.index:
        prob = random.randint(2, 6)
        for j in range(1, prob + 1):
            id = random.randint(0, length - 1)
            x = readrep["ID"][i]
            y = readrep["Name"][i]
            z = readprob["Problem_ID"][id]

            if (x, y, z) in done:
                continue

            res["Users_ID"].append(x)
            res["Name"].append(y)
            res["Problem_ID"].append(z)
            done[(x, y, z)] = True

    df = pd.DataFrame.from_dict(res)
    print(df.head())
    df.to_csv('../../tables/favourites.csv', index=False)


# Form todolist needs repository.csv & problems.csv
def form_todo():
    readrep = pd.read_csv('../../tables/repository.csv')
    readprob = pd.read_csv('../../tables/problems.csv')
    length = len((readprob.to_dict())["Problem_ID"])

    res = {
        "Users_ID": [],
        "Name": [],
        "Problem_ID": []
    }

    # To avoid duplicacy
    done = {}

    for i in readrep.index:
        prob = random.randint(2, 6)
        for j in range(1, prob + 1):
            id = random.randint(0, length - 1)
            x = readrep["ID"][i]
            y = readrep["Name"][i]
            z = readprob["Problem_ID"][id]

            if (x, y, z) in done:
                continue

            res["Users_ID"].append(x)
            res["Name"].append(y)
            res["Problem_ID"].append(z)
            done[(x, y, z)] = True

    df = pd.DataFrame.from_dict(res)
    print(df.head())
    df.to_csv('../../tables/todolist.csv', index=False)


# Needs repository.csv
def form_repo_tags():
    readrep = pd.read_csv('../../tables/repository.csv')

    res = {
        "User_ID": [],
        "Name": [],
        "Tag": []
    }

    # To avoid duplicacy
    done = {}
    for i in readrep.index:
        numofTags = random.randint(1, 5)
        for j in range(0, numofTags):
            id = random.randint(0, len(UNIV_TAGS) - 1)
            x = readrep["ID"][i]
            y = readrep["Name"][i]
            z = UNIV_TAGS[id]
            if (x, y, z) in done:
                continue

            res["User_ID"].append(x)
            res["Name"].append(y)
            res["Tag"].append(z)
            done[(x, y, z)] = True

    df = pd.DataFrame.from_dict(res)
    print(df.head())
    df.to_csv('../../tables/repo_tags.csv', index=False)


if __name__ == "__main__":
    # form_repository()
    form_repo_templates()
    # form_favourites()
    # form_todo()
    # form_repo_tags()
