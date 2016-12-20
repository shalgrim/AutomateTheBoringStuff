"""
From page 263
Write a program that goes to a photo-sharing site like Flickr or Imgur, searches for a category of photos, and then
downloads all the resulting images. You could write a program that works with any photo site that has a search feature.
"""

import logging
import requests
import sys
from selenium import webdriver
from selenium.common import exceptions as selenium_exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

DELAY_SEC = 10
logger = logging.getLogger('automate_boring.image_site_downloader')

if __name__ == '__main__':
    url = sys.argv[1]
    search_term = ' '.join(sys.argv[2:])

    browser = webdriver.Firefox()
    browser.get('https://{}'.format(url))

    search_elem = browser.find_element_by_css_selector('#search_query')
    search_elem.send_keys(search_term)
    search_elem.submit()

    try:
        pic_elems = browser.find_element_by_css_selector('img.photo')
        element_present = expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.z0'))
        WebDriverWait(browser, DELAY_SEC).until(element_present)
    except selenium_exceptions.TimeoutException:
        msg = 'Failed to find any images'
        logger.info(msg)
        raise

    for pic in pic_elems:
        pic_url = 'https://' + pic.get('src')
        res = requests.get(pic_url)
        res.raise_for_status
        # NEXT: save image to file




