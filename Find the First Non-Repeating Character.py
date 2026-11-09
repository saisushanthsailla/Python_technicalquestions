def first_non_repeating_character(s) :
    freq = {}
    if len(s) > 0 :
        for i in s :
            freq[i] = freq.get(i,0) + 1

        for key,value in freq.items() :
            if value == 1 :
                return key
        return None
    else :
        return None


print(first_non_repeating_character("programming"))