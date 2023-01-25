class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        end = len(people) - 1
        start = 0
        count = 0
        while start <= end:
            if people[start] + people[end] <= limit:
                count += 1
                start += 1
                end -= 1
            elif people[end] <= limit:
                count += 1
                end -= 1
                
        return count