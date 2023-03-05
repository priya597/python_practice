class Solution:
    def productExceptSelf(self, nums):  
        # new_arr = [];
        # for i in range(len(nums)):
        #     prod = 1
        #     for j in range(len(nums)):
        #         if(i != j):
        #             prod = prod * nums[j];     
        #     new_arr.append(prod);
        # return new_arr

        i = 0;
        j = len(nums) - 1;
        newlist = [];
        
        for k in range(len(nums)):
            while i < j:
                if i != j:
                    prod = nums[i]*nums[j]
            newlist.push(prod) 
        return newlist

    productExceptSelf('self',[1,2,3,4]);
                