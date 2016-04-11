from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect, HttpResponse
import oauth2 as oauth
import json

def tweets_list(request):
    if request.GET:
        tweets = []
        name = request.GET.get('N')
        count = request.GET.get('C')
        CONSUMER_KEY = "3AftlqM1umGMroSjZkpXr3GUH"
        CONSUMER_SECRET = "jchT7UAxWNcWlbyAFOkLgRSRcY56cDGuSLPMunAnW4ZouD91rm"
        ACCESS_KEY = "172601787-hgzlSicp47ARWKzYFvrjiiSPDBBvKbxwoVuvL9Q5"
        ACCESS_SECRET = "TznA0AKodZ2O7JI6lfz6PAM0lRDxtEtoHInP5ebU3sg37"
        consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
        access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
        client = oauth.Client(consumer, access_token)
        url= "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name="+str(name)+"&count="+str(count)
        resp, data = client.request(url)
        tweet = json.loads(data)
        for t in tweet:
            tweets.append(t['text'])      
        name=""
        return render(request,'tweets/tweets_print.html',{ 'tweets':tweets })
    return render(request,'tweets/tweets_list.html',{})
