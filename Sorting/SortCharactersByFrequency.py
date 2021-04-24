from collections import defaultdict


class Solution:
    def frequencySort(self, s: str) -> str:
        d = defaultdict(int)

        for c in s:
            d[c] += 1

        d = sorted(d.items(), key=lambda kv: (kv[1]), reverse=True)

        res = ""

        for ele in d:
            for i in range(ele[1]):
                res += ele[0]

        return (res)
