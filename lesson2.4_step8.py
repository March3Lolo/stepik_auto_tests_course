from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
import os 

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # ждем пока цена упадет до 100
    wait = WebDriverWait(browser, 12)
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h5#price"), "100"))

    # заказываем 
    button = browser.find_element(By.CSS_SELECTOR, "#book")
    button.click()

    # старый код, котоырй находит икс, считает уравнение и вписывает ответ
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