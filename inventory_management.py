import inventory
ch=int(input("enter any number 1. create inventory 2.addItem 3.print the data 4.get total value 5.search 6.update data 7.delete data "))
match ch:
    case 1:
        inventory.createInventory()
    case 2:
        inventory.addItem()
    case 3:
        print(inventory.load())
    case 4:
        inventory.total_value()
    case 5:
        print(inventory.search())
    case 6:
        inventory.updateDetails()
    case 7:
        inventory.delItem()
    case default:
        print("enter a valid value")
