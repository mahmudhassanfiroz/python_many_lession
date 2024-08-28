
import hashlib
from abc import ABC, abstractmethod
# password = 'dog4legs'
# password_hash = hashlib.md5()
# encode_password = password.encode('utf-8')
# # print(encode_password)
# password_hash.update(encode_password)
# password_hex = password_hash.hexdigest()
# print(password_hex)
def hash_password(password):
    password_hash = hashlib.md5()
    encode_password = password.encode('utf-8')
    password_hash.update(encode_password)
    password_hex = password_hash.hexdigest()
    return password_hex 

# password = input()
# hashed_password = hash_password(password)
# print(hashed_password)
class RideService(ABC):
    @abstractmethod
    def get_ride(self, user_id):
        pass
    @abstractmethod
    def book_ride(self, source, destination):
        pass
    @abstractmethod
    def calculate_fare(self, distance:float):
        pass
class UrbanRides(RideService):
    BASE_FARE = 50
    FARE_PER_KM = 10
    def get_ride(self, user_id):
        # return a list of available rides for the user
        return [1,2,3]
        
        # return a ride object with user_id
        # return Ride(user_id)
    
    
    def book_ride(self, source, destination):
        print(f'{source} from {destination} ')
    def calculate_fare(self, distance:float):
        fare = self.BASE_FARE + distance * self.FARE_PER_KM
        return fare
# Usages:
ride_service = UrbanRides()
ride_service.get_ride(2)
ride_service.book_ride('Downtown', 'Airport')
fare = ride_service.calculate_fare(12.5)
print(f'Total fare : {fare}')