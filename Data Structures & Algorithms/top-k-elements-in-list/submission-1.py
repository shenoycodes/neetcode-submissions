import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashed_nums={}

        for n in nums:
            if(n not in hashed_nums):
                hashed_nums[n]=1
            else:
                hashed_nums[n]+=1
        
        #print(f'hash map: {hashed_nums}')
        #print(hashed_nums)

        # Push tuple: (-frequency, number)
        max_heap = [(-freq, num) for num, freq in hashed_nums.items()]

        # Convert to max heap
        #max_heap = [-x for x in hashed_nums.values()]
        heapq.heapify(max_heap)

        # Get maximum element
        #print(-max_heap[0])  # 8

        # Pop maximum
        #print(-heapq.heappop(max_heap))  # 8      
        
        result=[]
        while (k>0):
            freq, num = heapq.heappop(max_heap)
            result.append(num)
            k -= 1
        return result
            

        