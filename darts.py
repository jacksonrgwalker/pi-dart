from dataclasses import dataclass


@dataclass
class Dart:

    x: float = 0.0
    y: float = 0.0

    def distance_from_origin(self):

        return (self.x**2 + self.y**2)**0.5

    @classmethod
    def throw(cls, x_bounds=None, y_bounds=None):

        import random

        if x_bounds is None:
            x_bounds = (-1, 1)
        if y_bounds is None:
            y_bounds = (-1, 1)

        x, y = random.uniform(*x_bounds), random.uniform(*y_bounds)

        return cls(x, y)


class DartSet:

    def __init__(self, darts):

        self.darts = darts

    def __len__(self):

        return len(self.darts)

    @property
    def x(self):

        return [p.x for p in self.darts]

    @property
    def y(self):

        return [p.y for p in self.darts]

    def distance_from_origin(self):

        return [dart.distance_from_origin() for dart in self.darts]

    @classmethod
    def throw_all(cls, n, x_bounds=None, y_bounds=None):

        return cls([Dart.throw(x_bounds, y_bounds) for _ in range(n)])
