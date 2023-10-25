# import os module
import os

# import requests module
import requests

# import json module
import json

token = os.environ['GH_TOKEN']

jira_username = os.environ['JIRA_USER_EMAIL']
jira_token = os.environ['JIRA_API_TOKEN']

jira_url = 'https://jsjiraapp.atlassian.net/rest/api/3/search'

jira_params = {
  'jql': 'project=STP',
  'issuetype': 'Bug'
}

jira_headers = {
    'Content-Type': 'application/json',
}

jira_auth = (jira_username, jira_token)

issue_details_response = requests.get(jira_url, params=jira_params, headers=jira_headers, auth=jira_auth)
issue_json = issue_details_response.json()
issue_list = issue_json['issues']
# issue_description_list = []
issue_codeql_list = []

for issue in issue_list:
  mapped_codeql_id = issue["fields"]["customfield_10043"]
  issue_codeql_list.append(mapped_codeql_id)
  # issue_description = issue["fields"]["description"]["content"][0]["content"][0]["text"]
  # issue_description_list.append(issue_description)

# store API url
url = 'https://api.github.com/repos/anauskadutta/sample1/code-scanning/alerts'

# assign the headers- not always necessary, but something we have to do with the GitHub API
headers = {'Accept': 'application/vnd.github+json',
          'Authorization': "Bearer {}".format(token),
          'X-GitHub-Api-Version': '2022-11-28'}

# assign the requests method
r = requests.get(url, headers=headers)

def get_json(r):
  if r.status_code == 200:             
    # store API response to variable
    alert_list = r.json()
    json_obj = {}
    json_obj['details'] = []
    
    ## iterating through the list of objects of CodeQL scan alerts
    for alert in alert_list:
      alert_dict = {}
      if alert['state'] == 'open':
        alert_dict['id'] = alert['number']
        alert_dict['name'] = alert['most_recent_instance']['message']['text']
        alert_dict['url'] = alert['html_url']
        if alert_dict['id'] in issue_codeql_list:
          continue
        else:
          json_obj['details'].append(alert_dict)
      else:
        continue

    if json_obj['details'] == []:
      json_obj = {}
    
    json_data = json.dumps(json_obj)

  else:
    print(f"Status code: {r.status_code}")
    print(r.json())
            
  return json_data

print(get_json(r))
