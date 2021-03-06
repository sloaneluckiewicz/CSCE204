# Author: Sloane Luckiewicz

from datetime import date

holidays = {
    "Valentines Day": date(2021, 2, 14),
    "St. Patricks Day": date(2021, 3, 17),
    "Arbor Day": date(2021, 4, 30),
    "Cinco De Mayo": date(2021, 5, 5),
    "4th of July": date(2021, 7, 4),
    "Pioneer Day": date(2021, 7, 24),
    "Halloween": date(2021, 10, 31),
    "Christmas": date(2021, 12, 25)
}


for holidayName in holidays:
    holiday = holidays[holidayName]
    daysTillHoliday = (holiday - date.today()).days

    if daysTillHoliday < 0:
        print(f"{holidayName} {holiday} has passed")

    elif daysTillHoliday <= 30:
        print(f"{holidayName} {holiday} is {daysTillHoliday} days away.")

    elif daysTillHoliday >= 31:
        print(f"{holidayName} {holiday}")



