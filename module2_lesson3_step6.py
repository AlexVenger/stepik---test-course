from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(x))))


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
try:
    browser.get(link)
    first_button = browser.find_element_by_class_name('trollface')
    first_button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = browser.find_element_by_id('input_value').text
    y = calc(int(x))
    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)
    button = browser.find_element_by_class_name('btn')
    button.click()
finally:
    time.sleep(10)
    browser.quit()
