x = 0
while x <=100:
    print(x)
    x+=1
    if x % 3 ==0 and x % 5 == 0:
        print("fizzbuzz")
    elif x % 3 == 0:
        print("fizz")
    elif x % 5 == 0:
        print("buzz")
