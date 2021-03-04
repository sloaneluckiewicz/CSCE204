# list birthdays and find closest birthday coming up
from datetime import date

birthdays = [
    date(2021, 2, 16), date(2021, 9, 3), date(2021, 7, 10), date(2021, 10, 28), date(2021, 10,9), date(2021, 5, 6), date(2021, 5, 25), date(2021, 8, 8)
]

closestBirthday = date(2021,12,31)

for birthday in birthdays:
    daysTillClosest = (closestBirthday - date.today()).days
    daysTillBirthday = (birthday - date.today()).days

    # birthday already passed
    if daysTillBirthday < 0:
        continue
    #go to next item in list --> back to beginning of for loop

    if daysTillBirthday < daysTillClosest:
        closestBirthday = birthday

print("Closest birthday is: " + closestBirthday.strftime("%m/%d/%y"))



