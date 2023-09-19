#IMPORT LIBRARIES
from bs4 import BeautifulSoup
import requests

def get_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if the GET request was unsuccessful
    except (requests.RequestException, ValueError) as err:
        print(f"An error occurred: {err}")
        return None
    else:
        return response.text

def scrape_crypto_news(crypto_name):
    url = f"https://www.sec.gov/news/pressreleases?aId=&combine={crypto_name}&year=All&month=All"
    html_doc = get_html(url)
    
    if html_doc is not None:
        soup = BeautifulSoup(html_doc, 'html.parser')
        print(soup.prettify())
        
        # Assuming that each news item is in an article tag
        for article in soup.find_all('article'):
            # The headline is the text of a span tag with class "show-for-small"
            headline_tag = article.find('span', {'class': 'show-for-small'})
            headline = headline_tag.get_text(strip=True) if headline_tag else "No headline found"
            
            # The date is the text of a time tag with class "datetime"
            date_tag = article.find('time', {'class': 'datetime'})
            date = date_tag.get_text(strip=True) if date_tag else "No date found"
            
            # Find the tbody tag
            tbody_tag = article.find('tbody')
            if tbody_tag:
                # Find all td tags with headers attribute inside the tbody tag
                td_tags = tbody_tag.find_all('td', headers=True)
                for td in td_tags:
                    print(td.get_text(strip=True))  # Print the text of each td tag
            
            print(f"Headline: {headline}\nDate: {date}\n")
    else:
        print("Failed to retrieve webpage.")
# Test the function
scrape_crypto_news("Bitcoin")
