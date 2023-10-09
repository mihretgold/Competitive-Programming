class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        arr = queryIP.split(':')
        arr2 = queryIP.split('.')


        def checkIPV4(arr):
            for value in arr:
                if value.isdigit() and 0 <= int(value) <= 255 and (len(value) == 1 or value[0] != '0'):
                    continue
                else:
                    return "Neither"

            return "IPv4"

        def checkIPV6(arr):
            for value in arr:
                if 1 <= len(value) <= 4:
                    for val in value:
                        
                        if val.isdigit() or "a" <= val <= "f" or "A" <= val <= "F":
                            continue
                        else:
                            return "Neither"
                    
                else:
                    return "Neither"

            return "IPv6"
        answer = ""
        if len(arr2) == 4:
            answer = checkIPV4(arr2)
        elif len(arr) == 8:
            answer = checkIPV6(arr)
        else:
            return "Neither"

        return answer