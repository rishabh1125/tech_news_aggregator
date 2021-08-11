import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup as BSoup
from news.models import Headline

# Create your views here.
def scrape(request):
    url = 'https://gadgets.ndtv.com/news'
    p = requests.get(url)
    pg  = p.content
    soup = BSoup(pg, 'html.parser')
    code = soup.findAll(class_ = 'thumb')
    for i in range(20):
        try:
            img = code[i].find('img')['data-original']                
        except:
            img = code[i].find('img')['src']
        title = code[i].find('img')['alt']
        link = code[i].find('a')['href']
        new_headline = Headline()
        new_headline.title = title
        new_headline.url = link
        new_headline.image = img
        try:
            new_headline.save()
        except:
            pass
    return redirect("../")    

def news_list(request):
    headlines = Headline.objects.all()[::-1]
    context = {
        'object_list': headlines,
    }
    return render(request, "home.html", context)