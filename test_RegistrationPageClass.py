import pytest

'''install selenium, pytest, pytest-html'''
'''to run file use ==> pytest -v -s --html=report.html'''

@pytest.mark.usefixtures('setup')
class Test_End2EndPage:
    # @pytest.mark.usefixtures
    '''This can be used if in method parameter writing setup has to avoid'''
    @pytest.mark.skip
    def test_registrationPage(self):
        first_name = "testFirst12"
        last_name = "testLast12"
        email_id = first_name + last_name + "@gmail.com"
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
        print("*" * 20 + "SUCCESSFUL" + "*" * 20)

    @pytest.mark.parametrize("email, password", [
        ("testFirst1testLast1@gmail.com", "Password@123"),
        ("testFirst2testLast2@gmail.com", "Password@123"),
        ("testFirst3testLast3@gmail.com", "Password@123")
    ])
    def test_loginPage(self, email, password):
        self.driver.find_element_by_css_selector("a[title='My Account']").click()
        self.driver.find_element_by_link_text('Login').click()
        self.driver.find_element_by_id("input-email").send_keys(email)
        self.driver.find_element_by_id("input-password").send_keys(password)
        self.driver.find_element_by_css_selector("input[value='Login']").click()
        actual_text = self.driver.find_element_by_xpath("//*[@id='content']/h2[1]").text
        assert actual_text == 'My Account'
        self.driver.find_element_by_css_selector("a[title='My Account']").click()
        self.driver.find_element_by_link_text("Logout").click()

    @pytest.mark.skip
    def test_logout(self):
        pass

#To run
#pytest -s -v .\test_RegistrationPageClass.py
#
