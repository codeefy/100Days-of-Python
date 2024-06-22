#Minimum Cost to Reach the Destination
"""There are N cities in a country. George is initially at the airport in city 1 and he wants to reach city N. For any city i, there is either a flight to city (i+1) or to (i+3) if it exists.
You have been given an array A with the costs of flight tickets for N cities. To find the cost of a flight ticket between any two cities i and j, you take the absolute difference of the costs of those cities in the array A. You can use the formula |a| = |Cost[i] – Cost[j]] to calculate the cost of a flight ticket, where [al represents the absolute value of a.
Your task is to find and return the minimum possible cost of flight ticket required to reach the
city N.
Note:
¢ The number of cities is always greater than 3.
e Assume | based indexing.
Input Specification:
input1: An integer value N, representing the number of cities.
input2: An integer array A, representing the cost of tickets to reach the i” a city.
Output Specification:
Return the minimum possible cost of flight ticket required to reach the city N.
Example |:
input1: 4
input2: (1,4,5,2)
Output: 1
Explanation:
George takes a flight in the below optimal manner:
From city | to city 4, as city 4 is the third next city to city 1 so the cost
will be |1-2|=1.
Hence, | is returned as the output.
Example 2:
input 1: 6
input2 (4,12,13,18,10,12)
Output: 10
Explanation:
George takes a flight in the below optimal manner: From city | to city 2, the cost will be |4-
12|=8
From city 2 to city 3, the cost will be |12-13] = 1
. From city 3 to city 6, the cost will be |13-12| = 1
Therefore, the total cost is 8 + 1 + 1 = 10. Hence, 10 is returned as the output."""

# Approach
# 1. We have to find the minimum possible cost of flight ticket required to reach the city N.
# 2. We have been given an array A with the costs of flight tickets for N cities.
# 3. To find the cost of a flight ticket between any two cities i and j, we take the absolute difference of the costs of those cities in the array A.
# 4. We can use the formula |a| = |Cost[i] – Cost[j]] to calculate the cost of a flight ticket, where [al represents the absolute value of a.
# 5. We have to find the minimum possible cost of flight ticket required to reach the city N.
# 6. The number of cities is always greater than 3.
# 7. We have to assume 0 based indexing.
# 8. We have to return the minimum possible cost of flight ticket required to reach the city N.
# 9. We have to take the input values of N and the array A.
# 10. We have to find the minimum possible cost of flight ticket required to reach the city N.
# 11. We have to print the output.
# 12. Let's write the code now.

def minCost(n, arr):
    dp = [0] * n
    dp[0] = 0
    dp[1] = abs(arr[1] - arr[0])
    dp[2] = abs(arr[2] - arr[0])
    for i in range(3, n):
        dp[i] = min(dp[i - 1] + abs(arr[i] - arr[i - 1]), dp[i - 3] + abs(arr[i] - arr[i - 3]))
    return dp[n - 1]

n = int(input())
arr = list(map(int, input().split()))
print(minCost(n, arr))


