import os
from functools import reduce
import pandas as pd

UNIV_LANG = ["C++",  "C#", "C", "Python", "Java", "JavaScript", "Kotlin"]
UNIV_MAP = {"cpp": "C++", "cs": "C", "c": "C", "py": "Python", "java": "Java", "js": "JavaScript", "kt": "Kotlin"}

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

# Generate Template table (Need to add user PK)
if __name__ == "__main__":
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