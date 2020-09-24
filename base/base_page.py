from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BasePage(object):
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    # 定位元素
    def locateElement(self, locator):
        return self.driver.find_element(*locator)

    # 定位元素
    # def locateElement(self, locator):
    #     return self.findElement(locator)

    # 查找页面的某个元素
    def findElement(self, locator, timeout = 10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator),
            message = f"Unable to locate the element: {locator} after {timeout} seconds.")

    # 判断页面的某个元素是否可点击
    def isElementClick(self, locator, timeout = 10):
        return self.findElement(locator, timeout).is_enabled()

    # 判断页面是否存在某个元素, timeout:单位秒
    def isElementExist(self, locator, timeout = 10):
        try:
            self.findElement(locator, timeout)
            return True
        except:
            return False

    # 检查在当前页面的url是否是指定的url
    def isCurrentPageUrl(self, url):
        assert url in self.driver.current_url

    # 获取标签元素的文本值
    def getElementText(self, locator):
        return self.findElement(locator).text

    def openBroswer(self):
        # self.driver.maximize_window()
        self.driver.get(self.url)
    
    def quit(self):
        sleep(2)
        self.driver.quit()