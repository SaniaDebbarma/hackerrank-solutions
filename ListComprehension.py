#PERMUTATIONS
x = int(input("enter a number : "))
y = int(input("enter a number: "))
z = int(input("enter a number: "))
n = int(input("enter a number: "))

result = [[ i, j, k]for i in range (z+1) for j in range (y+1) for k in range(z+1)if i + j+ k != n]
print (result)

#in this code, if u input is 3 = it will print possible combinations which is not equal to 3, for example [1,1,1]= 3 so it will not be included, and [1,0,1],[1,1,0]are included