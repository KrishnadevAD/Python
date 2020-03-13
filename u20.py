

# program to print the reverse of the string 
def reverse(string):
    result = ""
    for c in string:
        result = c + result
    return result
print(reverse("krishnadev adhikari "))
