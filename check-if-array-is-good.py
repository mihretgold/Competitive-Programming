class Solution:
    def isGood(self, nums: List[int]) -> bool:
        permutation = Counter(nums)
        length = len(nums)
        if length <= 1:
            return False

        for index in range(length-1, 0, -1):
            # print(index, permutation[index])
            if index == length-1:
                if permutation[index] != 2:
                    return False
            else:
                if permutation[index] != 1:
                    return False


        return True