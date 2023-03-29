from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

url = "https://bepick.net/#/game/default/nlotto_power"

driver = webdriver.Chrome()
driver.get(url)

wait = WebDriverWait(driver, 10)

element = wait.until(
        EC.frame_to_be_available_and_switch_to_it((By.ID, "contentFrame"))
    )



while True:
    # try:
    Category_Body = wait.until(EC.visibility_of_element_located((By.ID,"dt_more")))
    counter = counter + 1
    if counter <= 10:
        driver.implicitly_wait(2)
        Category_Body.click()
    else:
            break    
    # except:
    #     print("Reached bottom of page")
    #     break

soup = BeautifulSoup(driver.page_source,'lxml')

with open("logic.html", mode="w") as code:
        code.write((soup.prettify().encode("utf-8")))


