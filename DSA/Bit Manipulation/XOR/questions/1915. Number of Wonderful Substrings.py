class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        # Optimized solution
        # there are two subtask in this question, 
        # 1. To find those substring where every character count is even
        # 2. to find those substring where atmost one char count is odd

        # Mere se nahi bana, bilkul bhi nahi smjh aaya kuchh bhi. I tool help from here and editorials - https://youtu.be/1DdmbJj4xLE

        mapp = {}
        mapp[0] = 1
        pfix,n,count = 0,len(word),0

        for ch in word:
            char = ord(ch) - ord('a') # converting to ascii
            pfix ^= 1 << char  # this thing convert number to binary

            if pfix in mapp:
                count += mapp[pfix] # Subtask 1 completed here

            # Subtask 2
            for i in range(10):
                char1 = 1 << i # (a to j)
                if pfix ^ char1 in mapp:
                    count += mapp[pfix ^ char1]
            # Subtask 2 completed
            
            if pfix in mapp:
                mapp[pfix] = 1 + mapp[pfix]
            else:
                mapp[pfix] = 1
        
        return count

# https://leetcode.com/problems/number-of-wonderful-substrings/
