# Problem 61 #

There's this joke about engineers...

A mathematician, a physicist, and an engineer were all given a red rubber ball and told to find the volume. The mathematician measured the diameter and did the triple integral. The physicist filled a beaker with water, put the ball in the water, and measured its displacement. The engineer looked up the model number in his *Red Rubber Ball Handbook*.

Can we integrate to find the centroid of a cone and a hemisphere? Of course. In fact, that's what we did for the hemisphere in [Problem 58][1]. But working engineers don't do integrals just for the sake of doing integrals. We already know the c.g. of the hemisphere is \(3/8 r\) below its base. And if we go to our *Cone Handbook* (or [here][2]), we'll find that the centroid of the cone is \(1/4 h\) above its base. So, the c.g. of the composite body is

\[ \bar z = \frac{(1/3 \pi r^2 h)(1/4 h) + (2/3 \pi r^3)(-3/8 r)}{1/3 \pi r^2 h + 2/3 \pi r^3} = \frac{h^2 - 3 r^2}{4(h+2r)} \]

where the origin of *z* is on the plane where the cone and hemisphere meet. Note that the c.g. will be right on that plane if \(h = \sqrt{3} r\), below it if *h* is smaller, and above it if *h* is larger.


[1]: problem058.html
[2]: http://mathworld.wolfram.com/Cone.html

