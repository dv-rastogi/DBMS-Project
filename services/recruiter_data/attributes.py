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


def get_name_email_loc():
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
        res["ID"].append(id_cnt)
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
        res["DateOfJoining"].append(random_date(dLow, dHigh).date().strftime("%d-%m-%Y")) # Format date here

    assert (len(res["ID"]) == LIM)
    return res


if __name__ == "__main__":
    result = get_name_email_loc()
    df = pd.DataFrame.from_dict(result)
    print(df.head())
    df.to_csv("recruiter.csv", index=False)