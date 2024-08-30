
def store_immutable_data(passport_number, BOD, other_immutable_data):
    # Immutable data stored in a tuple
    # passport_number = 'A1234567'
    # BOD = '1999-11-15'
    # other_immutable_data = 'Your data is safe for our function.'
    immutable_data = (passport_number, BOD, other_immutable_data)
    return immutable_data

def send_reminder(data):
    passport_number, BOD, other_immutable_data = data
    
    print(f"Reminder: Your passport number is {passport_number}")
    print(f"Reminder: Your Birth of date is {BOD}")
    print(f"Reminder: Your Other data stored.. {other_immutable_data}")
    print("Please keep your information safe and up to date!")

passport_number = input('Enter your passport number...: ')
BOD = input('Enter your Birth of date..: ')
other_immutable_data = input('Enter your data..: ')
immutable_data = store_immutable_data(passport_number, BOD, other_immutable_data)
send_reminder(immutable_data)