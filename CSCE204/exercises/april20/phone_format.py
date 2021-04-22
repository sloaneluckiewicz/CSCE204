# original phone format (724)-610-7222
# desired phone format 724.610.7222

def update_phone(phone):
    answer = ""

    for char in phone:
        if char == "(" or char == ")":
            continue 
        elif char =="-":
            answer += "."
        else:
            answer += char

    return answer 

phone = update_phone("(724)-610-7222")
print(phone)