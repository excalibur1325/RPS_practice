to_do_list = ["Code", "Eat", "Sleep"]
selection = ""

while selection != "4":
    selection = input("\n Please enter a number: \n\
1. View to-do list \n\
2. Add to list \n\
3. Remove from list \n\
4. Quit\n")
    if selection == "1":
        print("Here's your to-do list:\n")
        for item in to_do_list:
            print(item)
        input("Press enter to continue...")
    if selection == "2":
        item_to_be_added = input("\nWhat would you like to add?\n")
        to_do_list.append(item_to_be_added)
        print(f"The following item was added to the to-do list{item_to_be_added}")
        print("Press enter to continue...")
    if selection == "3":
        counter = 1
        for item in to_do_list:
            print(f"{counter}. {item}")
            counter += 1
        item_to_be_removed = input("Which item would you like to remove?")
        to_do_list.pop(int(item_to_be_removed - 1))
        input("Item removed. Press enter to continue...")

print("Goodbye!")    