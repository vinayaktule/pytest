import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

test_url = "http://tutorialsninja.com/demo"

@pytest.fixture(scope='class')
def setup(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get(test_url)
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.quit()
