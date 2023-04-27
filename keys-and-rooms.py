class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque([0])
        visted = set()
        length = len(rooms)

        while queue and len(visted) < length:
            vertex = queue.popleft()
            visted.add(vertex)

            for neighbour in rooms[vertex]:
                if neighbour not in visted:
                    queue.append(neighbour)


        return len(visted) == length