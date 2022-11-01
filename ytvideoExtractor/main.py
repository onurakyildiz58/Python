from bs4 import BeautifulSoup
from selenium import webdriver
import time

url = "https://www.youtube.com/results?search_query=sign+language+alphabet"
urlL = "https://www.youtube.com"
driverPath = "chromedriver.exe"
listUrl = []

browser = webdriver.Chrome(driverPath)
browser.get(url)

time.sleep(5)
soup = BeautifulSoup(browser.page_source, "html.parser")

for link in soup.find_all('a', href=True):
    rawLink = str(link.get('href'))
    index = rawLink.find("/watch")

    if index > -1:
        fullUrl = urlL + rawLink
        lenUrl = len(fullUrl)
        if lenUrl < 46:
            listUrl.append(fullUrl)

setUrl = set(listUrl)
with open("links.txt", "w") as f:
    for i in setUrl:
        f.write(i + "\n")
