x=int(input("enter x="))
y=int(input("enter y="))
z=int(input("enter z="))
if x<y+z and y<x+z and z<x+y:
    result= triangle
else:
    result= square
print(result)