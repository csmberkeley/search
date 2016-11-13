from bs4 import BeautifulSoup
import requests
import csv

class Link:
    def __init__(self, type, title, semester, url):
        self.type = type
        self.title = title
        self.semester = semester
        self.url = url

    def __repr__(self):
        return '<Link to {0} {1} titled "{2}" at {3}>'.format(self.semester, self.type, self.title, self.url[:10])


def search_su16():
    url = 'http://www.cs61bl.org/su16/'
    soup = BeautifulSoup(requests.get(url).text)
    raw_links = soup.find('table', {'id': 'calendar'}).find_all('a')

    lecture_links = [{'type': 'Lecture',
                      'formatted_title': tag.get_text(),
                      'title': tag.get_text().lower(),
                      'semester': 'su15',
                      'url': url + tag['href']}
                      for tag in raw_links if '/lectures' in tag['href']]
    lab_links = [{'type': 'Lab',
                  'formatted_title': tag.get_text(),
                  'title': tag.get_text().lower(),
                  'semester': 'su15',
                  'url': url + tag['href']}
                  for tag in raw_links if 'Lab' in tag.get_text()]

    return lecture_links + lab_links

def search_sp14():
    url = 'https://www.cs.berkeley.edu/~jrs/61b/'
    soup = BeautifulSoup(requests.get(url).text)
    table = soup.find('table', {'border': 2, 'cellpadding': 2}).find_all('a')
    lecture_links = [{'type': 'Lecture',
                      'formatted_title': tag.get_text(),
                      'title': tag.get_text().lower(),
                      'semester': 'sp14',
                      'url': url + tag['href']}
                      for tag in table if len(tag['href']) == 6 and 'lec/' in tag['href']]

    return lecture_links

def search_sp16():
    url = 'http://datastructur.es/sp16/'
    soup = BeautifulSoup(requests.get(url).text)
    raw_links = soup.find('table', {'id': 'calendar'}).find_all('a')

    lecture_links = [{'type': 'Lecture',
                      'formatted_title': tag.get_text(),
                      'title': tag.get_text().lower(),
                      'semester': 'sp16',
                      'url': url + tag['href']}
                      for tag in raw_links if 'youtube.com' in tag['href']]
    lab_links = [{'type': 'Lab',
                  'formatted_title': tag.get_text(),
                  'title': tag.get_text().lower(),
                  'semester': 'sp16',
                  'url': url + tag['href']}
                  for tag in raw_links if '/lab' in tag['href']]

    # url_assignments = 'http://datastructur.es/sp16/assign.html'
    # soup_assignments = BeautifulSoup(requests.get(url_assignments).text)

    # guerrilla_table = soup.findAll("table", {"id": "guerrilla"})[0].find("table")


    return lecture_links + lab_links

def read_problems_csv():
    with open('practiceproblems.csv', 'r') as csvfile:
      reader = csv.reader(csvfile)
      
      return [{'type': 'Problem',
                      'formatted_title': row[2],
                      'title': row[2],
                      'semester': 'all',
                      'url': row[0],
                      'tags': row[1].lower().split(';')} for row in reader]