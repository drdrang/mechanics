# Problem 22 #

Here's another problem where the drawing in the book is good enough to use as a free-body-diagram.

There are two unknowns in this problem: the force, *R*, that the water exerts on the oar, and the force, *G*, that the oarlock exerts on the oar. To determine *R* without first (or simultaneously) determining *G*, we take the moments about the oarlock. The equilibrium equation is

\[ \sum M_G = 50\:\cdot\:15 - 60 R = 0 \]

which leads to *R* = 12.5 lbs.

To solve for *G*, we can either

* use this value of *R* in a force equilibrium equation or
* come up with another moment equilibrium equation that allows us to solve for *G* without knowing *R*.

Since we did Problem 21 the first way, let's do this one the second way. Taking moments about the tip of the oar, we get this equilibrium equation:

\[ \sum M_R = 50 (15+60) - 60 G = 0 \]

The solution is *G* = 62.5 lbs.

**Addendum**  
Now you may be asking yourself: Is it kosher to use two moment equilibrium equations in a planar statics problem? Aren't the three equations of planar statics \(\sum F_x = 0\), \(\sum F_y = 0\), and \(\sum M = 0\)? As it turns out, the answer to both these questions is "Yes," and there is no contradiction.

The three equations of planar statics are indeed \(\sum F_x = 0\), \(\sum F_y = 0\), and \(\sum M = 0\), but mathematics allows us to use linear combinations of these equations to solve them. So, for this problem

\[ \sum F_y = 50 - G + R = 0 \]

and if we multiply this equation by 60 and add it to the \(\sum M_G\) equation we used to solve for *R*, we get

\[ 50\:\cdot\:60 - 60 G + 60 R + 50\:\cdot\:15 - 60 R = 0 \]

which simplifies to

\[ 50 (15+60) - 60 G = 0 \]

the same as the \(\sum M_R\) equation.

This is not magic. The equilibrium equation for moments about some point will always be a linear combination of the equilibrium equation for moments about another point and one or more of the force equilibrium equations. So it *is* kosher to use two moment equilibrium equations, and it will often be advantageous for us to do so.
