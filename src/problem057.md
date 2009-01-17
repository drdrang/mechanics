# Problem 57 #

We're going to ignore the rounded-off corners at the ends and the inside corner of the angle and consider the cross-section to be composed of two rectangles:

1. a thin vertical rectangle, 0.75 inches wide and 7.25 inches high; and
2. a thin horizontal rectangle, 0.75 inches wide and 4 inches long.

We'll put the origin of our coordinate system at the top left corner of the cross-section with the *x* axis running to the right and the *y* axis running down. Combining the two rectangles, we get

\[ A = A_1 + A_2 = 0.75 \cdot 7.25 + 0.75 \cdot 4 = 8.4375\,\rm{in^2} \]


\[ \bar x = \frac{A_1 \cdot 0.375 + A_2 \cdot 2}{A} = \frac{8.0391}{8.4375} = 0.953\,\rm{in} \]


\[ \bar y = \frac{A_1 \cdot (0.75 + 7.25/2) + A_2 \cdot 0.375}{A} = \frac{24.914}{8.4375} = 2.95\,\rm{in} \]

So the center of gravity is 0.953 in to the right of the top left corner, 2.95 in down from the top left corner, and (trivially) 3 ft in from either end.
