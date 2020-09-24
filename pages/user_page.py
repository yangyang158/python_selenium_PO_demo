import sys
sys.path.append("..")
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

class UserPage(LoginPage):
    
    # 新增按钮元素
    addBtnEle = (By.CSS_SELECTOR, '.operate .ant-btn')
    # 姓名输入框元素
    usernameEle = (By.XPATH, '//*[@id="username"]')
    # 手机号输入框元素
    phoneInputEle = (By.XPATH, '//*[@id="telephone"]')
    # 角色选择框元素
    roleEle = (By.XPATH, '//*[@id="roleIds"]')
    # 下拉框选项
    option1 = (By.CSS_SELECTOR, '.ant-select-dropdown-menu-item')
    # 保存按钮元素
    saveBtnEle = (By.CSS_SELECTOR, '.ant-modal-footer .ant-btn-primary')
    # 取消按钮元素
    cancelBtnEle = (By.CSS_SELECTOR, '.ant-modal-content .ant-modal-close-x')
    # 用户管理菜单元素
    userMenuEle = (By.XPATH, '//*[@id="root"]/div/div[2]/aside/div/ul/li[4]/a')
    # 表单校验提示元素
    lintEle = (By.CSS_SELECTOR, '.ant-form-explain')
    # 弹框提示元素
    alertEle = (By.XPATH, '/html/body/div[4]/div/span/div/div/div/span[2]')
    # 分页总数
    totalEle = (By.CSS_SELECTOR, '.ant-pagination-total-text')
    # 用户管理页面url
    userPageUrl = 'system/user-manage'

    # 点击用户管理菜单
    def clickUserMenu(self):
        self.locateElement(self.userMenuEle).click()

    # 选择角色
    def selectRole(self):
        self.locateElement(self.roleEle).click()
        self.locateElement(self.option1).click()

    # 新增功能
    def addUser(self, userName, phone):
        self.locateElement(self.addBtnEle).click()
        self.locateElement(self.usernameEle).send_keys(userName)
        self.locateElement(self.phoneInputEle).send_keys(phone)
        self.selectRole()
        self.locateElement(self.saveBtnEle).click()

    # 执行操作
    def operateAdd(self, userName, phone):
        self.addUser(userName, phone)

    # 点击弹框的取消按钮
    def clickCancelBtn(self):
        self.locateElement(self.cancelBtnEle).click()

    # 判断用户管理页面url
    def assertNavigateToUserPage(self):
        self.isCurrentPageUrl(self.userPageUrl)