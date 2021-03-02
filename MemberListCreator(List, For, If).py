Total = int(input("How many people in the class?: "))
Member = int(input("How many are the most members you want to have in a group?: "))

if Total % Member == 0:
    Group = Total//Member
    print("Then we need to split people into " + str(Group) + " groups.")
else:
    Group = Total//Member + 1
    print("Then we need to split people into " + str(Group) + " groups.")

L = []

for i in range(1, Group+1):
    L.append(list())
    print("Please key in the members' name for the group_" + str(i))
    for j in range(0, Member):
        new_name = input("Please add a new name. And leave a blank to pass on to the next group: ").strip().capitalize()
        if new_name == "":
            break
        else:
            L[i-1].append(new_name)

print("Here is the member list of the class: ")
print(L)
