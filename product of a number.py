n=int(input("enter a number:"))
temp=n
product=1
while(temp!=0):
    product=product*(temp%10)
    temp=int(temp/10)
print("product is:",product)
