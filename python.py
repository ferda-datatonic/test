nums =  [2,3,1,1,4]
def can_jump_memoization(i, array, cache):

    if i >= len(array):
        return False
    elif i == len(array)-1:
        return True
    elif i in cache:
        return cache[i]
    else:
        cache[i] = False
        for j in range(1, array[i]+1):
            if can_jump_memoization(j+i, array, cache):
                cache[i] = True
                return True
        return cache[i]
print(can_jump_memoization(0,nums,{}))

# def canJump(nums):
#     N = len(nums)

#     def dfs(i, memo):
#         if i == N - 1:
#             return True
        
#         if nums[i] == 0:
#             return False
        
#         if memo[i] != None:
#             return memo[i]
        
#         is_valid = False
        
#         for j in range(i + 1, (i+nums[i])+1):
#             if dfs(j, memo):
#                 is_valid = True
#                 break
        
#         memo[i] = is_valid
#         return memo[i]
    
#     return dfs(0, [None] * N)
# print(canJump(nums))
