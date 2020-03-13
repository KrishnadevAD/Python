#number of occurances
T1=[2,3,2,3,3,4,4,5,5,5,5,66,6,7]
def numberof(list,element):
    occurances=0
    for e in list:
        if e==element:
            occurances+=1
    return occurances
print(numberof(T1,3))
   


   # To print the  reverse of the any string
#def reverse(string):
#    result=""
#   for c in string:
#      result = c + result
#   return result
#print(reverse("krishnadev"))