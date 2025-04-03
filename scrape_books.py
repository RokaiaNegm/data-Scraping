import requests
from bs4 import BeautifulSoup

# Target website
url = "http://books.toscrape.com"

# Send a request to the website
response = requests.get(url)

# Parse the HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find all book elements
books = soup.find_all("article", class_="product_pod")

# Extract book details
for book in books:
    title = book.h3.a["title"]#Finds the title of the book.  
    price = book.find("p", class_="price_color").text  
    availability = book.find("p", class_="instock availability").text.strip()  
    
    print(f"Title: {title}")
    print(f"Price: {price}")
    print(f"Availability: {availability}\n")


## run python scrape_books.py in  VS  Terminal
#Code Breakdown
#1. Import Required Libraries
#requests: Sends an HTTP request to the website and retrieves its HTML content.
#BeautifulSoup: Parses the HTML and helps extract specific data.
#The requests.get(url) function fetches the webpage.
#The response object contains the HTML of the page.
#"html.parser" tells BeautifulSoup to parse the webpage using Python’s built-in parser.
#