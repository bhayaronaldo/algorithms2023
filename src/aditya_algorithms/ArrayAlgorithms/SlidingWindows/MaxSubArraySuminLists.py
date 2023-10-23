
# Input: A = List[List[Int]]: list of list of integers.
# Write a program that gives you MaximumSubArraySum of each list in A. 
# Size of outpur should be a vector of size 100

# Once you get the result, count how many elements in the result are >= 25 and above

# also, find the number of elements in those lists whose maxSubArraySum exceeds 25

# Re-use the code of maximumSubArraySum that you wrote earlier
from MaxSubArraySum import maximumSubArraySum

def gen_listOfInts() -> list[list[int]]:
    # Think of this function as a blackbox, which is hidden from you and it's simply an INPUT
    # generator
    import numpy as np
    result = []
    for i in range(100):
        A = np.random.randint(0, 10, size=np.random.randint(3,50))
        result.append(A.tolist())
    return result



if __name__ == '__main__':
    # print(gen_listOfInts())

    # INPUT
    A = gen_listOfInts()
    
    # declare empty list to store result: it's a list of tuple;
    # each tuple "t" is of the form (int, int),
    #  the 1st element can be accessed t[0]: which has maximumSubArraySum
    # the 2nd element can be accessed t[1]: it contains the lenght of the array 
    maxsum_list_and_length: list[tuple[int, int]] = []
    
    # you can remove type hint "...: list[tuple[int, int]]", and re-write above as:
    #  maxsum_list_and_length = []
    for elem in A:
        temp_max = maximumSubArraySum(elem,3)
        # we are appending a Tuple : (maximumSubArraySum, len(array)) => [(sum_A[0], len(A[0])), ]
        maxsum_list_and_length.append((int(temp_max), len(elem)))

    print(maxsum_list_and_length)

    ctr = 0
    for elem in maxsum_list_and_length:
        if elem[0]>=25:
         ctr = ctr+1
         print("Sum of array:", elem[0], "length of array: ", elem[1])
    print("Number of such arrays are", ctr)




        