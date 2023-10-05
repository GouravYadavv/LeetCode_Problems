class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        L=[]
        for i in range(len(nums1)):
            if nums1[i] not in L and nums1[i] in nums2:
                L.append(nums1[i])
        return L