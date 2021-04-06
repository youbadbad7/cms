

def zhaoling():
    cash = int(input(''))
    money = [1,5,50]
    m = sorted(money,reverse=True)   ##降序

    jine = 0
    num = 0

    for i in m:
        jine = i
        num = cash // i   ##除以留整数  101/50=2
        if num == 0 :
            cash = cash
        else:
            cash = cash % i   ##留余数  101/50=1
        print(jine,num)

zhaoling()
