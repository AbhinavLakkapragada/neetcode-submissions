class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # step 1: edge case
        if len(s1)>len(s2):
            return False

        # step 2: create frequency arrays for lowercase letters
        count_s1 = [0] * 26
        count_window = [0] * 26

        # step 3: fill count_s1 and initial window count
        for i in range(len(s1)):
            count_s1[ord(s1[i]) - ord('a')] += 1
            count_window[ord(s2[i]) - ord('a')] +=1
        
        # step 4: slide the window
        l = 0 # left pointer of the window
        for r in range(len(s1), len(s2)):
            #step 4a. check if current window matches s1
            if count_s1 == count_window:
                return True

            # step4b. slide window by 1
            #remove the leftmost character from window
            count_window[ord(s2[l]) - ord('a')] -=1
            l+=1
            count_window[ord(s2[r]) - ord('a')] +=1

        # step5: final check for the last window
        return count_s1 == count_window
        