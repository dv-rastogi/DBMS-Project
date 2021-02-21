import pandas as pd
import requests 
from random_word import RandomWords
import random
import datetime


UNIV_TAGS = ["graphs", "dp", "binary search", "greedy", "implementation", "data structures", "brute force", "math", "strings", "number theory"]


def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + datetime.timedelta(seconds=random_second)


# Form blogs with FK of user
def form_blogs():

	users = pd.read_csv('../../tables/users.csv')
	rand = RandomWords()

	res = {
		"ID": [], 
		"Name": [], 
		"Date": [], 
		"Content": [], 
		"Likes": []
		}

	for i in range(len(users)):
		# get data
		URL = 'https://codeforces.com/api/user.blogEntries?handle=' + users['User_Name'][i]
		r = requests.get(url = URL)
		data = r.json()	
		print(data)

		if (data['status'] == 'OK') and (len(data['result']) > 0):
			for blog in data["result"]:

				# Add ID
				res["ID"].append(users['ID'][i])
				
				# Add blog name
				title = blog['title'][3:-4]
				res["Name"].append(title)

				# Add blog date
				dLow = datetime.datetime.strptime(users['DateOfJoining'][i] + ' 1:30 PM', '%Y-%m-%d %I:%M %p')
				dHigh = datetime.datetime.strptime('1/1/2021 1:30 PM', '%m/%d/%Y %I:%M %p')
				res["Date"].append(random_date(dLow, dHigh).date().strftime("%Y-%m-%d"))

				# Add blog content
				x = None
				while x is None:
					x = rand.get_random_words(hasDictionaryDef="true", minLength = 5, maxLength = 10)
				content = ' '.join(x)
				res["Content"].append(content)

				# Add blog likes
				res["Likes"].append(random.randint(0, 100))
		
	df = pd.DataFrame.from_dict(res)
	print(df.head())
	df.to_csv('../../tables/blogs.csv', index=False)


# form blogs tags, blogs.csv needs to exist
def form_blogs_tags():

	dfb = pd.read_csv('../../tables/blogs.csv')

	res = {
		"ID": [],
		"Name": [],
		"Date": [],
		"Tag": []
	}

	for idx in dfb.index:
		pick = random.sample(UNIV_TAGS, random.randint(1, 5))
		for tag in pick:
			res["ID"].append(dfb["ID"][idx])
			res["Name"].append(dfb["Name"][idx])
			res["Date"].append(dfb["Date"][idx])
			res["Tag"].append(tag)
	
	df = pd.DataFrame.from_dict(res)
	print(df.head())
	df.to_csv('../../tables/blogs_tags.csv')
			

if __name__ == "__main__":		
	form_blogs()
	form_blogs_tags()