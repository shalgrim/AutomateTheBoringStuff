"""
From page 263
2048 is a simple game where you combine tiles by sliding them up, down,
left, or right with the arrow keys. You can actually get a fairly high score
by repeatedly sliding in an up, right, down, and left pattern over and over
again. Write a program that will open the game at https://gabrielecirulli
.github.io/2048/ and keep sending up, right, down, and left keystrokes to
automatically play the game.
"""

import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

URL = r'https://gabrielecirulli.github.io/2048/'
KEYSTROKES = [Keys.ARROW_UP, Keys.ARROW_RIGHT, Keys.ARROW_DOWN, Keys.ARROW_LEFT]

logger = logging.getLogger('automate_boring.image_site_downloader')

if __name__ == '__main__':
    browser = webdriver.Firefox()
    browser.get(URL)

    game_over = False
    game_elem = ?


    while not game_over:
        game_elem.send_keys(KEYSTROKES[0])
        KEYSTROKES = KEYSTROKES[1:] + KEYSTROKES[:1]

        # game over selector: body > div > div.game-container > div.game-message.game-over
