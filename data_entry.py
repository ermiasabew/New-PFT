from datetime import datetime
date_format="%d-%m-%Y"
CATEGORIES={"I":"Income","E":"Expense"}
def get_date(prompt,allow_defualt=False):
    date_str=input(prompt)
    if allow_defualt and not date_str:
        return datetime.today().strftime(date_format)
    try:
        valid_date=datetime.strptime(date_str,date_format)
        return valid_date.strftime(date_format)
    except VlaueError:
        print("Invalid dateformat.please enter the date in dd-mm-yyyy format")
        return get_date(prompt,allow_defualt=False)

def get_amount():
    try:
        amount=float(input("Enter the amount:"))
        if amount <=0 :
            raise VlaueError("Amount must be none negative none zero value")
        return amount
    except VlaueError as e:
        print(e)
        return get_amount()

def get_category():
    category=input("Enter the catagory ('I' for Income and 'E' for expense):").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]
    print("Invalid Category.Please Enter 'I' for Income or 'E' for expense")
    return get_category()

def get_description():
    return input("Enter description(Optional):")
