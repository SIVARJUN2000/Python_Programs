list1=[]
a=int(input("enter how many no's in list1:"))
for n in range(a):
    num=int(input("enter numbers:"))
    list1.append(num)
list2=[]
b=int(input("enater how many no's in list2:"))
for n in range(b):
    num=int(input("enter numbers:"))
    list2.append(num)
merged_list=list1+list2
print("the third list is:",merged_list)
                  
