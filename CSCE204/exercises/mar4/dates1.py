from datetime import date, time, datetime

todaysDate = date.today()

print(todaysDate)
print(todaysDate.strftime("%m/%d/%y")) # format date
print(todaysDate.strftime("%A %B %d,%Y"))
print(todaysDate.strftime("%B %d: %A, Year: %y"))

todaysDateTime = datetime.now()
print(todaysDateTime.strftime("%B %d, %Y, %I:%M %p"))

halloween = date(2021, 10, 31)
meeting = time(14, 30)
appointment = datetime(2021, 3, 14, 13, 59)

birthdayInput = input("Enter Birthday (MM/DD/YYYY): ").strip() 
birthday = datetime.strptime(birthdayInput, "%m/%d/%Y")
print("Your birthday: " + birthday.strftime("%A %B %d, %Y"))    # dont use f command to input use concatenation symbol 

# how long untill your appt
days = (appointment - datetime.now()).days
print(f"You have {days} days until your appointment")
