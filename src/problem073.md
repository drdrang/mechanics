# Problem 73 #

We're going to reuse the solution Den Hartog graciously provided us on page 45:

\[ \delta_1 = \frac{R}{kL} \left( 6 \frac{c}{L} - 2 \right) \]

Our plan of attack is to express *R* and *c* in terms of the values given in the problem, then set \(\delta_1 = 0\) and solve for *b*.

With \(w_1 = 20\), \(L = 12\), and \(P = 1000\), \(R = 20 \cdot 12 + 1000 = 1240\,\rm{lb}\). The position of this resultant from the right end of the beam is

\[ c = \frac{240 \cdot 6 + 1000 b}{1240} = \frac{36 + 25b}{31} \]

Plugging these and the given values into the expression for \(\delta_1\) and setting it to zero gives

\[ \delta_1 = \frac{1240}{(100/12) \cdot 12} \left( \frac{6}{12} \frac{36 + 25b}{31} - 2 \right) = 0 \]

where we've divided by 12 to express *k* in lb/ft/ft. The solution is \(b = 88/25 = 3.52\,\rm{ft}\). If *P* gets any closer to the right end of the beam, the left end will lift up off the ground.
