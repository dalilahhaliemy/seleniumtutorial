import unittest


class LoginTest(unittest.TestCase):    # need to write all the test method

    def test_loginbyemail(self):
        print("This is login by email test")
        self.assertTrue(True)                      # to make it True for now

    def test_loginbyfb(self):
        print("This is login by fb test")
        self.assertTrue(True)

    def test_loginbytwitter(self):
        print("This is login by twitter test")
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
