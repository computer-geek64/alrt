from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup


def webscrape():  # opens the selenium driver and grabs the links of all websites in the homepage
    driver = webdriver.Chrome("./chromedriver")
    driver.get("https://gdacs.org/Alerts/default.aspx")

    elements = driver.find_elements_by_css_selector("tr.clickable-row")
    types = driver.find_element_by_tag_name("tr")
    for element in elements[:5]:
        link = element.get_attribute("data-href")
        if "eventtype=EQ" in link:
            # Earthquake
            driver.get(link)
            lat_lon = driver.find_elements_by_css_selector("td + td.cell_value_summary")[3].get_attribute("innerText")
            time = driver.find_elements_by_css_selector("td + td.cell_value_summary")[4].get_attribute("innerText")
        elif "eventtype=FL" in link:
            # Flood
            driver.get(link)
            
        elif "eventtype=TC" in link:
            # Hurricane
            driver.get(link)