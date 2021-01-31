sum, tmp = 0, 1
for i in range(1,11):
    tmp*=i
    print("{:2}的阶乘是:{}".format(i,tmp))
    sum+=tmp
print("运算结果是: {}".format(sum))

'''
tmp存的是阶乘
sum存的是每个阶乘的和
'''