# Importuokite reikiamus modulius, kad veiktų žemiau nurodytos funkcijos

#Importuojame modulius taip, kad veiktų žemiau esančios funkcijos. Tam kad main.py faile kodas būtų nepakeistas, kur reikia kintamieji ar funkcijų pavadinimai interpretuojami kitais vardais su "as"  

from modules.numbers.numbers import *
from modules.math.composition import composition as addition
from modules.math.division import division as divivsion
from modules.math.multiplication import *
from modules.math.subtraction import *


# Kitų failų ir žemiau esančio kodo nekeiskite
a = addition(one, four);
b = divivsion(four, two);
c = substraction(three, two);
d = multiplication(five, two);

print(a);
print(b);
print(c);
print(d);
