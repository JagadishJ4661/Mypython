def number():
    Number = input("please enter a number")
    Number = int(Number)
    if Number<10:
        Number = Number + 7
        Number = Number % 10
        print(Number)
    if Number>=10 and Number<100:
        Number = Number**5
        Number = Number % 10
        print(Number)
    if Number>=100 and Number<1000:
        Number2 = input("Please enter another number")
        Number2 = int(Number2)
        Number = Number + Number2
        Number = Number % 10
        print(Number) 
number()
