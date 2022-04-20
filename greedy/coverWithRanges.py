

def cover(A):
    sorted(A)
    ranges_counter = 0
    start = -1
    end = -1

    for i in range(len(A)):
        point = A[i]
        
        if(end == -1):
            ranges_counter +=1
            start = point
            end = point +1
        elif(point > end):
            ranges_counter +=1
            start = point
            end = point + 1
    return ranges_counter

print(cover([0.25,0.5,1.6]))