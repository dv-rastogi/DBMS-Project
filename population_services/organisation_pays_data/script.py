import pandas as pd
import random
from datetime import timedelta
from datetime import datetime
from random_word import RandomWords
def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + timedelta(seconds=random_second)


def form_organisation_pays():
    rand = RandomWords()
    res={"Organization_ID":[],"Admin_Role":[],"DateOfPayment":[],"AmountPaid":[],"Ads":[]}
    l = ["Technical", "General", "Financial", "Support", "Senior", "Domain", "Premium", "Advertisement", "HR",
         "Global", "User", "Organisation"]
    for i in range (10):
        if(i%2):
            res["Organization_ID"].append("P-1")
        else:
            res["Organization_ID"].append("P-2")
        res["Admin_Role"].append(l[random.randint(0, len(l)-1)])
        dLow = datetime.strptime('2020-2-1 1:30 PM', '%Y-%m-%d %I:%M %p')
        dHigh = datetime.strptime('1/2/2021 4:50 AM', '%m/%d/%Y %I:%M %p')
        res["DateOfPayment"].append(random_date(dLow, dHigh).date().strftime("%Y-%m-%d"))
        res["AmountPaid"].append(random.randint(3000, 10000))
        x = None
        while x is None:
            x = rand.get_random_words(hasDictionaryDef="true", minLength=5, maxLength=10)
        content = ' '.join(x)
        res["Ads"].append(content)
    df = pd.DataFrame.from_dict(res)
    print(df.head())
    df.to_csv('../../tables/organisation_paysto.csv', index=False)

if __name__ == "__main__":
    form_organisation_pays()