class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for idx, num in enumerate(numbers):
            if num * 2 == target : continue
            find = target - num
        
            l = idx + 1
            r = n - 1
            while l <= r:
                mid = l + (r - l) // 2
            
                if numbers[mid] == find :
                    return [idx + 1, mid + 1]
                
                elif numbers[mid] > find :
                    r = mid - 1
                
                else: 
                    l = mid + 1
                