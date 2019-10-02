from requests import get 
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup, Comment

def is_good_response(resp):
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 and content_type is not None and content_type.find('html') > -1)

def scrap_yahoo_news():
    data = None 

    try: 
        with closing(get("https://news.yahoo.com/", stream=True)) as resp:
            if is_good_response(resp):
                data = resp.content 
            else: 
                data = None
    except RequestException as re:
        print(re)
        data = None
    
    soup = BeautifulSoup(data, 'html.parser')

    tags = soup.find_all("a", class_="Fw(b)", href=True)

    yahooNews = {}

    for node in tags:
        yahooNews['https://news.yahoo.com' + node['href']] = ''.join(node.find_all(text=lambda  text:not isinstance(text, Comment)))

    return yahooNews