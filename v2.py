import requests
import urllib.parse

api_base = "https://search.censys.io/api/v2/hosts/search?q="
search = urllib.parse.quote("services.http.response.status_code: 200 and service.name: ELASTICSEARCH")

cur = "abc" # could be anything

while true:
    if cur !== "abc"
        r = requests.get(api_base + search + "&per_page=50&virtual_hosts=EXCLUDE&cursor=" + sys.argv[1], headers={"accept": "application/json", "Authorization": "Basic abc"})
    else:
        r = requests.get(api_base + search + "&per_page=50&virtual_hosts=EXCLUDE", headers={"accept": "application/json", "Authorization": "Basic abc"})

    api = r.json()

    for hits in api["result"]["hits"]:
        main_ip = hits["ip"]
        for service in hits["services"]:
            if service["service_name"] == "ELASTICSEARCH":
                try:
                    data = requests.get("http://" + main_ip + ":" + str(service["port"]) + "/_search", headers={"User-agent": "ElasticScraper (+https://github.com/RiversideRocks/ElasticScraper)"}, timeout=10)
                    with open(str(main_ip) + ".txt", "a") as yes:
                        # Writing data to a file
                        yes.write(data.text)
                        try:
                            cur = api["result"]["links"]["next"]
                        except:
                            print("Ended!")
                            sys.exit()
                except:
                    # oops
                    print()