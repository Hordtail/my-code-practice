"""

for i in "DevOps":
    print(i)
    if i == "O":
        print("Found my data.")
        break
print("Out of Loop")



for i in "DevOps":
    print(i)
    if i == "O":
        print("Found my data.")
        continue
    print(f"Value of i is {i}")
print("Out of Loop")


import random
Vaccines = ["Moderna", "Pfizer", "Sputnik V", "Covaxin", "AstraZeneca"]

random.shuffle(Vaccines)
print(Vaccines)

Lucky = random.choice(Vaccines)
print(Lucky)

for vac in Vaccines:
    print(f"*****TESTING VACCINE {vac}")
    if vac == Lucky:
        print("#################################")
        print(f"{Lucky} vaccine, test Succesful")
        print("#################################")
        print()
        break
    print("XXXXXXXXXXXXXXXX")
    print("Test Failed")
    print("XXXXXXXXXXXXXXXX")
print()

"""



import random
Vaccines = ["Moderna", "Pfizer", "Sputnik V", "Covaxin", "AstraZeneca"]

random.shuffle(Vaccines)
print(Vaccines)

Lucky = random.choice(Vaccines)
print(Lucky)

for vac in Vaccines:
    print(f"*****TESTING VACCINE {vac}")
    if vac == Lucky:
        print("#################################")
        print(f"{Lucky} vaccine, test Succesful")
        print("#################################")
        print()
        continue
    print("XXXXXXXXXXXXXXXX")
    print("Test Failed")
    print("XXXXXXXXXXXXXXXX")
print()