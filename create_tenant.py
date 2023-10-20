# tenant_id, apartment_id, name, contact, status
import random
import names

for i in range(1, 101):
    apartment_id = random.randint(1, 100)
    name = names.get_full_name()
    contact = random.randint(100000000, 999999999)
    status = random.choice(["ACTIVE", "INACTIVE"])
    print("({}, {}, '{}', '{}', '{}'),".format(i, apartment_id, name, contact, status))
