# Problem 59 #

This one will be a little different because we have to (mathematically) weight the areas according to their density when we work out the composite properties. We'll start again with our origin at the top left corner, the *x* axis pointing to the right and the *y* axis pointing down. The cross-section will be broken into three regions:

1. A thin horizontal steel rectangle with thickness \(a/8\), width \(9a/8\), and density 7.8.
2. A thin vertical rectangle with thickness \(a/8\), height \(a\), and density 7.8.
3. A wood square with height and width \(a\) and density 0.8.

This is the kind of problem that's easy to set up in a spreadsheet. The layout could look like this:

|n|w|h|d|x|y|Ad|Adx|Ady|
|-|-|-|-|-|-|-|---|---|
|1|1.125|0.125|7.8|0.5625|0.0625|1.0969|0.61699 |0.068555|
|2|0.125|1.000|7.8|0.0625|0.6250|0.9750|0.060937|0.60938|
|3|1.000|1.000|0.8|0.6250|0.6250|0.8000|0.500000|0.50000|
| |     |     |   |      |      |2.8719|1.1779  |1.1779 |


where *n* is the region number, *w* is the width, *h* the height, *d* the density, *x* and *y* the coordinates of the centroid, *Ad* the weighted area, and *Adx* and *Ady* the moments of the weighted areas about the axes. The line at the bottom represents the sum of the values above, and so the center of gravity is at

\[ \bar x = \bar y = \frac{1.1779}{2.8719} = 0.41 \]

Since the dimensions are all given in terms of *a*, the center of gravity is at \((0.41a, 0.41a)\).
