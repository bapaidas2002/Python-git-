class Animal:
    def __init__(self,age,name):
        self.age=age
        self.name=name
    def details(self):
        print(f"{self.name} says hello")
    def agee(self):
        print(f"my age is :{self.age}")

dog=Animal(5 , "dog")
dog.details()
dog.agee()
