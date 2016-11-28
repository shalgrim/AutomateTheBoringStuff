#! python3

import sys
import webbrowser
import pyperclip

if __name__ == '__main__':
    if len(sys.argv) > 1:
        # use arguments
        address = ' '.join(sys.argv[1:])
    else:
        # use clipboard
        address = (pyperclip.paste().split())

    webbrowser.open('https://www.google.com/maps/place/{}'.format(address))
