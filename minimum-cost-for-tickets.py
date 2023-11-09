class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @cache
        def calc(total):
            if total > days[-1]:
                return 0

            seven, thirty = float('inf'), float('inf')
            if total not in visted:
                one = calc(total + 1)
            else:
                one = costs[0] + calc(total + 1)
                seven = costs[1] + calc(total + 7)
                thirty = costs[2] + calc(total + 30)        
                

            return min(one, seven, thirty)

        visted = set(days)

        return calc(1)