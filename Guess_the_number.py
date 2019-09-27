a=input("Enter a Number Between 1-25 = ")
c=input("Enter Your Guess = ")
b=0
for i in range(1,25):
    if a==c:
        print("\nYou Found it in {} times".format(b+1))
        break
    elif c>a:
        print("Your Number is Higher\n")
        b+=1
        c=input("Wrong, Enter Again = ")
    else:
        print("Your Number is Lower\n")
        b+=1
        c=input("Wrong, Enter Again = ")
