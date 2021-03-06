# Author: Sloane Luckiewicz

from datetime import date, time, datetime

print("Today's appointments include: ")

appointments = {"Yoga -Vinyasa Flow": time(9,30),
                "Intro to Networking": time(10,45),
                "Feed cats": time(12,0),
                "Lunch": time(12,30),
                "Laundry": time(13,0),
                "Clean dishes": time(13,30),
                "Homework": time(14,00),
                "Tennis practice": time(15,15),
                "Dinner": time(16,30),
                "Work": time(18,0)           
}

# loop through and display list of appointments
counter = 1

for appointment in appointments:
    timeDue = appointments[appointment]
    print(f"{counter}. {appointment} -Due: " + timeDue.strftime("%I:%M %p"))

    counter +=1