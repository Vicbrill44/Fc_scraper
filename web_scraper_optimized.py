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

full_data = []
 
updating_article_titles = []

logs_cleaned = []



# logs will not be a list of the current shit in the text file
with open('FcScout_tracker.txt', 'r') as text_file: 
    logs = text_file.readlines()

# We will clean logs up and store it in logs_cleaned to remove all spaces, tabs, and newlines
for log in logs:
    log = log.replace('\n', '')
    log = log.replace(' ', '')
    log = log.replace('\t', '')
    logs_cleaned.append(log)




result = requests.get(url, headers=headers)     # Adding this headers = headers parameter workerd like a charm, apparently the site could detect if i was a bot and so using what is called a 'user agent solved the problem'

doc = BeautifulSoup(result.text, 'html.parser')     # gtmp parser will give me the html documemnt in a readable format

news_row = doc.find(class_='col-xs-12 col-sm-8 col-md-9')

news_blocks = news_row.find_all(class_='post-list-item col-xs-12 space-bottom col-sm-12 col-md-12')

for news in news_blocks:
    article = news.find_all(class_='col-md-8 text-left item-content')
    for published in article:
        title = published.find('h2')    #class_='post-title text-left h3'
        title = title.find('a')
        title = title.string
        
        if title not in starting_articles:
    
            author = published.find(class_='col-md-10 col-xs-9')
            author = author.find(class_= 'is-bar')
            author = author.find('li')
            author = author.find('a')
            author = author.string
            
            date = published.find(class_='col-md-10 col-xs-9')
            date = date.find(class_= 'is-bar')
            date = date.find_all('li')
            date = date[2].string
        
            potential_new_article = f'{title}{author}{date}'
            potential_new_article = potential_new_article.replace(' ', '')
            potential_new_article = potential_new_article.replace('\n', '')
            potential_new_article = potential_new_article.replace('\t', '')
            if potential_new_article not in logs_cleaned:
                with open('FcScout_tracker.txt', 'a') as text_file:
                    text_file.write(f'\n{title}\t{author}\t{date}')
            
        
    

        
        
















# Save spot; working but very unintuitive and can  be made more efficient and cleanly.       
""" full_data = []
 
updating_article_titles = []

logs_cleaned = []


result = requests.get(url, headers=headers)     # Adding this headers = headers parameter workerd like a charm, apparently the site could detect if i was a bot and so using what is called a 'user agent solved the problem'

doc = BeautifulSoup(result.text, 'html.parser')     # gtmp parser will give me the html documemnt in a readable format

news_row = doc.find(class_='col-xs-12 col-sm-8 col-md-9')

news_blocks = news_row.find_all(class_='post-list-item col-xs-12 space-bottom col-sm-12 col-md-12')

for news in news_blocks:
    article = news.find_all(class_='col-md-8 text-left item-content')
    for published in article:
        title = published.find('h2')    #class_='post-title text-left h3'
        title = title.find('a')
        title = title.string
        
        author = published.find(class_='col-md-10 col-xs-9')
        author = author.find(class_= 'is-bar')
        author = author.find('li')
        author = author.find('a')
        author = author.string
        
        date = published.find(class_='col-md-10 col-xs-9')
        date = date.find(class_= 'is-bar')
        date = date.find_all('li')
        date = date[2].string
        
        if title not in starting_articles:
            updating_article_titles.append(f'\n{title}\t{author}\t{date}')     # maybe add newline in the biginning

with open('FcScout_tracker.txt', 'r') as text_file:
    logs = text_file.readlines()
    


for log in logs:
    log = log.replace('\n', '')
    log = log.replace(' ', '')
    logs_cleaned.append(log)


for potential_new_article in updating_article_titles:
    potential_new_article = potential_new_article.replace('\n', '')
    potential_new_article = potential_new_article.replace('\t', '')
    potential_new_article = potential_new_article.replace(' ', '')
    if potential_new_article not in logs_cleaned:
        with open('FcScout_tracker.txt', 'a') as text_file:
            text_file.write(f'\n{potential_new_article}') """
        
        
        
        
        
        
        
""" Chicharito Return to Mexico National Team       Carlos Castaguila       on June 8, 2022
Liverpool Prepare Bid For Darwin Nunez  Carlos Castaguila       on June 8, 2022
Inter Milan Close To Signing Free Agent Paulo Dybala    Carlos Castaguila       on June 8, 2022
Jurgen Damm Closer To A Deal With Club America In Mexico        Carlos Castaguila       on June 8, 2022
West Ham United Secure Daniel Rigge     Carlos Castaguila       on June 9, 2022
Sadio Mane: Move Likely To Close Soon After Darwin Nunez Signs With Liverpool   Carlos Castaguila       on June 9, 2022
Reece James: Real Madrid Monitoring Current Contract Status     Carlos Castaguila       on June 9, 2022
Luca De La Torre Expects To Transfer This Summer Window Carlos Castaguila       on June 10, 2022
USMNT Rodrigo Neri Continues To Make An Impact At Atletico Madrid Academy       Carlos Castaguila       on June 10, 2022 """