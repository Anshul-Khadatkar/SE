from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

try:
    # Open YouTube
    driver.get("https://www.youtube.com")

    # Wait for the page to load
    time.sleep(3)

    # Locate the search input field
    search_box = driver.find_element(By.NAME, "search_query")

    # Enter the search term and press Enter
    search_box.send_keys("vct champion")
    search_box.send_keys(Keys.RETURN)

    # Wait for search results to load
    time.sleep(5)

finally:
    # Close the browser
    driver.quit()