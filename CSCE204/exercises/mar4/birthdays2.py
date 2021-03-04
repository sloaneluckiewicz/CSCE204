# list birthdays and find closest birthday coming up
from datetime import date

birthdays = {
    "Sloane": date(2021, 2, 16), 
    "Camille": date(2021, 9, 3), 
    "Jane": date(2021, 7, 10), 
    "Kaden": date(2021, 10, 28), 
    "Treyten": date(2021, 10,9), 
    "Mamacita": date(2021, 5, 6), 
    "Remi": date(2021, 5, 25), 
    "Mason": date(2021, 8, 8)
}

closestBirthday = date(2021,12,31)
closestFriend = ""

for person in birthdays:
    birthday = birthdays[person]
    daysTillClosest = (closestBirthday - date.today()).days
    daysTillBirthday = (birthday - date.today()).days

    # birthday already passed
    if daysTillBirthday < 0:
        continue
    #go to next item in list --> back to beginning of for loop

    if daysTillBirthday < daysTillClosest:
        closestBirthday = birthday
        closestFriend = person

print(f"Closest birthday is: {closestFriend} " + closestBirthday.strftime("%m/%d/%y"))