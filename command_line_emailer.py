"""
From page 262
Write a program that takes an email address and string of text on the command line and then, using Selenium, logs into
your email account and sends an email of the string to the provided address. (You might want to set up a separate email
account for this program.)
This would be a nice way to add a notification feature to your programs. You could also write a similar program to send
messages from a Facebook or Twitter account.
"""

import logging
import sys
from getpass import getpass
from selenium import webdriver
from selenium.common import exceptions as selenium_exceptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

logger = logging.getLogger('automate_boring.command_line_emailer')
DELAY_SEC = 10

if __name__ == '__main__':
    addy = sys.argv[1]
    msg = sys.argv[2]
    uname = 'shalgrim@gmail.com'
    pwd = getpass('Enter password for {}'.format(uname))

    browser = webdriver.Firefox()
    browser.get('https://gmail.com')

    try:
        uname_elem = browser.find_element_by_id('Email')
        uname_elem.send_keys(uname)
        uname_elem.submit()
    except selenium_exceptions.NoSuchElementException:
        logger.info('Assuming already on password page')

    try:
        element_present = expected_conditions.presence_of_element_located((By.ID, 'Passwd'))
        WebDriverWait(browser, DELAY_SEC).until(element_present)
    except selenium_exceptions.TimeoutException:
        msg = 'Failed to load password field in {} seconds'.format(DELAY_SEC)
        logger.error(msg)
        raise

    pwd_elem = browser.find_element_by_id('Passwd')
    pwd_elem.send_keys(pwd)
    pwd_elem.submit()

    html_elem = browser.find_element_by_tag_name('html')
    html_elem.send_keys('c')

    to_box = browser.find_element_by_css_selector('textarea[name="to"]')
    to_box.send_keys(addy)

    subject_box = browser.find_element_by_css_selector('input[name="subjectbox"]')
    subject_box.send_keys(msg)

    # send email
    buttons = browser.find_elements_by_css_selector('div[role="button"]')
    for button in buttons:
        if button.text == 'Send':
            logger.info('send button id: {}'.format(button.get_attribute('id')))
            button.click()
            break
    else:
        sys.stderr.write('Could not find send button')
        sys.exit(-1)

    profile_button = browser.find_element_by_css_selector('.gb_8a')
    profile_button.click()

    signout_button = browser.find_element_by_id('gb_71')
    signout_button.click()


