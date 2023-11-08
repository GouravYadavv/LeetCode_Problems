from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="": return ""

        countT,window=Counter(t),{}

        l=0
        have=0
        need=len(countT)
        res=[-1,-1]
        resL=float("infinity")

        for r in range(len(s)):
            window[s[r]]=1+window.get(s[r],0)

            if s[r] in countT and window[s[r]]==countT[s[r]]:
                have+=1
            
            while have==need:
                if r-l+1<resL:
                    resL=r-l+1
                    res=[l,r]

                window[s[l]]-=1
                if s[l] in countT and window[s[l]]<countT[s[l]]:
                    have-=1
                l+=1
        return "" if resL==float("infinity") else s[res[0]:res[1]+1]