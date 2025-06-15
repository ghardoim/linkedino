from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import Safari
from os import getenv

class URLs:
    JOBS = (HOME := "https://www.linkedin.com/") + "my-items/saved-jobs/?cardType=APPLIED"
    INVITATIONS = HOME + "mynetwork/invitation-manager/sent/"
    MESSAGES = HOME + "messaging/?filter=job"
    SEARCH = HOME + "search/results/all"

class Linkedin0(Safari):
    def __init__(self, url:str) -> None:
        super().__init__()

        self.wait = WebDriverWait(self, 10)
        self.action = ActionChains(self)
        self.maximize_window()

        self.get(url)
        self.__login()

    def __login(self) -> None:
        [ self.wait_by(By.ID, field).send_keys(getenv(field.upper())) for field in ("username", "password") ]
        self.clickby_text("Sign in", "button")

        self.wait_by(By.ID, "two-step-challenge").send_keys(input("Enter the code: "))
        self.js_click(self.wait_by(By.ID, "two-step-submit-button"))

    def clickby_text(self, text:str, html_tag:str="button") -> None:
        self.wait_by(By.XPATH, f"//{html_tag}[text()[contains(.,'{text}')]]").click()

    def js_click(self, element:WebElement) -> None: self.execute_script("arguments[0].click()", element)

    def wait_by(self, *locator:tuple) -> WebElement:
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    def wait_not(self, *locator:tuple) -> bool:
        return self.wait.until_not(EC.visibility_of_element_located(locator))

    def findby_classname(self, classname:str) -> WebElement:
        return self.wait_by(By.CLASS_NAME, classname)

    def findby_xpath(self, xpath:str) -> WebElement:
        return self.wait_by(By.XPATH, xpath)

    def clear(self, input) -> None:
        self.action.double_click(input).double_click().send_keys(Keys.DELETE).perform()

    def logout(self) -> None:
        self.close()
        self.quit()