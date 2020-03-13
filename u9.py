listVar=["apple","google", "miscrosoft"]
Tcompaney=listVar[2]
listVar[0]="Tesla"
listVar[1]="spaceX"
listVar[2]="Paypal"

print(Tcompaney)
Tcompaney1=listVar[1]
print(Tcompaney1)
#listVar
listVar=["apple","google", "miscrosoft"]
listVar.append("Tesla")
listVar.insert(3,"SpaceX")
listVar.insert(4,"Mango")#mango is added
listVar.remove("Mango")#mango is deleted/removed
#listVar.clear()#deleted all the listVar

print(len(listVar))

print(listVar)


#tuple variable 
tupleVar=["apple","google", "miscrosoft","tesla","tesla"]
#tupleVar[1]="tesla" # canot change the value in tuple variable
indexoftesla=tupleVar.index("apple")
print(indexoftesla)

print(tupleVar[2])
print(tupleVar[3])

#Myset
Myset={"apple","google", "miscrosoft","tesla1","tesla"}
Myset.add("Krishnaddev")#to add the element
Myset.update(["adhikari","Danuwar","Kridara"])# to update the element
Myset.discard("tesla")# to discard or to remove the element

print(Myset) #"Myset" variable prints the value only once
