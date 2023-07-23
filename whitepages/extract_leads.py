import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


def create_webdriver_instance():
    options = webdriver.ChromeOptions()
    options.add_argument('start-maximized')
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    return driver

def extract_record(url, driver):
    driver.get(url)
    name = driver.find_element(By.XPATH, '//*[@id="PN92mmlqXb8"]/div/div[1]/div[1]/div[1]/div[1]/div[1]/div/div/h1')
    age = driver.find_element(By.XPATH, '//*[@id="PN92mmlqXb8"]/div/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]')
    location = driver.find_element(By.XPATH, '//*[@id="PN92mmlqXb8"]/div/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]')

    data = {}
    data['url'] = url
    data['name'] = name.text
    data['age'] = age.text
    data['location'] = location.text

    return data

def form_submit(submit_url, data, driver):
    driver.get(submit_url)

    email = driver.find_element(By.XPATH, '//*[@id="request_anonymous_requester_email"]')
    email.send_keys('eusuf@gmail.com')

    url = driver.find_element(By.XPATH, '//*[@id="request_custom_fields_44339788"]')
    url.send_keys(data['url'])

    name = driver.find_element(By.XPATH, '//*[@id="request_custom_fields_360007194753"]')
    name.send_keys(data['name'])

    address = driver.find_element(By.XPATH, '//*[@id="request_custom_fields_360007272574"]')
    address.send_keys('5964 Fox Hill Ln')

    city_state = driver.find_element(By.XPATH, '//*[@id="request_custom_fields_360007194773"]')
    city_state.send_keys(data['location'])

    phn = driver.find_element(By.XPATH, '//*[@id="request_custom_fields_360007272554"]')
    phn.send_keys('01873176614')

    removed_cause = driver.find_element(By.XPATH, '//*[@id="new_request"]/div[8]/a')
    removed_cause.click()

    time.sleep(5)

    # value_select = driver.find_element(By.XPATH, '//*[@id="_9s95rl3ac"]')
    # value_select.click()

    # time.sleep(5)

    subject = driver.find_element(By.XPATH, '//*[@id="request_subject"]')
    subject.send_keys('Removed')

    description = driver.find_element(By.XPATH, '//*[@id="request_description"]')
    description.send_keys('I want to remove my account')

    time.sleep(20)

    button = driver.find_element(By.XPATH, '//*[@id="new_request"]/footer/input')
    button.click()

if __name__ == '__main__':
    driver = create_webdriver_instance()

    extract_url = 'https://www.whitepages.com/name/Dion-Chidozie/Dallas-TX/PN92mmlqXb8'
    submit_url = 'https://support.whitepages.com/hc/en-us/requests/new?ticket_form_id=580868'

    data = extract_record(extract_url, driver)

    time.sleep(3)

    form_submit(submit_url, data, driver)
    

    
