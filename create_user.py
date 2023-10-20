# user_idd, usernamed, passwordd, roled
import random

for i in range(1, 101):
    usernamed = "user" + str(i)
    passwordd = "password" + str(i)
    roled = "Tenant"
    print("({}, '{}', '{}', '{}'),".format(i, usernamed, passwordd, roled))
