class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr):
            return max(arr)
        count = 0
        while count < k:
            if arr[0] > arr[1]:
                arr.append(arr[1])
                arr.pop(1)
                count += 1
            else:
                arr.append(arr[0])
                arr.pop(0)
                count = 1
        return arr[0]