# Utility to export scraped links to a CSV for Google Sheets

import scrapers
import csv

if __name__ == '__main__':
  su16 = scrapers.search_su16()
  print 'added %d links from su16' % len(su16)
  sp14 = scrapers.search_sp14()
  print 'added %d links from sp14' % len(sp14)

  with open('ignore.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(['_id', 'topics', 'title', 'formatted_title', 'type', 'semester'])

    for link in su16 + sp14:
      writer.writerow([link.get('url'),
                       None,
                       link.get('title'),
                       link.get('formatted_title'),
                       link.get('type'),
                       link.get('semester')])
