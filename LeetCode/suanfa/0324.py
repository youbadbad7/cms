# 给定一个整数数组，判断是否存在重复元素。如果存在一值在数组中出现至少两次，函数返回true。如果数组中每个元素都不相同，则返回false

def c():
    list = [1,2,3,4]
    n = len(list)
    result = False
    for i in range(n - 1):
        for j in range(i,n-1):
            if list[i] == list[j+1]:
                result = True
                print(result)
                return False
    print(result)

# c()

def d():
    list = [1,2,3,4]

    for i in list:
        print(i)
        print(type(i))


d()