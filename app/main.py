"""
Fractal construction and fractal curves using recursive L-systems.
And in particular, the construction of a plausible fractal tree
"""

import turtle
from random import randint
from abc import ABC, abstractmethod
from dataclasses import dataclass
from functools import cached_property

class FractalSystem(ABC):
    """Abstract base class for fractal systems"""

    @abstractmethod
    def apply_rules(self, axiom):
        """Apply production rules to the axiom"""
        pass # pylint: disable=W0107

    @abstractmethod
    def get_result(self, gens, axiom):
        """Generate the final string by applying rules for the given generations"""
        pass # pylint: disable=W0107

@dataclass
class LSystem(FractalSystem):
    """L-System for generating fractal-like structures"""
    axiom: str
    rules: dict[str, str]
    num_gens: int = 13

    def apply_rules(self, axiom):
        """
        Apply rules to the given axiom string based on the rules dictionary,
        return the modified string
        """
        return ''.join(self.rules.get(char, char) for char in axiom)

    def get_result(self, gens, axiom):
        """
        Generates a result based on the given number of generations and an initial axiom
        """
        result = axiom
        for _ in range(gens):
            result = self.apply_rules(result)
        return result

class FractalRenderer:
    """Renders fractal structures using turtle graphics"""

    def __init__(self, width=800, height=600):
        """
        The __init__ function is called when the class is instantiated.
        It sets up the screen and turtle for drawing, as well as initializing some variables.
        """
        self.screen = turtle.Screen()
        self.screen.setup(width, height)
        self.screen.bgcolor('black')
        self.screen.delay(0)

        self.turtle = turtle.Turtle()
        self.turtle.pensize(3)
        self.turtle.speed(0)
        self.turtle.penup()
        self.turtle.setpos(0, -150)
        self.turtle.pendown()
        self.turtle.color('green')

        self.step = 60
        self.angle = lambda: randint(0, 45)
        self.stack = []
        self.color = [0.35, 0.2, 0.0]
        self.thickness = 13

    def render(self, fractal_system):
        """Render the fractal structure using the given fractal system"""
        axiom = fractal_system.get_result(fractal_system.num_gens, fractal_system.axiom)
        self.turtle.left(90)
        self.turtle.pensize(self.thickness)

        for char in axiom:
            self.turtle.color(self.color)
            if char == 'F' or char == 'X':
                self.turtle.forward(self.step)
            elif char == '@':
                self.step -= 4
                self.color[1] += 0.04
                self.thickness -= 1
                self.thickness = max(1, self.thickness)
                self.turtle.pensize(self.thickness)
            elif char == '+':
                self.turtle.right(self.angle())
            elif char == '-':
                self.turtle.left(self.angle())
            elif char == '[':
                angle, pos = self.turtle.heading(), self.turtle.pos()
                self.stack.append((angle, pos, self.thickness, self.step, self.color[1]))
            elif char == ']':
                angle, pos, self.thickness, self.step, self.color[1] = self.stack.pop()
                self.turtle.pensize(self.thickness)
                self.turtle.setheading(angle)
                self.turtle.penup()
                self.turtle.goto(pos)
                self.turtle.pendown()

    @cached_property
    def plant_system(self):
        """L-System for generating a plant-like structure"""
        rules = {
            'X': 'F[@[-X]+X]'
        }
        return LSystem('XY', rules)

    def run(self):
        """Start the rendering process"""
        self.render(self.plant_system)
        self.screen.exitonclick()

if __name__ == '__main__':
    renderer = FractalRenderer()
    renderer.run()
