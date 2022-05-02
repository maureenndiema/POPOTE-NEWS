import unittest
from app.models import Breaking

class KeywordTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Keyword class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_breaking = Breaking('A massive Bitcoin event is coming next week. Here’s what you need to know.' ,'https://abcnews.go.com', 'https://mashable.com/article/bitcoin-halving-2020/')

    def test_instance(self):
        '''
        Test case to test if the object is an instance of the class
        '''
        self.assertTrue(isinstance(self.new_breaking, Breaking))