import requests
from bs4 import BeautifulSoup

#REQUEST WEBPAGE AND STORE IT AS A VARIABLE

crypto_name = "Ripple" # replace this with the name of the cryptocurrency you're interested in

url = f"https://www.sec.gov/news/pressreleases?aId=&combine={crypto_name}&year=All&month=All"
response = requests.get(url)

html_doc = response.text
soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.find_all("h1"))
