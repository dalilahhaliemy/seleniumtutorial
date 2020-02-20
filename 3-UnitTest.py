import unittest
from selenium import webdriver


class SearchEnginesTest(unittest.TestCase):     # inherit TestCase class

    def test_Google(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\Diyanah\Downloads\chromedriver_win32\chromedriver.exe")
        self.driver.get("https://www.google.com/")
        print("Title of the page is : " + self.driver.title)

    def test_Bing(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\Diyanah\Downloads\chromedriver_win32\chromedriver.exe")
        self.driver.get("https://www.bing.com/")
        print("Title of the page is : " + self.driver.title)


if __name__=="__main__":
    unittest.main()


## TYPES OF METHODS 

# SETUP method
# - will be executed every time BEFORE the subsequent test method is executed

# TEARDOWN method
# - executed AFTER the completion of every test method in the class

# SETUP CLASS
# - executed 1 time before ALL method is executed

# TEARDOWN CLASS
# - executed 1 time after ALL method is executed

# SETUP MODULE
# - executed before module
# - need to define before the class definition

# TEARDOWN MODULE
# - executed after module
# - need to define before the class definition


import unittest


def setUpModule():                # before the class
    print("setUpModule")

def tearDownModule():                # after the class
    print("tearDownModule")


class AppTesting(unittest.TestCase):

    @classmethod        # meaning this apply to the class function
    def setUp(self):                    # this will run first before all the following method being executed
        print("This is login test")

    @classmethod                        # this will run after completion of every class method
    def tearDown(self):
        print("This is logout test")

    @classmethod                        # executed 1 time, before run all the method
    def setUpClass(cls):
        print("Open Application")

    @classmethod
    def tearDownClass(cls):             # executed 1 time, after all method has been executed
        print("Close Application")

    def test_search(self):               # for all method for test case, need to start with 'testXXXXX'
        print("This is search test")

    def test_advancedsearch(self):
        print("This is Advanced search test")

    def test_prepaidRecharge(self):
        print("This is prepaid Recharge test")

    def test_postpaidRecharge(self):
        print("This is post paid Recharge test")


if __name__ == "__main__":    # note the total test case is only 4. All setup/teardown do not count as test cases
    unittest.main()


# SKIPPING TESTS
# - skip test
# - skip test with reason
# - skip test with Based on Condition

import unittest


class AppTesting(unittest.TestCase):

    @unittest.SkipTest                  # skipped this function
    def test_search(self):
        print("This is search test")

    @unittest.skip("I am skipping this test method due to it is not yet ready")   # skip with reason
    def test_advancedsearch(self):
        print("This is Advanced search test")

    @unittest.skipIf(2 == 1, "NUMBERS ARE EQUAL")  # if this true, skip      skip with condition
    def test_prepaidRecharge(self):
        print("This is prepaid Recharge test")

    def test_postpaidRecharge(self):
        print("This is post paid Recharge test")

    def test_loginbygmail(self):
        print("This is login by email")

    def test_loginbytwitter(self):
        print("This is login by twitter")


if __name__ == "__main__":
    unittest.main()


# ASSERTION UNITTEST WITH SELENIUM
# - check points to evaluate some execution
# - to check if test case fail or not

# 1. Assert Equal
# - compare 2 parameter
# - if equals, then continue to subsequent execution
# - if diff, then the test case is failed

# 2. Assert Not Equal
# - pass if 2 parameters not equal

import unittest
from selenium import webdriver


class Package1(unittest.TestCase):

    def testName(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\Diyanah\Downloads\chromedriver_win32\chromedriver.exe")
        self.driver.get("https://www.google.com/")
        titleOFWebPage = self.driver.title

        # self.assertEqual("Google", titleOFWebPage, "Webpage title is not same")
        self.assertNotEqual("Google123", titleOFWebPage, "Webpage is equal")


if __name__ == '__main__':    # this is to run the class function
    unittest.main()


# ASSERT TRUE / FALSE

import unittest
from selenium import webdriver


class Package1(unittest.TestCase):

    def testName(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\Diyanah\Downloads\chromedriver_win32\chromedriver.exe")
        self.driver.get("https://www.google.com/")
        titleOFWebPage = self.driver.title

        self.assertTrue(titleOFWebPage == "Google")    # True
        self.assertFalse(titleOFWebPage != "Google")   # False


if __name__ == '__main__':    # this is to run the class function
    unittest.main()


# ASSERT IS NONE / NOT NONE

import unittest
from selenium import webdriver


class Package1(unittest.TestCase):

    def testName(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\Diyanah\Downloads\chromedriver_win32\chromedriver.exe")
        # self.driver = None
        # say we wanna check if the website is open/initiated or not, we can check if driver has some value in it or not
        # self.assertIsNone(self.driver)
        self.assertIsNotNone(self.driver)


if __name__ == '__main__':    # this is to run the class function
    unittest.main()


# ASSERT IN / NOT IN
# can be used in list, tuple, dictionaries

import unittest


class Package1(unittest.TestCase):

    def testName(self):
        list = {"python", "selenium", "java"}

        # self.assertIn("python", list)   # true
        # self.assertIn("ruby", list)     # false
        # self.assertNotIn("ruby", list)   # true
        self.assertNotIn("python", list)   # false


if __name__ == '__main__':    # this is to run the class function
    unittest.main()


# ASSERT GREATER / EQUAL / LESS
# comparison between 2 parameters

import unittest


class Package1(unittest.TestCase):

    def testName(self):
        # self.assertGreater(100, 10)   # if a > b then true
        # self.assertGreater(10, 100)

        # self.assertGreaterEqual(100, 99)  if a >=b then true
        # self.assertGreaterEqual(99, 99)
        # self.assertGreaterEqual(98, 99)
        # self.assertLessEqual(98, 99)
        self.assertLessEqual(99, 99)

        # self.assertLess(10, 100)       # if a < b, then true
        # self.assertLess(100, 100)


if __name__ == '__main__':    # this is to run the class function
    unittest.main()


# CREATING TEST CASE & TEST SUITES / EXECUTING THEM
'''
say we wanna create a function to run diff test cases, we can categorized them in deff test case

Package1
1. Login
- login by email
- login by fb
- login by twitter
2. Sign up
- by email 
- by fb
- by twitter

Package2
1. payment 
- in dollars
- in rupees
2. payment refund
- payment refund by bank

We want to use all these test case for
a) Sanity Package1
b) Master test suite
c) functional test suite

'''