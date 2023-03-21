class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        additive = []
        if len(num) < 3:
            return False
        def calcAdditive(index):
            nonlocal additive  
            if index >= len(num):
                return len(additive) >= 3

            for i in range(index, len(num)):                
                val = num[index:i+1]
                if len(val) > 1 and val[0] == "0":
                    return False
                val = int(val)
                if len(additive) < 2 or additive[-2] + additive[-1] == val:
                    additive.append(val)
                    if calcAdditive(i+1):
                        return True

                    additive.pop()
            
            return False
           

        return calcAdditive(0)