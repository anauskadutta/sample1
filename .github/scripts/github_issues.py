# import requests module
import requests

# import json module
import json

# store API url
url = 'https://api.github.com/repos/anauskadutta/sample1/issues'

# assign the headers- not always necessary, but something we have to do with the GitHub API
headers = {'Accept': 'application/vnd.github.v3+json'}

# assign the requests method
r = requests.get(url, headers=headers)

# print a status update for the requests command
print(f"Status code: {r.status_code}")

# store API response to variable
response = r.json()

# # process results
# print(response)

issue_dicts = response['items']

print(f"Total GitHub issues returned: {len(issue_dicts)}")

# for issue in response:
#   print("Title: {issue.title}")
