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
          'Authorization': "Bearer {}".format(token),
          'X-GitHub-Api-Version': '2022-11-28'}

# assign the requests method
r = requests.get(url, headers=headers)

def get_json(r):
          if r.status_code == 200:             
                    # store API response to variable
                    alert_list = r.json()
                    json_obj = {}
                    json_obj['reqd_alert_details'] = []
                    
                    ## iterating through the list of objects of CodeQL scan alerts
                    for alert in alert_list:
                              alert_dict = {}
                              if alert['state'] == 'open':
                                        alert_dict['title'] = alert['most_recent_instance']['message']['text']
                                        alert_dict['body'] = alert['html_url']
                                        json_obj['reqd_alert_details'].append(alert_dict)
                              else:
                                        continue

                    json_data = json.dumps(json_obj)
                    # with open("sample.json", "w") as myfile:
                    #   myfile.write(json_data)
          else:
                    print(f"Status code: {r.status_code}")
                    print(r.json())
                    
          return json_data

print(get_json(r))
