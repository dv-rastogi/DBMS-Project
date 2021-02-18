import requests
import json


BASE_CF = "https://codeforces.com/api"


def get_data_cf(uri):
	'''
	returns json response to specific uri
	'''
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


def get_cf_info(username: str):
	'''
	returns json of cf info of username
	'''
	uri = BASE_CF + "/user.info?handles=" + username + ";"
	return get_data_cf(uri)


def get_cf_problems(tags: list):
	'''
	returns problem set of cf on basis of tags
	'''
	tag_str = ';'.join(tags)
	uri = BASE_CF + "/problemset.problems?tags=" + tag_str
	return get_data_cf(uri)


def get_cf_user_status(username: str):
	'''
	return user's submissions from cf
	'''
	uri = BASE_CF + "user.status?handle=" + username
	return get_data_cf(uri)


if __name__ == "__main__":
    print(get_cf_problems(["dp", "binary search"]))