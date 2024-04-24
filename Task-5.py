dict={}
while True:
    print("Enter 1 to add contact:\nEnter 2 to update contact:\nEnter 3 to delete contact:\nEnter 4 to search contact:\n")
    a=int(input())
    if a==1:
        name=input("Enter Name: ")
        pho_no=input("Enter Mobile Number: ")
        email=input("Enter Email_id: ")
        address=input("Enter Address: ") 
        dict[name]={
            "Name":name,
            "Phone_number":pho_no,
            'Email_id':email,
            'Address':address
        }
        print(dict[name])
    elif a==2:
        va=input("Enter Your Category To Update:\nName\nPhone_number\nemail\nAddress\nPlease Enter as it is name as given Above..\n")
        dict[va]=input("Enter Details:\n")
        print(dict[va])
    elif a==3:
        val=input("Enter Name:\n")
        del(dict[val])
        print(dict[val])