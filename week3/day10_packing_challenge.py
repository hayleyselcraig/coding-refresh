
packing_list = ["passport", "sunglasses", "camera"]

new_item = (input("What would you like to add to your packing list? "))
if new_item in packing_list:
    print(f" {new_item} is already packed!")
else:
    packing_list.append(new_item)
    print(f"{new_item} has been added to your packing list.")

for item in packing_list:
    print(f"Remember to pack: {item}")