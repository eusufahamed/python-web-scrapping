import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


def create_webdriver_instance():
    options = webdriver.ChromeOptions()
    # options.add_argument('='.join(['--proxy-server', "http://localhost:8888/"]))
    # options.add_extension('./hostpotshield.crx')
    options.add_argument('start-maximized')
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    return driver

def extract_record(url, driver):
    driver.get(url)
    # time.sleep(5)
    name = driver.find_element(By.XPATH, '//*[@id="PN92mmlqXb8"]/div/div[1]/div[1]/div[1]/div[1]/div[1]/div/div/h1')
    age = driver.find_element(By.XPATH, '//*[@id="PN92mmlqXb8"]/div/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]')
    location = driver.find_element(By.XPATH, '//*[@id="PN92mmlqXb8"]/div/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]')

    # print('Name: ', name.text)
    data = {}
    data['url'] = url
    data['name'] = name.text
    data['age'] = age.text
    data['location'] = location.text

    # print('Age : ', age.text)
    # print('Location : ', location.text)

    return data

def form_submit(submit_url, data, driver):
    driver.get(submit_url)
    # driver.execute_script("window.open('https://support.whitepages.com/hc/en-us/requests/new?ticket_form_id=580868')")
    # time.sleep(10)
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

    # value_select = driver.find_element(By.XPATH, '//*[@id="request_custom_fields_360002663794"]')
    # value_select.click()

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
    print(data['name'])
    time.sleep(5)
    form_submit(submit_url, data, driver)
    # time.sleep(10)
    
    # time.sleep(30)
    # driver.execute_script("window.open('https://www.whitepages.com/checkout/summary?wpId=Po3jQN1Dey7&wp_content=card&wp_medium=PersonContactInfoUpsell&wp_source=PersonResults&wp_term=serp_ep0&funnelType=person_onepages_1')")
    # driver.get('https://www.whitepages.com/name/Dion-Chidozie/Dallas-TX/PN92mmlqXb8')
    # print(driver.page_source)
    # time.sleep(30)
    

    
