import json
import requests
from bs4 import BeautifulSoup
import time
import logging
import pandas

logging.basicConfig(level=logging.INFO, filename='errors_bs4.log', filemode='w')


def get_html_data() -> BeautifulSoup:
    while True:
        try:
            request = requests.get('https://www.rbc.ru').text
            return BeautifulSoup(request, features="html.parser")
            break
        except Exception as e:
            logging.error(e)
            time.sleep(3)


def pars(html: BeautifulSoup) -> list[dict]:
    try:
        news_list = []
        main_news_list = html.findAll('div', class_='js-main-reload-item')
        for item in main_news_list:
            news = {'News_header': item.text, 'News_url': item.find_all('a')[0].get('href')}
            news_list.append(news)
        return (news_list)

    except Exception as e:
        logging.error(e)

def write_to_csv(news_list: list):
    try:
        dataFrame = pandas.DataFrame(news_list)
        dataFrame.to_csv('news_bs4.csv', encoding='utf-8-sig')
        return json.dumps(news_list, ensure_ascii=False)
    except Exception as e:
        logging.error(e)
        return False

def bs4_main():
    html_data = get_html_data()
    news_list = pars(html_data)
    return write_to_csv(news_list)

