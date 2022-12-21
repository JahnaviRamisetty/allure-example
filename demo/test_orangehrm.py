from selenium import webdriver
import pytest
import allure
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# @allure.severity(allure.severity_level.NORMAL)
# class Attachment_Type:
#     pass


@allure.severity(allure.severity_level.NORMAL)
class TestHRM:

    @allure.severity(allure.severity_level.MINOR)
    def test_Logo(self):

        driver = webdriver.Chrome(ChromeDriverManager().install())
        # self.driver=webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")
        driver.get("https://opensource-demo.orangehrmlive.com/")
        status=driver.find_element(By.XPATH,"//*[@id='divLogo']/img").is_displayed()
        if status==True:
            assert True
        else:
            assert  False
            driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    def test_listemployees(self):
        pytest.skip('skipping test')

    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # self.driver=webdriver.Chrome(executable_path="C:\chromedriver_win32\chromedriver.exe")
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element(By.ID,"txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID,"txtPassword").send_keys("admin123")
        self.driver.find_element(By.ID,"btnLogin").click()
        act_title=self.driver.title

        if act_title=="OrangeHRM":
            self.driver.close()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Testcase01 title",attachment_type=AttachmentType.PNG)
            # allure.attach(self.driver.get_screenshot_as_png(),name="testloginscreen",attachment_type=Attachment_Type.PNG)
            self.driver.close()
            assert False
