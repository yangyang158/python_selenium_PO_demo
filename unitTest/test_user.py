import sys
sys.path.append("..")
import os
import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from ddt import ddt, data, unpack, file_data
from pages.user_page import UserPage
from datas.login_data import login_success_data
from base.utils import getYamlData
from driver import getDriver, url

current_path = os.getcwd()
yaml_path = os.path.join(current_path, "../datas/user_data.yml")
addUserData = getYamlData(yaml_path)['addUserData']

@ddt
class TestUserPage(unittest.TestCase):
    total = 0

    @classmethod
    def setUpClass(cls):
        driver = getDriver()
        p1 = UserPage(driver, url)
        p1.openBroswer()
        p1.operateLogin(login_success_data['account'], login_success_data['psw'])
        cls.p1 = p1

    @classmethod
    def tearDownClass(cls):
        cls.p1.quit()

    def test_1_showUserPage(self):
        '''测试正确打开用户管理页面'''
        if self.p1.isElementExist(self.p1.userMenuEle):
            self.p1.clickUserMenu()
            self.p1.assertNavigateToUserPage()
            self.p1.clickUserMenu()
            TestUserPage.total = self.p1.getElementText(self.p1.totalEle)
    
    @data(*addUserData)
    @unpack
    def test_2_addUser(self, username, phone, status, msg, desc):
        '''测试新增用户: {desc}'''
        sleep(1)
        self.p1.operateAdd(username, phone)
        sleep(1)
        if status == 0:
            self.assertEqual(msg, self.p1.getElementText(self.p1.lintEle))
            self.p1.clickCancelBtn()
        else:
            currentTotal = self.p1.getElementText(self.p1.totalEle)
            self.assertNotEqual(currentTotal, TestUserPage.total, msg='新增失败')


if __name__ == '__main__':
    unittest.main()