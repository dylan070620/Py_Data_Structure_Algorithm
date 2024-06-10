def select_sort(list):
    for i in range(len(list)-1):#重复n-1趟
        minloc = i#先设置最小的数是无序区第一个数
        for j in range(i+1,len(list)):#在无序区中找最小的index
             if list[j]<list[minloc]:
                minloc = j#更新最小数的位置
        list[i],list[minloc] = list[minloc],list[i]


list =[1,3,2,1,565,2,3,4,4]
select_sort(list)
print(list)

