import time
import pytest
from selenium.webdriver.common.by import By


class TestLogin:

    @pytest.mark.dependency(name='login')
    def test_navigate(self, driver):
        driver.get('https://app.vwo.com')
        time.sleep(1)
        assert driver.title == 'Login - VWO', 'Failed to navigate to app.vwo.com'

    @pytest.mark.dependency(depends=['login'])
    def test_login_invalid(self,driver):
        element = driver.find_element(By.ID, 'login-username')
        element.send_keys('admin')
        element = driver.find_element(By.ID, 'login-password')
        element.send_keys('admin')
        element = driver.find_element(By.ID, 'js-login-btn')
        element.click()
        time.sleep(5)
        element = driver.find_element(By.ID, 'js-notification-box-msg')
        assert element.is_displayed(), 'Invalid credential message is not displayed'

    @pytest.mark.dependency(depends=['login'])
    def test_login_passed(self, driver):
        element = driver.find_element(By.ID, 'login-username')
        element.clear()
        element.send_keys('contact+atb5x@thetestingacademy.com')
        element = driver.find_element(By.ID, 'login-password')
        element.clear()
        element.send_keys('ATBx@1234')
        element = driver.find_element(By.ID, 'js-login-btn')
        element.click()
        time.sleep(10)
        element = driver.find_element(By.XPATH, '//p[@data-qa = "page-sub-title"]/span')
        assert element.is_displayed(), 'Welcome message is not displayed'
