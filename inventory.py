import json
my_dict=[{"id":0,"name":"Biscuit","price":10,"quantity":100},{"id":7,"name":"Redbull","price":250,"quantity":200},{"id":1,"name":"choco","price":10,"quantity":100},{"id":8,"name":"TV","price":250,"quantity":200},{"id":2,"name":"tea","price":50,"quantity":200},{"id":9,"name":"AC","price":100,"quantity":100},{"id":3,"name":"coffee","price":250,"quantity":200},{"id":10,"name":"mobile","price":100,"quantity":100},{"id":4,"name":"dal","price":1250,"quantity":200},{"id":11,"name":"Laptop","price":100,"quantity":100},{"id":5,"name":"rice","price":4250,"quantity":200},{"id":12,"name":"tablet","price":100,"quantity":100}]

def createInventory(my_dict):
    with open("ch.json", "w") as f:
        json.dump(my_dict, f)

def load(my_dict):
    with open("ch.json", "r") as f:
        my_dict = json.load(f)
        print(my_dict)

def addItem(d,my_dict):
    my_dict.append(d)
    createInventory(my_dict)

def delItem(k):
    for i in my_dict:
        if i["id"]==k:
            my_dict.remove(i)
    createInventory(my_dict)

def search(k):
    for i in my_dict:
        if i["id"]==k:
            print(i)
def updateDetails():
    try:
        a=input("enter the id of the item which you wanted to change")
        k=input("enter the attribute name you want to change")
        v=input("enter the value to be changed")
        for i in my_dict:
            if i["id"]==a:
                i[k]=v
    except:
        print("enter correct data")
def total_value(my_dict):
    count=0
    for i in my_dict:
        count+=i["quantity"]*i["price"]
    print(count)






