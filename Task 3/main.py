# Turimas "audi" dict.

# Parašykite funkciją "showObjectKeys", kuri kaip argumentą priims objektą 
# ir grąžins visus jo "values" list'e.

audi = {
  "make": 'audi',
  "model": 'A6',
  "year": 2005,
  "color": 'white',
}

# Kuriame funkciją 'showObjectKeys' kuri paims objektą kaip argumentą ir grąžins masyvą su objekto 'values'
def showObjectKeys(obj):
  return list(obj.values())
    
#Išspausdiname funkcijos rezultatą
print(showObjectKeys(audi))