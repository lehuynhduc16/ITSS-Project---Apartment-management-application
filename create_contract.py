# contract_id, tenant_id, start_date, end_date, notes, payment_amount

import random

for i in range(1, 101):
    tenant_id = random.randint(1, 100)
    start_date = str(random.randint(2015, 2020)) + '-' + str(random.randint(1, 12)) + '-' + str(random.randint(1, 29))
    end_date = str(random.randint(2021, 2023)) + '-' + str(random.randint(1, 12)) + '-' + str(random.randint(1, 29))
    notes = ""
    payment_amount = random.randint(1000, 10000)
    print("({}, {}, '{}', '{}', '{}', {}),".format(i, tenant_id, start_date, end_date, notes, payment_amount))
