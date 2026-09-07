class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # Beautiful Question, apne se 90% bnaya, bas wo part jaha constants ko 0 man lena hai wo apne se nahi figure out karpaya
        # use example : kkeleetminikk
        # used concept from this question - https://leetcode.com/problems/number-of-wonderful-substrings/description


        n, length, pfix, mapp = len(s), 0, 0, {}
        mapp[0] = 0
        cnt =0

        vowel = ["a", "e", "i", "o", "u"]
        for i in range(n):
            if s[i] in vowel:
                char = ord(s[i]) - ord("a")
                pfix ^= 1 << char
            else:
                pfix ^= 0 

            if pfix in mapp:
                length = max(length, i + 1 - mapp[pfix])

            if pfix in mapp:
                mapp[pfix] = min(i + 1, mapp[pfix])
            else: 
                mapp[pfix] = i + 1
        return length



# https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts