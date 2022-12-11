from urllib.request import urlopen
from bs4 import BeautifulSoup

tag_map = {}
user_map = {}

def scrapeTags(url):
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')

    tags = soup.findAll('a', attrs={'class':'post-tag'})
    tag_len = len(tags)

    for i in range(0, tag_len):
        name = soup.select('div > div > a.post-tag')[i].text
        freq = soup.select('div > div > span > span.item-multiplier-count')[i].text
        tag_map[name] = freq


def scrapeUsers(url):
    page = urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')

    for n in soup.select('div > div > div.user-details > a'):
        user_name = n.get_text()
        user_map[user_name] = {}

        test = n.get('href', None)
        link = "https://stackoverflow.com" + test
        openLink(link, user_name)


def openLink(link, user_name):
    page = urlopen(link)
    soup = BeautifulSoup(page, 'html.parser')

    location = soup.select('ul.list-unstyled > li')[0].text
    user_map[user_name]['location'] = location.strip()

    reputation = soup.find('div', attrs={'class':'reputation'}).get_text().replace('reputation', '')
    user_map[user_name]['reputation'] = reputation.strip()


scrapeTags("https://stackoverflow.com/tags")
scrapeTags("https://stackoverflow.com/tags?page=2&tab=popular")

scrapeUsers("https://stackoverflow.com/users")
print(tag_map)
print(user_map)