# Turimas "users" masyvas. 

# Parašykite funkcijas, kurios atlikas nurodytas užduotis:
# 1. funkcija "getUserAverageAge" - kaip argumentą priims masyvą ir duoto masyvo 
# atveju grąžins visų "users" amžiaus visurkį kaip skaičių.
# 2. funkcija "getUsersNames" -  kaip argumentą priims masyvą ir duoto masyvo 
# atveju grąžins visų "users" vardus naujame list'e pvz., ['Alex John', 'Ann Smith'...].

# Pastaba: rezultatai turi būti išrikiuoti abėcėlės tvarka

users = [
  { "id": '1', "name": 'John Smith', "age": 20 },
  { "id": '2', "name": 'Ann Smith', "age": 24 },
  { "id": '3', "name": 'Tom Jones', "age": 31 },
  { "id": '4', "name": 'Rose Peterson', "age": 17 },
  { "id": '5', "name": 'Alex John', "age": 25 },
  { "id": '6', "name": 'Ronald Jones', "age": 63 },
  { "id": '7', "name": 'Elton Smith', "age": 16 },
  { "id": '8', "name": 'Simon Peterson', "age": 30 },
  { "id": '9', "name": 'Daniel Cane', "age": 51 },
]

# Kuriame funkciją 'getUserAverageAge' kuri iteruos paduotą masyvą kaip argumentą ir iš jo išrinks elementus kurių 'key' - age  ir 'value' poros 'value' reikšmės bus susumuotos ir padalintos iš elementų skaičiaus

def getUserAverageAge(arr):
  age = 0
  for i in arr:
    age = age + int((i['age']))
  print(f' Vidutinis amžius: {round(age / len(arr))} metai')
      
#Paledžiame funkciją 'getUserAverageAge' kuriai kaip argumentą paduodame 'users' masyvą
getUserAverageAge(users)  

# 2 užduoties dalies skirtukas
print('-------------------------------')

# Kuriame funkciją 'getUserNames' kuri iteruos paduotą masyvą kaip argumentą ir iš jo išrinks elementus kurių 'key' - name  ir 'value' poros 'value' reikšmės bus sudėtos surūšiuotai naujame masyve
vardai = []
def getUsersNames(arr):
  
  for i in arr:
    vardai.append(i['name'])
    vardai.sort()

#Paledžiame funkciją 'getUsersNames' kuriai kaip argumentą paduodame 'users' masyvą
getUsersNames(users)

#Išspausdiname naujai gautą masyvą 'vardai'
print(vardai)

