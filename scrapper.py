import requests
from bs4 import BeautifulSoup

def get_html(url):
    try:
        html_page = requests.get(url)
        print('* Get .html page: Successfull ')
        return html_page.content
    
    except:
        print('!! Connection Failed')
        return None

def extract_countries_data(html_page):


    soup = BeautifulSoup(html_page, "html.parser")
    
    countries_data = []
    for country in soup.select(".country"):

        name = country.select_one(".country-name").text.strip()
        capital = country.select_one(".country-capital").text.strip()
        population = int(country.select_one(".country-population").text.strip())
        area = int(float(country.select_one(".country-area").text.strip()))

        countries_data.append((name, capital, population,area))

    print(f'* {len(countries_data)} Countries Data Extracted')
    return countries_data


