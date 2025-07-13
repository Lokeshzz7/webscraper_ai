import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from selenium.webdriver import Remote, ChromeOptions

def scrape(website):
    print("chrome")

    path = "./chromedriver.exe"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(path),options=options)

    try:
        driver.get(website)
        print("Loading")
        files = driver.page_source
        return files

    finally:
        driver.quit()


def extract_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean(body_content):
    soup = BeautifulSoup(body_content,"html.parser")

    for i in soup(["script","style"]):
        i.extract()

    contentc = soup.get_text(separator="\n")
    contentc = "\n".join(i.strip() for i in contentc.splitlines() if i.strip())

    return contentc

def splitdom(dom,max_length=6000):
    return [dom[i : i + max_length] for i in range(0,len(dom),max_length)]
