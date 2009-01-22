#!/usr/bin/python

from glob import glob

# Get the names of the problem solution and chapter files.
probfiles = glob('problem*.md')
chapfiles = glob('chapter*.md')
last = int(probfiles[-1][7:10])


# The last problem number for each chapter. Chapter 0 is a fake.
problems = [0, 10, 52, 80, 100, 109, 123, 141, 160, 182, 211, 228, 244, 266, 288, 306, 323, 334]

# The chapter names. Chapter 0 is a fake.
names = ["", "Discrete Coplanar Forces", "Conditions of Equilibrium", "Distributed Forces", "Trusses and Cables", "Beams", "Friction", "Space Forces", "The Method of Work", "Kinematics of a Point", "Dynamics of a Particle", "Kinematics of Plane Motion", "Moments of Inertia", "Dynamics of Plane Motion", "Work and Energy", "Impulse and Momentum", "Relative Motion", "Gyroscopes"]

# Initialize the list of last solution linked to in each chapter file. Chapter 0 is a fake.
linked = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Determine the solutions already listed in each chapter file.
for fn in chapfiles:
  chnum = int(fn[7:9])
  f = open(fn, 'r')
  lines = f.readlines()
  numbers = [int(l.split()[2].split(']')[0]) for l in lines if l[0] == '*']
  linked[chnum] = max(numbers)
  f.close()


# Write new chapter files when necessary to reflect the latest solved problems. We write
# a new chapter file when
# 
# 1. the chapter wasn't finished in the last update;
# 2. the last solution is beyond the last update of this chapter file; and
# 3. the last solution is beyond the end of the previous chapter.
for c in range(1, len(problems)):
  if (linked[c] < problems[c]) and (linked[c] < last) and (problems[c-1] < last):
    f = open('chapter%02d.md' % c, 'w')
    f.write("# %s #\n\n" % names[c])
    for p in range(problems[c-1]+1, min(problems[c],last) + 1):
      f.write("* [Problem %d](problem%03d.html)\n" % (p, p))
    f.close()
    print 'chapter%02d.md' % c

