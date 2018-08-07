import unittest
import scoreKeeper as sk
from unittest.mock import patch # this is for data out of your control ie websites etc. able to mock data and get responses etc.

class TestScore(unittest.TestCase):

    @classmethod
    def SetUpClass(cls):
        # initial setup (databases etc)
        pass

    @classmethod
    def TearDownClass(cls):
        # final tear down
        pass

    # setup / teardown is before and after each test
    def setUp(self):
        self.scorek = sk.ScoreKeeper()
    def tearDown(self):
        # example of things to add would be to remove files if testing if files were created by a function.
        pass

    def test_add2Score(self):
        self.scorek.add2score(5)
        self.assertEquals(self.scorek.add2score(10), 15)
        self.assertEquals(self.scorek.add2score(35), 50)
        self.assertEquals(self.scorek.add2score(120), 170)

    def test_subFromScore(self):
        self.scorek.add2score(170)
        self.assertEquals(self.scorek.subFromScore(10), 160)
        self.assertEquals(self.scorek.subFromScore(35), 125)
        self.assertEquals(self.scorek.subFromScore(120), 5)

        #with self.assertRaises(ValueError):
         #   scorek2.subFromScore('a')  # or something that will raise an exception of value error

    def test_mockData(self):
        pass
        #with patch(employee.request.get) as mocked_get: # uses patch as context manager "with" ...this is swapping the get call with our patch/mock method
        #    # will use mocked instead of the actual request
        #    mocked_get.return_value.ok = True # here we set what should come back
        #    mocked_get.return_value.text = 'Success' # set what should come back here as well

        #    schedule = self.emp_1.monthly_Schedule('May') # setup as if we were testing it here and this calls the function
        #    mocked_get.assert_called_with('http://companyName.com/shafer/May') # testing if got called with proper URL
        #    self.assertEqual(schedule, 'Success') # testing if the return value came in correctly... ie 'sucess' set above




if __name__ == '__main__':
    unittest.main()