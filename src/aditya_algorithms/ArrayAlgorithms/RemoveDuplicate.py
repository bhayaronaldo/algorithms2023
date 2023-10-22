# complete the following function:
# removeDuplicate 

def removeDuplicate(A: list[int]) -> list[int]:
    # mylist = set()
    # for elem in A:
    #     if elem not in mylist: # much faster than looking up in list
    #         mylist.add(elem)
    # return list(mylist)
    temp = set(A)
    return list(temp)


if __name__ == "__main__":
    A = [1,1,1,2,3,4,3,2,2,5,1,3]
    assert sorted(removeDuplicate(A)) == [1,2,3,4,5]



    