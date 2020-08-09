import os
from selenium import webdriver
import time

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
try:
    browser.get(link)
    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("F")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("F")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("F")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    element = browser.find_element_by_id('file')
    file_path = os.path.join(current_dir, 'file.txt')
    element.send_keys(file_path)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(30)
    browser.quit()
