from encyptandbookride import hash_password
from abc import ABC, abstractmethod

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = self.hashed_password(password)
        self.books = []
        self.borrowed_books = []
        self.borrowed_books_count = 0
    def hashed_password(self, password):
        return hash_password(password)
    def verify_password(self, password):
        return self.password == hash_password(password)
""" # Uges:
user = User('Mahmub', 'mahmub@gmail.com', 'dog4legs')
# Verify password
print(user.verify_password('dog4legs'))  # True
password_input = 'dog4legs'
if user.verify_password(password_input):
    print('Password is correct!')
else:
    print('Password is Wrong!') """

class Rider(User):
    def __init__(self, username, email, password, license_number, vehicle_type):
        super().__init__(username, email, password)
        self.license_number = license_number
        self.trip_history = []
        self.vehicle_type = vehicle_type
    def book_ride(self, source, destination):
        # Add the ride to the trip history
        trip = {'source': source, 'destination': destination}
        self.trip_history.append(trip)
        print(f'{self.username} for a book rider : {source} from {destination}')
    def cancel_ride(self, source, destination):
        # Remove the ride from the trip history
        for trip in self.trip_history:
            if trip['source'] == source and trip['destination'] == destination:
                self.trip_history.remove(trip)
    def view_trip_history(self):
        print(f'{self.username} of trip history')
        for trip in self.trip_history:
            print(f'Source: {trip["source"]}, destination: {trip["destination"]}')
class Driver(User):
    def __init__(self, username, email, password, vehicle_number, license_number):
        super().__init__(username, email, password)
        self.vehicle_number = vehicle_number
        self.license_number = license_number
        self.assigned_rides = []   
    def accept_ride(self, ride_details:dict):
        self.assigned_rides.append(ride_details)
        print(f'{self.username} ride accept : {ride_details["source"]} from {ride_details["destination"]}')
    def cancel_ride(self, ride_details:dict):
        self.assigned_rides.remove(ride_details)
    def view_assigned_rides(self):
        print(f'{self.username} of assigned rides')
        for ride in self.assigned_rides:
            print(f'Source: {ride["source"]}, destination: {ride["destination"]}')
""" # Useges:
# Rider
rider = Rider('Mahbub', 'mahbub@gmail.com', 'dog4legs', '123Dh', 'Car')
rider.book_ride('Downtown', 'Airport')
rider.view_trip_history()
# Driver
driver = Driver('Mahmub', 'mahmub@gmail.com', 'dog4legs', 1)
ride_details = {'source':'Downtown', 'destination':'Airport'}
driver.accept_ride(ride_details)
driver.view_assigned_rides() """

""" class LicensecheckAuthority(ABC):
    @abstractmethod
    def check_license(self, user):
        pass
class LocalLicenseCheckAuthority(LicensecheckAuthority):
    def check_license(self, driver):
        if len(driver.license_number) == 6 and driver.license_number.isdigit():
            print(f'{driver.username}s license is authenticate ')
            return True
        else:
            print(f'{driver.username}s license is not authenticate')
            return False
# Usages:
driver = Driver('Rahim', 'rahim@gmail.com', 'dog4legs', 'ABC-1234', 123456)
license_authority = LocalLicenseCheckAuthority()
if license_authority.check_license(driver):
    print('Ride accept for you')
else:
    print('License authority fail. so Ride accept not for you ')
 """
