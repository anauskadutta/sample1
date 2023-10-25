## This script creates GitHub issues from CodeQL scan alerts

# import os module
import os

# import requests module
import requests

# import json module
import json

token = os.environ['GH_TOKEN']

# assign headers
headers = {
  'Accept': 'application/vnd.github+json',
  'Authorization': "Bearer {}".format(token),
  'X-GitHub-Api-Version': '2022-11-28'
}

## Gets list of body descriptions of existing issues in a repo
github_issue_url = 'https://api.github.com/repos/anauskadutta/sample1/issues'

# get existing github issue details
github_issue_response = requests.get(github_issue_url, headers=headers)
github_issue_json = github_issue_response.json()
codeql_gh_issue_mapping_list = []

for gh_issue in github_issue_json:
  codeql_scan_alert_url = gh_issue['body']
  codeql_gh_issue_mapping_list.append(codeql_scan_alert_url)

## Gets list of existing CodeQL scan alerts in a repo
codeql_scan_url = 'https://api.github.com/repos/anauskadutta/sample1/code-scanning/alerts'

# assign the requests method
codeql_scan_response = requests.get(codeql_scan_url, headers=headers)

if codeql_scan_response.status_code == 200:
  alert_list = codeql_scan_response.json()

  for alert in alert_list:
    if alert['state'] == 'open':
      if alert['html_url'] in codeql_gh_issue_mapping_list:
        print("Issue already exists")
        continue
      else:
        print("Creating GitHub issue...")
        issue_title = alert['most_recent_instance']['message']['text']
        issue_body = alert['html_url']
        data = {
          'title': issue_title,
          'body': issue_body
        }
        post_response = requests.post(github_issue_url,headers=headers,data=data)
        if post_response.status_code == 201:
          print(f"GitHub issue is created: {post_response}")
        else:
          print(f"Status code: {post_response.status_code}")
          print(post_response.json())
    else:
      continue
  
else:
  print(f"Status code: {codeql_scan_response.status_code}")
  print(codeql_scan_response.json())
