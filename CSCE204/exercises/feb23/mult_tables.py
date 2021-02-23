#  multiplication table
""" 
1 2 3 4 5
1 4 6 8 10
"""

tableSize = int(input("Enter size of table: "))

for row in range(1, tableSize+1):           # loop through rows
    for col in range(1, tableSize+1):       # for every row loop their cols
        ans = row * col

        # if there is just one digit in the number
        if len(str(ans)) == 1:
            print(f" {ans}", end= " ")
        else:
            print(ans, end = " ")
    print()