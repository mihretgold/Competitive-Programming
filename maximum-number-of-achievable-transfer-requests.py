class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        check = [0]*n
        def calcMaxReq(index, net_change, num_requests):
            if index >= len(requests):
                if check != net_change:
                    return 0

                return num_requests

            froms, to = requests[index]
            temp = net_change[:]
            net_change[froms] -= 1
            net_change[to] += 1

            all_buldings = calcMaxReq(index + 1, net_change[:], num_requests+1)
            without_last = calcMaxReq(index + 1, temp[:], num_requests)

            return max(all_buldings, without_last)

        return calcMaxReq(0, [0]*n, 0)