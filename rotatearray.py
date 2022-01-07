from sys import stdin


def rotate(arr, n, d):
    #Your code goes here 
    temp = []
    i = 0
    while i<d: #storing value of first to index in new list
        temp.append(arr[i])
        i = i + 1
    i = 0 
    while d<n:#rotating the array
         arr[i] = arr[d]
         i = i +1
         d = d + 1
    #adding the temp into main array
    arr[:] = arr[: i] + temp
    return arr
 

















#Taking Input Using Fats I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#to print the array/list 
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    arr, n = takeInput()
    d = int(stdin.readline().rstrip())
    rotate(arr, n, d)
    printList(arr, n)
    
    t -= 1
