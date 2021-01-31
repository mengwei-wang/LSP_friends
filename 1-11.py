n = 1
for i in range(5,0,-1):
    n = (n+1)<<1        # << 是按位左移的操作符
    print(n)
print(n)
