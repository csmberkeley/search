"""
Utility to seed the database with links from CSVs in the utils/ directory
A header row is expected with at least the column names listed in REQUIRED_KEYS.
CSVs with 'ignored' in the filename are skipped
"""

from pymongo import MongoClient
import argparse
import scrapers
import csv
import sys, os, glob

# Get this from the Google Sheet
VALID_TOPICS = set(['java','pointers','oop','polymorphism','arrays','linkedlists','iterators','runtime','trees','balancedtrees','disjointsets','hashtables','heaps','graphs','sorts','dp','tries','bits','gametrees','regex','design','advice','git'])
VALID_KEYS = set(['_id','topics','title','formatted_title','type','semester'])
REQUIRED_KEYS = set(['_id', 'formatted_title', 'type', 'semester'])

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--host', action='store', dest='host', type=str)
parser.add_argument('-p', '--port', action='store', dest='port', type=int)
parser.add_argument('-n', '--name', action='store', dest='name', type=str)

if __name__ == '__main__':
    args = parser.parse_args()
    host = 'localhost'
    port = 3001
    name = 'meteor'

    if args.port:
        port = args.port
    if args.host:
        host = args.host
    if args.name:
        name = args.name
    client = MongoClient(host, port)
    db = client[name]
    db.drop_collection('links')
    links = db.links

    csvs = filter(os.path.isfile, glob.glob('./*.csv'))
    csvs = filter(lambda f: 'ignore' not in f, csvs)

    if len(csvs) > 0:
        for filename in csvs:
            # flag if need to add title column
            cleanTitle = False
            # index of topics column
            topicsIndex = -1

            parsedLinks = []

            with open(filename, 'r') as csvfile:
                reader = csv.reader(csvfile)
                keys = reader.next()
                for key in REQUIRED_KEYS:
                    if key not in keys:
                        print 'Required key %s not present in %s. Aborting.' % (key, filename)
                        sys.exit()

                for key in keys:
                    if key not in VALID_KEYS:
                        print 'Invalid key %s found in %s. Aborting.' % (key, filename)
                        sys.exit()

                topicsIndex = keys.index('topics')
                cleanTitle = 'title' not in keys

                for row in reader:
                    link = dict()
                    for i in range(len(row)):
                        if i == topicsIndex:
                            link[keys[i]] = row[i].split(';')
                        else:
                            link[keys[i]] = row[i]
                    if cleanTitle:
                        link['title'] = link['formatted_title'].lower()

                    parsedLinks.append(link)
            links.insert_many(parsedLinks)
            print 'Inserted %d links from %s' % (len(parsedLinks), filename)



