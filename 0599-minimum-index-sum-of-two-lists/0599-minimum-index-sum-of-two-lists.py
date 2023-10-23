class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        min_idx=len(list1)+len(list2)
        ans=[]
        for i in range(len(list1)):

            for j in range(len(list2)):
                if list1[i]==list2[j]:
                    if i+j<min_idx:
                        min_idx=i+j
                        ans=[list1[i]]
                    elif i+j==min_idx:
                        ans.append(list1[i])
                    break
        
        if min_idx==len(list1)+len(list2):
            return -1
        else:
            return ans