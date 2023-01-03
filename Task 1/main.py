# Turimas "users" masyvas. 

# Parašykite funkcijas, kurios atlikas nurodytas užduotis:
# 1. funkcija "filterDogOwers" - kaip argumentą priims masyvą ir duoto masyvo 
# atveju grąžins "users", kurie turi augintinį.
# 2. funkcija "filterAdults" - kaip argumentą priims masyvą ir duoto masyvo 
# atveju grąžins masyvą su "users", kurie yra pilnamečiai.

users = [
  { "id": '1', "name": 'John Smith', "age": 20, "hasDog": True },
  { "id": '2', "name": 'Ann Smith', "age": 24, "hasDog": False },
  { "id": '3', "name": 'Tom Jones', "age": 31, "hasDog": True },
  { "id": '4', "name": 'Rose Peterson', "age": 17, "hasDog": False },
  { "id": '5', "name": 'Alex John', "age": 25, "hasDog": True },
  { "id": '6', "name": 'Ronald Jones', "age": 63, "hasDog": True },
  { "id": '7', "name": 'Elton Smith', "age": 16, "hasDog": True },
  { "id": '8', "name": 'Simon Peterson', "age": 30, "hasDog": False },
  { "id": '9', "name": 'Daniel Cane', "age": 51, "hasDog": True },
]

# Kuriame funkciją 'filterDogOwners' kuri iteruos paduotą masyvą kaip argumentą ir iš jo išrinks elementus kurių 'key' ir 'value' pora bus lygi 'hasDog': True

def filterDogOwers(arr):
  for i in arr:
    if i['hasDog'] == True:
      print(f'Šie users turi augintinį: {list(i.items())}')
      
  

#Paledžiame funkciją 'filterDogOwers' kuriai kaip argumentą paduodame 'users' masyvą
filterDogOwers(users)  

# 2 užduoties dalies skirtukas
print('-------------------------------')


# Kuriame funkciją 'filterAdults' kuri iteruos paduotą masyvą kaip argumentą ir iš jo išrinks elementus kurių 'key' ir 'value' poros 'value' vertė bus didesnė už 18 

def filterAdults(arr):
  for i in arr:
    if i['age'] >= 18:
      print(f'Šie Users yra pilnamečiai: {dict(i.items())}')
  
#Paledžiame funkciją 'filterAdults' kuriai kaip argumentą paduodame 'users' masyvą

filterAdults(users)  