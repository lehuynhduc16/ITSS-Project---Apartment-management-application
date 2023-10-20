# payment_id, contract_id, payment_date, amount

import random

for i in range(1, 101):
    contract_id = random.randint(1, 100)
    payment_date = str(random.randint(2024, 2025)) + '-' + str(random.randint(1, 12)) + '-' + str(random.randint(1, 29))
    amount = random.randint(1000, 10000)
    print("({}, {}, '{}', {}),".format(i, contract_id, payment_date, amount))
