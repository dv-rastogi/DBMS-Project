import random
import pandas as pd
from datetime import timedelta
from datetime import datetime

# Number of rows
LIM = 150


def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + timedelta(seconds=random_second)


def get_rand_locations():
    '''
    returns city and country zipped
    '''
    init_data = pd.read_csv("worldcities.csv")
    data = init_data.sample(n = LIM, replace = "False")
    result = list(zip(list(data["city_ascii"]), list(data["country"])))
    return result


def form_name_email_loc():
    '''
    returns first_name, last_name & email zipped
    '''  

    res = {
        "ID": [], 
        "First_Name": [], 
        "Last_Name": [], 
        "Email": [], 
        "Location_City": [], 
        "Location_Country": [], 
        "DateOfJoining": []
        }

    # Names
    f = open("names.txt", "r")
    names = f.read().split('\n')
    
    # Emails
    emails = {}
    extension = ["@gmail.com", "@yahoo.com", "@hotmail.com", "@iiitd.ac.in", "@iitd.ac.in"]

    # Dates
    dLow = datetime.strptime('1/1/2018 1:30 PM', '%m/%d/%Y %I:%M %p')
    dHigh = datetime.strptime('2/18/2021 4:50 AM', '%m/%d/%Y %I:%M %p')

    # Locations
    loc = get_rand_locations()
    
    # ID
    id_cnt = 1

    for name in names:
        temp = {}
        
        # Add ID
        res["ID"].append("R-" + str(id_cnt))
        id_cnt += 1

        # Add Names
        name_split = name.split(' ')
        res["First_Name"].append(name_split[0])
        res["Last_Name"].append(name_split[1])

        # Add Email
        ext = random.choice(extension)
        email = name_split[0] + "_" + name_split[1] + ext
        if email in emails:
            off = 1
            temp_email = name_split[0] + "_" + name_split[1] + str(off) + ext
            while temp_email in emails:
                off += 1
                temp_email = name_split[0] + "_" + name_split[1] + str(off) + ext
            email = temp_email
        emails[email] = True
        res["Email"].append(email)

        # Add Location
        location = loc.pop()
        res["Location_City"].append(location[0])
        res["Location_Country"].append(location[1])

        # Add date
        res["DateOfJoining"].append(random_date(dLow, dHigh).date().strftime("%Y-%m-%d")) # Format date here

    assert (len(res["ID"]) == LIM)
    df = pd.DataFrame.from_dict(res)
    print(df.head())
    df.to_csv("../../tables/recruiters.csv", index=False)

# First form recruiters.csv & users.csv
def form_recruiter_preferred():
    '''
    forms preferred relationship, only if user has joined after recruiter
    '''
    dfr = pd.read_csv('../../tables/recruiters.csv')
    dfu = pd.read_csv('../../tables/users.csv')

    dr = dict(dfr)
    du = dict(dfu)
    
    drID = dict(dr["ID"])
    drDate = dict(dr["DateOfJoining"])
    res = {"Recruiter_ID": [], "User_ID": []}
    for recruiter in drID:
        date_r = datetime.strptime(drDate[recruiter], "%Y-%m-%d")
        collected = []
        duDate = dict(du["DateOfJoining"])
        duID = dict(du["ID"])
        for idx in duDate:
            date_u = datetime.strptime(duDate[idx], "%Y-%m-%d")
            if date_u > date_r:
                collected.append(duID[idx])
        
        sz_prefer = random.randint(0, min(len(collected), 5))
        prefer = random.sample(collected, sz_prefer)
        for x in prefer:  
            res["Recruiter_ID"].append(drID[recruiter])
            res["User_ID"].append(x)

    df = pd.DataFrame.from_dict(res)
    print(df.head())
    df.to_csv('../../tables/preferred.csv', index=False)


# First form recruiters.csv & users.csv & preferred.csv
def form_recruiter_recruited():
    '''
    forms preferred relationship, only if user has joined after recruiter
    '''
    dfr = pd.read_csv('../../tables/recruiters.csv')
    dfu = pd.read_csv('../../tables/users.csv')
    dfp = pd.read_csv('../../tables/preferred.csv')

    preferred = dict()
    for idx in dfp.index:
        if dfp["Recruiter_ID"][idx] in preferred:
            preferred[dfp["Recruiter_ID"][idx]].append(dfp["User_ID"][idx]) 
        else:
            preferred[dfp["Recruiter_ID"][idx]] = [dfp["User_ID"][idx]]

    dr = dict(dfr)
    du = dict(dfu)
    
    drID = dict(dr["ID"])
    drDate = dict(dr["DateOfJoining"])
    res = {"Recruiter_ID": [], "User_ID": [], "DateOfRecruitment": []}

    dHigh = datetime.strptime('1/1/2021 1:30 PM', '%m/%d/%Y %I:%M %p')

    for recruiter in drID:
        date_r = datetime.strptime(drDate[recruiter], "%Y-%m-%d")
        collected = []
        duDate = dict(du["DateOfJoining"])
        duID = dict(du["ID"])
        for idx in duDate:
            date_u = datetime.strptime(duDate[idx], "%Y-%m-%d")
            if date_u > date_r:
                collected.append((duID[idx], date_u))
        
        sz_recruit = random.randint(0, min(len(collected), 10))
        recruit = random.sample(collected, sz_recruit)
        for x in recruit:
            if (drID[recruiter] in preferred) and (x[0] in preferred[drID[recruiter]]):
                continue  
            res["Recruiter_ID"].append(drID[recruiter])
            res["User_ID"].append(x[0])
            res["DateOfRecruitment"].append(random_date(x[1], dHigh).date().strftime("%Y-%m-%d"))

    df = pd.DataFrame.from_dict(res)
    print(df.head())
    df.to_csv('../../tables/recruited.csv', index=False)


if __name__ == "__main__":
    # form_name_email_loc()
    # form_recruiter_preferred()   
    form_recruiter_recruited()   