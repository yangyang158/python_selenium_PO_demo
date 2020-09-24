import sys
sys.path.append("..")
import unittest
from datas.login_data import login_success_data, login_wrong_data
from selenium import webdriver
from time import sleep
from ddt import ddt, data, unpack
from pages.login_page import LoginPage
from driver import getDriver, url

@ddt
class TestLoginPage(unittest.TestCase):
    def setUp(self):
        driver = getDriver()
        self.p1 = LoginPage(driver, url)
        self.p1.openBroswer()

    def tearDown(self):
        self.p1.quit()

    def test_1_phoneLogin(self):
        '''手机号密码正常登录的情况'''
        self.p1.operateLogin(login_success_data['account'], login_success_data['psw'])
        self.assertTrue(self.p1.isElementExist(self.p1.homeEle), msg='登录后跳转页面失败')

    # @data(*login_wrong_data)
    # @unpack
    # def test_1_phoneLogin_exception(self, account, psw, check, desc):
    #     '''手机号密码登录的异常情况：{desc}'''
    #     self.p1.operateLogin(account, psw)
    #     self.assertGreater(self.p1.driver.page_source.find(check), -1)
    #     sleep(1)

if __name__ == '__main__':
    unittest.main()