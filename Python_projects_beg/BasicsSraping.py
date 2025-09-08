
#opens browser and looks for https ling
# from selenium import webdriver

# driver = webdriver.Firefox()
# driver.get("https://www.geeksforgeeks.org/python/python-web-scraping-tutorial/") 

"""
from selenium import webdriver
#convenient ways to locate elements on a webpage.
from selenium.webdriver.common.by import By
#starting and stopping the ChromeDriver executable
from selenium.webdriver.chrome.service import Service
#automatically downloads the correct version of ChromeDriver for your installed Chrome
from webdriver_manager.chrome import ChromeDriverManager
import time

element_list = []

# Set up Chrome options (optional)
options = webdriver.ChromeOptions()
#without opening a visible window - for automation and speed
options.add_argument("--headless")
#Disables the Chrome sandbox security feature
options.add_argument("--no-sandbox")
# Prevents Chrome from using /dev/shm (shared memory) some systems have limited space → can cause crashes.
# use normal disk storage instead.
options.add_argument("--disable-dev-shm-usage")

#Checks your Chrome version installed on the system
#Returns the path to that ChromeDriver
#Takes that path and creates a Service object to launch Chrome.
service = Service(ChromeDriverManager().install())

#craping multiple pages of search results
for page in range(1, 3):
    # Important: Initializing a new driver inside a loop will open a new browser instance every time.
    #Launches a Chrome browser instance with the given setup.
    driver = webdriver.Chrome(service=service, options=options)

    url = f"https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page=%7Bpage%7D"
    driver.get(url)
    time.sleep(2) 

    #extract product details
    titles = driver.find_elements(By.CLASS_NAME,"title")
    prices = driver.find_elements(By.CLASS_NAME,"price")
    descriptions = driver.find_elements(By.CLASS_NAME,"description")
    ratings = driver.find_elements(By.CLASS_NAME,"ratings")

    #store result in a list
    for i in range(len(titles)):
        element_list.append([
            titles[i].text,
            prices[i].text,
            descriptions[i].text,
            ratings[i].text
            ])
    #Closes the browser to free system resources.
    driver.quit()

for row in element_list:
    print(row)

"""

from lxml import html
import requests

url = 'https://example.com/'
response = requests.get(url)
#parse the HTML content
#returns an HTML element tree.
#response.content = "<html><body><a href='link1'>Link 1</a><a href='li
tree =html.fromstring(response.content)

#use XPath expressions to extract specific elements from the HTML tree.
# returns list of all <a> ['Link 1', 'Link 2']
links = tree.xpath('//a/text()')

for title in links:
    print(title)
