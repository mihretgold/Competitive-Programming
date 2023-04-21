class ThroneInheritance:

    def __init__(self, kingName: str):
        self.inheritance = defaultdict(list)
        self.king = kingName
        self.deathList = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.inheritance[parentName].append(childName)

    def death(self, name: str) -> None:
        self.deathList.add(name)
        

    def getInheritanceOrder(self) -> List[str]:
        self.answer = [self.king]
        visted = set()
        
        def dfs(parent):
            visted.add(parent)
            for child in self.inheritance[parent]:
                if child not in visted:
                    # print(child)
                    self.answer.append(child)
                    dfs(child)


        dfs(self.king)
        print(self.answer)
        result = []
        for curr in self.answer:
            if curr not in self.deathList:
                result.append(curr)
        
        self.answer = result
        return self.answer
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()