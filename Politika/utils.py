# def translate_time(turkish_time):
#     translations = {
#         "saat önce": "hour ago",
#         "dakika önce": "minute ago",
#         "gün önce": "day ago",
#         "hafta önce": "week ago",
#         "ay önce": "month ago",
#         "yıl önce": "year ago",
#     }
#     for tr, en in translations.items():
#         if tr in turkish_time:
#             number = turkish_time.split()[0]
#             return f"{number} {en}"
#     return turkish_time

from datetime import datetime


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
