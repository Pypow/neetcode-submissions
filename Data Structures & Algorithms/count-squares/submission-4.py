class CountSquares:

    def __init__(self):
        self.hmap = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        self.hmap[tuple(point)] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        # Find Diagonal point, then count remaining points
        # difference of two diagonal points of x and y are equal (10, 5) - (12, 3) = (2, 2)
        res = 0
        px, py = point
        for x, y in self.points:
            if (abs(px - x) != abs(py - y)) or x == px or y == py:  # also elimate super imposed points
                continue
            # see if other two points exist, and get product to find total squares possible 
            res += self.hmap[(x, py)] * self.hmap[(px, y)]
        return res
