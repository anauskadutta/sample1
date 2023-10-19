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

def get_github_issue_json(r):
  if r.status_code == 200:
    issue_list = r.json()
    json_obj = {}
    json_obj['reqd_issue_details'] = []

    for issue in issue_list:
      issue_obj = {}
      if issue['state'] == 'open':
        issue_obj['title'] = issue['title']
        issue_obj['url'] = issue['html_url']
        json_obj['reqd_issue_details'].append(issue_obj)
      else:
        continue
    
    reqd_json_data = json.dumps(json_obj)
  else:
    print(f"Status code: {r.status_code}")
    print(r.json())

  return reqd_json_data

print(get_github_issue_json(r))
