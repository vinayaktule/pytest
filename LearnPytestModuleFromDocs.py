import pytest

@pytest.fixture(scope='class')
def setup():
    print("\n===================Using fixture===================")

def fun_increament(x):
    return x+1

@pytest.mark.sanity
def test_fun1_increament(setup):
    assert fun_increament(3) == 4

class Test_group:
    def test_fun2_increament(self):
        assert fun_increament(2) == 3

    @pytest.mark.skip
    def test_fun3_increament(self):
        assert fun_increament(3) == 4

    @pytest.mark.sanity
    def test_fun4_increament(self):
        assert fun_increament(4) == 5

    @pytest.mark.regression
    def test_fun5_increament(self):
        assert fun_increament(5) == 6

    @pytest.mark.xfail
    def test_fun6_increament(self):
        assert fun_increament(6) == 7

    @pytest.mark.xfail
    def test_fun7_increament(self):
        assert fun_increament(7) == 7

    @pytest.mark.parametrize("a, b, expected", [
        (2, 3, 5),
        (4, 4, 8),
        (5, 6, 10)  #"""This will be failed"""
    ])
    def test_add(self, a, b, expected):
        assert a+b == expected

#To run the above code use below commands in pycharm terminal
#pytest .\LearnPytestModuleFromDocs.py                # Plain run
#pytest -k test_add .\LearnPytestModuleFromDocs.py    # particular test/module from test
#pytest -v .\LearnPytestModuleFromDocs.py             # with verbose
#pytest -s .\LearnPytestModuleFromDocs.py             # with result per test
#pytest -m pytest .\LearnPytestModuleFromDocs.py      # using python marker
#pytest -m regression .\LearnPytestModuleFromDocs.py  # using marker as regression from pytest