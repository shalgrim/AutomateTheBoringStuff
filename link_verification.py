"""
From page 263
Write a program that, given the URL of a web page will attempt to down-
load every linked page on the page. The program should flag any pages
that have a 404 "Not Found" status code and print them out as broken links.
"""

import bs4
import logging
import requests

URL = r'http://www.warnerbros.com/archive/spacejam/movie/jam.htm'
logger = logging.getLogger('automate_boring.image_site_downloader')

if  __name__ == '__main__':
    res = requests.get(URL)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    link_elems = soup.select('.r a')

    # TODO: go through all the link elems and download while printing not founds
#    for link_elem in link_elems:



