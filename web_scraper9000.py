import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver


driver = webdriver.Edge(executable_path='C:/Users/vicvas/Documents/webdriver/edge/msedgedriver.exe')
driver.get('https://www.fcscout.com/north-america/usa/')

results = []

content =  driver.page_source

soup = BeautifulSoup(content, features='html.parser')

for element in soup.findAll(attrs='elementor-button-link elementor-button elementor-size-sm'):
    name = element.find('span')
    if name not in results:
        results.append(name.text)

for team in results:
    team = team.replace('\n', '')
    print(team)    
    
    



