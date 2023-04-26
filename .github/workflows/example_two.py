from datetime import datetime

import requests

url = "https://services.exactearth.com/gws?authkey=acbe735d-efe8-481a-a47e-d2199f91b5e1"

payload = {
    'service': 'WFS',

}

headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

http_response = requests.request("POST", url, headers=headers, data=payload)
resp_json = http_response.json()
print(resp_json)

# future_date = datetime.datetime.now() + datetime.timedelta(days=10)
# exact_earth_response = []
# for feature in resp_json["features"]:
#     try:
#         prop = feature["properties"]
#         ts = datetime.datetime.strptime(prop["ts_pos_utc"], "%Y%m%d%H%M%S")
#         data = {
#             "mmsi": prop["mmsi"],
#             "name": prop["vessel_name"],
#             "imo": prop["imo"],
#             "latitude": prop["latitude"],
#             "longitude": prop["longitude"],
#             "timestamp": ts,
#         }
#
#         exact_earth_response.append(data)
#     except:
#         pass
#
# exact_earth_response.sort(key=lambda d: d["timestamp"])
#
# print("exact_earth_response =", exact_earth_response)
