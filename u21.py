# program to print the  sum of the element in the list
def sumlist(list):
    result = 0
    for el in list:
        result +=el
    return result
print(sumlist([3,4,3,34,4]))