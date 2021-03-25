def getPhoneBook():
    phoneBook = {}
    with open("exercises/mar23/phones.txt") as file:
        for line in file:
            data = line.split(',')
            friend = data[0].strip()
            phone = data[1].strip()
            phoneBook[friend] = phone
        return phoneBook

def getPhone(phoneList):
    friend = input("Enter Person's Name: ").strip().lower()
    if friend in phoneList:
        print(f"{phoneList[friend]}")
    else:
        print(f"Sorry, {friend} is not in our system.")

print("Displaying Phone Book")
phoneList = getPhoneBook()
for person in phoneList:
    print(f"{person}: {phoneList[person]}")

getPhone(phoneList)