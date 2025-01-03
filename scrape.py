import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time


def scrape_website(website_url):
    print("Launching Chrome Browser...")


    chrome_driver_path = ""
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)


    try:
        driver.get(website_url)
        print("Page loaded successfully...")
        html = driver.page_source

        time.sleep(10)

        return html

    finally:
        driver.quit()




