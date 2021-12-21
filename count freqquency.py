list1=['a','s','d','f','g','h','h','g','f','d','ah']
frequency={}
for item in list1:
    if(item in frequency):
        frequency[item]+=1
    else:
        frequency[item]=1
for key,value in frequency.items():
    print("%s-%d"%(key,value))
