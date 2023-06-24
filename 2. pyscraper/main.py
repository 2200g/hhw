import requests
from bs4 import BeautifulSoup

url = input("url to scrape: ")
element = input("html element to scrape ['p', 'div', 'a']: ")

print("---")

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    elements = soup.find_all(element)

    for elem in elements:
        print(elem.get_text())
else:
    print("error.")
