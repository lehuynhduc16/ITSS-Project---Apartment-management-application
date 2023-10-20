# apartment_id, building_id, apartment_number, size, rent
import random

for i in range(1, 101):
    building_id = random.randint(1, 100)
    apartment_number = random.randint(1, 100)
    size = random.randint(30, 100)
    rent = random.randint(1000, 5000)
    print("({}, {}, {}, {}, {}),".format(i, building_id, apartment_number, size, rent))

