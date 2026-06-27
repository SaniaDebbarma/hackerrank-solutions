#to find the runner up score, so basically runner up score means 2nd 
n = int(input("enter numnber: "))
arr = map(int, input().split()) #here u will get input like [6,7,8], and what is split, so split() is a built-in string method used to divide a string into a list of substrings
runnerup = list(set(arr))
runnerup.sort(reverse=True)
print(runnerup[1])

#matlab split karne se --> " hey yo wossup becomes" = "hey", "yo", "wossup"
