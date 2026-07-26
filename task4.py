def my_max(nums):
    maxi=float('-inf')
    for i in nums:
        if maxi<i:
            maxi=i
    return maxi

my_list=[2,4,1,5,9,8,7]
print(my_max(my_list))


        
    