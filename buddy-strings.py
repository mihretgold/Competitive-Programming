class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        lengthS = len(s)
        lengthGoal = len(goal)
        countS = Counter(s)
        countGoal = Counter(goal)

        if lengthS != lengthGoal:
            return False

        if s == goal:
            maxi = max(countS.values())
            if maxi <= 1:
                return False
            else:
                return True

        answer = False
        count = 0

        for index in range(lengthS):
            if s[index] != goal[index]:
                count += 1

        if count == 2 and countS == countGoal:
            answer = True


        return answer