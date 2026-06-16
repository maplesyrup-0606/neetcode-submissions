class CountSquares:
    def __init__(self):
        self.mpX = defaultdict(list) # maps mp[x] = y
        self.mpY = defaultdict(list)
        self.pointCount = defaultdict(int)
    def add(self, point: List[int]) -> None:
        x, y = point 
        self.mpX[x].append(y)
        self.mpY[y].append(x)
        self.pointCount[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        x1, y1 = point 
        print(self.pointCount)
        vert = self.mpX[x1]
        horiz = self.mpY[y1]

        """
            Now for each point in vertical and horizontal
            see if [x1 + dx, y1 + dy] exists
        """
        
        res = 0
        visited = set()
        for y2 in vert:
            for x2 in horiz:
                points = [[x1, y1], [x2, y1], [x1, y2], [x2, y2]]
                if points.count([x1, y1]) > 1:
                    continue
                points.sort()
                strSeq = ""
                for u, v in points:
                    strSeq += str(u) + str(v)
                print(points, strSeq, visited)
                if strSeq in visited:
                    continue
                visited.add(strSeq)
                """
                    We have three points now:
                        (x1, y1),
                        (x1, y2),
                        (x2, y1)
                """
                if y2 in self.mpX[x1] and x2 in self.mpY[y1]:
                    print(strSeq)
                    res += self.pointCount[(x1, y2)] * self.pointCount[(x2, y1)] * self.pointCount[(x2, y2)]
        
        return res
                