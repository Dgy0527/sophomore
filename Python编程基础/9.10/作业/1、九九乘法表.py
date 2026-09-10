#顺序打印
for i in range(1,10):
    for j in range(1,i+1):
        print("%dx%d=%-2d" % (j, i, j*i),end=" ") #这里可改为print("{}x{}={}".format(j,i,j*i),end=' ')
    print("")
print('----------'*10)

# 倒序打印
for m in range(9,0,-1):
    for n in range(9,m-1,-1):
        print("{}x{}={}".format(n,m,n*m),end=' ')
    print(end='\n')
print('----------'*10)

for m in range(9,0,-1):
    for n in range(m,0,-1):
        print("{}x{}={}".format(n,m,n*m),end=' ')
    print(end='\n')
print('----------'*10)

#打印指定长度的乘法表
start=4 #可改成任意数字
end=10 #可改成任意数字
for i in range(start,end+1):
    for j in range(start,i+1):
        print("{}x{}={}".format(j,i,j*i),end=' ')
    print(end='\n')
print('start--end'*10)
