import firebase_admin
from firebase_admin import credentials, firestore
from config import FIREBASE_CREDENTIALS_PATH


def initialize_firebase():
    cred = credentials.Certificate(FIREBASE_CREDENTIALS_PATH)
    firebase_admin.initialize_app(cred)
    return firestore.client()


def update_firestore(db, politician, news_list):
    existing_news = (
        db.collection("news").where("politician_id", "==", politician["id"]).get()
    )
    existing_news_dict = {doc.to_dict()["link"]: doc for doc in existing_news}

    for news_item in news_list:
        if news_item["link"] in existing_news_dict:
            doc_ref = existing_news_dict[news_item["link"]].reference
            doc_ref.update(news_item)
        else:
            db.collection("news").add(news_item)

    all_news = (
        db.collection("news").where("politician_id", "==", politician["id"]).get()
    )
    sorted_news = sorted(
        all_news, key=lambda x: x.to_dict()["upload_time"], reverse=True
    )

    for doc in sorted_news[5:]:
        doc.reference.delete()
