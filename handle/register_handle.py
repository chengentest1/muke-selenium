from page.register_page import RegisterPage
from util.get_code import GetCode


class RegisterHandle(object):
    def __init__(self,driver):
        self.driver=driver
        self.register_p=RegisterPage(self.driver)
    def send_user_email(self,email):
        self.register_p.get_email_element().send_keys(email)
    def send_user_name(self,name):
        self.register_p.get_username_element().send_keys(name)
    def send_user_password(self,password):
        self.register_p.get_password_element().send_keys(password)
    #输入验证码
    def send_user_code(self,code):
        # get_code_text = GetCode(self.driver)
        # code=get_code_text.code_online(file_name)
        self.register_p.get_code_element().send_keys(code)
    #获取文字
    def get_user_text(self,info,user_info):
        try:
            if info=='email_error':
               text = self.register_p.get_email_error_element().text

            elif info=='name_error':
                text =self.register_p.get_name_error_element().text
            elif info=='password_error':
                text =self.register_p.get_password_error_element().text
            else:
                text =self.register_p.get_code_error_element().text
        except:
            text=None
        return text
    #点击注册按钮
    def click_register_button(self):
        self.register_p.get_button_element().click()

    def get_register_text(self):
        return self.register_p.get_button_element().text
