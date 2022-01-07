from sys import stdin


def binarySearch(arr, n, x) :
    #Your code goes here
    lower_bound=0
    upper_bound=n-1
    while lower_bound<=upper_bound:
        middle=(lower_bound+upper_bound)//2
        if x==arr[middle]:
            return middle
        elif x<arr[middle]:
            upper_bound=middle-1
        else:
            lower_bound=middle+1
    return -1

#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().strip())
    
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


#main
arr, n = takeInput()
t = int(stdin.readline().strip())

while t > 0 :
    
    x = int(input().strip())    
    print(binarySearch(arr, n, x))

    t -= 1
