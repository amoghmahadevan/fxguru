from bs4 import BeautifulSoup
import cloudscraper

#Scraping Finance News headlines from reuters.com

def get_article(card):
    return dict(
        headline = card.get_text(),
        link = 'https://www.reuters.com' + card.get('href')
    )

def reuters_com():

    scraper = cloudscraper.create_scraper()
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }

    response = scraper.get("https://www.reuters.com/business/finance/", headers = headers)

    soup = BeautifulSoup(response.content, 'html.parser')

    links = []
    #Selecting ALL cards that start with media story card body
    cards = soup.select('[class^="media-story-card__body"]')
    #List of links for headlines
    for card in cards:
        #Find heading first then link (Link is contained in Heading)
        card_heading = card.find('h3', {'data-testid' : 'Heading'})
        card_article = card_heading.find('a', {'data-testid' : 'Link'})
        links.append(get_article(card_article))
    return links