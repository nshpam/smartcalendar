import requests
from bs4 import BeautifulSoup
import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Fetch the webpage
url = "https://www.majorcineplex.com/movie"  # Change this to the actual page URL
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
response = requests.get(url, headers=headers)

# Parse HTML with BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# --- now showing tab ---
# Find the script tag with id="json_main"
nowshowing_tabs = soup.find("script", {"id": "json_main"})

if nowshowing_tabs:
    # Extract JSON content
    json_data = json.loads(nowshowing_tabs.string.strip())

    # Extract movie URLs
    movie_urls = [item["url"] for item in json_data["itemListElement"]]

    # Print results
    # print("Movie URLs:")
    # for url in movie_urls:
    #     print(url)
else:
    print("JSON script not found.")


# with open("output.html", "w", encoding="utf-8") as file:
#     file.write(soup.prettify())

# print("HTML saved to output.html")
# --- coming soon tab ---
# incoming_tabs = soup.find(class_="bma-movie-list")

incoming_tabs = soup.find_all('div', attrs={'class':'bma-movie-list'})


for tab in incoming_tabs:

    month = tab.find('div', attrs={'class': 'bmaml-month'})  # Search within tab
    if month:
        print(month.get_text(strip=True))
    
    month_movies = tab.find_all('div', attrs={'class': 'mlbc-name'})  # Search within tab

    for mm in month_movies:
        if mm:
            print(mm.get_text(strip=True))
    
    print()
# incoming_tabs = soup.find("div")

# if incoming_tabs:
#     # Extract JSON content
#     json_data = json.loads(incoming_tabs.string.strip())

#     print(json_data)

#     # # Extract movie URLs
#     # movie_urls = [item["url"] for item in json_data["itemListElement"]]

#     # Print results
#     # print("Movie URLs:")
#     # for url in movie_urls:
#     #     print(url)
# else:
#     print("JSON script not found.")