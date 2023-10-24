# Given an array of positive numbers, find if you can find numbers whose sum is N
# INPUT = [2,3,4,11,1,3,8,17]
# N = 11
# Result: yes, output would be list of tuple: list[tuple[int, int]]: [(3,8), (4,7)]


def findGivenSum(arr: list[int], N: int) -> list[tuple[int, int]]:
    set_of_elements: set[int] = set(arr)
    result: list[tuple[int, int]] = []
    for elem in set_of_elements.copy():
        if (N - elem) in set_of_elements:
            result.append((elem, N - elem))
            set_of_elements.remove(elem)
            set_of_elements.remove(N - elem)
    return result


if __name__ == "__main__":
    A = [2, 3, 4, 11, 1, 3, 8, 17, 7]
    print(findGivenSum(A, 11))
