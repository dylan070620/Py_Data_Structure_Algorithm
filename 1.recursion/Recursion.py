#递归的特点
#1.调用自身
#2.终止条件
def hanoi(n,a,b,c):#n:number of plates a,b,c；name of 3 coloums
    if n > 0:
        hanoi(n-1,a,c,b)
        print("Moving from %s to %s"%(a,c))
        hanoi(n-1,b,a,c)

print(divmod(5,7))
