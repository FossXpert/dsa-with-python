# letter se digit bnakar unka divisibilty test karna

class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        # Took help, apne se bilkul bhi nahi soch paya
        # got idea from here : https://leetcode.com/discuss/post/5119937/prefix-sum-problems-by-c0d3m-08l9
        # and here: https://leetcode.com/problems/find-the-divisibility-array-of-a-string/solutions/3231219/explained-reminder-checking-very-simple-hh0dx

        # mY PERSONAL take : Bro see aap jaise numbers ko divide karte to practiacally bas waise hi karna hai. just pen and paer pe jaise karte ho waise hi karna as simple as that, and usi ko code me likh dena hai bas
        # ek aur cheez jab bhi hm modulo lete hai, to remainder hmesha divisor se kam hi hota hai, i.e:  
        # Given two integers a and b, with b ≠ 0, a = bq + r , where 0 ≤ r < |b|
        ans = []
        num = 0
        for letter in word:
            num = 10 * num + int(letter)
            num = num % m
            if num == 0:
                ans.append(1)
            else:
                ans.append(0)
        return ans

#https://leetcode.com/problems/find-the-divisibility-array-of-a-string