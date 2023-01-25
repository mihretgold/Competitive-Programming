class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        length = len(skill)
        start = 0 
        end = length - 1
        count = 0
        sum = 0
        target = skill[start] + skill[end]
        while(start < end):
            if target == skill[start] + skill[end]:
                sum += skill[start] * skill[end]
                count += 1
                start += 1
                end -= 1
            else:
                break
        ans = -1        
        if count == length//2:
            ans = sum
        
        return ans

                

        