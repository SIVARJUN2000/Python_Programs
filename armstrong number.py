a=int(input("enter any number:"))
sum=0
temp=a
while(temp>0):
    d=temp%10
    sum+=d**3
    temp//=10
if(a==sum):
    print("armstrong number")
else:
    print("not an armstrong number")
