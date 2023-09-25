
message = "hola a todos"

"""
print(message)
print(message.capitalize())
message = message.capitalize()
print(message)


print(dir(message))



print(message.upper())
print(message.islower())
print(message.isupper())


seq1 = ("192", "168", "40", "90")
print(".".join(seq1))
print("/".join(seq1))
print("-".join(seq1))
"""

mountains = ["Everest", "Himalaya", "Sahyadri", "Alps", "K2", "Mt Hood"]
print(mountains)

mountains.append("Oregon Mount")
print(mountains)

mountains.extend(["Mt Rainer", "Satpuda"])
print(mountains)

mountains.insert(2, "Mt Abu")
print(mountains)

mountains.pop()
mountains.pop()
mountains.pop()
print(mountains)

mountains.pop(5)
print(mountains)

cntr_emp1 = {"name":"Brais", "Skill":"DevOps", "Code":1254}
print(cntr_emp1.keys())
print(cntr_emp1.values())
cntr_emp1.clear()
print(cntr_emp1)
