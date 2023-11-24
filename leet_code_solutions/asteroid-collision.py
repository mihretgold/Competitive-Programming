class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        length = len(asteroids)

        for idx in range(length):
            # print(stack)
            if stack:
                check = (stack[-1] > 0 and asteroids[idx] < 0)
                
            if not stack or not check:
                stack.append(asteroids[idx])

            elif check:
                if abs(stack[-1]) > abs(asteroids[idx]):
                    continue
                if abs(stack[-1]) == abs(asteroids[idx]):
                    stack.pop()
                else:
                    val = float('inf')
                    while stack and (stack[-1] > 0 and asteroids[idx] < 0) and abs(stack[-1]) <= abs(asteroids[idx]):

                        val = stack.pop()
                        if abs(val) == abs(asteroids[idx]):
                            break
                    if stack:
                        check = (stack[-1] > 0 and asteroids[idx] < 0)
                    
                    if (not stack and abs(asteroids[idx]) > abs(val)) or (stack and abs(asteroids[idx]) > abs(val) and (not check or (check and abs(stack[-1]) < abs(asteroids[idx])))):
                        stack.append(asteroids[idx])
            

            
        return stack
        