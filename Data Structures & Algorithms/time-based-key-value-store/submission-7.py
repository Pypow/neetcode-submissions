class TimeMap:

    def __init__(self):
        self.hmap = {}  # key: (timestamp, value)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hmap:
            self.hmap[key] = [] 
        self.hmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hmap:
            return ""
        values = self.hmap[key]
        l, r = 0, len(values) -1        # imp
        res = None
        while l <= r:
            m = (l + r) // 2
            if values[m][0] > timestamp:
                r = m - 1
            elif values[m][0] < timestamp:
                l = m + 1
                res = values[m][1]
            else:   
                return values[m][1]
        return "" if res is None else res
