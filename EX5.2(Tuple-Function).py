def EmpCalc():
    Name=input("Enter your name:")
    Age=int(input("Enter your age:"))
    Sal =float(input("Enter your salary:"))
    HRA=(Sal*35)/100
    PF=(Sal*25)/100
    NetSal=Sal+HRA+PF

    if (NetSal>=30000)and (NetSal<=100000):
        print("Senior Manager")
    elif (NetSal>=20000)and (NetSal<=29999):
         print("Manager")
    else:
        print("Frontlevel Job")
    return Name,Age,NetSal    
    
Name,Age,NetSal= EmpCalc()
print("Employee Name:",Name)
print("Employee Age:",Age)
print("Employee NetSalary:",NetSal)
