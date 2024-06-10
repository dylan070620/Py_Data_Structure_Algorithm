def insert_sort(list):
    for i in range(1,len(list)):#手里已经有第一张牌，i表示摸到的牌的下标
        j = i - 1#j是手里最后一张牌的下标
        while list[j]>list[i] and j>=0:#有序最后牌比摸得大 ，且指针没有移动到最左边 指针才能向左移
            j = j-1
        list[i],list[j+1] = list[j+1],list[i]

li = [3,2,4,7,5,9,56]

print(insert_sort(li))
print(li)