import sys
import requests
from src.page_analyser import Page


def get_page(url):
    '''Return the page at the given url as text'''
    req = requests.get(url)
    return req.text

if __name__ == '__main__':
    body = get_page(sys.argv[1])
    page = Page(body)
    page.analyse()
