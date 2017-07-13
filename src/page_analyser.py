from bs4 import BeautifulSoup


class Page:
    def __init__(self, body):
        self.body = body
        self.soup = BeautifulSoup(body, 'html.parser')

    def analyse(self):
        '''Displays analysis on the given page

        Displays the following information:
        Summary
            1. Page title
            2. Any meta tags
            3. Page file size in human readable form (e.g. 23k)

        Content analytics:
            1. Word count
            2. Number of unique words
            3. Most common 5 words
            4. List of meta keywords that do not appear in the content

        Other:
            1. List of links that appear on the page, including link text and target
        '''

    def get_title(self):
        '''Get the page title

        :return str: The page title
        '''

        return self.soup.title.string

    def get_meta_tags(self):
        '''Get the meta tags

        :return list of str: Meta tags
        '''

        meta_tags = self.soup.find_all('meta')

        return [{'name': tag.get('name'), 'content': tag.get('content')} for tag in meta_tags]

    def get_file_size(self):
        '''Get the page file size

        Get the page file size in human readable form (e.g. 23K)

        :return str: The file size in human readable form
        '''

    def get_word_count(self):
        '''Get the word count

        :return int: The number of words
        '''

    def get_number_of_unique_words(self):
        '''Get the number of unique words

        :return int: The number of unique words
        '''
    def get_most_common_words(self, n=5):
        '''Get the top n most common words

        :param list of str: The most common words (descending)
        '''
    def get_meta_keywords_not_in_content(self):
        '''Get a list of meta keywords that do not appear in the content

        :return list of str: Meta keywords that do not appear in the content
        '''

    def get_links(self):
        '''Get links that appear on the page

        :return list of tuple (string, string): Links and their targets
        '''
