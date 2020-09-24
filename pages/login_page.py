import sys
sys.path.append("..")
from selenium import webdriver
from selenium.webdriver.common.by import By
from base.base_page import BasePage

class LoginPage(BasePage):
    
    # 手机号元素
    phoneEle = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div[1]/div[2]/input')
    # 密码元素
    pswEle = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div[2]/div[2]/input')
    # 切换登录方式元素
    toggleEle = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div[3]/span[3]')
    # 登录按钮元素
    loginBtnEle = (By.CSS_SELECTOR, '.btn-font')
    # 主页面元素
    homeEle = (By.CSS_SELECTOR, '.layout-header')

    # 手机号密码登录操作
    def enterAccount(self, account, psw):
        self.locateElement(self.phoneEle).send_keys(account)
        self.togglePhonePswLogin()
        self.locateElement(self.pswEle).send_keys(psw)
        self.locateElement(self.loginBtnEle).click()

    # 执行操作
    def operateLogin(self, account, psw):
        self.enterAccount(account, psw)

    # 切换为手机号密码登录
    def togglePhonePswLogin(self):
        self.locateElement(self.toggleEle).click()

# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     url = 'https://hand.nandcloud.cn/#/login'
#     p1 = LoginPage(driver, url)
#     p1.operate()