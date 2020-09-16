from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    browser.maximize_window()
##    confirm = browser.switch_to.alert
##    confirm.accept()

    
    price = WebDriverWait(browser, 10).until(
                   EC.text_to_be_present_in_element((By.ID, "price"), '100')
                   )
    book = browser.find_element(By.ID, "book")
    book.click()

#    submit = browser.find_element("#solve")

    element = WebDriverWait(browser, 3).until(
        EC.presence_of_element_located((By.ID, 'solve'))
        )
    x_element = browser.find_element_by_xpath("//*[@id='input_value']")
    x = x_element.text
    y = calc(x)
    text_field = browser.find_element_by_xpath("//*[@name='text']")
    text_field.send_keys(y)
    button = browser.find_element_by_xpath("//button[@type ='submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
