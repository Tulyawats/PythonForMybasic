#HW python class 5
# Dictionary practice
# How to insert, del, edit data in dictionary

#insert data to dictionary
info = {}
#input 3 data to dictionary
info['apple'] = 25
info["grape"] = 40
info["avocado"] = 50
print(info)

#Edit data in dictionary
info['apple'] = 30
info['grape'] = 100
info['avocado'] = 80
print(info)

#Delete data in dictionary
del info['apple']

print(info)

#loop data in dictionary

for fruit, price in info.items() :
    print(f'fruit : {fruit} \nprice : {price} \n')

print('--------------------------------end---------------------------------------------------')