import requests
import json


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


if __name__ == "__main__":
    print(get_leetcode_data())