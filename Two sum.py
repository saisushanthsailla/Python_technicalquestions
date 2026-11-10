nums = [1, 5, 8, 10]
target = 20

def twosum(nums,target) :
    temp = {}
    for i in range(len(nums)) :
        diff = target - nums[i]

        if diff in temp :
            return [temp[diff],i]
        else :
            temp[nums[i]] = i

    return None


    


print(twosum(nums,target))