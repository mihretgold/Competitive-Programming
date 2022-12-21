# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
mp={}
for i in range(n):
   s=input()
   if s in mp:
     mp[s] +=1
   else:
    mp[s] = 1
print(len(mp))
for i in mp:
    print(mp[i] , end=" ")

