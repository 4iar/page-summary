import unittest
from src.page_analyser import  Page

class TestPage(unittest.TestCase):

    def setUp(self):
        self.body = '''
        <html>
            <head>
                <title>super duper title</title>
            </head>
            <meta name='keywords' content='sausages, pizza'>
            <meta name='description' content='super duper pizza'>
        </html>
        '''

        self.page = Page(self.body)

    def test_get_title(self):
        expected_title = 'super duper title'
        actual_title = self.page.get_title(self.body)
        self.assertEquals(expected_title, actual_title)

    def test_get_meta_tags(self):
        expected_tags = [
            {'name': 'keywords', 'content': 'sausages, pizza'},
            {'name': 'description', 'content': 'super duper pizza'},
        ]

        self.assertEqual(self.page.get_meta_tags(), expected_tags)




