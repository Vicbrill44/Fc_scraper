from html.parser import HTMLParser
from bs4 import BeautifulSoup
import requests










url = 'https://www.fcscout.com/category/news/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}    # This can be used to bypass a websites bot detecter
starting_articles = ['USMNT Rodrigo Neri Continues To Make An Impact At Atletico Madrid Academy', 
                     'Luca De La Torre Expects To Transfer This Summer Window', 
                     'Reece James: Real Madrid Monitoring Current Contract Status', 
                     'Sadio Mane: Move Likely To Close Soon After Darwin Nunez Signs With Liverpool', 
                     'West Ham United Secure Daniel Rigge', 
                     'Jurgen Damm Closer To A Deal With Club America In Mexico', 
                     'Inter Milan Close To Signing Free Agent Paulo Dybala', 
                     'Liverpool Prepare Bid For Darwin Nunez', 
                     'Chicharito Return to Mexico National Team', 
                     'Zlatan Ibrahimovic Knee Surgery Difficulties']
article_titles = [] 
updating_article_titles = []

result = requests.get(url, headers=headers)     # Adding this headers = headers parameter workerd like a charm, apparently the site could detect if i was a bot and so using what is called a 'user agent solved the problem'

doc = BeautifulSoup(result.text, 'html.parser')     # gtmp parser will give me the html documemnt in a readable format

news_row = doc.find(class_='col-xs-12 col-sm-8 col-md-9')

news_blocks = news_row.find_all(class_='post-list-item col-xs-12 space-bottom col-sm-12 col-md-12')

for news in news_blocks:
    article = news.find_all(class_='col-md-8 text-left item-content')
    for title in article:
        title = title.find('h2')    #class_='post-title text-left h3'
        title = title.find('a')
        article_titles.append(title.string)


for title in article_titles:
    if title not in starting_articles:
        updating_article_titles.append(title)
        
with open('FcScout_newstitle_tracker.txt', 'a') as text_file:
    for new_title in updating_article_titles:
        text_file.write(new_title) 
