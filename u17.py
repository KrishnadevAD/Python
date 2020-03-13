#inheritance example
class human:
    def __init__(self,name,age):
      self.name=name
      self.age=age
    def speaks(self):
       print("my name is "+ str(self.name))
class sex(human):
    def __init__(self,name,age,sex):
       super().__init__(name,age) 
       self.sex=sex
    def height(self):
        print("my sesx is  is "+(self.sex))
Ram=sex("ram",19,'male')
print(Ram.name)
print(Ram.speaks())
Ram.height()
