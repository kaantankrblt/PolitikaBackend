import json
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Initialize the WebDriver
driver = webdriver.Chrome()

url2 = 'https://www.google.com/search?q=korean+political+leaders&tbm=nws'

driver.get(url2)

# Function to translate Turkish time expressions to English


def translate_time(turkish_time):
    translations = {
        "saat önce": "hour ago",
        "dakika önce": "minute ago",
        "gün önce": "day ago",
        "hafta önce": "week ago",
        "ay önce": "month ago",
        "yıl önce": "year ago",
    }
    for tr, en in translations.items():
        if tr in turkish_time:
            number = turkish_time.split()[0]
            return f"{number} {en}"
    return turkish_time


# Extract the news data
news_data = []
news_results = driver.find_elements(
    By.CSS_SELECTOR, 'div#rso > div > div > div > div')
for news_div in news_results:
    news_item = {}
    try:
        news_link = news_div.find_element(
            By.TAG_NAME, 'a').get_attribute('href')
        news_item['Link'] = news_link

        divs_inside_news = news_div.find_elements(
            By.CSS_SELECTOR, 'a > div > div > div')

        if len(divs_inside_news) >= 5:
            news_item['Domain'] = divs_inside_news[1].text
            news_item['Title'] = divs_inside_news[2].text
            news_item['Description'] = divs_inside_news[3].text
            news_item['Date'] = translate_time(divs_inside_news[4].text)

            # Find the main photo URL
            try:
                main_photo = news_div.find_element(
                    By.CSS_SELECTOR, 'img').get_attribute('src')
                news_item['MainPhoto'] = main_photo
            except:
                pass

        news_data.append(news_item)

    except Exception as e:
        print("Error extracting data:", e)

driver.quit()

# Save to JSON
with open('news_data.json', 'w') as json_file:
    json.dump(news_data, json_file, indent=4)

# Save to Excel
df = pd.DataFrame(news_data)
df.to_excel('news_data.xlsx', index=False)

print("Data saved to 'news_data.json' and 'news_data.xlsx'")
