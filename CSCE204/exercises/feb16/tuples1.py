# tuple = things you cannot change -- i.e. assigned seats in a classroom (we know wont change)

weekDays = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

# \n = new line
# loop through and display items in the table
counter = 0
for day in weekDays:
    if counter == len(weekDays)-1:  #makes saturday not end with comma
        print(f"{day} ")
    else: 
        print(f"{day}, ", end="" )     #prints on one line
    counter +=1
