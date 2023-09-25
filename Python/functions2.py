"""

def order_food(min_order, *args):
    print(f"You have orderer: {min_order}")
    for item in args:
        print(f"You have ordered: {item}")
    print("Your food will be delivered in 30 mins:")
    print("Enjoy the party")

order_food("salad", "pizza", "Biryani", "Soup")
"""
import random


def time_activity(*args,**kwargs):

    min = sum(args) + random.randint(0, 60)
    choice = random.choice(list(kwargs.keys()))
    print(f"You have to spent {min} minutes for {kwargs[choice]}")

time_activity(10,20,10, hobby="Dance", sport="Boxing", fun="Driving", work="DevOps")