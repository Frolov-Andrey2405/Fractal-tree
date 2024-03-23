# Fractal-tree

## Fractal tree index
The fractal tree index, also known as the fractal trie or fractal tree, is a data structure designed for efficient information retrieval and storage in fractal metric spaces. It is particularly useful for handling high-dimensional data, such as multimedia data (images, audio, video), genomic data, and time-series data.

![Fractal tree](/img/tree.png)

The fractal tree index is based on the concept of self-similarity, a property exhibited by fractals. It recursively partitions the metric space into smaller and smaller regions, creating a tree-like structure. Each node in the tree represents a subset of the data points, and the tree's structure reflects the hierarchical clustering of the data.

### Construction

Let $S$ be a set of $n$ data points in a metric space $(X, d)$, where $d$ is the distance metric.

1. Select a "pivot" element $p \in S$.

2. Partition the remaining elements based on their distances from $p$:
$$S_i = \{x \in S \setminus \{p\} : r_i \leq d(x, p) < r_{i+1}\}$$
where $r_1, r_2, \ldots, r_m$ are appropriately chosen radii.

3. Recursively construct fractal tree indices for each non-empty subset $S_i$.

The resulting tree structure has the pivot $p$ as the root node, and the subtrees correspond to the subsets $S_i$.

## L-system

An L-system, or Lindenmayer system, is a parallel rewriting system that models the growth and development of various organisms and structures, particularly in the context of fractal geometry.

![L-system](/img/l_system.png)

**L-system trees form realistic models of natural patterns**

In an L-system, the growth process is defined by a set of rules that govern the transformation of an initial string of symbols (called the axiom) through successive iterations. The resulting strings represent the different stages of growth or development.

The formal definition of an L-system is given as follows:

An L-system is a triple $G = (V, \omega, P)$, where:

- $V$ is the alphabet, a finite set of symbols.
- $\omega \in V^*$ is the axiom, a string of symbols from $V$ that represents the initial state.
- $P \subseteq V \times V^*$ is a finite set of production rules, which determine how the symbols in the string are replaced in each iteration.

The production rules in $P$ take the form:

$$a \rightarrow \chi$$

where $a \in V$ is a symbol from the alphabet, and $\chi \in V^*$ is a string of symbols that replaces $a$ in the next iteration.

The growth process of an L-system is defined by the following steps:

1. Start with the axiom $\omega$.
2. For each iteration:
    a. Scan the current string from left to right.
    b. Replace each symbol $a$ in the string with the corresponding string $\chi$ specified by the production rule $a \rightarrow \chi$.
    c. Concatenate the resulting strings in the same order to form the new string for the next iteration.

This process continues indefinitely or until a specified termination condition is met.

## Turtle graphics

Turtle graphics is a programming paradigm and a way of teaching programming, where a virtual turtle (or cursor) is controlled by a set of commands to draw various shapes, patterns, and designs on a Cartesian plane. The turtle is initially positioned at the origin (0, 0) of the plane and can move forward or backward, turn left or right, and control its pen to draw or not draw as it moves.

![Turtle graphics](https://upload.wikimedia.org/wikipedia/commons/3/3d/Turtle-animation.gif)

**An animation that shows how the turtle is used to create graphics by combining forward and turn commands while a pen is touching the paper**

The basic commands in turtle graphics are:

- `forward(d)` or `fd(d)`: Moves the turtle forward by a distance `d` in the current direction, drawing a line if the pen is down.
- `backward(d)` or `bk(d)`: Moves the turtle backward by a distance `d` in the opposite direction of its current heading, drawing a line if the pen is down.
- `left(angle)` or `lt(angle)`: Rotates the turtle counterclockwise by the given `angle` in degrees.
- `right(angle)` or `rt(angle)`: Rotates the turtle clockwise by the given `angle` in degrees.
- `penup()` or `pu()`: Raises the pen, so the turtle's movement does not draw a line.
- `pendown()` or `pd()`: Lowers the pen, so the turtle's movement draws a line.
- ...

## Code realization, construction of fractals and fractal curves

The `main.py` file contains the code implementation for generating fractal-like structures using recursive L-systems and rendering them using turtle graphics.

### Functionality

1. **FractalSystem Abstract Base Class**:
    - Defines an abstract base class `FractalSystem` with two abstract methods:
        - `apply_rules(axiom)`: Applies production rules to the given axiom string.
        - `get_result(gens, axiom)`: Generates the final string by applying rules for the given generations and an initial axiom.

2. **LSystem Class**:
    - Inherits from `FractalSystem` and implements the L-system for generating fractal-like structures.
    - Attributes:
        - `axiom`: Initial axiom string.
        - `rules`: Dictionary containing production rules.
        - `num_gens`: Number of generations for the fractal system (default value is 13).
    - Methods:
        - `apply_rules(axiom)`: Applies rules to the given axiom string based on the rules dictionary.
        - `get_result(gens, axiom)`: Generates a result based on the given number of generations and an initial axiom.

3. **FractalRenderer Class**:
    - Handles the rendering of fractal structures using turtle graphics.
    - Attributes:
        - `screen`: Turtle screen for drawing.
        - `turtle`: Turtle object for drawing shapes.
        - `step`: Length of each step in drawing the fractal.
        - `angle`: Lambda function for generating random angles during drawing.
        - `stack`: Stack for saving turtle states during drawing.
        - `color`: List representing the RGB color values for drawing.
        - `thickness`: Thickness of the lines drawn by the turtle.
    - Methods:
        - `render(fractal_system)`: Renders the fractal structure using the given fractal system.
        - `plant_system`: Property that defines an L-system for generating a plant-like structure.
        - `run()`: Initiates the rendering process.

### Usage

To run the code and generate a fractal tree structure:
1. Ensure you have Python installed on your system.
2. Run the `main.py` script using a Python interpreter.
3. The script will generate and render the fractal tree using turtle graphics.

For customization, you can modify the L-system rules, step size, colors, and other parameters within the `main.py` file.

### Preview

![Result](/img/result.png)