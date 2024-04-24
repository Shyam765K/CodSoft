a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
print("Addtion : +\nSubtraction : -\nMultiplication : *\nDivision : /\nFloor Division : //\nModulus : %\nExponent : **")
c=input("Enter the operation:")
if c=='+':
    print("Addition of",a,'and',b,"is:",a+b)
elif c=="-":
    print("Subtraction of",a,'and',b,"is:",a-b)
elif c=="*":
    print("Multiplication of",a,'and',b,"is:",a*b)
elif c=="//":
    print("Floor Division of",a,'and',b,"is:",a//b)
elif c=="%":
    print("Modulus of",a,'and',b,"is:",a%b)
elif c=="/":
    print("Division of",a,'and',b,"is:",a/b)
elif c=="**":
    print("Exponent of",a,'and',b,"is:",a**b)
else:
    print("Enter a valid operation..!!")