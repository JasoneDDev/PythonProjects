import unittest
import scoreKeeper as sk

class TestScore(unittest.TestCase):

    def test_add2Score(self):
        scorek = sk.ScoreKeeper()
        scorek.add2score(5)
        self.assertEquals(scorek.add2score(10), 15)
        self.assertEquals(scorek.add2score(35), 50)
        self.assertEquals(scorek.add2score(120), 170)

    def test_subFromScore(self):
        scorek2 = sk.ScoreKeeper()
        scorek2.add2score(170)
        self.assertEquals(scorek2.subFromScore(10), 160)
        self.assertEquals(scorek2.subFromScore(35), 125)
        self.assertEquals(scorek2.subFromScore(120), 5)

        #with self.assertRaises(ValueError):
         #   scorek2.subFromScore('a')  # or something that will raise an exception of value error

if __name__ == '__main__':
    unittest.main()