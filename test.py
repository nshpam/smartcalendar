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

with open("output_2.html", "w", encoding="utf-8") as file:
    file.write(soup.prettify())

print("HTML saved to output.html")