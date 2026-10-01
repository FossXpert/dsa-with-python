# I knew the answer when i was solving prefix sum question as it can be solved by 1D-differential array method 

# but this format i was not aware of, so i needed to refer this solution - https://leetcode.com/problems/my-calendar-ii/solutions/323479/simple-c-solution-using-built-in-map-sam-6m1i
# same concept like 253. Meeting Rooms II
from sortedcontainers import SortedDict
class MyCalendarTwo:

    def __init__(self):
        self.mapp = SortedDict()

    def book(self, startTime: int, endTime: int) -> bool:
        self.mapp[startTime] = 1 + self.mapp.get(startTime,0)
        self.mapp[endTime] = -1 + self.mapp.get(endTime,0)
        
        temp = 0
        for x in self.mapp:
            temp += self.mapp[x]
            if temp == 3:
                self.mapp[startTime] -= 1
                self.mapp[endTime] += 1
                return False
        return True    


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()

# https://leetcode.com/problems/my-calendar-ii/