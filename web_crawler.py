import requests
from bs4 import BeautifulSoup
import pandas as pd
import os.path

URL = 'http://blog.yes24.com/BlogMain/Review/NewReview'


def download_html_from_url(url):
    try:
        response = requests.get(url)
        html = response.text
    except requests.ConnectionError:
        print('Connection Error')
        html = None
    return html


def get_review_url_date(tag):
    content = tag.text.split('|')
    return tag.a.attrs['href'], content[2].strip()


def crawler_new_post(root_soup):
    data = []
    for i in soup.find_all('p', attrs={'class': 'gulinfo'}):
        data.append(get_review_url_date(i))
    return data


ct_html = download_html_from_url(URL)
soup = BeautifulSoup(ct_html, 'html.parser')
new_data = crawler_new_post(soup)
df = pd.DataFrame(new_data)
df.rename(columns={0: 'Url', 1: 'Date'}, inplace=True)
df = df[['Date', 'Url']]

if os.path.isfile('test.csv'):
    past_csv = pd.read_csv('test.csv', usecols=[0, 1])
    df = pd.concat([past_csv, df], axis=0, ignore_index=True).reset_index()
df.to_csv('test.csv',  index=False)
