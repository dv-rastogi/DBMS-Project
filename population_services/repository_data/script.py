import os
from functools import reduce
from random_word import RandomWords
import pandas as pd
import datetime
import random

UNIV_LANG = ["C++",  "C#", "C", "Python", "Java", "JavaScript", "Kotlin"]
UNIV_MAP = {"cpp": "C++", "cs": "C", "c": "C", "py": "Python", "java": "Java", "js": "JavaScript", "kt": "Kotlin"}


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
    req = dict(get_directory_structure(os.getcwd())) # get current working directory
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
        titles = rand.get_random_words(hasDictionaryDef="true", minLength = 5, maxLength = 10)
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

    for idx in dfr.index:
        if len(left) == 0:
            break
        here = random.sample(left, random.randint(1, min(len(left), 5)))
        left = [x for x in left if x not in here] # remove elements
        for selected in here:
            res["ID"].append(dfr["ID"][idx])
            res["Name"].append(dfr["Name"][idx])
            res["Template_Name"].append(dft["Name"][selected])
            res["Template_Language"].append(dft["Language"][selected])
            res["Template_Content"].append(dft["Content"][selected])

    df = pd.DataFrame.from_dict(res)
    print(df.head())
    df.to_csv('../../tables/repo_templates.csv', index=False)


if __name__ == "__main__":
    # form_repository()
    form_repo_templates()