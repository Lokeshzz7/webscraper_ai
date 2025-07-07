import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service

def scrape(website):
    print("chrome")

    path = ""
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(path),options=options)

    try:
        driver.get(website)
        print("Loading")
        files = driver.page_source
        return files

    finally:
        driver.quit()