import requests
from bs4 import BeautifulSoup

# wikipedia api func:
def search_wikipedia(term):
    search_url = f"https://en.wikipedia.org/w/api.php?action=opensearch&search={term}&limit=1&format=json"
    response = requests.get(search_url)
    data = response.json()
    if data[3]:
        return data[3][0]
    else:
        return None

search_term = input("search term: ")

page_url = search_wikipedia(search_term)

if page_url:
    response = requests.get(page_url)
    soup = BeautifulSoup(response.content, "html.parser")

    headings = soup.find_all(["p"])

    for heading in headings:
        print(heading.text)
else:
    print("wikipedia page not found for the given search term.")
    
