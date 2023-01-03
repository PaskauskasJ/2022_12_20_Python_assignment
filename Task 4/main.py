# Sukurkite klasę "Movie", kuri gebės sukurti objektus 3 savybėm ir 1 metodu. 
# Naudojant šią klasę sukurkite bent du skirtingus objektus.

# Savybės:
# title: string
# director: string
# budget: number

# Metodas: 
# wasExpensive() - jeigu filmo "budget" yra daugiau nei 100 000 000 mln USD, tada grąžins True, kitu atveju False. 


#Kuriame klasę 'Movie', kuri turi 3 savybes: title, director ir budget
class Movie():
    def __init__(self, title, director, budget):
        self.title = str(title)
        self.director = str(director)
        self.budget = int(budget)

    #Kuriames metodą 'wasExpensive' klasėje 'Movie', kuris grąžins True jei sąvybė budget bus didesnė už 100000000         
    def wasExpensive(self):
        if self.budget  >  100000000:
            print(f'"{self.title}" movie is expensive - {True}')
        else:
            print(f'"{self.title}" movie is expensive - {False}')
        
        
#Kuriame 1-ą objektą pagal klasę 'Movie'  
avatarasMovie = Movie('Avatar', 'James Cameron', 10000000000)

#Kuriame 2-ą objektą pagal klasę 'Movie'  
gentlemanMovie = Movie('The Gentleman', 'Guy Richie', 5000000)

#Iškviečiame 1-ą objektą pagal metodą 'wasExpensive' 
avatarasMovie.wasExpensive()
#Iškviečiame 1-ą objektą pagal metodą 'wasExpensive' 
gentlemanMovie.wasExpensive()