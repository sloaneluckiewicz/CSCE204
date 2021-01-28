print("Let's Find a Discount")

weekDay = input("Enter day of week: ") .lower() .strip()

if weekDay == "monday" or weekDay == "mon":
    print("Moes Monday")
elif weekDay == "tuesday" or weekDay == "tues":
    print("Taco Tuesday")
elif weekDay == "wednesday" or weekDay == "wed":
    print("Woo Wednesday")
elif weekDay == "thursday" or weekDay == "thurs":
    print("Thirsty Thursday")
elif weekDay == "friday" or weekDay == "fri":
    print("Friendly Friday")
else:
    print ("No discount today")

print("Goodbye")