import json
import pandas as pd
from config import CHROME_OPTIONS
from firebase_manager import initialize_firebase
from politician_manager import process_politicians  # Updated import
from selenium import webdriver


def main():
    db = initialize_firebase()
    driver = webdriver.Chrome(options=CHROME_OPTIONS)

    try:
        all_news = process_politicians(db, driver)

        # Save to JSON file
        with open("news_data.json", "w") as json_file:
            json.dump(all_news, json_file, indent=4)

        # Save to Excel file
        df = pd.DataFrame(all_news)
        df.to_excel("news_data.xlsx", index=False)

        print(
            "All politicians and their news have been processed and uploaded to Firebase Firestore. "
            "News data has been saved to news_data.json and news_data.xlsx"
        )
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
