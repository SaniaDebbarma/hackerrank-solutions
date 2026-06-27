
n = int (input("Enter a number : ").strip())
if n % 2 != 0: #if n is odd then print "Weird"
    print("Weird")
elif n % 2 == 0 and 2<= n <=5 : #if n is even and also between 2 and 5 then print ("Not weird")
    #you can also write ----->> elif n % 2 == 0 and n<=2 and n<=5:
    print("Not Weird")
else:
    print ("Weird")