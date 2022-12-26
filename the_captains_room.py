# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict 
group_size = int(input())
room_list = list(map(int, input().split()))
map_room = defaultdict(int)
length = len(room_list)
for num in range(length):
    map_room[room_list[num]] += 1
    
for room in map_room:
    if map_room[room] != group_size:
        print(room)
        break
    
