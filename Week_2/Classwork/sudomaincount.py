import collections
from typing import List

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        ans = collections.Counter()
        for domains in cpdomains:
            count, domains = domains.split()
            
            count = int(count)

            frags = domains.split('.')
            # print(frags)

            for i in range(len(frags)):
                # print(frags[i:])
                print( ".".join(frags[i:]))
                ans[".".join(frags[i:])] += count


        formatted_list = []
        for dom,ct in ans.items():
            formatted_string = "{} {}".format(ct,dom)
            formatted_list.append(formatted_string)
        
        return formatted_list 

if __name__ == "__main__":
    sol = Solution()
    print(sol.subdomainVisits(["9001 discuss.leetcode.com"]))
        