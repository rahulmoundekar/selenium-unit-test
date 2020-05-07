import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import HTMLTestRunner

CHROME_DRIVER_PATH = 'E:\OnlyForPython\SELENIUM\drivers\chromedriver_win32\chromedriver.exe'


class orange_hrm(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

    def test_login(self):
        self.driver.find_element(By.XPATH, "//input[@id='txtUsername']").send_keys('admin')
        self.driver.find_element_by_xpath("//input[@id='txtPassword']").send_keys('admin123')
        self.driver.find_element(By.XPATH, "//input[@id='btnLogin']").click()


        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(self.driver.find_element(By.XPATH, "//a[@id='menu_leave_viewLeaveModule']")).perform()
        action_chains.move_to_element(self.driver.find_element(By.XPATH, "//a[@id='menu_leave_Reports']")).perform()

        self.driver.find_element(By.ID, "menu_leave_viewLeaveBalanceReport").click()

        select = Select(self.driver.find_element_by_id('leave_balance_report_type'))
        select.select_by_visible_text("Employee")

        self.driver.find_element_by_id("leave_balance_employee_empName").send_keys("Rahul")
        self.driver.find_element_by_id("viewBtn").click()

        self.driver.find_element(By.XPATH, "//a[@id='welcome']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'Logout')]").click()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    HTMLTestRunner.main()
#
# Now open terminal and fire below command
# python scriptFileName.py > TestReport.HTML