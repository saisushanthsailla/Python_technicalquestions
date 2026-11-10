s = [1,1, 2, 2, 3, 3, 3, 4, 4]

def  Second_Most_Frequent_Element(s) :
    freq = {}
    for i in s :
        freq[i] = freq.get(i,0) + 1

    highest = float("-inf")
    second_highest = float("-inf")
    
    for key,value in freq.items() :
        if value > highest :
            second_highest = highest
            highest = value
        elif value > second_highest and value < highest :
            second_highest = value

    for key, value in freq.items():
        if value == second_highest:
            return key



    





print(Second_Most_Frequent_Element(s))