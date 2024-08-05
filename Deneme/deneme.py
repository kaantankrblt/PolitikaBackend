import requests
from bs4 import BeautifulSoup


def extract_body_text(url):
    # Define headers to simulate a browser request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

    # Send a GET request to the URL with the custom headers
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract the text from the <body> tag
        body_text = soup.body.get_text(separator=" ", strip=True)

        return body_text
    else:
        return "Failed to retrieve content"


# Example URL
url = "https://www.fdd.org/analysis/op_eds/2024/08/02/enough-is-enough-nato-must-suspend-cooperation-with-turkey/"

# Get the body text of the domain
text = extract_body_text(url)

print("Body Text:", text)
