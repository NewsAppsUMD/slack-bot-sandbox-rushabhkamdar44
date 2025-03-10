import os
import json
import requests

congress_api_key = "N65EPrA5o6ytVv3mtBU2xGYrMzSaxASEtmqEqedR"

url = f"https://api.congress.gov/v3/committee-report/119/hrpt?api_key={congress_api_key}&format=json"

r = requests.get(url)

results = r.json()


print(results['reports'][0]['url'])
