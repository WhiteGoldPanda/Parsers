from bs4 import BeautifulSoup
from urllib.request import *

url = 'https://www.some.web.site.com/random?page='

def get_html(url):
    req = Request(url)
    html = urlopen(req).read()
    return html

def main():
    opener = build_opener()
    opener.addheaders = [('User-Agent','Mozilla/5.0')]
    install_opener(opener)
    for i in range(1,4):
        html = get_html(url+str(i))
        soup = BeautifulSoup(html, 'html.parser')
        list = soup.find_all(class_='preview')
        for index,a in enumerate(list):
            secondary_html = get_html(a['href'])
            secondary_soup = BeautifulSoup(secondary_html, 'html.parser')
            image = secondary_soup.find(id='foto')['src']
            urlretrieve('https:'+image, image[22:])
            print(str(index),image[22:], 'downloaded')
main()