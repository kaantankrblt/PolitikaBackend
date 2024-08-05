from datetime import datetime
from selenium.webdriver.common.by import By
import uuid
from utils import translate_time
from firebase_manager import update_firestore


def fetch_news(driver, politician):
    search_term = f"{politician['name']} {politician['title']}"
    url = f"https://www.google.com/search?q={search_term.replace(' ', '+')}&tbm=nws"
    driver.get(url)

    news_results = driver.find_elements(By.CSS_SELECTOR, "div#rso > div >div>div>div")
    news_list = []

    for news_div in news_results:
        try:
            news_item = process_news_item(news_div, politician)
            news_list.append(news_item)
        except Exception as e:
            print(f"Error processing news item: {e}")

    return news_list


def process_news_item(news_div, politician):
    news_item = {}
    news_item["link"] = news_div.find_element(By.TAG_NAME, "a").get_attribute("href")

    divs_inside_news = news_div.find_elements(By.CSS_SELECTOR, "a>div>div>div")

    for i, new in enumerate(divs_inside_news):
        if i == 1:
            news_item["domain"] = new.text
        elif i == 2:
            news_item["title"] = new.text
        elif i == 3:
            news_item["description"] = new.text
        elif i == 4:
            news_item["date"] = translate_time(new.text)

    news_item["id"] = str(uuid.uuid4())
    news_item["upload_time"] = datetime.now().isoformat()
    news_item["politician_id"] = politician["id"]
    news_item["politician_name"] = politician["name"]
    news_item["politician_title"] = politician["title"]

    return news_item


def fetch_and_update_news(db, driver, politician):
    news_list = fetch_news(driver, politician)
    update_firestore(db, politician, news_list)
    return news_list
