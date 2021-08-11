import requests
from bs4 import BeautifulSoup as BSoup


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
    print(str(img)+'\t'+str(title)+'\t'+str(link))