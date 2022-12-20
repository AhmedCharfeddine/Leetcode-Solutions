class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque(rooms[0])
        keys = set(rooms[0]) | {0}
        visited = {0}
        i = 0
        while queue:
            cur_room = queue.popleft()
            if cur_room not in visited:
                for key in rooms[cur_room]:
                    if key not in keys: queue.append(key)
                keys |= set(rooms[cur_room])
                visited.add(cur_room)
                if len(keys) == len(rooms): return True
        
        return len(keys) == len(rooms)