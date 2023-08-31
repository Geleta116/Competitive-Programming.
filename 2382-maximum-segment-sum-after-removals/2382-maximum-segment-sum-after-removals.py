class Solution:
    def find(self, i, ds):
        return i if ds[i] < 0 else self.find(ds[i], ds)

    def merge(self, s1, s2, ds):
        p1 = self.find(s1, ds)
        p2 = self.find(s2, ds)
        ds[p2] += ds[p1]
        ds[p1] = p2

    def maximumSegmentSum(self, nums, rq):
        res = [0] * len(nums)
        ds = [float('inf')] * len(nums)

        for i in range(len(rq) - 1, 0, -1):
            j = rq[i]
            ds[j] = -nums[j]

            if j > 0 and ds[j - 1] != float('inf'):
                self.merge(j, j - 1, ds)
            if j < len(nums) - 1 and ds[j + 1] != float('inf'):
                self.merge(j, j + 1, ds)

            res[i - 1] = max(res[i], -ds[self.find(j, ds)])

        return res
