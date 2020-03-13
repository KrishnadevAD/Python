class myiteration:
    def __iter__(self):
       self.current=0
       return self
    def __next__(self): #define for the next iteraion 
        if self.current<100:
           self.current+=5 #iterar]tion in the interval of  5
           return self.current
        else:
            raise stop


s=myiteration() # s is the instance (उदाहरणका) of myiteration
myiter=iter(s) #passing to the  iter in the my iteration
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))