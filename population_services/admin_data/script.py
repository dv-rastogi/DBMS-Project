import pandas as pd
import random


def form_admin():
    res = {
        "Role": ["Technical", "General", "Financial", "Support", "Senior", "Domain", "Signatory", "Advertisement", "HR",
                 "Global", "User"]
        , "Revenue": []
        , "Email": ["Technical@codebook.com",
                    "General@codebook.com",
                    "Financial@codebook.com",
                    "Support@codebook.com",
                    "Senior@codebook.com",
                    "Domain@codebook.com",
                    "Signatory@codebook.com",
                    "Advertisement@codebook.com",
                    "HR@codebook.com",
                    "Global@codebook.com",
                    "User@codebook.com"]}

    for i in range(11):
        res["Revenue"].append(random.randint(2000,10000))
    print(res)
    df = pd.DataFrame.from_dict(res)
    print(df.head())
    df.to_csv('../../tables/admin.csv', index=False)
if __name__ == "__main__":
    form_admin()
