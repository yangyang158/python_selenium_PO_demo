
# 正常场景 - 登录成功
login_success_data = {'account': '15803469205', 'psw': '123456'}
 
# 异常场景 - 账号为空\密码为空
login_wrong_data = [
    {'account': '', 'psw': '123456', 'check':'手机号、密码不能为空', 'desc': '手机号不能为空'},
    {'account': '', 'psw': '', 'check':'手机号、密码不能为空', 'desc': '手机号、密码不能为空'},
    {'account': '15803469205', 'psw':'', 'check':'手机号、密码不能为空', 'desc': '密码不能为空'}
]
 
# 异常场景 - 错误的用户名\错误的密码
login_error_accountOrpsw = [
    {'account': '15803469205', 'psw': '1234567', 'check': '手机号或密码错误'},
    {'account': '15803469523', 'psw': '123456', 'check': '手机号或密码错误'}
]