from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        S,P = len(s),len(p)
        if S < P:
            return []
            #in case the length of S is shorter than P
        
        p_count = Counter(p)
        s_count = Counter()

        output = []

        for i in range(S):
            s_count[s[i]] += 1
            #populating the hash map
            #a 1 b 1 c 1 etc.

            if i>=P: #to ensure the sliding window has the length equal to or less than the length of p
                if s_count[s[i-P]] == 1:
                    del s_count[s[i-P]]
                else:
                    s_count[s[i-P]] -= 1
            
            if p_count == s_count:
                output.append(i-P+1)
        
        return output



        