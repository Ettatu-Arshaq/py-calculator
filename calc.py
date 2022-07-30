def summ(a,b):
    s=a+b
    print("THE SUM IS : ",s)
    

def diff(a,b):
    s=a-b
    print("THE DIFFRENCE IS : ",s)
    
    
def mul(a,b):
    s=a*b
    print("THE PRODUCT IS : ",s)
    

def div(a,b):
    s=a/b
    print("THE QUOTIENT IS : ",s)
    
y=0
while(y==0):
    print("\nMENUS\n1:ADD\n2:SUBTRACT\n3:MULTIPLY\n4DIVIDE\n0:EXIT\n")
    u=eval(input("ENTER YOUR CHOICE : "))
    if (u==1):
        a=eval(input("\nENTER YOUR NUMBER 1: "))
        b=eval(input("ENTER YOUR NUMBER 2: "))
        summ(a,b)
    elif (u==2):
        a=eval(input("\nENTER YOUR NUMBER 1: "))
        b=eval(input("ENTER YOUR NUMBER 2: "))
        diff(a,b)
    elif (u==3):
        a=eval(input("\nENTER YOUR NUMBER 1: "))
        b=eval(input("ENTER YOUR NUMBER 2: "))
        mul(a,b)
    elif (u==4):
        a=eval(input("\nENTER YOUR NUMBER 1: "))
        b=eval(input("ENTER YOUR NUMBER 2: "))
        div(a,b)
    elif (u==0):
        quit()
    else:
        print("USER ERROR")
        continue
    
