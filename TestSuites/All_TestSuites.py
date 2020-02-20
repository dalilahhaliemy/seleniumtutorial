import unittest
from Package1.TC_LoginTest import LoginTest
from Package1.TC_SignupTest import SignupTest

from Package2.TC_PaymentTest import PaymentTest
from Package2.TC_PaymentReturnsTest import PaymentReturnsTest


# Get all test from these method
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)


# Sanity test is login/signup
sanityTestSuite = unittest.TestSuite([tc1, tc2])
# unittest.TextTestRunner().run(sanityTestSuite)

# Functional test is payment/payment refund
functionalTestSuite = unittest.TestSuite([tc3, tc4])
# unittest.TextTestRunner().run(functionalTestSuite)

# All test suite
masterTestSuite = unittest.TestSuite([tc1, tc2, tc3, tc4])
unittest.TextTestRunner(verbosity=2).run(masterTestSuite)
