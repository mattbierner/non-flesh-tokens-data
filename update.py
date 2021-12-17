import requests
import json
import datetime

count = 308
limit = 50

asset_data = []

keys = ['id', 'token_id', 'num_sales', 'image_url', 'image_preview_url', 'image_thumbnail_url', 'name', 'description', 'last_sale', 'top_bid']

for start in range(0, count, limit):
    url = f"https://api.opensea.io/api/v1/assets?order_direction=desc&offset={start}&limit={limit}&collection=non-flesh-tokens"

    response = requests.request("GET", url)

    for asset in response.json()['assets']:
        asset_data.append({ k:v for (k,v) in asset.items() if k in keys })

with open('data.json', 'w') as f:
    f.write(json.dumps({
        'captured': str(int(datetime.datetime.now().timestamp())),
        'assets': asset_data
    }))