if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    lst=[]
    for i in arr:
        lst.append(i)
    lst.sort()
    a=max(lst)
    for i in range(0,len(lst)):
        if a in lst:
            lst.pop()
    print(max(lst))
