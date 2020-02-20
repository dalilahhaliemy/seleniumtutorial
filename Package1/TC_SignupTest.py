import unittest


class SignupTest(unittest.TestCase):    # need to write all the test method

    def test_signupbyemail(self):
        print("This is signup by email test")
        self.assertTrue(True)                      # to make it True for now

    def test_signupbyfb(self):
        print("This is signup by fb test")
        self.assertTrue(True)

    def test_signupbytwitter(self):
        print("This is signup by twitter test")
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
