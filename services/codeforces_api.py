import requests
import json
import datetime
import random

# TODO: Read json and create essential filter for the same

BASE_CF = "https://codeforces.com/api"
UNIV_TAGS = ["graphs", "dp", "binary search", "greedy", "implementation", "data structures", "brute force", "math", "strings", "number theory"]
UNIV_LANG = ["C++",  "C#", "C", "Python", "Java", "JavaScript", "Kotlin"]


def get_data_cf(uri):
	'''
	returns json response to specific uri
	'''
	try:
		response = requests.get(uri)
	except Exception as e:
		print("Failed in request")
		print(e)
		return

	j_response = response.text
	try:
		data = json.loads(j_response)
		if data["status"] != "OK":
			raise Exception("Status != OK")
	except Exception as e:
		print("Failed json load")
		print(e)
	
	return data


def get_cf_info(username: str):
	'''
	returns json of cf info of username
	'''
	uri = BASE_CF + "/user.info?handles=" + username + ";"
	return get_data_cf(uri)


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
    print(str(get_cf_problems(UNIV_TAGS)))