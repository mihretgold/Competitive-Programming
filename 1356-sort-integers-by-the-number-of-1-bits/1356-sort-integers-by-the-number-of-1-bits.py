class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        store = defaultdict(list)
        for num in arr:
            string = bin(num)[2:]
            ones = string.count("1")
            store[ones].append(num)
            
        store = OrderedDict(sorted(store.items()))
        answer = []
        
        for num in store:
            nums = sorted(store[num])
            answer.extend(nums)
        
        return answer