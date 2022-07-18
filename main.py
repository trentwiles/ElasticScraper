import requests
import urllib.parse

api_base = "https://search.censys.io/api/v2/hosts/search?q="
search = urllib.parse.quote("services.http.response.status_code: 200 and service.name: ELASTICSEARCH")

r = requests.get(api_base + search + "&per_page=50&virtual_hosts=EXCLUDE", headers={"accept": "application/json", "Authorization": "Basic abc"})

#print(api_base + search + "&per_page=50&virtual_hosts=EXCLUDE")
api = r.json()

for hits in api["result"]["hits"]:
    main_ip = hits["ip"]
    for service in hits["services"]:
        if service["service_name"] == "ELASTICSEARCH":
            print("Got a hit for elastic: " + main_ip + ":" + str(service["port"]))
            print("Sending an HTTP request (unauthenticated) to the port")
