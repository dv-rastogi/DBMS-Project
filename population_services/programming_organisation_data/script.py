import pandas as pd
import random


def form_organisation():
    res = {"ID": ["P-1","P-2"],
           "Revenue Spent": [10000,5000],
           "Name": ["Codeforces","Leetcode"],
           "Email":["Codeforces@gmail.com","Leetcode@gmail.com"]}

    df = pd.DataFrame.from_dict(res)
    print(df.head())
    df.to_csv('../../tables/programming_organisation.csv', index=False)

if __name__ == "__main__":
    form_organisation()