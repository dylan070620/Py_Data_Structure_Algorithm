def bubble_sort(list):
    for i in range(len(list)-1):#重复n-1
        flag = False
        for j in range(len(list)-i-1):#重复无序区-1
            if list[j]>list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp 
                flag = True
                print(list)
        if flag == False:#已经排好了（无交换）跳出
            break
    
list1 = [3,2,1,4,5,6]
bubble_sort(list1)
print(list1)