class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner_map = defaultdict(int)
        losser_map = defaultdict(int)
        winner = []
        losser = []
        answer = []
        
        # Add 1st index to winner map and 2nd index to losser map
        for num in matches:
            winner_map[num[0]] += 1
            losser_map[num[1]] += 1
        
        #check if keys in winner map are in losser map
        for num in winner_map:
            if num not in losser_map:
                winner.append(num)
        winner.sort()
        answer.append(winner)
        
        # Find only 1 time lossers
        for num in losser_map:
            if losser_map[num] == 1:
                losser.append(num)
        losser.sort()
        answer.append(losser)
        
        return answer
        
                
           