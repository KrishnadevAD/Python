f = open("myTextfile.txt","w")
f.write(" Elon  ")
f.write("musk\n")
f.write("krishnadev ")
f.write("adhikari\n")
f=open("mytextfile.txt","r")
print(f.read())
f = open("myTextfile.txt","r")
print(f.read(8))

#for line in f:
#    print(line)
#for line in f:
#    print(line)  
#import os
#if os.path.exists("myTextfile.txt"):
#   os.remove("myTextfile.txt")
#else:
#    print("the file doesnot exists") 


#os.rmdir("xyz")   #to remove the directiory