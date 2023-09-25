print("This IT Organization has various skill sets")
print("Find out your match")
print("Enter Capitalised Values: ")

DevOps = ["Jenkins", "Ansible", "Bash", "Puppet", "Dockers", "Kubernetes", "Terraform"]
Development = ("nodeJS", "Angularjs", "Java", ".net", "Python")
cntr_emp1 = {"name": "Santa", "Skill":"Blockchain", "Code":1024}
cntr_emp2 = {"name": "Rocky", "Skill":"AI", "Code":1218}
usr_skill = input("Enter here desired skill: ")
print(usr_skill)

if usr_skill in DevOps:
    print(f"We have {usr_skill} in DevOps Team.")
elif (usr_skill in Development):
    print(f"we have {usr_skill} in Development Team.")
elif (usr_skill in cntr_emp1.values()) or (usr_skill in cntr_emp2.values()):
    print(f"We have contract employees with {usr_skill} skill")
else:
    print("Skill not found")
    print("Please check if you have entered value in capitalize or check the spelling")
