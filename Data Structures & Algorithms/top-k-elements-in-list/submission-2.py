class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        answer_mid = (Counter(nums).most_common(k))
        for i in range(len(answer_mid)):
            inter = answer_mid[i]
            result.append(inter[0])
        return (result)

        