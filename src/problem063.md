# Problem 63 #

In [Problem 61][1], we saw that the c.g. of a cone is one-quarter of the way up from the base to the tip. It turns out that the one-quarter rule works for any pyramid-like object. And you probably learned in geometry class that the volume of a pyramid is one-third the base area times the height, regardless of the shape of the base. We'll use these formulas and the concept of negative space to solve this problem.

We've seen in several problems how to break up a complex body into several simpler bodies and combine their volumes and centers of gravity to get the c.g. of the complex shape. The usual formula is

\[ \bar x = \frac{\sum_{i=1}^n \rho_i V_i \bar x_i}{\sum_{i=1}^n \rho_i V_i} \]

where *n* is the number of parts, and the \(\rho_i\), \(V_i\), and \(\bar x_i\) are the densities, volumes, and c.g. coordinates of the parts. The same formula holds, of course, for the *y* and *z* coordinates. In most of the problems we've done, the densities are all the same, so they drop of the formula and can be ignored.

If the body we're looking at has a hole in it or has some part chopped away, we can still use this formula, we just treat the volume of the hole or chopped-away part as a negative quantity.

So for the truncated pyramid in this problem,

\[ \bar z = \frac{\frac{1}{3}a^2 h \frac{h}{4} - \frac{1}{3}\left(\frac{a}{3}\right)\frac{h}{3} \left(\frac{2h}{3} - \frac{h}{12}\right)}{\frac{1}{3}a^2 h - \frac{1}{3}\left(\frac{a}{3}\right)\frac{h}{3}} = \frac{3}{13}h \]

which is the answer to part a).

For part b), we'll call the base area *A*, the height of the full pyramid *h*, and the height of the truncated part \(h_1\). (No, I would not have used this notation if I hadn't peeked the back of the book to see what symbols Den Hartog used.)  For this generalized problem,

\[ \bar z = \frac{\frac{1}{3}A h \frac{h}{4} - \frac{1}{3} \frac{h_1^2}{h^2} A h_1 \left( h - h_1 + \frac{h_1}{4} \right)}{\frac{1}{3}A h - \frac{1}{3} \frac{h_1^2}{h^2} A h_1} \]

which simplifies to 

\[ \bar z = \frac{h^4 - 4 h h_1^3 + 3 h_1^4}{4 (h^3 - h_1^3)}  \]




[1]: problem061.html
[2]: problem059.html

