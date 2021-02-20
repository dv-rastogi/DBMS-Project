import requests
import json
import datetime
import random
import pandas as pd

# TODO: Read json and create essential filter for the same

BASE_CF = "https://codeforces.com/api"
UNIV_TAGS = ["graphs", "dp", "binary search", "greedy", "implementation", "data structures", "brute force", "math", "strings", "number theory"]
UNIV_LANG = ["C++",  "C#", "C", "Python", "Java", "JavaScript", "Kotlin"]
USERS_LIM = 300
NAME_LIM = 50


def get_leetcode_data():
	'''
	IMP Need to login first
	Returns json of logged in user
	'''
	uri = "https://leetcode.com/api/problems/algorithms/"
	response = None
	try:
		response = requests.get(uri)
	except requests.ConnectionError:
		print("ConnectionError")
		return
	except Exception:
		print("Exception occured")
		print(response)
		return
	j_response = response.text
	data = json.loads(j_response)
	return data


def get_data_cf(uri):
	'''
	returns json response to specific uri
	'''
	try:
		response = requests.get(uri)
	except Exception as e:
		print("Failed in request")
		print(e)
		exit(1)

	j_response = response.text
	try:
		data = json.loads(j_response)
		if data["status"] != "OK":
			raise Exception("Status != OK")
	except Exception as e:
		print("Failed json load")
		print(e)
		exit(1)
	return data


def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + datetime.timedelta(seconds=random_second)

# saves as users.csv in cwd
def form_cf_users():
	'''
	returns cf users
	'''
	# retrieve standings from a random contest
	uri = "https://codeforces.com/api/contest.standings?contestId=1486&from=1&count=1200"
	rows = get_data_cf(uri)["result"]["rows"]
	t_users = []
	for row in rows:
			if "party" in row:
				t_users.append(row["party"]["members"][0]["handle"])
	handles = random.sample(t_users, USERS_LIM)
	
	# get user info from handle
	def get_cf_info(usernames: str):
		'''
		returns json of cf info of username
		'''
		username_list = ';'.join(usernames)
		uri = BASE_CF + "/user.info?handles=" + username_list
		return get_data_cf(uri)["result"]
	
	res = {
		"ID": [],
		"User_Name": [],
		"First_Name": [],
		"Last_Name": [],
		"Email": [],
		"Organization": [],
		"Location_City": [],
		"Location_Country": [],
		"DateOfBirth": [],
		"DateOfJoining": [],
		"TrustRating": []
	}

	# id
	id_cnt = 1

	# random names (backup ambiguity & Name_Lim)
	f = open("names.txt", "r")
	rand_names = f.read().split('\n')

	# random cities 
	# NOTE: Form recruiter.csv before User
	df = pd.read_csv('../../tables/recruiters.csv')
	locations = list(zip(list(df["Location_City"]), list(df["Location_Country"])))

	# Date of birth
	dLowDOB = datetime.datetime.strptime('1/1/1980 1:30 PM', '%m/%d/%Y %I:%M %p')
	dHighDOB = datetime.datetime.strptime('1/1/2005 1:30 PM', '%m/%d/%Y %I:%M %p')
	
	# Date of joining, low would be from date of birth + randint(yeargap)
	dHighJoin = datetime.datetime.strptime('1/1/2021 1:30 PM', '%m/%d/%Y %I:%M %p')

	# In case of emails, give according to user handle
	extension = ["@gmail.com", "@yahoo.com", "@hotmail.com", "@iiitd.ac.in", "@iitd.ac.in"]

	# get users
	users = get_cf_info(handles)
	
	# In case of org, if None then choose from random
	for user in users:
		handle = user["handle"]
		assert (len(handle) <= NAME_LIM)
		
		# Add ID
		res["ID"].append("U-" + str(id_cnt))
		id_cnt += 1

		# Add User_Name
		res["User_Name"].append(handle)

		# Add First_Name
		gotName = random.choice(rand_names).split(' ')
		if ("firstName" in user) and ("lastName" in user) and (len(user["firstName"]) <= NAME_LIM) and (len(user["lastName"]) <= NAME_LIM):
			gotName[0] = user["firstName"]
			gotName[1] = user["lastName"]
		assert (len(gotName) == 2)
		res["First_Name"].append(gotName[0])
		res["Last_Name"].append(gotName[1])

		# Add Email
		res["Email"].append(handle + random.choice(extension))

		# Add Org., "Google" is random default org
		if ("organization" in user) and (len(user["organization"]) <= NAME_LIM) and (len(user["organization"]) > 0):
			res["Organization"].append(user["organization"])
		elif len(res["Organization"]) != 0:
			res["Organization"].append(random.choice(res["Organization"]))
		else:
			res["Organization"].append("Google")

		# Add location city & country
		random_loc = random.choice(locations)
		res["Location_City"].append(random_loc[0])
		res["Location_Country"].append(random_loc[1])

		# Add DOB
		got_date = random_date(dLowDOB, dHighDOB).date().strftime("%d-%m-%Y")
		res["DateOfBirth"].append(got_date)

		# Add Date of joining
		date_obj_low = datetime.datetime.strptime(got_date, "%d-%m-%Y")
		date_obj_low += datetime.timedelta(days=13*365) # Add 13 years
		res["DateOfJoining"].append(random_date(date_obj_low, dHighJoin).date().strftime("%d-%m-%Y"))

		# Add trust rating, 100 is default
		res["TrustRating"].append(100)
	
	df = pd.DataFrame.from_dict(res)
	print(df.tail())
	df.to_csv("../../tables/users.csv", index=False)


# For modelling entity Problems
def get_cf_problems(tags: list):
	'''
	returns problem set of cf on basis of tags
	'''
	def ratingFilter(rating: int):
		if rating < 1600:
			return "Easy"
		elif rating < 2100:
			return "Medium"
		else:
			return "Hard"

	def get_cf_tag_problems(tag : str):
		'''
		return problems of specific tag
		'''
		uri = BASE_CF + "/problemset.problems?tags=" + tag
		return get_data_cf(uri)["result"]["problems"]

	result = {}
	for tag in UNIV_TAGS:
		problem_set = get_cf_tag_problems(tag)
		for problem in problem_set[:200]:
			if "rating" not in problem:
					continue
			if problem["name"] in result:
				result[problem["name"]]["Tags"].append(tag)
			else:
				dic = dict()
				dic["Name"] = str(problem["name"])
				dic["Tags"] = [tag]
				dic["Difficulty"] = ratingFilter(problem["rating"])
				result[dic["Name"]] = dic
	return result


# For modelling relationship SOLVED
def get_cf_user_status(username: str):
	'''
	return user's submissions from cf
	select problem name (key), language, time of submission
	'''
	uri = BASE_CF + "/user.status?handle=" + username
	submissions = get_data_cf(uri)["result"]
	# print(submissions)

	def okTags(tags: list):
		for tag in tags:
			if tag in UNIV_TAGS:
				return True
		return False

	def convertUnixTime(unixTime: int):
		return str(datetime.datetime.utcfromtimestamp(unixTime).strftime('%Y-%m-%d %H:%M:%S'))
	
	def getLanguage(language: str):
		'''
		Convert submission lang into one of UNIV_LANG & if not found, return random
		'''
		for lang in UNIV_LANG:
			if language.find(lang) != -1:
				return lang
			if lang == "Python":
				if language.find("Pypy") != -1:
					return "Python"
		return random.choice(UNIV_LANG)

	result = {}
	# Extract "OK" verdicts
	for submission in submissions:
		if (submission["verdict"] == "OK"):
			if okTags(submission["problem"]["tags"]):
				dic = dict()
				dic["Name"] =  submission["problem"]["name"]
				dic["Language"] = getLanguage(submission["programmingLanguage"])
				dic["Date"] = convertUnixTime(submission["creationTimeSeconds"])
				result[dic["Name"]] = dic
	return result


if __name__ == "__main__":
    form_cf_users()