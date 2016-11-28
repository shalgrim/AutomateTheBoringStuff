from selenium import webdriver

if __name__ == '__main__':
    browser = webdriver.Firefox()
    type(browser)
    browser.get('http://inventwithpython.com')
