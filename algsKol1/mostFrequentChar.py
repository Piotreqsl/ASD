
def second(str):
    occurences = [0] *26
    for i in range(len(str)):
        occurences[ord(str[i]) - ord('a')] +=1
    
    first = 0
    second = 0
    for i in range(1,26):
        if(occurences[i] > occurences[first]):
            second = first
            first = i
        elif (occurences[i] > occurences[second] and occurences[i] != occurences[first]):
            second = i
    
    print(occurences)
    return chr(second + ord('a'))
print(second("acccabbbbbcba"))

T=[11,567788,2344,557]