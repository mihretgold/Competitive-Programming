class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = defaultdict(int)

        for index, num in enumerate(nums):
            find = target - num
            if find in store:
                return [store[find], index]

            store[num] = index


        return  []


        