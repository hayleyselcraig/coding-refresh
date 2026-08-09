## Create a simple holiday packing list.

packing_list = ["passport", "sunglasses", "camera", "suncream"]

print(packing_list)
print(packing_list[2])
print(len(packing_list))

packing_list.append("toothbrush")
packing_list.remove("suncream")

print(packing_list)

for item in packing_list:
    print(f"Remember to pack: {item}")


packing_list.append(input("What would you like to add to your packing list? "))
for item in packing_list:
    print(f"Remember to pack: {item}")


if "passport" in packing_list:
    print("Passort is already packed!")
else:
    print("Remember to pack your passport!")