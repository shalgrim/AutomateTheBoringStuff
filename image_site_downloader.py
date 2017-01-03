"""
From page 263
Write a program that goes to a photo-sharing site like Flickr or Imgur, searches for a category of photos, and then
downloads all the resulting images. You could write a program that works with any photo site that has a search feature.
"""

import logging
import os
import requests
import sys
from selenium import webdriver
from selenium.common import exceptions as selenium_exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

DELAY_SEC = 10
IMAGE_DIR = r'.\out\downloaded_images'
logger = logging.getLogger('automate_boring.image_site_downloader')

if __name__ == '__main__':
    os.makedirs(IMAGE_DIR, exist_ok=True)
    url = sys.argv[1]
    search_term = ' '.join(sys.argv[2:])

    browser = webdriver.Firefox()
    browser.get('https://{}'.format(url))

    search_elem = browser.find_element_by_css_selector('#search_query')
    search_elem.send_keys(search_term)
    search_elem.submit()

    try:
        pic_elems = browser.find_elements_by_css_selector('img.photo')
        # article.is_photo:nth-child(2) > section:nth-child(1) > div:nth-child(1) > img:nth-child(1)
        # element_present = expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.z0'))
        # WebDriverWait(browser, DELAY_SEC).until(element_present)
    except selenium_exceptions.TimeoutException:
        msg = 'Failed to find any images'
        logger.info(msg)
        raise

    for pic in pic_elems:
        pic_url = pic.get_attribute('src')

        try:
            res = requests.get(pic_url)
        except requests.exceptions.InvalidSchema as e:
            logger.error(repr(e))
            continue

        res.raise_for_status()

        with open(os.path.join(IMAGE_DIR, 'CHANGEME.jpg'), 'wb') as f:
            for chunk in res.iter_content(100000): # TODO: upgrade to python 3.6 for 100_000
                f.write(chunk)




