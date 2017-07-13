import sys


def get_page(url):
    '''Return the page at the given url as text
    '''
    return

def run_analysis(body):
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

    return

def get_title(body):
    '''Get the page title

    :param str body: The body of the page
    :return str: The page title
    '''

def get_meta_tags(body):
    '''Get the meta tags

    :param str body: The body of the page
    :return list of str: Meta tags
    '''
def get_file_size(body):
    '''Get the page file size

    Get the page file size in human readable form (e.g. 23K)

    :param str body: The body of the page
    :return str: The file size in human readable form
    '''

def get_word_count(body):
    '''Get the word count

    :param str body: The body of the page
    :return int: The number of words
    '''

def get_number_of_unique_words(body):
    '''Get the number of unique words

    :param str body: The body of the page
    :return int: The number of unique words
    '''
def get_most_common_words(body, n=5):
    '''Get the top n most common words

    :param str body: The body of the page
    :param list of str: The most common words (descending)
    '''
def get_meta_keywords_not_in_content(body):
    '''Get a list of meta keywords that do not appear in the content

    :param body:
    :return list of str: Meta keywords that do not appear in the content
    '''

def get_links(body):
    '''Get links that appear on the page

    :param body:
    :return list of tuple (string, string): Links and their targets
    '''


if __name__ == 'main':
    body = get_page(sys.argv[1])
    run_analysis(body)
