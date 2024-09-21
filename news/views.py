import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup as BSoup
from news.models import Headline
import logging
logging.basicConfig(filename='app.log', level=logging.DEBUG, 
                       format='%(asctime)s - %(levelname)s - %(message)s')

# Create your views here.
def scrape(request):
    try:
        logging.info()
        url = 'https://gadgets.ndtv.com/news'
        p = requests.get(url)
        pg  = p.content
        soup = BSoup(pg, 'html.parser')
        code = soup.findAll(class_ = 'thumb')
        for i in range(20):
            img_data = code[i].find('img') 
            if 'data-original' in img_data:    
                img = img_data['data-original']                
            else:
                img = img_data['src']
            title = code[i].find('img')['alt']
            link = code[i].find('a')['href']
            new_headline = Headline()
            new_headline.title = title
            new_headline.url = link
            new_headline.image = img
            new_headline.save()
    except Exception as e:
        logging.error(e)
    finally:
        return redirect("../")    

def news_list(request):
    headlines = Headline.objects.all()[::-1]
    context = {
        'object_list': headlines,
    }
    return render(request, "home.html", context)