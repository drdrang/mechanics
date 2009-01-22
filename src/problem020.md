# Problem 20 #

Den Hartog slips a couple of advanced concepts into this problem, items that aren't properly covered until Chapter 3. But their introduction is gentle and shouldn't cause much head scratching.

First, we have to deal with the force coming from the pressure pushing up on the valve and transmitted by the valve to the horizontal arm. The pressure is acting over a circular area with a diameter of \(d\). Because pressure is measured in force units per area units--e.g., pounds per square inch in part b) of this problem--it seems reasonable to believe that the force due to pressure on a flat plate is equal to the pressure multiplied by the area over which the pressure acts. And that's exactly right. So here the upward force on valve is 

\[ F_p = p \left (\frac{\pi d^2}{4} \right ) \]

When he described the weight of the arm itself, Den Hartog says that it's "concentrated at a distance \(c\) from the valve." This, of course, is nonsense. The weight of the arm is spread out over the length of the arm; it isn't concentrated at a single point. But, as we'll see later, the *effect* of its distributed weight is equivalent to a concentrated force acting at its center of mass.

OK, enough theory. We know the weight of the bar, \(w\); we know the pressure force, \(F_p\); we don't know the required weight at the right end of the arm, \(W\), or the reaction force at the pivot at the left end of the arm. Since we're asked in part a) to determine \(W\), it makes since to try to find an equilibrium equation that includes \(W\) but doesn't include the pivot force. The equilibrium equation for moments about the pivot--which we'll call O--will do the trick:

\[ \sum M_O = F_p b - w (b+c) - W (b+a) = 0 \]

The pivot force doesn't show up in this equation because its lever arm is zero. Substituting in the expression for \(F_p\) and solving for \(W\), we get

\[ W = \frac{p \pi d^2}{4}\frac{b}{b+a} - w \frac{b+c}{b+a} \]

This is the weight that will exactly balance the pressure. If the pressure is less than \(p\), the weight will push the valve down onto the top of the boiler and the contact force between the boiler wall and the valve will provide the extra upward force needed to satisfy equilibrium. If, on the other hand, the pressure is increased above \(p\), the weight will not be enough to hold the arm down and steam will escape out the valve, reducing the pressure back down to \(p\). That's the purpose of a safety valve--by opening at a given pressure, it limits the pressure in the boiler to a safe level.

For part b), we simply substitute the given values into the equation.

\[ W = \frac{200 \pi 2^2}{4}\frac{3}{3+12} - w \frac{3+5}{3+12} = 125.7 - 0.533 w \]

which is, except for some rounding, the answer in the back of the book. I'll never understand why Den Hartog didn't give a numerical value for \(w\).
