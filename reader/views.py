from django.shortcuts import render
import feedparser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
# Create your views here.

@csrf_exempt
def reader_page(request):
	entered_url = request.POST.get('url')
        #print entered_url
	data_feed = feedparser.parse(entered_url)
        #print data_feed
        entries = data_feed.entries
        #print entries[0]
        data_list = []
        for data in entries:
                data_dict = {
                'title':data.title,
                'description' : data.description,
                'link' : data.link
                }
                data_list.append(data_dict)

        #print data_one
        return HttpResponse(json.dumps(data_list))
	


def entry_page(request):
	return render(request, 'entry_page.html')
