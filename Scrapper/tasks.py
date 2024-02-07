
from celery import shared_task
import requests
from .models import Proxy,CountriesOnline
import celery

app = celery.Celery('Proxy_scrape')


@shared_task
def start_scraping():

    headers = {
        'Referer': 'https://geonode.com/'
    }
    data = requests.get('https://proxylist.geonode.com/api/proxy-summary', headers=headers).json()
    total_proxies = data['summary']['proxiesOnline']
    countries_online = data['summary']['countriesOnline']
    current_time = data['summary']['lastUpdated']
    if len(CountriesOnline.objects.all()) == 0:
        CountriesOnline.objects.create(count=countries_online, last_update=current_time)
    else:
        CountriesOnline.objects.all().update(count=countries_online, last_update=current_time)

    for x in range(1, (total_proxies//100+1)):
        print(x)
        data = requests.get(f'https://proxylist.geonode.com/api/proxy-list?limit=100&page={x}&sort_by=lastChecked&sort_type=desc', headers=headers).json()
        for x in data["data"]:
            ip_address = x["ip"]
            port =  x["port"]
            country = x["country"]
            protocol = x["protocols"][0]
            anonymity = x["anonymityLevel"]
            speed = x["speed"]
            uptime = x["upTime"]
            last_check = x["lastChecked"]
            response = x["responseTime"]
            latency = x["latency"]
            org_and_asn = str(x["asn"]) + " " + str(x["org"])
            if Proxy.objects.filter(ip_address=ip_address, port=port).exists():
                Proxy.objects.filter(ip_address=ip_address, port=port).update(ip_address=ip_address, port=port, country=country, protocol=protocol, anonymity=anonymity, speed=speed, uptime=uptime, last_check=last_check, response=response, latency=latency, org_and_asn=org_and_asn)
            else:
                Proxy.objects.create(ip_address=ip_address, port=port, country=country, protocol=protocol, anonymity=anonymity, speed=speed, uptime=uptime, last_check=last_check, response=response, latency=latency, org_and_asn=org_and_asn)



