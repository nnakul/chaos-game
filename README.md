# ABOUT
The project contains simulations of various chaos games that generate a fractal. Each of the simulation starts with a polygon (like triangle, square, pentagon) and a randomly chosen point inside the polygon. A fractal is *possibly* generated on iteratively creating a sequence of points, starting with the initial random point, in which each point in the sequence is a given fraction of the distance between the previous point and one of the vertices of the polygon (or any other fixed point associated with the polygon's geometry, like midpoint of an edge or geometric center); the latter being chosen at random in each iteration under some or not under any constraints.

As the game reaches higher and higher count of iterations, the fractal becomes more and more prominent and sharp. Though a familiar figure can be spotted just after a few thousands of iterations, it is only after millions of iterations (here achieved in about 8 minutes) that an extremely sharp fractal is formed, too sharp for the successive iterations to produce any visible change.

*Note that these estimations naturally depend on the size of the polygon (or width of the GUI window). These are deduced from a polygon of a particular size as used in the program.*

# CONTENTS
The project contains simulations for eight fractals including Sierpinski Triangle, Sierpinski Carpet, T-Square and Vicsek fractal. The first file named *Copy_Generator* contains the code of the fractal that I find the most interesting. It asks the user to draw something on the window and when the user instructs the start of the chaos game, the simulation creates infinte number of copies of the drawing of variable sizes on the screen, smaller than the size of the drawing. As stated earlier, the game might take a few minutes to produce a sufficiently sharp fractal. At first few thousands of iterations the fractal might be too blurred (or incomplete) to seem complex and similar at different levels of magnification; but after enough number of iterations it will appear as sharp as it can possibly be on that scale.

# EXPERIENCE
I came across fractals and chaos games for the first time in my first college semester and that's when I coded a simulation for Sierpinski Triangle on a graphics library in C language ( for that was the only language I knew back then ). It is extremely satisfying to watch how a symmetrical self-similar pattern is created by randomly placed points inside a polygon on introducing some constraints. The fractals produced through these simulations can be used (upon compressing, resizing, rotating etc) in graphics-based applications and animations. The project is obviously less about the Mathematical aspects of *Chaos Theory* and more about directly applying its construction recipes to produce some very complex graphics.
