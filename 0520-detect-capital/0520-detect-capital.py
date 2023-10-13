class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word==word.upper() or word==word.lower() or word==word.title():
            return True
        return False