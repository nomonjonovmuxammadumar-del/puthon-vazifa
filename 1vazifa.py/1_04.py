ism = input("Ism: ")
familiya = input("Familiya: ")
username = ism[:3].lower() + "_" + familiya[:3].lower()
print("Username:", username)