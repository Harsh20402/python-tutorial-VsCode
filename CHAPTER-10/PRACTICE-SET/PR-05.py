# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways. 

from random import randint

# Class representing an Indian Railways train
class Train:
    # Constructor to initialize train details
    def __init__(self, train_no, start_place, destination_place):
        self.train_no = train_no
        self.start_place = start_place
        self.destination_place = destination_place
        self.seats = 100  # Assume 100 seats are available initially
        self.fare_per_km = 2  # Example: ₹2 per km
        self.distance = randint(200, 2000)  # Random distance between 200–2000 km

    # Method to book a ticket
    def book(self):
        if self.seats > 0:
            self.seats -= 1
            print(f"✅ Ticket booked in train no. {self.train_no} from {self.start_place} to {self.destination_place}.")
            print(f"Remaining seats: {self.seats}")
        else:
            print("❌ No seats available.")

    # Method to check train status
    def getStatus(self):
        print(f"ℹ️  Train no. {self.train_no} is running on time.")

    # Method to get fare information
    def getFare(self):
        fare = self.fare_per_km * self.distance
        print(f"💰 Fare from {self.start_place} to {self.destination_place} is ₹{fare} (Distance: {self.distance} km).")

# Create an object of the Train class
t = Train(1234, "Kolkata", "Delhi")

# Call methods
t.book()
t.getStatus()
t.getFare()
