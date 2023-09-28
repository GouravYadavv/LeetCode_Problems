class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans=""
        if len(word1)>len(word2):
            bada=word1
            chota=word2
        else:
            bada=word2
            chota=word1
        for i in range(len(bada)):
            if i>=len(chota):
                ans+=bada[i]
            else:
                ans+=word1[i]
                ans+=word2[i]
        return ans