# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup
import requests

def create_webdriver_instance():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()

    return driver

def get_search_url(search_term):
    """Generate a url from search term"""
    format_search = search_term.replace(' ', '%20')
    search_url = f'https://2gis.ae/dubai/search/{format_search}/rubricId/319'
    search_url += '/page/{}'

    return search_url


def data_page_url(search_url):
    # Get every single data page
    baseUrl = 'https://2gis.ae'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }
    allDataLinks = []
    for page in range(1, 2):
        r = requests.get(search_url.format(page), headers=headers)
        soup = BeautifulSoup(r.content, 'lxml')

        allDiv = soup.find_all('div', class_='_1h3cgic')

        for data in allDiv:
            for link in data.find_all('a', href=True):
                allDataLinks.append(baseUrl + link['href'])

    print(len(allDataLinks))
    print(allDataLinks)

    return allDataLinks

def extract_record(getUrl, driver):
    for link in getUrl:
        driver.get(link)
        # linkClick = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Show phone numbers']")))
        # linkClick.click()
        soup = BeautifulSoup(driver.page_source, 'lxml')

        companyName = soup.find('span', class_='_oqoid').text.strip()

        addressDiv = soup.find('div', class_='_13eh3hvq')
        allAddressDiv = addressDiv.find_all('div', class_=None)
        for data in allAddressDiv:
            for item in data.find_all('div', class_=None):
                address1 = item.contents[0].get_text(separator=' ', strip=True)
                address2 = item.contents[1].get_text()
                address3 = item.contents[2].get_text()

                fullAddress = ' / '.join((address1, address2, address3))

        # driver.find_element_by_xpath("//button[text()='Show phone numbers']").click()
        # linkClick = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Show phone numbers']")))
        # linkClick.click()

        print(fullAddress)

if __name__ == '__main__':
    driver = create_webdriver_instance()
    url = get_search_url('Safety and security systems')
    all_url = data_page_url(url)

    data = extract_record(all_url, driver)
