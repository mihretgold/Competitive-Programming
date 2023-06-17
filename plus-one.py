class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        found = 0
        for index in range(len(digits)-1, -1, -1):
            if index == len(digits) - 1 and digits[index] == 9:
                digits[index] = 0
                if index - 1 < 0:
                    digits = [1] + digits
                else:
                    digits[index - 1] += 1
                    if digits[index - 1] <= 9:
                        found = 1
            elif digits[index] > 9:
                digits[index] = 0
                if index - 1 < 0:
                    digits = [1] + digits
                else:
                    digits[index - 1] += 1
                    if digits[index - 1] <= 9:
                        found = 1
            elif found == 0:
                digits[index] += 1
                break
            else:
                break


        return digits