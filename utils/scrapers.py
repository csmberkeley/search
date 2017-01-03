from bs4 import BeautifulSoup
import requests
import csv
import os
import glob

class Link:
    def __init__(self, type, title, semester, url):
        self.type = type
        self.title = title
        self.semester = semester
        self.url = url

    def __repr__(self):
        return '<Link to {0} {1} titled "{2}" at {3}>'.format(self.semester, self.type, self.title, self.url[:10])

def search_su16(include_lectures=True):
    url = 'http://www.cs61bl.org/su16/'
    soup = BeautifulSoup(requests.get(url).text)
    raw_links = soup.find('table', {'id': 'calendar'}).find_all('a')

    if include_lectures:
      lecture_links = [{'type': 'slides',
                        'formatted_title': '61BL: ' + tag.get_text(),
                        'title': tag.get_text().lower(),
                        'semester': 'su16',
                        'url': tag['href']}
                        for tag in raw_links if 'docs.google' in tag['href']]
    else:
      lecture_links = []

    lab_links = [{'type': 'lab',
                  'formatted_title': '61BL ' + tag.get_text(),
                  'title': tag.get_text().lower(),
                  'semester': 'su15',
                  'url': url + tag['href']}
                  for tag in raw_links if 'Lab' in tag.get_text()]

    return lecture_links + lab_links

def search_sp14():
    url = 'https://www.cs.berkeley.edu/~jrs/61b/'
    soup = BeautifulSoup(requests.get(url).text)
    table = soup.find('table', {'border': 2, 'cellpadding': 2}).find_all('a')
    lecture_links = [{'type': 'notes',
                      'formatted_title': 'Shewchuk\'s Notes: ' + tag.get_text(),
                      'title': tag.get_text().lower(),
                      'semester': 'sp14',
                      'url': url + tag['href']}
                      for tag in table if len(tag['href']) == 6 and 'lec/' in tag['href']]

    return lecture_links

def search_sp16(include_lectures=True):
    url = 'http://datastructur.es/sp16/'
    soup = BeautifulSoup(requests.get(url).text)
    raw_links = soup.find('table', {'id': 'calendar'}).find_all('a')

    if include_lectures:
      lecture_links = [{'type': 'notes',
                        'formatted_title': tag.get_text(),
                        'title': tag.get_text().lower(),
                        'semester': 'sp16',
                        'url': url + tag['href']}
                        for tag in raw_links if 'youtube.com' in tag['href']]
    else:
      lecture_links = []

    lab_links = [{'type': 'lab',
                  'formatted_title': tag.get_text(),
                  'title': tag.get_text().lower(),
                  'semester': 'sp16',
                  'url': url + tag['href']}
                  for tag in raw_links if '/lab' in tag['href']]

    # url_assignments = 'http://datastructur.es/sp16/assign.html'
    # soup_assignments = BeautifulSoup(requests.get(url_assignments).text)
    # guerrilla_table = soup.findAll("table", {"id": "guerrilla"})[0].find("table")

    return lecture_links + lab_links

def import_from_csv():
    csvs = filter(os.path.isfile, glob.glob('./*.csv'))
    if len(csvs) > 0:
        with open(csvs[0], 'r') as csvfile:
            reader = csv.reader(csvfile)

            return [{'type': row[3],
                     'formatted_title': row[2],
                     'title': row[2].lower(),
                     'semester': '--',
                     'url': row[0],
                     'topics': row[1].lower().split(';')} for row in reader]
    else:
        return []

