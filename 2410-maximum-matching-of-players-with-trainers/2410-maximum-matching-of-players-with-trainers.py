class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        play = 0
        train = 0
        lenPlay = len(players)
        lenTrain = len(trainers)
        count = 0
        while play < lenPlay and train < lenTrain:
            if players[play] <= trainers[train]:
                count += 1
                play += 1
           
            train += 1
            
        return count