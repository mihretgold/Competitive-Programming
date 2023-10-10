class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        prevGas = gas[0]
        negatives = 0
        length = len(gas)
        idx = -1

        for index in range(length):
            nextGas = 0
            if index < length - 1:
                nextGas = gas[index + 1]
            prevGas = prevGas - cost[index] 
            if prevGas < 0:
                negatives += prevGas
                prevGas = 0
                idx = -1
            elif idx == -1:
                idx = index

            prevGas += nextGas

        answer = prevGas + negatives 
        

        if answer < 0:
           return -1
        return idx