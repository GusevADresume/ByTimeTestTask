import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
import time

logging.basicConfig(level=logging.INFO, filename='errors_selenium.log', filemode='w')
import pandas


def get_html_data() -> list[webdriver.remote.webelement.WebElement]:
    while True:
        try:
            driver = webdriver.Chrome()
            driver.set_window_size(1200, 800)
            driver.get('https://www.rbc.ru')
            driver_list = driver.find_elements(By.CLASS_NAME, "js-main-reload-item")
            return driver_list
            break
        except Exception as e:
            logging.error(e)
            time.sleep(3)


def pars(element_list: list) -> list[dict]:
    result = []
    for item in element_list:
        news = {'News_header': item.text, 'News_url': item.find_element(By.TAG_NAME, 'a').get_attribute('href')}
        result.append(news)

    return result


def write_to_csv(news_list: list) -> str:
    try:
        dataFrame = pandas.DataFrame(news_list)
        dataFrame.to_csv('news_selenium.csv', encoding='utf-8-sig')
        return json.dumps(news_list, ensure_ascii=False)
    except Exception as e:
        logging.error(e)
        return False

def selenium_main():
    html_data = get_html_data()
    news_list = pars(html_data)
    return write_to_csv(news_list)
