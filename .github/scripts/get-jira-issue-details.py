import os
import requests
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
issue_json = issue_details_response.json()
issue_list = issue_json['issues']

for issue in issue_list:
  issue_description = issue.fields
  print(issue_description)
