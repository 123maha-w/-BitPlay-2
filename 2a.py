def oddOccurring(arr):

    res = 0

    for element in arr:
        res = res ^ element
    return res
arr = []

n = int(input("enter array size"))

while (n):
    num = int(input("enter a number:"))
    arr.append(num)
    n-=1

print("\n\nOdd occurring number is:",oddOccurring(arr))