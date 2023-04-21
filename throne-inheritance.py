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
        self.answer = []
        
        def dfs(parent):
            if parent not in self.deathList:
                self.answer.append(parent)
            for child in self.inheritance[parent]:
                dfs(child)


        dfs(self.king)
        return self.answer
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()