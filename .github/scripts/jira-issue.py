# import os module
import os

# import requests module
import requests

# import json module
import json

token = os.environ['GH_TOKEN']

# store API url
url = 'https://api.github.com/repos/anauskadutta/sample1/code-scanning/alerts'

# assign the headers- not always necessary, but something we have to do with the GitHub API
headers = {'Accept': 'application/vnd.github+json',
          'Authorization': 'Bearer {token}',
          'X-GitHub-Api-Version': '2022-11-28'}

# assign the requests method
r = requests.get(url, headers=headers)

if r.status_code == 200:
  # store API response to variable
  alert_list = r.json()
  
  # process results
  print(alert_list)
  
  print(f"Total CodeQL scan alerts returned: {len(alert_list)}")
  
  # ## iterating through the list of objects of CodeQL scan alerts
  # for alert in alert_list:
  #   if alert['state'] == 'open':
  #     alert_title = alert['most_recent_instance']['message']['text']
  #     alert_body = alert['html_url']
  #     print("Title: " + alert_title)
  #     print("Body: " + alert_body)
  #     # print("Creating Jira issue...")
  #   else:
  #     print("CodeQL scan alert " + alert['html_url'] + " is resolved")
else:
  print(f"Status code: {r.status_code}")
  print(r.json())
