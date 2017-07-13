import unittest
from src.page_analyser import  Page

class TestPage(unittest.TestCase):

    def setUp(self):
        self.body = '''
        <!-- no peeping please -->
        <html>
            <head>
                <title>super duper title</title>
            </head>
            <body>
            <h1>super duper pizzas</h1>
            <h2>the most super duper pizzas</h2>
            <a href='https://www.google.co.uk/search?q=super+duper+pizza'>find us on google</a>
            <a href='https://www.dominos.co.uk/'>or betray us</a>
            </body>
            <meta name='keywords' content='sausages, pizza'>
            <meta name='description' content='super duper pizza'>
        </html>
        '''

        self.page = Page(self.body)

    def test_get_title(self):
        expected_title = 'super duper title'
        actual_title = self.page.get_title()
        self.assertEquals(expected_title, actual_title)

    def test_get_meta_tags(self):
        expected_tags = [
            {'name': 'keywords', 'content': 'sausages, pizza'},
            {'name': 'description', 'content': 'super duper pizza'},
        ]

        self.assertEqual(self.page.get_meta_tags(), expected_tags)

    def test_get_file_size(self):
        page = Page('1234')
        self.assertEqual('4 Bytes', page.get_file_size())

        page = Page('1' * 323841)
        self.assertEqual('323.8 kB', page.get_file_size())

    def test_get_word_count(self):
        self.assertEqual(self.page.get_word_count(), 18)

    def test_get_number_of_unique_words(self):
        self.assertEqual(self.page.get_number_of_unique_words(), 12)

    def test_get_most_common_words(self):
        page = Page('''
        <body>
        one one one one one one one two two two two two three three three three four four four five five
        some other words that should not count
        </body>''')

        self.assertEqual(page.get_most_common_words(), ['one', 'two', 'three', 'four', 'five'])

    def test_get_meta_keywords_not_in_content(self):
        page = Page('''
            <head>
                <title>super duper title</title>
            </head>
            <body>
            <h1>super duper pizza</h1>
            <h2>the most super duper pizza</h2>
            </body>
            <meta name='keywords' content='super,sausages,pizza,horsemeat,octopus'>
        </html>
        ''')

        self.assertCountEqual(page.get_meta_keywords_not_in_content(), ['horsemeat', 'octopus', 'sausages'])

    def test_get_links(self):
        pass
