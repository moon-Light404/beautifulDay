冒泡排序1
def buublesort(arr):
    len1 = len(arr)
    for i in range(len1-1):
        for j in range(len1 - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

    return arr

arr = [13,38,5,6,9,10,20,21,44,19]
buublesort(arr)
print(arr)

冒泡排序2
def buubleSort(a):
    len2 = len(a)
    i = len2 - 1
    while i > 0:
        lastchange = 0
        for j in range(0,i):
            if a[j+1] < a[j]:
                a[j+1],a[j] = a[j],a[j+1]
                lastchange = j
        i = lastchange
oldlist = eval(input("请输入你的列表:"))
buublesort(oldlist)
print(oldlist)
冒泡倒序排序:
def buubleSort(a):
    len2 = len(a)
    i = len2 - 1
    while i > 0:
        lastchange = 0
        for j in range(0,i):
            if a[j+1] > a[j]:
                a[j+1],a[j] = a[j],a[j+1]
                lastchange = j
        i = lastchange
oldlist = eval(input("请输入你的列表:"))
buubleSort(oldlist)
print(oldlist)




选择排序:
def selectionsort(mylist):
    len1 = len(mylist)
    for i in range(len1 - 1):
        mindex = i
        for j in range(i+1,len1):
            if mylist[j] < mylist[mindex]:
                mindex = j
        mylist[i],mylist[mindex] = mylist[mindex],mylist[i]

oldlist = eval(input("请输入你的列表:"))
selectionsort(oldlist)
print(oldlist)

插入排序:
ep:[1,5,0,9,6,8,15,7,3,11,12]
def insertSort(list):
    len3 = len(list)
    for i in range(1,len3-1):
        preindex = i -1
        current = list[i]
        while preindex >= 0 and list[preindex]>current:
            list[preindex+1] = list[preindex]
            #可以把下面的这条插到while里面list [ preindex] = current

            preindex -= 1

        list [preindex + 1] = current

    return list
oldlist = eval(input("请输入你的列表:"))
insertSort(oldlist)
print(oldlist)




快速排序:
def quicksort(array):

    if len(array) < 2:
        return array
    else:
        pivot = array[0] #privot = array[len(array)//2]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
print (quicksort([1,5,0,9,6,8,15,7,3,11,12]))
oldlist = eval(input("请输入你的列表:"))
quicksort(oldlist)
print(oldlist)
newlist = oldlist
print(newlist)



选择排序倒序(从大到小排序):
def selectionsort(mylist):
    len1 = len(mylist)
    for i in range(len1 - 1):
        maxdex = i
        for j in range(i+1,len1):
            if mylist[j] > mylist[maxdex]:
                maxdex = j
        mylist[i],mylist[maxdex] = mylist[maxdex],mylist[i]

oldlist = eval(input("请输入你的列表:"))
selectionsort(oldlist)
print(oldlist)