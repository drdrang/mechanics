#!/usr/bin/python

import os
import re

print '''<?xml version="1.0" encoding="ISO-8859-1" ?>
<rss version="2.0">
<channel>
  <title>Den Hartog's Mechanics</title>
  <link>http://www.leancrew.com/mechanics/</link>
  <description>A web-based solutions manual for statics and dynamics problems.</description>
'''

log = os.popen('git log -n 10', 'r').read()

commits = re.split(r'commit .+\n', log)[1:]

for commit in commits:
  lines = commit.split('\n')
  author = lines[0][7:].strip()
  date   = lines[1][5:].strip()
  title  = lines[3].strip()
  desc   = '\n'.join(lines[4:]).strip()
  titleParts = title.split()
  if len(titleParts) == 2 and \
      titleParts[0] == 'Problem' and \
      titleParts[1].isdigit():
    link = 'http://www.leancrew.com/mechanics/problem%03d.html' % int(titleParts[1])
    print '''<item>
<title>%s</title>
<date>%s</date>
<link>%s</link>
<description>%s</description>
</item>
''' % (title, date, link, desc)
  
print '''</channel>
</rss>
'''
