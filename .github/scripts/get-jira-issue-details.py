## This script gets details of GitHub Issues and returns the required json as output

# import requests module
import requests

# import json module
import json

# store API url
url = 'https://jsjiraapp.atlassian.net/rest/api/3/search'

username = os.environ['JIRA_USER_EMAIL']
token = os.environ['JIRA_API_TOKEN']

params = {
  'jql': 'project=STP',
  'issuetype': 'Bug'
}

# Set up headers for the JIRA request
headers = {
    'Content-Type': 'application/json',
}

# Set up authentication for the JIRA request
auth = (username, token)

issue_details_response = requests.get(url, params=params, headers=headers, auth=auth)

print(issue_details_response.status_code)
print(issue_details_response.json())
