import no_ads
import requests
from bs4 import BeautifulSoup




url = "https://123moviesfree.net/home"
download_html = requests.get(url)
soup = BeautifulSoup(download_html.text)
with open('downloaded.html', 'w', encoding="utf-8") as file:
    file.write(soup.prettify())

mydivs = soup.findAll("div", {"class": "ml-item"})

for films in mydivs:
    print("----------------------")
    data = films.find('a', href = True)
    title = data['title']
    links = data['href']
    #img = data[]
    #print(data)
    print(title)
    link = 'https://123moviesfree.net/'+links+'/watching.html'
    no_ads.no_ads(link)