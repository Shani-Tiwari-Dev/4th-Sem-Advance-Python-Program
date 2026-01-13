address_book = {}


def add_record():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    address_book[name] = phone
    print("Record Added")


def modify_record():
    name = input("Enter name to modify: ")
    if name in address_book:
        phone = input("Enter new phone: ")
        address_book[name] = phone
        print("Record Updated")
    else:
        print("Record Not Found")


def display_record():
    for name, phone in address_book.items():
        print(name, ":", phone)


def delete_record():
    name = input("Enter name to delete: ")
    if name in address_book:
        del address_book[name]
        print("Record Deleted")
    else:
        print("Record Not Found")


while True:
    print("\n1.Add 2.Modify 3.Display 4.Delete 5.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        add_record()
    elif choice == 2:
        modify_record()
    elif choice == 3:
        display_record()
    elif choice == 4:
        delete_record()
    elif choice == 5:
        break
    else:
        print("Invalid Choice")
