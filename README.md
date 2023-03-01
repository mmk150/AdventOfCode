# Advent of Code 2022


This currently is my repository for code and solution sketches to the [2022 Advent of Code problem/puzzle set](https://adventofcode.com/2022/). Advent of Code is a yearly [advent calendar](https://en.wikipedia.org/wiki/Advent_calendar) of daily programming puzzles, with difficulty that generally increases over time on a day to day basis: the earlier problems are significantly easier than the later ones. I figured this would be a good opportunity to dust off some of my programming skills and also get a bit more familiar with Python.

These problems tend to be Christmas themed and have a massive expository component to them. Often I find that the difficult part of a given puzzle is trying to understand exactly what is desired given the exposition (and stripping away components that are not entirely relevant to the actual structure of the problem). Problem come in two distinct parts, with part two becoming visible after submitting the correct solution to the first part. At some point, I would like to go through and rewrite all of the problems to be more succinct, but this is an absolutely titanic task for most of these. 

At the moment, the "solutions" here are really more of a sketch that is meant to be moderately helpful in pointing out a few aspects of a given problem. In the future I will probably expand the solution sketches here to be a bit more in-depth, and probably work on a full "solutions manual" with a couple different approaches to each problem that I'll write up in LaTeX. Also, I will probably go through all of these again and solve them purely with Numpy and/or Rust just for the experience. 

I also plan on adding past and future years to this repository.

A small spoiler warning: if you're looking to do these problems yourself, I would suggest checking each one out before looking at the solution sketches or my code. Working on things for a bit yourself (even being stumped on something for a while and attempting to power through confusion on your own for a bit) can be pretty important to the learning process!

## Problem 1

### Problem Statement

The original problem statement is [here](https://adventofcode.com/2022/day/1). For practical purposes, here is a condensed and simplified version:

Given a list of integers with sublists separated by an empty line, determine:
(a) The largest possible sum of all sublists.
(b) The sum of the three largest sublists (ordered according to their own totals)


### Solution

The solution here is pretty straightforward. Loop through the list (calculating the sublist sums as you go) and update `largest_sum` when you encounter a larger sum.  For the second part, sorting the end list and summing the three largest entries gives the answer. One can be slightly more efficient here, of course, but splitting hairs on a problem this easy is too impractical for me to justify really getting into the weeds.


## Problem 2

### Problem Statement

The original problem statement is [here](https://adventofcode.com/2022/day/2).

### Solution

This problem is also very simple. For the first part, it's solved by parsing through the input line by line and incrementing a `score` variable by an amount based on the game state that's determined by the given line. The second part is slightly more tedious to handle but it can be done in Python with some match statements. 

There is not much interesting going on yet. 


## Problem 3

### Problem Statement

The original problem statement is [here](https://adventofcode.com/2022/day/3).


### Solution

I chose to start the solution by hardcoding the alphabetical priorities listed. The function `decode` is a simple lambda expression that will handle this for a given character input. The rest can be done with set intersections after parsing and casting the input properly. The second part only changes the number of sets you are working with. 



## Problem 4

### Problem Statement

The original problem statement is [here](https://adventofcode.com/2022/day/4).

### Solution

The important thing in this problem is essentially understanding how to check whether a given interval `[a,b]` is contained in `[x,y]` or vice-versa (and in part 2, how to check for overlapping intervals in general). Coding a function that checks whether one interval is nested inside of the other is fairly straightforward, as is coding one that checks if they have non-empty intersection. 

If the reader is still confused, then I suggest looking at the code provided while drawing a few concrete examples on the same number line.


## Problem 5

### Problem Statement

The original problem statement is [here](https://adventofcode.com/2022/day/5).

### Solution

The idea here is to initialize the "piles" of crates in a stack-esque data structure, popping them from one pile and pushing them onto another pile as needed. In part one, the crane can only move one crate at a time. In part two, the crane can move multiple crates at once (but with the order preserved, as it would be in the physical analogy), so one should take care of this by making sure the intermediary data structure handling "what the crate is currently moving" takes this into account in some fashion when you are inserting and removing elements from it.


## Problem 6

### Problem Statement

The original problem statement is [here](https://adventofcode.com/2022/day/6).

### Solution

Looping through the string of characters given as an input, we can examine substrings in chunks of length four. If all characters are distinct (we use Python's set methods for this) then we've found the "start of transmission" substring and clean the message accordingly.In part two, we change the length of the substrings we are examining to those of length 14 instead of length 4. 

Tangent: A common theme in many of these problems is that a lot of them are designed in such a way that if you do part one "correctly" (by which I mean, solve them in the way the problem author undoubtedly had in mind when creating the puzzle in the first place) then part two is often a trivial modification of the part one solution. This does not always hold. 

## Problem 7

### Problem Statement

The original problem statement is [here](https://adventofcode.com/2022/day/7).

### Solution

This is the first problem where I can say that I found it somewhat fun to solve. I decided to use a few custom classes here, but the general point of this problem is to properly build a file structure system given the (parsed) input. 

My solution initializes a graph whose nodes are the file directories, and where each node object contains a list of files that that specific node contains (so it does not at initialization count space taken up by any subdirectories). After initialization, we adjust the actual space taken up by each directory recursively with `SizeAdj()` to correct the values.

After that is done, in part one we can loop over a list of `DirNode` objects and perform the required calculation. Part two is only slightly more nuanced. 


## Problem 8

### Problem Statement

The original problem statement is [here](https://adventofcode.com/2022/day/8).

### Solution

In part one the idea here is to work from the perimeter inwards to determine whether a given tree on the interior is "visible" from the outside. 

I am sure that there is some hyper-optimized method for determining this given the constraints (at least the problem statement certainly causes that "someone has probably written an algorithm for this" feeling in the back of my mind) but the naive solution in `findVisible()` that I came up with handles the given input size fairly quickly.

In part two, you are asked to compute a calculation based on "how visible" each tree is from every direction. A quick modification to our part one solution gives `findScenicScore()` which also handles the input fairly easily. 


## Problem 9

### Problem Statement

The original problem statement is [here](https://adventofcode.com/2022/day/9).

### Solution

The main ideas of my solution are that for each "knot" (i.e. piece of rope) that is forced to move, it is going to move a discrete distance towards the piece of rope that immediately proceeds it. Thinking about the physical analogue of the problem gives this intuition, and we need only make sure it's implemented correctly according to the rules laid out in the problem statement. 

To make calculations easier, I've made several functions `differencev(), addv(), cmetric(), knotnormalize()` to handle the vector physics. 

We are rewarded in trying to tackle this problem in general after getting to the second part, where they ask us to do the same input but with 10 knots instead of 2.

## Problem 10

### Problem Statement

The original problem statement is [here](https://adventofcode.com/2022/day/10).

### Solution

I think that the best advice I can offer with respect to this problem is "read the worked example very carefully in both parts". I originally did this while very exhausted one morning, and it took me a while to realize in part one that the instruction sent to handheld device needed to be executed one at a time.

I found part two to be more tedious than complex. You essentially just need to work out a way to wrap around the register value to get the correct row on the "screen", one way to do this is shown in my `cycle2array` function. 

## Problem 11

### Problem Statement

The original problem statement is [here](https://adventofcode.com/2022/day/11).

### Solution

I took the opportunity here to get a bit more familiar with classes in Python, and so made a `Monkey` class with class variables and built-in methods to handle many aspects of the puzzle. In part one it is entirely sufficient to just set up the game state in this fashion and let it run to completion.

I smiled slightly after reading the first part of this problem, as my own experience in problem design and mathematical background gave me a solid guess as to where we would be headed in part two.

In part two an important restriction on the process is removed (we no longer divide by 3 during each inspection) and the number of rounds is increased dramatically, so if a workaround isn't found here then the arithmetic can quickly balloon out of control. 

Luckily, we have access to the [chinese remainder theorem](https://en.wikipedia.org/wiki/Chinese_remainder_theorem) (and it would be remiss of me not to link [this set of notes](https://kconrad.math.uconn.edu/blurbs/ugradnumthy/crt.pdf) by Prof. Keith Conrad) so we can avoid this pitfall.

The important takeaway here is that since the inspection operations done by any given monkey is just an integer divisibility condition (and lo and behold, all of the divisors are co-prime) the set of integers which are going to pass all of these individual criteria are in bijection with the set of integers modulo N (where N is the product of all of the divisors) that would. 

In short, instead of dividing by '3' we can calculate 'N' and divide by that instead.



## Problem 12

### Problem Statement

The original problem statement is [here](https://adventofcode.com/2022/day/12).

### Solution

This is a terrain-traversal problem where the person traversing the terrain only has the ability to climb so far at once. We are being asked for the shortest path to get to a given spot (the highest on the map), so immediately my mind went to [Dijkstras algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm), a variant of which is implemented in `Dijkstras()` after initializing the terrain as a graph (though this time I used a dictionary for this instead of a custom class).

For part two, in practice it is sufficient to simply check the shortest path from all `'a'` squares which we do in `getShortestAPath()`. 


## Problem 13

### Problem Statement

The original problem statement is [here](https://adventofcode.com/2022/day/13).

### Solution

This problem is pretty straightforward. Making two functions `listComp()` and `intComp()` to handle the comparison logic is the bulk of the work in part one. In the second part, we are handed two extra packets `[[2]]` and `[[6]]` and are told to figure out the positions of these two in the final, sorted result so that we can perform a calculation on their indicies to get the desired solution. A key observation here is noting that we can get away with finding all of the elements less than either of them to determine their indices in the sorted result, so we do not actually have to sort everything. 

## Problem 14

### Problem Statement

The original problem statement is [here](https://adventofcode.com/2022/day/14).

### Solution

I chose to encode the movement logic of each element of the sandpile in the `Grain()` class, initialize an array from my puzzle input,and then run through the results until the first grain of sand started spilling into the bottomless pit. Part two requires some slight modifications (there is a floor instead of a pit) to the code, but they aren't particularly onerous. 

I believe you can solve part two mathematically with a volume calculation and a bit of thinking (the sand grains should form a triangle piling up from the floor, for instance), but I haven't investigated to see if that approach actually works.

## Problem 15

### Problem Statement

The original problem statement is [here](https://adventofcode.com/2022/day/15).

### Solution

One of the key things in my solution of this problem is that this boils down to covering a space with n-balls in the [taxicab metric](https://en.wikipedia.org/wiki/Taxicab_geometry) at the end of the day. This will look like a bunch of diamonds centered at points where the sensors are firing off, with radii determined by the taxicab distance to the nearest beacon position.

For part one, it suffices to just cover the space (I used a large array) and count the empty spaces on the given row. 

For part two, it is a bit more complicated. One way of figuring out where the "distress beacon" is is to search the perimeters of all of the diamonds (intuitions says that the "distress beacon" is not picked up by sensors (which go out to the nearest beacon) if and only if it happens to be on the perimeters of some of the diamonds-- you can verify that this is true) for the beacon. The equations for the bordering lines of each diamond are well known and computable by hand, so one can do this as I have done in `lineset`. 

You can narrow down the search space a bit in this manner and then manually check the list of final candidates to find the beacon's location. 

## Problem 16

### Problem Statement

The original problem statement is [here](https://adventofcode.com/2022/day/16).

### Solution

This is the first problem that actually stumped me for most of a day.

The context boils down to a graph `G` with each vertex having a valve with a given flow rate and edges to some other vertices. The hero of the story must traverse this graph (taking one minute to move from vertex to vertex) and choose the path that gives the optimal total flow volume after time runs out.

The first mathematical simplification here (that one can convince themselves of with enough thought) is that there is no advantage to working with `G` as opposed to `G'`, the graph one creates by removing all vertices with zero flow rate and connecting all vertices with edges of the proper weight (timed-distance).

To actually solve things, I tried a number of different approaches (some sort of greedy algorithm taking into account flow-rates was tried, as was a probabilistic approach). Eventually I settled on a bound and branch approach implemented recursively, with initial parameters set by a heuristic run (that would get most of the way there and hopefully prune a large portion of the search space). This was implemented in `heuristicRun` and `recursive`. 

In part two of this problem, the hero has a helper "Elephant" that can assist them and we are asked to calculate the best possible flow rate. Without loss of generality (at least in my specific recontexturalization of the problem), one can assume that the paths the Hero and the Elephant take in the best possible result are independent of one another. Thus, if `P` is the path calculated in part one, we can consider `G'/P` (adding the origin vertex back in, of course) and perform the same calculation on this subgraph to get the best path the Elephant can take. The numerical result follows. 



## Problem 17

### Problem Statement

The original problem statement is [here](https://adventofcode.com/2022/day/17).

### "Solution"

This is the only problem that I'm declining to actually post my code (which is messy) or give a detailed solution for. Part one is, morally speaking "make a Tetris variant", while the takeaway from part two is "and at some point this process should cycle. Use this fact to calculate what happens after an absurd amount of time" in a nutshell.

Overall, this one was far too much work, and uninteresting work (at least for me) at that. I think this is the only problem out of the AoC 2022 puzzles that I would just recommend skipping.


## Problem 18

### Problem Statement

The original problem statement is [here](https://adventofcode.com/2022/day/18).

### Solution

This puzzle is much more fun than the previous one. The input is a list of co-ordinates in 3-space that essentially represent "lava cubes".

In part one, we are asked to compute the "surface area of the pile of lava cubes that touches air". There are a number of ways to do this, but invariably the approach is going to involve constructing the actual 3D shape that results, in some fashion or another.One can do this with a 3-d array, or you can use something more complicated. I chose to use a custom lava cube object (this approach will help us later), keeping track of it's neighbors. To calculate the surface area that touches the air you can simply loop through the list of cubes and calculate `6-#Neighbors`.

In part two, we are asked to do something a bit more complicated. The part one calculation neglects to take into account that the topology of the resulting shape might be more complicated (suppose there are bubbles of air on the interior of our giant lava blob). We are asked to calculate the surface area of the lava exposed to the exterior air (where "exterior" in this context means "path-connected to the protagonist character" in the situation). 

At first glance, this might appear fairly difficult. One solution (the one I chose) involves sort of a cellular automata approach: if you designate a few cubes of air on the exterior of the lava blob as "Definitely Outside Air" and then define the "outside air" to be "any air that is path-connected to Definitely Outside Air", then you can start at the cubes of Definitely Outside Air and define their neighbors to be "on the outside" (and then their neighbors and so on).This is accomplished by creating an "air cube" object using our lava cube one as a template, and giving it some extra parameters. 

One problem with this approach is that it is not at all obvious that the shape of the lava blob is such that the smallest array that could hold it won't result in "pockets" of air that would in reality be on the outside, but that aren't connected to each other due to the limits of the array size. This can be easily fixed by artificially expanding the size of array by a decent amount in each dimension.

Now we just loop through our list of lava cubes and calculate `#Neighbors Who Are Outside Air` to get the result for part two.


## Problem 19

### Problem Statement

The original problem statement is [here](https://adventofcode.com/2022/day/19). 

### Solution

This day's problem was certainly an interesting one. At first glance, this parses as an integer programming problem. My background in that particular subfield is virtually nil, and while it would be a nice excuse to justify a deep dive into linear optimization, in practice I can't justify expending that sort of time for one particular daily programming puzzle. Intuition says then that we'll probably end up solving this in a similar fashion to Problem 16. 

There are a few simplifying assumptions that one can make. First off, we need only consider build order sequences with elements in `{O,C,Obs,Geo}`, all of which will (by necessity) have a total length bounded by the amount of time we have. The rounds where we must wait around for resource production to happen by the gathering robots need not be factored in to our solution directly. Second, I should note that one sensible criteria to implement is "one never needs to build more of a given robot than the highest resource cost of the resource associated with that particular robot", which can be illustrated in simpler terms by "if you only ever need to spend a maximum of 7 Obsidian at once, then you only need a maximum of 7 Obsidian gathering robots, period". This is a strict upper bound: in practice I expect the actual number to be less than the maximum.

With that out of the way, we can begin computing the solution. Similar to problem 16, we're going to attack this by examining the total solution space and pruning large swathes of it with various heuristics, which we handle in `initGraph`. We calculate an "impossible path" in `impossiblePath` that essentially serves as an upper bound estimate for anny particular build sequence we are currently working with: if at a given point in the sequence, we suddenly have infinite O and C resources, and we only choose to build Obsidian and Geode bots after this, then do we surpass the current best possible path? If the "impossible path" can't reach this, then the current build sequence is doomed to fail, so we can abort it. This saves a lot of actual computation.

We calculate the best build sequence of all the blueprints given to us and get the part one solution. In part two, there are some minor optimizations to the code to make it run a bit faster. 



## Problem 20

### Problem Statement

The original problem statement is [here](https://adventofcode.com/2022/day/20). 

### Solution

This problem is an exercise in performing rotations on a decoder ring (or if you prefer, modular arithmatic). I coded the movement logic in the `Wrapped` class, as well as a function `calcMod` to calculate where the destinations that are being asked for are going to "land", in this representation. Part one is straightforward having done this. In part two, we scale up everything by a large prime number and need to do repeated version of the first part. You must keep a copy of the original input as instructions for future rotations. 

Everything is more or less straightforward.


## Problem 21

### Problem Statement

The original problem statement is [here](https://adventofcode.com/2022/day/21). 

### Solution

I found this problem to be fun. I started out by making a `Monkey` object to store the parsed input data. This wasn't all that necessary (an array or a `dict()` would have sufficed) but it's how I felt like approaching it at the time. 

For part one, the solution (that I chose to implement) is sketched as follows:


- If the Monkey just has an integer value instead of an arithmetic operation, it is "done" and can be added to the `dict()` of finished Monkeys, `Monkeys`.
- Otherwise the Monkey has some sort of arithmetic expression that depends on other Monkeys. Add it to a separate list `pre_Monkeys`.
- While `pre_Monkeys` is nonempty, loop through it, and for each Monkey `M` in `pre_Monkeys`, search through `Monkeys` looking for any whose names fit depencies for `M`.
- When both dependent Monkeys for `M` are found (and so finished themselves!), evaluate this Monkey's arithmetic expression and replace it's value with the result. Add it to `Monkeys` and pop it from `pre_Monkeys`.

After this terminates you can check the list of (now finished) Monkeys for the one with name `root` to see what it's value is.

For part two, there are several complications that boil down to solving a linear equation with an unknown input for one of the Monkeys after all of this. We will either have to implement a basic computer algebra system, use an existing package or module that does this, or we can dodge this neatly by using complex numbers. The lazy mathematician in me chose to take the third option here.

We can set the value for `humn` to `complex(0,1)` which is the complex number `i` (or `j` as Python writes it) and set the function for `root` to `=`. At the end of the day, we will now get a linear equation (treating `j` as a variable now) that we can solve with little effort to get the answer.

## Problem 22

### Problem Statement

The original problem statement is [here](https://adventofcode.com/2022/day/22). 

### Solution

This problem is a topoligical one at its heart. 

In part one we are given a 2D map constructed by a flattened cube, and handed a set of movement instructions. We are told that exiting off the side of the map will "wrap back around" to the other side. Implementing this is fairly straightforward, but in the context of the problem it does require we be careful and check that this is a valid move to begin with.

In part two we are told that the 2D map is actually a representation of a 3D map, and that we need to implement the same set of walking directions given earlier, but within the new context. The solution I've chosen to pursue is creating a `CubeFace` class to handle movement tracking on every individual face. After some considerable work parsing the input text file to get it into a reasonable format, I also spent some time working out the transition maps by hand on a whiteboard (stored in the `transitions` dictionary). This is necessary, because (and you can convince yourself of this if you construct a physical model of the 2D input map and fold it into a cube) travel from one cube face to another-- and what the result of that operation is, exactly --is dependent on how the edges of each cube face are glued to each other. The solution is then obtained by placing the hero down at the starting square and following the movement instructions given.

## Problem 23

### Problem Statement

The original problem statement is [here](https://adventofcode.com/2022/day/23). 

### Solution

This problem was surprisingly straightforward (though perhaps there was a clever solution that was more elegant than mine) in terms of theoretical difficulty, though the specific implementation I chose involved a bit of work.

I created the `Elf` class and encoded the various movement mechanics and board updating methods, as well as some helper functions `moveConv`, `checkPos`, and `checkJolly`. 

The movement rules here follow a cellular automata design of sorts, so I chose to instantiate all of the individual elves and allow the states to move to completion. Once this is done, you can calculate the bounding rectangle asked for in part one (let the simulation run for 10 rounds) and get the answer to part two by allowing the simulation to run to completion (terminate once all of the elves are jolly).

## Problem 24

### Problem Statement

The original problem statement is [here](https://adventofcode.com/2022/day/24). 

### Solution

The gist of this problem is that there is a shifting maze of icicles that needs safely navigated from Point A to Point B. I chose to represent the problem in 3-space with `(x,y,t)` coordinates, building a graph out of these (connectivity between vertices being represented both spacially and temporally) and perform a BFS from Point A to reach Point B. An important note is that you can limit the size of the graph generated considerably-- you can calculate the period of the icicle-maze based on the LCM of the length and width (with some index-shifting).

In part two, we are asked to perform the computation three times, essentially. If you did not implement part one efficiently, this is probably going to be a point of contention. Luckily my solution seems to do just fine. 

## Problem 25

### Problem Statement

The original problem statement is [here](https://adventofcode.com/2022/day/25). 

### Solution

The point of this question is essentially testing how comfortable you are with a base-b expansion where the coefficients can be in a different ring (in the mathematical sense) than the set of integers.

The function `snafu2real` converts the "snafu" numbers to their equivalents in base-10. The function `convert_to_quinary` converts the base-10 representation to the base-5 representation. Finally, the function `quinary_to_snafu` converts from quinary to "snafu". I recommend verifying they give the correct results by working through a few conversions by hand, if you are unconvinced. 

