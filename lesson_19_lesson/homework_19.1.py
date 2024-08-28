import requests
import json


url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?api_key=cIl7v8Y2Dbvnt3rA9eGKAZUtQPU7wZDKhffdsFD2&sol=1000&camera=fhaz"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload, verify=False, stream=True)

print(response.text)

json_string = json.loads(response.text)
print(json_string)

key_ = 'img_src'

pict_1 = json_string['photos'][0]['img_src']
pict_2 = json_string['photos'][1]['img_src']

list_pict = [pict_1, pict_2]

for i in range(len(list_pict)):
    with open(f'file_{i}.jpg', 'wb') as file:
        file.write(response.content)
        print(list_pict[i])




 # response = requests.get('http://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/01000/opgs/edr/fcam/FLB_486265257EDR_F0481570FHAZ00323M_.JPG', verify=False)
