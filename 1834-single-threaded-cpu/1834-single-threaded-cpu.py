class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [[i] + tasks[i] for i in range(len(tasks))]
        tasks.sort(key=lambda task: (task[1], task[2]))
        res = []
        
        # custom class to define comparaisons between tasks in heap
        class Task(list):
            def __lt__(self, other):
                if self[2] != other[2]:
                    return self[2] < other[2]
                return self[0] < other[0]
        
        tasks = list(map(Task, tasks))
        available = []
        heapify(available)
        
        while available or tasks:
            if not available:
                heappush(available, tasks.pop(0))
                t = available[0][1]
            task = heappop(available)
            
            res.append(task[0])


            t += task[2]
            while tasks and tasks[0][1] <= t:
                heappush(available, tasks.pop(0))
        return res
