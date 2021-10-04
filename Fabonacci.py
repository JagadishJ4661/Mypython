def fab():
    a = 1
    b = 2
    count = 0
    while count<10:
        count = count + 1
        a = a + b
        b = a + b
        print(a, b)
fab()
