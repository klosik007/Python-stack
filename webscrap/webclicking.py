from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#browser = webdriver.Firefox()
#browser.get('http://inventwithpython.com')

browser = webdriver.Firefox()
browser.get('http://stackoverflow.com')

try:
    elem = browser.find_element_by_class_name('bookcover')
    print('Found <%s> element with that class name!' % (elem.tag_name))
    linkElem = browser.find_element_by_link_text('Read It Online')
    linkElem.click()
    emailElem = browser.find_element_by_id('identifierId')
    emailElem.send_keys('pklos1992@gmail.com')
    htmlElem = browser.find_element_by_tag_name('html')
    htmlElem.send_keys(Keys.END)
    nextButton = browser.find_element_by_class_name('ZFr60d CeoRYc')
    nextButton.click()

    passElem = browser.find_element_by_name('password')
    passElem.send_keys('haslo')
    passElem.emailElem.submit()
except:
    print('Was not able to find an element with that name.')

#<input class="whsOnd zHQkBf" jsname="YPqjbf" autocomplete="current-password" spellcheck="false" tabindex="0" aria-label="Wpisz hasło" name="password" autocapitalize="off" autocorrect="off" dir="ltr" data-initial-dir="ltr" data-initial-value="" type="password">
#<div class="ZFr60d CeoRYc"></div>