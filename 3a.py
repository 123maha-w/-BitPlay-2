def printTwoOdd(arr,size):
    
    xorof2 = arr[0]
    x=0
    y=0

    Setbit = 0

    for i in range(1,size):
        xorof2 = xorof2^arr[i]
    Setbit = xorof2 & ~(xorof2 - 1)
    
    for i in range(size):
        if(arr[i]&Setbit):
            x =x ^ arr[i]
        else:
            y=y^ arr[i]

    print("the two Odd elements are ", x, " & ", y)

arr = []

arr_size = int(input("enter size of arry : "))
for i in range(0,arr_size):
    Z= int(input("enter element : "))
    arr.append(Z)

printTwoOdd(arr,arr_size)