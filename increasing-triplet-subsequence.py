class Solution:

    '''
    val1, val2
    Algo
    if num if < val1 num repalace val1
    if num < val2 replace val2
    if num > val2 return True
    '''
    def increasingTriplet(self, nums: List[int]) -> bool:
        val1, val2 = float('inf'), float('inf')
        for num in nums:
            if num > val1 and num < val2:
                val2 = num
            elif num < val1:
                val1 = num
            if num > val2:
                return True

        return False