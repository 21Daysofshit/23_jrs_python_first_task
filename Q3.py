Computers = {
    "Laptop1" :{
        "brand" : "Dell", "OS" : "Windows"
    },
    "Laptop2" : {
        "brand" : "HP", "OS" : "Linux"
    },
    "Laptop3" : {
        "brand" : "Apple", "OS" : "Mac-OS"
    }
}
brand = []
os = []
for i in Computers:
    brand.append(Computers[i]["brand"])
    os.append(Computers[i]["OS"])
print(brand)
print(os)