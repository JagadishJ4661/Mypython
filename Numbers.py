'''Take 2 numbers from the user, Print which number is 2 digit number and which number is 3 digit number
If it neither, then print the number as it is'''


def entry():
    num1 = input("Select any number that you wish.")
    num1 = int(num1)
    num2 = input("select any number that you wish again.")
    num2 = int(num2)
    print(num1, num2)
    if num1>=10 and num1<100:
        print(num1,"is a two digit number")
    if num2>=10 and num2<100:
        print(num2, "is a two digit number")
    if num1>=100 and num2<1000:
        print(num1,"is a three digit number")
    if num2>=100 and num2<1000:
        print(num2,"is a two digit number")
    if num1<10 and num1>=1000:
        print(num1)
    if num2<10 and num2>=1000:
        print(num2)

entry()
