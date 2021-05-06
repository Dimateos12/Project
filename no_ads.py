import requests
from bs4 import BeautifulSoup


def no_ads(urls):
    url = str(urls)
    soup_url = BeautifulSoup(requests.get(url, verify=True).text, 'html.parser')
    list_link = []
    for link in soup_url.find_all('a'):
        if link.get('onclick') != None and "load_episode_video" in link.get('onclick') and "player" in link.get(
                'onclick'):
            list_link.append(link.get('onclick'))
    print(list_link)
