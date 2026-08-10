class Solution:
    def minWindow(self, s: str, t: str) -> str:

        #invalid edge case
        if t == "":
            return ""
        
        #initialize 2 hashmaps
        countT, window = {}, {}
        # count characters in t
        for c in t:
            countT[c] = 1+ countT.get(c,0)

        #initialize
        have, need = 0, len(countT)
        res, resLen = [-1,-1], float("infinity")
        l = 0

        #expand window
        for r in range(len(s)):
            c = s[r]
            window[c] = 1+ window.get(c,0)

            # Check if this char satisfies requirement
            if c in countT and window[c] == countT[c]:
                have +=1

            #Shrink window while valid
            while have == need:
                #Update result
                if (r-l+1) < resLen:
                    res = [l,r]
                    resLen = (r-l+1)

                # Remove left char
                window[s[l]] -= 1

                # Check if window becomes invalid
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -=1

                l+=1

        l,r = res
        return s[l:r+1] if resLen != float("infinity") else ""


                


