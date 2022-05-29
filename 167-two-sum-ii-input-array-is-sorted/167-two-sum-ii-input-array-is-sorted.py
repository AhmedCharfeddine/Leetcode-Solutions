class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ptr1, ptr2 = 0, len(numbers) - 1
        s = numbers[ptr1] + numbers[ptr2]
        while s != target:
            if s < target:
                ptr1 += 1
            else:
                ptr2 -= 1
            s = numbers[ptr1] + numbers[ptr2]
        return [ptr1+1, ptr2+1]