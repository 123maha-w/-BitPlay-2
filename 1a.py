def checkIfSame (number1,number2):
    if ((number1 ^ number2) !=0 ):
        print("Numbers are not equal ")
    else:
        print("both Numbers are equal")

number1 = int(input("enter first numer to compare : "))
number2 = int(input("enter second numer to compare : "))

checkIfSame(number1,number2)