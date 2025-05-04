f =open("bapai.txt","a")
f.write("\ni live in kolkata")

f.close()
f= open("bapai.txt","r")
data=f.read()
print(data)
f.close()