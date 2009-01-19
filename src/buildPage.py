#!/usr/bin/env python

import sys
import os
import os.path
import time
import string
import urllib

# Initialize the dictionary of dynamic information.
info = {}

# The argument is the basename of the Markdown source file.
mdFile = sys.argv[1] + '.md'

# Get the top line of the Markdown source. If it's a problem, set up
# navigation links for the bottom of the page.
topLine = open(mdFile, 'r').readline().strip(' #\n')
titleWords = topLine.split()
if titleWords[0] == 'Problem':
  num = int(titleWords[1])
  if num == 1:
    navString = '''<hr />
<p><span id="next"><a href="problem%03d.html">Problem %d</a></span>
<span id="prev">&nbsp;</span></p>
''' % (num + 1, num + 1)
  elif num == 334:
    navString = '''<hr />
<p><span id="next">&nbsp;</span>
<span id="prev"><a href="problem%03d.html">Problem %d</a></span></p>
''' % (num - 1, num - 1)
  else:
    navString = '''<hr />
<p><span id="next"><a href="problem%03d.html">Problem %d</a></span>
<span id="prev"><a href="problem%03d.html">Problem %d</a></span></p>
''' % (num + 1, num + 1, num - 1, num - 1)
else:
  navString = ''


# Open the page files and process the content.
header = open('header.tmpl', 'r')
footer = open('footer.tmpl', 'r')
cmd = 'mmmd %s | SmartyPants' % mdFile
content = os.popen(cmd, 'r')

#  Make the template.
templateParts = [header.read(), content.read(), navString, footer.read()]
template = string.Template(''.join(templateParts))

# Close the page files.
header.close()
footer.close()
content.close()

# Dictionary entry with long modification date of the Markdown file.
mdModTime = time.localtime(os.path.getmtime(mdFile))
info['modldate'] = time.strftime('%B %e, %Y', mdModTime)
info['modldate'] = info['modldate'].replace('  ', ' ')

# Dictionary entry with short modification date of the Markdown file.
info['modsdate'] = time.strftime('%m/%e/%y', mdModTime)
info['modsdate'] = info['modsdate'].replace(' ', '')

# Dictionary entry with modification time of the Markdown file.
info['modtime'] = time.strftime('%l:%M %p', mdModTime)
if info['modtime'][0] == ' ':
  info['modtime'] = info['modtime'][1:]

# Output the template with the dynamic information substituted in.
print template.safe_substitute(info)
