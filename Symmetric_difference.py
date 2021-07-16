m = int(input())
a = set(map(int, input().split()))
n = int(input())
b = set(map(int, input().split()))
x=a.symmetric_difference(b)
y=sorted(x)
for i in y:
    print(i)
