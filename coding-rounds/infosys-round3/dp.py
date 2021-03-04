import collections
class Solution(object):
    def subarraysDivByK(self, A, K):
        P = [0]
        for x in A:
            P.append((P[-1] + x) % K)
        print(P)
        count = collections.Counter(P)
        print(count)
        return sum(v*(v-1)/2 for v in count.values())
s=Solution()
print(s.subarraysDivByK([3,5,1],3))