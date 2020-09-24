from selenium import webdriver

url = 'https://hand.nandcloud.cn/#/login'
broswer = 'firefox'

def getDriver():
    if (broswer == 'chrome'):
        driver = webdriver.Chrome()
    elif (broswer == 'firefox'):
        driver = webdriver.Firefox()
    elif (broswer == 'ie'):
        driver = webdriver.Ie()
    else:
        driver = webdriver.Edge()
    return driver

