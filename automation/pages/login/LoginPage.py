import clusters
from pages.login import locators


class LoginPage:
    def __init__(self,page):
        self.page = page 
       
    def verify_home_page_visible(self) -> str:
        '''Returns home page URL'''
        self.page.goto(clusters.URL)
        return clusters.URL
    
    def verify_new_user_signup_visible(self) -> str:
        '''Returns New User SignUp text'''
        self.page.locator(clusters.SIGNUPLOGIN).click()
        return self.page.get_by_text(locators.LoginUser.LOGINTOYOURACCOUNT)
        
