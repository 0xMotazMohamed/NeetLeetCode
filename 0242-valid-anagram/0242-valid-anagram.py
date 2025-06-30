class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return bool(sorted(s)==sorted(t))