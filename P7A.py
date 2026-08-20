import requests
from bs4 import BeautifulSoup

url = "https://www.wikipedia.org/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    print("Palak Jaiswal S089")
    print("===== WIKIPEDIA HOMEPAGE SCRAPER =====")

    paragraphs = soup.find_all("p")
    print("\n1. FIRST 3 PARAGRAPHS:")
    for i, p in enumerate(paragraphs[:3], 1):
        print(f"Paragraph {i}: {p.get_text(strip=True)}")

    images = soup.find_all("img")
    print("\n2. IMAGE SRC URLs:")
    for i, img in enumerate(images, 1):
        print(f"{i}. {img.get('src')}")

    links = soup.find_all("a")
    print("\n3. TOTAL NUMBER OF LINKS:")
    print(len(links))

    headings = soup.find_all(["h1", "h2", "h3"])
    print("\n4. HEADINGS:")
    for heading in headings:
        text = heading.get_text(" ", strip=True)
        if text:
            print(f"{heading.name.upper()}: {text}")

    print("\n5. LANGUAGE NAMES:")
    languages = soup.select(".central-featured-lang")

    for language in languages:
        name = language.find("strong")
        if name:
            print(name.get_text(strip=True))

else:
    print("Failed to access Wikipedia.")
    print("Status Code:", response.status_code)
