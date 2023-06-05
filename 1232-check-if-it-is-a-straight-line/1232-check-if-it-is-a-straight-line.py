class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:   return True
        try:
            slope = (coordinates[1][1]-coordinates[0][1])/(coordinates[1][0]-coordinates[0][0])
        except ZeroDivisionError:
            return len(set([p[0] for p in coordinates])) == 1
        offset = coordinates[0][1] - slope*coordinates[0][0]
        return all([coordinates[i][0]*slope+offset == coordinates[i][1] for i in range(2, len(coordinates))])