
def cal_fact(num):
    fact=1
    for i in range(1,num+1):
        fact *=i
    print("Factorial is : ",fact)
number=int(input("Enter number for Factorial : "))
cal_fact(number)



