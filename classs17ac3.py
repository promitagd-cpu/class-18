flag = False
while not flag:
    try:
        number = int(input("Enter a number:  "))
        while number % 2 == 0:
            print ("Bye")
            number = int(input("Enter a number:  "))
        valid = True
    except ValueError:
        print ("Invalid")
        

