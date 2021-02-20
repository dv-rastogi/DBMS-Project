import pandas as pd
import random


def form_following():
    # Pairs of users
    pair = {}
    #reading the users.csv file
    users_read = pd.read_csv('../../tables/users.csv')
    users_read = dict(users_read)
    res = {"User_ID": [], "Following_ID": []}
    users_ids_dict = dict(users_read["ID"])
    user_ids_list = list(users_ids_dict.values())
    for i in range(300):
        id1 = random.choice(user_ids_list)
        id2 = random.choice(user_ids_list)
        while id2 == id1:
            id2 = random.choice(user_ids_list)
        while (id1, id2) in pair:
            id1 = random.choice(user_ids_list)
            id2 = random.choice(user_ids_list)
            while id2 == id1:
                id2 = random.choice(user_ids_list)
        pair[(id1,id2)]=True
        res["User_ID"].append(id1)
        res["Following_ID"].append(id2)
    df = pd.DataFrame.from_dict(res)
    print(df.head())
    df.to_csv('../../tables/following.csv', index=False)
if __name__ == "__main__":
    form_following()
