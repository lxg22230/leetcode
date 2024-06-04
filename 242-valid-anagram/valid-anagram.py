class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = dict()
        for char in s:
            counter[char] = counter.get(char,0) + 1
        for char in t:
            counter[char] = counter.get(char,0) - 1
        for _,value in counter.items():
            if value != 0:
                return False
        return True

        