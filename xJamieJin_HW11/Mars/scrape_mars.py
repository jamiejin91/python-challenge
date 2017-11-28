import pandas as pd
from bs4 import BeautifulSoup
from splinter import Browser
import requests
import time

def scrape():
    
	executable_path = {'executable_path': 'chromedriver'}
    browser = Browser('chrome', **executable_path, headless=True)


    # Title & Paragraph Scrape
    url_1 = 'https://mars.nasa.gov/news/'
    browser.visit(url_1)
    soup_1 = BeautifulSoup(browser.html, "html.parser")
    news_title = soup_1.find('div', class_='content_title').find('a').text
    news_p = soup_1.find('div', class_='article_teaser_body').text

    # Image Scrape
    url_2 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url_2)
    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(5)
    browser.click_link_by_partial_text('more info')
    soup_2 = BeautifulSoup(browser.html, "html.parser")
    featured_image_url = "https://www.jpl.nasa.gov{}".format(soup_2.find('figure', class_='lede').a['href'])

    # Weather Scrape
    url_3 = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url_3)
    soup_3 = BeautifulSoup(browser.html, 'html.parser')
    mars_tweets = soup_3.find_all('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")
    for mars_tweet in mars_tweets:
        first_word = mars_tweet.text.split(" ")[0]
        if first_word == "Sol":
            mars_weather = mars_tweet.text
            break

    # Facts B Scrape
	url_4 = "https://space-facts.com/mars/"
    browser.visit(url_4)
    soup_4 = BeautifulSoup(browser.html, 'html.parser')
    facts_data = soup_4.find('table', class_="tablepress tablepress-id-mars")
    df_facts = pd.read_html(str(facts_data))
    facts_table = df_facts[0].to_html(index=False, header=None, escape=True).replace("\n", "")

    # Hemisphere Images Scrape
    url_5 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url_5)
    soup_5 = BeautifulSoup(browser.html, "html.parser")
    facts_links = soup_5.find('div', class_="collapsible results").find_all('a', href=True)
    hemisphere_image_urls = []
    for facts_link in facts_links:
        r = requests.get('https://astrogeology.usgs.gov'+facts_link['href'])
        soup_5_temp = BeautifulSoup(r.content)
        facts_title = soup_5_temp.find('title').text.split(' Enhanced')[0]
        facts_img = 'https://astrogeology.usgs.gov' + soup_5_temp.find('img',class_='wide-image').get('src')
        hemisphere_image_urls.append({'title': facts_title, 'img_url':facts_img})


    # Creating and Returning Dictionary for API
    final = {
        "id": 0,
        "news_title": news_title,
        "news_p": news_p,
        "featured_image": featured_image_url,
        "mars_weather": mars_weather,
        "facts_table": facts_table,
        "hemisphere_images": hemisphere_image_urls
    }

    return final