# Sukurkite klasę "Movie", kuri gebės sukurti objektus 3 savybėm ir 1 metodu. 
# Naudojant šią klasę sukurkite bent du skirtingus objektus.

# Savybės:
# title: string
# director: string
# budget: number

# Metodas: 
# wasExpensive() - jeigu filmo "budget" yra daugiau nei 100 000 000 mln USD, tada grąžins True, kitu atveju False. 

class Movie():
    def __init__(self, title, director, budget):
        self.title = str(title)
        self.director = str(director)
        self.budget = int(budget)
        
    def wasExpensive(self):
        if self.budget  >  100000000:
            print(True)
        else:
            print(False)
        
        
        
avatarasMovie = Movie('Avatar', 'James Cameron', 10000000000)
gentlemanMovie = Movie('The Gentleman', 'Guy Richie', 5000000)

avatarasMovie.wasExpensive()
gentlemanMovie.wasExpensive()