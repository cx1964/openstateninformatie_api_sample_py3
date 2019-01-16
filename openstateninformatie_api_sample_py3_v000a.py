# filenaam:         openstateninformatie_api_sample_py3_v000a.py
# Functie:          Voorbeeld hoe mbv de api van open StatenInformatie of open raadsinformatie
#                   in python3 open data opgevraagd kan worden.
#                   Dit voorbeeld vraagt informatie op over vergaderingen.
#
#                   Voorbeeld api call
#                   
#                   curl -i -XPOST 'http://api.openraadsinformatie.nl/v0/search' -d '{"query": "vergadering", "size": 5}'
#                   zie https://curl.trillworks.com/ 
#                   tbv omzetten van curl naar python request. Roep de url naar trillworks.com aan via chrome browser
#
#                   Zie: http://docs.openraadsinformatie.nl/user/api.html
#
# Ptyhon version:   3.X
#                   
# Achtergrond mbt http request: https://www.tutorialspoint.com/http/http_requests.htm                 
#
# command:          python3 openstateninformatie_api_sample_py3_v000.py

# Tbv om webservices obv een API aan te roepen
import requests
import json


### input ####
aantalRecords = 1  
# serviceurl = 'http://api.openraadsinformatie.nl/v0/search' of 'http://api.openstateninformatie.nl/v0/search'
serviceurl = 'http://api.openstateninformatie.nl/v0/search' 
### input ###


# *** nieuw ***
# specificeer de parameters van de post van het request
payload = {"query": "vergadering", "size": aantalRecords} # de json parameters van de api
print('payload type:',type(payload))
# headers = {'content-type': 'application/json'}
# *** nieuw ***

# debug print("serviceurl: ", serviceurl)

try:
    # response = urlopen(uh)
    response = requests.post(serviceurl, data=json.dumps(payload)) #, headers=headers)
except HTTPError as e:
    # do something
    print('Error code: ', e.code)
except URLError as e:
    # do something
    print('Reason: ', e.reason)
else:
    # do something
    print('good!')

print('Encoding van response:', response.encoding)
print('response.headers.get:', response.headers.get('content-type'))

# Print de response als text 
#print(response.text)

# debug print(response.content) # werkt; dit bevat de inhoud

# Zet response om in een JSON format 
data = response.content
js = json.loads(data)
# debug print(js)
# debug print(json.dumps(js, indent=4)) # hiermee kan men de keys vinden in het bericht   
print(json.dumps(js, indent=4))

# interpreteer de response in JSON format
# nog afmaken !!!!!!!!!!!!!!!!!!!!!!!!!!!
#print ('gelezen events',js['events'][0])
#print ('gelezen events',js['ĺocation'][0])
# lat = js["results"][0]["geometry"]["location"]["lat"]
# lng = js["results"][0]["geometry"]["location"]["lng"]
# print ('lat', lat, 'lng', lng)


