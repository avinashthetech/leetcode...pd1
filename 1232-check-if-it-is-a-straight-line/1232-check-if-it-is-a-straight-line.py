class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if (coordinates[0][0]-coordinates[1][0])!=0:
            slope=(coordinates[0][1]-coordinates[1][1])/((coordinates[0][0]-coordinates[1][0]))
        else:slope=10000
        i=0
        l=len(coordinates)
        while i<l-1:
            if (coordinates[i][0]-coordinates[i+1][0])!=0:
                
                m=(coordinates[i][1]-coordinates[i+1][1])/((coordinates[i][0]-coordinates[i+1][0]))
            else:m=10000
            if m!=slope:
                return False
            i+=1
        return True