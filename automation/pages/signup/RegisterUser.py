from automation.pages.signup import locators
from src.data.data import RegisterData
import clusters


class RegisterUser:
    def __init__(self,page):
        self.page = page 
       
    def verify_home_page_visible(self) -> str:
        '''Returns home page URL'''
        self.page.goto(clusters.URL)
        return clusters.URL
    
    def verify_new_user_signup_visible(self) -> str:
        '''Returns New User SignUp text'''
        self.page.locator(locators.RegisterUser.SIGNUPLOGIN).click()
        return self.page.get_by_text(locators.RegisterUser.NEWUSERSIGNUP)

    def enter_account_info_visible(self) -> str:
        '''
        Returns Enter account information string.
        
        Fields:
        name(str): The first field.
        email_address(str): The second field

        Returns:
        str: The name and email_address are valid after signup btn click then it returns a string.
        
        '''
        self.page.get_by_placeholder(locators.RegisterUser.NAME).fill(RegisterData.name)
        self.page.locator(locators.RegisterUser.SIGNUPEMAIL).fill(RegisterData.email_address)
        self.page.locator(locators.RegisterUser.SIGNUPBUTTON).click()
        return self.page.get_by_text(locators.RegisterUser.ENTERACCOUNTINFORMATION)
    
    def enter_acc_info(self):
        '''Check gender,newsletter, offers and  fill password.'''
        self.page.locator(locators.RegisterUser.DETAILS.format("id_gender1")).check()
        self.page.locator(locators.RegisterUser.DETAILS.format("password")).fill(RegisterData.password)
        self.page.locator(locators.RegisterUser.DETAILS.format("newsletter")).check()
        self.page.locator(locators.RegisterUser.DETAILS.format("optin")).check()
        
    
    def verify_acc_created_success(self):
        '''
        Returns Account Created String.

        Fields:
        first_name(str): The first field.
        last_name(str): The second field.
        address(str): The fourth field.
        state(str): The seventh field.
        city(str): The eigth field.
        mobile_number(str): The nineth field
        
        Returns:
        Fills all the required fields and then upon button click, returns sccount created string.
        '''
        self.page.locator(locators.RegisterUser.DETAILS.format("first_name")).fill(RegisterData.first_name)
        self.page.locator(locators.RegisterUser.DETAILS.format("last_name")).fill(RegisterData.last_name)
        self.page.locator(locators.RegisterUser.DETAILS.format("address1")).fill(RegisterData.address)
        self.page.locator(locators.RegisterUser.DETAILS.format("state")).fill(RegisterData.state)
        self.page.locator(locators.RegisterUser.DETAILS.format("city")).fill(RegisterData.city)
        self.page.locator(locators.RegisterUser.DETAILS.format("zipcode")).fill(RegisterData.zip_code)
        self.page.locator(locators.RegisterUser.DETAILS.format("mobile_number"))\
           .fill(RegisterData.mobile_number)
        self.page.locator(locators.RegisterUser.CREATEACCOUNT).click()
        return  self.page.get_by_text(locators.RegisterUser.ACCOUNTCREATED)
       
    
    def verify_logged_in(self):
        '''Verify user logged-in'''
        self.page.locator(locators.RegisterUser.CONTINUEBUTTON).click()
        return self.page.locator(locators.RegisterUser.LOGGEDIN)
    
    def verify_acc_deleted(self):
        '''Verify acc deleted'''
        self.page.locator(locators.RegisterUser.DELETEACCOUNT).click()
        return self.page.locator(locators.RegisterUser.ACCOUNTDELETED)
    
    def continue_page(self):
        self.page.locator(locators.RegisterUser.CONTINUEBUTTON).click()
                         
        
        
    




        
        


