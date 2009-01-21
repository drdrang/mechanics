#!/usr/bin/python

from glob import glob

# Get the names of the problem solution files.
mdfiles = glob('problem*.md')


# The problem number ranges for each chapter.
chapterProblems = [(1,10), (11,52), (53,80), (81,100), (101,109), (110,123), (124,141), (142,160), (161,182), (183,211), (212,228), (229,244), (245,266), (267,288), (289,306), (307,323), (324,334)]

chapterNames = ["Discrete Coplanar Forces", "Conditions of Equilibrium", "Distributed Forces", "Trusses and Cables", "Beams", "Friction", "Space Forces", "The Method of Work", "Kinematics of a Point", "Dynamics of a Particle", "Kinematics of Plane Motion", "Moments of Inertia", "Dynamics of Plane Motion", "Work and Energy", "Impulse and Momentum", "Relative Motion", "Gyroscopes"] 

for i,c in enumerate(chapterProblems):
  f = open('chapter%02d.md' % (i+1), 'w')
  f.write("# %s #\n\n" % chapterNames[i])
  for p in range(c[0], c[1]+1):
    if 'problem%03d.md' % p in mdfiles:
      f.write("* [Problem %d](problem%03d.html)\n" % (p, p))
    else:
      f.write("* Problem %d\n" % p)
  f.close()
