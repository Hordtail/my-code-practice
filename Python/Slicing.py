"""

planet1 = "Closest to Sun"

print(planet1)

print(planet1[0])
print(planet1[1])
print(planet1[2])
print(planet1[3])

print(planet1[-1])
print(planet1[-2])
print(planet1[-3])

print(planet1[1:4])

print(planet1[:])
print(planet1[:7])
print(planet1[11:])

DevOps = ("Linux", "Vagrant", "Bash", "AWS", "Jenkins")
print(DevOps[0])
print(DevOps[4])

print(DevOps[2:4])


print(DevOps[2:4][0])

print(DevOps[2:4][0][0:4])

"""

Skills = {"DevOps": ("AWS", "Jenkins", "Python", "Ansible"), "Development": ["Java", "NodeJS", ".net"]}

print(Skills)
print(Skills["DevOps"])
print(Skills["Development"])
print(Skills["DevOps"][-1])
print(Skills["DevOps"][-1][:5])