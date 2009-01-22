#!/usr/bin/python

from glob import glob

# Get the number of problem solution files.
count = len(glob('problem*.md'))

# Print out a JavaScript function that will print that number.
print '''function problemCount() {
  document.write(%d);
}
''' % count

# Get the chapter files.
chapters = glob('chapter*.md')

# Turn them into an HTML list of links.
chapterList = ['<li><a href="%s">Chapter %d</a></li>' % (f.replace('md', 'html'),i+1) for i,f in enumerate(chapters)]
chapterListString = '\\n'.join(chapterList)

# Print a JavaScript function that will print the chapter list.
print '''function chapterList() {
  document.write('%s');
}
''' % chapterListString