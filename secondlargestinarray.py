from sys import stdin


def secondLargestElement(arr, n):
    #Your code goes here
    if n <=1:
        return -2147483648 
    mx = max (arr[0],arr[1])
    second_mx = min (arr[0],arr[1])
    for i in range (2,n):
        if arr[i]>mx:
            second_mx = mx
            mx = arr[i]
        elif arr[i]>second_mx and mx != arr[i]:
            second_mx = arr[i]
    if second_mx == mx:
        return -2147483648 
    return second_mx
#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n != 0:
        arr = list(map(int, stdin.readline().rstrip().split(" ")))
        return arr, n

    return list(), 0



#main
t = int(stdin.readline().rstrip())

while t > 0 : 
    
    arr, n = takeInput()
    print(secondLargestElement(arr, n))

    t -= 1
