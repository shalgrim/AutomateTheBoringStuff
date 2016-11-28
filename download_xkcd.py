#! python3
# downloadXkcd.py

import bs4
import os
import requests

url = 'http://xkcd.com'             # starting url
os.makedirs('xkcd', exist_ok=True)  # store comics in ./xkcd

while not url.endswith('#'):
    # Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Find the URL of the comic image.
    comic_elems = soup.select('#comic img')

    if comic_elems == []:
        print('Could not find comic image.')
    else:
        comic_url = 'http:' + comic_elems[0].get('src')
        # Download the image.
        print('Downloading the image %s...' % (comic_url))
        res = requests.get(comic_url)
        res.raise_for_status()

    # Save the image to ./xkcd.
    with open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb') as \
            image_file:
        for chunk in res.iter_content(100000):
            image_file.write(chunk)

    # Get the Prev button's url.
    # <a rel="prev" href="/1761/" accesskey="p">&lt; Prev</a>
    prev_elems = soup.select('a[rel="prev"]')
    prev_link = prev_elems[0]
    url = 'http://xkcd.com' + prev_link.get('href')

print('Done.')
