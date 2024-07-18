lis=['add','sub','mul']
print(lis)
oper=input("enter your operation from lis:")
def cal():
    num1=int(input("enter num1:"))
    num2=int(input("enter num2:"))
    if oper =='add':
        sum=num1+num2
        print("sum is:",sum)
    elif oper =='sub':
        diff=num1-num2
        print("difference is:",diff)
cal()
        
    
    
    
