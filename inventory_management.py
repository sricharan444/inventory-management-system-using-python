import inventory
product=[{"id":0,"name":"Biscuit","price":10,"quantity":100},{"id":7,"name":"Redbull","price":250,"quantity":200},{"id":1,"name":"choco","price":10,"quantity":100},{"id":8,"name":"TV","price":250,"quantity":200},{"id":2,"name":"tea","price":50,"quantity":200},{"id":9,"name":"AC","price":100,"quantity":100},{"id":3,"name":"coffee","price":250,"quantity":200},{"id":10,"name":"mobile","price":100,"quantity":100},{"id":4,"name":"dal","price":1250,"quantity":200},{"id":11,"name":"Laptop","price":100,"quantity":100},{"id":5,"name":"rice","price":4250,"quantity":200},{"id":12,"name":"tablet","price":100,"quantity":100}]
inventory.createInventory(product)
ch=int(input("enter any number 1.addItem 2.print the data 3.get total value 4.search 5.delete a item 6.update details"))
match ch:
    case 1:
        id=input("enter id of product")
        name=input("enter your product name")
        price=int(input("enter cost of product"))
        quantity=int(input("enter quantity in inventory"))
        d={"id":id,"name":name,"price":price,"quantity":quantity}
        inventory.addItem(d,product)
    case 2:
        inventory.load(product)
    case 3:
        inventory.total_value(product)
    case 4:
        try:
            k=input("enter id of the product you want to search")
            inventory.search(k)
        except:
            print("data not found")
    case 5:
        try:
            k=input("enter the id of the data you want to delete")
            inventory.delItem(k)
        except:
             print("data not found")
    case 6:
        inventory.updateDetails()
    case default:
        print("enter a valid value")