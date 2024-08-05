import json
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import firebase_admin
from firebase_admin import credentials, firestore
import uuid

# Initialize Firebase
cred = credentials.Certificate(
    "/Users/kaantankarabulut/Desktop/Developer/WebFetching/politika-13050-firebase-adminsdk-kg4xy-1244cca38f.json"
)
firebase_admin.initialize_app(cred)
db = firestore.client()

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--lang=en-US")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(options=chrome_options)


countries = ["Turkey", "USA", "South Korea"]


def translate_time(turkish_time):
    # Clean the input
    turkish_time = turkish_time.replace("CANLI", "").strip()

    # Define translations for relative times
    translations = {
        "saat önce": "hour ago",
        "dakika önce": "minute ago",
        "gün önce": "day ago",
        "hafta önce": "week ago",
        "ay önce": "month ago",
        "yıl önce": "year ago",
    }

    # Define translations for month names
    month_translations = {
        "Oca": "Jan",
        "Şub": "Feb",
        "Mar": "Mar",
        "Nis": "Apr",
        "May": "May",
        "Haz": "Jun",
        "Tem": "Jul",
        "Ağu": "Aug",
        "Eyl": "Sep",
        "Eki": "Oct",
        "Kas": "Nov",
        "Ara": "Dec",
    }

    # Translate relative times
    for tr, en in translations.items():
        if tr in turkish_time:
            number = turkish_time.split()[0]
            return f"{number} {en}"

    # Translate month names in specific date formats
    for tr_month, en_month in month_translations.items():
        if tr_month in turkish_time:
            turkish_time = turkish_time.replace(tr_month, en_month)

    # Process specific date formats
    try:
        date = datetime.strptime(turkish_time, "%d %b %Y")
        return date.strftime("%d %b %Y")
    except ValueError:
        return turkish_time


def fetch_news(search_term):
    url = (
        f"https://www.google.com/search?q={search_term.replace(' ', '+')}&tbm=nws&hl=en"
    )
    driver.get(url)

    news_results = driver.find_elements(By.CSS_SELECTOR, "div#rso > div >div>div>div")
    news_list = []

    for news_div in news_results[:10]:  # Limit to top 10 news items
        try:
            news_item = {}
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

            news_item["id"] = str(uuid.uuid4())
            news_item["upload_time"] = datetime.now().isoformat()

            news_list.append(news_item)

        except Exception as e:
            print(f"Error processing news item: {e}")

    return news_list


def fetch_top_news_for_countries(countries):
    all_news = []
    for country in countries:
        print(f"Fetching top news for {country}")
        country_news = fetch_news(f"{country} news")
        print(f"Fetched {len(country_news)} news items for {country}")
        for news_item in country_news:
            news_item["country"] = country
        all_news.extend(country_news)
    return all_news


def update_firestore(news_list):
    # Get all existing news
    existing_news = db.collection("World_news").get()

    # Create a dictionary of existing news with their links as keys
    existing_news_dict = {doc.to_dict()["link"]: doc for doc in existing_news}

    # Update or add new news
    for news_item in news_list:
        if news_item["link"] in existing_news_dict:
            # Update existing news
            doc_ref = existing_news_dict[news_item["link"]].reference
            doc_ref.update(news_item)
        else:
            # Add new news
            db.collection("World_news").add(news_item)

    # Fetch all news again
    all_news = db.collection("World_news").get()

    # Sort news items by upload time (descending order)
    sorted_news = sorted(
        all_news, key=lambda x: x.to_dict()["upload_time"], reverse=True
    )

    # Keep only the latest 10 news items
    for doc in sorted_news[len(countries * 10) :]:
        doc.reference.delete()


# Fetch top news for specified countries
print("Fetching top world news")
top_news = fetch_top_news_for_countries(countries)

# Update Firestore
update_firestore(top_news)

driver.quit()

# Save to JSON file
with open("World_news.json", "w") as json_file:
    json.dump(top_news, json_file, indent=4)
