t = int(input())
for x in range(t): 
    S = input()
    for i in range(0,len(S),2):
        print(S[i],end="")
    print(end=" ")
    for i in range(1,len(S),2):
        print(S[i],end="")
    print("") 
	
	
#Input:
#2
#Hacker
#Rank