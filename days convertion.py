a=int(input("enter number of days:"))
year=a//365
print(year)
week=(a%365)//7
print(week)
days=(a%365)%7
print(days)
