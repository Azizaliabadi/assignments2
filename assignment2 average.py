name=input("enter name=")
family=input("enter family=")
x=float(input("enter chemistry="))
y=float(input("enter physics="))
z=float(input("enter lab="))
Average=(x+y+z/3)
if Average >= 17:
    result="great"
if  12 <=Average < 17: 
    result="normal"
if Average < 12:
    result="fail"
print(result)