n,m=map(int,input().split())
n1,m1=map(int,input().split())
m2=(n*60)+(n1*60)+m+m1
m3=m2//60
print("{:0>2}".format(m3%24),end=' ')
print("{:0>2}".format(m2%60))