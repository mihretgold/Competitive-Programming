class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        answer = []
        queen_set = tuple(map(tuple,queens))
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        
        for dx, dy in direction:
            cur_x = king[0]
            cur_y = king[1]
            while cur_x >= 0 and cur_y >= 0 and cur_x < 8 and cur_y < 8:
                if (cur_x, cur_y) in queen_set:
                    answer.append([cur_x, cur_y])
                    break
                cur_x += dx
                cur_y += dy
            
        return answer
            
                    