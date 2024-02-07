from django.shortcuts import render
from .models import *
import pytz
from dotenv import load_dotenv 
load_dotenv()
from datetime import datetime
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .tasks import *


def index(request):
    proxy = Proxy.objects.all()
    proxies_scraped = len(proxy)
    if len(CountriesOnline.objects.all()) == 0:
        countries_online = 0
        last_update = "Never"
    else:
        countries_online = CountriesOnline.objects.all()[0].count
        last_update = CountriesOnline.objects.all()[0].last_update
        ist = pytz.timezone('Asia/Kolkata')
        last_update_datetime = datetime.strptime(last_update, "%Y-%m-%dT%H:%M:%S.%fZ")

        last_update_datetime_ist = last_update_datetime.replace(tzinfo=pytz.utc).astimezone(ist)

        # Format as date and time in AM/PM in IST
        formatted_last_update_ist = last_update_datetime_ist.strftime("%Y-%m-%d %I:%M:%S %p IST")

    return render(request, 'index.html', {'proxy': proxy,'proxies_scraped': proxies_scraped,'countries_online': countries_online,'last_update': formatted_last_update_ist})

# @api_view(['GET'])
# def startScraping(request):
#     start_scraping.delay()
#     return Response({'status': 'success'})