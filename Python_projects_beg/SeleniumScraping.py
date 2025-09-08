import time
#driver to interact with site
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd

URL = 'https://web.archive.org/web/20220513152428/https://www.thesun.co.uk/sport/football/'
chromedriver_path = r"C:\Users\User\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"

service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service)
# waits 60 seconds because page loads slowly
driver.set_page_load_timeout(60)  
driver.get(URL)

#Xpath to text boxes //div[@class="teaser__copy-container"].
#Returns a list
containers = driver.find_elements(by="xpath",value='//div[@class="teaser__copy-container"]')
titles = []
subtitles = []
links = [] 

for container in containers:
    #Xpath to text boxes' titles //div[@class="teaser__copy-container"]/a/h2
    title = container.find_element(by='xpath', value = './a/h2').text
    titles.append(title)
    #Xpath to text boxes' texts //div[@class="teaser__copy-container"]/a/p
    subtitle = container.find_element(by='xpath', value = './a/p').text
    subtitles.append(subtitle)
    #Xpath to text boxes' links //div[@class="teaser__copy-container"]/a
    #get atribute href in a -->link itself
    link = container.find_element(by = 'xpath', value = './a').get_attribute("href")
    links.append(link)

footballnews_data = {"Title":titles,"Subtitle":subtitles, "Link":links}
df = pd.DataFrame(footballnews_data, index=False)
df.to_csv("Website_football_news.csv")

driver.quit()