from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os 

link = "http://suninjuly.github.io/alert_accept.html"  

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    answer_button = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer_button.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
