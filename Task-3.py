import random
small_alphabets="abcdefghijklmnopqrstuvwxyz"
capital_alphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
special_character="!@#$%^&*()_+<>?:;[]{}|\/~`"
s = capital_alphabets + small_alphabets + numbers + special_character
length = int(input("Enter Length of the Password:\n"))
password = "".join(random.sample(s,length))
print("Password : \n"+password)