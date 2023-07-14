


n=int(input())
s=input()
s1=[int(i) for i in s]
# print(s1)
Cond=True
pali=s1[0]^s1[n-1]

for i in range(1,int(n/2)):
    if(s1[i]^s1[n-1-i]!=pali):
        Cond=False


if Cond:
    print("YES")
else:
    print("NO")    