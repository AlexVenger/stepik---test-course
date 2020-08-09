from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

link = 'http://suninjuly.github.io/selects1.html'
browser = webdriver.Chrome()
try:
    browser.get(link)
    value1 = browser.find_element_by_id('num1').text
    value2 = browser.find_element_by_id('num2').text
    value = int(value1) + int(value2)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(value))
    button = browser.find_element_by_css_selector('button.btn')
    button.click()
finally:
    time.sleep(10)
    browser.quit()
