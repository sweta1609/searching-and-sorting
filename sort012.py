from sys import stdin 

def sort012(arr, n) :
    #Your code goes here
    count0 = 0
    count1 = 0
    count2 = 0
    for i in range(0,n):
        if (arr[i] == 0):
            count0=count0+1
        if (arr[i] == 1):
            count1=count1+1
        if (arr[i] == 2):
            count2=count2+1
     
 
  
    for i in range(0,count0):
        arr[i] = 0
     
  
    for i in range( count0, (count0 + count1)) :
        arr[i] = 1
     

    for i in range((count0 + count1),n) :
        arr[i] = 2
     
    return arr
#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0 :
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

    sort012(arr, n)
    printList(arr, n)
    
    t -= 1
