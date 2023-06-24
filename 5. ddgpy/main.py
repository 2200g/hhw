import requests
from bs4 import BeautifulSoup

def search_duckduckgo(query):
    response = requests.get(f"https://duckduckgo.com/html/?q={query}",
                            headers={"User-Agent": "Mozilla/5.0 (X11; Arch Linux; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0"})
    
    if response.ok:
        results = BeautifulSoup(response.content, "html.parser").select(".result.results_links.results_links_deep.web-result")
        
        for result in results[:1]: 
            print("title:", result.select_one(".result__title").get_text())
            print("url:", result.select_one(".result__url").get_text())
            print("", result.select_one(".result__snippet").get_text())
            print()
    else:
        print("error while retrieving search results.")

search_duckduckgo(input("search query: "))
