# Objective: Given an array A of size N and a number k <= N, find the sub-array
# of size k, such that sum of that sub-array is maximum
# Example:
# A = [1,2,3,4,5,6,7,8,9,10]
# N = 10
# k = 3
# Answer: 27
# its sum is 8+9+10 == 27, which is maximum


def maximumSubArraySum(A: list[int], k: int) -> float:
    # write the body of the program here
    maxsum = float('-inf')
    for i in range(len(A)-k+1):
        list_sum = sum(A[i:i+k])
        if(list_sum>maxsum):
            maxsum = list_sum

    return maxsum
        


if __name__ == '__main__':
    assert maximumSubArraySum([1,2,3,4,10,8,9,5,6,7,], 3) == 27
    print(maximumSubArraySum([1,2,3,4,10,8,9,5,6,7,], 3))
