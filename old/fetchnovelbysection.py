import requests
from bs4 import BeautifulSoup
import os

# Create a directory to save the HTML files
os.makedirs('novel_pages', exist_ok=True)

# Base URL for the novel pages
base_url = "https://ncode.syosetu.com/n3900hn/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
# Loop through pages 1 to 100
for page_number in range(1, 101):
    # Construct the full URL for the current page
    url = f"{base_url}{page_number}"
    
    # Send a GET request to fetch the page content
    response = requests.get(url, headers=headers)  

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the content within the specified div
        content_div = soup.find('div', class_='js-novel-text p-novel__text')
        
        # If the content div is found, save it to an HTML file
        if content_div:
            with open(f'novel_pages/page_{page_number}.html', 'w', encoding='utf-8') as file:
                file.write(str(content_div))
            print(f"Saved: page_{page_number}.html")
        else:
            print(f"Content not found on page {page_number}")
    else:
        print(f"Failed to retrieve page {page_number}: Status code {response.status_code}")