import bs4
import requests
import argparse

parser = argparse.ArgumentParser(description='Scourer')
parser.add_argument('-u', '--url', help='URL to scour')
args = parser.parse_args()

url = args.url

if url is None:
    print('Please provide a URL to scour')
    exit()

page = requests.get(url)


soup = bs4.BeautifulSoup(page.text, 'html.parser')
images = soup.findAll('img')

for image in images:
    print(image['src'])

for image in images:
    name = image['src'].split('/')[-1]
    with open(name, 'wb') as f:
        im = requests.get(image['src'])
        f.write(im.content)

