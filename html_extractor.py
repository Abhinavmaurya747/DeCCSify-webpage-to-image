import requests
from bs4 import BeautifulSoup
from lxml import html
import os
import pandas as pd

path = os.getcwd()
extracted_path = os.path.join(path, 'downloaded_pages')

def extract_content_from_URL(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    soup = soup.find()
    code = str(soup.prettify())
    
    filename = URL[URL.rfind("/")+1:]
    filename = filename.replace(".", "_small.")
    if filename[-4:] != 'html':
        filename = filename+'.html'
    
    with open(os.path.join(extracted_path,filename),'w', encoding='utf-8') as file:
        file.write(code)

    print('success')

    return filename


def clean_html(URL):
    """
        By cleaning the HTML we mean that all the css codes, graphics code like svg, etc, will be removed.
        And only the html content remains. No HTML, No CSS,...
        Scripts are to be retained as it may contain some information that is needed.

        The file we are accessing and modifying is now locally stored.
    """
    with open(URL, "r", encoding='utf-8') as f:
        page = f.read()
    page_content = html.fromstring(page)
    
    soup = BeautifulSoup(page, 'html.parser')
    all_tags = [tag.name for tag in soup.find_all()]
    try:
        while True:
            soup.find('meta').decompose()
    except:
        pass
    try:
        while True:
            soup.find('svg').decompose()
    except:
        pass
    try:
        while True:
            soup.find('link').decompose()
    except:
        pass
    try:
        while True:
            soup.find('script').decompose()
    except:
        pass
    

    all_tags = [tag.name for tag in soup.find_all()]
    number_of_tags = (len(all_tags))
    with open(URL, "w", encoding='utf-8') as f:
        f.write(soup.prettify())

def extract(URL):
    local_URL = extract_content_from_URL(URL)
    clean_html(os.path.join(extracted_path,local_URL))


def getURLs():
    URLs = pd.read_csv('training/links.csv')
    URLs = URLs['links'].to_numpy()
    return URLs

def html_extractor():
    URLs = getURLs()
    for url in URLs:
        extract(url)


#URL='https://pypi.org/project/imgkit/'
#extract(URL)
html_extractor()