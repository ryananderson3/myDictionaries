person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

#print(person["children"][1])

#print(person["pets"]["cat"])

for child in person["children"]:
    print(child)
print()
for pet in person["pets"]:
    print(person["pets"][pet])
