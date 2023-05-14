# Instructions :
# The goal is to create a class that represents a simple circle.
# A Circle can be defined by either specifying the radius or the diameter.
# The user can query the circle for either its radius or diameter.
#
# Other abilities of a Circle instance:
#
# Compute the circle’s area
# Print the circle and get something nice
# Be able to add two circles together
# Be able to compare two circles to see which is bigger
# Be able to compare two circles and see if there are equal
# Be able to put them in a list and sort them
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
