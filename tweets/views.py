from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_protect
import oauth2 as oauth
import json
from tweets.keys import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET

@csrf_protect
def tweets_list(request):

    return render(request,'tweets/tweets_list.html',{})

def tweets_print(request):
    response_data = {}
    if request.method == 'GET':
        name = request.GET['name']
        count = request.GET['count']
        tweets = []
        consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
        access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
        client = oauth.Client(consumer, access_token)
        url= "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name="+str(name)+"&count="+str(count)
        print url
        resp, data = client.request(url)
        tweet = json.loads(data)
        for t in tweet:
            tweets.append("<p>"+t['text']+"<p>")      
        name=""
        response_data['message'] = tweets
        return HttpResponse(json.dumps(response_data),content_type="application/json")
    return HttpResponse()
