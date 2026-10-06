# https://leetcode.com/problems/remove-interval/description/
# https://algo.monster/liteproblems/1272#editor


def remove_interval(intervals: list[list[int]], to_be_removed: list[int]) -> list[list[int]]:
    # WRITE YOUR BRILLIANT CODE HERE
    mapp = {}

    for i in range(len(intervals)):
        L = intervals[i][0]
        R = intervals[i][1]
        mapp[L] = 1 + mapp.get(L,0)
        mapp[R] = -1 + mapp.get(R,0)

    L = to_be_removed[0]
    R = to_be_removed[1]
    mapp[L] = -1 + mapp.get(L,0)
    mapp[R] = 1 + mapp.get(R,0)

    keys = sorted(mapp.keys())
    count = 0
    isPos = False
    result = []
    for i in range(len(mapp)):
        count += mapp[keys[i]]
        if count >0 and isPos == False:
            first = keys[i]
            isPos = True

        if count == 0 and isPos == True:
            last = keys[i]
            result.append([first,last])
            isPos = False
        
    return result

if __name__ == "__main__":
    intervals = [[int(x) for x in input().split()] for _ in range(int(input()))]
    to_be_removed = [int(x) for x in input().split()]
    res = remove_interval(intervals, to_be_removed)
    for row in res:
        print(" ".join(map(str, row)))
