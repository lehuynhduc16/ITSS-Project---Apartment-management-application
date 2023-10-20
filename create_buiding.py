# building_id, name, address, total_apartment

import random_address
import random

add_address = [random_address.real_random_address()['address1'] for i in range(100)]
names = ['Mckinnis', 'Gallegos', 'Parker', 'Toney', 'Mclarney', 'Myers', 'Oge', 'Beal', 'Carrillo', 'Macneil', 'Harian', 'Cardenas', 'Voss', 'Jordon', 'Robinson', 'Spires', 'Helmy', 'Majewski', 'Kelley', 'Martin', 'Yates', 'Dennis', 'Hall', 'Mincks', 'Gutierrez', 'Hill', 'Kasack', 'Roberts', 'Caplinger', 'Oswalt', 'Dorado', 'Tippin', 'Rice', 'Petersen', 'Richards', 'Serasio', 'Torpey', 'Magelssen', 'Garza', 'Rios', 'Sanchez', 'Raney', 'Howe', 'Ford', 'Bretz', 'Zeller', 'Baker', 'Householder', 'Schultz', 'Dickson', 'Pavia', 'Clark', 'Bouleris', 'Rothrock', 'Juelfs', 'Cawthorne', 'Hernandez', 'Rutledge', 'Fornili', 'Heath', 'Posadas', 'Kresge', 'Soto', 'Jackson', 'Edwards', 'Shephard', 'Liff', 'Caskey', 'Born', 'Anderson', 'Miller', 'Kachermeyer', 'Jusino', 'Merkle', 'Elliott', 'Alonso', 'Louie', 'Estes', 'Karle', 'Lucas', 'Hammonds', 'Braaten', 'Debartolo', 'Medina', 'Diaz', 'Jones', 'Benoit', 'Ruiz', 'Roberson', 'Hammond', 'Painter', 'Bartos', 'Eckard', 'Shuffler', 'Mcneil', 'Brendan', 'Jonathan', 'Nancy', 'Sandra', 'Beverly']

for i in range(100):
    print('(' + str(i+1) + ', \'' + names[i] + ' Building\', \'' + add_address[i] + '\', ' + str(random.randint(1, 20)) + '),')


