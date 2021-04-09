import requests


url = "https://discord.com/api/v8/applications/791048344956043274/commands"

json = {
    "name": "test",
    "description": "test",
    "options": [
        {
            "name": "user",
            "type": 6,
            "required": True,
        }
    ]
}

# For authorization, you can use either your bot token
headers = {
    "Authorization": "NzkxMDQ4MzQ0OTU2MDQzMjc0.X-JfLg.8hAsWeOGRuMlXY9na8q9GLHs72A"
}

r = requests.post(url, headers=headers, json=json)