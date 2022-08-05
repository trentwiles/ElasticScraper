import requests
import urllib.parse

api_base = "https://search.censys.io/api/v2/hosts/search?q="
search = urllib.parse.quote("services.http.response.status_code: 200 and service.name: ELASTICSEARCH")

if sys.argv[1] == "":
    r = requests.get(api_base + search + "&per_page=50&virtual_hosts=EXCLUDE", headers={"accept": "application/json", "Authorization": "Basic abc"})
else:
    r = requests.get(api_base + search + "&per_page=50&virtual_hosts=EXCLUDE&cursor=" + sys.argv[1], headers={"accept": "application/json", "Authorization": "Basic abc"})

    #print(api_base + search + "&per_page=50&virtual_hosts=EXCLUDE")
api = r.json()

for hits in api["result"]["hits"]:
    main_ip = hits["ip"]
    for service in hits["services"]:
        if service["service_name"] == "ELASTICSEARCH":
            #print("Got a hit for elastic: " + main_ip + ":" + str(service["port"]))
            #print("Sending an HTTP request (unauthenticated) to the port")
            try:
                data = requests.get("http://" + main_ip + ":" + str(service["port"]) + "/_search", headers={"User-agent": "ElasticScraper (+https://github.com/RiversideRocks/ElasticScraper)"}, timeout=10)
                #print(data.text)
                with open(str(main_ip) + ".txt", "a") as yes:
                    # Writing data to a file
                    yes.write(data.text)
            except:
                # oops
                print()

print(api["result"]["links"]["next"]); #returns the next cursor, good for the bash script
# by the end of development, this will only return the "next" cursor
