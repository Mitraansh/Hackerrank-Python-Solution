def average(array):
    x=(set(array))
    y=len(x)
    return sum(x)/y

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
