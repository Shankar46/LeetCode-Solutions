class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        maxs=0
        max_apples=0
        while max_apples<neededApples:
            maxs+=1
            max_apples+=(12*maxs*maxs)
        return (8*maxs)