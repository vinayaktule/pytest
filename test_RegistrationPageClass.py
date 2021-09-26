'''install selenium, pytest, pytest-html'''
'''to run file use ==> pytest -v -s --html=report.html'''

import pytest

@pytest.mark.usefixtures("setup")
class test_RegistrationPage:
    #@pytest.mark.usefixtures
    '''This can be used if in method parameter writing setup has to avoid'''
    def test_registrationPage(self):
        first_name = "testFirst9"
        last_name = "testLast9"
        email_id = first_name+last_name+"@gmail.com"
        telephone = "9999999999"
        password = "Password@123"
        confirm_password = password

        self.driver.find_element_by_css_selector("a[title='My Account']").click()
        self.driver.find_element_by_link_text("Register").click()

        self.driver.find_element_by_id("input-firstname").send_keys(first_name)
        self.driver.find_element_by_id("input-lastname").send_keys(last_name)
        self.driver.find_element_by_id("input-email").send_keys(email_id)
        self.driver.find_element_by_id("input-telephone").send_keys(telephone)
        self.driver.find_element_by_id("input-password").send_keys(password)
        self.driver.find_element_by_id("input-confirm").send_keys(confirm_password)
        self.driver.find_element_by_name("agree").click()
        self.driver.find_element_by_xpath("//input[@type='submit']").click()

        msg = self.driver.find_element_by_xpath("//*[@id='content']/h1").text
        assert_msg = "Your Account Has Been Created!"

        assert msg == assert_msg, "FAILED"
        print()
        print("*"*20+"SUCCESSFUL"+"*"*20)


    @pytest.mark.sanity
    def test_loginPage(self):
        pass

    '''test skip in pytest'''
    @pytest.mark.skip
    def test_skip(self):
        assert True

    '''Test xfail in pytest'''
    @pytest.mark.xfail
    def test_xfail(self):
        assert False

