class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        tests = minutesToTest//minutesToDie
        
        answer = math.log(buckets, tests + 1)
        # print(answer)
        val = int(answer)
        if answer > val + 0.1:
            answer = ceil(answer)
        else:
            answer = val
       
        return answer
        
        