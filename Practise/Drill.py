
for a in range(int(input())):
    n,k,m=map(int,input().split())
    s=input()
    power=[int(i) for i in list(s)]#5,4,1,8
    for j in range(m):
        for i in range(len(power)):
            power[i]=power[i]*k
        pow1=[str(i) for i in power]#45,36,9,72
        s1=""
        for i in range(len(pow1)):
            s1=s1+pow1[i]
        pow2=[int(i) for i in list(s1)]
        power=pow2

    print(f"{len(power)}")








