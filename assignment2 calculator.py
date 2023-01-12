
import math
a=float(input("enter a="))
b=float(input("enter b="))
x=float(input("enter x="))
op=input("enter op=")
if op=="+":
    result=a+b
if op=="-":
    result=a-b
if op=="*":
    result=a*b
if op=="/":
    if b==0:
        result="error"
    else:
        result=a/b
if op=="radical":
    result=math.sqrt(x)
if op=="sin":
    result=math.sin(x)
if op=="cos":
    result=math.cos(x)
if op=="tan":
    result=math.tan(x)
if op=="cot":
    result=(math.cos(x)/sin(x))
if op=="factorial":
    result=math.factorial(x)
print(result)