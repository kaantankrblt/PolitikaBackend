import uuid
from politicians_data import politicians
from news_fetcher import fetch_and_update_news


def update_or_create_politician(db, politician_data):
    query = db.collection("politicians").where("title", "==", politician_data["title"])
    docs = query.stream()

    for doc in docs:
        doc_ref = db.collection("politicians").document(doc.id)
        doc_ref.update(politician_data)
        print(f"Updated existing politician: {politician_data['name']}")
        return doc.to_dict()

    politician_data["id"] = str(uuid.uuid4())
    db.collection("politicians").add(politician_data)
    print(f"Created new politician: {politician_data['name']}")
    return politician_data


def process_politicians(db, driver):
    all_news = []
    for politician in politicians:
        try:
            updated_politician = update_or_create_politician(db, politician)
            print(f"Fetching news for {updated_politician['name']}")
            position_news = fetch_and_update_news(db, driver, updated_politician)
            all_news.extend(position_news)
        except Exception as e:
            print(f"Error processing {politician['name']}: {str(e)}")
    return all_news
