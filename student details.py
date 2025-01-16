name = input("Please Enter Your Name : ")
roll = int(input("Please Enter Your Roll No : "))
print("Enter Your Marks of 4 Subjects(out of 100) : ")
m1=int(input("Subject 1 : "))
m2=int(input("Subject 2 : "))
m3=int(input("Subject 3 : "))
m4=int(input("Subject 4 : "))
total = m1 + m2 + m3 + m4
avg= (m1 + m2 + m3 + m4)/4
per = avg
print("Your Total Marks is : ",total)
print("Your average marks is : ", avg)
print("Percentage is : ",per)