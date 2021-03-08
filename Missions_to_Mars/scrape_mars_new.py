# Import dependencies

from bs4 import BeautifulSoup as bs
from splinter import Browser
import pandas as pd
import requests

executable_path = {"executable_path": "/Users/shayn/Downloads/chromedriver"}

browser = Browser("chrome", **executable_path, headless=False)

news_url = "https://mars.nasa.gov/news/"
browser.visit(news_url)
html = browser.html
soup = BeautifulSoup(html, "html.parser")

article = soup.find("div", class_='list_text')
news_title = article.find("div", class_="content_title").text
news_p = article.find("div", class_ ="article_teaser_body").text
print(news_title)
print(news_p)

image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(image_url)
html = browser.html
soup = BeautifulSoup(html, "html.parser")

image = soup.find("img", class_="thumb")["src"]
featured_image_url = "https://www.jpl.nasa.gov" + image
print(featured_image_url)

import pandas as pd

# Visit Mars facts url 
facts_url = 'http://space-facts.com/mars/'

mars_facts = pd.read_html(facts_url)

mars_df = mars_facts[0]

# Assign column names
mars_df.columns = ['Description','Value']

mars_df.set_index('Description', inplace=True)

# Display mars_df
print(mars_df)

import time 
hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(hemispheres_url)
html = browser.html
soup = BeautifulSoup(html, "html.parser")
mars_hemisphere = []

products = soup.find("div", class_ = "result-list" )
hemispheres = products.find_all("div", class_="item")

for hemisphere in hemispheres:
    title = hemisphere.find("h3").text
    title = title.replace("Enhanced", "")
    end_link = hemisphere.find("a")["href"]
    image_link = "https://astrogeology.usgs.gov/" + end_link    
    browser.visit(image_link)
    html = browser.html
    soup=BeautifulSoup(html, "html.parser")
    downloads = soup.find("div", class_="downloads")
    image_url = downloads.find("a")["href"]
    mars_hemisphere.append({"title": title, "img_url": image_url})