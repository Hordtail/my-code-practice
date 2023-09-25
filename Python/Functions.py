"""
def add(arg1, arg2):
    total = arg1 + arg2
    return total

out = add(2,3)
print(out)
print(add(10,30))

def adder(arg1, arg2):
    total = arg1 + arg2
    print(total)
    return None

adder(10,50)
print(adder(10,50))


def summ(arg):
    x = 0
    for i in arg:
        x = x + i
    return x

out = summ([10,20,30])
print(out)

summ([10,20],[30,50])



def greetings(MSG="Morning"):
    print(f"Good {MSG}")
    print("Welcome to the function")

greetings("Evening")

"""


def vac_feedback(vac, efficacy):
    print(f"{vac} vaccine is having {efficacy} % efficacy.")
    if (efficacy > 50) and (efficacy <= 75):
        print("Seems not so effective, need more trial")
    elif (efficacy > 75) and (efficacy < 90):
        print("Can consider this vaccine")
    elif efficacy >= 90:
        print("Sure, will take the shot")
    else:
        print("Needs many more trials")


vac_feedback("pfizer", 95)
vac_feedback("unknown", 45)
vac_feedback(efficacy=34, vac="unknown")
