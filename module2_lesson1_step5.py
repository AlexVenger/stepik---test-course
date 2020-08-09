import math
from selenium import webdriver
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = 'http://suninjuly.github.io/math.html'
browser = webdriver.Chrome()
try:
    browser.get(link)
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    y_element = browser.find_element_by_id("answer")
    y_element.send_keys(str(y))
    check = browser.find_element_by_css_selector('label[for="robotCheckbox"]')
    check.click()
    radio = browser.find_element_by_css_selector('label[for="robotsRule"]')
    radio.click()
    button = browser.find_element_by_css_selector('button.btn')
    button.click()
finally:
    time.sleep(10)
    browser.quit()
