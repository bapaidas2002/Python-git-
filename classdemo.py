class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def showDetails(self):
        print("Name : ",self.name)
        print("Age : ",self.age)
class employe:
    def __init__(self,eid,salary):
        self.eid=eid
        self.salary=salary
    def showdetails(self):
        print("E id : ",self.eid)
        print("Salry : ",self.salary)
class edata(person,employe):
    def show(self):
        self.showDetails()
        self.showdetails()



e1=person("bapai",21)
p1.showDetails()