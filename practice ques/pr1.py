for i in range(int(input())):
    n=int(input())
    x = list(map(int, input().split()))
    l6=[i for i in range(1,31) if i % 6==0]
    l7=[i for i in range(1,31) if i % 7==0]
    z =set(x).intersection(set(l6))
    z1=set(z).intersection(set(l7))
    print(z1)   



