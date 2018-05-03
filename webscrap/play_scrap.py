from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

#specify a browser we'll use
browser = webdriver.Firefox()
browser.get('https://logowanie.play.pl/opensso/logowanie')
#get username and password elements by id or name, then log in
try:
    user_name = browser.find_element_by_name('IDToken1')
    user_name.send_keys('pklos1992@gmail.com')

    password = browser.find_element_by_name('IDToken2')
    password.send_keys('wtf007klos')

    login_click = browser.find_element_by_name('Login.Submit')
    login_click.click()
except Exception as exc:
    print('Was not able to log in! %s' % exc)

try:
    #wait 'till log in is completed
    #wait = WebDriverWait(browser, 15)
    browser.get('https://24.play.pl/')
    browser.get('https://24.play.pl/Play24/Billing')
    radio_from = browser.find_element_by_id('from')
    radio_from.send_keys('01.01.2016')


except Exception as exc:
    print('Was not able to log in! %s' % exc)



