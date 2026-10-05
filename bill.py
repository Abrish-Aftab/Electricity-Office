import time
from datetime import date, timedelta
import shutil


# FAKE DATE
fake_date = date(2026, 7, 2)
last_update = time.time()

# USER CODES
bills = ["1279", "1280", "1281"]

# USER STATUS
user_status = {
    "1279": "ACTIVE",
    "1280": "ACTIVE",
    "1281": "ACTIVE"
}

# BILL AMOUNTS
bill_amount = {
    "1279": 150.00,
    "1280": 123.69,
    "1281": 2950.01
}


# DUE DATES
due_date = {
    "1279": date(2026, 7, 15),
    "1280": date(2026, 7, 19),
    "1281": date(2026, 7, 23)
}


# BILL STATUS
# 0 = unpaid
# 1 = paid
bill_status = {
    "1279": 0,
    "1280": 0,
    "1281": 0
}


# EXTRA BILL STATUS
# 0 = extra bill not added
# 1 = extra bill already added

extra_bill_added = {
    "1279": 0,
    "1280": 0,
    "1281": 0
}


# WIDTH
width = shutil.get_terminal_size(fallback=(80, 24)).columns


# FUNCTIONS

def disconnect_meter(user):
    if user_status[user] == "ACTIVE":
        user_status[user] = "DISCONNECTED"
        time.sleep(1)
        print("NOTIFICATION: Your meter has been disconnected.")
    else:
        time.sleep(1)
        print("User is already disconnected")
    input("Click enter to continue...")


def bill_1279():
    status = user_status["1279"]
    print()
    user = """68h Albun Street
Mincur Road
578345
First Name:    John
Last Name:     Schmo
Mobile:        +782345
Email:         JohnSchmo@email.com"""
    time.sleep(1)
    print(user)
    current_status = f"USER STATUS : {status}"
    print()
    print(current_status.center(width))
    input("Click enter to continue...")


def bill_1280():
    status = user_status["1280"]
    print()
    user = """89h Ginger Street
Pesnum Road
578988
First Name:    Mark
Last Name:     Lester

Mobile:        +895345
Email:         MarkLester@email.com"""
    time.sleep(1)
    print(user)
    current_status = f"USER STATUS : {status}"
    print()
    print(current_status.center(width))
    input("Click enter to continue...")


def bill_1281():
    status = user_status["1281"]
    print()
    user = """34h Kensula Street
Alexander Road
234681
First Name:    Lisbon
Last Name:     Clark
Mobile:        +998292
Email:         LisbonClark@email.com"""
    time.sleep(1)
    print(user)
    current_status = f"USER STATUS : {status}"
    print()
    print(current_status.center(width))
    input("Click enter to continue...")


# BILL CHECK


def check_bill(user):
    time.sleep(1)
    print("BILL INFORMATION".center(width))
    print()
    print(f"User code = {user}".center(width))
    print(f"Amount = ${bill_amount[user]}".center(width))

    print(f"Due date = {due_date[user]}".center(width))

    if bill_status[user] == 1:
        print("BILL STATUS = PAID".center(width))
    else:
        print("BILL STATUS = UNPAID".center(width))
    input("Click enter to continue...")

# PAY BILL


def pay_bill(user):
    if bill_status[user] == 1:
        time.sleep(1)
        print("\nBill already paid")
    elif user_status[user] == "DISCONNECTED":
        time.sleep(1)
        print("\nMeter disconnected")
    else:
        time.sleep(1)
        ans = input("\nDo you want to pay the bill?  ")
        ans = ans.capitalize()
        if ans == "Yes":
            bill_status[user] = 1
            time.sleep(2.5)
            print("\nYour bill has been paid")
        elif ans == "No":
            time.sleep(1)
            print("\nYour bill remains unpaid")
        else:
            print("\nInvalid answer")
    input("Click enter to continue...")


# START

print("STARS electricity office".center(width))
print("\t\t\t\t\t\tDate:",fake_date)
time.sleep(1)
print("Goodmorning.")
time.sleep(1)
print("Do you want to do anything else?  ")
print("What else would u like to perform")


# USER CODE LIST

time.sleep(1)
print("*USER CODE LIST*".center(width))

print(bills[0])
print(bills[1])
print(bills[2])


time.sleep(2)
user_input = input("\nWhat is your user code?  ")

match user_input:
    case "1279" | "1280" | "1281":
        pass
    case _:
        print("\nWrong user code")
        exit()


# KEEP SAME USER RUNNING

while True:

    # CHECK DATE
    if time.time() - last_update >= 30:
        fake_date += timedelta(days=1)
        last_update = time.time()
        print("\t\t\t\t\t\tDate:",fake_date)


        # CHECK EXTRA BILL
        for user in bills:
            if (fake_date > due_date[user] and extra_bill_added[user] == 0):
                bill_amount[user] = (bill_amount[user] + 40.63)
                extra_bill_added[user] = 1


    # USER ACTIONS

    actions = """1. Check user information
2. Check pending bills
3. Pay the pending bill
4. Disconnect your meter
5. Exit"""
    print()
    print("*USER ACTION LIST*\n".center(width))
    print(actions)
    time.sleep(2)
    action = input("\nWhat help do you need today?  ")


    # ACTIONS
    match action:
        # CHECK USER INFORMATION
        case "1":
            if user_input == "1279":
                bill_1279()
            elif user_input == "1280":
                bill_1280()
            elif user_input == "1281":
                bill_1281()


        # CHECK BILL
        case "2":
            check_bill(user_input)


        # PAY BILL
        case "3":
            pay_bill(user_input)


        # DISCONNECT METER
        case "4":
            disconnect_meter(user_input)


        # EXIT
        case "5":
            print("\nThank you for visiting STARS electricity office.")
            break
            exit()

        # INVALID ACTION

        case _:
            print("\nInvalid action.")