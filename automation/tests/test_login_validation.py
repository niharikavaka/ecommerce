from playwright.sync_api import Page
from playwright.sync_api import expect 
from pages.login.LoginPage import LoginPage
# from pages.signup.RegisterUser import RegisterUser
import time

def test_login_with_correct_email_and_password(page:Page):
     login_page = LoginPage(page)
     home_page_visible = login_page.verify_home_page_visible()
     expect(page).to_have_url(home_page_visible)
     # new_user_signup_visible = login_page.verify_new_user_signup_visible()
     # expect(new_user_signup_visible).to_be_visible()



