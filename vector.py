from math import dist


class Vector():

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y) if isinstance(other, Vector) else NotImplemented

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return NotImplemented

    def __truediv__(self, other):
        return Vector(self.x / other, self.y / other) if isinstance(other, (int, float)) else NotImplemented

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y if isinstance(other, Vector) else NotImplemented

    def __pos__(self):
        return self

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __iter__(self):
        for i in (self.x, self.y):
            yield i

    def norm(self):
        return dist((0, 0), (self.x, self.y))

    def normalized(self):
        return self / self.norm()

# def test():
#     v = Vector(2, 3)
#     w = Vector(4, 5)
#     z = Vector(2.8, -6.7)
#     unit = Vector(1, 1)
#     print(v)
#     print(v.x)
#     print(v.y)
#     print(w)
#     print(v + w)
#     print(z)
#     print(+z)
#     print(-z)
#     print(v*5)
#     print(tuple(v))
#     print(v / 2)
#     print(v * 2)
#     print(v * unit)
#     print(v.normalized())
#     print(v == Vector(2, 3))
#     print(v == Vector(2, 4))
#     print(v != Vector(2, 4))
#     print(v != Vector(2, 3))

# if __name__ == "__main__":  # Python syntax that means "if you are launching from this file, run main()", useful if this file is going to be imported.
#     test()