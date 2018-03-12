# ringRoads_codeFights
Your city has two ringroads, which are concentric circles with different radiuses. There are also some roads that connect these ringroads. These roads are segments of the radius at some angle of the outer ringroad. 

You need to go from a point on the inner ringroad to a point on the outer ringroad, and you can only travel on the ringroads and the connecting roads. Of course you want to find the shortest path!

You have the radius of the inner ringroad innerRing, the radius of the outer ringroad outerRing, an array roads that defines the angles of the connecting roads (the ith road lies at the angle roads[i]), and an array travels, where each element is a pair [start, finish] that defines the travel between the point in the inner ringroad with the angle start and the point in the outer ringroad with the angle finish. Return an array in which the ith element is the length of the shortest path of travels[i].

Example

For innerRing = 10, outerRing = 20, roads = [180] and travels = [[0, 0], [60, 300]], the output should be
ringRoads(innerRing, outerRing, roads, travels) = [104.24778, 72.83185].

