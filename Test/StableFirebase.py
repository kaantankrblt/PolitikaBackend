import json
import pandas as pd
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase
cred = credentials.Certificate(
    "/Users/kaantankarabulut/Desktop/Developer/WebFetching/politika-13050-firebase-adminsdk-kg4xy-1244cca38f.json"
)
firebase_admin.initialize_app(cred)
db = firestore.client()

chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode if needed
chrome_options.add_argument("--lang=en-US")  # Set language to English
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(options=chrome_options)

search_term = "Recep Tyyip Erdogan"

url = f"https://www.google.com/search?q={search_term.replace(' ', '+')}&tbm=nws"
driver.get(url)


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


news_results = driver.find_elements(By.CSS_SELECTOR, "div#rso > div >div>div>div")
news_list = []

for news_div in news_results:
    news_item = {}
    try:
        news_link = news_div.find_element(By.TAG_NAME, "a").get_attribute("href")
        news_item["link"] = news_link

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

        news_list.append(news_item)

        news_item["upload_time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Upload to Firebase Firestore
        db.collection("news").add(news_item)

    except Exception as e:
        print("No Elems", e)

driver.quit()

# Save to JSON file
with open("news_data.json", "w") as json_file:
    json.dump(news_list, json_file, indent=4)

# Save to Excel file
df = pd.DataFrame(news_list)
df.to_excel("news_data.xlsx", index=False)

print(
    "All news has been uploaded to Firebase Firestore and saved to news_data.json and news_data.xlsx"
)
