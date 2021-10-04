def table():
    num = input("Which table do you want to print?")
    num = int(num)
    count = 0
    while count<10:
        count = count + 1
        table = num*count
        print(table)
table()
