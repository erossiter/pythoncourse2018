#### Class 04
#### Using Selenium: An Example

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs, NavigableString
import time

def start_chrome(webpage):
    driver = webdriver.Chrome()
    driver.get(webpage)
    return driver

def define_search(driver):
    ## search element changed id randomly, class was the only other info
    ## but 2 elements in this class... we want the 2nd.
    search_elem = driver.find_elements_by_class_name('searchmenu_open')
    search_elem[1].click()

    time.sleep(2)

    keyword_elem = driver.find_element_by_name("query")
    keyword_elem.send_keys("Shirley Clark")

    time.sleep(2)

    button_elem = driver.find_element_by_xpath("//input[@value='Search']")
    button_elem.click()

    return driver

def get_headlines(driver):
    html_source = driver.page_source
    soup = bs(html_source, "lxml")
    
    gma_tags = soup.find_all("span", {"class" : "headline a"})
    gma_headlines = [tag.get_text() for tag in gma_tags]
    with open("headlines.txt", "w") as f:
        f.writelines("\n".join(gma_headlines))

    driver.quit()

def main(webpage):
    driver = start_chrome(webpage)
    time.sleep(2)
    driver = define_search(driver)
    time.sleep(2)
    get_headlines(driver)


main("http://www.spencerdailyreporter.com/")