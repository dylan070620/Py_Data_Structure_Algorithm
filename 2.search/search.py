def linear_search(x,list):
    for i in range(len(list)):
        if x == list[i]:
            return i
    return "none"


def binary_search(x,list):
    left = 0
    right  = len(list) - 1
    while left <= right :#确保范围有值
        mid  = (left + right)//2
        if x == list[mid]:
            return mid
        elif x > list[mid]:
            left = mid + 1
        elif x < list[mid]:
            right = mid - 1
    else:
        return "not found"
list1 = [1,2,3,4,5,6] 
x= 5

print(linear_search(5,list1))
print(binary_search(5,list1))