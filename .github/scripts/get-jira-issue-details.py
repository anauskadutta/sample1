import os
import requests
import json

jira_base_url = os.environ['JIRA_BASE_URL']
jira_username = os.environ['JIRA_USER_EMAIL']
jira_token = os.environ['JIRA_API_TOKEN']

jira_rest_api = '{jira_base_url}/rest/api/3/search'

jira_params = {
  'jql': 'project=STP',
  'issuetype': 'Bug'
}

# Set up headers for the JIRA request
jira_headers = {
    'Content-Type': 'application/json',
}

# Set up authentication for the JIRA request
jira_auth = (jira_username, jira_token)

issue_details_response = requests.get(jira_rest_api, params=jira_params, headers=jira_headers, auth=jira_auth)
issue_json = issue_details_response.json()
issue_list = issue_json['issues']
issue_description_list = []

for issue in issue_list:
  issue_description = issue["fields"]["description"]["content"][0]["content"][0]["text"]
  issue_description_list.append(issue_description)

if "https://github.com/anauskadutta/sample1/security/code-scanning/13" in issue_description_list:
  print("Issue already exists")

else:
  print("New issue")
