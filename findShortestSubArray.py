class Solution(object):
    def findShortestSubArray(self, nums):
        opt = {}
        opt[nums[0]] = 1
        pathWatcher = {}
        pathWatcher[nums[0]] = 0
        max_contigous = 0
        max_size = float('inf')
        cur_smallest = -1
        for i in range(1, len(nums)):
            if nums[i] in opt:
                opt[nums[i]] += 1
            else:
                opt[nums[i]] = 1
                pathWatcher[nums[i]] = i
            if opt[nums[i]] >= max_contigous and opt[nums[i]] > 1:
                max_contigous = opt[nums[i]]
                if nums[i] == cur_smallest:
                    max_size = i - pathWatcher[nums[i]]
                elif i - pathWatcher[nums[i]] < max_size or opt[nums[i]] > opt[cur_smallest]:
                    max_size = i - pathWatcher[nums[i]]
                    cur_smallest = nums[i]
        if cur_smallest == -1:
            return 1
        return (max_size + 1)
        """
        :type nums: List[int]
        :rtype: int
        """
