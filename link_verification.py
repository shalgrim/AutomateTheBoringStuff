"""
From page 263
Write a program that, given the URL of a web page will attempt to down-
load every linked page on the page. The program should flag any pages
that have a 404 "Not Found" status code and print them out as broken links.
"""

import bs4
import logging
import os
import requests

URL = r'http://www.warnerbros.com/archive/spacejam/movie/'
logger = logging.getLogger('automate_boring.image_site_downloader')

if __name__ == '__main__':

    os.makedirs('links', exist_ok=True)

    res = requests.get(URL)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    link_elems = soup.select('a')

    for link_elem in link_elems:
        link_url = link_elem.get('href')
        if link_url[:4] != 'http':
            link_url = URL + link_url       # relative link
        link_res = requests.get(link_url)

        try:
            link_res.raise_for_status()
        except requests.exceptions.HTTPError as e:
            if link_res.status_code == 404:
                print('broken link {}'.format(link_url))
            else:
                raise

        basename = os.path.basename(link_url)

        if basename:
            basename = basename.replace('?', '')
            with open(os.path.join('links', basename), 'wb') as f:
                for chunk in link_res.iter_content(100000):
                    f.write(chunk)




