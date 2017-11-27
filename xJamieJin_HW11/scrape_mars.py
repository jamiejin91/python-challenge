import pandas as pd
from bs4 import BeautifulSoup
from splinter import Browser
import requests
import time

def scrape():
    
	executable_path = {'executable_path': 'chromedriver'}
    browser = Browser('chrome', **executable_path, headless=True)
    soup = BeautifulSoup(browser.html, "html.parser")

    # Title & Paragraph Scrape
    url_1 = 'https://mars.nasa.gov/news/'
    browser.visit(url_1)
    news_title = soup.find('div', class_='content_title').find('a').text
    news_p = soup.find('div', class_='article_teaser_body').text

    # Image Scrape
    url_2 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url_2)
    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(5)
    browser.click_link_by_partial_text('more info')
    soup = BeautifulSoup(browser.html, "html.parser")
    featured_image_url = "https://www.jpl.nasa.gov/{}".format(soup.find('figure', class_='lede').a['href'])

    # Weather Scrape
    url_3 = "https://twitter.com/marswxreport?lang=en"
    browser.visit("https://twitter.com/marswxreport?lang=en")
    soup = BeautifulSoup(browser.html, 'html.parser')
    mars_weather = soup.find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text

    # Facts B Scrape
	url_4 = "https://space-facts.com/mars/"
    browser.visit(url_4)
    soup = BeautifulSoup(browser.html, 'html.parser')
    facts_data = soup.find('table', class_="tablepress tablepress-id-mars")
    df_facts = pd.read_html(str(table))
    facts_table = df_facts[0].to_html(index=False, escape=True, header=None).replace('\n','')

    # Hemisphere Images Scrape
    url_5 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url_5)
    soup = BeautifulSoup(browser.html, "html.parser")
    hemispheres = soup.find('div', class_="collapsible results").find_all('a')
	hemisphere_image_urls = []
	hemispheredict = {}
    for hemisphere in hemispheres:
        browser.visit('https://astrogeology.usgs.gov{}'.format(hemisphere.get('href')))
        soup = BeautifulSoup(browser.html, 'html.parser')
        title = soup.find('title').text
        hemisphereTitle = title.split('|')
        hemisphereTitle = hemisphereTitle[0].replace(' Enhanced ','')
        imgUrl = soup.find('img',class_='wide-image').get('src')
        imgUrl = hemisphereBaseUrl + imgUrl
        hemispheredict = {"title": hemisphereTitle, "img_url":imgUrl}
        hemisphere_image_urls.append(hemispheredict)


    # Creating and Returning Dictionary for API
    final = {
        "id": 1,
        "news_title": news_title,
        "news_p": news_p,
        "featured_image": featured_image_url,
        "mars_weather": mars_weather,
        "facts_table": facts_table,
        "hemisphere_images": hemisphere_image_urls
    }

    return final