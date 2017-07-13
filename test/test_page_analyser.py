import unittest
from src.page_analyser import  Page

class TestPage(unittest.TestCase):

    def setUp(self):
        self.body = '''
        <head>
        <title>super duper title</title>
        </head>
        '''

        self.page = Page(self.body)

    def test_get_title(self):
        expected_title = 'super duper title'
        actual_title = self.page.get_title(self.body)
        self.assertEquals(expected_title, actual_title)





