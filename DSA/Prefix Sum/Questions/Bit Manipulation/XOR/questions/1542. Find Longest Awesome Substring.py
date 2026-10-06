class Solution:
    def longestAwesome(self, s: str) -> int:
        # using concept from this question : https://leetcode.com/problems/number-of-wonderful-substrings/description
        
        length,n,pfix,mapp = 0,len(s),0,{}
        mapp[0] = 0

        for i in range(n):
            pfix ^= 1<<int(s[i])
            #subtask 1: FInding the longest substring having even count of digits
            if pfix in mapp:
                length = max(length,i+1 - mapp[pfix])

            #subtask 2: finding the substring having atmost one digit in odd count (eg, 76263)
            for j in range(10):
                pfix1 = pfix ^ 1<<int(j)
                if pfix1 in mapp:
                    length = max(length,i+1 - mapp[pfix1])
            
            if pfix in mapp:
                mapp[pfix] = min(mapp[pfix], i+1)
            else:
                mapp[pfix] = i+1

        return length