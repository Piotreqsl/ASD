'''Given an integer array arr[], write a program to find 
three numbers in the array whose product 
is maximum and return the maximum product of these three numbers
'''

#F[i][j] - maksymalny iloczyn j elementów przy założeniu że uwzgledniamy
## i pierwszych elementów z tablicy i oraz A[i] jest ostatnim


'''We need not necessarily sort the given numsnums array to find the maximum product. Instead, we 
can only find the required 2 smallest values(min1min1 and min2min2) and the three largest values(max1, max2, max3) in 
the nums array, by iterating over the nums array only once.

At the end, again we can find out the larger value out of min1*min2 * max1 or max1*max2*max3.'''

def maxProduct(arr):
        n = len(arr)
        DP = [[0 for i in range(3+1)] for j in range(n+1)]

        for i in range(1,n+1):
            DP[i][1] = arr[i-1]
        
        for i in range(1,n+1):
            for prev_i in range(1,i):
                DP[i][2] = max(DP[i][2], DP[prev_i][1] * arr[i-1])
        for i in range(1,n+1):
            for prev_i in range(1,i):
                DP[i][3] = max(DP[i][3], DP[prev_i][2] * arr[i-1])
        
        
        maxE = float("-inf")
        for i in range(1,n+1):
            if DP[i][3] > maxE:
                maxE = DP[i][3]
        return maxE

A = [4, 5, -19, 3]
print(maxProduct(A))
    

