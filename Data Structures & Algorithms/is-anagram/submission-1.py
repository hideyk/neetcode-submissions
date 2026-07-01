from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = defaultdict(int)
        for letter in s:
            d[letter] += 1
        for letter in t:
            d[letter] -= 1

        for k, v in d.items():
            if v != 0:
                return False
        return True