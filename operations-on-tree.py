class LockingTree:

    def __init__(self, parent: List[int]):
        self.graph = defaultdict(list)
        self.revGraph = defaultdict(list)
        for end, start in enumerate(parent):
            if start != -1:
                self.graph[start].append(end)
                self.revGraph[end].append(start)

        self.locking = defaultdict(int)


    def lock(self, num: int, user: int) -> bool:
        if self.locking[num] == 0:
            self.locking[num] = user
            return True
        return False
        

    def unlock(self, num: int, user: int) -> bool:
        if self.locking[num] == user:
            self.locking[num] = 0
            return True
        return False


    def upgrade(self, num: int, user: int) -> bool:
        def lockDes(vertex):
            if self.locking[vertex] != 0:
                return True

            for child in self.graph[vertex]:
                if lockDes(child):
                    return True
            return False

        def unlockAnces(vertex):
            if self.locking[vertex] != 0:
                return False

            for child in self.revGraph[vertex]:
                if not unlockAnces(child):
                    return False
            return True
        def unlockDes(vertex):

            for child in self.graph[vertex]:
                if self.locking[child] != 0:
                    self.locking[child] = 0
                unlockDes(child)
           
        # print(self.locking[num],lockDes(num), unlockAnces(num))
        if self.locking[num] == 0:
            if lockDes(num):
                if unlockAnces(num):
                    ans = self.lock(num, user)
                    unlockDes(num)
                    return True

        return False


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)