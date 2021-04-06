# 给定一个数组，将数组中的元素向右移动K个位置，其中K是非负数

def d():

    d = [1,2,3,4,5,6,7,8,9,10]
    key = 3
    n = len(d)
    for j in range(key):
        one = d[-1]
        # print(d)
        for i in range(1,n):
            d[-(i)] = d[-(i+1)]
        d[0]=one
        print(d)
    # print(d)

d()