import sys
from src.page_analyser import Page

def get_page(url):
    '''Return the page at the given url as text
    '''
    return


if __name__ == 'main':
    body = get_page(sys.argv[1])
    page = Page(body)
    body.run_analysis()
