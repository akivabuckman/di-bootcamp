import math


class Circle:
    circles = []

    def __init__(self, radius=None, diameter=None):
        self.radius = radius if radius else diameter / 2
        self.area = math.pi * self.radius ** 2
        Circle.circles.append(self)

    def __repr__(self):
        return "Here's a fancy circle: O"

    def __iadd__(self, other):
        self.radius += other.radius
        return self

    def __gt__(self, other):
        return self.radius > other.radius

    def __eq__(self, other):
        return self.radius == other.radius
