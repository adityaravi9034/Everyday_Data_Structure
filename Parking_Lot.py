"""You are tasked with designing a parking lot management system for a multi-level parking structure. 
The parking structure has multiple levels, each containing a certain number of parking spots. 
The parking spots can be either regular spots or spots reserved for specific vehicles (e.g., handicapped spots).

Design a data structure and implement the necessary functions to support the parking lot management system.
The data structure should store information about the parking levels, spots, and their availability. 
Additionally, the functions should include the ability to check spot availability, park vehicles, and retrieve parking details.

Write a class ParkingLot that represents the parking lot management system. The class should include the following methods:

add_level(level_number, num_regular_spots, num_reserved_spots): Adds a new parking level with the specified level number, 
number of regular spots, and number of reserved spots.

park_vehicle(vehicle_number, is_reserved): Parks a vehicle with the specified vehicle number in an available spot.
      If the vehicle is reserved, it should be parked in a reserved spot if available; otherwise, it should be parked in a regular spot.

unpark_vehicle(vehicle_number): Unparks the vehicle with the specified vehicle number from the parking lot.

get_parking_details(): Returns the current parking details, including the occupied and available spots on each level.

You can assume that vehicle numbers are unique within the parking lot.
Implement the ParkingLot class with the above methods, along with any additional helper methods or data structures you may need.

Note: You do not need to handle edge cases such as input validation or error handling in this implementation."""

class ParkingLot:
    def __init__(self):
        self.levels = {}

    def add_level(self, level_number, num_regular_spots, num_reserved_spots):
        self.levels[level_number] = {
            "regular_spots": [False] * num_regular_spots,
            "reserved_spots": [False] * num_reserved_spots
        }

    def park_vehicle(self, vehicle_number, is_reserved):
        for level_number, level in self.levels.items():
            if is_reserved:
                spots = level["reserved_spots"]
            else:
                spots = level["regular_spots"]

            for i in range(len(spots)):
                if not spots[i]:
                    spots[i] = vehicle_number
                    return level_number, i, is_reserved

        return None, None, None

    def unpark_vehicle(self, vehicle_number):
        for level in self.levels.values():
            for spots in [level["regular_spots"], level["reserved_spots"]]:
                for i in range(len(spots)):
                    if spots[i] == vehicle_number:
                        spots[i] = False
                        return

    def get_parking_details(self):
        details = {}
        for level_number, level in self.levels.items():
            details[level_number] = {
                "regular_spots": [i if i else "Available" for i in level["regular_spots"]],
                "reserved_spots": [i if i else "Available" for i in level["reserved_spots"]]
            }
        return details

# Example usage:
parking_lot = ParkingLot()

# Add parking levels
parking_lot.add_level(1, 10, 2)
parking_lot.add_level(2, 8, 3)

# Park vehicles
vehicle1_details = parking_lot.park_vehicle("ABC123", False)
vehicle2_details = parking_lot.park_vehicle("XYZ789", True)

# Get parking details
parking_details = parking_lot.get_parking_details()
print("Parking Details:")
for level_number, level_details in parking_details.items():
    print(f"Level {level_number}:")
    print("Regular Spots:", level_details["regular_spots"])
    print("Reserved Spots:", level_details["reserved_spots"])
    print()

# Unpark vehicle
parking_lot.unpark_vehicle("ABC123")

# Get updated parking details
parking_details = parking_lot.get_parking_details()
print("Updated Parking Details:")
for level_number, level_details in parking_details.items():
    print(f"Level {level_number}:")
    print("Regular Spots:", level_details["regular_spots"])
    print("Reserved Spots:", level_details["reserved_spots"])
    print()
