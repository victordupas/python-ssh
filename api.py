import requests
url_api = 'https://api.midway.tomtom.com/ranking/liveHourly/USA_los-angeles'
usa_req = requests.get(url_api)
usa_json = usa_req.json()

print(usa_json)


