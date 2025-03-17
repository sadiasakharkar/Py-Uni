n = int(input("Enter the number of rows: "))

for i in range(n):
    for j in range(i , n):
        print("*" , end=" ")
    print()


# * * * * *     i = 0       will run from 0 to 5
# * * * *       i = 1       will run from 1 to 5
# * * *         i = 2       will run from 2 to 5
# * *           i = 3       will run from 3 to 5
# *             i = 4       will run from 4 to 5