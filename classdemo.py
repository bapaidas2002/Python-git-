class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def showDetails(self):
        print("Name : ",self.name)
        print("Age : ",self.age)

p1=person("bapai",21)
p1.showDetails()