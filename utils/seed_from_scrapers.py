from pymongo import MongoClient
import argparse
import scrapers
import csv

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

  su16 = scrapers.search_su16()
  print 'added %d links from su16' % len(su16)
  sp14 = scrapers.search_sp14()
  print 'added %d links from sp14' % len(sp14)
  sp16 = scrapers.search_sp16()
  print 'added %d links from sp16' % len(sp16)
  links.insert_many(su16 + sp14 + sp16 + problems)
