from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()
driver.get('http://www.python.org')

assert 'Python' in driver.title

elem = driver.find_element_by_name('q')
elem.clear()

elem.send_keys('pycon')
elem.send_keys(Keys.RETURN)

assert 'No results found.' not in driver.page_source

element = driver.find_element_by_xpath("//select[@name='name']")
all_options = element.find_element_by_tag_name("option")
for option in all_options:
    pass


driver.close()

