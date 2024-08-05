from selenium.webdriver.chrome.options import Options

FIREBASE_CREDENTIALS_PATH = "/Users/kaantankarabulut/Desktop/Developer/WebFetching/politika-13050-firebase-adminsdk-kg4xy-1244cca38f.json"

CHROME_OPTIONS = Options()
CHROME_OPTIONS.add_argument("--headless")
CHROME_OPTIONS.add_argument("--lang=en-US")
CHROME_OPTIONS.add_argument("--disable-dev-shm-usage")
CHROME_OPTIONS.add_argument("--no-sandbox")

MAX_NEWS_PER_POLITICIAN = 5
