import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import webdriver
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
from selenium.webdriver.common.by import By

class Test_a() :
    def test_google(self):
        from selenium import webdriver
        google = webdriver.Chrome()
        google.get("https://www.google.com/")
        logo = google.find_element(By.XPATH,"//img[@alt='Google']").is_displayed()
        if logo == True:
            assert True
            print("yes i am on google home page")
        else:
            assert False
        google.implicitly_wait(5)

    @pytest.mark.xfail
    def test_sum_001(self):
        a=3
        b=5
        sum= a+b
        print(sum)
        if sum == 8:
            print("test_sum_001 is passed")
            assert True
        else:
            print("test_sum_001 is Failed ")
            assert False

    @pytest.mark.skip
    def test_mul_002(self):
        a = 3
        b= 5
        mul= a*b
        print(mul)
        if mul  == 16:
            print("test_mul_002 is passed")
            assert True
        else:
            print("test_mul_002 is Failed")
            assert False

    def sum_003(self):  # this item/function will not consider as testcase because of name
        a = 3
        b = 5
        sum = a + b
        print(sum)

        if sum == 16:
            print("test_mul_002 is Passed")
            assert True
        else:
            print("test_mul_002 is Failed")
            assert False

