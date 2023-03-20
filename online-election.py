class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.dicts = defaultdict(int)
        self.length = len(persons)
        leader = persons[0]
        self.election = []
        for i in range(self.length):
            self.dicts[persons[i]] += 1
            if self.dicts[persons[i]] >= self.dicts[leader]:
                leader = persons[i]
            self.election.append(leader)

        self.votes = list(zip(times, self.election))


    def q(self, t: int) -> int:
        low = 0
        high = self.length-1
        while low <= high:
            mid = low + (high - low)//2
            if self.votes[mid][0] <= t:
                low = mid + 1
            else:
                high = mid - 1
        

        return  self.votes[high][1]     
        
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)