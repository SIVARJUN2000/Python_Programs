a=int(input("enter number of days:"))
year=a//365
print("no of years:",year)
week=(a%365)//7
print("no of weeks:",week)
days=(a%365)%7
print("no of days:",days)
