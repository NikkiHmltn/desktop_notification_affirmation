from plyer import notification
import requests 
import json


#affirmations api
API_URL = requests.get("https://www.affirmations.dev/")
data = API_URL.text
parse_json = json.loads(data)
affirmation = parse_json['affirmation']

title = "Daily Affirmation"
message = affirmation

notification.notify(title = title, 
                    message = message,
                    app_icon = None,
                    timeout=10,
                    toast=False)