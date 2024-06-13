class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:      
        x=sorted(seats)
        a=sorted(students)
        c=0
        for i in range(len(a)):
            c+=abs(x[i]-a[i])
        return c