#!/usr/bin/python

from glob import glob

# Get the number of problem solution files.
count = len(glob('problem*.md'))

# Print out a JavaScript function that will print that number.
print '''function problemCount() {
  document.write(%d);
}
''' % count
