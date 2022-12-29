class Solution:                
    def countPairs(self, deliciousness: List[int]) -> int:
        length = len(deliciousness)
        power_two = defaultdict(int)
        power_two[deliciousness[0]] += 1
        
        map_pow = []
        count = 0
        for index in range(22):
            map_pow.append(2**index)
        
        for index in range(1, length):
            temp = deliciousness[index]
            for num in map_pow:
                if num - temp in power_two:
                    count += power_two[num - temp]
            power_two[temp] += 1
        
        return count % (10**9 + 7)
   
                
                