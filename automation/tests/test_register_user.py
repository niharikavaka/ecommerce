from playwright.sync_api import Page
from playwright.sync_api import expect 
import time 
from automation.pages.signup.RegisterUser import RegisterUser
# from src.pages.signup.RegisterUser import RegisterUser

class TestRegisterUser:
    def test_register_user(self,page:Page):
        register_user = RegisterUser(page)
        home_page_visible = register_user.verify_home_page_visible()
        expect(page).to_have_url(home_page_visible)
        new_user_signup_visible = register_user.verify_new_user_signup_visible()
        expect(new_user_signup_visible).to_be_visible()
        acc_info_visible = register_user.enter_account_info_visible()
        expect(acc_info_visible).to_be_visible()
        register_user.enter_acc_info()  
        acc_created_success = register_user.verify_acc_created_success()
        expect(acc_created_success).to_be_visible()
        logged_in = register_user.verify_logged_in()
        expect(logged_in).to_be_visible()
        acc_deleted = register_user.verify_acc_deleted()
        expect(acc_deleted).to_be_visible()
        register_user.continue_page()
        print("Niha")


        
    # def test_1(self,page:Page):
    #      register_user = RegisterUser(page)
    #      acc_info_visible = register_user.enter_account_info_visible()
    #      expect(acc_info_visible).to_be_visible()

    # def test_12(self,page:Page):
    #      register_user = RegisterUser(page)
    #      acc_deleted = register_user.verify_acc_deleted()
    #      expect(acc_deleted).to_be_visible()
        

    # def test_2(self,page:Page):
    #      register_user = RegisterUser(page)
    #      acc_info_visible = register_user.enter_account_info_visible()
        #  expect(acc_info_visible).to_be_visible()


   



    # time.sleep(40)
