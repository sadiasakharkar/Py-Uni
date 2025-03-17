# pattern program 
n = 5
for i in range(n+1):
    for j in range(i , (n+1)-1):
        print("*", end=" ")
    print()