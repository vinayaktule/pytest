import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# test_url = "http://tutorialsninja.com/demo"
# #driver = webdriver.Chrome()
# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.maximize_window()
# driver.get(test_url)
# driver.implicitly_wait(10)

'''test the scope of setup is for whole module'''
@pytest.fixture()
def setup():
    test_url = "http://tutorialsninja.com/demo"
    # driver = webdriver.Chrome()
    global driver
    driver= webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get(test_url)
    driver.implicitly_wait(10)
    yield
    driver.quit()

#@pytest.mark.usefixtures
'''This can be used if in method parameter writing setup has to avoid'''
def test_registrationPage(setup):
    first_name = "testFirst9"
    last_name = "testLast9"
    email_id = first_name+last_name+"@gmail.com"
    telephone = "9999999999"
    password = "Password@123"
    confirm_password = password

    driver.find_element_by_css_selector("a[title='My Account']").click()
    driver.find_element_by_link_text("Register").click()

    driver.find_element_by_id("input-firstname").send_keys(first_name)
    driver.find_element_by_id("input-lastname").send_keys(last_name)
    driver.find_element_by_id("input-email").send_keys(email_id)
    driver.find_element_by_id("input-telephone").send_keys(telephone)
    driver.find_element_by_id("input-password").send_keys(password)
    driver.find_element_by_id("input-confirm").send_keys(confirm_password)
    driver.find_element_by_name("agree").click()
    driver.find_element_by_xpath("//input[@type='submit']").click()

    msg = driver.find_element_by_xpath("//*[@id='content']/h1").text
    assert_msg = "Your Account Has Been Created!"

    assert msg == assert_msg, "FAILED"
    print()
    print("*"*20+"SUCCESSFUL"+"*"*20)

'''test skip in pytest'''
@pytest.mark.skip
def test_loginPage(setup):
    pass

'''Test xfail in pytest'''
@pytest.mark.xfail
def test_xfail(setup):
    assert False
